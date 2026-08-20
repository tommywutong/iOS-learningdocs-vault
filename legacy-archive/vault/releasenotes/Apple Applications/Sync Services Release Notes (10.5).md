---
title: Sync Services Release Notes (10.5)
apple_id: TP40004725
resource_type: Release Note
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/releasenotes/AppleApplications/RN_SyncServices/index.html
archived_at: '2026-07-18T02:50:20.851815Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Sync Services Release Notes (10.5)

> [!IMPORTANT]
> 

### Known Problems and Fixes

### Radar #3700924 [ISyncSession clientChangedRecordIdentifiers:] should be "atomic"

Clients cannot swap two identifiers of two records in one pass using `clientChangedRecordIdentifiers:`.

For example, if `clientChangedRecordIdentifiers:` is given the dictionary:

```
(
   a => b,
   b => a,
)
```

The two identifiers will not be swapped.

Workaround: Use two calls, and temporary IDs. First, remap B->TMPID2, and A->TMPID1. Then TMPID2->A and TMPID1->B.

### Radar #3928977 Support for strongly ordered relationships

Relationships whose Ordering key is "strong" do not cause an alert panel to appear when a conflict occurs. Order is still maintained, and the sync engine merges ordering conflicts. This behavior is identical to the behavior for relationships whose Ordering key is "weak".

### Radar #4427308 OriginalRelationshipTuple table should give way to a FormattedRelationshipTuple table

Clients which do not format relationships can get improved performance by setting the key "NeverFormatsRelationships" to true in their client description property list.

### Radar #4532551 ISDDataWrappers rely on the underlying file system to support hard links

The way weakly ordered relationships are handled has been changed slightly to give the original intended semantics of a weakly ordered list. Such merges should result in more predictable behaviour.

### Radar #4593540 A client should be able to immediately reuse a localid of an accepted deleted record

Clients can't delete a record, then re-use the deleted record's local ID within the same session.

Workaround: Remap the record to be deleted to a new local ID before deleting it. This frees the old record id so clients can rename a second record to the deleted local ID. For example, a client which wants to delete and/or accept a delete of a record with a local ID of "Phone1" and then rename the record with a local ID of "Phone2" to "Phone1" would do the following:

1. Remap "Phone1" to "temporaryID".
2. Delete "temporaryID".
3. Remap "Phone2" to "Phone1".

### Don’t use or sync some com.apple.contacts entities and properties

The following additions to the `com.apple.contacts` schema are private and should not be synced:

- `originalImage` property in `com.apple.contacts.Contact`
- `imageTransformationInfo` property in `com.apple.contacts.Contact`
- `com.apple.contacts.ImageTransformationInfo` entity
