---
title: naturalSize
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassettrack/naturalsize
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/naturalsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/naturalsize.json'
content_hash: 'sha256:cf5caa7fc324e96b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# naturalSize

<sub>Instance Property</sub>

The natural dimensions of the media data that the track references.

> [!warning] Deprecated
> Load the value of [naturalSize](../avpartialasyncproperty/naturalsize.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var naturalSize: CGSize { get }
```

## Discussion

For visual tracks, like video or subtitle tracks, this property value is the natural size of the media. For nonvisual tracks, like audio or chapter tracks, the value is [zero](../../corefoundation/cgsize/zero.md).
