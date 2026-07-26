---
title: 'add(_:forMode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/runloop/add(_:formode:)-6z982'
source_url: 'https://developer.apple.com/documentation/foundation/runloop/add(_:formode:)-6z982'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/add%28_%3Aformode%3A%29-6z982.json'
content_hash: 'sha256:aa1faffecf908d38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# add(_:forMode:)

<sub>Instance Method</sub>

Adds a port as an input source to the specified mode of the run loop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func add(_ aPort: Port, forMode mode: RunLoop.Mode)
```

## Parameters

- `aPort` — The port to add to the receiver.

- `mode` — The mode in which to add `aPort`. You may specify a custom mode or use one of the modes listed in `Run Loop Modes`.

## Discussion

This method schedules the port with the receiver. You can add a port to multiple input modes. When the receiver is running in the specified mode, it dispatches messages destined for that port to the port’s designated handler routine.

## See Also

### Managing Ports

- [- removePort:forMode:](<remove(__formode_).md>) — Removes a port from the specified input mode of the run loop.
