---
title: isMultiThreaded()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/ismultithreaded()
source_url: 'https://developer.apple.com/documentation/foundation/thread/ismultithreaded()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/ismultithreaded%28%29.json'
content_hash: 'sha256:05107c021d996374'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# isMultiThreaded()

<sub>Type Method</sub>

Returns whether the application is multithreaded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func isMultiThreaded() -> Bool
```

## Return Value

[true](../../swift/true.md) if the application is multithreaded, otherwise [false](../../swift/false.md).

## Discussion

An application is considered multithreaded if a thread was ever detached from the main thread using either [+ detachNewThreadSelector:toTarget:withObject:](<detachnewthreadselector(__totarget_with_).md>) or [- start](<start().md>). If you detached a thread in your application using a non-Cocoa API, such as the POSIX or Multiprocessing Services APIs, this method could still return [false](../../swift/false.md). The detached thread does not have to be currently running for the application to be considered multithreaded—this method only indicates whether a single thread has been spawned.

## See Also

### Querying the Environment

- [currentThread](current.md) — Returns the thread object representing the current thread of execution.
- [callStackReturnAddresses](callstackreturnaddresses.md) — Returns an array containing the call stack return addresses.
- [callStackSymbols](callstacksymbols.md) — Returns an array containing the call stack symbols.
