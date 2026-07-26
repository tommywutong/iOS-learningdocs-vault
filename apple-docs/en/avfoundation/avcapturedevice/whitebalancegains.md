---
title: AVCaptureDevice.WhiteBalanceGains
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/whitebalancegains
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancegains'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/whitebalancegains.json'
content_hash: 'sha256:afbcb68e151cd0fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.WhiteBalanceGains

<sub>Structure</sub>

A structure that defines RGB white balance gain values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
struct WhiteBalanceGains
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Sendable](../../swift/sendable.md)

## Topics

### Creating white balance gains

- [init()](<whitebalancegains/init().md>) — The default initializer for white balance gains.
- [init(redGain:greenGain:blueGain:)](<whitebalancegains/init(redgain_greengain_bluegain_).md>) — Initializes a white balance gain from its red, green, and blue gain components.

### Isolating gain by color channel

- [blueGain](whitebalancegains/bluegain.md) — The blue gain component of the white balance value.
- [greenGain](whitebalancegains/greengain.md) — The green gain component of the white balance value.
- [redGain](whitebalancegains/redgain.md) — The red gain component of the white balance value.

## See Also

### Performing conversions

- [- chromaticityValuesForDeviceWhiteBalanceGains:](<chromaticityvalues(for_).md>) — Converts device-specific white balance RGB gain values to device-independent chromaticity values.
- [- temperatureAndTintValuesForDeviceWhiteBalanceGains:](<temperatureandtintvalues(for_).md>) — Converts device-specific white balance RGB gain values to device-independent temperature and tint values.
- [- deviceWhiteBalanceGainsForChromaticityValues:](<devicewhitebalancegains(for_)-9gdtw.md>) — Converts device-independent chromaticity values to device-specific white balance RGB gain values.
- [- deviceWhiteBalanceGainsForTemperatureAndTintValues:](<devicewhitebalancegains(for_)-3wtsa.md>) — Converts device-independent temperature and tint values to device-specific white balance RGB gain values.
- [WhiteBalanceChromaticityValues](whitebalancechromaticityvalues.md) — A structure that defines CIE 1931 xy chromaticity values.
- [WhiteBalanceTemperatureAndTintValues](whitebalancetemperatureandtintvalues.md) — A structure that defines temperature and tint values correlated to a white-balance color.
