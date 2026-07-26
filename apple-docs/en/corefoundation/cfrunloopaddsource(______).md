---
title: 'CFRunLoopAddSource(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopaddsource(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopaddsource(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopaddsource%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:bbe1e79993010905'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopAddSource(_:_:_:)

<sub>Function</sub>

Adds a CFRunLoopSource object to a run loop mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopAddSource(_ rl: CFRunLoop!, _ source: CFRunLoopSource!, _ mode: CFRunLoopMode!)
```

## Parameters

- `rl` — The run loop to modify.

- `source` — The run loop source to add. The source is retained by the run loop.

- `mode` — The run loop mode to which to add `source`. Use the constant [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) to add `source` to the set of objects monitored by all the common modes.

## Discussion

If `source` is a version 0 source, this function calls the `schedule` callback function specified in the context structure for `source`. See [CFRunLoopSourceContext](cfrunloopsourcecontext.md) for more details.

A run loop source can be registered in multiple run loops and run loop modes at the same time. When the source is signaled, whichever run loop that happens to detect the signal first will fire the source.

If `rl` already contains `source` in `mode`, this function does nothing.

## See Also

### Managing Sources

- [CFRunLoopContainsSource](<cfrunloopcontainssource(______).md>) — Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopSource object.
- [CFRunLoopRemoveSource](<cfrunloopremovesource(______).md>) — Removes a CFRunLoopSource object from a run loop mode.
