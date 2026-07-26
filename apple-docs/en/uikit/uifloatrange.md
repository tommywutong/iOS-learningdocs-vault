---
title: UIFloatRange
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifloatrange
source_url: 'https://developer.apple.com/documentation/uikit/uifloatrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifloatrange.json'
content_hash: 'sha256:fcaee9dc7099148e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFloatRange

<sub>Structure</sub>

The range of motion for attached objects.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UIFloatRange
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a float range

- [init()](<uifloatrange/init().md>)
- [init(minimum:maximum:)](<uifloatrange/init(minimum_maximum_)-8dzgq.md>) — Returns a new float range structure from the given components.
- [UIFloatRangeInfinite](uifloatrange/infinite.md) — A range whose range is minus infinity to infinity.
- [UIFloatRangeZero](uifloatrange/zero.md) — A range whose minimum and maximum are both `0.0`.

### Getting the range values

- [maximum](uifloatrange/maximum.md) — The maximum range of motion for sliding and pin attachments.
- [minimum](uifloatrange/minimum.md) — The minimum range of motion for sliding and pin attachments.

### Testing the range values

- [UIFloatRangeIsInfinite](uifloatrange/isinfinite.md) — Returns a Boolean indicating whether the specified float range is infinitely large.
- [UIFloatRangeIsEqualToRange(_:_:)](<uifloatrangeisequaltorange(____).md>) — Returns a Boolean indicating whether two float ranges are equivalent. _(deprecated)_

## See Also

### Constants

- [AttachmentType](uiattachmentbehavior/attachmenttype.md) — Constants indicating the type of the attachment behavior object.
- [Float range constants](float-range-constants.md) — Constants for specifying standard ranges.
- [UIOffset](uioffset.md) — A structure that specifies an amount to offset a position.
