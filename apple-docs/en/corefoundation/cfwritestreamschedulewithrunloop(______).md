---
title: 'CFWriteStreamScheduleWithRunLoop(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfwritestreamschedulewithrunloop(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfwritestreamschedulewithrunloop(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfwritestreamschedulewithrunloop%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8f5115e46ffb39d4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFWriteStreamScheduleWithRunLoop(_:_:_:)

<sub>Function</sub>

Schedules a stream into a run loop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFWriteStreamScheduleWithRunLoop(_ stream: CFWriteStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFRunLoopMode!)
```

## Parameters

- `stream` — The stream to schedule.

- `runLoop` — The run loop in which to schedule `stream`.

- `runLoopMode` — The run loop mode of `runLoop` in which to schedule `stream`.

## Discussion

After scheduling `stream` into a run loop, its client (set with [CFWriteStreamSetClient](<cfwritestreamsetclient(________).md>)) is notified when various events happen with the stream, such as when it finishes opening, when it can accept new bytes, and when an error occurs. A stream can be scheduled into multiple run loops and run loop modes. Use [CFWriteStreamUnscheduleFromRunLoop](<cfwritestreamunschedulefromrunloop(______).md>) to later remove `stream` from the run loop.

## See Also

### Scheduling a Write Stream

- [CFWriteStreamUnscheduleFromRunLoop](<cfwritestreamunschedulefromrunloop(______).md>) — Removes a stream from a particular run loop.
