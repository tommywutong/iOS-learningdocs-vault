---
title: Scheduler Implementations
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/operationqueue/scheduler-implementations
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/scheduler-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/scheduler-implementations.json'
content_hash: 'sha256:83796bd8d3b88c34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Processes and Threads](../processes-and-threads.md) · [OperationQueue](../operationqueue.md)

# Scheduler Implementations

<sub>API Collection</sub>

## Topics

### Structures

- [SchedulerOptions](scheduleroptions.md) — A type that defines options the operation queue accepts.
- [SchedulerTimeType](schedulertimetype.md) — The scheduler time type the operation queue uses.

### Instance Properties

- [minimumTolerance](minimumtolerance.md) — The minimum tolerance the dispatch queue scheduler allows.
- [now](now.md) — The operation queue’s definition of the current moment in time.

### Instance Methods

- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [schedule(after:tolerance:options:_:)](<schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date, optionally taking into account tolerance if possible.
- [schedule(options:_:)](<schedule(options___).md>) — Performs the action at the next possible opportunity.
