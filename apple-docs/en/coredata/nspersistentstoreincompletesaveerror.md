---
title: NSPersistentStoreIncompleteSaveError
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoreincompletesaveerror
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoreincompletesaveerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoreincompletesaveerror.json'
content_hash: 'sha256:a1cbf8675516df13'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreIncompleteSaveError

<sub>Global Variable</sub>

Error code to denote that one or more of the stores returned an error during a save operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSPersistentStoreIncompleteSaveError: Int { get }
```

## Discussion

The stores or objects that failed are in the corresponding user info dictionary of the `NSError` object.

## See Also

### Error codes

- [NSCoreDataError](nscoredataerror.md) — An error code that indicates a nonspecific Core Data error.
- [NSEntityMigrationPolicyError](nsentitymigrationpolicyerror.md) — An error code that indicates a migration failure during processing of an entity migration policy.
- [NSExternalRecordImportError](nsexternalrecordimporterror.md) — Error code to denote a general error encountered while importing external records.
- [NSInferredMappingModelError](nsinferredmappingmodelerror.md) — Error code to denote a problem with the creation of an inferred mapping model.
- [NSManagedObjectConstraintMergeError](nsmanagedobjectconstraintmergeerror.md) — Error code to denote a problem with the merging of instances of a managed object.
- [NSManagedObjectConstraintValidationError](nsmanagedobjectconstraintvalidationerror.md) — Error code to denote a problem with the validation of a managed object.
- [NSManagedObjectContextLockingError](nsmanagedobjectcontextlockingerror.md) — Error code to denote an inability to acquire a lock in a managed object context.
- [NSManagedObjectExternalRelationshipError](nsmanagedobjectexternalrelationshiperror.md) — Error code to denote that an object being saved has a relationship containing an object from another store.
- [NSManagedObjectMergeError](nsmanagedobjectmergeerror.md) — Error code to denote that a merge policy failed—Core Data is unable to complete merging.
- [NSManagedObjectModelReferenceNotFoundError](nsmanagedobjectmodelreferencenotfounderror.md) — An error code that indicates Core Data isn’t able to find or instantiate the referenced object model.
- [NSManagedObjectReferentialIntegrityError](nsmanagedobjectreferentialintegrityerror.md) — Error code to denote an attempt to fire a fault pointing to an object that does not exist.
- [NSManagedObjectValidationError](nsmanagedobjectvalidationerror.md) — Error code to denote a generic validation error.
- [NSMigrationCancelledError](nsmigrationcancellederror.md) — Error code to denote that migration failed due to manual cancellation.
- [NSMigrationConstraintViolationError](nsmigrationconstraintviolationerror.md) — Error code to denote a problem with the validation of a managed object during a migration.
- [NSMigrationError](nsmigrationerror.md) — Error code to denote a general migration error.
