---
title: 'remove(_:forMode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/runloop/remove(_:formode:)'
source_url: 'https://developer.apple.com/documentation/foundation/runloop/remove(_:formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/remove%28_%3Aformode%3A%29.json'
content_hash: 'sha256:a0effc6ced456dbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# remove(_:forMode:)

<sub>Instance Method</sub>

Removes a port from the specified input mode of the run loop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remove(_ aPort: Port, forMode mode: RunLoop.Mode)
```

## Parameters

- `aPort` — The port to remove from the receiver.

- `mode` — The mode from which to remove `aPort`. You may specify a custom mode or use one of the modes listed in `Run Loop Modes`.

## Discussion

If you added the port to multiple input modes, you must remove it from each mode separately.

## See Also

### Managing Ports

- [- addPort:forMode:](<add(__formode_)-6z982.md>) — Adds a port as an input source to the specified mode of the run loop.
