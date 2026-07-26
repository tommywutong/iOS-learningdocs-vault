---
title: 'remove(from:forMode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmachport/remove(from:formode:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmachport/remove(from:formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachport/remove%28from%3Aformode%3A%29.json'
content_hash: 'sha256:ea53c729d6af5150'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMachPort](../nsmachport.md)

# remove(from:forMode:)

<sub>Instance Method</sub>

Removes the receiver from the run loop mode `mode` of `runLoop`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remove(from runLoop: RunLoop, forMode mode: RunLoop.Mode)
```

## Parameters

- `runLoop` — The run loop from which to remove the receiver.

- `mode` — The run loop mode from which to remove the receiver.

## Discussion

When the receiver is removed, the run loop stops monitoring the Mach port for incoming messages.

## See Also

### Scheduling the Port on a Run Loop

- [- scheduleInRunLoop:forMode:](<schedule(in_formode_).md>) — Schedules the receiver into the run loop mode `mode` of `runLoop`.
