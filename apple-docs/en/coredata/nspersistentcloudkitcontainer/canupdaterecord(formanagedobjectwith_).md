---
title: 'canUpdateRecord(forManagedObjectWith:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcloudkitcontainer/canupdaterecord(formanagedobjectwith:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/canupdaterecord(formanagedobjectwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainer/canupdaterecord%28formanagedobjectwith%3A%29.json'
content_hash: 'sha256:b35d7cf3f4bd6850'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainer](../nspersistentcloudkitcontainer.md)

# canUpdateRecord(forManagedObjectWith:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the user can modify the managed object’s underlying CloudKit record.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func canUpdateRecord(forManagedObjectWith objectID: NSManagedObjectID) -> Bool
```

## Parameters

- `objectID` — The ID of the managed object.

## Return Value

[true](../../swift/true.md) if the user can modify the CloudKit record; otherwise, [false](../../swift/false.md).

## Discussion

This method returns [true](../../swift/true.md) if [- canModifyManagedObjectsInStore:](<canmodifymanagedobjects(in_).md>) returns [true](../../swift/true.md) and any of the following conditions are true:

- `objectID` is a temporary object identifier.
- The persistent store that contains the managed object isn’t using CloudKit.
- The persistent store manages the user’s private database.
- The persistent store manages the public database, and the user owns the underlying record or Core Data has yet to save the managed object to iCloud.
- The persistent store manages the shared database, and the user has the necessary permissions to update the managed object’s underlying record. For more information, see [CKShare.ParticipantPermission](../../cloudkit/ckshare/participantpermission.md).

## See Also

### Checking Permissions

- [- canDeleteRecordForManagedObjectWithID:](<candeleterecord(formanagedobjectwith_).md>) — Returns a Boolean value that indicates whether the user can delete the managed object’s underlying CloudKit record.
- [- canModifyManagedObjectsInStore:](<canmodifymanagedobjects(in_).md>) — Returns a Boolean value that indicates whether the user can modify the specified persistent store.
