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
doc_path: '/documentation/coreimage/cicontext/calculatehdrstats(for:)-3ia7r'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/calculatehdrstats(for:)-3ia7r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/calculatehdrstats%28for%3A%29-3ia7r.json'
content_hash: 'sha256:164cc6d094410ab4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# calculateHDRStats(for:)

<sub>Instance Method</sub>

Given a Core Graphics image, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then return a new Core Graphics image that has the calculated values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func calculateHDRStats(for cgimage: CGImage) -> CGImage
```

## Parameters

- `cgimage` — An immutable `CGImage` for which to calculate statistics.

## Return Value

Returns a new `CGImage` instance that has the calculated statistics attached.
