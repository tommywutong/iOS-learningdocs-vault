---
title: 'init(preparationHandler:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+（17.0 起废弃）, iPadOS 10.0+（17.0 起废弃）, Mac Catalyst 13.1+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicloudsharingcontroller/init(preparationhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/init(preparationhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingcontroller/init%28preparationhandler%3A%29.json'
content_hash: 'sha256:2bf730afaa9ae8d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICloudSharingController](../uicloudsharingcontroller.md)

# init(preparationHandler:)

<sub>Initializer</sub>

Initializes the CloudKit sharing controller with a preparation handler intending to save a new share record.

> [!warning] Deprecated
> Use [- initWithActivityItemsConfiguration:](<../uiactivityviewcontroller/init(activityitemsconfiguration_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(preparationHandler: @escaping (UICloudSharingController, @escaping (CKShare?, CKContainer?, (any Error)?) -> Void) -> Void)
```

## Parameters

- `preparationHandler` — The block invoked by [UICloudSharingController](../uicloudsharingcontroller.md) when it is time for your application to save a newly created [CKShare](../../cloudkit/ckshare.md) record.

## Discussion

Use the [- initWithPreparationHandler:](<init(preparationhandler_).md>) initializer method to create a new [UICloudSharingController](../uicloudsharingcontroller.md) instance when the user who owns a [CKRecord](../../cloudkit/ckrecord.md) wants to share the record with other people. To determine if the record is shared, check its [share](../../cloudkit/ckrecord/share.md) property. If the property value is `nil`, the record is not shared, and this method is the one to use.

> [!important] Important
> You must initialize the controller with the correct initializer method. Do not use [- initWithPreparationHandler:](<init(preparationhandler_).md>) if the [CKRecord](../../cloudkit/ckrecord.md) is already shared. Likewise, do not use [- initWithShare:container:](<init(share_container_).md>) if the [CKRecord](../../cloudkit/ckrecord.md) is not shared. Using the wrong initializer leads to errors when saving the record.

The `preparationHandler:` provided to the initializer method is responsible for saving the new [CKShare](../../cloudkit/ckshare.md) record. The handler has two parameters:

- A reference to the [UICloudSharingController](../uicloudsharingcontroller.md) instance that called the preparation handler
- A reference to a completion block

After you save the new [CKShare](../../cloudkit/ckshare.md) record and its root record (the [CKRecord](../../cloudkit/ckrecord.md) representing the data to share) in the preparation handler, you call the completion block. Calling the completion block tells the [UICloudSharingController](../uicloudsharingcontroller.md) instance to continue with the invitation workflow.

For more information and sample code, see [Inviting participants to a new share](../uicloudsharingcontroller.md#Inviting-participants-to-a-new-share).

## See Also

### Creating the cloud sharing controller

- [- initWithShare:container:](<init(share_container_).md>) — Initializes the CloudKit sharing view controller with a CloudKit share record and container to manage participants and restrictions.
