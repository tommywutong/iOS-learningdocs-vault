---
title: current
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsassertionhandler/current
source_url: 'https://developer.apple.com/documentation/foundation/nsassertionhandler/current'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsassertionhandler/current.json'
content_hash: 'sha256:e55e104f74bf41d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAssertionHandler](../nsassertionhandler.md)

# current

<sub>Type Property</sub>

Returns the `NSAssertionHandler` object associated with the current thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var current: NSAssertionHandler { get }
```

## Return Value

The `NSAssertionHandler` object associated with the current thread.

## Discussion

If no assertion handler is associated with the current thread, this method creates one and assigns it to the thread.
