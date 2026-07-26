---
title: 'schedule(in:forMode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/netservicebrowser/schedule(in:formode:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservicebrowser/schedule(in:formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicebrowser/schedule%28in%3Aformode%3A%29.json'
content_hash: 'sha256:a4982c41ba18664f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceBrowser](../netservicebrowser.md)

# schedule(in:forMode:)

<sub>Instance Method</sub>

Adds the receiver to the specified run loop.

> [!warning] Deprecated
> Use nw_browser_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func schedule(in aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

## Parameters

- `aRunLoop` — Run loop in which to schedule the receiver.

- `mode` — Run loop mode in which to perform this operation, such as [NSDefaultRunLoopMode](../runloop/mode/default.md). See the Run Loop Modes section of the [RunLoop](../runloop.md) class for other run loop mode values.

## Discussion

You can use this method in conjunction with [- removeFromRunLoop:forMode:](<remove(from_formode_).md>) to transfer the receiver to a run loop other than the default one. You should not attempt to run the receiver on multiple run loops.

## See Also

### Managing Run Loops

- [- removeFromRunLoop:forMode:](<remove(from_formode_).md>) — Removes the receiver from the specified run loop. _(deprecated)_
