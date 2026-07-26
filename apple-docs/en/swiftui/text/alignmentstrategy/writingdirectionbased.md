---
title: writingDirectionBased
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/alignmentstrategy/writingdirectionbased
source_url: 'https://developer.apple.com/documentation/swiftui/text/alignmentstrategy/writingdirectionbased'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/alignmentstrategy/writingdirectionbased.json'
content_hash: 'sha256:009a9959e91a9276'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Text](../../text.md) · [AlignmentStrategy](../alignmentstrategy.md)

# writingDirectionBased

<sub>Type Property</sub>

The alignment following the writing direction of the same paragraph.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let writingDirectionBased: Text.AlignmentStrategy
```

## Discussion

When [multilineTextAlignment](../../environmentvalues/multilinetextalignment.md) is [TextAlignment.leading](../../textalignment/leading.md), alignment follows the writing direction. If the value is [TextAlignment.trailing](../../textalignment/trailing.md) alignment is the opposite of the writing direction and finally, a [TextAlignment.center](../../textalignment/center.md) value always results in centered alignment.
