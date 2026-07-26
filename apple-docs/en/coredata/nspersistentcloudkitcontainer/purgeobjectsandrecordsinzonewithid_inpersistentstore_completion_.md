---
title: 'purgeObjectsAndRecordsInZoneWithID:inPersistentStore:completion:'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentcloudkitcontainer/purgeobjectsandrecordsinzonewithid:inpersistentstore:completion:'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/purgeobjectsandrecordsinzonewithid:inpersistentstore:completion:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainer/purgeobjectsandrecordsinzonewithid%3Ainpersistentstore%3Acompletion%3A.json'
content_hash: 'sha256:6e3505657e62ef18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainer](../nspersistentcloudkitcontainer.md)

# purgeObjectsAndRecordsInZoneWithID:inPersistentStore:completion:

<sub>Instance Method</sub>

Deletes all CloudKit records in the specified record zone, along with their corresponding managed objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) purgeObjectsAndRecordsInZoneWithID:(CKRecordZoneID *) zoneID inPersistentStore:(NSPersistentStore *) persistentStore completion:(void (^)(CKRecordZoneID *purgedZoneID, NSError *purgeError)) completion;
```

## Parameters

- `zoneID` — The ID of the record zone to purge.

- `persistentStore` — The persistent store that manages the CloudKit database containing the record zone. Use `nil` to attempt the purge in each of the container’s persistent stores that manages a CloudKit database.

- `completion` — The handler to invoke after Core Data purges the CloudKit records and managed objects.

## Discussion

The `completion` callback returns no value and takes the following parameters:

- The ID of the purged record zone, or `nil` if the purge fails.
- An error object that contains information about a problem, or `nil` if Core Data successfully purges the record zone.

If `persistentStore` is `nil`, the method invokes the completion handler once for each of the persistent container’s stores that manages a CloudKit database.
