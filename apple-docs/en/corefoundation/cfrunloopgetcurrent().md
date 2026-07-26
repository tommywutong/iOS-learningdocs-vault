---
title: CFRunLoopGetCurrent()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopgetcurrent()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopgetcurrent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopgetcurrent%28%29.json'
content_hash: 'sha256:23076472849907ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopGetCurrent()

<sub>Function</sub>

Returns the CFRunLoop object for the current thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopGetCurrent() -> CFRunLoop!
```

## Return Value

Current thread’s run loop. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

Each thread has exactly one run loop associated with it.

## See Also

### Related Documentation

- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091)

### Getting a Run Loop

- [CFRunLoopGetMain](<cfrunloopgetmain().md>) — Returns the main CFRunLoop object.
