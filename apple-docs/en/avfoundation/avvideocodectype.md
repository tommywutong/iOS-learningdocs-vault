---
title: AVVideoCodecType
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, swift, swift, swift, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocodectype
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocodectype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocodectype.json'
content_hash: 'sha256:3016a269c6f4ed66'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoCodecType

<sub>Structure</sub>

A set of constants that describe the codecs the system supports for video capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVVideoCodecType
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Video codecs

- [AVVideoCodecTypeH264](avvideocodectype/h264.md) — The H.264 video codec.
- [AVVideoCodecTypeHEVC](avvideocodectype/hevc.md) — The HEVC video codec.
- [AVVideoCodecTypeHEVCWithAlpha](avvideocodectype/hevcwithalpha.md) — The HEVC video codec that supports an alpha channel.
- [AVVideoCodecTypeJPEG](avvideocodectype/jpeg.md) — The JPEG video codec.
- [AVVideoCodecTypeJPEGXL](avvideocodectype/jpegxl.md) — The JPEG XL video codec.
- [AVVideoCodecTypeAppleProRes422](avvideocodectype/prores422.md) — The Apple ProRes 422 video codec.
- [AVVideoCodecTypeAppleProRes422LT](avvideocodectype/prores422lt.md) — The Apple ProRes 422 LT video codec.
- [AVVideoCodecTypeAppleProRes422HQ](avvideocodectype/prores422hq.md) — The Apple ProRes 422 HQ video codec.
- [AVVideoCodecTypeAppleProRes422Proxy](avvideocodectype/prores422proxy.md) — The Apple ProRes 422 Proxy video codec.
- [AVVideoCodecTypeAppleProRes4444](avvideocodectype/prores4444.md) — The Apple ProRes 4444 video codec.
- [AVVideoCodecTypeAppleProResRAW](avvideocodectype/proresraw.md)
- [AVVideoCodecTypeAppleProResRAWHQ](avvideocodectype/proresrawhq.md)
- [AVVideoCodecTypeAppleProRes4444XQ](avvideocodectype/appleprores4444xq.md) — The Apple ProRes 4444 XQ video codec.

### Deprecated

- [AVVideoCodecH264](avvideocodech264.md) — A key to access the name of the H.264 codec for compressing video. _(deprecated)_
- [AVVideoCodecHEVC](avvideocodechevc.md) — A key to access the name of the HEVC codec used to encode the video. _(deprecated)_
- [AVVideoCodecJPEG](avvideocodecjpeg.md) — A key to access the name of the JPEG codec for compressing video. _(deprecated)_
- [AVVideoCodecAppleProRes422](avvideocodecappleprores422.md) — A key to access the name of the Apple ProRes422 codec used to encode the video. _(deprecated)_
- [AVVideoCodecAppleProRes4444](avvideocodecappleprores4444.md) — A key to access the name of the Apple ProRes4444 codec used to encode the video. _(deprecated)_

### Initializers

- [init(rawValue:)](<avvideocodectype/init(rawvalue_).md>) — Creates a codec type from its raw string value.

## See Also

### Video codecs

- [AVVideoCodecKey](avvideocodeckey.md) — A key to access the name of the codec for compressing video.
