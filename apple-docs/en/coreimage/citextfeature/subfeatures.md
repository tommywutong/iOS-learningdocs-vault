---
title: subFeatures
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/citextfeature/subfeatures
source_url: 'https://developer.apple.com/documentation/coreimage/citextfeature/subfeatures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/citextfeature/subfeatures.json'
content_hash: 'sha256:e974167523c9c67c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CITextFeature](../citextfeature.md)

# subFeatures

<sub>Instance Property</sub>

An array containing additional features detected within the feature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var subFeatures: [Any]? { get }
```

## Discussion

A text detector can identify both a major region that is likely to contain text as well as the areas within that region that likely to contain individual text features. Such features might be single characters, groups of closely-packed characters, or entire words.

To detect sub-features, `/CIDetector/featuresInImage:options:` needs to be called with the [CIDetectorReturnSubFeatures](../cidetectorreturnsubfeatures.md) option set to true.
