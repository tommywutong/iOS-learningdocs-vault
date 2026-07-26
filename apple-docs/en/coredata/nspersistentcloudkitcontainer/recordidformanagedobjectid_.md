---
title: 'recordIDForManagedObjectID:'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcloudkitcontainer/recordidformanagedobjectid:'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/recordidformanagedobjectid:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainer/recordidformanagedobjectid%3A.json'
content_hash: 'sha256:75dcdc3fa5cebb6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainer](../nspersistentcloudkitcontainer.md)

# recordIDForManagedObjectID:

<sub>Instance Method</sub>

Returns the CloudKit record ID for the specified managed object ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (CKRecordID *) recordIDForManagedObjectID:(NSManagedObjectID *) managedObjectID;
```

## Parameters

- `managedObjectID` — The ID of the managed object.

## Return Value

An instance of [CKRecord.ID](../../cloudkit/ckrecord/id.md) if the managed object has an underlying CloudKit record; otherwise, `nil`.

## See Also

### Accessing Records

- [recordForManagedObjectID:](recordformanagedobjectid_.md) — Returns the CloudKit record for the specified managed object ID.
- [recordsForManagedObjectIDs:](recordsformanagedobjectids_.md) — Returns a dictionary that contains the CloudKit records for the specified managed object IDs.
- [recordIDsForManagedObjectIDs:](recordidsformanagedobjectids_.md) — Returns a dictionary that contains the CloudKit record IDs for the specified managed object IDs.
