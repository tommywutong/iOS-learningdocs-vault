---
title: 'CFRunLoopCopyAllModes(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopcopyallmodes(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopcopyallmodes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopcopyallmodes%28_%3A%29.json'
content_hash: 'sha256:8c311a4780993b35'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopCopyAllModes(_:)

<sub>Function</sub>

Returns an array that contains all the defined modes for a CFRunLoop object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopCopyAllModes(_ rl: CFRunLoop!) -> CFArray!
```

## Parameters

- `rl` — The run loop to examine.

## Return Value

An array that contains all the run loop modes defined for `rl`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Managing Run Loop Modes

- [CFRunLoopAddCommonMode](<cfrunloopaddcommonmode(____).md>) — Adds a mode to the set of run loop common modes.
- [CFRunLoopCopyCurrentMode](<cfrunloopcopycurrentmode(__).md>) — Returns the name of the mode in which a given run loop is currently running.
