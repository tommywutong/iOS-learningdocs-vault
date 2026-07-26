---
title: 'provider(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/provider(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/provider(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/provider%28for%3A%29.json'
content_hash: 'sha256:73d8fdea63578b5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# provider(for:)

<sub>Instance Method</sub>

Asks the responder for an element provider to fulfill the given focus-based deferred element. Check the `identifier` of the deferred element to identify which deferred element this is. By default, this returns nil. Return a non-nil `provider` to make this responder responsible for providing elements for this fulfillment of the deferred element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func provider(for deferredElement: UIDeferredMenuElement) -> UIDeferredMenuElement.Provider?
```
