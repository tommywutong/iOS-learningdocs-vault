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
doc_path: '/documentation/foundation/netservice/schedule(in:formode:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservice/schedule(in:formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/schedule%28in%3Aformode%3A%29.json'
content_hash: 'sha256:6c053fdf8c89a036'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# schedule(in:forMode:)

<sub>Instance Method</sub>

Adds the service to the specified run loop.

> [!warning] Deprecated
> Use nw_connection_t or nw_listener_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func schedule(in aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

## Parameters

- `aRunLoop` — The run loop to which to add the receiver.

- `mode` — The run loop mode to which to add the receiver. Possible values for `mode` are discussed in the “Constants” section of [RunLoop](../runloop.md).

## Discussion

You can use this method in conjunction with [- removeFromRunLoop:forMode:](<remove(from_formode_).md>) to transfer a service to a different run loop. You should not attempt to run a service on multiple run loops.

## See Also

### Managing Run Loops

- [- removeFromRunLoop:forMode:](<remove(from_formode_).md>) — Removes the service from the given run loop for a given mode. _(deprecated)_
