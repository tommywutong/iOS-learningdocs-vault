---
title: 'continuityDevicePicker(_:didConnect:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepicker(_:didconnect:)'
source_url: 'https://developer.apple.com/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepicker(_:didconnect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate/continuitydevicepicker%28_%3Adidconnect%3A%29.json'
content_hash: 'sha256:21cf41c9f95152de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVContinuityDevicePickerViewControllerDelegate](../avcontinuitydevicepickerviewcontrollerdelegate.md)

# continuityDevicePicker(_:didConnect:)

<sub>Instance Method</sub>

Informs the delegate when a person selects and connects a continuity device to the system with a continuity device picker.

<sub>tvOS</sub>

```swift
optional func continuityDevicePicker(_ pickerViewController: AVContinuityDevicePickerViewController, didConnect device: AVContinuityDevice)
```

## Parameters

- `pickerViewController` — The continuity device picker that’s connecting `device` to the system.

- `device` — A continuity device that’s connecting to the system.

## See Also

### Responding to continuity device events

- [- continuityDevicePickerWillBeginPresenting:](<continuitydevicepickerwillbeginpresenting(__).md>) — Informs the delegate that a continuity device picker is about to present its UI so that a person can select and connect a continuity device.
- [- continuityDevicePickerDidCancel:](<continuitydevicepickerdidcancel(__).md>) — Informs the delegate when a person declines to select a continuity device by dismissing an app’s continuity device picker.
- [- continuityDevicePickerDidEndPresenting:](<continuitydevicepickerdidendpresenting(__).md>) — Informs the delegate that a continuity device picker is no longer presenting its UI to a person.
