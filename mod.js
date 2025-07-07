module.exports = {
  title: "Homestuck Commentary",
  summary: "Adds Andrew Hussie's author commentary from the Homestuck/Problem Sleuth books and some additional notes by fans.",
  description: "Adds Andrew Hussie's author commentary from the Problem Sleuth and Homestuck (1-6) books, as well as some additional notes by fans. Credits to Bambosh for the original OCR, Makin for proof of concept and original Homestuck Companion browser extension, Drew Linky for book page to webcomic page conversion, and GiovanH for modding API implementation. More information and Github repo available at https://homestuck.net/collection.html. This mod is open source and licensed under the GPLv3.",

  author: "GiovanH, /r/homestuck",
  version: 0.2,

  footnotes: true,

  async asyncComputed(api) {
    store = api.store

    // Store defaults
    store.set("show_author", store.get("show_author", true))
    store.set("show_notes", store.get("show_notes", true))

    // Compute footnotes object
    let notes = []
    if (store.get("show_author")) {
      notes.push({
        "author": store.get("hidename") ? "" : "Andrew Hussie",
        "story": await api.readJsonAsync('./authornotes.json')
      })
    }

    if (store.get("show_notes")) {
      notes.push({
        "author": "Homestuck Companion",
        "story": await api.readJsonAsync('./archivist.json')
      })
    }

    return {
      footnotes: notes
    }
  },

  settings: {
    boolean: [{
      model: "show_author",
      label: "Include author commentary",
    }, {
      model: "show_notes",
      label: "Include archivist commentary",
    }, {
      model: "hidename",
      label: "Hide Name",
      desc: "Don't show \"Andrew Hussie\" name on commentary footnotes"
    }]
  }
}
