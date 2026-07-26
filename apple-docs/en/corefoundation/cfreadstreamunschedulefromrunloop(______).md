---
title: 'CFReadStreamUnscheduleFromRunLoop(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfreadstreamunschedulefromrunloop(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfreadstreamunschedulefromrunloop(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfreadstreamunschedulefromrunloop%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:65ed555654af4986'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFReadStreamUnscheduleFromRunLoop(_:_:_:)

<sub>Function</sub>

Removes a read stream from a given run loop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFReadStreamUnscheduleFromRunLoop(_ stream: CFReadStream!, _ runLoop: CFRunLoop!, _ runLoopMode: CFRunLoopMode!)
```

## Parameters

- `stream` — The stream to unschedule.

- `runLoop` — The run loop from which to remove `stream`.

- `runLoopMode` — The run loop mode of `runLoop` from which to remove `stream`.

## See Also

### Scheduling a Read Stream

- [CFReadStreamScheduleWithRunLoop](<cfreadstreamschedulewithrunloop(______).md>) — Schedules a stream into a run loop.
