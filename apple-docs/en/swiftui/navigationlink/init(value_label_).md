---
title: 'init(value:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/navigationlink/init(value:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationlink/init(value:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationlink/init%28value%3Alabel%3A%29.json'
content_hash: 'sha256:4ac9d9e34dc348e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationLink](../navigationlink.md)

# init(value:label:)

<sub>Initializer</sub>

Creates a navigation link that presents the view corresponding to a codable value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<P>(value: P?, @ContentBuilder label: () -> Label) where P : Decodable, P : Encodable, P : Hashable
```

## Parameters

- `value` — An optional value to present. When the user selects the link, SwiftUI stores a copy of the value. Pass a `nil` value to disable the link.

- `label` — A label that describes the view that this link presents.

## Discussion

When someone activates the navigation link that this initializer creates, SwiftUI looks for a nearby [navigationDestination(for:destination:)](<../view/navigationdestination(for_destination_).md>) view modifier with a `data` input parameter that matches the type of this initializer’s `value` input, with one of the following outcomes:

- If SwiftUI finds a matching modifier within the view hierarchy of an enclosing [NavigationStack](../navigationstack.md), it pushes the modifier’s corresponding `destination` view onto the stack.
- If SwiftUI finds a matching modifier in the view hierarchy of a stack that’s in a later column of a [NavigationSplitView](../navigationsplitview.md), it puts the modifier’s destination view as the first and only item onto the stack while preserving the stack’s root view.
- If there’s no matching modifier, but the link appears in a [List](../list.md) with selection inside a leading column of a navigation split view, the link updates the selection, which might affect the appearance of a trailing view. For an example of this, see [NavigationLink](../navigationlink.md).
- In other cases, the link doesn’t do anything.

Because this initializer takes a value that conforms to the [Codable](../../swift/codable.md) protocol, you ensure that a [NavigationPath](../navigationpath.md) that includes this link can produce a non-`nil` value for its [codable](../navigationpath/codable.md) property. This helps to make the path serializable.

## See Also

### Presenting a value

- [init(_:value:)](<init(__value_).md>) — Creates a navigation link that presents the view corresponding to a codable value, with a text label that the link generates from a localized string resource.
