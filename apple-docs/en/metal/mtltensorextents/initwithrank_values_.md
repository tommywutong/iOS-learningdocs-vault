---
title: 'initWithRank:values:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltensorextents/initwithrank:values:'
source_url: 'https://developer.apple.com/documentation/metal/mtltensorextents/initwithrank:values:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorextents/initwithrank%3Avalues%3A.json'
content_hash: 'sha256:da24c871be6fa19a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorExtents](../mtltensorextents.md)

# initWithRank:values:

<sub>Instance Method</sub>

Creates an extents object with the rank and values you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (instancetype) initWithRank:(NSUInteger) rank values:(const NSInteger *) values;
```

## Parameters

- `rank` — The number of values in the extents. Pass `0` to create a scalar (rank-zero) extents.

- `values` — A C array of `rank` integer values, or `nil` when `rank` is `0`. The first element corresponds to the innermost dimension.

## Return Value

A new extents instance, or `nil` if `rank` exceeds 0 and `values` is `nil`, or if `rank` exceeds [MTL_TENSOR_MAX_RANK](../mtl_tensor_max_rank.md).

## Discussion

Zero rank extents represent scalars. `values` can only be `nil` if `rank` is 0.
