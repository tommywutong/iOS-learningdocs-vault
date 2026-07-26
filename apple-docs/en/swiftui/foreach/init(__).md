---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/foreach/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/foreach/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/foreach/init%28_%3A%29.json'
content_hash: 'sha256:9b9c711d0a8f7587'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ForEach](../foreach.md)

# init(_:)

<sub>Initializer</sub>

Creates an instance that uniquely identifies and creates table rows across updates based on the identity of the underlying data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ data: Data) where ID == Data.Element.ID, Content == TableRow<Data.Element>, Data.Element : Identifiable
```

## Parameters

- `data` — The identified data that the [ForEach](../foreach.md) instance uses to create table rows dynamically.

## Discussion

The following example creates a `Person` type that conforms to [Identifiable](../../swift/identifiable.md), and an array of this type called `people`. A `ForEach` instance iterates over the array, producing new [TableRow](../tablerow.md) instances implicitly.

```swift
private struct Person: Identifiable {
    var id = UUID()
    var name: String
}

@State private var people: [Person] = /* ... */

Table(of: Person.self) {
    TableColumn("ID", value: \.id.uuidString)
    TableColumn("Name", value: \.name)
} rows: {
    Section("Team") {
        /* This is equivalent to the line below:
        ForEach(people) { TableRow($0) }
        */
        ForEach(people)
    }
}
```

## See Also

### Creating a collection

- [init(_:content:)](<init(__content_).md>) — Creates an instance that uniquely identifies and creates map content across updates based on the identity of the underlying data.
- [init(_:id:content:)](<init(__id_content_).md>) — Creates an instance that uniquely identifies and creates map content across updates based on the provided key path to the underlying data’s identifier.
- [init(sections:content:)](<init(sections_content_).md>) — Creates an instance that uniquely identifies and creates views across updates based on the sections of a given view.
- [init(subviews:content:)](<init(subviews_content_).md>) — Creates an instance that uniquely identifies and creates views across updates based on the subviews of a given view.
