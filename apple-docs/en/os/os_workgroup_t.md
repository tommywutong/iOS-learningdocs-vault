---
title: os_workgroup_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_t
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_t.json'
content_hash: 'sha256:56f0f296d6cc6c2c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_workgroup_t

<sub>Type Alias</sub>

An opaque object representing a default workgroup in the current process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef OS_os_workgroup * os_workgroup_t;
```

## See Also

### Common Utilities

- [os_workgroup_create_with_workgroup](os_workgroup_create_with_workgroup.md) — Create a new workgroup that is bound to the specified workgroup.
- [os_workgroup_create_with_port](os_workgroup_create_with_port.md) — Creates a new workgroup that is bound to the workgroup with the specified Mach port.
- [os_workgroup_copy_port](os_workgroup_copy_port.md) — Returns the Mach port associated with the workgroup.
- [os_workgroup_attr_t](os_workgroup_attr_t.md) — An opaque structure for storing workgroup-related attributes.
