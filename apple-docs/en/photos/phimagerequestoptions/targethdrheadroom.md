---
title: targetHDRHeadroom
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptions/targethdrheadroom
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptions/targethdrheadroom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptions/targethdrheadroom.json'
content_hash: 'sha256:68fffc6a6a2fdb07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptions](../phimagerequestoptions.md)

# targetHDRHeadroom

<sub>Instance Property</sub>

Target HDR headroom for image rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var targetHDRHeadroom: CGFloat { get set }
```

## Discussion

Specifies the target headroom value for HDR image rendering. Headroom represents the ratio between the maximum display brightness and standard dynamic range (SDR) white level.

- A headroom value of `0.0` means “headroom unknown”. Images with unknown content headroom will be excluded from tone mapping, following CGImage documentation behavior.
- Headroom values less than `0.0` or between `0.0` and `1.0` (exclusive) are undefined and will be clamped to `0.0` (unknown) rather than throwing an error.
- Headroom is dependent on the current display capabilities. It is the responsibility of the caller to re-request the image if the display’s headroom characteristics change. Swift view default behavior applies to views that use images outside of the current display headroom supported range.

Defaults to `1.0` (SDR, fully tone mapped).
