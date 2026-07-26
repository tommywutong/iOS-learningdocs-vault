---
title: dispatch_data_copy_region
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_data_copy_region
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_data_copy_region'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_data_copy_region.json'
content_hash: 'sha256:48ef101df4d0701c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_data_copy_region

<sub>Function</sub>

Returns a data object containing a portion of the data in another data object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern dispatch_data_tdispatch_data_copy_region(dispatch_data_t data, size_t location, size_t *offset_ptr);
```

## Parameters

- `data` — The dispatch data object to query.

- `location` — The byte offset to use when determining which memory region to return.

- `offset_ptr` — On input, a pointer to a variable. On output, this variable contains the offset from the beginning of `data` of the returned memory region.

## Return Value

A dispatch data object containing a copy of the entire memory region that contains the specified location.

## See Also

### Creating a Dispatch Data Object

- [dispatch_data_create](dispatch_data_create.md) — Creates a new dispatch data object with the specified memory buffer.
- [dispatch_data_create_map](dispatch_data_create_map.md) — Returns a new dispatch data object containing a contiguous representation of the specified object’s memory.
- [dispatch_data_create_concat](dispatch_data_create_concat.md) — Returns a new dispatch data object consisting of the concatenated data from two other data objects.
- [dispatch_data_create_subrange](dispatch_data_create_subrange.md) — Returns a new dispatch data object whose contents consist of a portion of another object’s memory region.
- [dispatch_data_empty](dispatch_data_empty.md) — A dispatch data object representing a zero-length memory region.
- [dispatch_data_t](dispatch_data_t.md) — An immutable object representing a contiguous or sparse region of memory.
- [OS_dispatch_data](os_dispatch_data.md)
- [DISPATCH_DATA_DESTRUCTOR_DEFAULT](dispatch_data_destructor_default.md) — The default data destructor for dispatch objects.
- [DISPATCH_DATA_DESTRUCTOR_FREE](dispatch_data_destructor_free.md) — The destructor for dispatch data objects whose memory buffer was created using the malloc family of allocation routines.
