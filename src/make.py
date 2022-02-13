import json
import re

def vizToMspa(story_name, viz_num):
    # Somehow this is actually correct
    ret = viz_num

    # assert int(viz_num) not in [
    #     992,
    #     4299,
    #     4938,
    #     4988,
    #     9802,
    #     9803,
    #     9804
    # ]

    if story_name == "problem-sleuth":
        ret = int(viz_num) + 218
    elif story_name == "story":
        ret = int(viz_num) + 1900

    print(story_name, viz_num, ret, sep="\t")
    return ret


with open("commentary.json", "r", encoding="utf-8") as fp:
    commentary = json.load(fp)

andrew_footnotes = {
    "author": "Andrew Hussie",
    "story": {}
}
archivist_notes = {
    "author": "Homestuck Companion",
    "story": {}
}

for record in commentary:
    story_name = record['name']
    for page in record['data']:
        try:
            pageid = (vizToMspa(story_name, page['id']))
            pageid = f"{int(pageid):06}"

            if pc := page.get("commentary"):
                andrew_footnotes['story'][pageid] = [{"content": pc}]

            if mn := page.get("notes"):
                if match := re.match(r'([A-Za-z]+[A-Za-z ][A-Za-z]+): (.+)', mn):
                    author, content = match.groups()
                    archivist_notes['story'][pageid] = [{
                        "author": author,
                        "content": content
                    }]
                else:
                    archivist_notes['story'][pageid] = [{"content": mn}]
        except:
            print(page)
            raise

footnoteCollection = [
    andrew_footnotes,
    archivist_notes
]

with open("footnotes.js", "w", encoding="utf-8") as fp:
    fp.write("\nstory_archivist = ")
    fp.write(json.dumps(archivist_notes['story'], ensure_ascii=False, indent=2))
    fp.write("story_author = ")
    fp.write(json.dumps(andrew_footnotes['story'], ensure_ascii=False, indent=2))
