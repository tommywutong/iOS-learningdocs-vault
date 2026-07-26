---
title: 'CFRunLoopAddCommonMode(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopaddcommonmode(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopaddcommonmode(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopaddcommonmode%28_%3A_%3A%29.json'
content_hash: 'sha256:af461a5526c5a600'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopAddCommonMode(_:_:)

<sub>Function</sub>

Adds a mode to the set of run loop common modes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopAddCommonMode(_ rl: CFRunLoop!, _ mode: CFRunLoopMode!)
```

## Parameters

- `rl` — The run loop to modify. Each run loop has its own independent list of modes that are in the set of common modes.

- `mode` — The run loop mode to add to the set of common modes of `rl`.

## Discussion

Sources, timers, and observers get registered to one or more run loop modes and only run when the run loop is running in one of those modes. Common modes are a set of run loop modes for which you can define a set of sources, timers, and observers that are shared by these modes. Instead of registering a source, for example, to each specific run loop mode, you can register it once to the run loop’s common pseudo-mode and it will be automatically registered in each run loop mode in the common mode set. Likewise, when a mode is added to the set of common modes, any sources, timers, or observers already registered to the common pseudo-mode are added to the newly added common mode.

Once a mode is added to the set of common modes, it cannot be removed.

The Add, Contains, and Remove functions for sources, timers, and observers operate on a run loop’s set of common modes when you use the constant [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) for the run loop mode.

## See Also

### Managing Run Loop Modes

- [CFRunLoopCopyAllModes](<cfrunloopcopyallmodes(__).md>) — Returns an array that contains all the defined modes for a CFRunLoop object.
- [CFRunLoopCopyCurrentMode](<cfrunloopcopycurrentmode(__).md>) — Returns the name of the mode in which a given run loop is currently running.
