---
title: 'subscript(dynamicMember:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/attributedtextformatting/attributecontainerproxy/subscript(dynamicmember:)'
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformatting/attributecontainerproxy/subscript(dynamicmember:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformatting/attributecontainerproxy/subscript%28dynamicmember%3A%29.json'
content_hash: 'sha256:c76489db22140a4b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [AttributedTextFormatting](../../attributedtextformatting.md) · [AttributeContainerProxy](../attributecontainerproxy.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Access the value of the attribute to constrain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(dynamicMember keyPath: KeyPath<AttributeDynamicLookup, Attribute>) -> Attribute.Value? { get set }
```

## Overview

For details on how attribute value constraining works, refer to [constrain(_:)](<../../attributedtextvalueconstraint/constrain(__).md>).
