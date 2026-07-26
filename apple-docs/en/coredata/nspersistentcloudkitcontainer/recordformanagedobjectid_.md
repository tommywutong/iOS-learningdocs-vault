---
title: 'recordForManagedObjectID:'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcloudkitcontainer/recordformanagedobjectid:'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/recordformanagedobjectid:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainer/recordformanagedobjectid%3A.json'
content_hash: 'sha256:92d64c50d8c9cebd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainer](../nspersistentcloudkitcontainer.md)

# recordForManagedObjectID:

<sub>Instance Method</sub>

Returns the CloudKit record for the specified managed object ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (CKRecord *) recordForManagedObjectID:(NSManagedObjectID *) managedObjectID;
```

## Parameters

- `managedObjectID` — The ID of the managed object.

## Return Value

An instance of [CKRecord](../../cloudkit/ckrecord.md) if the managed object has an underlying CloudKit record; otherwise, `nil`.

## See Also

### Accessing Records

- [recordsForManagedObjectIDs:](recordsformanagedobjectids_.md) — Returns a dictionary that contains the CloudKit records for the specified managed object IDs.
- [recordIDForManagedObjectID:](recordidformanagedobjectid_.md) — Returns the CloudKit record ID for the specified managed object ID.
- [recordIDsForManagedObjectIDs:](recordidsformanagedobjectids_.md) — Returns a dictionary that contains the CloudKit record IDs for the specified managed object IDs.
