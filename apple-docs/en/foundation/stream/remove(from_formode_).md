---
title: 'remove(from:forMode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/stream/remove(from:formode:)'
source_url: 'https://developer.apple.com/documentation/foundation/stream/remove(from:formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/remove%28from%3Aformode%3A%29.json'
content_hash: 'sha256:25d6ef922410d454'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Stream](../stream.md)

# remove(from:forMode:)

<sub>Instance Method</sub>

Removes the receiver from a given run loop running in a given mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remove(from aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

## Parameters

- `aRunLoop` — The run loop on which the receiver was scheduled.

- `mode` — The mode for the run loop.

## See Also

### Managing Run Loops

- [- scheduleInRunLoop:forMode:](<schedule(in_formode_).md>) — Schedules the receiver on a given run loop in a given mode.
