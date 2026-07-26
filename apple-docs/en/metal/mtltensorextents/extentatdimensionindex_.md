---
title: 'extentAtDimensionIndex:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltensorextents/extentatdimensionindex:'
source_url: 'https://developer.apple.com/documentation/metal/mtltensorextents/extentatdimensionindex:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorextents/extentatdimensionindex%3A.json'
content_hash: 'sha256:27b37161074fc3b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorExtents](../mtltensorextents.md)

# extentAtDimensionIndex:

<sub>Instance Method</sub>

Returns the value at the specified dimension index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (NSInteger) extentAtDimensionIndex:(NSUInteger) dimensionIndex;
```

## Parameters

- `dimensionIndex` — The index of the value to retrieve. The first index corresponds to the innermost dimension.

## Return Value

The value at `dimensionIndex`, or `-1` if `dimensionIndex` is greater than or equal to [rank](rank.md).
