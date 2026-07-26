---
title: 'copyResourceViews(sourcePool:sourceRange:destinationIndex:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlresourceviewpool/copyresourceviews(sourcepool:sourcerange:destinationindex:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlresourceviewpool/copyresourceviews(sourcepool:sourcerange:destinationindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourceviewpool/copyresourceviews%28sourcepool%3Asourcerange%3Adestinationindex%3A%29.json'
content_hash: 'sha256:5263efeee4cc916c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceViewPool](../mtlresourceviewpool.md)

# copyResourceViews(sourcePool:sourceRange:destinationIndex:)

<sub>Instance Method</sub>

Copies a range of resource views from a source view pool to a destination location in this view pool.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copyResourceViews(sourcePool: any MTLResourceViewPool, sourceRange: Range<Int>, destinationIndex: Int) -> MTLResourceID
```

## Parameters

- `sourcePool` — Resource view pool from which to copy resource views.

- `sourceRange` — The range in the source resource view pool to copy.

- `destinationIndex` — The starting index in this destination view pool into which to copy the source range of resource views.

## Return Value

The [MTLResourceID](../mtlresourceid.md) of the resource view corresponding to `destinationIndex` of the copy in this resource view pool.
