---
title: AVCaptionRegion.DisplayAlignment
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionregion/displayalignment-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionregion/displayalignment-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionregion/displayalignment-swift.enum.json'
content_hash: 'sha256:94ce05a3173339f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRegion](../avcaptionregion.md)

# AVCaptionRegion.DisplayAlignment

<sub>Enumeration</sub>

Constants that indicate the alignment of lines in a region.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
enum DisplayAlignment
```

## Overview

When you insert a caption line, the region places it relative to existing lines. The system determines the order in which the region places lines by its block progression direction. For example, English captions’ block progression direction are top-to-bottom, while Japanese vertical captions use right-to-left.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Display alignments

- [AVCaptionRegionDisplayAlignmentBefore](displayalignment-swift.enum/before.md) — An alignment that positions lines at the top of the block progression direction.
- [AVCaptionRegionDisplayAlignmentCenter](displayalignment-swift.enum/center.md) — An alignment that positions lines in the middle of the block progression direction.
- [AVCaptionRegionDisplayAlignmentAfter](displayalignment-swift.enum/after.md) — An alignment that positions lines at the bottom of the block progression direction.

### Initializers

- [init(rawValue:)](<displayalignment-swift.enum/init(rawvalue_).md>)

## See Also

### Accessing the display alignment

- [displayAlignment](displayalignment-swift.property.md) — The alignment of lines for the region.
