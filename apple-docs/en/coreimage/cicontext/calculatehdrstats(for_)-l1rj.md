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
doc_path: '/documentation/coreimage/cicontext/calculatehdrstats(for:)-l1rj'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/calculatehdrstats(for:)-l1rj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/calculatehdrstats%28for%3A%29-l1rj.json'
content_hash: 'sha256:026fc4e20bbd29e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# calculateHDRStats(for:)

<sub>Instance Method</sub>

Given a Core Image image, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then return a new Core Image image that has the calculated values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func calculateHDRStats(for image: CIImage) -> CIImage?
```

## Parameters

- `image` — An immutable [CIImage](../ciimage.md) for which to calculate statistics.

## Return Value

Returns a new [CIImage](../ciimage.md) instance that has the calculated statistics attached.

## Discussion

If the image extent is not finite, then nil will be returned.
