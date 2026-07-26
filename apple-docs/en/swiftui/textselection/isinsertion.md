---
title: isInsertion
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textselection/isinsertion
source_url: 'https://developer.apple.com/documentation/swiftui/textselection/isinsertion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textselection/isinsertion.json'
content_hash: 'sha256:34bdd545873c3422'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextSelection](../textselection.md)

# isInsertion

<sub>Instance Property</sub>

Return `true` if the selection is an insertion point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isInsertion: Bool { get }
```

## Discussion

An insertion point effectively represents a range that contains no characters, indicating a location in the string. This location refers to the point in the text where new characters will be inserted. In other words, it represents cases when the start and end index are equal.
