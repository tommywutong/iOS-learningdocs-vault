---
title: AVCaptionRegion
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionregion
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionregion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionregion.json'
content_hash: 'sha256:51fbf6be44aaa7ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptionRegion

<sub>Class</sub>

An object that represents the region in which the system presents a caption.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AVCaptionRegion
```

## Overview

The framework defines four regions, and doesn’t support configuring region settings.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVMutableCaptionRegion](avmutablecaptionregion.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Accessing defined regions

- [appleITTTopRegion](avcaptionregion/appleitttop.md) — The top region for iTT format captions.
- [appleITTBottomRegion](avcaptionregion/appleittbottom.md) — The bottom region for iTT format captions.
- [appleITTLeftRegion](avcaptionregion/appleittleft.md) — The left region for iTT format captions.
- [appleITTRightRegion](avcaptionregion/appleittright.md) — The right region for iTT format captions.
- [subRipTextBottomRegion](avcaptionregion/subriptextbottom.md) — The bottom caption region for SubRip Text (SRT) format captions.

### Identifying a region

- [identifier](avcaptionregion/identifier.md) — A string that identifies the region.

### Accessing dimensions

- [AVCaptionDimension](avcaptiondimension.md) — A structure that defines a caption dimension.

### Accessing the location

- [origin](avcaptionregion/origin.md) — The region’s top-left position.
- [AVCaptionPoint](avcaptionpoint.md) — A structure that defines the origin point for a caption.

### Accessing the size

- [size](avcaptionregion/size.md) — The height and width of the region.
- [AVCaptionSize](avcaptionsize.md) — A structure that defines the height and width of a caption.

### Accessing the display alignment

- [displayAlignment](avcaptionregion/displayalignment-swift.property.md) — The alignment of lines for the region.
- [DisplayAlignment](avcaptionregion/displayalignment-swift.enum.md) — Constants that indicate the alignment of lines in a region.

### Accessing the scroll mode

- [scroll](avcaptionregion/scroll-swift.property.md) — The scroll mode of the region.
- [Scroll](avcaptionregion/scroll-swift.enum.md) — Constants that indicate the scrolling effects the system applies to a region.

### Accessing the writing mode

- [writingMode](avcaptionregion/writingmode-swift.property.md) — The block and inline progression direction of the region.
- [WritingMode](avcaptionregion/writingmode-swift.enum.md) — Constants that indicate the writing mode for a region.

### Processing regions

- [- mutableCopyWithZone:](<avcaptionregion/mutablecopy(with_).md>) — Creates a mutable copy of a caption region.
- [- encodeWithCoder:](<avcaptionregion/encode(with_).md>) — Encodes the region using the specified encoder.
- [- isEqual:](<avcaptionregion/isequal(__).md>) — Returns a Boolean value that indicates whether an object equals another.

### Initializers

- [init(coder:)](<avcaptionregion/init(coder_).md>)

## See Also

### Regions

- [AVMutableCaptionRegion](avmutablecaptionregion.md) — A mutable caption region subclass that you use to create new caption regions.
