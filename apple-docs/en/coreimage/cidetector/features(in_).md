---
title: 'features(in:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cidetector/features(in:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cidetector/features(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidetector/features%28in%3A%29.json'
content_hash: 'sha256:58f77c1a2687161c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIDetector](../cidetector.md)

# features(in:)

<sub>Instance Method</sub>

Searches for features in an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func features(in image: CIImage) -> [CIFeature]
```

## Parameters

- `image` — The image you want to examine.

## Return Value

An array of [CIFeature](../cifeature.md) objects. Each object represents a feature detected in the image.

## See Also

### Using a Detector Object to Find Features

- [- featuresInImage:options:](<features(in_options_).md>) — Searches for features in an image based on the specified image orientation.
