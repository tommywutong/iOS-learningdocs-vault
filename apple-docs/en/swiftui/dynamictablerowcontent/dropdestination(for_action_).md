---
title: 'dropDestination(for:action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dynamictablerowcontent/dropdestination(for:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dynamictablerowcontent/dropdestination(for:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dynamictablerowcontent/dropdestination%28for%3Aaction%3A%29.json'
content_hash: 'sha256:d8b0728bd2519e66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DynamicTableRowContent](../dynamictablerowcontent.md)

# dropDestination(for:action:)

<sub>Instance Method</sub>

Sets the insert action for the dynamic table rows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func dropDestination<T>(for payloadType: T.Type = T.self, action: @escaping (Int, [T]) -> Void) -> ModifiedContent<Self, OnInsertTableRowModifier> where T : Transferable
```

## Parameters

- `payloadType` — Type of the models that are dropped.

- `action` — A closure that SwiftUI invokes when elements are added to the collection of rows. The closure takes two arguments: The first argument is the offset relative to the dynamic view’s underlying collection of data. The second argument is an array of `Transferable` items that represents the data that you want to insert.

## Return Value

A view that calls `action` when elements are inserted into the original view.

## Discussion

```swift
struct Profile: Identifiable {
    let givenName: String
    let familyName: String
    let id = UUID()
}

@State private var profiles: [Profile] = [
    Person(givenName: "Juan", familyName: "Chavez"),
    Person(givenName: "Mei", familyName: "Chen"),
    Person(givenName: "Tom", familyName: "Clark"),
    Person(givenName: "Gita", familyName: "Kumar")
]

var body: some View {
    Table {
        TableColumn("Given Name", value: \.givenName)
        TableColumn("Family Name", value: \.familyName)
    } rows: {
        ForEach(profiles) {
            TableRow($0)
        }
        .dropDestination(
            for: Profile.self
        ) { offset, receivedProfiles in
            people.insert(contentsOf: receivedProfiles, at: offset)
        }
    }
}
```
