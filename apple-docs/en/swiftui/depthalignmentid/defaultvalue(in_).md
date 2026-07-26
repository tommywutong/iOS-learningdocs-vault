---
title: 'defaultValue(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/depthalignmentid/defaultvalue(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/depthalignmentid/defaultvalue(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/depthalignmentid/defaultvalue%28in%3A%29.json'
content_hash: 'sha256:0124ec3f7ca2223b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DepthAlignmentID](../depthalignmentid.md)

# defaultValue(in:)

<sub>Type Method</sub>

Calculates a default value for the corresponding guide in the specified context.

<sub>visionOS</sub>

```swift
static func defaultValue(in context: ViewDimensions3D) -> CGFloat
```

## Parameters

- `context` — The context of the view that you apply the alignment guide to. The context gives you the view’s dimensions, as well as the values of other alignment guides that apply to the view, including both built-in and custom guides. You can use any of these values, if helpful, to calculate the value for your custom guide.

## Return Value

The offset of the guide from the origin in the view’s coordinate space.

## Discussion

Implement this method when you create a type that conforms to the [DepthAlignmentID](../depthalignmentid.md) protocol. Use the method to calculate the default offset of the corresponding alignment guide. SwiftUI interprets the value that you return as an offset in the coordinate space of the view that’s being laid out. For example, you can use the context to return a value that’s one-third of the height of the view:

```swift
private struct FirstThirdAlignment: DepthAlignmentID {
    static func defaultValue(in context: ViewDimensions3D) -> CGFloat {
        context.depth / 3
    }
}
```

You can override the default value that this method returns for a particular guide by adding the [alignmentGuide(_:computeValue:)](<../view/alignmentguide(__computevalue_).md>) view modifier to a particular view.
