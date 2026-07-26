---
title: RunLoop.SchedulerOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/scheduleroptions
source_url: 'https://developer.apple.com/documentation/foundation/runloop/scheduleroptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/scheduleroptions.json'
content_hash: 'sha256:207cbce730ed5e91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# RunLoop.SchedulerOptions

<sub>Structure</sub>

A set of options that affect the operation of the run loop scheduler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SchedulerOptions
```

## Overview

The run loop doesn’t support any scheduler options.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## See Also

### Scheduling Combine Publishers

- [schedule(options:_:)](<schedule(options___).md>) — Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [schedule(after:tolerance:options:_:)](<schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date, using the specified tolerance and options.
- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, using the specified tolerance and options.
- [minimumTolerance](minimumtolerance.md) — The minimum tolerance the run loop scheduler allows.
- [now](now.md) — The run loop scheduler’s definition of the current moment in time.
- [SchedulerTimeType](schedulertimetype.md) — The scheduler time type that the run loop uses.
