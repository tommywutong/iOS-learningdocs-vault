---
title: 'init(share:container:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicloudsharingcontroller/init(share:container:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicloudsharingcontroller/init(share:container:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicloudsharingcontroller/init%28share%3Acontainer%3A%29.json'
content_hash: 'sha256:cf94b6f3215c98fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICloudSharingController](../uicloudsharingcontroller.md)

# init(share:container:)

<sub>Initializer</sub>

Initializes the CloudKit sharing view controller with a CloudKit share record and container to manage participants and restrictions.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(share: CKShare, container: CKContainer)
```

## Parameters

- `share` — An instance of [CKShare](../../cloudkit/ckshare.md) that was previously saved.

- `container` — An instance of [CKContainer](../../cloudkit/ckcontainer.md) that contains the record that is shared.

## Discussion

Use the [- initWithShare:container:](<init(share_container_).md>) initializer method to create the [UICloudSharingController](../uicloudsharingcontroller.md) instance when the user who owns the [CKShare](../../cloudkit/ckshare.md) record wants to manage the participants and restrictions associated with the share. (For more information, see [Adding and removing participants from an existing share](../uicloudsharingcontroller.md#Adding-and-removing-participants-from-an-existing-share).) You also use this initializer method when users are participants who want to remove themselves from a share. (For more information, see [Viewing participants and leaving a share](../uicloudsharingcontroller.md#Viewing-participants-and-leaving-a-share).)

> [!important] Important
> You must initialize the controller with the correct initializer method. Do not use [- initWithPreparationHandler:](<init(preparationhandler_).md>) if the [CKRecord](../../cloudkit/ckrecord.md) is already shared. Likewise, do not use [- initWithShare:container:](<init(share_container_).md>) if the [CKRecord](../../cloudkit/ckrecord.md) is not shared. Using the wrong initializer leads to errors when saving the record.

[- initWithShare:container:](<init(share_container_).md>) requires a reference to the [CKShare](../../cloudkit/ckshare.md) instance associated with the [CKRecord](../../cloudkit/ckrecord.md) instance that represents the shared data. To retrieve the [CKShare](../../cloudkit/ckshare.md) instance, get the [share](../../cloudkit/ckrecord/share.md) property value (a [CKRecord.Reference](../../cloudkit/ckrecord/reference.md) instance) from the [CKRecord](../../cloudkit/ckrecord.md) instance. Then pass the [recordID](../../cloudkit/ckrecord/reference/recordid.md) from the [CKRecord.Reference](../../cloudkit/ckrecord/reference.md) instance to the [fetch(withRecordID:completionHandler:)](<../../cloudkit/ckdatabase/fetch(withrecordid_completionhandler_).md>) method on a [CKDatabase](../../cloudkit/ckdatabase.md) instance, as shown in the following code.

```objc
CKRecord *record = [self record];
CKReference *shareReference = [record share];
if (shareReference == nil) {
  return;
}
CKContainer *container = [CKContainer defaultContainer];
[[container privateCloudDatabase] fetchRecordWithID:[shareReference recordID] completionHandler:^(CKRecord * _Nullable record, NSError * _Nullable error) {
  
  if (record == nil) {
    NSLog(@"%@", [error localizedDescription]);
  } else if ([record isKindOfClass:[CKShare class]]) {
    CKShare *shareRecord = (CKShare *)record;
    NSLog(@"%@", [shareRecord URL]);
  }
  
}];
```

## See Also

### Creating the cloud sharing controller

- [- initWithPreparationHandler:](<init(preparationhandler_).md>) — Initializes the CloudKit sharing controller with a preparation handler intending to save a new share record. _(deprecated)_
