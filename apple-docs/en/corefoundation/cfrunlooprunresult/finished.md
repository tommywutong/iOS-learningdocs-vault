---
title: CFRunLoopRunResult.finished
framework: Core Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunlooprunresult/finished
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult/finished'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunlooprunresult/finished.json'
content_hash: 'sha256:ac35778bdfea7a7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFRunLoopRunResult](../cfrunlooprunresult.md)

# CFRunLoopRunResult.finished

<sub>Case</sub>

The running run loop mode has no sources or timers to process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case finished
```

## See Also

### Constants

- [kCFRunLoopRunStopped](stopped.md) — [CFRunLoopStop](<../cfrunloopstop(__).md>) was called on the run loop.
- [kCFRunLoopRunTimedOut](timedout.md) — The specified time interval for running the run loop has passed.
- [kCFRunLoopRunHandledSource](handledsource.md) — A source has been processed. This value is returned only if the run loop was told to run only until a source was processed.
