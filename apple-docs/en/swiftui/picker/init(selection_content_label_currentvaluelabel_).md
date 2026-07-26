---
title: 'init(selection:content:label:currentValueLabel:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/picker/init(selection:content:label:currentvaluelabel:)'
source_url: 'https://developer.apple.com/documentation/swiftui/picker/init(selection:content:label:currentvaluelabel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/picker/init%28selection%3Acontent%3Alabel%3Acurrentvaluelabel%3A%29.json'
content_hash: 'sha256:0a65fff05a509f49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Picker](../picker.md)

# init(selection:content:label:currentValueLabel:)

<sub>Initializer</sub>

Creates a picker that displays a custom label and a custom value label where applicable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label, @ContentBuilder currentValueLabel: () -> some View)
```

## Parameters

- `selection` — A binding to a property that determines the currently-selected option.

- `content` — A view that contains the set of options.

- `label` — A view that describes the purpose of selecting an option.

- `currentValueLabel` — A view that represents the current value of the picker.

## Discussion

The following example shows a picker with a current value label that only displays the title of the currently selected song:

```swift
struct Song: Identifiable, Hashable {
    let id = UUID()
    let title: String
    let artist: String
    let genre: String
}

private let songs: [Song] = [ /* songs */]

@State private var selectedSong: Song? = nil

var body: some View {
    NavigationStack {
        List {
            Picker(selection: $selectedSong) {
                ForEach(songs) { song in
                    VStack(alignment: .leading) {
                        Text(song.title)
                            .bold()
                        Text(song.artist)
                        Text(song.genre)
                            .foregroundColor(.secondary)
                            .font(.caption)
                    }
                    .tag(song as Song?)
                }
            } label: {
                Text("Request a song")
            } currentValueLabel: {
                Text(selectedSong?.title ?? "No selection")
            }
        }
        .pickerStyle(.navigationLink)
    }
}
```
