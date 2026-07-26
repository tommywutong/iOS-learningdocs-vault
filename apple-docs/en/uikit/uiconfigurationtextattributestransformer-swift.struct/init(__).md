---
title: 'init(_:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiconfigurationtextattributestransformer-swift.struct/init(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationtextattributestransformer-swift.struct/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationtextattributestransformer-swift.struct/init%28_%3A%29.json'
content_hash: 'sha256:87839a7c5a3e7da8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIConfigurationTextAttributesTransformer](../uiconfigurationtextattributestransformer-swift.struct.md)

# init(_:)

<sub>Initializer</sub>

Creates a new text attributes transformer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(_ transform: @escaping (AttributeContainer) -> AttributeContainer)
```

## Parameters

- `transform` — A closure that defines the text transformation.
