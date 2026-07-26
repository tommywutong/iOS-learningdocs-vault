---
title: 'schedule(in:forMode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/port/schedule(in:formode:)'
source_url: 'https://developer.apple.com/documentation/foundation/port/schedule(in:formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/port/schedule%28in%3Aformode%3A%29.json'
content_hash: 'sha256:e90661f49361b06b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Port](../port.md)

# schedule(in:forMode:)

<sub>Instance Method</sub>

This method should be implemented by a subclass to set up monitoring of a port when added to a given run loop in a given input mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func schedule(in runLoop: RunLoop, forMode mode: RunLoop.Mode)
```

## Parameters

- `runLoop` — The run loop to which to add the receiver.

- `mode` — The run loop mode to which to add the receiver

## Discussion

This method should not be called directly.

## See Also

### Port monitoring

- [- removeFromRunLoop:forMode:](<remove(from_formode_).md>) — This method should be implemented by a subclass to stop monitoring of a port when removed from a give run loop in a given input mode.
