---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicloudsharingcontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingcontroller/delegate.json'
content_hash: 'sha256:43e7bed4ed1497d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICloudSharingController](../uicloudsharingcontroller.md)

# delegate

<sub>Instance Property</sub>

A reference to an object that conforms to the CloudKit sharing controller delegate protocol.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UICloudSharingControllerDelegate)? { get set }
```

## Discussion

The [UICloudSharingController](../uicloudsharingcontroller.md) instance can interact with your app by way of a delegate object (an object that conforms to the [UICloudSharingControllerDelegate](../uicloudsharingcontrollerdelegate.md) protocol). If you provide a delegate object to the controller, the controller can notify your app of status changes to the [CKShare](../../cloudkit/ckshare.md) record that happen while the user interacts with the controller’s user interface. The controller can also ask the delegate object for app-specific settings, such as a title, for display in the controller’s user interface.

Although providing a delegate object is not required, doing so ensures that, at a minimum, a meaningful title is displayed in the controller’s user interface.

## See Also

### Customizing the cloud sharing controller behavior

- [UICloudSharingControllerDelegate](../uicloudsharingcontrollerdelegate.md) — The protocol you implement to provide additional information to, and receive notifications from, the CloudKit sharing controller.
