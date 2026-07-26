---
title: 'unregisterClass(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocol/unregisterclass(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol/unregisterclass(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol/unregisterclass%28_%3A%29.json'
content_hash: 'sha256:f4de87823512d921'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocol](../urlprotocol.md)

# unregisterClass(_:)

<sub>Type Method</sub>

Unregisters the specified subclass of [URLProtocol](../urlprotocol.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func unregisterClass(_ protocolClass: AnyClass)
```

## Parameters

- `protocolClass` — The subclass of [URLProtocol](../urlprotocol.md) to unregister.

## Discussion

After this method is invoked, `protocolClass` is no longer consulted by the URL loading system.

## See Also

### Registering and unregistering protocol classes

- [+ registerClass:](<registerclass(__).md>) — Attempts to register a subclass of [URLProtocol](../urlprotocol.md), making it visible to the URL loading system.
