---
title: naturalSize
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/naturalsize
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/naturalsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/naturalsize.json'
content_hash: 'sha256:c80ae6a2a29a47af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# naturalSize

<sub>Type Property</sub>

The natural dimensions of the media data that the track references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var naturalSize: AVAsyncProperty<Root, CGSize> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

For visual tracks, like video or subtitle tracks, this property value is the natural size of the media. For nonvisual tracks, like audio or chapter tracks, the value is [zero](../../corefoundation/cgsize/zero.md).

## See Also

### Loading visual characteristics

- [preferredTransform](preferredtransform-90jdn.md) — The track’s transform preference to apply to its visual content during presentation or processing.
