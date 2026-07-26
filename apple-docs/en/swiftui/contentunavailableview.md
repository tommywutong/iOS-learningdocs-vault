---
title: ContentUnavailableView
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contentunavailableview
source_url: 'https://developer.apple.com/documentation/swiftui/contentunavailableview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentunavailableview.json'
content_hash: 'sha256:9aa0ee9bf2e9a375'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ContentUnavailableView

<sub>Structure</sub>

An interface, consisting of a label and additional content, that you display when the content of your app is unavailable to users.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct ContentUnavailableView<Label, Description, Actions> where Label : View, Description : View, Actions : View
```

## Overview

It is recommended to use `ContentUnavailableView` in situations where a view’s content cannot be displayed. That could be caused by a network error, a list without items, a search that returns no results etc.

You create an `ContentUnavailableView` in its simplest form, by providing a label and some additional content such as a description or a call to action:

```swift
ContentUnavailableView {
    Label("No Mail", systemImage: "tray.fill")
} description: {
    Text("New mails you receive will appear here.")
}
```

The system provides default `ContentUnavailableView`s that you can use in specific situations. The example below illustrates the usage of the [search](contentunavailableview/search.md) view:

```swift
struct ContentView: View {
    @ObservedObject private var viewModel = ContactsViewModel()

    var body: some View {
        NavigationStack {
            List {
                ForEach(viewModel.searchResults) { contact in
                    NavigationLink {
                        ContactsView(contact)
                    } label: {
                        Text(contact.name)
                    }
                }
            }
            .navigationTitle("Contacts")
            .searchable(text: $viewModel.searchText)
            .overlay {
                if searchResults.isEmpty {
                    ContentUnavailableView.search
                }
            }
        }
    }
}
```

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Getting built-in unavailable views

- [search](contentunavailableview/search.md) — Creates a `ContentUnavailableView` instance that conveys a search state.
- [search(text:)](<contentunavailableview/search(text_).md>) — Creates a `ContentUnavailableView` instance that conveys a search state.

### Creating an unavailable view

- [init(label:description:actions:)](<contentunavailableview/init(label_description_actions_).md>) — Creates an interface, consisting of a label and additional content, that you display when the content of your app is unavailable to users.
- [init(_:image:description:)](<contentunavailableview/init(__image_description_).md>) — Creates an interface, consisting of a title generated from a localized string resource, an image and additional content, that you display when the content of your app is unavailable to users.
- [init(_:systemImage:description:)](<contentunavailableview/init(__systemimage_description_).md>) — Creates an interface, consisting of a title generated from a localized string resource, a system icon image and additional content, that you display when the content of your app is unavailable to users.

### Supporting types

- [SearchUnavailableContent](searchunavailablecontent.md) — A structure that represents the body of a static placeholder search view.
