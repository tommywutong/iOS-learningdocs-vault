---
title: White balance
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capture-device-white-balance
source_url: 'https://developer.apple.com/documentation/avfoundation/capture-device-white-balance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capture-device-white-balance.json'
content_hash: 'sha256:c42fbb74b271ce5e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Capture setup](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# White balance

<sub>API Collection</sub>

Configure the automatic white balance behavior of a camera, or manually control white balance settings.

## Topics

### Configuring automatic white balance

- [- isWhiteBalanceModeSupported:](<avcapturedevice/iswhitebalancemodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the specified white balance mode.
- [whiteBalanceMode](avcapturedevice/whitebalancemode-swift.property.md) — The current white balance mode.
- [WhiteBalanceMode](avcapturedevice/whitebalancemode-swift.enum.md) — Constants to specify the white balance mode of a capture device.

### Monitoring white balance changes

- [adjustingWhiteBalance](avcapturedevice/isadjustingwhitebalance.md) — A Boolean value that indicates whether the device is currently adjusting the white balance.

### Inspecting gain levels

- [deviceWhiteBalanceGains](avcapturedevice/devicewhitebalancegains.md) — The current device-specific RGB white balance gain values in use.
- [grayWorldDeviceWhiteBalanceGains](avcapturedevice/grayworlddevicewhitebalancegains.md) — The current device-specific white balance values required for a neutral gray white point.
- [maxWhiteBalanceGain](avcapturedevice/maxwhitebalancegain.md) — The maximum supported value to which you can set a color channel.

### Performing conversions

- [- chromaticityValuesForDeviceWhiteBalanceGains:](<avcapturedevice/chromaticityvalues(for_).md>) — Converts device-specific white balance RGB gain values to device-independent chromaticity values.
- [- temperatureAndTintValuesForDeviceWhiteBalanceGains:](<avcapturedevice/temperatureandtintvalues(for_).md>) — Converts device-specific white balance RGB gain values to device-independent temperature and tint values.
- [- deviceWhiteBalanceGainsForChromaticityValues:](<avcapturedevice/devicewhitebalancegains(for_)-9gdtw.md>) — Converts device-independent chromaticity values to device-specific white balance RGB gain values.
- [- deviceWhiteBalanceGainsForTemperatureAndTintValues:](<avcapturedevice/devicewhitebalancegains(for_)-3wtsa.md>) — Converts device-independent temperature and tint values to device-specific white balance RGB gain values.
- [WhiteBalanceGains](avcapturedevice/whitebalancegains.md) — A structure that defines RGB white balance gain values.
- [WhiteBalanceChromaticityValues](avcapturedevice/whitebalancechromaticityvalues.md) — A structure that defines CIE 1931 xy chromaticity values.
- [WhiteBalanceTemperatureAndTintValues](avcapturedevice/whitebalancetemperatureandtintvalues.md) — A structure that defines temperature and tint values correlated to a white-balance color.

### Setting white balance manually

- [lockingWhiteBalanceWithCustomDeviceGainsSupported](avcapturedevice/islockingwhitebalancewithcustomdevicegainssupported.md) — A Boolean value that indicates whether the device supports locking white balance to specific gain values.
- [- setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:](<avcapturedevice/setwhitebalancemodelocked(with_completionhandler_).md>) — Sets the white balance to locked mode with the specified white balance gains.
- [- setWhiteBalanceModeLockedWithDeviceWhiteBalanceTemperatureAndTintValues:completionHandler:](<avcapturedevice/setwhitebalancemodelocked(whitebalancetemperatureandtintvalues_handler_).md>) — Sets white balance to locked mode with explicit temperature and tint values.

## See Also

### Configuring camera hardware

- [- lockForConfiguration:](<avcapturedevice/lockforconfiguration().md>) — Requests exclusive access to configure device hardware properties.
- [- unlockForConfiguration](<avcapturedevice/unlockforconfiguration().md>) — Releases exclusive control over device hardware properties.
- [subjectAreaChangeMonitoringEnabled](avcapturedevice/issubjectareachangemonitoringenabled.md) — A Boolean value that indicates whether the device monitors the subject area for changes.
- [AVCaptureDeviceSubjectAreaDidChangeNotification](avcapturedevice/subjectareadidchangenotification.md) — A notification the system posts when a capture device detects a substantial change to the video subject area.
- [Formats](capture-device-formats.md) — Configure capture formats and camera frame rates.
- [Focus](capture-device-focus.md) — Configure the automatic focus behavior of a camera, or manually set its lens position.
- [Exposure](capture-device-exposure.md) — Configure the automatic exposure behavior of a camera, or manually control its exposure settings.
- [Lighting](capture-device-lighting.md) — Configure the device flash, torch, and low light settings.
- [Color](capture-device-color.md) — Manage HDR and color space settings for a device.
- [Zoom](capture-device-zoom.md) — Configure device zooming behavior and inspect hardware capabilities.
