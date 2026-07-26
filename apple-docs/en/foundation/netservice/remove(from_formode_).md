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
doc_path: '/documentation/foundation/netservice/remove(from:formode:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservice/remove(from:formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/remove%28from%3Aformode%3A%29.json'
content_hash: 'sha256:e0ff53441d29977c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# remove(from:forMode:)

<sub>Instance Method</sub>

Removes the service from the given run loop for a given mode.

> [!warning] Deprecated
> Use nw_connection_t or nw_listener_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func remove(from aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

## Parameters

- `aRunLoop` — The run loop from which to remove the receiver.

- `mode` — The run loop mode from which to remove the receiver. Possible values for `mode` are discussed in the “Constants” section of [RunLoop](../runloop.md).

## Discussion

You can use this method in conjunction with [- scheduleInRunLoop:forMode:](<schedule(in_formode_).md>) to transfer the service to a different run loop. Although it is possible to remove an `NSNetService` object completely from any run loop and then attempt actions on it, it is an error to do so.

## See Also

### Managing Run Loops

- [- scheduleInRunLoop:forMode:](<schedule(in_formode_).md>) — Adds the service to the specified run loop. _(deprecated)_
