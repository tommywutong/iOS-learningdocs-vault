---
title: documentRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextelementprovider/documentrange
source_url: 'https://developer.apple.com/documentation/uikit/nstextelementprovider/documentrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextelementprovider/documentrange.json'
content_hash: 'sha256:cb23d5a45e2fe6a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextElementProvider](../nstextelementprovider.md)

# documentRange

<sub>Instance Property</sub>

Describes the starting and ending locations for the document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var documentRange: NSTextRange { get }
```

## Discussion

The subclass could use its own implementation of a location object conforming to [NSTextRange](../nstextrange.md).
