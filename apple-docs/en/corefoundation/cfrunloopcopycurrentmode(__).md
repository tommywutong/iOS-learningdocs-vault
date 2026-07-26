---
title: 'CFRunLoopCopyCurrentMode(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopcopycurrentmode(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopcopycurrentmode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopcopycurrentmode%28_%3A%29.json'
content_hash: 'sha256:121091a1557cc6eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopCopyCurrentMode(_:)

<sub>Function</sub>

Returns the name of the mode in which a given run loop is currently running.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopCopyCurrentMode(_ rl: CFRunLoop!) -> CFRunLoopMode!
```

## Parameters

- `rl` — The run loop to examine.

## Return Value

The mode in which `rl` is currently running; `NULL` if `rl` is not running. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

When run on the current thread’s run loop, the returned value identifies the run loop mode that made the callout in which your code is currently executing.

## See Also

### Managing Run Loop Modes

- [CFRunLoopAddCommonMode](<cfrunloopaddcommonmode(____).md>) — Adds a mode to the set of run loop common modes.
- [CFRunLoopCopyAllModes](<cfrunloopcopyallmodes(__).md>) — Returns an array that contains all the defined modes for a CFRunLoop object.
