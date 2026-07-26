---
title: 'registerClass(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocol/registerclass(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol/registerclass(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol/registerclass%28_%3A%29.json'
content_hash: 'sha256:cd6bb77a5454f35b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocol](../urlprotocol.md)

# registerClass(_:)

<sub>Type Method</sub>

Attempts to register a subclass of [URLProtocol](../urlprotocol.md), making it visible to the URL loading system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func registerClass(_ protocolClass: AnyClass) -> Bool
```

## Parameters

- `protocolClass` — The subclass to register.

## Return Value

[true](../../swift/true.md) if the registration is successful, [false](../../swift/false.md) otherwise. The only failure condition is if `protocolClass` is not a subclass of [URLProtocol](../urlprotocol.md).

## Discussion

Register any custom [URLProtocol](../urlprotocol.md) subclasses prior to making URL requests. When the URL loading system begins to load a request, it tries to initialize each registered protocol class with the specified request. The first [URLProtocol](../urlprotocol.md) subclass to return [true](../../swift/true.md) when sent a [+ canInitWithRequest:](<caninit(with_)-76brg.md>) message is used to load the request. There is no guarantee that all registered protocol classes will be consulted.

Classes are consulted in the reverse order of their registration. A similar design governs the process to create the canonical form of a request with [+ canonicalRequestForRequest:](<canonicalrequest(for_).md>).

## See Also

### Registering and unregistering protocol classes

- [+ unregisterClass:](<unregisterclass(__).md>) — Unregisters the specified subclass of [URLProtocol](../urlprotocol.md).
