---
title: 'CFRunLoopContainsSource(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopcontainssource(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopcontainssource(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopcontainssource%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f0944e96bfd49e6a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopContainsSource(_:_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopSource object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopContainsSource(_ rl: CFRunLoop!, _ source: CFRunLoopSource!, _ mode: CFRunLoopMode!) -> Bool
```

## Parameters

- `rl` — The run loop to examine.

- `source` — The run loop source for which to search.

- `mode` — The run loop mode of `rl` in which to search. Use the constant [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) to search for `source` in the set of objects monitored by all the common modes.

## Return Value

`true` if `source` is in mode `mode` of the run loop `rl`, otherwise `false`.

## Discussion

If `source` was added to [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md), this function returns `true` if `mode` is either [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) or any of the modes that has been added to the set of common modes.

## See Also

### Managing Sources

- [CFRunLoopAddSource](<cfrunloopaddsource(______).md>) — Adds a CFRunLoopSource object to a run loop mode.
- [CFRunLoopRemoveSource](<cfrunloopremovesource(______).md>) — Removes a CFRunLoopSource object from a run loop mode.
