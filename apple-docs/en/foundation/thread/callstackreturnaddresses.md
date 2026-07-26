---
title: callStackReturnAddresses
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/callstackreturnaddresses
source_url: 'https://developer.apple.com/documentation/foundation/thread/callstackreturnaddresses'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/callstackreturnaddresses.json'
content_hash: 'sha256:2ca7e7b1910d1bc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# callStackReturnAddresses

<sub>Type Property</sub>

Returns an array containing the call stack return addresses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var callStackReturnAddresses: [NSNumber] { get }
```

## Return Value

An array containing the call stack return addresses. Each element is an `NSNumber` object containing an `NSUInteger` value.

## See Also

### Querying the Environment

- [+ isMultiThreaded](<ismultithreaded().md>) — Returns whether the application is multithreaded.
- [currentThread](current.md) — Returns the thread object representing the current thread of execution.
- [callStackSymbols](callstacksymbols.md) — Returns an array containing the call stack symbols.
