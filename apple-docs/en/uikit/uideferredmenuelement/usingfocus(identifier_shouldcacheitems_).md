---
title: 'usingFocus(identifier:shouldCacheItems:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uideferredmenuelement/usingfocus(identifier:shouldcacheitems:)'
source_url: 'https://developer.apple.com/documentation/uikit/uideferredmenuelement/usingfocus(identifier:shouldcacheitems:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uideferredmenuelement/usingfocus%28identifier%3Ashouldcacheitems%3A%29.json'
content_hash: 'sha256:6697a4c9d72c0fe5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDeferredMenuElement](../uideferredmenuelement.md)

# usingFocus(identifier:shouldCacheItems:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func usingFocus(identifier: UIDeferredMenuElement.Identifier, shouldCacheItems: Bool) -> Self
```

## Parameters

- `identifier` — An identifier for this deferred element that responders can check to determine which elements to provide.

- `shouldCacheItems` — Whether or not the deferred element caches items. Passing in @c YES causes this deferred element to ask the responder chain for elements only once, when the element is first encountered in a menu. Passing in @c NO asks the responder chain for elements every time the element is displayed.

## Discussion

Returns a placeholder menu element that is replaced with elements provided from the responder chain. A loading UI takes the place of the element in the menu until it is fulfilled. The element may be stored and re-used across menus.

## See Also

### Creating a deferred menu element

- [+ elementWithProvider:](<init(__).md>) — A convenience initializer that creates a placeholder menu element that the system replaces with the result of the provider’s completion handler.
- [+ elementWithUncachedProvider:](<uncached(__).md>) — Returns a placeholder menu element that the system replaces with the result of the provider’s completion handler.
