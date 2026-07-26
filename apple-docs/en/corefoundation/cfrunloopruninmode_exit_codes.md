---
title: CFRunLoopRunInMode Exit Codes
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopruninmode_exit_codes
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopruninmode_exit_codes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopruninmode_exit_codes.json'
content_hash: 'sha256:230ddb1f9a41bac4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFRunLoop](cfrunloop.md)

# CFRunLoopRunInMode Exit Codes

<sub>API Collection</sub>

Return codes for `CFRunLoopRunInMode`, identifying the reason the run loop exited.

## Topics

### Constants

- [kCFRunLoopRunFinished](cfrunlooprunresult/finished.md) — The running run loop mode has no sources or timers to process.
- [kCFRunLoopRunStopped](cfrunlooprunresult/stopped.md) — [CFRunLoopStop](<cfrunloopstop(__).md>) was called on the run loop.
- [kCFRunLoopRunTimedOut](cfrunlooprunresult/timedout.md) — The specified time interval for running the run loop has passed.
- [kCFRunLoopRunHandledSource](cfrunlooprunresult/handledsource.md) — A source has been processed. This value is returned only if the run loop was told to run only until a source was processed.

## See Also

### Constants

- [Common Mode Flag](common-mode-flag.md) — A run loop pseudo-mode that manages objects monitored in the “common” modes.
- [Default Run Loop Mode](default-run-loop-mode.md) — Default run loop mode.
