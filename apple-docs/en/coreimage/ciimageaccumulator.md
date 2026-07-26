---
title: CIImageAccumulator
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageaccumulator
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageaccumulator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageaccumulator.json'
content_hash: 'sha256:5d4d7a85cc1f0f1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIImageAccumulator

<sub>Class</sub>

An object that manages feedback-based image processing for tasks such as painting or fluid simulation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIImageAccumulator
```

## Overview

The `CIImageAccumulator` class enables feedback-based image processing for such things as iterative painting operations or fluid dynamics simulations. You use `CIImageAccumulator` objects in conjunction with other Core Image classes, such as  [CIFilter](cifilter-swift.class.md), [CIImage](ciimage.md), [CIVector](civector.md), and [CIContext](cicontext.md), to take advantage of the built-in Core Image filters when processing images.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing an Image Accumulator

- [- initWithExtent:format:](<ciimageaccumulator/init(extent_format_).md>) — Initializes an image accumulator with the specified extent and pixel format.
- [- initWithExtent:format:colorSpace:](<ciimageaccumulator/init(extent_format_colorspace_).md>) — Initializes an image accumulator with the specified extent, pixel format, and color space.

### Setting an Image

- [- setImage:](<ciimageaccumulator/setimage(__).md>) — Sets the contents of the image accumulator to the contents of the specified image object.
- [- setImage:dirtyRect:](<ciimageaccumulator/setimage(__dirtyrect_).md>) — Updates an image accumulator with a subregion of an image object.

### Obtaining Data From an Image Accumulator

- [extent](ciimageaccumulator/extent.md) — The extent of the image associated with the image accumulator.
- [format](ciimageaccumulator/format.md) — The pixel format of the image accumulator.
- [- image](<ciimageaccumulator/image().md>) — Returns the current contents of the image accumulator.

### Resetting an Accumulator

- [- clear](<ciimageaccumulator/clear().md>) — Resets the accumulator, discarding any pending updates and the current content.
