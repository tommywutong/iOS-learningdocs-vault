---
title: os_clockid_t
framework: os
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_clockid_t
source_url: 'https://developer.apple.com/documentation/os/os_clockid_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_clockid_t.json'
content_hash: 'sha256:6df80fd4219efa90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_clockid_t

<sub>Enumeration</sub>

Options for how to specify time-specific values in an interval workgroup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef enum { ... } os_clockid_t;
```

## Topics

### Clock Options

- [OS_CLOCK_MACH_ABSOLUTE_TIME](os_clockid_t/os_clock_mach_absolute_time.md) — Units relative to Mach absolute time value.

## See Also

### Interval Tasks

- [os_workgroup_interval_start](os_workgroup_interval_start.md) — Starts the regular execution of the workgroup’s threads at the specified time.
- [os_workgroup_interval_update](os_workgroup_interval_update.md) — Schedules a new deadline for workgroup threads that run at regular intervals.
- [os_workgroup_interval_finish](os_workgroup_interval_finish.md) — Stops the current interval-based execution of the workgroup’s threads.
- [os_workgroup_interval_t](os_workgroup_interval_t.md) — A workgroup object that supports the scheduling of threads on a repeating cadence.
- [os_workgroup_interval_data_t](os_workgroup_interval_data_t.md) — An opaque structure that contains additional configuration data for the interval workgroup.
