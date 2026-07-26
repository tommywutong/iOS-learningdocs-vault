---
title: CFRunLoopRunResult.timedOut
framework: Core Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunlooprunresult/timedout
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult/timedout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunlooprunresult/timedout.json'
content_hash: 'sha256:458738734d221975'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFRunLoopRunResult](../cfrunlooprunresult.md)

# CFRunLoopRunResult.timedOut

<sub>Case</sub>

The specified time interval for running the run loop has passed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case timedOut
```

## See Also

### Constants

- [kCFRunLoopRunFinished](finished.md) — The running run loop mode has no sources or timers to process.
- [kCFRunLoopRunStopped](stopped.md) — [CFRunLoopStop](<../cfrunloopstop(__).md>) was called on the run loop.
- [kCFRunLoopRunHandledSource](handledsource.md) — A source has been processed. This value is returned only if the run loop was told to run only until a source was processed.
