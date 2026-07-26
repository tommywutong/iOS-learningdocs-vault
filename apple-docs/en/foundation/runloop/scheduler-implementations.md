---
title: Scheduler Implementations
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/scheduler-implementations
source_url: 'https://developer.apple.com/documentation/foundation/runloop/scheduler-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/scheduler-implementations.json'
content_hash: 'sha256:edb24d77eb35ceaf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Processes and Threads](../processes-and-threads.md) · [RunLoop](../runloop.md)

# Scheduler Implementations

<sub>API Collection</sub>

## Topics

### Structures

- [SchedulerOptions](scheduleroptions.md) — A set of options that affect the operation of the run loop scheduler.
- [SchedulerTimeType](schedulertimetype.md) — The scheduler time type that the run loop uses.

### Instance Properties

- [minimumTolerance](minimumtolerance.md) — The minimum tolerance the run loop scheduler allows.
- [now](now.md) — The run loop scheduler’s definition of the current moment in time.

### Instance Methods

- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, using the specified tolerance and options.
- [schedule(after:tolerance:options:_:)](<schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date, using the specified tolerance and options.
- [schedule(options:_:)](<schedule(options___).md>) — Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
