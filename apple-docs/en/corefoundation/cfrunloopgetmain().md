---
title: CFRunLoopGetMain()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopgetmain()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopgetmain()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopgetmain%28%29.json'
content_hash: 'sha256:8f05ba33c830eaaa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopGetMain()

<sub>Function</sub>

Returns the main CFRunLoop object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopGetMain() -> CFRunLoop!
```

## Return Value

The main run loop. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Getting a Run Loop

- [CFRunLoopGetCurrent](<cfrunloopgetcurrent().md>) — Returns the CFRunLoop object for the current thread.
