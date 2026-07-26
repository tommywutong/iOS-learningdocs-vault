---
title: 'uncached(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uideferredmenuelement/uncached(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uideferredmenuelement/uncached(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uideferredmenuelement/uncached%28_%3A%29.json'
content_hash: 'sha256:7d96ba0963860f1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDeferredMenuElement](../uideferredmenuelement.md)

# uncached(_:)

<sub>Type Method</sub>

Returns a placeholder menu element that the system replaces with the result of the provider’s completion handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func uncached(_ elementProvider: @escaping (@escaping ([UIMenuElement]) -> Void) -> Void) -> Self
```

## Parameters

- `elementProvider` — The closure the system calls to request the deferred menu items.

## Discussion

When you use this initializer, the system calls each deferred element’s completion closure every time it encounters the element in a menu. The system doesn’t cache the element for reuse.

## See Also

### Creating a deferred menu element

- [+ elementWithProvider:](<init(__).md>) — A convenience initializer that creates a placeholder menu element that the system replaces with the result of the provider’s completion handler.
- [+ elementUsingFocusWithIdentifier:shouldCacheItems:](<usingfocus(identifier_shouldcacheitems_).md>)
