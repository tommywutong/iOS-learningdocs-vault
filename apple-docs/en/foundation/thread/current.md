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
doc_path: /documentation/foundation/thread/current
source_url: 'https://developer.apple.com/documentation/foundation/thread/current'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/current.json'
content_hash: 'sha256:ad1490670f397081'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# current

<sub>Type Property</sub>

Returns the thread object representing the current thread of execution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var current: Thread { get }
```

## Return Value

A thread object representing the current thread of execution.

## See Also

### Related Documentation

- [+ detachNewThreadSelector:toTarget:withObject:](<detachnewthreadselector(__totarget_with_).md>) — Detaches a new thread and uses the specified selector as the thread entry point.

### Querying the Environment

- [+ isMultiThreaded](<ismultithreaded().md>) — Returns whether the application is multithreaded.
- [callStackReturnAddresses](callstackreturnaddresses.md) — Returns an array containing the call stack return addresses.
- [callStackSymbols](callstacksymbols.md) — Returns an array containing the call stack symbols.
