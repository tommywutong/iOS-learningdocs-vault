---
title: AVDisplayDynamicRange
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avdisplaydynamicrange
source_url: 'https://developer.apple.com/documentation/avkit/avdisplaydynamicrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avdisplaydynamicrange.json'
content_hash: 'sha256:a50db518d4b86c00'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVDisplayDynamicRange

<sub>Enumeration</sub>

Describes how High Dynamic Range (HDR) video content renders.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
enum AVDisplayDynamicRange
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a dynamic range

- [init(rawValue:)](<avdisplaydynamicrange/init(rawvalue_).md>)

### Dynamic Ranges

- [AVDisplayDynamicRangeAutomatic](avdisplaydynamicrange/automatic.md) — Defines an automatic dynamic range. Indicates that the dynamic range will be set automatically.
- [AVDisplayDynamicRangeStandard](avdisplaydynamicrange/standard.md) — Defines a standard dynamic range. Restricts the video content dynamic range to the standard range regardless of the actual range of the video content.
- [AVDisplayDynamicRangeConstrainedHigh](avdisplaydynamicrange/constrainedhigh.md) — Defines a constrained high dynamic range. Allows for constrained High Dynamic Range (HDR) video content which is useful for mixing HDR and Standard Dynamic Range (SDR) content.
- [AVDisplayDynamicRangeHigh](avdisplaydynamicrange/high.md) — Defines a high dynamic range. Allows video content to use extended dynamic range if it has dynamic range content.

## See Also

### High dynamic range

- [preferredDisplayDynamicRange](avplayerview/preferreddisplaydynamicrange.md) — Describes how High Dynamic Range (HDR) video content renders.
