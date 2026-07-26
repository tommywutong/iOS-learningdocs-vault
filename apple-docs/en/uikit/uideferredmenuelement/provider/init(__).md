---
title: 'init(_:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uideferredmenuelement/provider/init(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uideferredmenuelement/provider/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uideferredmenuelement/provider/init%28_%3A%29.json'
content_hash: 'sha256:e3a00d73c48fb4cf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIDeferredMenuElement](../../uideferredmenuelement.md) · [Provider](../provider.md)

# init(_:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(_ elementProvider: @escaping (@escaping ([UIMenuElement]) -> Void) -> Void)
```

## Parameters

- `elementProvider` — An asynchronous element provider block. Call this block’s completion handler when the responder’s menu items are available.

## Discussion

Creates a deferred menu element provider with an asynchronous block.
