---
title: UICloudSharingPermissionStandard
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicloudsharingpermissionoptions/uicloudsharingpermissionstandard
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingpermissionoptions/uicloudsharingpermissionstandard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingpermissionoptions/uicloudsharingpermissionstandard.json'
content_hash: 'sha256:286d919a51e1f6e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [PermissionOptions](../uicloudsharingcontroller/permissionoptions.md)

# UICloudSharingPermissionStandard

<sub>Enumeration Case</sub>

The option that makes all user options available.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
UICloudSharingPermissionStandard
```

## Discussion

To tell the [UICloudSharingController](../uicloudsharingcontroller.md) instance to display all user options, set its [availablePermissions](../uicloudsharingcontroller/availablepermissions.md) property to [UICloudSharingPermissionStandard](uicloudsharingpermissionstandard.md).

The other [PermissionOptions](../uicloudsharingcontroller/permissionoptions.md) options override this option, so there’s no need to combine the other options with [UICloudSharingPermissionStandard](uicloudsharingpermissionstandard.md).

## See Also

### Constants

- [UICloudSharingPermissionAllowPublic](../uicloudsharingcontroller/permissionoptions/allowpublic.md) — The option that grants access to anyone who has the share link.
- [UICloudSharingPermissionAllowPrivate](../uicloudsharingcontroller/permissionoptions/allowprivate.md) — The option that restricts access to people who have been invited.
- [UICloudSharingPermissionAllowReadOnly](../uicloudsharingcontroller/permissionoptions/allowreadonly.md) — The option that gives participants read-only permission to the shared data.
- [UICloudSharingPermissionAllowReadWrite](../uicloudsharingcontroller/permissionoptions/allowreadwrite.md) — The option that gives participants read/write permission to the shared data.
