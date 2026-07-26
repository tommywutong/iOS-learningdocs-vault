---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/verticalalignment/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/verticalalignment/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/verticalalignment/init%28_%3A%29.json'
content_hash: 'sha256:f18dad87f9b7c0af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VerticalAlignment](../verticalalignment.md)

# init(_:)

<sub>Initializer</sub>

Creates a custom vertical alignment of the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ id: any AlignmentID.Type)
```

## Parameters

- `id` — The type of an identifier that uniquely identifies a vertical alignment.

## Discussion

Use this initializer to create a custom vertical alignment. Define an [AlignmentID](../alignmentid.md) type, and then use that type to create a new static property on [VerticalAlignment](../verticalalignment.md):

```swift
private struct FirstThirdAlignment: AlignmentID {
    static func defaultValue(in context: ViewDimensions) -> CGFloat {
        context.height / 3
    }
}

extension VerticalAlignment {
    static let firstThird = VerticalAlignment(FirstThirdAlignment.self)
}
```

Every vertical alignment instance that you create needs a unique identifier. For more information, see [AlignmentID](../alignmentid.md).

## See Also

### Creating a custom alignment

- [combineExplicit(_:)](<combineexplicit(__).md>) — Merges a sequence of explicit alignment values produced by this instance.
