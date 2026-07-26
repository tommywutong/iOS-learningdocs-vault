---
title: 'capsule(maximumRadius:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicornerconfiguration-swift.struct/capsule(maximumradius:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicornerconfiguration-swift.struct/capsule(maximumradius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicornerconfiguration-swift.struct/capsule%28maximumradius%3A%29.json'
content_hash: 'sha256:af3c720657510e5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICornerConfiguration](../uicornerconfiguration-swift.struct.md)

# capsule(maximumRadius:)

<sub>Type Method</sub>

A configuration that rounds the corners into a capsule shape, scaling with the view’s size up to the maximum radius you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func capsule(maximumRadius: Double? = nil) -> UICornerConfiguration
```

## Parameters

- `maximumRadius` — A double value that represents the maximum radius to apply to corners for this configuration.
