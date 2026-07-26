---
title: ImmediateScheduler
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/immediatescheduler
source_url: 'https://developer.apple.com/documentation/combine/immediatescheduler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/immediatescheduler.json'
content_hash: 'sha256:ca7aeacb61c016d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# ImmediateScheduler

<sub>Structure</sub>

A scheduler for performing synchronous actions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ImmediateScheduler
```

## Overview

You can only use this scheduler for immediate actions. If you attempt to schedule actions after a specific date, this scheduler ignores the date and performs them immediately.

## Relationships

- **Conforms To**: [Scheduler](scheduler.md)

## Topics

### Declaring scheduler timekeeping and options

- [SchedulerTimeType](immediatescheduler/schedulertimetype.md) — The time type used by the immediate scheduler.
- [SchedulerOptions](immediatescheduler/scheduleroptions.md) — A type that defines options accepted by the immediate scheduler.

### Accessing scheduler time properties

- [minimumTolerance](immediatescheduler/minimumtolerance.md) — The minimum tolerance allowed by the immediate scheduler.
- [now](immediatescheduler/now.md) — The immediate scheduler’s definition of the current moment in time.

### Using the shared scheduler

- [shared](immediatescheduler/shared.md) — The shared instance of the immediate scheduler.

### Scheduling actions

- [schedule(after:interval:tolerance:options:_:)](<immediatescheduler/schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [schedule(after:tolerance:options:_:)](<immediatescheduler/schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date.
- [schedule(options:_:)](<immediatescheduler/schedule(options___).md>) — Performs the action at the next possible opportunity.

## See Also

### Schedulers

- [Scheduler](scheduler.md) — A protocol that defines when and how to execute a closure.
- [SchedulerTimeIntervalConvertible](schedulertimeintervalconvertible.md) — A protocol that provides a scheduler with an expression for relative time.
