---
title: 'CFWriteStreamUnscheduleFromRunLoop(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfwritestreamunschedulefromrunloop(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfwritestreamunschedulefromrunloop(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfwritestreamunschedulefromrunloop%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ed80a4dd0a3b8fc0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFWriteStreamUnscheduleFromRunLoop(_:_:_:)

<sub>Function</sub>

Removes a stream from a particular run loop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFWriteStreamUnscheduleFromRunLoop(_ stream: CFWriteStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFRunLoopMode!)
```

## Parameters

- `stream` — The stream to remove.

- `runLoop` — The run loop from which to remove `stream`.

- `runLoopMode` — The run loop mode of `runLoop` from which to remove `stream`.

## See Also

### Scheduling a Write Stream

- [CFWriteStreamScheduleWithRunLoop](<cfwritestreamschedulewithrunloop(______).md>) — Schedules a stream into a run loop.
