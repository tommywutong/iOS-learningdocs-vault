---
title: 'locationManagerShouldDisplayHeadingCalibration(_:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.15+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanagerdelegate/locationmanagershoulddisplayheadingcalibration(_:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanagershoulddisplayheadingcalibration(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanagerdelegate/locationmanagershoulddisplayheadingcalibration%28_%3A%29.json'
content_hash: 'sha256:e6d3e3c2bb9c685f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManagerDelegate](../cllocationmanagerdelegate.md)

# locationManagerShouldDisplayHeadingCalibration(_:)

<sub>Instance Method</sub>

Asks the delegate whether the heading calibration alert should be displayed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
optional func locationManagerShouldDisplayHeadingCalibration(_ manager: CLLocationManager) -> Bool
```

## Parameters

- `manager` — The location manager object coordinating the display of the heading calibration alert.

## Return Value

[true](../../swift/true.md) if you want to allow the heading calibration alert to be displayed; [false](../../swift/false.md) if you do not.

## Discussion

Core Location may call this method in an effort to calibrate the onboard hardware used to determine heading values. Typically, Core Location calls this method at the following times:

- The first time heading updates are ever requested
- When Core Location observes a significant change in magnitude or inclination of the observed magnetic field

If you return [true](../../swift/true.md) from this method, Core Location displays the heading calibration alert on top of the current window immediately. The calibration alert prompts the user to move the device in a particular pattern so that Core Location can distinguish between the Earth’s magnetic field and any local magnetic fields. The alert remains visible until calibration is complete or until you explicitly dismiss it by calling the [- dismissHeadingCalibrationDisplay](<../cllocationmanager/dismissheadingcalibrationdisplay().md>) method. In the latter case, you can use this method to set up a timer and dismiss the interface after a specified amount of time has elapsed.

> [!note] Note
> The calibration process is able to filter out only those magnetic fields that move with the device. To calibrate a device that is near other sources of magnetic interference, the user must either move the device away from the source or move the source in conjunction with the device during the calibration process.

If you return [false](../../swift/false.md) from this method or do not provide an implementation for it in your delegate, Core Location does not display the heading calibration alert. Even if the alert is not displayed, calibration can still occur naturally when any interfering magnetic fields move away from the device. However, if the device is unable to calibrate itself for any reason, the value in the [headingAccuracy](../clheading/headingaccuracy.md) property of any subsequent events will reflect the uncalibrated readings.

## See Also

### Receiving heading updates

- [- locationManager:didUpdateHeading:](<locationmanager(__didupdateheading_).md>) — Tells the delegate that the location manager received updated heading information.
