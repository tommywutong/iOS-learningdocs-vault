---
title: callStackSymbols
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/callstacksymbols
source_url: 'https://developer.apple.com/documentation/foundation/thread/callstacksymbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/callstacksymbols.json'
content_hash: 'sha256:eafc35efb2341fef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# callStackSymbols

<sub>Type Property</sub>

Returns an array containing the call stack symbols.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var callStackSymbols: [String] { get }
```

## Return Value

An array containing the call stack symbols. Each element is an `NSString` object with a value in a format determined by the `backtrace_symbols()` function. For more information, see backtrace_symbols(3) macOS Developer Tools Manual Page.

## Discussion

The return value describes the call stack backtrace of the current thread at the moment this method was called.

## See Also

### Querying the Environment

- [+ isMultiThreaded](<ismultithreaded().md>) — Returns whether the application is multithreaded.
- [currentThread](current.md) — Returns the thread object representing the current thread of execution.
- [callStackReturnAddresses](callstackreturnaddresses.md) — Returns an array containing the call stack return addresses.
