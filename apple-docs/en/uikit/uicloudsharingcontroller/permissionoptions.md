---
title: UICloudSharingController.PermissionOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicloudsharingcontroller/permissionoptions
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/permissionoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingcontroller/permissionoptions.json'
content_hash: 'sha256:f65ef0396cf0e338'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICloudSharingController](../uicloudsharingcontroller.md)

# UICloudSharingController.PermissionOptions

<sub>Structure</sub>

A set of options that determine the permission options available to the user when viewing the Cloud sharing controller screens.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct PermissionOptions
```

## Overview

These options are used when setting the [availablePermissions](availablepermissions.md) property on the [UICloudSharingController](../uicloudsharingcontroller.md) instance. This property determines which permission options are presented to the user in the controller’s user interface.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [UICloudSharingPermissionAllowPublic](permissionoptions/allowpublic.md) — The option that grants access to anyone who has the share link.
- [UICloudSharingPermissionAllowPrivate](permissionoptions/allowprivate.md) — The option that restricts access to people who have been invited.
- [UICloudSharingPermissionAllowReadOnly](permissionoptions/allowreadonly.md) — The option that gives participants read-only permission to the shared data.
- [UICloudSharingPermissionAllowReadWrite](permissionoptions/allowreadwrite.md) — The option that gives participants read/write permission to the shared data.

### Initializers

- [init(rawValue:)](<permissionoptions/init(rawvalue_).md>) — Creates a new permission option set with the given raw integer value.

## See Also

### Configuring the permissions

- [availablePermissions](availablepermissions.md) — A combination of permission and access options made available to the user when viewing screens presented by the CloudKit sharing controller.
