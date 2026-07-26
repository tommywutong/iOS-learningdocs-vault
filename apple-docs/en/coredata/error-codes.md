---
title: Validation Error Codes
framework: Core Data
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/error-codes
source_url: 'https://developer.apple.com/documentation/coredata/error-codes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/error-codes.json'
content_hash: 'sha256:32ceec7c5e71b24a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md) · [Core Data Constants](core-data-constants.md)

# Validation Error Codes

<sub>API Collection</sub>

Error codes relating to the validation of managed objects.

## Topics

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
- [NSMigrationManagerDestinationStoreError](nsmigrationmanagerdestinationstoreerror.md) — Error code to denote that migration failed due to a problem with the destination data store.
- [NSMigrationManagerSourceStoreError](nsmigrationmanagersourcestoreerror.md) — Error code to denote that migration failed due to a problem with the source data store.
- [NSMigrationMissingMappingModelError](nsmigrationmissingmappingmodelerror.md) — Error code to denote that migration failed due to a missing mapping model.
- [NSMigrationMissingSourceModelError](nsmigrationmissingsourcemodelerror.md) — Error code to denote that migration failed due to a missing source data model.
- [NSPersistentHistoryTokenExpiredError](nspersistenthistorytokenexpirederror.md) — Error code to denote that the persistent history token has expired.
- [NSPersistentStoreCoordinatorLockingError](nspersistentstorecoordinatorlockingerror.md) — Error code to denote an inability to acquire a lock in a persistent store.
- [NSPersistentStoreIncompatibleSchemaError](nspersistentstoreincompatibleschemaerror.md) — Error code to denote that a persistent store returned an error for a save operation.
- [NSPersistentStoreIncompatibleVersionHashError](nspersistentstoreincompatibleversionhasherror.md) — Error code to denote that entity version hashes in the store are incompatible with the current managed object model.
- [NSPersistentStoreIncompleteSaveError](nspersistentstoreincompletesaveerror.md) — Error code to denote that one or more of the stores returned an error during a save operations.
- [NSPersistentStoreInvalidTypeError](nspersistentstoreinvalidtypeerror.md) — Error code to denote an unknown persistent store type/format/version.
- [NSPersistentStoreOpenError](nspersistentstoreopenerror.md) — Error code to denote an error occurred while attempting to open a persistent store.
- [NSPersistentStoreOperationError](nspersistentstoreoperationerror.md) — Error code to denote that a persistent store operation failed.
- [NSPersistentStoreSaveConflictsError](nspersistentstoresaveconflictserror.md) — Error code to denote that an unresolved merge conflict was encountered during a save. .
- [NSPersistentStoreSaveError](nspersistentstoresaveerror.md) — Error code to denote that a persistent store returned an error for a save operation.
- [NSPersistentStoreTimeoutError](nspersistentstoretimeouterror.md) — Error code to denote that Core Data failed to connect to a persistent store within the time specified by `NSPersistentStoreTimeoutOption`.
- [NSPersistentStoreTypeMismatchError](nspersistentstoretypemismatcherror.md) — Error code returned by a persistent store coordinator if a store is accessed that does not match the specified type.
- [NSPersistentStoreUnsupportedRequestTypeError](nspersistentstoreunsupportedrequesttypeerror.md) — Error code to denote that an `NSPersistentStore` subclass was passed a request (an instance of [NSPersistentStoreRequest](nspersistentstorerequest.md)) that it did not understand.
- [NSSQLiteError](nssqliteerror.md) — Error code to denote a general SQLite error.
- [NSStagedMigrationBackwardMigrationError](nsstagedmigrationbackwardmigrationerror.md) — An error code that indicates a failed migration because of an attempt to migrate backward.
- [NSStagedMigrationFrameworkVersionMismatchError](nsstagedmigrationframeworkversionmismatcherror.md) — An error code that indicates a failed migration because the persistent store’s metadata doesn’t support staged lightweight migrations.
- [NSValidationInvalidURIError](nsvalidationinvalidurierror.md) — Error code to denote a problem with the validation of a URI property.
- [NSValidationMultipleErrorsError](nsvalidationmultipleerrorserror.md) — Error code to denote an error containing multiple validation errors.
- [NSValidationMissingMandatoryPropertyError](nsvalidationmissingmandatorypropertyerror.md) — Error code for a non-optional property with a nil value.
- [NSValidationRelationshipLacksMinimumCountError](nsvalidationrelationshiplacksminimumcounterror.md) — Error code to denote a to-many relationship with too few destination objects.
- [NSValidationRelationshipExceedsMaximumCountError](nsvalidationrelationshipexceedsmaximumcounterror.md) — Error code to denote a bounded to-many relationship with too many destination objects.
- [NSValidationRelationshipDeniedDeleteError](nsvalidationrelationshipdenieddeleteerror.md) — Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is non-empty.
- [NSValidationNumberTooLargeError](nsvalidationnumbertoolargeerror.md) — Error code to denote some numerical value is too large.
- [NSValidationNumberTooSmallError](nsvalidationnumbertoosmallerror.md) — Error code to denote some numerical value is too small.
- [NSValidationDateTooLateError](nsvalidationdatetoolateerror.md) — Error code to denote some date value is too late.
- [NSValidationDateTooSoonError](nsvalidationdatetoosoonerror.md) — Error code to denote some date value is too soon.
- [NSValidationInvalidDateError](nsvalidationinvaliddateerror.md) — Error code to denote some date value fails to match date pattern.
- [NSValidationStringTooLongError](nsvalidationstringtoolongerror.md) — Error code to denote some string value is too long.
- [NSValidationStringTooShortError](nsvalidationstringtooshorterror.md) — Error code to denote some string value is too short.
- [NSValidationStringPatternMatchingError](nsvalidationstringpatternmatchingerror.md) — Error code to denote some string value fails to match some pattern.

## See Also

### Errors

- [NSSQLiteErrorDomain](nssqliteerrordomain.md) — Domain for SQLite errors.
