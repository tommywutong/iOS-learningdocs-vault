---
title: 'continuityDevicePickerDidCancel(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerdidcancel(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerdidcancel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepickerdidcancel%28_%3A%29.json'
content_hash: 'sha256:8b1f258ccaa4d2c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVContinuityDevicePickerViewControllerDelegate](../avcontinuitydevicepickerviewcontrollerdelegate.md)

# continuityDevicePickerDidCancel(_:)

<sub>Instance Method</sub>

Informs the delegate when a person declines to select a continuity device by dismissing an app’s continuity device picker.

<sub>tvOS</sub>

```swift
optional func continuityDevicePickerDidCancel(_ pickerViewController: AVContinuityDevicePickerViewController)
```

## Parameters

- `pickerViewController` — The continuity device picker that’s informing the delegate.

## See Also

### Responding to continuity device events

- [- continuityDevicePickerWillBeginPresenting:](<continuitydevicepickerwillbeginpresenting(__).md>) — Informs the delegate that a continuity device picker is about to present its UI so that a person can select and connect a continuity device.
- [- continuityDevicePicker:didConnectDevice:](<continuitydevicepicker(__didconnect_).md>) — Informs the delegate when a person selects and connects a continuity device to the system with a continuity device picker.
- [- continuityDevicePickerDidEndPresenting:](<continuitydevicepickerdidendpresenting(__).md>) — Informs the delegate that a continuity device picker is no longer presenting its UI to a person.
