---
title: intendedSpatialExperience
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/opaquepointer/intendedspatialexperience
source_url: 'https://developer.apple.com/documentation/swift/opaquepointer/intendedspatialexperience'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/opaquepointer/intendedspatialexperience.json'
content_hash: 'sha256:acc2ee79a177f7f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OpaquePointer](../opaquepointer.md)

# intendedSpatialExperience

<sub>Instance Property</sub>

The AudioQueue’s intended spatial audio experience.

<sub>visionOS</sub>

```swift
var intendedSpatialExperience: any SpatialAudioExperience { get set }
```

## Discussion

This value is only useful for output AudioQueues not configured in offline mode; otherwise it’s a no-op.

If unspecified, the property value defaults to `AutomaticSpatialAudio`.
