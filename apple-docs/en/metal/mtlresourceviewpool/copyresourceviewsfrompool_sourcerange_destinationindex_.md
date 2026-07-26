---
title: 'copyResourceViewsFromPool:sourceRange:destinationIndex:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlresourceviewpool/copyresourceviewsfrompool:sourcerange:destinationindex:'
source_url: 'https://developer.apple.com/documentation/metal/mtlresourceviewpool/copyresourceviewsfrompool:sourcerange:destinationindex:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourceviewpool/copyresourceviewsfrompool%3Asourcerange%3Adestinationindex%3A.json'
content_hash: 'sha256:6b9781e99c543b7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceViewPool](../mtlresourceviewpool.md)

# copyResourceViewsFromPool:sourceRange:destinationIndex:

<sub>Instance Method</sub>

Copies a range of resource views from a source view pool to a destination location in this view pool.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (MTLResourceID) copyResourceViewsFromPool:(id<MTLResourceViewPool>) sourcePool sourceRange:(NSRange) sourceRange destinationIndex:(NSUInteger) destinationIndex;
```

## Parameters

- `sourcePool` — Resource view pool from which to copy resource views.

- `sourceRange` — The range in the source resource view pool to copy.

- `destinationIndex` — The starting index in this destination view pool into which to copy the source range of resource views.

## Return Value

The [MTLResourceID](../mtlresourceid.md) of the resource view corresponding to `destinationIndex` of the copy in this resource view pool.
