---
title: destructive
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/buttonrole/destructive
source_url: 'https://developer.apple.com/documentation/swiftui/buttonrole/destructive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/buttonrole/destructive.json'
content_hash: 'sha256:3e69346436e9ae50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ButtonRole](../buttonrole.md)

# destructive

<sub>Type Property</sub>

A role that indicates a destructive button.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let destructive: ButtonRole
```

## Discussion

Use this role for a button that deletes user data, or performs an irreversible operation. A destructive button signals by its appearance that the user should carefully consider whether to tap or click the button. For example, SwiftUI presents a destructive button that you add with the [swipeActions(edge:allowsFullSwipe:content:)](<../view/swipeactions(edge_allowsfullswipe_content_).md>) modifier using a red background:

```swift
List {
    ForEach(items) { item in
        Text(item.title)
            .swipeActions {
                Button(role: .destructive) { delete() } label: {
                    Label("Delete", systemImage: "trash")
                }
            }
    }
}
.navigationTitle("Shopping List")
```

![A screenshot of a list of three items, where the second item is](../../../../attachments/2209f1ece4e578c31a5d2523b4ed010c/ButtonRole-destructive-1@2x.png)

## See Also

### Getting button roles

- [cancel](cancel.md) — A role that indicates a button that cancels an operation.
