---
title: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/whitebalancetemperatureandtintvalues
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancetemperatureandtintvalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/whitebalancetemperatureandtintvalues.json'
content_hash: 'sha256:ebb52f474a372236'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.WhiteBalanceTemperatureAndTintValues

<sub>Structure</sub>

A structure that defines temperature and tint values correlated to a white-balance color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
struct WhiteBalanceTemperatureAndTintValues
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Sendable](../../swift/sendable.md)

## Topics

### Accessing standard values

- [AVCaptureWhiteBalanceTemperatureAndTintValuesCloudy](whitebalancetemperatureandtintvalues/cloudy.md) — Temperature and tint values ideal for scenes illuminated with natural cloudy daylight.
- [AVCaptureWhiteBalanceTemperatureAndTintValuesDaylight](whitebalancetemperatureandtintvalues/daylight.md) — Temperature and tint values ideal for scenes illuminated with natural daylight.
- [AVCaptureWhiteBalanceTemperatureAndTintValuesFluorescent](whitebalancetemperatureandtintvalues/fluorescent.md) — Temperature and tint values ideal for scenes illuminated with a fluorescent light source.
- [AVCaptureWhiteBalanceTemperatureAndTintValuesShadow](whitebalancetemperatureandtintvalues/shadow.md) — Temperature and tint values ideal for scenes illuminated with daylight but in heavy shade.
- [AVCaptureWhiteBalanceTemperatureAndTintValuesTungsten](whitebalancetemperatureandtintvalues/tungsten.md) — Temperature and tint values ideal for scenes illuminated with a tungsten light source.

### Creating temperature and tint values

- [init()](<whitebalancetemperatureandtintvalues/init().md>) — Creates a default value.
- [init(temperature:tint:)](<whitebalancetemperatureandtintvalues/init(temperature_tint_).md>) — Creates a structure with a white balance temperature and tint.

### Inspecting the values

- [temperature](whitebalancetemperatureandtintvalues/temperature.md) — The white balance color correlated temperature in kelvin.
- [tint](whitebalancetemperatureandtintvalues/tint.md) — The white balance tint value in the range of `-150.0` through `+150.0`.

## See Also

### Performing conversions

- [- chromaticityValuesForDeviceWhiteBalanceGains:](<chromaticityvalues(for_).md>) — Converts device-specific white balance RGB gain values to device-independent chromaticity values.
- [- temperatureAndTintValuesForDeviceWhiteBalanceGains:](<temperatureandtintvalues(for_).md>) — Converts device-specific white balance RGB gain values to device-independent temperature and tint values.
- [- deviceWhiteBalanceGainsForChromaticityValues:](<devicewhitebalancegains(for_)-9gdtw.md>) — Converts device-independent chromaticity values to device-specific white balance RGB gain values.
- [- deviceWhiteBalanceGainsForTemperatureAndTintValues:](<devicewhitebalancegains(for_)-3wtsa.md>) — Converts device-independent temperature and tint values to device-specific white balance RGB gain values.
- [WhiteBalanceGains](whitebalancegains.md) — A structure that defines RGB white balance gain values.
- [WhiteBalanceChromaticityValues](whitebalancechromaticityvalues.md) — A structure that defines CIE 1931 xy chromaticity values.
