---
title: 'recordIDsForManagedObjectIDs:'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcloudkitcontainer/recordidsformanagedobjectids:'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/recordidsformanagedobjectids:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainer/recordidsformanagedobjectids%3A.json'
content_hash: 'sha256:fdb40cb84d40a56f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainer](../nspersistentcloudkitcontainer.md)

# recordIDsForManagedObjectIDs:

<sub>Instance Method</sub>

Returns a dictionary that contains the CloudKit record IDs for the specified managed object IDs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSDictionary<NSManagedObjectID *,CKRecordID *> *) recordIDsForManagedObjectIDs:(NSArray<NSManagedObjectID *> *) managedObjectIDs;
```

## Parameters

- `managedObjectIDs` — An array of the managed object IDs.

## Return Value

A dictionary that uses `managedObjectIDs` as its keys, and the [CKRecord.ID](../../cloudkit/ckrecord/id.md) of each object’s underlying CloudKit record as its values. The dictionary excludes IDs that don’t have a CloudKit record.

## See Also

### Accessing Records

- [recordForManagedObjectID:](recordformanagedobjectid_.md) — Returns the CloudKit record for the specified managed object ID.
- [recordsForManagedObjectIDs:](recordsformanagedobjectids_.md) — Returns a dictionary that contains the CloudKit records for the specified managed object IDs.
- [recordIDForManagedObjectID:](recordidformanagedobjectid_.md) — Returns the CloudKit record ID for the specified managed object ID.
