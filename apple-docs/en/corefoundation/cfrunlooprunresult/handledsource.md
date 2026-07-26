---
title: CFRunLoopRunResult.handledSource
framework: Core Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunlooprunresult/handledsource
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult/handledsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunlooprunresult/handledsource.json'
content_hash: 'sha256:da02125a7112e79d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFRunLoopRunResult](../cfrunlooprunresult.md)

# CFRunLoopRunResult.handledSource

<sub>Case</sub>

A source has been processed. This value is returned only if the run loop was told to run only until a source was processed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case handledSource
```

## See Also

### Constants

- [kCFRunLoopRunFinished](finished.md) — The running run loop mode has no sources or timers to process.
- [kCFRunLoopRunStopped](stopped.md) — [CFRunLoopStop](<../cfrunloopstop(__).md>) was called on the run loop.
- [kCFRunLoopRunTimedOut](timedout.md) — The specified time interval for running the run loop has passed.
