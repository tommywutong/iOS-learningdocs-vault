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
doc_path: '/documentation/avfoundation/avcapturedevice/devicewhitebalancegains(for:)-3wtsa'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicewhitebalancegains(for:)-3wtsa'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/devicewhitebalancegains%28for%3A%29-3wtsa.json'
content_hash: 'sha256:de0d3b4a244f214e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# deviceWhiteBalanceGains(for:)

<sub>Instance Method</sub>

Converts device-independent temperature and tint values to device-specific white balance RGB gain values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func deviceWhiteBalanceGains(for tempAndTintValues: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues) -> AVCaptureDevice.WhiteBalanceGains
```

## Parameters

- `tempAndTintValues` — An [WhiteBalanceTemperatureAndTintValues](whitebalancetemperatureandtintvalues.md) structure containing the temperature and tint values.

## Return Value

A fully populated [WhiteBalanceGains](whitebalancegains.md) structure containing device-specific RGB gain values.

## Discussion

Call this method to convert device-independent temperature and tint values to device-specific RGB white balance gain values.

You may pass any temperature and tint values and corresponding white balance gains will be produced. Note, though, that some temperature and tint combinations yield out-of-range device RGB values that will cause an exception to be thrown if passed directly to [- setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:](<setwhitebalancemodelocked(with_completionhandler_).md>).  Be sure to verify that the red, green, and blue gain values are within the range of [`1.0` - [maxWhiteBalanceGain](maxwhitebalancegain.md)].

## See Also

### Performing conversions

- [- chromaticityValuesForDeviceWhiteBalanceGains:](<chromaticityvalues(for_).md>) — Converts device-specific white balance RGB gain values to device-independent chromaticity values.
- [- temperatureAndTintValuesForDeviceWhiteBalanceGains:](<temperatureandtintvalues(for_).md>) — Converts device-specific white balance RGB gain values to device-independent temperature and tint values.
- [- deviceWhiteBalanceGainsForChromaticityValues:](<devicewhitebalancegains(for_)-9gdtw.md>) — Converts device-independent chromaticity values to device-specific white balance RGB gain values.
- [WhiteBalanceGains](whitebalancegains.md) — A structure that defines RGB white balance gain values.
- [WhiteBalanceChromaticityValues](whitebalancechromaticityvalues.md) — A structure that defines CIE 1931 xy chromaticity values.
- [WhiteBalanceTemperatureAndTintValues](whitebalancetemperatureandtintvalues.md) — A structure that defines temperature and tint values correlated to a white-balance color.
