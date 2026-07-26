---
title: 'canModifyManagedObjects(in:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcloudkitcontainer/canmodifymanagedobjects(in:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/canmodifymanagedobjects(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainer/canmodifymanagedobjects%28in%3A%29.json'
content_hash: 'sha256:54a0940aa332db80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainer](../nspersistentcloudkitcontainer.md)

# canModifyManagedObjects(in:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the user can modify the specified persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func canModifyManagedObjects(in store: NSPersistentStore) -> Bool
```

## Parameters

- `store` — The persistent store.

## Return Value

[true](../../swift/true.md) if the user can modify records in the persistent store’s CloudKit database; otherwise, [false](../../swift/false.md).

## Discussion

Use this method to determine whether the user is able to write any records to the CloudKit database. To find out if the user can modify a specific object, use the [- canUpdateRecordForManagedObjectWithID:](<canupdaterecord(formanagedobjectwith_).md>) and [- canDeleteRecordForManagedObjectWithID:](<candeleterecord(formanagedobjectwith_).md>) methods instead.

This method always returns [true](../../swift/true.md) for persistent stores that manage the user’s private CloudKit database.

## See Also

### Checking Permissions

- [- canUpdateRecordForManagedObjectWithID:](<canupdaterecord(formanagedobjectwith_).md>) — Returns a Boolean value that indicates whether the user can modify the managed object’s underlying CloudKit record.
- [- canDeleteRecordForManagedObjectWithID:](<candeleterecord(formanagedobjectwith_).md>) — Returns a Boolean value that indicates whether the user can delete the managed object’s underlying CloudKit record.
