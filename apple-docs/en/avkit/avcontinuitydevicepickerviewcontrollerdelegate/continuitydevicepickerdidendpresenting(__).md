---
title: 'continuityDevicePickerDidEndPresenting(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerdidendpresenting(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerdidendpresenting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerdidendpresenting%28_%3A%29.json'
content_hash: 'sha256:6db29f19ffac253c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVContinuityDevicePickerViewControllerDelegate](../avcontinuitydevicepickerviewcontrollerdelegate.md)

# continuityDevicePickerDidEndPresenting(_:)

<sub>Instance Method</sub>

Informs the delegate that a continuity device picker is no longer presenting its UI to a person.

<sub>tvOS</sub>

```swift
optional func continuityDevicePickerDidEndPresenting(_ pickerViewController: AVContinuityDevicePickerViewController)
```

## Parameters

- `pickerViewController` — The continuity device picker that’s informing the delegate.

## See Also

### Responding to continuity device events

- [- continuityDevicePickerWillBeginPresenting:](<continuitydevicepickerwillbeginpresenting(__).md>) — Informs the delegate that a continuity device picker is about to present its UI so that a person can select and connect a continuity device.
- [- continuityDevicePickerDidCancel:](<continuitydevicepickerdidcancel(__).md>) — Informs the delegate when a person declines to select a continuity device by dismissing an app’s continuity device picker.
- [- continuityDevicePicker:didConnectDevice:](<continuitydevicepicker(__didconnect_).md>) — Informs the delegate when a person selects and connects a continuity device to the system with a continuity device picker.
