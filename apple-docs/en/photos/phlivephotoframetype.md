---
title: PHLivePhotoFrameType
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoframetype
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoframetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoframetype.json'
content_hash: 'sha256:fb2e16d91c232cde'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHLivePhotoFrameType

<sub>Enumeration</sub>

Identifiers for the type of frame image to be processed. Used with the [type](phlivephotoframe/type.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHLivePhotoFrameType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [PHLivePhotoFrameTypePhoto](phlivephotoframetype/photo.md) — The image is a still photo.
- [PHLivePhotoFrameTypeVideo](phlivephotoframetype/video.md) — The image is a single frame from the Live Photo’s video content.

### Initializers

- [init(rawValue:)](<phlivephotoframetype/init(rawvalue_).md>)

## See Also

### Getting Information About the Frame

- [renderScale](phlivephotoframe/renderscale.md) — The scale factor of the frame image relative to the Live Photo’s photo content.
- [time](phlivephotoframe/time.md) — The time offset, in seconds, of this frame relative to the start of the Live Photo.
- [type](phlivephotoframe/type.md) — The type of image content in this frame.
