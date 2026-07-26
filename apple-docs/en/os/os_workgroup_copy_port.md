---
title: os_workgroup_copy_port
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 11.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_copy_port
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_copy_port'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_copy_port.json'
content_hash: 'sha256:c5b0664290aeac8a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_workgroup_copy_port

<sub>Function</sub>

Returns the Mach port associated with the workgroup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int os_workgroup_copy_port(os_workgroup_t wg, mach_port_t *mach_port_out);
```

## Parameters

- `wg` — The workgroup whose Mach port you want.

- `mach_port_out` — A pointer to a Mach port variable. When the function returns, this parameter contains the specified workgroup’s Mach port reference.

## Return Value

A value of `0` on success, or a nonzero error code if an error occurred.

## Discussion

This function returns the send right for the workgroup’s Mach port in the kernel. Pass this port to other processes and use it to construct a reference to the same workgroup in those processes, which lets those processes coordinate their threads with the threads of the workgroup in the `wg` parameter.

## See Also

### Common Utilities

- [os_workgroup_create_with_workgroup](os_workgroup_create_with_workgroup.md) — Create a new workgroup that is bound to the specified workgroup.
- [os_workgroup_create_with_port](os_workgroup_create_with_port.md) — Creates a new workgroup that is bound to the workgroup with the specified Mach port.
- [os_workgroup_t](os_workgroup_t.md) — An opaque object representing a default workgroup in the current process.
- [os_workgroup_attr_t](os_workgroup_attr_t.md) — An opaque structure for storing workgroup-related attributes.
