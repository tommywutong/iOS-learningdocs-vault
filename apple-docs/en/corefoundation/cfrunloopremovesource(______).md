---
title: 'CFRunLoopRemoveSource(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopremovesource(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopremovesource(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopremovesource%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:aa1c279cc58805d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopRemoveSource(_:_:_:)

<sub>Function</sub>

Removes a CFRunLoopSource object from a run loop mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopRemoveSource(_ rl: CFRunLoop!, _ source: CFRunLoopSource!, _ mode: CFRunLoopMode!)
```

## Parameters

- `rl` — The run loop to modify.

- `source` — The run loop source to remove.

- `mode` — The run loop mode of `rl` from which to remove `source`. Use the constant [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) to remove `source` from the set of objects monitored by all the common modes.

## Discussion

If `source` is a version 0 source, this function calls the `cancel` callback function specified in the context structure for `source`. See [CFRunLoopSourceContext](cfrunloopsourcecontext.md) and [CFRunLoopSourceContext1](cfrunloopsourcecontext1.md)for more details.

If `rl` does not contain `source` in `mode`, this function does nothing.

## See Also

### Managing Sources

- [CFRunLoopAddSource](<cfrunloopaddsource(______).md>) — Adds a CFRunLoopSource object to a run loop mode.
- [CFRunLoopContainsSource](<cfrunloopcontainssource(______).md>) — Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopSource object.
