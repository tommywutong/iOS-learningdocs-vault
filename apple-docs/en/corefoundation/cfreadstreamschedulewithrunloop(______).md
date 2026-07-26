---
title: 'CFReadStreamScheduleWithRunLoop(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfreadstreamschedulewithrunloop(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfreadstreamschedulewithrunloop(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfreadstreamschedulewithrunloop%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:5d28145401dd7411'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFReadStreamScheduleWithRunLoop(_:_:_:)

<sub>Function</sub>

Schedules a stream into a run loop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFReadStreamScheduleWithRunLoop(_ stream: CFReadStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFRunLoopMode!)
```

## Parameters

- `stream` — The stream to schedule.

- `runLoop` — The run loop with which to schedule `stream`.

- `runLoopMode` — The run loop mode of `runLoop` in which to schedule `stream`.

## Discussion

After scheduling `stream` with a run loop, its client (set with [CFReadStreamSetClient](<cfreadstreamsetclient(________).md>)) is notified when various events happen with the stream, such as when it finishes opening, when it has bytes available, and when an error occurs. A stream can be scheduled with multiple run loops and run loop modes. Use [CFReadStreamUnscheduleFromRunLoop](<cfreadstreamunschedulefromrunloop(______).md>) to later remove `stream` from the run loop.

## See Also

### Scheduling a Read Stream

- [CFReadStreamUnscheduleFromRunLoop](<cfreadstreamunschedulefromrunloop(______).md>) — Removes a read stream from a given run loop.
