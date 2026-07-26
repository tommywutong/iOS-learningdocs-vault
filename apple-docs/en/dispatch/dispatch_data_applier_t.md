---
title: dispatch_data_applier_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_data_applier_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_data_applier_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_data_applier_t.json'
content_hash: 'sha256:a3aab51b307d568e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_data_applier_t

<sub>Type Alias</sub>

A block to invoke for every contiguous memory region in a data object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef _Bool (^)(NSObject<OS_dispatch_data> *, unsigned long, const void *, unsigned long) dispatch_data_applier_t;
```

## Discussion

The parameters of a dispatch data applier block are as follows:

- `region` - A data object containing the current memory region being analyzed.
- `offset` - The logical offset to the current region from the start of the data object.
- `buffer` - A pointer to the memory for the current region.
- `size` - The size of the memory for the current region.

This handler returns a Boolean value indicating whether traversal of the region should continue.

## See Also

### Applying Changes to the Data

- [dispatch_data_apply](dispatch_data_apply.md) — Traverses the memory of a dispatch data object and executes custom code on each region.
