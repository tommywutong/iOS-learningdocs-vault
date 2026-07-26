---
title: 'init(_:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uideferredmenuelement/init(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uideferredmenuelement/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uideferredmenuelement/init%28_%3A%29.json'
content_hash: 'sha256:d47b0ecfa8454c4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDeferredMenuElement](../uideferredmenuelement.md)

# init(_:)

<sub>Initializer</sub>

A convenience initializer that creates a placeholder menu element that the system replaces with the result of the provider’s completion handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(_ elementProvider: @escaping (@escaping ([UIMenuElement]) -> Void) -> Void)
```

## Parameters

- `elementProvider` — The closure the system calls to request the deferred menu items.

## Discussion

The system calls each element’s closure once, when it first encounters the element in a menu. Once provided, the system caches the element and may reuse it across menus.

You can use [+ elementWithUncachedProvider:](<uncached(__).md>) to initialize a deferred menu element without caching. With caching disabled, the system calls the provider closure each time it displays the element.

## See Also

### Creating a deferred menu element

- [+ elementWithUncachedProvider:](<uncached(__).md>) — Returns a placeholder menu element that the system replaces with the result of the provider’s completion handler.
- [+ elementUsingFocusWithIdentifier:shouldCacheItems:](<usingfocus(identifier_shouldcacheitems_).md>)
