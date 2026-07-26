---
title: 'continuityDevicePickerWillBeginPresenting(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerwillbeginpresenting(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerwillbeginpresenting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerwillbeginpresenting%28_%3A%29.json'
content_hash: 'sha256:96cf634c32f6f8b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVContinuityDevicePickerViewControllerDelegate](../avcontinuitydevicepickerviewcontrollerdelegate.md)

# continuityDevicePickerWillBeginPresenting(_:)

<sub>Instance Method</sub>

Informs the delegate that a continuity device picker is about to present its UI so that a person can select and connect a continuity device.

<sub>tvOS</sub>

```swift
optional func continuityDevicePickerWillBeginPresenting(_ pickerViewController: AVContinuityDevicePickerViewController)
```

## Parameters

- `pickerViewController` — The continuity device picker that’s informing the delegate.

## See Also

### Responding to continuity device events

- [- continuityDevicePickerDidCancel:](<continuitydevicepickerdidcancel(__).md>) — Informs the delegate when a person declines to select a continuity device by dismissing an app’s continuity device picker.
- [- continuityDevicePicker:didConnectDevice:](<continuitydevicepicker(__didconnect_).md>) — Informs the delegate when a person selects and connects a continuity device to the system with a continuity device picker.
- [- continuityDevicePickerDidEndPresenting:](<continuitydevicepickerdidendpresenting(__).md>) — Informs the delegate that a continuity device picker is no longer presenting its UI to a person.
