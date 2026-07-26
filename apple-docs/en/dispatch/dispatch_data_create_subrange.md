---
title: dispatch_data_create_subrange
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_data_create_subrange
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_data_create_subrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_data_create_subrange.json'
content_hash: 'sha256:8d741b624a6edb24'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_data_create_subrange

<sub>Function</sub>

Returns a new dispatch data object whose contents consist of a portion of another object’s memory region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern dispatch_data_tdispatch_data_create_subrange(dispatch_data_t data, size_t offset, size_t length);
```

## Parameters

- `data` — The dispatch data object containing the original memory to use for the new object.

- `offset` — A byte offset into the memory of `data`. This offset marks the starting point of the memory for the new object.

- `length` — The number of bytes from `offset` to include in the new object.

## Return Value

A new dispatch data object whose memory is a subrange of the memory associated with the object in the `data` parameter.

## Discussion

After calling this function, it is safe to release the object in `data`. However, be aware that the memory from that object may not be deallocated immediately if the newly created dispatch data object references it, as opposed to copies it.

## See Also

### Creating a Dispatch Data Object

- [dispatch_data_create](dispatch_data_create.md) — Creates a new dispatch data object with the specified memory buffer.
- [dispatch_data_create_map](dispatch_data_create_map.md) — Returns a new dispatch data object containing a contiguous representation of the specified object’s memory.
- [dispatch_data_create_concat](dispatch_data_create_concat.md) — Returns a new dispatch data object consisting of the concatenated data from two other data objects.
- [dispatch_data_copy_region](dispatch_data_copy_region.md) — Returns a data object containing a portion of the data in another data object.
- [dispatch_data_empty](dispatch_data_empty.md) — A dispatch data object representing a zero-length memory region.
- [dispatch_data_t](dispatch_data_t.md) — An immutable object representing a contiguous or sparse region of memory.
- [OS_dispatch_data](os_dispatch_data.md)
- [DISPATCH_DATA_DESTRUCTOR_DEFAULT](dispatch_data_destructor_default.md) — The default data destructor for dispatch objects.
- [DISPATCH_DATA_DESTRUCTOR_FREE](dispatch_data_destructor_free.md) — The destructor for dispatch data objects whose memory buffer was created using the malloc family of allocation routines.
