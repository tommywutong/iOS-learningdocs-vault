---
title: AVFrameRateRange
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avframeraterange
source_url: 'https://developer.apple.com/documentation/avfoundation/avframeraterange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avframeraterange.json'
content_hash: 'sha256:bfe89c0fe25b2b90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVFrameRateRange

<sub>Class</sub>

An immutable type that represents a range of valid frame rates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVFrameRateRange
```

## Overview

An AVFrameRateRange object is immutable.

An [Format](avcapturedevice/format.md) object wraps a CMFormatDescription and expresses a range of valid video frame rates as an array of `AVFrameRateRange` objects.

An [AVCaptureDevice](avcapturedevice.md) object uses `AVCaptureDeviceFormat` to describe the formats it supports and the currently-active format.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing properties

- [maxFrameDuration](avframeraterange/maxframeduration.md) — The maximum frame duration supported by the range.
- [maxFrameRate](avframeraterange/maxframerate.md) — The maximum frame rate supported by the range.
- [minFrameDuration](avframeraterange/minframeduration.md) — The minimum frame duration supported by the range.
- [minFrameRate](avframeraterange/minframerate.md) — The minimum frame rate supported by the range.

## See Also

### Determining video capture support

- [autoVideoFrameRateSupported](avcapturedevice/format/isautovideoframeratesupported.md) — A Boolean value that Indicates whether the format supports performing automatic video frame rate adjustments.
- [videoSupportedFrameRateRanges](avcapturedevice/format/videosupportedframerateranges.md) — A list of frame rate ranges that a format supports.
- [videoBinned](avcapturedevice/format/isvideobinned.md) — A Boolean value that indicates whether the format produces video data in a binned format.
- [videoHDRSupported](avcapturedevice/format/isvideohdrsupported.md) — A Boolean value that indicates whether the format supports high dynamic range streaming.
- [multiCamSupported](avcapturedevice/format/ismulticamsupported.md) — A Boolean value that indicates whether a multi-camera capture session supports this format.
