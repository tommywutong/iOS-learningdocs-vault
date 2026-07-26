---
title: OS_dispatch_data
framework: Dispatch
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/os_dispatch_data
source_url: 'https://developer.apple.com/documentation/dispatch/os_dispatch_data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/os_dispatch_data.json'
content_hash: 'sha256:6f0c3d6726ec2fd5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# OS_dispatch_data

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@protocol OS_dispatch_data <OS_dispatch_object>
```

## Relationships

- **Inherits From**: [OS_dispatch_object](os_dispatch_object.md)

## See Also

### Creating a Dispatch Data Object

- [dispatch_data_create](dispatch_data_create.md) — Creates a new dispatch data object with the specified memory buffer.
- [dispatch_data_create_map](dispatch_data_create_map.md) — Returns a new dispatch data object containing a contiguous representation of the specified object’s memory.
- [dispatch_data_create_concat](dispatch_data_create_concat.md) — Returns a new dispatch data object consisting of the concatenated data from two other data objects.
- [dispatch_data_create_subrange](dispatch_data_create_subrange.md) — Returns a new dispatch data object whose contents consist of a portion of another object’s memory region.
- [dispatch_data_copy_region](dispatch_data_copy_region.md) — Returns a data object containing a portion of the data in another data object.
- [dispatch_data_empty](dispatch_data_empty.md) — A dispatch data object representing a zero-length memory region.
- [dispatch_data_t](dispatch_data_t.md) — An immutable object representing a contiguous or sparse region of memory.
- [DISPATCH_DATA_DESTRUCTOR_DEFAULT](dispatch_data_destructor_default.md) — The default data destructor for dispatch objects.
- [DISPATCH_DATA_DESTRUCTOR_FREE](dispatch_data_destructor_free.md) — The destructor for dispatch data objects whose memory buffer was created using the malloc family of allocation routines.
