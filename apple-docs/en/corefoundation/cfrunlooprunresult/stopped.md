---
title: CFRunLoopRunResult.stopped
framework: Core Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunlooprunresult/stopped
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult/stopped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunlooprunresult/stopped.json'
content_hash: 'sha256:ec3771d55a50b459'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFRunLoopRunResult](../cfrunlooprunresult.md)

# CFRunLoopRunResult.stopped

<sub>Case</sub>

[CFRunLoopStop](<../cfrunloopstop(__).md>) was called on the run loop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case stopped
```

## See Also

### Constants

- [kCFRunLoopRunFinished](finished.md) — The running run loop mode has no sources or timers to process.
- [kCFRunLoopRunTimedOut](timedout.md) — The specified time interval for running the run loop has passed.
- [kCFRunLoopRunHandledSource](handledsource.md) — A source has been processed. This value is returned only if the run loop was told to run only until a source was processed.
