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
doc_path: '/documentation/foundation/stream/schedule(in:formode:)'
source_url: 'https://developer.apple.com/documentation/foundation/stream/schedule(in:formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/schedule%28in%3Aformode%3A%29.json'
content_hash: 'sha256:ce15628b86ec0a04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Stream](../stream.md)

# schedule(in:forMode:)

<sub>Instance Method</sub>

Schedules the receiver on a given run loop in a given mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func schedule(in aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

## Parameters

- `aRunLoop` — The run loop on which to schedule the receiver.

- `mode` — The mode for the run loop.

## Discussion

Unless the client is polling the stream, it is responsible for ensuring that the stream is scheduled on at least one run loop and that at least one of the run loops on which the stream is scheduled is being run.

## See Also

### Managing Run Loops

- [- removeFromRunLoop:forMode:](<remove(from_formode_).md>) — Removes the receiver from a given run loop running in a given mode.
