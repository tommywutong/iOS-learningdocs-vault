---
title: AVCaptureDevice.WhiteBalanceChromaticityValues
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/whitebalancechromaticityvalues
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancechromaticityvalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/whitebalancechromaticityvalues.json'
content_hash: 'sha256:6818bcd082425624'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.WhiteBalanceChromaticityValues

<sub>Structure</sub>

A structure that defines CIE 1931 xy chromaticity values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
struct WhiteBalanceChromaticityValues
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Sendable](../../swift/sendable.md)

## Topics

### Creating chromaticity values

- [init()](<whitebalancechromaticityvalues/init().md>) — Creates a structure for white balance chromaticity values.
- [init(x:y:)](<whitebalancechromaticityvalues/init(x_y_).md>) — Creates a structure for white balance chromaticity values from its x and y coordinates.

### Inspecting the values

- [x](whitebalancechromaticityvalues/x.md) — The x component of the CIE 1931 chromaticity value.
- [y](whitebalancechromaticityvalues/y.md) — The y component of the CIE 1931 chromaticity value.

## See Also

### Performing conversions

- [- chromaticityValuesForDeviceWhiteBalanceGains:](<chromaticityvalues(for_).md>) — Converts device-specific white balance RGB gain values to device-independent chromaticity values.
- [- temperatureAndTintValuesForDeviceWhiteBalanceGains:](<temperatureandtintvalues(for_).md>) — Converts device-specific white balance RGB gain values to device-independent temperature and tint values.
- [- deviceWhiteBalanceGainsForChromaticityValues:](<devicewhitebalancegains(for_)-9gdtw.md>) — Converts device-independent chromaticity values to device-specific white balance RGB gain values.
- [- deviceWhiteBalanceGainsForTemperatureAndTintValues:](<devicewhitebalancegains(for_)-3wtsa.md>) — Converts device-independent temperature and tint values to device-specific white balance RGB gain values.
- [WhiteBalanceGains](whitebalancegains.md) — A structure that defines RGB white balance gain values.
- [WhiteBalanceTemperatureAndTintValues](whitebalancetemperatureandtintvalues.md) — A structure that defines temperature and tint values correlated to a white-balance color.
