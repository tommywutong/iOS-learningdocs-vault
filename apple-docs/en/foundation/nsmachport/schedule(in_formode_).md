---
title: 'schedule(in:forMode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmachport/schedule(in:formode:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmachport/schedule(in:formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachport/schedule%28in%3Aformode%3A%29.json'
content_hash: 'sha256:23765a0a4111ca32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMachPort](../nsmachport.md)

# schedule(in:forMode:)

<sub>Instance Method</sub>

Schedules the receiver into the run loop mode `mode` of `runLoop`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func schedule(in runLoop: RunLoop, forMode mode: RunLoop.Mode)
```

## Parameters

- `runLoop` — The run loop to which to add the receiver.

- `mode` — The run loop mode in which to add the receiver.

## Discussion

When the receiver is scheduled, the run loop monitors the mach port for incoming messages and, when a message arrives, invokes the delegate method [- handleMachMessage:](<../nsmachportdelegate/handlemachmessage(__).md>).

## See Also

### Scheduling the Port on a Run Loop

- [- removeFromRunLoop:forMode:](<remove(from_formode_).md>) — Removes the receiver from the run loop mode `mode` of `runLoop`.
