---
title: UIImage.DynamicRange
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/dynamicrange
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/dynamicrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/dynamicrange.json'
content_hash: 'sha256:67e03094154ac8d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# UIImage.DynamicRange

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum DynamicRange
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [UIImageDynamicRangeConstrainedHigh](dynamicrange/constrainedhigh.md) — Allow image content to use some extended range. This is appropriate for mixing content with standard and high dynamic ranges.
- [UIImageDynamicRangeHigh](dynamicrange/high.md) — Allow image content to use unrestricted extended range.
- [UIImageDynamicRangeStandard](dynamicrange/standard.md) — Restrict the image content dynamic range to the standard range.
- [UIImageDynamicRangeUnspecified](dynamicrange/unspecified.md) — Do not specify a preferred dynamic range.

### Initializers

- [init(rawValue:)](<dynamicrange/init(rawvalue_).md>)

## See Also

### Specifying the dynamic range

- [isHighDynamicRange](ishighdynamicrange.md) — Indicates that this image is tagged for display of high dynamic range content.
- [- imageRestrictedToStandardDynamicRange](<imagerestrictedtostandarddynamicrange().md>) — Returns a new image that will render within the standard range.
- [UIImageHEICRepresentation](<heicdata().md>) — Returns HEIC data representing the image, or nil if such a representation could not be generated. HEIC is recommended for efficiently storing all kinds of images, including those with high dynamic range content.
