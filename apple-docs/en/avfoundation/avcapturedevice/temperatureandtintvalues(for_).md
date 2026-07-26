---
title: 'temperatureAndTintValues(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/temperatureandtintvalues(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/temperatureandtintvalues(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/temperatureandtintvalues%28for%3A%29.json'
content_hash: 'sha256:174c7dc6010df306'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# temperatureAndTintValues(for:)

<sub>Instance Method</sub>

Converts device-specific white balance RGB gain values to device-independent temperature and tint values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func temperatureAndTintValues(for whiteBalanceGains: AVCaptureDevice.WhiteBalanceGains) -> AVCaptureDevice.WhiteBalanceTemperatureAndTintValues
```

## Parameters

- `whiteBalanceGains` — The white balance gain values. You can’t specify a value of [AVCaptureWhiteBalanceGainsCurrent](currentwhitebalancegains.md).

## Return Value

A structure that contains device-independent values.

## Discussion

Each change in the structure supports values between `1.0` and [maxWhiteBalanceGain](maxwhitebalancegain.md). This method throws an exception if you specify an unsupported value.

## See Also

### Performing conversions

- [- chromaticityValuesForDeviceWhiteBalanceGains:](<chromaticityvalues(for_).md>) — Converts device-specific white balance RGB gain values to device-independent chromaticity values.
- [- deviceWhiteBalanceGainsForChromaticityValues:](<devicewhitebalancegains(for_)-9gdtw.md>) — Converts device-independent chromaticity values to device-specific white balance RGB gain values.
- [- deviceWhiteBalanceGainsForTemperatureAndTintValues:](<devicewhitebalancegains(for_)-3wtsa.md>) — Converts device-independent temperature and tint values to device-specific white balance RGB gain values.
- [WhiteBalanceGains](whitebalancegains.md) — A structure that defines RGB white balance gain values.
- [WhiteBalanceChromaticityValues](whitebalancechromaticityvalues.md) — A structure that defines CIE 1931 xy chromaticity values.
- [WhiteBalanceTemperatureAndTintValues](whitebalancetemperatureandtintvalues.md) — A structure that defines temperature and tint values correlated to a white-balance color.
