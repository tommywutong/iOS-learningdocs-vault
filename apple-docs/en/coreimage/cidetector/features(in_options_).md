---
title: 'features(in:options:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cidetector/features(in:options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cidetector/features(in:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidetector/features%28in%3Aoptions%3A%29.json'
content_hash: 'sha256:643d36f8b76cddac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIDetector](../cidetector.md)

# features(in:options:)

<sub>Instance Method</sub>

Searches for features in an image based on the specified image orientation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func features(in image: CIImage, options: [String : Any]? = nil) -> [CIFeature]
```

## Parameters

- `image` — The image you want to examine.

- `options` — A dictionary that specifies feature detection options. See [Feature Detection Keys](../feature-detection-keys.md) for allowed keys and their possible values.

## Return Value

An array of [CIFeature](../cifeature.md) objects. Each object represents a feature detected in the image.

## See Also

### Using a Detector Object to Find Features

- [- featuresInImage:](<features(in_).md>) — Searches for features in an image.
