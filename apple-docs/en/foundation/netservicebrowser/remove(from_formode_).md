---
title: 'remove(from:forMode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/netservicebrowser/remove(from:formode:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservicebrowser/remove(from:formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicebrowser/remove%28from%3Aformode%3A%29.json'
content_hash: 'sha256:70c7aeb586ee7b7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceBrowser](../netservicebrowser.md)

# remove(from:forMode:)

<sub>Instance Method</sub>

Removes the receiver from the specified run loop.

> [!warning] Deprecated
> Use nw_browser_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func remove(from aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

## Parameters

- `aRunLoop` — Run loop from which to remove the receiver.

- `mode` — Run loop mode in which to perform this operation, such as [NSDefaultRunLoopMode](../runloop/mode/default.md). See the Run Loop Modes section of the [RunLoop](../runloop.md) class for other run loop mode values.

## Discussion

You can use this method in conjunction with [- scheduleInRunLoop:forMode:](<schedule(in_formode_).md>) to transfer the receiver to a run loop other than the default one. Although it is possible to remove an `NSNetService` object completely from any run loop and then attempt actions on it, you must not do it.

## See Also

### Managing Run Loops

- [- scheduleInRunLoop:forMode:](<schedule(in_formode_).md>) — Adds the receiver to the specified run loop. _(deprecated)_
