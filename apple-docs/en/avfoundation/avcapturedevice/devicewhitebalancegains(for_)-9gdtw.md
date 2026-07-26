---
title: 'deviceWhiteBalanceGains(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/devicewhitebalancegains(for:)-9gdtw'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicewhitebalancegains(for:)-9gdtw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/devicewhitebalancegains%28for%3A%29-9gdtw.json'
content_hash: 'sha256:ee0fd98e2dc51563'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# deviceWhiteBalanceGains(for:)

<sub>Instance Method</sub>

Converts device-independent chromaticity values to device-specific white balance RGB gain values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func deviceWhiteBalanceGains(for chromaticityValues: AVCaptureDevice.WhiteBalanceChromaticityValues) -> AVCaptureDevice.WhiteBalanceGains
```

## Parameters

- `chromaticityValues` — The chromaticity values for which to get white balance RGB gain values.

## Return Value

A structure that contains device-specific RGB gain values.

## Discussion

This property specifies the current red, green, and blue gain values used for white balance. You can use the values to adjust color casts for a given scene.

Each channel supports values between `1.0` and -[maxWhiteBalanceGain](maxwhitebalancegain.md).

This property is key-value observable.

## See Also

### Performing conversions

- [- chromaticityValuesForDeviceWhiteBalanceGains:](<chromaticityvalues(for_).md>) — Converts device-specific white balance RGB gain values to device-independent chromaticity values.
- [- temperatureAndTintValuesForDeviceWhiteBalanceGains:](<temperatureandtintvalues(for_).md>) — Converts device-specific white balance RGB gain values to device-independent temperature and tint values.
- [- deviceWhiteBalanceGainsForTemperatureAndTintValues:](<devicewhitebalancegains(for_)-3wtsa.md>) — Converts device-independent temperature and tint values to device-specific white balance RGB gain values.
- [WhiteBalanceGains](whitebalancegains.md) — A structure that defines RGB white balance gain values.
- [WhiteBalanceChromaticityValues](whitebalancechromaticityvalues.md) — A structure that defines CIE 1931 xy chromaticity values.
- [WhiteBalanceTemperatureAndTintValues](whitebalancetemperatureandtintvalues.md) — A structure that defines temperature and tint values correlated to a white-balance color.
