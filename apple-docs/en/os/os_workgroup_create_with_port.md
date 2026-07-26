---
title: os_workgroup_create_with_port
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 11.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_create_with_port
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_create_with_port'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_create_with_port.json'
content_hash: 'sha256:097c064cda05d4f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_workgroup_create_with_port

<sub>Function</sub>

Creates a new workgroup that is bound to the workgroup with the specified Mach port.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern os_workgroup_tos_workgroup_create_with_port(const char *name, mach_port_t mach_port);
```

## Parameters

- `name` — An optional name for the workgroup. Use this name to identify the workgroups you create. You may specify `NULL` for this parameter.

- `mach_port` — A port that represents the send right for a kernel workgroup object. Typically, you obtain this port from another process, which creates it using the [os_workgroup_copy_port](os_workgroup_copy_port.md) function. This function doesn’t consume a reference to the port’s send right.

## Return Value

An immutable workgroup object that refers to the workgroup with the specified port.

## Discussion

Use this function to join threads of your app to a workgroup in a different process. A process may export its workgroup’s Mach port to coordinate any work it’s doing with similar work happening in other processes. For example, the system’s audio APIs export workgroups that allow other processes to provide audio data on the same schedule as the system. Use this function to construct a local workgroup from the provided port information.

The workgroup this function returns is a reference to the workgroup with the specified port. You can add threads to the newly created workgroup, but you cannot change the configuration or scheduling details of the original group. For example, you cannot start, stop, or update the deadlines for an interval workgroup, and those functions return errors if you try to do so. Instead, the process that owns the original workgroup handles all configuration and scheduling details.

This function sets the name of the new workgroup to the value in the `name` property. It then configures the new workgroup as a reference to the workgroup in the `wg` parameter. The newly created workgroup doesn’t contain any threads initially, and it doesn’t contain any context data.

## See Also

### Common Utilities

- [os_workgroup_create_with_workgroup](os_workgroup_create_with_workgroup.md) — Create a new workgroup that is bound to the specified workgroup.
- [os_workgroup_copy_port](os_workgroup_copy_port.md) — Returns the Mach port associated with the workgroup.
- [os_workgroup_t](os_workgroup_t.md) — An opaque object representing a default workgroup in the current process.
- [os_workgroup_attr_t](os_workgroup_attr_t.md) — An opaque structure for storing workgroup-related attributes.
