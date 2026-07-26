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
doc_path: '/documentation/swiftui/horizontalalignment/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/horizontalalignment/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/horizontalalignment/init%28_%3A%29.json'
content_hash: 'sha256:ecf21a068a737921'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HorizontalAlignment](../horizontalalignment.md)

# init(_:)

<sub>Initializer</sub>

Creates a custom horizontal alignment of the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ id: any AlignmentID.Type)
```

## Parameters

- `id` — The type of an identifier that uniquely identifies a horizontal alignment.

## Discussion

Use this initializer to create a custom horizontal alignment. Define an [AlignmentID](../alignmentid.md) type, and then use that type to create a new static property on [HorizontalAlignment](../horizontalalignment.md):

```swift
private struct OneQuarterAlignment: AlignmentID {
    static func defaultValue(in context: ViewDimensions) -> CGFloat {
        context.width / 4
    }
}

extension HorizontalAlignment {
    static let oneQuarter = HorizontalAlignment(OneQuarterAlignment.self)
}
```

Every horizontal alignment instance that you create needs a unique identifier. For more information, see [AlignmentID](../alignmentid.md).

## See Also

### Creating a custom alignment

- [combineExplicit(_:)](<combineexplicit(__).md>) — Merges a sequence of explicit alignment values produced by this instance.
