---
title: 'calculateHDRStats(for:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/calculatehdrstats(for:)-6lwmz'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/calculatehdrstats(for:)-6lwmz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/calculatehdrstats%28for%3A%29-6lwmz.json'
content_hash: 'sha256:0abae46874ec680c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# calculateHDRStats(for:)

<sub>Instance Method</sub>

Given an IOSurface, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then update the surface’s attachments to store the values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func calculateHDRStats(for surface: IOSurfaceRef)
```

## Parameters

- `surface` — A mutable `IOSurfaceRef` for which to calculate and attach statistics.

## Discussion

If the `IOSurface` has a Clean Aperture rectangle then only pixels within that rectangle are considered.
