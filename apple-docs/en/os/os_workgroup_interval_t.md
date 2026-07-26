---
title: os_workgroup_interval_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_interval_t
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_interval_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_interval_t.json'
content_hash: 'sha256:045bbf26d101799a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_workgroup_interval_t

<sub>Type Alias</sub>

A workgroup object that supports the scheduling of threads on a repeating cadence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef OS_os_workgroup<OS_os_workgroup_interval> * os_workgroup_interval_t;
```

## Discussion

Use the `os_workgroup_interval_create` function to create a new interval workgroup for your app. Use the workgroup that method returns to configure the group’s attributes, and to start, update, and stop the interval work. You can also create a reference to a workgroup using the [os_workgroup_create_with_workgroup](os_workgroup_create_with_workgroup.md) function.

## See Also

### Interval Tasks

- [os_workgroup_interval_start](os_workgroup_interval_start.md) — Starts the regular execution of the workgroup’s threads at the specified time.
- [os_workgroup_interval_update](os_workgroup_interval_update.md) — Schedules a new deadline for workgroup threads that run at regular intervals.
- [os_workgroup_interval_finish](os_workgroup_interval_finish.md) — Stops the current interval-based execution of the workgroup’s threads.
- [os_workgroup_interval_data_t](os_workgroup_interval_data_t.md) — An opaque structure that contains additional configuration data for the interval workgroup.
- [os_clockid_t](os_clockid_t.md) — Options for how to specify time-specific values in an interval workgroup.
