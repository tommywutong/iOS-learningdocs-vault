---
title: allowPrivate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicloudsharingcontroller/permissionoptions/allowprivate
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/permissionoptions/allowprivate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingcontroller/permissionoptions/allowprivate.json'
content_hash: 'sha256:9262e03aa571d72b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICloudSharingController](../../uicloudsharingcontroller.md) · [PermissionOptions](../permissionoptions.md)

# allowPrivate

<sub>Type Property</sub>

The option that restricts access to people who have been invited.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var allowPrivate: UICloudSharingController.PermissionOptions { get }
```

## Discussion

To give the user the option to limit access to people who have been invited, include the [UICloudSharingPermissionAllowPrivate](allowprivate.md) option when setting the [availablePermissions](../availablepermissions.md) property on the [UICloudSharingController](../../uicloudsharingcontroller.md) instance.

> [!note] Note
> When inviting someone, the user must provide that person’s email address or phone number. This is how the person is identified when accepting the invitation.

## See Also

### Constants

- [UICloudSharingPermissionAllowPublic](allowpublic.md) — The option that grants access to anyone who has the share link.
- [UICloudSharingPermissionAllowReadOnly](allowreadonly.md) — The option that gives participants read-only permission to the shared data.
- [UICloudSharingPermissionAllowReadWrite](allowreadwrite.md) — The option that gives participants read/write permission to the shared data.
