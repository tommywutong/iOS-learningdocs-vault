---
title: transform
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiconfigurationtextattributestransformer-swift.struct/transform
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationtextattributestransformer-swift.struct/transform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationtextattributestransformer-swift.struct/transform.json'
content_hash: 'sha256:823abfda64cb716e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIConfigurationTextAttributesTransformer](../uiconfigurationtextattributestransformer-swift.struct.md)

# transform

<sub>Instance Property</sub>

A closure that defines the text transformation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
let transform: (AttributeContainer) -> AttributeContainer
```

## Discussion

This closure accepts a container with the current text attributes and returns a container with the new text attributes.
