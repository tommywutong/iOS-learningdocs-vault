---
title: os_workgroup_interval_data_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_interval_data_t
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_interval_data_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_interval_data_t.json'
content_hash: 'sha256:9c2207b4365233fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_workgroup_interval_data_t

<sub>Type Alias</sub>

An opaque structure that contains additional configuration data for the interval workgroup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef struct os_workgroup_interval_data_opaque_s * os_workgroup_interval_data_t;
```

## See Also

### Interval Tasks

- [os_workgroup_interval_start](os_workgroup_interval_start.md) — Starts the regular execution of the workgroup’s threads at the specified time.
- [os_workgroup_interval_update](os_workgroup_interval_update.md) — Schedules a new deadline for workgroup threads that run at regular intervals.
- [os_workgroup_interval_finish](os_workgroup_interval_finish.md) — Stops the current interval-based execution of the workgroup’s threads.
- [os_workgroup_interval_t](os_workgroup_interval_t.md) — A workgroup object that supports the scheduling of threads on a repeating cadence.
- [os_clockid_t](os_clockid_t.md) — Options for how to specify time-specific values in an interval workgroup.
