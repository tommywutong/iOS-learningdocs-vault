---
title: 'dropDestination(for:action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dynamicviewcontent/dropdestination(for:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dynamicviewcontent/dropdestination(for:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dynamicviewcontent/dropdestination%28for%3Aaction%3A%29.json'
content_hash: 'sha256:7e717bd1213a6981'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DynamicViewContent](../dynamicviewcontent.md)

# dropDestination(for:action:)

<sub>Instance Method</sub>

Sets the insert action for the dynamic view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func dropDestination<T>(for payloadType: T.Type = T.self, action: @escaping ([T], Int) -> Void) -> some DynamicViewContent where T : Transferable

```

## Parameters

- `payloadType` — Type of the models that are dropped.

- `action` — A closure that SwiftUI invokes when elements are added to the view. The closure takes two arguments: The first argument is the offset relative to the dynamic view’s underlying collection of data. The second argument is an array of `Transferable` items that represents the data that you want to insert.

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
    List {
        ForEach(profiles) { profile in
            Text(profile.givenName)
        }
        .dropDestination(for: Profile.self) { receivedProfiles, offset in
            profiles.insert(contentsOf: receivedProfiles, at: offset)
        }
    }
}
```

## See Also

### Responding to updates

- [onDelete(perform:)](<ondelete(perform_).md>) — Sets the deletion action for the dynamic view. You must delete the corresponding item within `action`, as it will be called after the row has already been removed from the [List](../list.md).
- [onInsert(of:perform:)](<oninsert(of_perform_).md>) — Sets the insert action for the dynamic view.
- [onMove(perform:)](<onmove(perform_).md>) — Sets the move action for the dynamic view.
