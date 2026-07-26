---
title: allowReadWrite
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicloudsharingcontroller/permissionoptions/allowreadwrite
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/permissionoptions/allowreadwrite'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingcontroller/permissionoptions/allowreadwrite.json'
content_hash: 'sha256:65a96cc46a0857e6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICloudSharingController](../../uicloudsharingcontroller.md) · [PermissionOptions](../permissionoptions.md)

# allowReadWrite

<sub>Type Property</sub>

The option that gives participants read/write permission to the shared data.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var allowReadWrite: UICloudSharingController.PermissionOptions { get }
```

## Discussion

To give the user the option to allow other people to edit the shared data, include the [UICloudSharingPermissionAllowReadWrite](allowreadwrite.md) option when setting the [availablePermissions](../availablepermissions.md) property on the [UICloudSharingController](../../uicloudsharingcontroller.md) instance.

## See Also

### Constants

- [UICloudSharingPermissionAllowPublic](allowpublic.md) — The option that grants access to anyone who has the share link.
- [UICloudSharingPermissionAllowPrivate](allowprivate.md) — The option that restricts access to people who have been invited.
- [UICloudSharingPermissionAllowReadOnly](allowreadonly.md) — The option that gives participants read-only permission to the shared data.
