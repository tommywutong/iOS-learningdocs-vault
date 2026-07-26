---
title: Merge Policies
framework: Core Data
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/merge-policies
source_url: 'https://developer.apple.com/documentation/coredata/merge-policies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/merge-policies.json'
content_hash: 'sha256:7e8f1d1c4c6619f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md) · [Conflict resolution](conflict-resolution.md) · [NSMergePolicy](nsmergepolicy.md)

# Merge Policies

<sub>API Collection</sub>

Define standard ways to handle conflicts during a save operation.

## Overview

`NSErrorMergePolicy` is the default policy. It is the only policy that requires action to correct any conflicts. The other policies make a save go through silently by making changes that follow rules specific to that policy.

## Topics

### Policies

- [NSErrorMergePolicy](nserrormergepolicy.md) — The default merge policy for all managed object contexts.
- [NSMergeByPropertyStoreTrumpMergePolicy](nsmergebypropertystoretrumpmergepolicy.md) — A property-based merge policy that applies external changes.
- [NSMergeByPropertyObjectTrumpMergePolicy](nsmergebypropertyobjecttrumpmergepolicy.md) — A property-based merge policy that applies in-memory changes.
- [NSOverwriteMergePolicy](nsoverwritemergepolicy.md) — A merge policy that overwrites the entire stored object.
- [NSRollbackMergePolicy](nsrollbackmergepolicy.md) — A merge policy that discards unsaved changes.
- [NSMergePolicyType](nsmergepolicytype.md) — Constants that define merge policy types.

## See Also

### Defining Merge Policies

- [errorMergePolicy](nsmergepolicy/error.md) — The default merge policy for all managed object contexts.
- [mergeByPropertyStoreTrumpMergePolicy](nsmergepolicy/mergebypropertystoretrump.md) — A property-based merge policy that applies external changes.
- [mergeByPropertyObjectTrumpMergePolicy](nsmergepolicy/mergebypropertyobjecttrump.md) — A property-based merge policy that applies in-memory changes.
- [overwriteMergePolicy](nsmergepolicy/overwrite.md) — A merge policy that overwrites the entire stored object.
- [rollbackMergePolicy](nsmergepolicy/rollback.md) — A merge policy that discards unsaved changes.
