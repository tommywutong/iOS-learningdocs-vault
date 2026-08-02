---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/CoreData.html
archived_at: '2026-07-18T02:55:12.246442Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# CoreData Changes for Swift

### CoreData

Removed NSCocoaError.CoreDataErrorRemoved NSCocoaError.EntityMigrationPolicyErrorRemoved NSCocoaError.ExternalRecordImportErrorRemoved NSCocoaError.InferredMappingModelErrorRemoved NSCocoaError.ManagedObjectConstraintMergeErrorRemoved NSCocoaError.ManagedObjectContextLockingErrorRemoved NSCocoaError.ManagedObjectExternalRelationshipErrorRemoved NSCocoaError.ManagedObjectMergeErrorRemoved NSCocoaError.ManagedObjectReferentialIntegrityErrorRemoved NSCocoaError.ManagedObjectValidationErrorRemoved NSCocoaError.MigrationCancelledErrorRemoved NSCocoaError.MigrationErrorRemoved NSCocoaError.MigrationManagerDestinationStoreErrorRemoved NSCocoaError.MigrationManagerSourceStoreErrorRemoved NSCocoaError.MigrationMissingMappingModelErrorRemoved NSCocoaError.MigrationMissingSourceModelErrorRemoved NSCocoaError.PersistentStoreCoordinatorLockingErrorRemoved NSCocoaError.PersistentStoreIncompatibleSchemaErrorRemoved NSCocoaError.PersistentStoreIncompatibleVersionHashErrorRemoved NSCocoaError.PersistentStoreIncompvareSaveErrorRemoved NSCocoaError.PersistentStoreInvalidTypeErrorRemoved NSCocoaError.PersistentStoreOpenErrorRemoved NSCocoaError.PersistentStoreOperationErrorRemoved NSCocoaError.PersistentStoreSaveConflictsErrorRemoved NSCocoaError.PersistentStoreSaveErrorRemoved NSCocoaError.PersistentStoreTimeoutErrorRemoved NSCocoaError.PersistentStoreTypeMismatchErrorRemoved NSCocoaError.PersistentStoreUnsupportedRequestTypeErrorRemoved NSCocoaError.SQLiteErrorRemoved NSCocoaError.ValidationDateTooLateErrorRemoved NSCocoaError.ValidationDateTooSoonErrorRemoved NSCocoaError.ValidationInvalidDateErrorRemoved NSCocoaError.ValidationMissingMandatoryPropertyErrorRemoved NSCocoaError.ValidationMultipleErrorsErrorRemoved NSCocoaError.ValidationNumberTooLargeErrorRemoved NSCocoaError.ValidationNumberTooSmallErrorRemoved NSCocoaError.ValidationRelationshipDeniedDevareErrorRemoved NSCocoaError.ValidationRelationshipExceedsMaximumCountErrorRemoved NSCocoaError.ValidationRelationshipLacksMinimumCountErrorRemoved NSCocoaError.ValidationStringPatternMatchingErrorRemoved NSCocoaError.ValidationStringTooLongErrorRemoved NSCocoaError.ValidationStringTooShortErrorRemoved [NSManagedObject.contextShouldIgnoreUnmodeledPropertyChanges() -> Bool [class]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506727-contextshouldignoreunmodeledprop)Removed [NSPersistentStoreCoordinator.registeredStoreTypes() -> [String : NSValue] [class]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468870-registeredstoretypes)Added [CocoaError.affectedObjects](https://developer.apple.com/documentation/foundation/cocoaerror/2300160-affectedobjects)Added [CocoaError.affectedStores](https://developer.apple.com/documentation/foundation/cocoaerror/2300187-affectedstores)Added [CocoaError.coreData](https://developer.apple.com/documentation/foundation/cocoaerror/2506259-coredata)Added [CocoaError.coreDataError](https://developer.apple.com/documentation/foundation/cocoaerror/2300144-coredataerror)Added [CocoaError.entityMigrationPolicy](https://developer.apple.com/documentation/foundation/cocoaerror/2506226-entitymigrationpolicy)Added [CocoaError.entityMigrationPolicyError](https://developer.apple.com/documentation/foundation/cocoaerror/2300182-entitymigrationpolicyerror)Added [CocoaError.externalRecordImport](https://developer.apple.com/documentation/foundation/cocoaerror/2506296-externalrecordimport)Added [CocoaError.externalRecordImportError](https://developer.apple.com/documentation/foundation/cocoaerror/2300136-externalrecordimporterror)Added [CocoaError.inferredMappingModel](https://developer.apple.com/documentation/foundation/cocoaerror/2506289-inferredmappingmodel)Added [CocoaError.inferredMappingModelError](https://developer.apple.com/documentation/foundation/cocoaerror/2300185-inferredmappingmodelerror)Added [CocoaError.managedObjectConstraintMerge](https://developer.apple.com/documentation/foundation/cocoaerror/2506287-managedobjectconstraintmerge)Added [CocoaError.managedObjectConstraintMergeError](https://developer.apple.com/documentation/foundation/cocoaerror/2300132-managedobjectconstraintmergeerro)Added [CocoaError.managedObjectContextLocking](https://developer.apple.com/documentation/foundation/cocoaerror/2506254-managedobjectcontextlocking)Added [CocoaError.managedObjectContextLockingError](https://developer.apple.com/documentation/foundation/cocoaerror/2300163-managedobjectcontextlockingerror)Added [CocoaError.managedObjectExternalRelationship](https://developer.apple.com/documentation/foundation/cocoaerror/2506238-managedobjectexternalrelationshi)Added [CocoaError.managedObjectExternalRelationshipError](https://developer.apple.com/documentation/foundation/cocoaerror/2300148-managedobjectexternalrelationshi)Added [CocoaError.managedObjectMerge](https://developer.apple.com/documentation/foundation/cocoaerror/2506276-managedobjectmerge)Added [CocoaError.managedObjectMergeError](https://developer.apple.com/documentation/foundation/cocoaerror/2300161-managedobjectmergeerror)Added [CocoaError.managedObjectReferentialIntegrity](https://developer.apple.com/documentation/foundation/cocoaerror/2506231-managedobjectreferentialintegrit)Added [CocoaError.managedObjectReferentialIntegrityError](https://developer.apple.com/documentation/foundation/cocoaerror/2300125-managedobjectreferentialintegrit)Added [CocoaError.managedObjectValidation](https://developer.apple.com/documentation/foundation/cocoaerror/2506244-managedobjectvalidation)Added [CocoaError.managedObjectValidationError](https://developer.apple.com/documentation/foundation/cocoaerror/2300159-managedobjectvalidationerror)Added [CocoaError.migration](https://developer.apple.com/documentation/foundation/cocoaerror/2506263-migration)Added [CocoaError.migrationCancelled](https://developer.apple.com/documentation/foundation/cocoaerror/2506260-migrationcancelled)Added [CocoaError.migrationCancelledError](https://developer.apple.com/documentation/foundation/cocoaerror/2300188-migrationcancellederror)Added [CocoaError.migrationError](https://developer.apple.com/documentation/foundation/cocoaerror/2300149-migrationerror)Added [CocoaError.migrationManagerDestinationStore](https://developer.apple.com/documentation/foundation/cocoaerror/2506245-migrationmanagerdestinationstore)Added [CocoaError.migrationManagerDestinationStoreError](https://developer.apple.com/documentation/foundation/cocoaerror/2300130-migrationmanagerdestinationstore)Added [CocoaError.migrationManagerSourceStore](https://developer.apple.com/documentation/foundation/cocoaerror/2506252-migrationmanagersourcestore)Added [CocoaError.migrationManagerSourceStoreError](https://developer.apple.com/documentation/foundation/cocoaerror/2300170-migrationmanagersourcestoreerror)Added [CocoaError.migrationMissingMappingModel](https://developer.apple.com/documentation/foundation/cocoaerror/2506215-migrationmissingmappingmodel)Added [CocoaError.migrationMissingMappingModelError](https://developer.apple.com/documentation/foundation/cocoaerror/2300126-migrationmissingmappingmodelerro)Added [CocoaError.migrationMissingSourceModel](https://developer.apple.com/documentation/foundation/cocoaerror/2506256-migrationmissingsourcemodel)Added [CocoaError.migrationMissingSourceModelError](https://developer.apple.com/documentation/foundation/cocoaerror/2300169-migrationmissingsourcemodelerror)Added [CocoaError.persistentStoreCoordinatorLocking](https://developer.apple.com/documentation/foundation/cocoaerror/2506271-persistentstorecoordinatorlockin)Added [CocoaError.persistentStoreCoordinatorLockingError](https://developer.apple.com/documentation/foundation/cocoaerror/2300145-persistentstorecoordinatorlockin)Added [CocoaError.persistentStoreIncompatibleSchema](https://developer.apple.com/documentation/foundation/cocoaerror/2506251-persistentstoreincompatibleschem)Added [CocoaError.persistentStoreIncompatibleSchemaError](https://developer.apple.com/documentation/foundation/cocoaerror/2300196-persistentstoreincompatibleschem)Added [CocoaError.persistentStoreIncompatibleVersionHash](https://developer.apple.com/documentation/foundation/cocoaerror/2506278-persistentstoreincompatibleversi)Added [CocoaError.persistentStoreIncompatibleVersionHashError](https://developer.apple.com/documentation/foundation/cocoaerror/2300175-persistentstoreincompatibleversi)Added [CocoaError.persistentStoreIncompleteSave](https://developer.apple.com/documentation/foundation/cocoaerror/2506233-persistentstoreincompletesave)Added [CocoaError.persistentStoreIncompleteSaveError](https://developer.apple.com/documentation/foundation/cocoaerror/2506267-persistentstoreincompletesaveerr)Added [CocoaError.persistentStoreInvalidType](https://developer.apple.com/documentation/foundation/cocoaerror/2506250-persistentstoreinvalidtype)Added [CocoaError.persistentStoreInvalidTypeError](https://developer.apple.com/documentation/foundation/cocoaerror/2300198-persistentstoreinvalidtypeerror)Added [CocoaError.persistentStoreOpen](https://developer.apple.com/documentation/foundation/cocoaerror/2506297-persistentstoreopen)Added [CocoaError.persistentStoreOpenError](https://developer.apple.com/documentation/foundation/cocoaerror/2300137-persistentstoreopenerror)Added [CocoaError.persistentStoreOperation](https://developer.apple.com/documentation/foundation/cocoaerror/2506211-persistentstoreoperation)Added [CocoaError.persistentStoreOperationError](https://developer.apple.com/documentation/foundation/cocoaerror/2300201-persistentstoreoperationerror)Added [CocoaError.persistentStoreSave](https://developer.apple.com/documentation/foundation/cocoaerror/2506291-persistentstoresave)Added [CocoaError.persistentStoreSaveConflicts](https://developer.apple.com/documentation/foundation/cocoaerror/2506212-persistentstoresaveconflicts)Added [CocoaError.persistentStoreSaveConflicts](https://developer.apple.com/documentation/foundation/cocoaerror/2300191-persistentstoresaveconflicts)Added [CocoaError.persistentStoreSaveConflictsError](https://developer.apple.com/documentation/foundation/cocoaerror/2300195-persistentstoresaveconflictserro)Added [CocoaError.persistentStoreSaveError](https://developer.apple.com/documentation/foundation/cocoaerror/2300190-persistentstoresaveerror)Added [CocoaError.persistentStoreTimeout](https://developer.apple.com/documentation/foundation/cocoaerror/2506284-persistentstoretimeout)Added [CocoaError.persistentStoreTimeoutError](https://developer.apple.com/documentation/foundation/cocoaerror/2300139-persistentstoretimeouterror)Added [CocoaError.persistentStoreTypeMismatch](https://developer.apple.com/documentation/foundation/cocoaerror/2506221-persistentstoretypemismatch)Added [CocoaError.persistentStoreTypeMismatchError](https://developer.apple.com/documentation/foundation/cocoaerror/2300154-persistentstoretypemismatcherror)Added [CocoaError.persistentStoreUnsupportedRequestType](https://developer.apple.com/documentation/foundation/cocoaerror/2506298-persistentstoreunsupportedreques)Added [CocoaError.persistentStoreUnsupportedRequestTypeError](https://developer.apple.com/documentation/foundation/cocoaerror/2300176-persistentstoreunsupportedreques)Added [CocoaError.sqlite](https://developer.apple.com/documentation/foundation/cocoaerror/2506255-sqlite)Added [CocoaError.sqliteError](https://developer.apple.com/documentation/foundation/cocoaerror/2300186-sqliteerror)Added [CocoaError.validationDateTooLate](https://developer.apple.com/documentation/foundation/cocoaerror/2506281-validationdatetoolate)Added [CocoaError.validationDateTooLateError](https://developer.apple.com/documentation/foundation/cocoaerror/2300172-validationdatetoolateerror)Added [CocoaError.validationDateTooSoon](https://developer.apple.com/documentation/foundation/cocoaerror/2506279-validationdatetoosoon)Added [CocoaError.validationDateTooSoonError](https://developer.apple.com/documentation/foundation/cocoaerror/2300121-validationdatetoosoonerror)Added [CocoaError.validationInvalidDate](https://developer.apple.com/documentation/foundation/cocoaerror/2506272-validationinvaliddate)Added [CocoaError.validationInvalidDateError](https://developer.apple.com/documentation/foundation/cocoaerror/2300135-validationinvaliddateerror)Added [CocoaError.validationKey](https://developer.apple.com/documentation/foundation/cocoaerror/2300192-validationkey)Added [CocoaError.validationMissingMandatoryProperty](https://developer.apple.com/documentation/foundation/cocoaerror/2506234-validationmissingmandatoryproper)Added [CocoaError.validationMissingMandatoryPropertyError](https://developer.apple.com/documentation/foundation/cocoaerror/2300200-validationmissingmandatoryproper)Added [CocoaError.validationMultipleErrors](https://developer.apple.com/documentation/foundation/cocoaerror/2506282-validationmultipleerrors)Added [CocoaError.validationMultipleErrorsError](https://developer.apple.com/documentation/foundation/cocoaerror/2300120-validationmultipleerrorserror)Added [CocoaError.validationNumberTooLarge](https://developer.apple.com/documentation/foundation/cocoaerror/2506248-validationnumbertoolarge)Added [CocoaError.validationNumberTooLargeError](https://developer.apple.com/documentation/foundation/cocoaerror/2300119-validationnumbertoolargeerror)Added [CocoaError.validationNumberTooSmall](https://developer.apple.com/documentation/foundation/cocoaerror/2506225-validationnumbertoosmall)Added [CocoaError.validationNumberTooSmallError](https://developer.apple.com/documentation/foundation/cocoaerror/2300168-validationnumbertoosmallerror)Added [CocoaError.validationObject](https://developer.apple.com/documentation/foundation/cocoaerror/2300157-validationobject)Added [CocoaError.validationPredicate](https://developer.apple.com/documentation/foundation/cocoaerror/2300180-validationpredicate)Added [CocoaError.validationRelationshipDeniedDelete](https://developer.apple.com/documentation/foundation/cocoaerror/2506270-validationrelationshipdenieddele)Added [CocoaError.validationRelationshipDeniedDeleteError](https://developer.apple.com/documentation/foundation/cocoaerror/2506228-validationrelationshipdenieddele)Added [CocoaError.validationRelationshipExceedsMaximumCount](https://developer.apple.com/documentation/foundation/cocoaerror/2506213-validationrelationshipexceedsmax)Added [CocoaError.validationRelationshipExceedsMaximumCountError](https://developer.apple.com/documentation/foundation/cocoaerror/2300194-validationrelationshipexceedsmax)Added [CocoaError.validationRelationshipLacksMinimumCount](https://developer.apple.com/documentation/foundation/cocoaerror/2506219-validationrelationshiplacksminim)Added [CocoaError.validationRelationshipLacksMinimumCountError](https://developer.apple.com/documentation/foundation/cocoaerror/2300199-validationrelationshiplacksminim)Added [CocoaError.validationStringPatternMatching](https://developer.apple.com/documentation/foundation/cocoaerror/2506232-validationstringpatternmatching)Added [CocoaError.validationStringPatternMatchingError](https://developer.apple.com/documentation/foundation/cocoaerror/2300113-validationstringpatternmatchinge)Added [CocoaError.validationStringTooLong](https://developer.apple.com/documentation/foundation/cocoaerror/2506273-validationstringtoolong)Added [CocoaError.validationStringTooLongError](https://developer.apple.com/documentation/foundation/cocoaerror/2300114-validationstringtoolongerror)Added [CocoaError.validationStringTooShort](https://developer.apple.com/documentation/foundation/cocoaerror/2506223-validationstringtooshort)Added [CocoaError.validationStringTooShortError](https://developer.apple.com/documentation/foundation/cocoaerror/2300151-validationstringtooshorterror)Added [CocoaError.validationValue](https://developer.apple.com/documentation/foundation/cocoaerror/2300189-validationvalue)Added [CocoaError.Code.coreData](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506283-coredata)Added [CocoaError.Code.coreDataError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300184-coredataerror)Added [CocoaError.Code.entityMigrationPolicy](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506239-entitymigrationpolicy)Added [CocoaError.Code.entityMigrationPolicyError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300150-entitymigrationpolicyerror)Added [CocoaError.Code.externalRecordImport](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506277-externalrecordimport)Added [CocoaError.Code.externalRecordImportError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300155-externalrecordimporterror)Added [CocoaError.Code.inferredMappingModel](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506293-inferredmappingmodel)Added [CocoaError.Code.inferredMappingModelError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300171-inferredmappingmodelerror)Added [CocoaError.Code.managedObjectConstraintMerge](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506294-managedobjectconstraintmerge)Added [CocoaError.Code.managedObjectConstraintMergeError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300142-managedobjectconstraintmergeerro)Added [CocoaError.Code.managedObjectContextLocking](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506265-managedobjectcontextlocking)Added [CocoaError.Code.managedObjectContextLockingError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300131-managedobjectcontextlockingerror)Added [CocoaError.Code.managedObjectExternalRelationship](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506222-managedobjectexternalrelationshi)Added [CocoaError.Code.managedObjectExternalRelationshipError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300138-managedobjectexternalrelationshi)Added [CocoaError.Code.managedObjectMerge](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506295-managedobjectmerge)Added [CocoaError.Code.managedObjectMergeError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300164-managedobjectmergeerror)Added [CocoaError.Code.managedObjectReferentialIntegrity](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506218-managedobjectreferentialintegrit)Added [CocoaError.Code.managedObjectReferentialIntegrityError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300124-managedobjectreferentialintegrit)Added [CocoaError.Code.managedObjectValidation](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506275-managedobjectvalidation)Added [CocoaError.Code.managedObjectValidationError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300118-managedobjectvalidationerror)Added [CocoaError.Code.migration](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506261-migration)Added [CocoaError.Code.migrationCancelled](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506235-migrationcancelled)Added [CocoaError.Code.migrationCancelledError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300129-migrationcancellederror)Added [CocoaError.Code.migrationError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300167-migrationerror)Added [CocoaError.Code.migrationManagerDestinationStore](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506285-migrationmanagerdestinationstore)Added [CocoaError.Code.migrationManagerDestinationStoreError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300122-migrationmanagerdestinationstore)Added [CocoaError.Code.migrationManagerSourceStore](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506262-migrationmanagersourcestore)Added [CocoaError.Code.migrationManagerSourceStoreError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300146-migrationmanagersourcestoreerror)Added [CocoaError.Code.migrationMissingMappingModel](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506269-migrationmissingmappingmodel)Added [CocoaError.Code.migrationMissingMappingModelError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300140-migrationmissingmappingmodelerro)Added [CocoaError.Code.migrationMissingSourceModel](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506242-migrationmissingsourcemodel)Added [CocoaError.Code.migrationMissingSourceModelError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300158-migrationmissingsourcemodelerror)Added [CocoaError.Code.persistentStoreCoordinatorLocking](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506241-persistentstorecoordinatorlockin)Added [CocoaError.Code.persistentStoreCoordinatorLockingError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300143-persistentstorecoordinatorlockin)Added [CocoaError.Code.persistentStoreIncompatibleSchema](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506249-persistentstoreincompatibleschem)Added [CocoaError.Code.persistentStoreIncompatibleSchemaError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300178-persistentstoreincompatibleschem)Added [CocoaError.Code.persistentStoreIncompatibleVersionHash](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506246-persistentstoreincompatibleversi)Added [CocoaError.Code.persistentStoreIncompatibleVersionHashError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300202-persistentstoreincompatibleversi)Added [CocoaError.Code.persistentStoreIncompleteSave](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506237-persistentstoreincompletesave)Added [CocoaError.Code.persistentStoreIncompleteSaveError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506220-persistentstoreincompletesaveerr)Added [CocoaError.Code.persistentStoreInvalidType](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506216-persistentstoreinvalidtype)Added [CocoaError.Code.persistentStoreInvalidTypeError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300179-persistentstoreinvalidtypeerror)Added [CocoaError.Code.persistentStoreOpen](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506230-persistentstoreopen)Added [CocoaError.Code.persistentStoreOpenError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300162-persistentstoreopenerror)Added [CocoaError.Code.persistentStoreOperation](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506290-persistentstoreoperation)Added [CocoaError.Code.persistentStoreOperationError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300156-persistentstoreoperationerror)Added [CocoaError.Code.persistentStoreSave](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506229-persistentstoresave)Added [CocoaError.Code.persistentStoreSaveConflicts](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506264-persistentstoresaveconflicts)Added [CocoaError.Code.persistentStoreSaveConflictsError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300203-persistentstoresaveconflictserro)Added [CocoaError.Code.persistentStoreSaveError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300152-persistentstoresaveerror)Added [CocoaError.Code.persistentStoreTimeout](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506214-persistentstoretimeout)Added [CocoaError.Code.persistentStoreTimeoutError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300133-persistentstoretimeouterror)Added [CocoaError.Code.persistentStoreTypeMismatch](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506217-persistentstoretypemismatch)Added [CocoaError.Code.persistentStoreTypeMismatchError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300117-persistentstoretypemismatcherror)Added [CocoaError.Code.persistentStoreUnsupportedRequestType](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506253-persistentstoreunsupportedreques)Added [CocoaError.Code.persistentStoreUnsupportedRequestTypeError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300116-persistentstoreunsupportedreques)Added [CocoaError.Code.sqlite](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506257-sqlite)Added [CocoaError.Code.sqliteError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300127-sqliteerror)Added [CocoaError.Code.validationDateTooLate](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506280-validationdatetoolate)Added [CocoaError.Code.validationDateTooLateError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300134-validationdatetoolateerror)Added [CocoaError.Code.validationDateTooSoon](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506288-validationdatetoosoon)Added [CocoaError.Code.validationDateTooSoonError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300123-validationdatetoosoonerror)Added [CocoaError.Code.validationInvalidDate](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506274-validationinvaliddate)Added [CocoaError.Code.validationInvalidDateError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300174-validationinvaliddateerror)Added [CocoaError.Code.validationMissingMandatoryProperty](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506266-validationmissingmandatoryproper)Added [CocoaError.Code.validationMissingMandatoryPropertyError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300193-validationmissingmandatoryproper)Added [CocoaError.Code.validationMultipleErrors](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506224-validationmultipleerrors)Added [CocoaError.Code.validationMultipleErrorsError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300115-validationmultipleerrorserror)Added [CocoaError.Code.validationNumberTooLarge](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506243-validationnumbertoolarge)Added [CocoaError.Code.validationNumberTooLargeError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300153-validationnumbertoolargeerror)Added [CocoaError.Code.validationNumberTooSmall](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506292-validationnumbertoosmall)Added [CocoaError.Code.validationNumberTooSmallError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300166-validationnumbertoosmallerror)Added [CocoaError.Code.validationRelationshipDeniedDelete](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506227-validationrelationshipdenieddele)Added [CocoaError.Code.validationRelationshipDeniedDeleteError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506236-validationrelationshipdenieddele)Added [CocoaError.Code.validationRelationshipExceedsMaximumCount](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506240-validationrelationshipexceedsmax)Added [CocoaError.Code.validationRelationshipExceedsMaximumCountError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300181-validationrelationshipexceedsmax)Added [CocoaError.Code.validationRelationshipLacksMinimumCount](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506258-validationrelationshiplacksminim)Added [CocoaError.Code.validationRelationshipLacksMinimumCountError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300147-validationrelationshiplacksminim)Added [CocoaError.Code.validationStringPatternMatching](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506286-validationstringpatternmatching)Added [CocoaError.Code.validationStringPatternMatchingError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300165-validationstringpatternmatchinge)Added [CocoaError.Code.validationStringTooLong](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506268-validationstringtoolong)Added [CocoaError.Code.validationStringTooLongError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300141-validationstringtoolongerror)Added [CocoaError.Code.validationStringTooShort](https://developer.apple.com/documentation/foundation/cocoaerror/code/2506247-validationstringtooshort)Added [CocoaError.Code.validationStringTooShortError](https://developer.apple.com/documentation/foundation/cocoaerror/code/2300183-validationstringtooshorterror)Added [NSFetchRequest.execute() throws -> [ResultType]](https://developer.apple.com/documentation/coredata/nsfetchrequest/1640594-execute)Added [NSFetchRequestResult](https://developer.apple.com/documentation/coredata/nsfetchrequestresult)Added [NSManagedObject.contextShouldIgnoreUnmodeledPropertyChanges](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506727-contextshouldignoreunmodeledprop)Added [NSManagedObject.entity() -> NSEntityDescription [class]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1640588-entity)Added [NSManagedObject.fetchRequest() -> NSFetchRequest<NSFetchRequestResult> [class]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1640605-fetchrequest)Added [NSManagedObject.init(context: NSManagedObjectContext)](https://developer.apple.com/documentation/coredata/nsmanagedobject/1640602-init)Added [NSManagedObjectContext.automaticallyMergesChangesFromParent](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1845237-automaticallymergeschangesfrompa)Added [NSManagedObjectContext.count<T : NSFetchRequestResult>(for: NSFetchRequest<T>) throws -> Int](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1948985-count)Added [NSManagedObjectContext.fetch<T : NSFetchRequestResult>(_: NSFetchRequest<T>) throws -> [T]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1948986-fetch)Added [NSManagedObjectContext.queryGenerationToken](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1640477-querygenerationtoken)Added [NSManagedObjectContext.setQueryGenerationFrom(_: NSQueryGenerationToken?) throws](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1640469-setquerygenerationfromtoken)Added [NSMergePolicy.error](https://developer.apple.com/documentation/coredata/nsmergepolicy/1690612-errormergepolicy)Added [NSMergePolicy.mergeByPropertyObjectTrump](https://developer.apple.com/documentation/coredata/nsmergepolicy/1690607-mergebypropertyobjecttrump)Added [NSMergePolicy.mergeByPropertyStoreTrump](https://developer.apple.com/documentation/coredata/nsmergepolicy/1690609-mergebypropertystoretrump)Added [NSMergePolicy.overwrite](https://developer.apple.com/documentation/coredata/nsmergepolicy/1690610-overwrite)Added [NSMergePolicy.rollback](https://developer.apple.com/documentation/coredata/nsmergepolicy/1690613-rollback)Added [NSPersistentContainer](https://developer.apple.com/documentation/coredata/nspersistentcontainer)Added [NSPersistentContainer.defaultDirectoryURL() -> URL [class]](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640597-defaultdirectoryurl)Added [NSPersistentContainer.init(name: String)](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640557-initwithname)Added [NSPersistentContainer.init(name: String, managedObjectModel: NSManagedObjectModel)](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640584-init)Added [NSPersistentContainer.loadPersistentStores(completionHandler: (NSPersistentStoreDescription, Error?) -> Swift.Void)](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640568-loadpersistentstoreswithcompleti)Added [NSPersistentContainer.managedObjectModel](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640561-managedobjectmodel)Added [NSPersistentContainer.name](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640579-name)Added [NSPersistentContainer.newBackgroundContext() -> NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640581-newbackgroundcontext)Added [NSPersistentContainer.performBackgroundTask(_: (NSManagedObjectContext) -> Swift.Void)](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640564-performbackgroundtask)Added [NSPersistentContainer.persistentStoreCoordinator](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640567-persistentstorecoordinator)Added [NSPersistentContainer.persistentStoreDescriptions](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640577-persistentstoredescriptions)Added [NSPersistentContainer.viewContext](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640622-viewcontext)Added [NSPersistentStoreCoordinator.addPersistentStore(with: NSPersistentStoreDescription, completionHandler: (NSPersistentStoreDescription, Error?) -> Swift.Void)](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1640556-addpersistentstorewithdescriptio)Added [NSPersistentStoreCoordinator.registeredStoreTypes](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468870-registeredstoretypes)Added [NSPersistentStoreDescription](https://developer.apple.com/documentation/coredata/nspersistentstoredescription)Added [NSPersistentStoreDescription.configuration](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640634-configuration)Added [NSPersistentStoreDescription.init(url: URL)](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640563-initwithurl)Added [NSPersistentStoreDescription.isReadOnly](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640626-readonly)Added [NSPersistentStoreDescription.options](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640571-options)Added [NSPersistentStoreDescription.setOption(_: NSObject?, forKey: String)](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640574-setoption)Added [NSPersistentStoreDescription.setValue(_: NSObject?, forPragmaNamed: String)](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640598-setvalue)Added [NSPersistentStoreDescription.shouldAddStoreAsynchronously](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640599-shouldaddstoreasynchronously)Added [NSPersistentStoreDescription.shouldInferMappingModelAutomatically](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640623-shouldinfermappingmodelautomatic)Added [NSPersistentStoreDescription.shouldMigrateStoreAutomatically](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640566-shouldmigratestoreautomatically)Added [NSPersistentStoreDescription.sqlitePragmas](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640614-sqlitepragmas)Added [NSPersistentStoreDescription.timeout](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640587-timeout)Added [NSPersistentStoreDescription.type](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640609-type)Added [NSPersistentStoreDescription.url](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/1640616-url)Added [NSQueryGenerationToken](https://developer.apple.com/documentation/coredata/nsquerygenerationtoken)Added [NSQueryGenerationToken.current](https://developer.apple.com/documentation/coredata/nsquerygenerationtoken/1640578-currentquerygenerationtoken)Added [NSCoreDataVersionNumber10_11](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_11)Added [NSCoreDataVersionNumber10_11_3](https://developer.apple.com/documentation/coredata/nscoredataversionnumber10_11_3)Added [NSCoreDataVersionNumber_iPhoneOS_9_0](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_9_0)Added [NSCoreDataVersionNumber_iPhoneOS_9_2](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_9_2)Added [NSCoreDataVersionNumber_iPhoneOS_9_3](https://developer.apple.com/documentation/coredata/nscoredataversionnumber_iphoneos_9_3)Added [NSManagedObjectContextQueryGenerationKey](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextquerygenerationkey)Added [NSPersistentStoreConnectionPoolMaxSizeKey](https://developer.apple.com/documentation/coredata/nspersistentstoreconnectionpoolmaxsizekey)Modified [NSAsynchronousFetchRequest](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest)

|  | Declaration | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` class NSAsynchronousFetchRequest : NSPersistentStoreRequest {     var fetchRequest: NSFetchRequest { get }     var completionBlock: NSPersistentStoreAsynchronousFetchResultCompletionBlock? { get }     var estimatedResultCount: Int     init(fetchRequest request: NSFetchRequest, completionBlock blk: NSPersistentStoreAsynchronousFetchResultCompletionBlock?) } ``` | ```  ``` | -- |
| To | ``` class NSAsynchronousFetchRequest<ResultType : NSFetchRequestResult> : NSPersistentStoreRequest {     var fetchRequest: NSFetchRequest<ResultType> { get }     var completionBlock: CoreData.NSPersistentStoreAsynchronousFetchResultCompletionBlock? { get }     var estimatedResultCount: Int     init(fetchRequest request: NSFetchRequest<ResultType>, completionBlock blk: (@escaping (NSAsynchronousFetchResult<ResultType>) -> Swift.Void)? = nil) } ``` | ``` ResultType : NSFetchRequestResult ``` | ResultType |

Modified [NSAsynchronousFetchRequest.completionBlock](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/1506815-completionblock)

|  | Declaration |
| --- | --- |
| From | ``` var completionBlock: NSPersistentStoreAsynchronousFetchResultCompletionBlock? { get } ``` |
| To | ``` var completionBlock: CoreData.NSPersistentStoreAsynchronousFetchResultCompletionBlock? { get } ``` |

Modified [NSAsynchronousFetchRequest.fetchRequest](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/1506719-fetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` var fetchRequest: NSFetchRequest { get } ``` |
| To | ``` var fetchRequest: NSFetchRequest<ResultType> { get } ``` |

Modified [NSAsynchronousFetchRequest.init(fetchRequest: NSFetchRequest<ResultType>, completionBlock: ( (NSAsynchronousFetchResult<ResultType>) -> Swift.Void)?)](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/1506218-initwithfetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` init(fetchRequest request: NSFetchRequest, completionBlock blk: NSPersistentStoreAsynchronousFetchResultCompletionBlock?) ``` |
| To | ``` init(fetchRequest request: NSFetchRequest<ResultType>, completionBlock blk: (@escaping (NSAsynchronousFetchResult<ResultType>) -> Swift.Void)? = nil) ``` |

Modified [NSAsynchronousFetchResult](https://developer.apple.com/documentation/coredata/nsasynchronousfetchresult)

|  | Declaration | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` class NSAsynchronousFetchResult : NSPersistentStoreAsynchronousResult {     var fetchRequest: NSAsynchronousFetchRequest { get }     var finalResult: [AnyObject]? { get } } ``` | ```  ``` | -- |
| To | ``` class NSAsynchronousFetchResult<ResultType : NSFetchRequestResult> : NSPersistentStoreAsynchronousResult {     var fetchRequest: NSAsynchronousFetchRequest<ResultType> { get }     var finalResult: [ResultType]? { get } } ``` | ``` ResultType : NSFetchRequestResult ``` | ResultType |

Modified [NSAsynchronousFetchResult.fetchRequest](https://developer.apple.com/documentation/coredata/nsasynchronousfetchresult/1404906-fetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` var fetchRequest: NSAsynchronousFetchRequest { get } ``` |
| To | ``` var fetchRequest: NSAsynchronousFetchRequest<ResultType> { get } ``` |

Modified [NSAsynchronousFetchResult.finalResult](https://developer.apple.com/documentation/coredata/nsasynchronousfetchresult/1404930-finalresult)

|  | Declaration |
| --- | --- |
| From | ``` var finalResult: [AnyObject]? { get } ``` |
| To | ``` var finalResult: [ResultType]? { get } ``` |

Modified [NSAtomicStore](https://developer.apple.com/documentation/coredata/nsatomicstore)

|  | Declaration |
| --- | --- |
| From | ``` class NSAtomicStore : NSPersistentStore {     init(persistentStoreCoordinator coordinator: NSPersistentStoreCoordinator?, configurationName configurationName: String?, URL url: NSURL, options options: [NSObject : AnyObject]?)     func load() throws     func save() throws     func newCacheNodeForManagedObject(_ managedObject: NSManagedObject) -> NSAtomicStoreCacheNode     func updateCacheNode(_ node: NSAtomicStoreCacheNode, fromManagedObject managedObject: NSManagedObject)     func cacheNodes() -> Set<NSAtomicStoreCacheNode>     func addCacheNodes(_ cacheNodes: Set<NSAtomicStoreCacheNode>)     func willRemoveCacheNodes(_ cacheNodes: Set<NSAtomicStoreCacheNode>)     func cacheNodeForObjectID(_ objectID: NSManagedObjectID) -> NSAtomicStoreCacheNode?     func objectIDForEntity(_ entity: NSEntityDescription, referenceObject data: AnyObject) -> NSManagedObjectID     func newReferenceObjectForManagedObject(_ managedObject: NSManagedObject) -> AnyObject     func referenceObjectForObjectID(_ objectID: NSManagedObjectID) -> AnyObject } ``` |
| To | ``` class NSAtomicStore : NSPersistentStore {     init(persistentStoreCoordinator coordinator: NSPersistentStoreCoordinator?, configurationName configurationName: String?, at url: URL, options options: [AnyHashable : Any]? = nil)     func load() throws     func save() throws     func newCacheNode(for managedObject: NSManagedObject) -> NSAtomicStoreCacheNode     func updateCacheNode(_ node: NSAtomicStoreCacheNode, from managedObject: NSManagedObject)     func cacheNodes() -> Set<NSAtomicStoreCacheNode>     func addCacheNodes(_ cacheNodes: Set<NSAtomicStoreCacheNode>)     func willRemoveCacheNodes(_ cacheNodes: Set<NSAtomicStoreCacheNode>)     func cacheNode(for objectID: NSManagedObjectID) -> NSAtomicStoreCacheNode?     func objectID(for entity: NSEntityDescription, withReferenceObject data: Any) -> NSManagedObjectID     func newReferenceObject(for managedObject: NSManagedObject) -> Any     func referenceObject(for objectID: NSManagedObjectID) -> Any } ``` |

Modified [NSAtomicStore.cacheNode(for: NSManagedObjectID) -> NSAtomicStoreCacheNode?](https://developer.apple.com/documentation/coredata/nsatomicstore/1388040-cachenodeforobjectid)

|  | Declaration |
| --- | --- |
| From | ``` func cacheNodeForObjectID(_ objectID: NSManagedObjectID) -> NSAtomicStoreCacheNode? ``` |
| To | ``` func cacheNode(for objectID: NSManagedObjectID) -> NSAtomicStoreCacheNode? ``` |

Modified [NSAtomicStore.init(persistentStoreCoordinator: NSPersistentStoreCoordinator?, configurationName: String?, at: URL, options: [AnyHashable : Any]?)](https://developer.apple.com/documentation/coredata/nsatomicstore/1388054-initwithpersistentstorecoordinat)

|  | Declaration |
| --- | --- |
| From | ``` init(persistentStoreCoordinator coordinator: NSPersistentStoreCoordinator?, configurationName configurationName: String?, URL url: NSURL, options options: [NSObject : AnyObject]?) ``` |
| To | ``` init(persistentStoreCoordinator coordinator: NSPersistentStoreCoordinator?, configurationName configurationName: String?, at url: URL, options options: [AnyHashable : Any]? = nil) ``` |

Modified [NSAtomicStore.newCacheNode(for: NSManagedObject) -> NSAtomicStoreCacheNode](https://developer.apple.com/documentation/coredata/nsatomicstore/1388052-newcachenodeformanagedobject)

|  | Declaration |
| --- | --- |
| From | ``` func newCacheNodeForManagedObject(_ managedObject: NSManagedObject) -> NSAtomicStoreCacheNode ``` |
| To | ``` func newCacheNode(for managedObject: NSManagedObject) -> NSAtomicStoreCacheNode ``` |

Modified [NSAtomicStore.newReferenceObject(for: NSManagedObject) -> Any](https://developer.apple.com/documentation/coredata/nsatomicstore/1388050-newreferenceobject)

|  | Declaration |
| --- | --- |
| From | ``` func newReferenceObjectForManagedObject(_ managedObject: NSManagedObject) -> AnyObject ``` |
| To | ``` func newReferenceObject(for managedObject: NSManagedObject) -> Any ``` |

Modified [NSAtomicStore.objectID(for: NSEntityDescription, withReferenceObject: Any) -> NSManagedObjectID](https://developer.apple.com/documentation/coredata/nsatomicstore/1388058-objectid)

|  | Declaration |
| --- | --- |
| From | ``` func objectIDForEntity(_ entity: NSEntityDescription, referenceObject data: AnyObject) -> NSManagedObjectID ``` |
| To | ``` func objectID(for entity: NSEntityDescription, withReferenceObject data: Any) -> NSManagedObjectID ``` |

Modified [NSAtomicStore.referenceObject(for: NSManagedObjectID) -> Any](https://developer.apple.com/documentation/coredata/nsatomicstore/1388046-referenceobject)

|  | Declaration |
| --- | --- |
| From | ``` func referenceObjectForObjectID(_ objectID: NSManagedObjectID) -> AnyObject ``` |
| To | ``` func referenceObject(for objectID: NSManagedObjectID) -> Any ``` |

Modified [NSAtomicStore.updateCacheNode(_: NSAtomicStoreCacheNode, from: NSManagedObject)](https://developer.apple.com/documentation/coredata/nsatomicstore/1388044-updatecachenode)

|  | Declaration |
| --- | --- |
| From | ``` func updateCacheNode(_ node: NSAtomicStoreCacheNode, fromManagedObject managedObject: NSManagedObject) ``` |
| To | ``` func updateCacheNode(_ node: NSAtomicStoreCacheNode, from managedObject: NSManagedObject) ``` |

Modified [NSAtomicStoreCacheNode](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSAtomicStoreCacheNode : NSObject {     init(objectID moid: NSManagedObjectID)     var objectID: NSManagedObjectID { get }     var propertyCache: NSMutableDictionary?     func valueForKey(_ key: String) -> AnyObject?     func setValue(_ value: AnyObject?, forKey key: String) } ``` | -- |
| To | ``` class NSAtomicStoreCacheNode : NSObject {     init(objectID moid: NSManagedObjectID)     var objectID: NSManagedObjectID { get }     var propertyCache: NSMutableDictionary?     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSAtomicStoreCacheNode : CVarArg { } extension NSAtomicStoreCacheNode : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NSAtomicStoreCacheNode.setValue(_: Any?, forKey: String)](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/1506456-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ value: AnyObject?, forKey key: String) ``` |
| To | ``` func setValue(_ value: Any?, forKey key: String) ``` |

Modified [NSAtomicStoreCacheNode.value(forKey: String) -> Any?](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/1506550-valueforkey)

|  | Declaration |
| --- | --- |
| From | ``` func valueForKey(_ key: String) -> AnyObject? ``` |
| To | ``` func value(forKey key: String) -> Any? ``` |

Modified [NSAttributeDescription](https://developer.apple.com/documentation/coredata/nsattributedescription)

|  | Declaration |
| --- | --- |
| From | ``` class NSAttributeDescription : NSPropertyDescription {     var attributeType: NSAttributeType     var attributeValueClassName: String?     var defaultValue: AnyObject?     @NSCopying var versionHash: NSData { get }     var valueTransformerName: String?     var allowsExternalBinaryDataStorage: Bool } ``` |
| To | ``` class NSAttributeDescription : NSPropertyDescription {     var attributeType: NSAttributeType     var attributeValueClassName: String?     var defaultValue: Any?     var versionHash: Data { get }     var valueTransformerName: String?     var allowsExternalBinaryDataStorage: Bool } ``` |

Modified [NSAttributeDescription.defaultValue](https://developer.apple.com/documentation/coredata/nsattributedescription/1498302-defaultvalue)

|  | Declaration |
| --- | --- |
| From | ``` var defaultValue: AnyObject? ``` |
| To | ``` var defaultValue: Any? ``` |

Modified [NSAttributeDescription.versionHash](https://developer.apple.com/documentation/coredata/nsattributedescription/1498310-versionhash)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var versionHash: NSData { get } ``` |
| To | ``` var versionHash: Data { get } ``` |

Modified [NSAttributeType [enum]](https://developer.apple.com/documentation/coredata/nsattributetype)

|  | Declaration |
| --- | --- |
| From | ``` enum NSAttributeType : UInt {     case UndefinedAttributeType     case Integer16AttributeType     case Integer32AttributeType     case Integer64AttributeType     case DecimalAttributeType     case DoubleAttributeType     case FloatAttributeType     case StringAttributeType     case BooleanAttributeType     case DateAttributeType     case BinaryDataAttributeType     case TransformableAttributeType     case ObjectIDAttributeType } ``` |
| To | ``` enum NSAttributeType : UInt {     case undefinedAttributeType     case integer16AttributeType     case integer32AttributeType     case integer64AttributeType     case decimalAttributeType     case doubleAttributeType     case floatAttributeType     case stringAttributeType     case booleanAttributeType     case dateAttributeType     case binaryDataAttributeType     case transformableAttributeType     case objectIDAttributeType } ``` |

Modified [NSAttributeType.binaryDataAttributeType](https://developer.apple.com/documentation/coredata/nsattributetype/binarydataattributetype)

|  | Declaration |
| --- | --- |
| From | ``` case BinaryDataAttributeType ``` |
| To | ``` case binaryDataAttributeType ``` |

Modified [NSAttributeType.booleanAttributeType](https://developer.apple.com/documentation/coredata/nsattributetype/booleanattributetype)

|  | Declaration |
| --- | --- |
| From | ``` case BooleanAttributeType ``` |
| To | ``` case booleanAttributeType ``` |

Modified [NSAttributeType.dateAttributeType](https://developer.apple.com/documentation/coredata/nsattributetype/nsdateattributetype)

|  | Declaration |
| --- | --- |
| From | ``` case DateAttributeType ``` |
| To | ``` case dateAttributeType ``` |

Modified [NSAttributeType.decimalAttributeType](https://developer.apple.com/documentation/coredata/nsattributetype/decimalattributetype)

|  | Declaration |
| --- | --- |
| From | ``` case DecimalAttributeType ``` |
| To | ``` case decimalAttributeType ``` |

Modified [NSAttributeType.doubleAttributeType](https://developer.apple.com/documentation/coredata/nsattributetype/doubleattributetype)

|  | Declaration |
| --- | --- |
| From | ``` case DoubleAttributeType ``` |
| To | ``` case doubleAttributeType ``` |

Modified [NSAttributeType.floatAttributeType](https://developer.apple.com/documentation/coredata/nsattributetype/floatattributetype)

|  | Declaration |
| --- | --- |
| From | ``` case FloatAttributeType ``` |
| To | ``` case floatAttributeType ``` |

Modified [NSAttributeType.integer16AttributeType](https://developer.apple.com/documentation/coredata/nsattributetype/integer16attributetype)

|  | Declaration |
| --- | --- |
| From | ``` case Integer16AttributeType ``` |
| To | ``` case integer16AttributeType ``` |

Modified [NSAttributeType.integer32AttributeType](https://developer.apple.com/documentation/coredata/nsattributetype/nsinteger32attributetype)

|  | Declaration |
| --- | --- |
| From | ``` case Integer32AttributeType ``` |
| To | ``` case integer32AttributeType ``` |

Modified [NSAttributeType.integer64AttributeType](https://developer.apple.com/documentation/coredata/nsattributetype/nsinteger64attributetype)

|  | Declaration |
| --- | --- |
| From | ``` case Integer64AttributeType ``` |
| To | ``` case integer64AttributeType ``` |

Modified [NSAttributeType.objectIDAttributeType](https://developer.apple.com/documentation/coredata/nsattributetype/nsobjectidattributetype)

|  | Declaration |
| --- | --- |
| From | ``` case ObjectIDAttributeType ``` |
| To | ``` case objectIDAttributeType ``` |

Modified [NSAttributeType.stringAttributeType](https://developer.apple.com/documentation/coredata/nsattributetype/stringattributetype)

|  | Declaration |
| --- | --- |
| From | ``` case StringAttributeType ``` |
| To | ``` case stringAttributeType ``` |

Modified [NSAttributeType.transformableAttributeType](https://developer.apple.com/documentation/coredata/nsattributetype/transformableattributetype)

|  | Declaration |
| --- | --- |
| From | ``` case TransformableAttributeType ``` |
| To | ``` case transformableAttributeType ``` |

Modified [NSAttributeType.undefinedAttributeType](https://developer.apple.com/documentation/coredata/nsattributetype/undefinedattributetype)

|  | Declaration |
| --- | --- |
| From | ``` case UndefinedAttributeType ``` |
| To | ``` case undefinedAttributeType ``` |

Modified [NSBatchDeleteRequest](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest)

|  | Declaration |
| --- | --- |
| From | ``` class NSBatchDeleteRequest : NSPersistentStoreRequest {     convenience init()     init(fetchRequest fetch: NSFetchRequest)     convenience init(objectIDs objects: [NSManagedObjectID])     var resultType: NSBatchDeleteRequestResultType     @NSCopying var fetchRequest: NSFetchRequest { get } } ``` |
| To | ``` class NSBatchDeleteRequest : NSPersistentStoreRequest {     convenience init()     init(fetchRequest fetch: NSFetchRequest<NSFetchRequestResult>)     convenience init(objectIDs objects: [NSManagedObjectID])     var resultType: NSBatchDeleteRequestResultType     @NSCopying var fetchRequest: NSFetchRequest<NSFetchRequestResult> { get } } ``` |

Modified [NSBatchDeleteRequest.fetchRequest](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/1506206-fetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var fetchRequest: NSFetchRequest { get } ``` |
| To | ``` @NSCopying var fetchRequest: NSFetchRequest<NSFetchRequestResult> { get } ``` |

Modified [NSBatchDeleteRequest.init(fetchRequest: NSFetchRequest<NSFetchRequestResult>)](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/1506302-init)

|  | Declaration |
| --- | --- |
| From | ``` init(fetchRequest fetch: NSFetchRequest) ``` |
| To | ``` init(fetchRequest fetch: NSFetchRequest<NSFetchRequestResult>) ``` |

Modified [NSBatchDeleteRequestResultType [enum]](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype)

|  | Declaration |
| --- | --- |
| From | ``` enum NSBatchDeleteRequestResultType : UInt {     case ResultTypeStatusOnly     case ResultTypeObjectIDs     case ResultTypeCount } ``` |
| To | ``` enum NSBatchDeleteRequestResultType : UInt {     case resultTypeStatusOnly     case resultTypeObjectIDs     case resultTypeCount } ``` |

Modified [NSBatchDeleteRequestResultType.resultTypeCount](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype/resulttypecount)

|  | Declaration |
| --- | --- |
| From | ``` case ResultTypeCount ``` |
| To | ``` case resultTypeCount ``` |

Modified [NSBatchDeleteRequestResultType.resultTypeObjectIDs](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype/resulttypeobjectids)

|  | Declaration |
| --- | --- |
| From | ``` case ResultTypeObjectIDs ``` |
| To | ``` case resultTypeObjectIDs ``` |

Modified [NSBatchDeleteRequestResultType.resultTypeStatusOnly](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype/resulttypestatusonly)

|  | Declaration |
| --- | --- |
| From | ``` case ResultTypeStatusOnly ``` |
| To | ``` case resultTypeStatusOnly ``` |

Modified [NSBatchDeleteResult](https://developer.apple.com/documentation/coredata/nsbatchdeleteresult)

|  | Declaration |
| --- | --- |
| From | ``` class NSBatchDeleteResult : NSPersistentStoreResult {     var result: AnyObject? { get }     var resultType: NSBatchDeleteRequestResultType { get } } ``` |
| To | ``` class NSBatchDeleteResult : NSPersistentStoreResult {     var result: Any? { get }     var resultType: NSBatchDeleteRequestResultType { get } } ``` |

Modified [NSBatchDeleteResult.result](https://developer.apple.com/documentation/coredata/nsbatchdeleteresult/1404922-result)

|  | Declaration |
| --- | --- |
| From | ``` var result: AnyObject? { get } ``` |
| To | ``` var result: Any? { get } ``` |

Modified [NSBatchUpdateRequest](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest)

|  | Declaration |
| --- | --- |
| From | ``` class NSBatchUpdateRequest : NSPersistentStoreRequest {     convenience init(entityName entityName: String)     class func batchUpdateRequestWithEntityName(_ entityName: String) -> Self     init(entityName entityName: String)     init(entity entity: NSEntityDescription)     var entityName: String { get }     var entity: NSEntityDescription { get }     var predicate: NSPredicate?     var includesSubentities: Bool     var resultType: NSBatchUpdateRequestResultType     var propertiesToUpdate: [NSObject : AnyObject]? } ``` |
| To | ``` class NSBatchUpdateRequest : NSPersistentStoreRequest {     convenience init(entityName entityName: String)     class func withEntityName(_ entityName: String) -> Self     init(entityName entityName: String)     init(entity entity: NSEntityDescription)     var entityName: String { get }     var entity: NSEntityDescription { get }     var predicate: NSPredicate?     var includesSubentities: Bool     var resultType: NSBatchUpdateRequestResultType     var propertiesToUpdate: [AnyHashable : Any]? } ``` |

Modified [NSBatchUpdateRequest.propertiesToUpdate](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/1506582-propertiestoupdate)

|  | Declaration |
| --- | --- |
| From | ``` var propertiesToUpdate: [NSObject : AnyObject]? ``` |
| To | ``` var propertiesToUpdate: [AnyHashable : Any]? ``` |

Modified [NSBatchUpdateRequestResultType [enum]](https://developer.apple.com/documentation/coredata/nsbatchupdaterequestresulttype)

|  | Declaration |
| --- | --- |
| From | ``` enum NSBatchUpdateRequestResultType : UInt {     case StatusOnlyResultType     case UpdatedObjectIDsResultType     case UpdatedObjectsCountResultType } ``` |
| To | ``` enum NSBatchUpdateRequestResultType : UInt {     case statusOnlyResultType     case updatedObjectIDsResultType     case updatedObjectsCountResultType } ``` |

Modified [NSBatchUpdateRequestResultType.statusOnlyResultType](https://developer.apple.com/documentation/coredata/nsbatchupdaterequestresulttype/nsstatusonlyresulttype)

|  | Declaration |
| --- | --- |
| From | ``` case StatusOnlyResultType ``` |
| To | ``` case statusOnlyResultType ``` |

Modified [NSBatchUpdateRequestResultType.updatedObjectIDsResultType](https://developer.apple.com/documentation/coredata/nsbatchupdaterequestresulttype/updatedobjectidsresulttype)

|  | Declaration |
| --- | --- |
| From | ``` case UpdatedObjectIDsResultType ``` |
| To | ``` case updatedObjectIDsResultType ``` |

Modified [NSBatchUpdateRequestResultType.updatedObjectsCountResultType](https://developer.apple.com/documentation/coredata/nsbatchupdaterequestresulttype/nsupdatedobjectscountresulttype)

|  | Declaration |
| --- | --- |
| From | ``` case UpdatedObjectsCountResultType ``` |
| To | ``` case updatedObjectsCountResultType ``` |

Modified [NSBatchUpdateResult](https://developer.apple.com/documentation/coredata/nsbatchupdateresult)

|  | Declaration |
| --- | --- |
| From | ``` class NSBatchUpdateResult : NSPersistentStoreResult {     var result: AnyObject? { get }     var resultType: NSBatchUpdateRequestResultType { get } } ``` |
| To | ``` class NSBatchUpdateResult : NSPersistentStoreResult {     var result: Any? { get }     var resultType: NSBatchUpdateRequestResultType { get } } ``` |

Modified [NSBatchUpdateResult.result](https://developer.apple.com/documentation/coredata/nsbatchupdateresult/1404946-result)

|  | Declaration |
| --- | --- |
| From | ``` var result: AnyObject? { get } ``` |
| To | ``` var result: Any? { get } ``` |

Modified [NSConstraintConflict](https://developer.apple.com/documentation/coredata/nsconstraintconflict)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSConstraintConflict : NSObject {     var constraint: [String] { get }     var constraintValues: [String : AnyObject] { get }     var databaseObject: NSManagedObject? { get }     var databaseSnapshot: [String : AnyObject]? { get }     var conflictingObjects: [NSManagedObject] { get }     var conflictingSnapshots: [[NSObject : AnyObject]] { get }     init(constraint contraint: [String], databaseObject databaseObject: NSManagedObject?, databaseSnapshot databaseSnapshot: [NSObject : AnyObject]?, conflictingObjects conflictingObjects: [NSManagedObject], conflictingSnapshots conflictingSnapshots: [AnyObject]) } ``` | -- |
| To | ``` class NSConstraintConflict : NSObject {     var constraint: [String] { get }     var constraintValues: [String : Any] { get }     var databaseObject: NSManagedObject? { get }     var databaseSnapshot: [String : Any]? { get }     var conflictingObjects: [NSManagedObject] { get }     var conflictingSnapshots: [[AnyHashable : Any]] { get }     init(constraint contraint: [String], database databaseObject: NSManagedObject?, databaseSnapshot databaseSnapshot: [AnyHashable : Any]?, conflicting conflictingObjects: [NSManagedObject], conflictingSnapshots conflictingSnapshots: [Any])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSConstraintConflict : CVarArg { } extension NSConstraintConflict : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NSConstraintConflict.conflictingSnapshots](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506774-conflictingsnapshots)

|  | Declaration |
| --- | --- |
| From | ``` var conflictingSnapshots: [[NSObject : AnyObject]] { get } ``` |
| To | ``` var conflictingSnapshots: [[AnyHashable : Any]] { get } ``` |

Modified [NSConstraintConflict.constraintValues](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506399-constraintvalues)

|  | Declaration |
| --- | --- |
| From | ``` var constraintValues: [String : AnyObject] { get } ``` |
| To | ``` var constraintValues: [String : Any] { get } ``` |

Modified [NSConstraintConflict.databaseSnapshot](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506687-databasesnapshot)

|  | Declaration |
| --- | --- |
| From | ``` var databaseSnapshot: [String : AnyObject]? { get } ``` |
| To | ``` var databaseSnapshot: [String : Any]? { get } ``` |

Modified [NSConstraintConflict.init(constraint: [String], database: NSManagedObject?, databaseSnapshot: [AnyHashable : Any]?, conflicting: [NSManagedObject], conflictingSnapshots: [Any])](https://developer.apple.com/documentation/coredata/nsconstraintconflict/1506668-init)

|  | Declaration |
| --- | --- |
| From | ``` init(constraint contraint: [String], databaseObject databaseObject: NSManagedObject?, databaseSnapshot databaseSnapshot: [NSObject : AnyObject]?, conflictingObjects conflictingObjects: [NSManagedObject], conflictingSnapshots conflictingSnapshots: [AnyObject]) ``` |
| To | ``` init(constraint contraint: [String], database databaseObject: NSManagedObject?, databaseSnapshot databaseSnapshot: [AnyHashable : Any]?, conflicting conflictingObjects: [NSManagedObject], conflictingSnapshots conflictingSnapshots: [Any]) ``` |

Modified [NSDeleteRule [enum]](https://developer.apple.com/documentation/coredata/nsdeleterule)

|  | Declaration |
| --- | --- |
| From | ``` enum NSDeleteRule : UInt {     case NoActionDeleteRule     case NullifyDeleteRule     case CascadeDeleteRule     case DenyDeleteRule } ``` |
| To | ``` enum NSDeleteRule : UInt {     case noActionDeleteRule     case nullifyDeleteRule     case cascadeDeleteRule     case denyDeleteRule } ``` |

Modified [NSDeleteRule.cascadeDeleteRule](https://developer.apple.com/documentation/coredata/nsdeleterule/nscascadedeleterule)

|  | Declaration |
| --- | --- |
| From | ``` case CascadeDeleteRule ``` |
| To | ``` case cascadeDeleteRule ``` |

Modified [NSDeleteRule.denyDeleteRule](https://developer.apple.com/documentation/coredata/nsdeleterule/nsdenydeleterule)

|  | Declaration |
| --- | --- |
| From | ``` case DenyDeleteRule ``` |
| To | ``` case denyDeleteRule ``` |

Modified [NSDeleteRule.noActionDeleteRule](https://developer.apple.com/documentation/coredata/nsdeleterule/nsnoactiondeleterule)

|  | Declaration |
| --- | --- |
| From | ``` case NoActionDeleteRule ``` |
| To | ``` case noActionDeleteRule ``` |

Modified [NSDeleteRule.nullifyDeleteRule](https://developer.apple.com/documentation/coredata/nsdeleterule/nullifydeleterule)

|  | Declaration |
| --- | --- |
| From | ``` case NullifyDeleteRule ``` |
| To | ``` case nullifyDeleteRule ``` |

Modified [NSEntityDescription](https://developer.apple.com/documentation/coredata/nsentitydescription)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSEntityDescription : NSObject, NSCoding, NSCopying, NSFastEnumeration {     class func entityForName(_ entityName: String, inManagedObjectContext context: NSManagedObjectContext) -> NSEntityDescription?     class func insertNewObjectForEntityForName(_ entityName: String, inManagedObjectContext context: NSManagedObjectContext) -> NSManagedObject     unowned(unsafe) var managedObjectModel: NSManagedObjectModel { get }     var managedObjectClassName: String!     var name: String?     var abstract: Bool     var subentitiesByName: [String : NSEntityDescription] { get }     var subentities: [NSEntityDescription]     unowned(unsafe) var superentity: NSEntityDescription? { get }     var propertiesByName: [String : NSPropertyDescription] { get }     var properties: [NSPropertyDescription]     var userInfo: [NSObject : AnyObject]?     var attributesByName: [String : NSAttributeDescription] { get }     var relationshipsByName: [String : NSRelationshipDescription] { get }     func relationshipsWithDestinationEntity(_ entity: NSEntityDescription) -> [NSRelationshipDescription]     func isKindOfEntity(_ entity: NSEntityDescription) -> Bool     @NSCopying var versionHash: NSData { get }     var versionHashModifier: String?     var renamingIdentifier: String?     var compoundIndexes: [[AnyObject]]     var uniquenessConstraints: [[AnyObject]] } ``` | NSCoding, NSCopying, NSFastEnumeration |
| To | ``` class NSEntityDescription : NSObject, NSCoding, NSCopying, NSFastEnumeration {     class func entity(forEntityName entityName: String, in context: NSManagedObjectContext) -> NSEntityDescription?     class func insertNewObject(forEntityName entityName: String, into context: NSManagedObjectContext) -> NSManagedObject     unowned(unsafe) var managedObjectModel: NSManagedObjectModel { get }     var managedObjectClassName: String!     var name: String?     var isAbstract: Bool     var subentitiesByName: [String : NSEntityDescription] { get }     var subentities: [NSEntityDescription]     unowned(unsafe) var superentity: NSEntityDescription? { get }     var propertiesByName: [String : NSPropertyDescription] { get }     var properties: [NSPropertyDescription]     var userInfo: [AnyHashable : Any]?     var attributesByName: [String : NSAttributeDescription] { get }     var relationshipsByName: [String : NSRelationshipDescription] { get }     func relationships(forDestination entity: NSEntityDescription) -> [NSRelationshipDescription]     func isKindOf(entity entity: NSEntityDescription) -> Bool     var versionHash: Data { get }     var versionHashModifier: String?     var renamingIdentifier: String?     var compoundIndexes: [[Any]]     var uniquenessConstraints: [[Any]]     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSEntityDescription : CVarArg { } extension NSEntityDescription : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying, NSFastEnumeration |

Modified [NSEntityDescription.compoundIndexes](https://developer.apple.com/documentation/coredata/nsentitydescription/1425115-compoundindexes)

|  | Declaration |
| --- | --- |
| From | ``` var compoundIndexes: [[AnyObject]] ``` |
| To | ``` var compoundIndexes: [[Any]] ``` |

Modified [NSEntityDescription.entity(forEntityName: String, in: NSManagedObjectContext) -> NSEntityDescription? [class]](https://developer.apple.com/documentation/coredata/nsentitydescription/1425111-entityforname)

|  | Declaration |
| --- | --- |
| From | ``` class func entityForName(_ entityName: String, inManagedObjectContext context: NSManagedObjectContext) -> NSEntityDescription? ``` |
| To | ``` class func entity(forEntityName entityName: String, in context: NSManagedObjectContext) -> NSEntityDescription? ``` |

Modified [NSEntityDescription.insertNewObject(forEntityName: String, into: NSManagedObjectContext) -> NSManagedObject [class]](https://developer.apple.com/documentation/coredata/nsentitydescription/1425093-insertnewobjectforentityforname)

|  | Declaration |
| --- | --- |
| From | ``` class func insertNewObjectForEntityForName(_ entityName: String, inManagedObjectContext context: NSManagedObjectContext) -> NSManagedObject ``` |
| To | ``` class func insertNewObject(forEntityName entityName: String, into context: NSManagedObjectContext) -> NSManagedObject ``` |

Modified [NSEntityDescription.isAbstract](https://developer.apple.com/documentation/coredata/nsentitydescription/1425097-isabstract)

|  | Declaration |
| --- | --- |
| From | ``` var abstract: Bool ``` |
| To | ``` var isAbstract: Bool ``` |

Modified [NSEntityDescription.isKindOf(entity: NSEntityDescription) -> Bool](https://developer.apple.com/documentation/coredata/nsentitydescription/1425113-iskindofentity)

|  | Declaration |
| --- | --- |
| From | ``` func isKindOfEntity(_ entity: NSEntityDescription) -> Bool ``` |
| To | ``` func isKindOf(entity entity: NSEntityDescription) -> Bool ``` |

Modified [NSEntityDescription.relationships(forDestination: NSEntityDescription) -> [NSRelationshipDescription]](https://developer.apple.com/documentation/coredata/nsentitydescription/1425127-relationships)

|  | Declaration |
| --- | --- |
| From | ``` func relationshipsWithDestinationEntity(_ entity: NSEntityDescription) -> [NSRelationshipDescription] ``` |
| To | ``` func relationships(forDestination entity: NSEntityDescription) -> [NSRelationshipDescription] ``` |

Modified [NSEntityDescription.uniquenessConstraints](https://developer.apple.com/documentation/coredata/nsentitydescription/1425095-uniquenessconstraints)

|  | Declaration |
| --- | --- |
| From | ``` var uniquenessConstraints: [[AnyObject]] ``` |
| To | ``` var uniquenessConstraints: [[Any]] ``` |

Modified [NSEntityDescription.userInfo](https://developer.apple.com/documentation/coredata/nsentitydescription/1425117-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]? ``` |
| To | ``` var userInfo: [AnyHashable : Any]? ``` |

Modified [NSEntityDescription.versionHash](https://developer.apple.com/documentation/coredata/nsentitydescription/1425133-versionhash)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var versionHash: NSData { get } ``` |
| To | ``` var versionHash: Data { get } ``` |

Modified [NSEntityMapping](https://developer.apple.com/documentation/coredata/nsentitymapping)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSEntityMapping : NSObject {     var name: String!     var mappingType: NSEntityMappingType     var sourceEntityName: String?     @NSCopying var sourceEntityVersionHash: NSData?     var destinationEntityName: String?     @NSCopying var destinationEntityVersionHash: NSData?     var attributeMappings: [NSPropertyMapping]?     var relationshipMappings: [NSPropertyMapping]?     var sourceExpression: NSExpression?     var userInfo: [NSObject : AnyObject]?     var entityMigrationPolicyClassName: String? } ``` | -- |
| To | ``` class NSEntityMapping : NSObject {     var name: String!     var mappingType: NSEntityMappingType     var sourceEntityName: String?     var sourceEntityVersionHash: Data?     var destinationEntityName: String?     var destinationEntityVersionHash: Data?     var attributeMappings: [NSPropertyMapping]?     var relationshipMappings: [NSPropertyMapping]?     var sourceExpression: NSExpression?     var userInfo: [AnyHashable : Any]?     var entityMigrationPolicyClassName: String?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSEntityMapping : CVarArg { } extension NSEntityMapping : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NSEntityMapping.destinationEntityVersionHash](https://developer.apple.com/documentation/coredata/nsentitymapping/1443169-destinationentityversionhash)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var destinationEntityVersionHash: NSData? ``` |
| To | ``` var destinationEntityVersionHash: Data? ``` |

Modified [NSEntityMapping.sourceEntityVersionHash](https://developer.apple.com/documentation/coredata/nsentitymapping/1443182-sourceentityversionhash)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var sourceEntityVersionHash: NSData? ``` |
| To | ``` var sourceEntityVersionHash: Data? ``` |

Modified [NSEntityMapping.userInfo](https://developer.apple.com/documentation/coredata/nsentitymapping/1443184-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]? ``` |
| To | ``` var userInfo: [AnyHashable : Any]? ``` |

Modified [NSEntityMappingType [enum]](https://developer.apple.com/documentation/coredata/nsentitymappingtype)

|  | Declaration |
| --- | --- |
| From | ``` enum NSEntityMappingType : UInt {     case UndefinedEntityMappingType     case CustomEntityMappingType     case AddEntityMappingType     case RemoveEntityMappingType     case CopyEntityMappingType     case TransformEntityMappingType } ``` |
| To | ``` enum NSEntityMappingType : UInt {     case undefinedEntityMappingType     case customEntityMappingType     case addEntityMappingType     case removeEntityMappingType     case copyEntityMappingType     case transformEntityMappingType } ``` |

Modified [NSEntityMappingType.addEntityMappingType](https://developer.apple.com/documentation/coredata/nsentitymappingtype/addentitymappingtype)

|  | Declaration |
| --- | --- |
| From | ``` case AddEntityMappingType ``` |
| To | ``` case addEntityMappingType ``` |

Modified [NSEntityMappingType.copyEntityMappingType](https://developer.apple.com/documentation/coredata/nsentitymappingtype/nscopyentitymappingtype)

|  | Declaration |
| --- | --- |
| From | ``` case CopyEntityMappingType ``` |
| To | ``` case copyEntityMappingType ``` |

Modified [NSEntityMappingType.customEntityMappingType](https://developer.apple.com/documentation/coredata/nsentitymappingtype/nscustomentitymappingtype)

|  | Declaration |
| --- | --- |
| From | ``` case CustomEntityMappingType ``` |
| To | ``` case customEntityMappingType ``` |

Modified [NSEntityMappingType.removeEntityMappingType](https://developer.apple.com/documentation/coredata/nsentitymappingtype/nsremoveentitymappingtype)

|  | Declaration |
| --- | --- |
| From | ``` case RemoveEntityMappingType ``` |
| To | ``` case removeEntityMappingType ``` |

Modified [NSEntityMappingType.transformEntityMappingType](https://developer.apple.com/documentation/coredata/nsentitymappingtype/transformentitymappingtype)

|  | Declaration |
| --- | --- |
| From | ``` case TransformEntityMappingType ``` |
| To | ``` case transformEntityMappingType ``` |

Modified [NSEntityMappingType.undefinedEntityMappingType](https://developer.apple.com/documentation/coredata/nsentitymappingtype/nsundefinedentitymappingtype)

|  | Declaration |
| --- | --- |
| From | ``` case UndefinedEntityMappingType ``` |
| To | ``` case undefinedEntityMappingType ``` |

Modified [NSEntityMigrationPolicy](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSEntityMigrationPolicy : NSObject {     func beginEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func createDestinationInstancesForSourceInstance(_ sInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func endInstanceCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func createRelationshipsForDestinationInstance(_ dInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func endRelationshipCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func performCustomValidationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func endEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws } ``` | -- |
| To | ``` class NSEntityMigrationPolicy : NSObject {     func begin(_ mapping: NSEntityMapping, with manager: NSMigrationManager) throws     func createDestinationInstances(forSource sInstance: NSManagedObject, in mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func endInstanceCreation(forMapping mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func createRelationships(forDestination dInstance: NSManagedObject, in mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func endRelationshipCreation(forMapping mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func performCustomValidation(forMapping mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func end(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSEntityMigrationPolicy : CVarArg { } extension NSEntityMigrationPolicy : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NSEntityMigrationPolicy.begin(_: NSEntityMapping, with: NSMigrationManager) throws](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423785-beginentitymapping)

|  | Declaration |
| --- | --- |
| From | ``` func beginEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |
| To | ``` func begin(_ mapping: NSEntityMapping, with manager: NSMigrationManager) throws ``` |

Modified [NSEntityMigrationPolicy.createDestinationInstances(forSource: NSManagedObject, in: NSEntityMapping, manager: NSMigrationManager) throws](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423801-createdestinationinstances)

|  | Declaration |
| --- | --- |
| From | ``` func createDestinationInstancesForSourceInstance(_ sInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |
| To | ``` func createDestinationInstances(forSource sInstance: NSManagedObject, in mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |

Modified [NSEntityMigrationPolicy.createRelationships(forDestination: NSManagedObject, in: NSEntityMapping, manager: NSMigrationManager) throws](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423783-createrelationshipsfordestinatio)

|  | Declaration |
| --- | --- |
| From | ``` func createRelationshipsForDestinationInstance(_ dInstance: NSManagedObject, entityMapping mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |
| To | ``` func createRelationships(forDestination dInstance: NSManagedObject, in mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |

Modified [NSEntityMigrationPolicy.end(_: NSEntityMapping, manager: NSMigrationManager) throws](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423787-endentitymapping)

|  | Declaration |
| --- | --- |
| From | ``` func endEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |
| To | ``` func end(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |

Modified [NSEntityMigrationPolicy.endInstanceCreation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423805-endinstancecreation)

|  | Declaration |
| --- | --- |
| From | ``` func endInstanceCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |
| To | ``` func endInstanceCreation(forMapping mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |

Modified [NSEntityMigrationPolicy.endRelationshipCreation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423793-endrelationshipcreation)

|  | Declaration |
| --- | --- |
| From | ``` func endRelationshipCreationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |
| To | ``` func endRelationshipCreation(forMapping mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |

Modified [NSEntityMigrationPolicy.performCustomValidation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423791-performcustomvalidationforentity)

|  | Declaration |
| --- | --- |
| From | ``` func performCustomValidationForEntityMapping(_ mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |
| To | ``` func performCustomValidation(forMapping mapping: NSEntityMapping, manager manager: NSMigrationManager) throws ``` |

Modified [NSFetchedPropertyDescription](https://developer.apple.com/documentation/coredata/nsfetchedpropertydescription)

|  | Declaration |
| --- | --- |
| From | ``` class NSFetchedPropertyDescription : NSPropertyDescription {     var fetchRequest: NSFetchRequest? } ``` |
| To | ``` class NSFetchedPropertyDescription : NSPropertyDescription {     var fetchRequest: NSFetchRequest<NSFetchRequestResult>? } ``` |

Modified [NSFetchedPropertyDescription.fetchRequest](https://developer.apple.com/documentation/coredata/nsfetchedpropertydescription/1494679-fetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` var fetchRequest: NSFetchRequest? ``` |
| To | ``` var fetchRequest: NSFetchRequest<NSFetchRequestResult>? ``` |

Modified [NSFetchedResultsChangeType [enum]](https://developer.apple.com/documentation/coredata/nsfetchedresultschangetype)

|  | Declaration |
| --- | --- |
| From | ``` enum NSFetchedResultsChangeType : UInt {     case Insert     case Delete     case Move     case Update } ``` |
| To | ``` enum NSFetchedResultsChangeType : UInt {     case insert     case delete     case move     case update } ``` |

Modified [NSFetchedResultsChangeType.delete](https://developer.apple.com/documentation/coredata/nsfetchedresultschangetype/delete)

|  | Declaration |
| --- | --- |
| From | ``` case Delete ``` |
| To | ``` case delete ``` |

Modified [NSFetchedResultsChangeType.insert](https://developer.apple.com/documentation/coredata/nsfetchedresultschangetype/insert)

|  | Declaration |
| --- | --- |
| From | ``` case Insert ``` |
| To | ``` case insert ``` |

Modified [NSFetchedResultsChangeType.move](https://developer.apple.com/documentation/coredata/nsfetchedresultschangetype/move)

|  | Declaration |
| --- | --- |
| From | ``` case Move ``` |
| To | ``` case move ``` |

Modified [NSFetchedResultsChangeType.update](https://developer.apple.com/documentation/coredata/nsfetchedresultschangetype/update)

|  | Declaration |
| --- | --- |
| From | ``` case Update ``` |
| To | ``` case update ``` |

Modified [NSFetchedResultsController](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller)

|  | Declaration | Protocols | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` class NSFetchedResultsController : NSObject {     init(fetchRequest fetchRequest: NSFetchRequest, managedObjectContext context: NSManagedObjectContext, sectionNameKeyPath sectionNameKeyPath: String?, cacheName name: String?)     func performFetch() throws     var fetchRequest: NSFetchRequest { get }     var managedObjectContext: NSManagedObjectContext { get }     var sectionNameKeyPath: String? { get }     var cacheName: String? { get }     unowned(unsafe) var delegate: NSFetchedResultsControllerDelegate?     class func deleteCacheWithName(_ name: String?)     var fetchedObjects: [AnyObject]? { get }     func objectAtIndexPath(_ indexPath: NSIndexPath) -> AnyObject     func indexPathForObject(_ object: AnyObject) -> NSIndexPath?     func sectionIndexTitleForSectionName(_ sectionName: String) -> String?     var sectionIndexTitles: [String] { get }     var sections: [NSFetchedResultsSectionInfo]? { get }     func sectionForSectionIndexTitle(_ title: String, atIndex sectionIndex: Int) -> Int } ``` | -- | ```  ``` | -- |
| To | ``` class NSFetchedResultsController<ResultType : NSFetchRequestResult> : NSObject {     init(fetchRequest fetchRequest: NSFetchRequest<ResultType>, managedObjectContext context: NSManagedObjectContext, sectionNameKeyPath sectionNameKeyPath: String?, cacheName name: String?)     func performFetch() throws     var fetchRequest: NSFetchRequest<ResultType> { get }     var managedObjectContext: NSManagedObjectContext { get }     var sectionNameKeyPath: String? { get }     var cacheName: String? { get }     unowned(unsafe) var delegate: NSFetchedResultsControllerDelegate?     class func deleteCache(withName name: String?)     var fetchedObjects: [ResultType]? { get }     func object(at indexPath: IndexPath) -> ResultType     func indexPath(forObject object: ResultType) -> IndexPath?     func sectionIndexTitle(forSectionName sectionName: String) -> String?     var sectionIndexTitles: [String] { get }     var sections: [NSFetchedResultsSectionInfo]? { get }     func section(forSectionIndexTitle title: String, at sectionIndex: Int) -> Int     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSFetchedResultsController : CVarArg { } extension NSFetchedResultsController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable | ``` ResultType : NSFetchRequestResult ``` | ResultType |

Modified [NSFetchedResultsController.deleteCache(withName: String?) [class]](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622283-deletecachewithname)

|  | Declaration |
| --- | --- |
| From | ``` class func deleteCacheWithName(_ name: String?) ``` |
| To | ``` class func deleteCache(withName name: String?) ``` |

Modified [NSFetchedResultsController.fetchedObjects](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622278-fetchedobjects)

|  | Declaration |
| --- | --- |
| From | ``` var fetchedObjects: [AnyObject]? { get } ``` |
| To | ``` var fetchedObjects: [ResultType]? { get } ``` |

Modified [NSFetchedResultsController.fetchRequest](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622287-fetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` var fetchRequest: NSFetchRequest { get } ``` |
| To | ``` var fetchRequest: NSFetchRequest<ResultType> { get } ``` |

Modified [NSFetchedResultsController.indexPath(forObject: ResultType) -> IndexPath?](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622306-indexpathforobject)

|  | Declaration |
| --- | --- |
| From | ``` func indexPathForObject(_ object: AnyObject) -> NSIndexPath? ``` |
| To | ``` func indexPath(forObject object: ResultType) -> IndexPath? ``` |

Modified [NSFetchedResultsController.init(fetchRequest: NSFetchRequest<ResultType>, managedObjectContext: NSManagedObjectContext, sectionNameKeyPath: String?, cacheName: String?)](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622282-initwithfetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` init(fetchRequest fetchRequest: NSFetchRequest, managedObjectContext context: NSManagedObjectContext, sectionNameKeyPath sectionNameKeyPath: String?, cacheName name: String?) ``` |
| To | ``` init(fetchRequest fetchRequest: NSFetchRequest<ResultType>, managedObjectContext context: NSManagedObjectContext, sectionNameKeyPath sectionNameKeyPath: String?, cacheName name: String?) ``` |

Modified [NSFetchedResultsController.object(at: IndexPath) -> ResultType](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622281-object)

|  | Declaration |
| --- | --- |
| From | ``` func objectAtIndexPath(_ indexPath: NSIndexPath) -> AnyObject ``` |
| To | ``` func object(at indexPath: IndexPath) -> ResultType ``` |

Modified [NSFetchedResultsController.section(forSectionIndexTitle: String, at: Int) -> Int](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622284-sectionforsectionindextitle)

|  | Declaration |
| --- | --- |
| From | ``` func sectionForSectionIndexTitle(_ title: String, atIndex sectionIndex: Int) -> Int ``` |
| To | ``` func section(forSectionIndexTitle title: String, at sectionIndex: Int) -> Int ``` |

Modified [NSFetchedResultsController.sectionIndexTitle(forSectionName: String) -> String?](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/1622308-sectionindextitle)

|  | Declaration |
| --- | --- |
| From | ``` func sectionIndexTitleForSectionName(_ sectionName: String) -> String? ``` |
| To | ``` func sectionIndexTitle(forSectionName sectionName: String) -> String? ``` |

Modified [NSFetchedResultsControllerDelegate](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSFetchedResultsControllerDelegate : NSObjectProtocol {     optional func controller(_ controller: NSFetchedResultsController, didChangeObject anObject: AnyObject, atIndexPath indexPath: NSIndexPath?, forChangeType type: NSFetchedResultsChangeType, newIndexPath newIndexPath: NSIndexPath?)     optional func controller(_ controller: NSFetchedResultsController, didChangeSection sectionInfo: NSFetchedResultsSectionInfo, atIndex sectionIndex: Int, forChangeType type: NSFetchedResultsChangeType)     optional func controllerWillChangeContent(_ controller: NSFetchedResultsController)     optional func controllerDidChangeContent(_ controller: NSFetchedResultsController)     optional func controller(_ controller: NSFetchedResultsController, sectionIndexTitleForSectionName sectionName: String) -> String? } ``` |
| To | ``` protocol NSFetchedResultsControllerDelegate : NSObjectProtocol {     optional func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>, didChange anObject: Any, at indexPath: IndexPath?, for type: NSFetchedResultsChangeType, newIndexPath newIndexPath: IndexPath?)     optional func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>, didChange sectionInfo: NSFetchedResultsSectionInfo, atSectionIndex sectionIndex: Int, for type: NSFetchedResultsChangeType)     optional func controllerWillChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>)     optional func controllerDidChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>)     optional func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>, sectionIndexTitleForSectionName sectionName: String) -> String? } ``` |

Modified [NSFetchedResultsControllerDelegate.controller(_: NSFetchedResultsController<NSFetchRequestResult>, didChange: Any, at: IndexPath?, for: NSFetchedResultsChangeType, newIndexPath: IndexPath?)](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/1622296-controller)

|  | Declaration |
| --- | --- |
| From | ``` optional func controller(_ controller: NSFetchedResultsController, didChangeObject anObject: AnyObject, atIndexPath indexPath: NSIndexPath?, forChangeType type: NSFetchedResultsChangeType, newIndexPath newIndexPath: NSIndexPath?) ``` |
| To | ``` optional func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>, didChange anObject: Any, at indexPath: IndexPath?, for type: NSFetchedResultsChangeType, newIndexPath newIndexPath: IndexPath?) ``` |

Modified [NSFetchedResultsControllerDelegate.controller(_: NSFetchedResultsController<NSFetchRequestResult>, didChange: NSFetchedResultsSectionInfo, atSectionIndex: Int, for: NSFetchedResultsChangeType)](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/1622298-controller)

|  | Declaration |
| --- | --- |
| From | ``` optional func controller(_ controller: NSFetchedResultsController, didChangeSection sectionInfo: NSFetchedResultsSectionInfo, atIndex sectionIndex: Int, forChangeType type: NSFetchedResultsChangeType) ``` |
| To | ``` optional func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>, didChange sectionInfo: NSFetchedResultsSectionInfo, atSectionIndex sectionIndex: Int, for type: NSFetchedResultsChangeType) ``` |

Modified [NSFetchedResultsControllerDelegate.controller(_: NSFetchedResultsController<NSFetchRequestResult>, sectionIndexTitleForSectionName: String) -> String?](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/1622286-controller)

|  | Declaration |
| --- | --- |
| From | ``` optional func controller(_ controller: NSFetchedResultsController, sectionIndexTitleForSectionName sectionName: String) -> String? ``` |
| To | ``` optional func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>, sectionIndexTitleForSectionName sectionName: String) -> String? ``` |

Modified [NSFetchedResultsControllerDelegate.controllerDidChangeContent(_: NSFetchedResultsController<NSFetchRequestResult>)](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/1622290-controllerdidchangecontent)

|  | Declaration |
| --- | --- |
| From | ``` optional func controllerDidChangeContent(_ controller: NSFetchedResultsController) ``` |
| To | ``` optional func controllerDidChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) ``` |

Modified [NSFetchedResultsControllerDelegate.controllerWillChangeContent(_: NSFetchedResultsController<NSFetchRequestResult>)](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/1622295-controllerwillchangecontent)

|  | Declaration |
| --- | --- |
| From | ``` optional func controllerWillChangeContent(_ controller: NSFetchedResultsController) ``` |
| To | ``` optional func controllerWillChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) ``` |

Modified [NSFetchedResultsSectionInfo](https://developer.apple.com/documentation/coredata/nsfetchedresultssectioninfo)

|  | Declaration |
| --- | --- |
| From | ``` protocol NSFetchedResultsSectionInfo {     var name: String { get }     var indexTitle: String? { get }     var numberOfObjects: Int { get }     var objects: [AnyObject]? { get } } ``` |
| To | ``` protocol NSFetchedResultsSectionInfo {     var name: String { get }     var indexTitle: String? { get }     var numberOfObjects: Int { get }     var objects: [Any]? { get } } ``` |

Modified [NSFetchedResultsSectionInfo.objects](https://developer.apple.com/documentation/coredata/nsfetchedresultssectioninfo/1622293-objects)

|  | Declaration |
| --- | --- |
| From | ``` var objects: [AnyObject]? { get } ``` |
| To | ``` var objects: [Any]? { get } ``` |

Modified [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest)

|  | Declaration | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` class NSFetchRequest : NSPersistentStoreRequest, NSCoding {     convenience init(entityName entityName: String)     class func fetchRequestWithEntityName(_ entityName: String) -> Self     init()     convenience init(entityName entityName: String)     var entity: NSEntityDescription?     var entityName: String? { get }     var predicate: NSPredicate?     var sortDescriptors: [NSSortDescriptor]?     var fetchLimit: Int     var affectedStores: [NSPersistentStore]?     var resultType: NSFetchRequestResultType     var includesSubentities: Bool     var includesPropertyValues: Bool     var returnsObjectsAsFaults: Bool     var relationshipKeyPathsForPrefetching: [String]?     var includesPendingChanges: Bool     var returnsDistinctResults: Bool     var propertiesToFetch: [AnyObject]?     var fetchOffset: Int     var fetchBatchSize: Int     var shouldRefreshRefetchedObjects: Bool     var propertiesToGroupBy: [AnyObject]?     var havingPredicate: NSPredicate? } ``` | ```  ``` | -- |
| To | ``` class NSFetchRequest<ResultType : NSFetchRequestResult> : NSPersistentStoreRequest, NSCoding {     convenience init(entityName entityName: String)     class func withEntityName(_ entityName: String) -> Self     init()     convenience init(entityName entityName: String)     func execute() throws -> [ResultType]     var entity: NSEntityDescription?     var entityName: String? { get }     var predicate: NSPredicate?     var sortDescriptors: [NSSortDescriptor]?     var fetchLimit: Int     var affectedStores: [NSPersistentStore]?     var resultType: NSFetchRequestResultType     var includesSubentities: Bool     var includesPropertyValues: Bool     var returnsObjectsAsFaults: Bool     var relationshipKeyPathsForPrefetching: [String]?     var includesPendingChanges: Bool     var returnsDistinctResults: Bool     var propertiesToFetch: [Any]?     var fetchOffset: Int     var fetchBatchSize: Int     var shouldRefreshRefetchedObjects: Bool     var propertiesToGroupBy: [Any]?     var havingPredicate: NSPredicate? } ``` | ``` ResultType : NSFetchRequestResult ``` | ResultType |

Modified [NSFetchRequest.propertiesToFetch](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506851-propertiestofetch)

|  | Declaration |
| --- | --- |
| From | ``` var propertiesToFetch: [AnyObject]? ``` |
| To | ``` var propertiesToFetch: [Any]? ``` |

Modified [NSFetchRequest.propertiesToGroupBy](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506191-propertiestogroupby)

|  | Declaration |
| --- | --- |
| From | ``` var propertiesToGroupBy: [AnyObject]? ``` |
| To | ``` var propertiesToGroupBy: [Any]? ``` |

Modified [NSFetchRequestExpression](https://developer.apple.com/documentation/coredata/nsfetchrequestexpression)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSFetchRequestExpression : NSExpression {     class func expressionForFetch(_ fetch: NSExpression, context context: NSExpression, countOnly countFlag: Bool) -> NSExpression     var requestExpression: NSExpression { get }     var contextExpression: NSExpression { get }     var countOnlyRequest: Bool { get } } ``` | -- |
| To | ``` class NSFetchRequestExpression : NSExpression {     class func expression(forFetch fetch: NSExpression, context context: NSExpression, countOnly countFlag: Bool) -> NSExpression     var requestExpression: NSExpression { get }     var contextExpression: NSExpression { get }     var isCountOnlyRequest: Bool { get }     convenience init(format expressionFormat: String, _ args: CVarArg...)     enum ExpressionType : UInt {         case constantValue         case evaluatedObject         case variable         case keyPath         case function         case unionSet         case intersectSet         case minusSet         case subquery         case aggregate         case anyKey         case block         case conditional     }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSFetchRequestExpression : CVarArg { } extension NSFetchRequestExpression : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NSFetchRequestExpression.expression(forFetch: NSExpression, context: NSExpression, countOnly: Bool) -> NSExpression [class]](https://developer.apple.com/documentation/coredata/nsfetchrequestexpression/1391661-expression)

|  | Declaration |
| --- | --- |
| From | ``` class func expressionForFetch(_ fetch: NSExpression, context context: NSExpression, countOnly countFlag: Bool) -> NSExpression ``` |
| To | ``` class func expression(forFetch fetch: NSExpression, context context: NSExpression, countOnly countFlag: Bool) -> NSExpression ``` |

Modified [NSFetchRequestExpression.isCountOnlyRequest](https://developer.apple.com/documentation/coredata/nsfetchrequestexpression/1391670-countonlyrequest)

|  | Declaration |
| --- | --- |
| From | ``` var countOnlyRequest: Bool { get } ``` |
| To | ``` var isCountOnlyRequest: Bool { get } ``` |

Modified [NSFetchRequestResultType [struct]](https://developer.apple.com/documentation/coredata/nsfetchrequestresulttype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSFetchRequestResultType : OptionSetType {     init(rawValue rawValue: UInt)     static var ManagedObjectResultType: NSFetchRequestResultType { get }     static var ManagedObjectIDResultType: NSFetchRequestResultType { get }     static var DictionaryResultType: NSFetchRequestResultType { get }     static var CountResultType: NSFetchRequestResultType { get } } ``` | OptionSetType |
| To | ``` struct NSFetchRequestResultType : OptionSet {     init(rawValue rawValue: UInt)     static var managedObjectResultType: NSFetchRequestResultType { get }     static var managedObjectIDResultType: NSFetchRequestResultType { get }     static var dictionaryResultType: NSFetchRequestResultType { get }     static var countResultType: NSFetchRequestResultType { get }     func intersect(_ other: NSFetchRequestResultType) -> NSFetchRequestResultType     func exclusiveOr(_ other: NSFetchRequestResultType) -> NSFetchRequestResultType     mutating func unionInPlace(_ other: NSFetchRequestResultType)     mutating func intersectInPlace(_ other: NSFetchRequestResultType)     mutating func exclusiveOrInPlace(_ other: NSFetchRequestResultType)     func isSubsetOf(_ other: NSFetchRequestResultType) -> Bool     func isDisjointWith(_ other: NSFetchRequestResultType) -> Bool     func isSupersetOf(_ other: NSFetchRequestResultType) -> Bool     mutating func subtractInPlace(_ other: NSFetchRequestResultType)     func isStrictSupersetOf(_ other: NSFetchRequestResultType) -> Bool     func isStrictSubsetOf(_ other: NSFetchRequestResultType) -> Bool } extension NSFetchRequestResultType {     func union(_ other: NSFetchRequestResultType) -> NSFetchRequestResultType     func intersection(_ other: NSFetchRequestResultType) -> NSFetchRequestResultType     func symmetricDifference(_ other: NSFetchRequestResultType) -> NSFetchRequestResultType } extension NSFetchRequestResultType {     func contains(_ member: NSFetchRequestResultType) -> Bool     mutating func insert(_ newMember: NSFetchRequestResultType) -> (inserted: Bool, memberAfterInsert: NSFetchRequestResultType)     mutating func remove(_ member: NSFetchRequestResultType) -> NSFetchRequestResultType?     mutating func update(with newMember: NSFetchRequestResultType) -> NSFetchRequestResultType? } extension NSFetchRequestResultType {     convenience init()     mutating func formUnion(_ other: NSFetchRequestResultType)     mutating func formIntersection(_ other: NSFetchRequestResultType)     mutating func formSymmetricDifference(_ other: NSFetchRequestResultType) } extension NSFetchRequestResultType {     convenience init<S : Sequence where S.Iterator.Element == NSFetchRequestResultType>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: NSFetchRequestResultType...)     mutating func subtract(_ other: NSFetchRequestResultType)     func isSubset(of other: NSFetchRequestResultType) -> Bool     func isSuperset(of other: NSFetchRequestResultType) -> Bool     func isDisjoint(with other: NSFetchRequestResultType) -> Bool     func subtracting(_ other: NSFetchRequestResultType) -> NSFetchRequestResultType     var isEmpty: Bool { get }     func isStrictSuperset(of other: NSFetchRequestResultType) -> Bool     func isStrictSubset(of other: NSFetchRequestResultType) -> Bool } ``` | OptionSet |

Modified [NSFetchRequestResultType.countResultType](https://developer.apple.com/documentation/coredata/nsfetchrequestresulttype/1506211-countresulttype)

|  | Declaration |
| --- | --- |
| From | ``` static var CountResultType: NSFetchRequestResultType { get } ``` |
| To | ``` static var countResultType: NSFetchRequestResultType { get } ``` |

Modified [NSFetchRequestResultType.dictionaryResultType](https://developer.apple.com/documentation/coredata/nsfetchrequestresulttype/1506237-dictionaryresulttype)

|  | Declaration |
| --- | --- |
| From | ``` static var DictionaryResultType: NSFetchRequestResultType { get } ``` |
| To | ``` static var dictionaryResultType: NSFetchRequestResultType { get } ``` |

Modified [NSFetchRequestResultType.managedObjectIDResultType](https://developer.apple.com/documentation/coredata/nsfetchrequestresulttype/nsmanagedobjectidresulttype)

|  | Declaration |
| --- | --- |
| From | ``` static var ManagedObjectIDResultType: NSFetchRequestResultType { get } ``` |
| To | ``` static var managedObjectIDResultType: NSFetchRequestResultType { get } ``` |

Modified [NSFetchRequestResultType.managedObjectResultType](https://developer.apple.com/documentation/coredata/nsfetchrequestresulttype/1506452-managedobjectresulttype)

|  | Declaration |
| --- | --- |
| From | ``` static var ManagedObjectResultType: NSFetchRequestResultType { get } ``` |
| To | ``` static var managedObjectResultType: NSFetchRequestResultType { get } ``` |

Modified [NSIncrementalStore](https://developer.apple.com/documentation/coredata/nsincrementalstore)

|  | Declaration |
| --- | --- |
| From | ``` class NSIncrementalStore : NSPersistentStore {     func loadMetadata() throws     func executeRequest(_ request: NSPersistentStoreRequest, withContext context: NSManagedObjectContext?) throws -> AnyObject     func newValuesForObjectWithID(_ objectID: NSManagedObjectID, withContext context: NSManagedObjectContext) throws -> NSIncrementalStoreNode     func newValueForRelationship(_ relationship: NSRelationshipDescription, forObjectWithID objectID: NSManagedObjectID, withContext context: NSManagedObjectContext?) throws -> AnyObject     class func identifierForNewStoreAtURL(_ storeURL: NSURL) -> AnyObject     func obtainPermanentIDsForObjects(_ array: [NSManagedObject]) throws -> [NSManagedObjectID]     func managedObjectContextDidRegisterObjectsWithIDs(_ objectIDs: [NSManagedObjectID])     func managedObjectContextDidUnregisterObjectsWithIDs(_ objectIDs: [NSManagedObjectID])     func newObjectIDForEntity(_ entity: NSEntityDescription, referenceObject data: AnyObject) -> NSManagedObjectID     func referenceObjectForObjectID(_ objectID: NSManagedObjectID) -> AnyObject } ``` |
| To | ``` class NSIncrementalStore : NSPersistentStore {     func loadMetadata() throws     func execute(_ request: NSPersistentStoreRequest, with context: NSManagedObjectContext?) throws -> Any     func newValuesForObject(with objectID: NSManagedObjectID, with context: NSManagedObjectContext) throws -> NSIncrementalStoreNode     func newValue(forRelationship relationship: NSRelationshipDescription, forObjectWith objectID: NSManagedObjectID, with context: NSManagedObjectContext?) throws -> Any     class func identifierForNewStore(at storeURL: URL) -> Any     func obtainPermanentIDs(for array: [NSManagedObject]) throws -> [NSManagedObjectID]     func managedObjectContextDidRegisterObjects(with objectIDs: [NSManagedObjectID])     func managedObjectContextDidUnregisterObjects(with objectIDs: [NSManagedObjectID])     func newObjectID(for entity: NSEntityDescription, referenceObject data: Any) -> NSManagedObjectID     func referenceObject(for objectID: NSManagedObjectID) -> Any } ``` |

Modified [NSIncrementalStore.execute(_: NSPersistentStoreRequest, with: NSManagedObjectContext?) throws -> Any](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506653-executerequest)

|  | Declaration |
| --- | --- |
| From | ``` func executeRequest(_ request: NSPersistentStoreRequest, withContext context: NSManagedObjectContext?) throws -> AnyObject ``` |
| To | ``` func execute(_ request: NSPersistentStoreRequest, with context: NSManagedObjectContext?) throws -> Any ``` |

Modified [NSIncrementalStore.identifierForNewStore(at: URL) -> Any [class]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506781-identifierfornewstore)

|  | Declaration |
| --- | --- |
| From | ``` class func identifierForNewStoreAtURL(_ storeURL: NSURL) -> AnyObject ``` |
| To | ``` class func identifierForNewStore(at storeURL: URL) -> Any ``` |

Modified [NSIncrementalStore.managedObjectContextDidRegisterObjects(with: [NSManagedObjectID])](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506199-managedobjectcontextdidregistero)

|  | Declaration |
| --- | --- |
| From | ``` func managedObjectContextDidRegisterObjectsWithIDs(_ objectIDs: [NSManagedObjectID]) ``` |
| To | ``` func managedObjectContextDidRegisterObjects(with objectIDs: [NSManagedObjectID]) ``` |

Modified [NSIncrementalStore.managedObjectContextDidUnregisterObjects(with: [NSManagedObjectID])](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506878-managedobjectcontextdidunregiste)

|  | Declaration |
| --- | --- |
| From | ``` func managedObjectContextDidUnregisterObjectsWithIDs(_ objectIDs: [NSManagedObjectID]) ``` |
| To | ``` func managedObjectContextDidUnregisterObjects(with objectIDs: [NSManagedObjectID]) ``` |

Modified [NSIncrementalStore.newObjectID(for: NSEntityDescription, referenceObject: Any) -> NSManagedObjectID](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506666-newobjectidforentity)

|  | Declaration |
| --- | --- |
| From | ``` func newObjectIDForEntity(_ entity: NSEntityDescription, referenceObject data: AnyObject) -> NSManagedObjectID ``` |
| To | ``` func newObjectID(for entity: NSEntityDescription, referenceObject data: Any) -> NSManagedObjectID ``` |

Modified [NSIncrementalStore.newValue(forRelationship: NSRelationshipDescription, forObjectWith: NSManagedObjectID, with: NSManagedObjectContext?) throws -> Any](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506438-newvalue)

|  | Declaration |
| --- | --- |
| From | ``` func newValueForRelationship(_ relationship: NSRelationshipDescription, forObjectWithID objectID: NSManagedObjectID, withContext context: NSManagedObjectContext?) throws -> AnyObject ``` |
| To | ``` func newValue(forRelationship relationship: NSRelationshipDescription, forObjectWith objectID: NSManagedObjectID, with context: NSManagedObjectContext?) throws -> Any ``` |

Modified [NSIncrementalStore.newValuesForObject(with: NSManagedObjectID, with: NSManagedObjectContext) throws -> NSIncrementalStoreNode](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506729-newvaluesforobject)

|  | Declaration |
| --- | --- |
| From | ``` func newValuesForObjectWithID(_ objectID: NSManagedObjectID, withContext context: NSManagedObjectContext) throws -> NSIncrementalStoreNode ``` |
| To | ``` func newValuesForObject(with objectID: NSManagedObjectID, with context: NSManagedObjectContext) throws -> NSIncrementalStoreNode ``` |

Modified [NSIncrementalStore.obtainPermanentIDs(for: [NSManagedObject]) throws -> [NSManagedObjectID]](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506348-obtainpermanentidsforobjects)

|  | Declaration |
| --- | --- |
| From | ``` func obtainPermanentIDsForObjects(_ array: [NSManagedObject]) throws -> [NSManagedObjectID] ``` |
| To | ``` func obtainPermanentIDs(for array: [NSManagedObject]) throws -> [NSManagedObjectID] ``` |

Modified [NSIncrementalStore.referenceObject(for: NSManagedObjectID) -> Any](https://developer.apple.com/documentation/coredata/nsincrementalstore/1506828-referenceobject)

|  | Declaration |
| --- | --- |
| From | ``` func referenceObjectForObjectID(_ objectID: NSManagedObjectID) -> AnyObject ``` |
| To | ``` func referenceObject(for objectID: NSManagedObjectID) -> Any ``` |

Modified [NSIncrementalStoreNode](https://developer.apple.com/documentation/coredata/nsincrementalstorenode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSIncrementalStoreNode : NSObject {     init(objectID objectID: NSManagedObjectID, withValues values: [String : AnyObject], version version: UInt64)     func updateWithValues(_ values: [String : AnyObject], version version: UInt64)     var objectID: NSManagedObjectID { get }     var version: UInt64 { get }     func valueForPropertyDescription(_ prop: NSPropertyDescription) -> AnyObject? } ``` | -- |
| To | ``` class NSIncrementalStoreNode : NSObject {     init(objectID objectID: NSManagedObjectID, withValues values: [String : Any], version version: UInt64)     func update(withValues values: [String : Any], version version: UInt64)     var objectID: NSManagedObjectID { get }     var version: UInt64 { get }     func value(for prop: NSPropertyDescription) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSIncrementalStoreNode : CVarArg { } extension NSIncrementalStoreNode : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NSIncrementalStoreNode.init(objectID: NSManagedObjectID, withValues: [String : Any], version: UInt64)](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506321-initwithobjectid)

|  | Declaration |
| --- | --- |
| From | ``` init(objectID objectID: NSManagedObjectID, withValues values: [String : AnyObject], version version: UInt64) ``` |
| To | ``` init(objectID objectID: NSManagedObjectID, withValues values: [String : Any], version version: UInt64) ``` |

Modified [NSIncrementalStoreNode.update(withValues: [String : Any], version: UInt64)](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506721-update)

|  | Declaration |
| --- | --- |
| From | ``` func updateWithValues(_ values: [String : AnyObject], version version: UInt64) ``` |
| To | ``` func update(withValues values: [String : Any], version version: UInt64) ``` |

Modified [NSIncrementalStoreNode.value(for: NSPropertyDescription) -> Any?](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/1506442-value)

|  | Declaration |
| --- | --- |
| From | ``` func valueForPropertyDescription(_ prop: NSPropertyDescription) -> AnyObject? ``` |
| To | ``` func value(for prop: NSPropertyDescription) -> Any? ``` |

Modified [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSManagedObject : NSObject {     class func contextShouldIgnoreUnmodeledPropertyChanges() -> Bool     init(entity entity: NSEntityDescription, insertIntoManagedObjectContext context: NSManagedObjectContext?)     unowned(unsafe) var managedObjectContext: NSManagedObjectContext? { get }     var entity: NSEntityDescription { get }     var objectID: NSManagedObjectID { get }     var inserted: Bool { get }     var updated: Bool { get }     var deleted: Bool { get }     var hasChanges: Bool { get }     var hasPersistentChangedValues: Bool { get }     var fault: Bool { get }     func hasFaultForRelationshipNamed(_ key: String) -> Bool     func objectIDsForRelationshipNamed(_ key: String) -> [NSManagedObjectID]     var faultingState: Int { get }     func willAccessValueForKey(_ key: String?)     func didAccessValueForKey(_ key: String?)     func willChangeValueForKey(_ key: String)     func didChangeValueForKey(_ key: String)     func willChangeValueForKey(_ inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: Set<NSObject>)     func didChangeValueForKey(_ inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: Set<NSObject>)     func awakeFromFetch()     func awakeFromInsert()     func awakeFromSnapshotEvents(_ flags: NSSnapshotEventType)     func prepareForDeletion()     func willSave()     func didSave()     func willTurnIntoFault()     func didTurnIntoFault()     func valueForKey(_ key: String) -> AnyObject?     func setValue(_ value: AnyObject?, forKey key: String)     func primitiveValueForKey(_ key: String) -> AnyObject?     func setPrimitiveValue(_ value: AnyObject?, forKey key: String)     func committedValuesForKeys(_ keys: [String]?) -> [String : AnyObject]     func changedValues() -> [String : AnyObject]     func changedValuesForCurrentEvent() -> [String : AnyObject]     func validateValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String) throws     func validateForDelete() throws     func validateForInsert() throws     func validateForUpdate() throws } ``` | -- |
| To | ``` class NSManagedObject : NSObject {     class var contextShouldIgnoreUnmodeledPropertyChanges: Bool { get }     class func entity() -> NSEntityDescription     class func fetchRequest() -> NSFetchRequest<NSFetchRequestResult>     init(entity entity: NSEntityDescription, insertInto context: NSManagedObjectContext?)     convenience init(context moc: NSManagedObjectContext)     unowned(unsafe) var managedObjectContext: NSManagedObjectContext? { get }     var entity: NSEntityDescription { get }     var objectID: NSManagedObjectID { get }     var isInserted: Bool { get }     var isUpdated: Bool { get }     var isDeleted: Bool { get }     var hasChanges: Bool { get }     var hasPersistentChangedValues: Bool { get }     var isFault: Bool { get }     func hasFault(forRelationshipNamed key: String) -> Bool     func objectIDs(forRelationshipNamed key: String) -> [NSManagedObjectID]     var faultingState: Int { get }     func willAccessValue(forKey key: String?)     func didAccessValue(forKey key: String?)     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChangeValue(forKey inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, using inObjects: Set<AnyHashable>)     func didChangeValue(forKey inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, using inObjects: Set<AnyHashable>)     func awakeFromFetch()     func awakeFromInsert()     func awake(fromSnapshotEvents flags: NSSnapshotEventType)     func prepareForDeletion()     func willSave()     func didSave()     func willTurnIntoFault()     func didTurnIntoFault()     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func primitiveValue(forKey key: String) -> Any?     func setPrimitiveValue(_ value: Any?, forKey key: String)     func committedValues(forKeys keys: [String]?) -> [String : Any]     func changedValues() -> [String : Any]     func changedValuesForCurrentEvent() -> [String : Any]     func validateValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: String) throws     func validateForDelete() throws     func validateForInsert() throws     func validateForUpdate() throws     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSManagedObject : NSFetchRequestResult { } extension NSManagedObject : CVarArg { } extension NSManagedObject : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSFetchRequestResult |

Modified [NSManagedObject.awake(fromSnapshotEvents: NSSnapshotEventType)](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506861-awake)

|  | Declaration |
| --- | --- |
| From | ``` func awakeFromSnapshotEvents(_ flags: NSSnapshotEventType) ``` |
| To | ``` func awake(fromSnapshotEvents flags: NSSnapshotEventType) ``` |

Modified [NSManagedObject.changedValues() -> [String : Any]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506775-changedvalues)

|  | Declaration |
| --- | --- |
| From | ``` func changedValues() -> [String : AnyObject] ``` |
| To | ``` func changedValues() -> [String : Any] ``` |

Modified [NSManagedObject.changedValuesForCurrentEvent() -> [String : Any]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506472-changedvaluesforcurrentevent)

|  | Declaration |
| --- | --- |
| From | ``` func changedValuesForCurrentEvent() -> [String : AnyObject] ``` |
| To | ``` func changedValuesForCurrentEvent() -> [String : Any] ``` |

Modified [NSManagedObject.committedValues(forKeys: [String]?) -> [String : Any]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506771-committedvaluesforkeys)

|  | Declaration |
| --- | --- |
| From | ``` func committedValuesForKeys(_ keys: [String]?) -> [String : AnyObject] ``` |
| To | ``` func committedValues(forKeys keys: [String]?) -> [String : Any] ``` |

Modified [NSManagedObject.didAccessValue(forKey: String?)](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506865-didaccessvalue)

|  | Declaration |
| --- | --- |
| From | ``` func didAccessValueForKey(_ key: String?) ``` |
| To | ``` func didAccessValue(forKey key: String?) ``` |

Modified [NSManagedObject.didChangeValue(forKey: String)](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506976-didchangevalue)

|  | Declaration |
| --- | --- |
| From | ``` func didChangeValueForKey(_ key: String) ``` |
| To | ``` func didChangeValue(forKey key: String) ``` |

Modified [NSManagedObject.didChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506936-didchangevalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` func didChangeValueForKey(_ inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: Set<NSObject>) ``` |
| To | ``` func didChangeValue(forKey inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, using inObjects: Set<AnyHashable>) ``` |

Modified [NSManagedObject.hasFault(forRelationshipNamed: String) -> Bool](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506973-hasfaultforrelationshipnamed)

|  | Declaration |
| --- | --- |
| From | ``` func hasFaultForRelationshipNamed(_ key: String) -> Bool ``` |
| To | ``` func hasFault(forRelationshipNamed key: String) -> Bool ``` |

Modified [NSManagedObject.init(entity: NSEntityDescription, insertInto: NSManagedObjectContext?)](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506357-init)

|  | Declaration |
| --- | --- |
| From | ``` init(entity entity: NSEntityDescription, insertIntoManagedObjectContext context: NSManagedObjectContext?) ``` |
| To | ``` init(entity entity: NSEntityDescription, insertInto context: NSManagedObjectContext?) ``` |

Modified [NSManagedObject.isDeleted](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506681-deleted)

|  | Declaration |
| --- | --- |
| From | ``` var deleted: Bool { get } ``` |
| To | ``` var isDeleted: Bool { get } ``` |

Modified [NSManagedObject.isFault](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506837-isfault)

|  | Declaration |
| --- | --- |
| From | ``` var fault: Bool { get } ``` |
| To | ``` var isFault: Bool { get } ``` |

Modified [NSManagedObject.isInserted](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506281-inserted)

|  | Declaration |
| --- | --- |
| From | ``` var inserted: Bool { get } ``` |
| To | ``` var isInserted: Bool { get } ``` |

Modified [NSManagedObject.isUpdated](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506867-updated)

|  | Declaration |
| --- | --- |
| From | ``` var updated: Bool { get } ``` |
| To | ``` var isUpdated: Bool { get } ``` |

Modified [NSManagedObject.objectIDs(forRelationshipNamed: String) -> [NSManagedObjectID]](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506201-objectidsforrelationshipnamed)

|  | Declaration |
| --- | --- |
| From | ``` func objectIDsForRelationshipNamed(_ key: String) -> [NSManagedObjectID] ``` |
| To | ``` func objectIDs(forRelationshipNamed key: String) -> [NSManagedObjectID] ``` |

Modified [NSManagedObject.primitiveValue(forKey: String) -> Any?](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506728-primitivevalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` func primitiveValueForKey(_ key: String) -> AnyObject? ``` |
| To | ``` func primitiveValue(forKey key: String) -> Any? ``` |

Modified [NSManagedObject.setPrimitiveValue(_: Any?, forKey: String)](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506960-setprimitivevalue)

|  | Declaration |
| --- | --- |
| From | ``` func setPrimitiveValue(_ value: AnyObject?, forKey key: String) ``` |
| To | ``` func setPrimitiveValue(_ value: Any?, forKey key: String) ``` |

Modified [NSManagedObject.setValue(_: Any?, forKey: String)](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506397-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` func setValue(_ value: AnyObject?, forKey key: String) ``` |
| To | ``` func setValue(_ value: Any?, forKey key: String) ``` |

Modified [NSManagedObject.value(forKey: String) -> Any?](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506613-value)

|  | Declaration |
| --- | --- |
| From | ``` func valueForKey(_ key: String) -> AnyObject? ``` |
| To | ``` func value(forKey key: String) -> Any? ``` |

Modified [NSManagedObject.willAccessValue(forKey: String?)](https://developer.apple.com/documentation/coredata/nsmanagedobject/1507001-willaccessvalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` func willAccessValueForKey(_ key: String?) ``` |
| To | ``` func willAccessValue(forKey key: String?) ``` |

Modified [NSManagedObject.willChangeValue(forKey: String)](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506229-willchangevalue)

|  | Declaration |
| --- | --- |
| From | ``` func willChangeValueForKey(_ key: String) ``` |
| To | ``` func willChangeValue(forKey key: String) ``` |

Modified [NSManagedObject.willChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506801-willchangevalue)

|  | Declaration |
| --- | --- |
| From | ``` func willChangeValueForKey(_ inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, usingObjects inObjects: Set<NSObject>) ``` |
| To | ``` func willChangeValue(forKey inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, using inObjects: Set<AnyHashable>) ``` |

Modified [NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSManagedObjectContext : NSObject, NSCoding, NSLocking {     class func new() -> Self     convenience init()     init(concurrencyType ct: NSManagedObjectContextConcurrencyType)     func performBlock(_ block: () -> Void)     func performBlockAndWait(_ block: () -> Void)     var persistentStoreCoordinator: NSPersistentStoreCoordinator?     var parentContext: NSManagedObjectContext?     var name: String?     var undoManager: NSUndoManager?     var hasChanges: Bool { get }     var userInfo: NSMutableDictionary { get }     var concurrencyType: NSManagedObjectContextConcurrencyType { get }     func objectRegisteredForID(_ objectID: NSManagedObjectID) -> NSManagedObject?     func objectWithID(_ objectID: NSManagedObjectID) -> NSManagedObject     func existingObjectWithID(_ objectID: NSManagedObjectID) throws -> NSManagedObject     func executeFetchRequest(_ request: NSFetchRequest) throws -> [AnyObject]     func countForFetchRequest(_ request: NSFetchRequest, error error: NSErrorPointer) -> Int     func executeRequest(_ request: NSPersistentStoreRequest) throws -> NSPersistentStoreResult     func insertObject(_ object: NSManagedObject)     func deleteObject(_ object: NSManagedObject)     func refreshObject(_ object: NSManagedObject, mergeChanges flag: Bool)     func detectConflictsForObject(_ object: NSManagedObject)     func observeValueForKeyPath(_ keyPath: String?, ofObject object: AnyObject?, change change: [String : AnyObject]?, context context: UnsafeMutablePointer<Void>)     func processPendingChanges()     func assignObject(_ object: AnyObject, toPersistentStore store: NSPersistentStore)     var insertedObjects: Set<NSManagedObject> { get }     var updatedObjects: Set<NSManagedObject> { get }     var deletedObjects: Set<NSManagedObject> { get }     var registeredObjects: Set<NSManagedObject> { get }     func undo()     func redo()     func reset()     func rollback()     func save() throws     func refreshAllObjects()     func lock()     func unlock()     func tryLock() -> Bool     var propagatesDeletesAtEndOfEvent: Bool     var retainsRegisteredObjects: Bool     var shouldDeleteInaccessibleFaults: Bool     func shouldHandleInaccessibleFault(_ fault: NSManagedObject, forObjectID oid: NSManagedObjectID, triggeredByProperty property: NSPropertyDescription?) -> Bool     var stalenessInterval: NSTimeInterval     var mergePolicy: AnyObject     func obtainPermanentIDsForObjects(_ objects: [NSManagedObject]) throws     func mergeChangesFromContextDidSaveNotification(_ notification: NSNotification)     class func mergeChangesFromRemoteContextSave(_ changeNotificationData: [NSObject : AnyObject], intoContexts contexts: [NSManagedObjectContext]) } ``` | NSCoding, NSLocking |
| To | ``` class NSManagedObjectContext : NSObject, NSCoding, NSLocking {     class func new() -> Self     convenience init()     init(concurrencyType ct: NSManagedObjectContextConcurrencyType)     func perform(_ block: @escaping () -> Swift.Void)     func performAndWait(_ block: @escaping () -> Swift.Void)     var persistentStoreCoordinator: NSPersistentStoreCoordinator?     var parent: NSManagedObjectContext?     var name: String?     var undoManager: UndoManager?     var hasChanges: Bool { get }     var userInfo: NSMutableDictionary { get }     var concurrencyType: NSManagedObjectContextConcurrencyType { get }     func registeredObject(for objectID: NSManagedObjectID) -> NSManagedObject?     func object(with objectID: NSManagedObjectID) -> NSManagedObject     func existingObject(with objectID: NSManagedObjectID) throws -> NSManagedObject     func fetch(_ request: NSFetchRequest<NSFetchRequestResult>) throws -> [Any]     func count(for request: NSFetchRequest<NSFetchRequestResult>) throws -> Int     func execute(_ request: NSPersistentStoreRequest) throws -> NSPersistentStoreResult     func insert(_ object: NSManagedObject)     func delete(_ object: NSManagedObject)     func refresh(_ object: NSManagedObject, mergeChanges flag: Bool)     func detectConflicts(for object: NSManagedObject)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [String : Any]?, context context: UnsafeMutableRawPointer?)     func processPendingChanges()     func assign(_ object: Any, to store: NSPersistentStore)     var insertedObjects: Set<NSManagedObject> { get }     var updatedObjects: Set<NSManagedObject> { get }     var deletedObjects: Set<NSManagedObject> { get }     var registeredObjects: Set<NSManagedObject> { get }     func undo()     func redo()     func reset()     func rollback()     func save() throws     func refreshAllObjects()     func lock()     func unlock()     func tryLock() -> Bool     var propagatesDeletesAtEndOfEvent: Bool     var retainsRegisteredObjects: Bool     var shouldDeleteInaccessibleFaults: Bool     func shouldHandleInaccessibleFault(_ fault: NSManagedObject, for oid: NSManagedObjectID, triggeredByProperty property: NSPropertyDescription?) -> Bool     var stalenessInterval: TimeInterval     var mergePolicy: Any     func obtainPermanentIDs(for objects: [NSManagedObject]) throws     func mergeChanges(fromContextDidSave notification: Notification)     class func mergeChanges(fromRemoteContextSave changeNotificationData: [AnyHashable : Any], into contexts: [NSManagedObjectContext])     var queryGenerationToken: NSQueryGenerationToken? { get }     func setQueryGenerationFrom(_ generation: NSQueryGenerationToken?) throws     var automaticallyMergesChangesFromParent: Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSManagedObjectContext : CVarArg { } extension NSManagedObjectContext : Equatable, Hashable {     var hashValue: Int { get } } extension NSManagedObjectContext {     func fetch<T : NSFetchRequestResult>(_ request: NSFetchRequest<T>) throws -> [T]     func count<T : NSFetchRequestResult>(for request: NSFetchRequest<T>) throws -> Int } ``` | CVarArg, Equatable, Hashable, NSCoding, NSLocking |

Modified [NSManagedObjectContext.assign(_: Any, to: NSPersistentStore)](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506436-assignobject)

|  | Declaration |
| --- | --- |
| From | ``` func assignObject(_ object: AnyObject, toPersistentStore store: NSPersistentStore) ``` |
| To | ``` func assign(_ object: Any, to store: NSPersistentStore) ``` |

Modified [NSManagedObjectContext.count(for: NSFetchRequest<NSFetchRequestResult>) throws -> Int](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506868-countforfetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` func countForFetchRequest(_ request: NSFetchRequest, error error: NSErrorPointer) -> Int ``` |
| To | ``` func count(for request: NSFetchRequest<NSFetchRequestResult>) throws -> Int ``` |

Modified [NSManagedObjectContext.delete(_: NSManagedObject)](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506847-deleteobject)

|  | Declaration |
| --- | --- |
| From | ``` func deleteObject(_ object: NSManagedObject) ``` |
| To | ``` func delete(_ object: NSManagedObject) ``` |

Modified [NSManagedObjectContext.detectConflicts(for: NSManagedObject)](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506843-detectconflictsforobject)

|  | Declaration |
| --- | --- |
| From | ``` func detectConflictsForObject(_ object: NSManagedObject) ``` |
| To | ``` func detectConflicts(for object: NSManagedObject) ``` |

Modified [NSManagedObjectContext.execute(_: NSPersistentStoreRequest) throws -> NSPersistentStoreResult](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506834-execute)

|  | Declaration |
| --- | --- |
| From | ``` func executeRequest(_ request: NSPersistentStoreRequest) throws -> NSPersistentStoreResult ``` |
| To | ``` func execute(_ request: NSPersistentStoreRequest) throws -> NSPersistentStoreResult ``` |

Modified [NSManagedObjectContext.existingObject(with: NSManagedObjectID) throws -> NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506686-existingobject)

|  | Declaration |
| --- | --- |
| From | ``` func existingObjectWithID(_ objectID: NSManagedObjectID) throws -> NSManagedObject ``` |
| To | ``` func existingObject(with objectID: NSManagedObjectID) throws -> NSManagedObject ``` |

Modified [NSManagedObjectContext.fetch(_: NSFetchRequest<NSFetchRequestResult>) throws -> [Any]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506672-executefetchrequest)

|  | Declaration |
| --- | --- |
| From | ``` func executeFetchRequest(_ request: NSFetchRequest) throws -> [AnyObject] ``` |
| To | ``` func fetch(_ request: NSFetchRequest<NSFetchRequestResult>) throws -> [Any] ``` |

Modified [NSManagedObjectContext.insert(_: NSManagedObject)](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506794-insertobject)

|  | Declaration |
| --- | --- |
| From | ``` func insertObject(_ object: NSManagedObject) ``` |
| To | ``` func insert(_ object: NSManagedObject) ``` |

Modified [NSManagedObjectContext.mergeChanges(fromContextDidSave: Notification)](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506606-mergechanges)

|  | Declaration |
| --- | --- |
| From | ``` func mergeChangesFromContextDidSaveNotification(_ notification: NSNotification) ``` |
| To | ``` func mergeChanges(fromContextDidSave notification: Notification) ``` |

Modified [NSManagedObjectContext.mergeChanges(fromRemoteContextSave: [AnyHashable : Any], into: [NSManagedObjectContext]) [class]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506546-mergechanges)

|  | Declaration |
| --- | --- |
| From | ``` class func mergeChangesFromRemoteContextSave(_ changeNotificationData: [NSObject : AnyObject], intoContexts contexts: [NSManagedObjectContext]) ``` |
| To | ``` class func mergeChanges(fromRemoteContextSave changeNotificationData: [AnyHashable : Any], into contexts: [NSManagedObjectContext]) ``` |

Modified [NSManagedObjectContext.mergePolicy](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506490-mergepolicy)

|  | Declaration |
| --- | --- |
| From | ``` var mergePolicy: AnyObject ``` |
| To | ``` var mergePolicy: Any ``` |

Modified [NSManagedObjectContext.object(with: NSManagedObjectID) -> NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506197-objectwithid)

|  | Declaration |
| --- | --- |
| From | ``` func objectWithID(_ objectID: NSManagedObjectID) -> NSManagedObject ``` |
| To | ``` func object(with objectID: NSManagedObjectID) -> NSManagedObject ``` |

Modified [NSManagedObjectContext.observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?, context: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506849-observevalue)

|  | Declaration |
| --- | --- |
| From | ``` func observeValueForKeyPath(_ keyPath: String?, ofObject object: AnyObject?, change change: [String : AnyObject]?, context context: UnsafeMutablePointer<Void>) ``` |
| To | ``` func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [String : Any]?, context context: UnsafeMutableRawPointer?) ``` |

Modified [NSManagedObjectContext.obtainPermanentIDs(for: [NSManagedObject]) throws](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506793-obtainpermanentids)

|  | Declaration |
| --- | --- |
| From | ``` func obtainPermanentIDsForObjects(_ objects: [NSManagedObject]) throws ``` |
| To | ``` func obtainPermanentIDs(for objects: [NSManagedObject]) throws ``` |

Modified [NSManagedObjectContext.parent](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506529-parentcontext)

|  | Declaration |
| --- | --- |
| From | ``` var parentContext: NSManagedObjectContext? ``` |
| To | ``` var parent: NSManagedObjectContext? ``` |

Modified [NSManagedObjectContext.perform(_: () -> Swift.Void)](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506578-perform)

|  | Declaration |
| --- | --- |
| From | ``` func performBlock(_ block: () -> Void) ``` |
| To | ``` func perform(_ block: @escaping () -> Swift.Void) ``` |

Modified [NSManagedObjectContext.performAndWait(_: () -> Swift.Void)](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506364-performblockandwait)

|  | Declaration |
| --- | --- |
| From | ``` func performBlockAndWait(_ block: () -> Void) ``` |
| To | ``` func performAndWait(_ block: @escaping () -> Swift.Void) ``` |

Modified [NSManagedObjectContext.refresh(_: NSManagedObject, mergeChanges: Bool)](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506224-refresh)

|  | Declaration |
| --- | --- |
| From | ``` func refreshObject(_ object: NSManagedObject, mergeChanges flag: Bool) ``` |
| To | ``` func refresh(_ object: NSManagedObject, mergeChanges flag: Bool) ``` |

Modified [NSManagedObjectContext.registeredObject(for: NSManagedObjectID) -> NSManagedObject?](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506789-objectregisteredforid)

|  | Declaration |
| --- | --- |
| From | ``` func objectRegisteredForID(_ objectID: NSManagedObjectID) -> NSManagedObject? ``` |
| To | ``` func registeredObject(for objectID: NSManagedObjectID) -> NSManagedObject? ``` |

Modified [NSManagedObjectContext.shouldHandleInaccessibleFault(_: NSManagedObject, for: NSManagedObjectID, triggeredByProperty: NSPropertyDescription?) -> Bool](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506810-shouldhandleinaccessiblefault)

|  | Declaration |
| --- | --- |
| From | ``` func shouldHandleInaccessibleFault(_ fault: NSManagedObject, forObjectID oid: NSManagedObjectID, triggeredByProperty property: NSPropertyDescription?) -> Bool ``` |
| To | ``` func shouldHandleInaccessibleFault(_ fault: NSManagedObject, for oid: NSManagedObjectID, triggeredByProperty property: NSPropertyDescription?) -> Bool ``` |

Modified [NSManagedObjectContext.stalenessInterval](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506875-stalenessinterval)

|  | Declaration |
| --- | --- |
| From | ``` var stalenessInterval: NSTimeInterval ``` |
| To | ``` var stalenessInterval: TimeInterval ``` |

Modified [NSManagedObjectContext.undoManager](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506663-undomanager)

|  | Declaration |
| --- | --- |
| From | ``` var undoManager: NSUndoManager? ``` |
| To | ``` var undoManager: UndoManager? ``` |

Modified [NSManagedObjectContextConcurrencyType [enum]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype)

|  | Declaration |
| --- | --- |
| From | ``` enum NSManagedObjectContextConcurrencyType : UInt {     case ConfinementConcurrencyType     case PrivateQueueConcurrencyType     case MainQueueConcurrencyType } ``` |
| To | ``` enum NSManagedObjectContextConcurrencyType : UInt {     case confinementConcurrencyType     case privateQueueConcurrencyType     case mainQueueConcurrencyType } ``` |

Modified [NSManagedObjectContextConcurrencyType.confinementConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/confinementconcurrencytype)

|  | Declaration |
| --- | --- |
| From | ``` case ConfinementConcurrencyType ``` |
| To | ``` case confinementConcurrencyType ``` |

Modified [NSManagedObjectContextConcurrencyType.mainQueueConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/mainqueueconcurrencytype)

|  | Declaration |
| --- | --- |
| From | ``` case MainQueueConcurrencyType ``` |
| To | ``` case mainQueueConcurrencyType ``` |

Modified [NSManagedObjectContextConcurrencyType.privateQueueConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/nsprivatequeueconcurrencytype)

|  | Declaration |
| --- | --- |
| From | ``` case PrivateQueueConcurrencyType ``` |
| To | ``` case privateQueueConcurrencyType ``` |

Modified [NSManagedObjectID](https://developer.apple.com/documentation/coredata/nsmanagedobjectid)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSManagedObjectID : NSObject, NSCopying {     var entity: NSEntityDescription { get }     weak var persistentStore: NSPersistentStore? { get }     var temporaryID: Bool { get }     func URIRepresentation() -> NSURL } ``` | NSCopying |
| To | ``` class NSManagedObjectID : NSObject, NSCopying {     var entity: NSEntityDescription { get }     weak var persistentStore: NSPersistentStore? { get }     var isTemporaryID: Bool { get }     func uriRepresentation() -> URL     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSManagedObjectID : NSFetchRequestResult { } extension NSManagedObjectID : CVarArg { } extension NSManagedObjectID : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSFetchRequestResult |

Modified [NSManagedObjectID.isTemporaryID](https://developer.apple.com/documentation/coredata/nsmanagedobjectid/1391691-temporaryid)

|  | Declaration |
| --- | --- |
| From | ``` var temporaryID: Bool { get } ``` |
| To | ``` var isTemporaryID: Bool { get } ``` |

Modified [NSManagedObjectID.uriRepresentation() -> URL](https://developer.apple.com/documentation/coredata/nsmanagedobjectid/1391689-urirepresentation)

|  | Declaration |
| --- | --- |
| From | ``` func URIRepresentation() -> NSURL ``` |
| To | ``` func uriRepresentation() -> URL ``` |

Modified [NSManagedObjectModel](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSManagedObjectModel : NSObject, NSCoding, NSCopying, NSFastEnumeration {     class func mergedModelFromBundles(_ bundles: [NSBundle]?) -> NSManagedObjectModel?      init?(byMergingModels models: [NSManagedObjectModel]?)     class func modelByMergingModels(_ models: [NSManagedObjectModel]?) -> NSManagedObjectModel?     init()     convenience init?(contentsOfURL url: NSURL)     var entitiesByName: [String : NSEntityDescription] { get }     var entities: [NSEntityDescription]     var configurations: [String] { get }     func entitiesForConfiguration(_ configuration: String?) -> [NSEntityDescription]?     func setEntities(_ entities: [NSEntityDescription], forConfiguration configuration: String)     func setFetchRequestTemplate(_ fetchRequestTemplate: NSFetchRequest?, forName name: String)     func fetchRequestTemplateForName(_ name: String) -> NSFetchRequest?     func fetchRequestFromTemplateWithName(_ name: String, substitutionVariables variables: [String : AnyObject]) -> NSFetchRequest?     var localizationDictionary: [String : String]?     class func mergedModelFromBundles(_ bundles: [NSBundle]?, forStoreMetadata metadata: [String : AnyObject]) -> NSManagedObjectModel?      init?(byMergingModels models: [NSManagedObjectModel], forStoreMetadata metadata: [String : AnyObject])     class func modelByMergingModels(_ models: [NSManagedObjectModel], forStoreMetadata metadata: [String : AnyObject]) -> NSManagedObjectModel?     var fetchRequestTemplatesByName: [String : NSFetchRequest] { get }     var versionIdentifiers: Set<NSObject>     func isConfiguration(_ configuration: String?, compatibleWithStoreMetadata metadata: [String : AnyObject]) -> Bool     var entityVersionHashesByName: [String : NSData] { get } } ``` | NSCoding, NSCopying, NSFastEnumeration |
| To | ``` class NSManagedObjectModel : NSObject, NSCoding, NSCopying, NSFastEnumeration {     class func mergedModel(from bundles: [Bundle]?) -> NSManagedObjectModel?      init?(byMerging models: [NSManagedObjectModel]?)     class func merging(_ models: [NSManagedObjectModel]?) -> NSManagedObjectModel?     init()     convenience init?(contentsOf url: URL)     var entitiesByName: [String : NSEntityDescription] { get }     var entities: [NSEntityDescription]     var configurations: [String] { get }     func entities(forConfigurationName configuration: String?) -> [NSEntityDescription]?     func setEntities(_ entities: [NSEntityDescription], forConfigurationName configuration: String)     func setFetchRequestTemplate(_ fetchRequestTemplate: NSFetchRequest<NSFetchRequestResult>?, forName name: String)     func fetchRequestTemplate(forName name: String) -> NSFetchRequest<NSFetchRequestResult>?     func fetchRequestFromTemplate(withName name: String, substitutionVariables variables: [String : Any]) -> NSFetchRequest<NSFetchRequestResult>?     var localizationDictionary: [String : String]?     class func mergedModel(from bundles: [Bundle]?, forStoreMetadata metadata: [String : Any]) -> NSManagedObjectModel?      init?(byMerging models: [NSManagedObjectModel], forStoreMetadata metadata: [String : Any])     class func merging(_ models: [NSManagedObjectModel], forStoreMetadata metadata: [String : Any]) -> NSManagedObjectModel?     var fetchRequestTemplatesByName: [String : NSFetchRequest<NSFetchRequestResult>] { get }     var versionIdentifiers: Set<AnyHashable>     func isConfiguration(withName configuration: String?, compatibleWithStoreMetadata metadata: [String : Any]) -> Bool     var entityVersionHashesByName: [String : Data] { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSManagedObjectModel : CVarArg { } extension NSManagedObjectModel : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying, NSFastEnumeration |

Modified [NSManagedObjectModel.entities(forConfigurationName: String?) -> [NSEntityDescription]?](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506693-entities)

|  | Declaration |
| --- | --- |
| From | ``` func entitiesForConfiguration(_ configuration: String?) -> [NSEntityDescription]? ``` |
| To | ``` func entities(forConfigurationName configuration: String?) -> [NSEntityDescription]? ``` |

Modified [NSManagedObjectModel.entityVersionHashesByName](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506992-entityversionhashesbyname)

|  | Declaration |
| --- | --- |
| From | ``` var entityVersionHashesByName: [String : NSData] { get } ``` |
| To | ``` var entityVersionHashesByName: [String : Data] { get } ``` |

Modified [NSManagedObjectModel.fetchRequestFromTemplate(withName: String, substitutionVariables: [String : Any]) -> NSFetchRequest<NSFetchRequestResult>?](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506422-fetchrequestfromtemplate)

|  | Declaration |
| --- | --- |
| From | ``` func fetchRequestFromTemplateWithName(_ name: String, substitutionVariables variables: [String : AnyObject]) -> NSFetchRequest? ``` |
| To | ``` func fetchRequestFromTemplate(withName name: String, substitutionVariables variables: [String : Any]) -> NSFetchRequest<NSFetchRequestResult>? ``` |

Modified [NSManagedObjectModel.fetchRequestTemplate(forName: String) -> NSFetchRequest<NSFetchRequestResult>?](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506369-fetchrequesttemplateforname)

|  | Declaration |
| --- | --- |
| From | ``` func fetchRequestTemplateForName(_ name: String) -> NSFetchRequest? ``` |
| To | ``` func fetchRequestTemplate(forName name: String) -> NSFetchRequest<NSFetchRequestResult>? ``` |

Modified [NSManagedObjectModel.fetchRequestTemplatesByName](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506580-fetchrequesttemplatesbyname)

|  | Declaration |
| --- | --- |
| From | ``` var fetchRequestTemplatesByName: [String : NSFetchRequest] { get } ``` |
| To | ``` var fetchRequestTemplatesByName: [String : NSFetchRequest<NSFetchRequestResult>] { get } ``` |

Modified [NSManagedObjectModel.init(byMerging: [NSManagedObjectModel]?)](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506450-modelbymergingmodels)

|  | Declaration |
| --- | --- |
| From | ``` init?(byMergingModels models: [NSManagedObjectModel]?) ``` |
| To | ``` init?(byMerging models: [NSManagedObjectModel]?) ``` |

Modified [NSManagedObjectModel.init(byMerging: [NSManagedObjectModel], forStoreMetadata: [String : Any])](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506856-modelbymergingmodels)

|  | Declaration |
| --- | --- |
| From | ``` init?(byMergingModels models: [NSManagedObjectModel], forStoreMetadata metadata: [String : AnyObject]) ``` |
| To | ``` init?(byMerging models: [NSManagedObjectModel], forStoreMetadata metadata: [String : Any]) ``` |

Modified [NSManagedObjectModel.init(contentsOf: URL)](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506225-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` convenience init?(contentsOfURL url: NSURL) ``` |
| To | ``` convenience init?(contentsOf url: URL) ``` |

Modified [NSManagedObjectModel.isConfiguration(withName: String?, compatibleWithStoreMetadata: [String : Any]) -> Bool](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506940-isconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` func isConfiguration(_ configuration: String?, compatibleWithStoreMetadata metadata: [String : AnyObject]) -> Bool ``` |
| To | ``` func isConfiguration(withName configuration: String?, compatibleWithStoreMetadata metadata: [String : Any]) -> Bool ``` |

Modified [NSManagedObjectModel.mergedModel(from: [Bundle]?) -> NSManagedObjectModel? [class]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506704-mergedmodelfrombundles)

|  | Declaration |
| --- | --- |
| From | ``` class func mergedModelFromBundles(_ bundles: [NSBundle]?) -> NSManagedObjectModel? ``` |
| To | ``` class func mergedModel(from bundles: [Bundle]?) -> NSManagedObjectModel? ``` |

Modified [NSManagedObjectModel.mergedModel(from: [Bundle]?, forStoreMetadata: [String : Any]) -> NSManagedObjectModel? [class]](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506788-mergedmodelfrombundles)

|  | Declaration |
| --- | --- |
| From | ``` class func mergedModelFromBundles(_ bundles: [NSBundle]?, forStoreMetadata metadata: [String : AnyObject]) -> NSManagedObjectModel? ``` |
| To | ``` class func mergedModel(from bundles: [Bundle]?, forStoreMetadata metadata: [String : Any]) -> NSManagedObjectModel? ``` |

Modified [NSManagedObjectModel.setEntities(_: [NSEntityDescription], forConfigurationName: String)](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506287-setentities)

|  | Declaration |
| --- | --- |
| From | ``` func setEntities(_ entities: [NSEntityDescription], forConfiguration configuration: String) ``` |
| To | ``` func setEntities(_ entities: [NSEntityDescription], forConfigurationName configuration: String) ``` |

Modified [NSManagedObjectModel.setFetchRequestTemplate(_: NSFetchRequest<NSFetchRequestResult>?, forName: String)](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506695-setfetchrequesttemplate)

|  | Declaration |
| --- | --- |
| From | ``` func setFetchRequestTemplate(_ fetchRequestTemplate: NSFetchRequest?, forName name: String) ``` |
| To | ``` func setFetchRequestTemplate(_ fetchRequestTemplate: NSFetchRequest<NSFetchRequestResult>?, forName name: String) ``` |

Modified [NSManagedObjectModel.versionIdentifiers](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506268-versionidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` var versionIdentifiers: Set<NSObject> ``` |
| To | ``` var versionIdentifiers: Set<AnyHashable> ``` |

Modified [NSMappingModel](https://developer.apple.com/documentation/coredata/nsmappingmodel)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSMappingModel : NSObject {      init?(fromBundles bundles: [NSBundle]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel destinationModel: NSManagedObjectModel?)     class func mappingModelFromBundles(_ bundles: [NSBundle]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel destinationModel: NSManagedObjectModel?) -> NSMappingModel?     class func inferredMappingModelForSourceModel(_ sourceModel: NSManagedObjectModel, destinationModel destinationModel: NSManagedObjectModel) throws -> NSMappingModel     init?(contentsOfURL url: NSURL?)     var entityMappings: [NSEntityMapping]!     var entityMappingsByName: [String : NSEntityMapping] { get } } ``` | -- |
| To | ``` class NSMappingModel : NSObject {      init?(from bundles: [Bundle]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel destinationModel: NSManagedObjectModel?)     class func fromBundles(_ bundles: [Bundle]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel destinationModel: NSManagedObjectModel?) -> NSMappingModel?     class func inferredMappingModel(forSourceModel sourceModel: NSManagedObjectModel, destinationModel destinationModel: NSManagedObjectModel) throws -> NSMappingModel     init?(contentsOf url: URL?)     var entityMappings: [NSEntityMapping]!     var entityMappingsByName: [String : NSEntityMapping] { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSMappingModel : CVarArg { } extension NSMappingModel : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NSMappingModel.inferredMappingModel(forSourceModel: NSManagedObjectModel, destinationModel: NSManagedObjectModel) throws -> NSMappingModel [class]](https://developer.apple.com/documentation/coredata/nsmappingmodel/1506468-inferredmappingmodelforsourcemod)

|  | Declaration |
| --- | --- |
| From | ``` class func inferredMappingModelForSourceModel(_ sourceModel: NSManagedObjectModel, destinationModel destinationModel: NSManagedObjectModel) throws -> NSMappingModel ``` |
| To | ``` class func inferredMappingModel(forSourceModel sourceModel: NSManagedObjectModel, destinationModel destinationModel: NSManagedObjectModel) throws -> NSMappingModel ``` |

Modified [NSMappingModel.init(contentsOf: URL?)](https://developer.apple.com/documentation/coredata/nsmappingmodel/1506304-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(contentsOfURL url: NSURL?) ``` |
| To | ``` init?(contentsOf url: URL?) ``` |

Modified [NSMappingModel.init(from: [Bundle]?, forSourceModel: NSManagedObjectModel?, destinationModel: NSManagedObjectModel?)](https://developer.apple.com/documentation/coredata/nsmappingmodel/1506930-mappingmodelfrombundles)

|  | Declaration |
| --- | --- |
| From | ``` init?(fromBundles bundles: [NSBundle]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel destinationModel: NSManagedObjectModel?) ``` |
| To | ``` init?(from bundles: [Bundle]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel destinationModel: NSManagedObjectModel?) ``` |

Modified [NSMergeConflict](https://developer.apple.com/documentation/coredata/nsmergeconflict)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSMergeConflict : NSObject {     var sourceObject: NSManagedObject { get }     var objectSnapshot: [String : AnyObject]? { get }     var cachedSnapshot: [String : AnyObject]? { get }     var persistedSnapshot: [String : AnyObject]? { get }     var newVersionNumber: Int { get }     var oldVersionNumber: Int { get }     init(source srcObject: NSManagedObject, newVersion newvers: Int, oldVersion oldvers: Int, cachedSnapshot cachesnap: [String : AnyObject]?, persistedSnapshot persnap: [String : AnyObject]?)     convenience init() } ``` | -- |
| To | ``` class NSMergeConflict : NSObject {     var sourceObject: NSManagedObject { get }     var objectSnapshot: [String : Any]? { get }     var cachedSnapshot: [String : Any]? { get }     var persistedSnapshot: [String : Any]? { get }     var newVersionNumber: Int { get }     var oldVersionNumber: Int { get }     init(source srcObject: NSManagedObject, newVersion newvers: Int, oldVersion oldvers: Int, cachedSnapshot cachesnap: [String : Any]?, persistedSnapshot persnap: [String : Any]?)     convenience init()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSMergeConflict : CVarArg { } extension NSMergeConflict : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NSMergeConflict.cachedSnapshot](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506685-cachedsnapshot)

|  | Declaration |
| --- | --- |
| From | ``` var cachedSnapshot: [String : AnyObject]? { get } ``` |
| To | ``` var cachedSnapshot: [String : Any]? { get } ``` |

Modified [NSMergeConflict.init(source: NSManagedObject, newVersion: Int, oldVersion: Int, cachedSnapshot: [String : Any]?, persistedSnapshot: [String : Any]?)](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506216-init)

|  | Declaration |
| --- | --- |
| From | ``` init(source srcObject: NSManagedObject, newVersion newvers: Int, oldVersion oldvers: Int, cachedSnapshot cachesnap: [String : AnyObject]?, persistedSnapshot persnap: [String : AnyObject]?) ``` |
| To | ``` init(source srcObject: NSManagedObject, newVersion newvers: Int, oldVersion oldvers: Int, cachedSnapshot cachesnap: [String : Any]?, persistedSnapshot persnap: [String : Any]?) ``` |

Modified [NSMergeConflict.objectSnapshot](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506454-objectsnapshot)

|  | Declaration |
| --- | --- |
| From | ``` var objectSnapshot: [String : AnyObject]? { get } ``` |
| To | ``` var objectSnapshot: [String : Any]? { get } ``` |

Modified [NSMergeConflict.persistedSnapshot](https://developer.apple.com/documentation/coredata/nsmergeconflict/1506412-persistedsnapshot)

|  | Declaration |
| --- | --- |
| From | ``` var persistedSnapshot: [String : AnyObject]? { get } ``` |
| To | ``` var persistedSnapshot: [String : Any]? { get } ``` |

Modified [NSMergePolicy](https://developer.apple.com/documentation/coredata/nsmergepolicy)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSMergePolicy : NSObject {     var mergeType: NSMergePolicyType { get }     init(mergeType ty: NSMergePolicyType)     convenience init()     func resolveConflicts(_ list: [AnyObject]) throws     func resolveOptimisticLockingVersionConflicts(_ list: [NSMergeConflict]) throws     func resolveConstraintConflicts(_ list: [NSConstraintConflict]) throws } ``` | -- |
| To | ``` class NSMergePolicy : NSObject {     class var error: NSMergePolicy { get }     class var rollback: NSMergePolicy { get }     class var overwrite: NSMergePolicy { get }     class var mergeByPropertyObjectTrump: NSMergePolicy { get }     class var mergeByPropertyStoreTrump: NSMergePolicy { get }     var mergeType: NSMergePolicyType { get }     init(merge ty: NSMergePolicyType)     convenience init()     func resolve(mergeConflicts list: [Any]) throws     func resolve(optimisticLockingConflicts list: [NSMergeConflict]) throws     func resolve(constraintConflicts list: [NSConstraintConflict]) throws     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSMergePolicy : CVarArg { } extension NSMergePolicy : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NSMergePolicy.init(merge: NSMergePolicyType)](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506763-init)

|  | Declaration |
| --- | --- |
| From | ``` init(mergeType ty: NSMergePolicyType) ``` |
| To | ``` init(merge ty: NSMergePolicyType) ``` |

Modified [NSMergePolicy.resolve(constraintConflicts: [NSConstraintConflict]) throws](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506678-resolve)

|  | Declaration |
| --- | --- |
| From | ``` func resolveConstraintConflicts(_ list: [NSConstraintConflict]) throws ``` |
| To | ``` func resolve(constraintConflicts list: [NSConstraintConflict]) throws ``` |

Modified [NSMergePolicy.resolve(mergeConflicts: [Any]) throws](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506253-resolve)

|  | Declaration |
| --- | --- |
| From | ``` func resolveConflicts(_ list: [AnyObject]) throws ``` |
| To | ``` func resolve(mergeConflicts list: [Any]) throws ``` |

Modified [NSMergePolicy.resolve(optimisticLockingConflicts: [NSMergeConflict]) throws](https://developer.apple.com/documentation/coredata/nsmergepolicy/1506787-resolve)

|  | Declaration |
| --- | --- |
| From | ``` func resolveOptimisticLockingVersionConflicts(_ list: [NSMergeConflict]) throws ``` |
| To | ``` func resolve(optimisticLockingConflicts list: [NSMergeConflict]) throws ``` |

Modified [NSMergePolicyType [enum]](https://developer.apple.com/documentation/coredata/nsmergepolicytype)

|  | Declaration |
| --- | --- |
| From | ``` enum NSMergePolicyType : UInt {     case ErrorMergePolicyType     case MergeByPropertyStoreTrumpMergePolicyType     case MergeByPropertyObjectTrumpMergePolicyType     case OverwriteMergePolicyType     case RollbackMergePolicyType } ``` |
| To | ``` enum NSMergePolicyType : UInt {     case errorMergePolicyType     case mergeByPropertyStoreTrumpMergePolicyType     case mergeByPropertyObjectTrumpMergePolicyType     case overwriteMergePolicyType     case rollbackMergePolicyType } ``` |

Modified [NSMergePolicyType.errorMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype/nserrormergepolicytype)

|  | Declaration |
| --- | --- |
| From | ``` case ErrorMergePolicyType ``` |
| To | ``` case errorMergePolicyType ``` |

Modified [NSMergePolicyType.mergeByPropertyObjectTrumpMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype/nsmergebypropertyobjecttrumpmergepolicytype)

|  | Declaration |
| --- | --- |
| From | ``` case MergeByPropertyObjectTrumpMergePolicyType ``` |
| To | ``` case mergeByPropertyObjectTrumpMergePolicyType ``` |

Modified [NSMergePolicyType.mergeByPropertyStoreTrumpMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype/mergebypropertystoretrumpmergepolicytype)

|  | Declaration |
| --- | --- |
| From | ``` case MergeByPropertyStoreTrumpMergePolicyType ``` |
| To | ``` case mergeByPropertyStoreTrumpMergePolicyType ``` |

Modified [NSMergePolicyType.overwriteMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype/overwritemergepolicytype)

|  | Declaration |
| --- | --- |
| From | ``` case OverwriteMergePolicyType ``` |
| To | ``` case overwriteMergePolicyType ``` |

Modified [NSMergePolicyType.rollbackMergePolicyType](https://developer.apple.com/documentation/coredata/nsmergepolicytype/nsrollbackmergepolicytype)

|  | Declaration |
| --- | --- |
| From | ``` case RollbackMergePolicyType ``` |
| To | ``` case rollbackMergePolicyType ``` |

Modified [NSMigrationManager](https://developer.apple.com/documentation/coredata/nsmigrationmanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSMigrationManager : NSObject {     init(sourceModel sourceModel: NSManagedObjectModel, destinationModel destinationModel: NSManagedObjectModel)     func migrateStoreFromURL(_ sourceURL: NSURL, type sStoreType: String, options sOptions: [NSObject : AnyObject]?, withMappingModel mappings: NSMappingModel?, toDestinationURL dURL: NSURL, destinationType dStoreType: String, destinationOptions dOptions: [NSObject : AnyObject]?) throws     var usesStoreSpecificMigrationManager: Bool     func reset()     var mappingModel: NSMappingModel { get }     var sourceModel: NSManagedObjectModel { get }     var destinationModel: NSManagedObjectModel { get }     var sourceContext: NSManagedObjectContext { get }     var destinationContext: NSManagedObjectContext { get }     func sourceEntityForEntityMapping(_ mEntity: NSEntityMapping) -> NSEntityDescription?     func destinationEntityForEntityMapping(_ mEntity: NSEntityMapping) -> NSEntityDescription?     func associateSourceInstance(_ sourceInstance: NSManagedObject, withDestinationInstance destinationInstance: NSManagedObject, forEntityMapping entityMapping: NSEntityMapping)     func destinationInstancesForEntityMappingNamed(_ mappingName: String, sourceInstances sourceInstances: [NSManagedObject]?) -> [NSManagedObject]     func sourceInstancesForEntityMappingNamed(_ mappingName: String, destinationInstances destinationInstances: [NSManagedObject]?) -> [NSManagedObject]     var currentEntityMapping: NSEntityMapping { get }     var migrationProgress: Float { get }     var userInfo: [NSObject : AnyObject]?     func cancelMigrationWithError(_ error: NSError) } ``` | -- |
| To | ``` class NSMigrationManager : NSObject {     init(sourceModel sourceModel: NSManagedObjectModel, destinationModel destinationModel: NSManagedObjectModel)     func migrateStore(from sourceURL: URL, sourceType sStoreType: String, options sOptions: [AnyHashable : Any]? = nil, with mappings: NSMappingModel?, toDestinationURL dURL: URL, destinationType dStoreType: String, destinationOptions dOptions: [AnyHashable : Any]? = nil) throws     var usesStoreSpecificMigrationManager: Bool     func reset()     var mappingModel: NSMappingModel { get }     var sourceModel: NSManagedObjectModel { get }     var destinationModel: NSManagedObjectModel { get }     var sourceContext: NSManagedObjectContext { get }     var destinationContext: NSManagedObjectContext { get }     func sourceEntity(for mEntity: NSEntityMapping) -> NSEntityDescription?     func destinationEntity(for mEntity: NSEntityMapping) -> NSEntityDescription?     func associate(sourceInstance sourceInstance: NSManagedObject, withDestinationInstance destinationInstance: NSManagedObject, for entityMapping: NSEntityMapping)     func destinationInstances(forEntityMappingName mappingName: String, sourceInstances sourceInstances: [NSManagedObject]?) -> [NSManagedObject]     func sourceInstances(forEntityMappingName mappingName: String, destinationInstances destinationInstances: [NSManagedObject]?) -> [NSManagedObject]     var currentEntityMapping: NSEntityMapping { get }     var migrationProgress: Float { get }     var userInfo: [AnyHashable : Any]?     func cancelMigrationWithError(_ error: Error)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSMigrationManager : CVarArg { } extension NSMigrationManager : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NSMigrationManager.associate(sourceInstance: NSManagedObject, withDestinationInstance: NSManagedObject, for: NSEntityMapping)](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417604-associatesourceinstance)

|  | Declaration |
| --- | --- |
| From | ``` func associateSourceInstance(_ sourceInstance: NSManagedObject, withDestinationInstance destinationInstance: NSManagedObject, forEntityMapping entityMapping: NSEntityMapping) ``` |
| To | ``` func associate(sourceInstance sourceInstance: NSManagedObject, withDestinationInstance destinationInstance: NSManagedObject, for entityMapping: NSEntityMapping) ``` |

Modified [NSMigrationManager.cancelMigrationWithError(_: Error)](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417608-cancelmigrationwitherror)

|  | Declaration |
| --- | --- |
| From | ``` func cancelMigrationWithError(_ error: NSError) ``` |
| To | ``` func cancelMigrationWithError(_ error: Error) ``` |

Modified [NSMigrationManager.destinationEntity(for: NSEntityMapping) -> NSEntityDescription?](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417598-destinationentityforentitymappin)

|  | Declaration |
| --- | --- |
| From | ``` func destinationEntityForEntityMapping(_ mEntity: NSEntityMapping) -> NSEntityDescription? ``` |
| To | ``` func destinationEntity(for mEntity: NSEntityMapping) -> NSEntityDescription? ``` |

Modified [NSMigrationManager.destinationInstances(forEntityMappingName: String, sourceInstances: [NSManagedObject]?) -> [NSManagedObject]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417594-destinationinstances)

|  | Declaration |
| --- | --- |
| From | ``` func destinationInstancesForEntityMappingNamed(_ mappingName: String, sourceInstances sourceInstances: [NSManagedObject]?) -> [NSManagedObject] ``` |
| To | ``` func destinationInstances(forEntityMappingName mappingName: String, sourceInstances sourceInstances: [NSManagedObject]?) -> [NSManagedObject] ``` |

Modified [NSMigrationManager.migrateStore(from: URL, sourceType: String, options: [AnyHashable : Any]?, with: NSMappingModel?, toDestinationURL: URL, destinationType: String, destinationOptions: [AnyHashable : Any]?) throws](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417584-migratestore)

|  | Declaration |
| --- | --- |
| From | ``` func migrateStoreFromURL(_ sourceURL: NSURL, type sStoreType: String, options sOptions: [NSObject : AnyObject]?, withMappingModel mappings: NSMappingModel?, toDestinationURL dURL: NSURL, destinationType dStoreType: String, destinationOptions dOptions: [NSObject : AnyObject]?) throws ``` |
| To | ``` func migrateStore(from sourceURL: URL, sourceType sStoreType: String, options sOptions: [AnyHashable : Any]? = nil, with mappings: NSMappingModel?, toDestinationURL dURL: URL, destinationType dStoreType: String, destinationOptions dOptions: [AnyHashable : Any]? = nil) throws ``` |

Modified [NSMigrationManager.sourceEntity(for: NSEntityMapping) -> NSEntityDescription?](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417596-sourceentityforentitymapping)

|  | Declaration |
| --- | --- |
| From | ``` func sourceEntityForEntityMapping(_ mEntity: NSEntityMapping) -> NSEntityDescription? ``` |
| To | ``` func sourceEntity(for mEntity: NSEntityMapping) -> NSEntityDescription? ``` |

Modified [NSMigrationManager.sourceInstances(forEntityMappingName: String, destinationInstances: [NSManagedObject]?) -> [NSManagedObject]](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417580-sourceinstances)

|  | Declaration |
| --- | --- |
| From | ``` func sourceInstancesForEntityMappingNamed(_ mappingName: String, destinationInstances destinationInstances: [NSManagedObject]?) -> [NSManagedObject] ``` |
| To | ``` func sourceInstances(forEntityMappingName mappingName: String, destinationInstances destinationInstances: [NSManagedObject]?) -> [NSManagedObject] ``` |

Modified [NSMigrationManager.userInfo](https://developer.apple.com/documentation/coredata/nsmigrationmanager/1417588-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]? ``` |
| To | ``` var userInfo: [AnyHashable : Any]? ``` |

Modified [NSNotification.Name.NSManagedObjectContextDidSave](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextdidsavenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | NSManagedObjectContextDidSaveNotification | ``` let NSManagedObjectContextDidSaveNotification: String ``` |
| To | NSManagedObjectContextDidSave | ``` static let NSManagedObjectContextDidSave: NSNotification.Name ``` |

Modified [NSNotification.Name.NSManagedObjectContextObjectsDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1506884-nsmanagedobjectcontextobjectsdid)

|  | Name | Declaration |
| --- | --- | --- |
| From | NSManagedObjectContextObjectsDidChangeNotification | ``` let NSManagedObjectContextObjectsDidChangeNotification: String ``` |
| To | NSManagedObjectContextObjectsDidChange | ``` static let NSManagedObjectContextObjectsDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.NSManagedObjectContextWillSave](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextwillsavenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | NSManagedObjectContextWillSaveNotification | ``` let NSManagedObjectContextWillSaveNotification: String ``` |
| To | NSManagedObjectContextWillSave | ``` static let NSManagedObjectContextWillSave: NSNotification.Name ``` |

Modified [NSNotification.Name.NSPersistentStoreCoordinatorStoresDidChange](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinatorstoresdidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | NSPersistentStoreCoordinatorStoresDidChangeNotification | ``` let NSPersistentStoreCoordinatorStoresDidChangeNotification: String ``` |
| To | NSPersistentStoreCoordinatorStoresDidChange | ``` static let NSPersistentStoreCoordinatorStoresDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.NSPersistentStoreCoordinatorStoresWillChange](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinatorstoreswillchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | NSPersistentStoreCoordinatorStoresWillChangeNotification | ``` let NSPersistentStoreCoordinatorStoresWillChangeNotification: String ``` |
| To | NSPersistentStoreCoordinatorStoresWillChange | ``` static let NSPersistentStoreCoordinatorStoresWillChange: NSNotification.Name ``` |

Modified [NSNotification.Name.NSPersistentStoreCoordinatorWillRemoveStore](https://developer.apple.com/documentation/foundation/nsnotification/name/1468876-nspersistentstorecoordinatorwill)

|  | Name | Declaration |
| --- | --- | --- |
| From | NSPersistentStoreCoordinatorWillRemoveStoreNotification | ``` let NSPersistentStoreCoordinatorWillRemoveStoreNotification: String ``` |
| To | NSPersistentStoreCoordinatorWillRemoveStore | ``` static let NSPersistentStoreCoordinatorWillRemoveStore: NSNotification.Name ``` |

Modified [NSNotification.Name.NSPersistentStoreDidImportUbiquitousContentChanges](https://developer.apple.com/documentation/coredata/nspersistentstoredidimportubiquitouscontentchangesnotification)

|  | Name | Declaration | Deprecation |
| --- | --- | --- | --- |
| From | NSPersistentStoreDidImportUbiquitousContentChangesNotification | ``` let NSPersistentStoreDidImportUbiquitousContentChangesNotification: String ``` | -- |
| To | NSPersistentStoreDidImportUbiquitousContentChanges | ``` static let NSPersistentStoreDidImportUbiquitousContentChanges: NSNotification.Name ``` | iOS 10.0 |

Modified [NSPersistentStore](https://developer.apple.com/documentation/coredata/nspersistentstore)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSPersistentStore : NSObject {     class func metadataForPersistentStoreWithURL(_ url: NSURL) throws -> [String : AnyObject]     class func setMetadata(_ metadata: [String : AnyObject]?, forPersistentStoreWithURL url: NSURL) throws     class func migrationManagerClass() -> AnyClass     init(persistentStoreCoordinator root: NSPersistentStoreCoordinator?, configurationName name: String?, URL url: NSURL, options options: [NSObject : AnyObject]?)     convenience init()     func loadMetadata() throws     weak var persistentStoreCoordinator: NSPersistentStoreCoordinator? { get }     var configurationName: String { get }     var options: [NSObject : AnyObject]? { get }     var URL: NSURL?     var identifier: String!     var type: String { get }     var readOnly: Bool     var metadata: [String : AnyObject]!     func didAddToPersistentStoreCoordinator(_ coordinator: NSPersistentStoreCoordinator)     func willRemoveFromPersistentStoreCoordinator(_ coordinator: NSPersistentStoreCoordinator?) } ``` | -- |
| To | ``` class NSPersistentStore : NSObject {     class func metadataForPersistentStore(with url: URL) throws -> [String : Any]     class func setMetadata(_ metadata: [String : Any]?, forPersistentStoreAt url: URL) throws     class func migrationManagerClass() -> Swift.AnyClass     init(persistentStoreCoordinator root: NSPersistentStoreCoordinator?, configurationName name: String?, at url: URL, options options: [AnyHashable : Any]? = nil)     convenience init()     func loadMetadata() throws     weak var persistentStoreCoordinator: NSPersistentStoreCoordinator? { get }     var configurationName: String { get }     var options: [AnyHashable : Any]? { get }     var url: URL?     var identifier: String!     var type: String { get }     var isReadOnly: Bool     var metadata: [String : Any]!     func didAdd(to coordinator: NSPersistentStoreCoordinator)     func willRemove(from coordinator: NSPersistentStoreCoordinator?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSPersistentStore : CVarArg { } extension NSPersistentStore : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NSPersistentStore.didAdd(to: NSPersistentStoreCoordinator)](https://developer.apple.com/documentation/coredata/nspersistentstore/1506873-didadd)

|  | Declaration |
| --- | --- |
| From | ``` func didAddToPersistentStoreCoordinator(_ coordinator: NSPersistentStoreCoordinator) ``` |
| To | ``` func didAdd(to coordinator: NSPersistentStoreCoordinator) ``` |

Modified [NSPersistentStore.init(persistentStoreCoordinator: NSPersistentStoreCoordinator?, configurationName: String?, at: URL, options: [AnyHashable : Any]?)](https://developer.apple.com/documentation/coredata/nspersistentstore/1506232-initwithpersistentstorecoordinat)

|  | Declaration |
| --- | --- |
| From | ``` init(persistentStoreCoordinator root: NSPersistentStoreCoordinator?, configurationName name: String?, URL url: NSURL, options options: [NSObject : AnyObject]?) ``` |
| To | ``` init(persistentStoreCoordinator root: NSPersistentStoreCoordinator?, configurationName name: String?, at url: URL, options options: [AnyHashable : Any]? = nil) ``` |

Modified [NSPersistentStore.isReadOnly](https://developer.apple.com/documentation/coredata/nspersistentstore/1506183-readonly)

|  | Declaration |
| --- | --- |
| From | ``` var readOnly: Bool ``` |
| To | ``` var isReadOnly: Bool ``` |

Modified [NSPersistentStore.metadata](https://developer.apple.com/documentation/coredata/nspersistentstore/1506564-metadata)

|  | Declaration |
| --- | --- |
| From | ``` var metadata: [String : AnyObject]! ``` |
| To | ``` var metadata: [String : Any]! ``` |

Modified [NSPersistentStore.metadataForPersistentStore(with: URL) throws -> [String : Any] [class]](https://developer.apple.com/documentation/coredata/nspersistentstore/1506741-metadataforpersistentstorewithur)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataForPersistentStoreWithURL(_ url: NSURL) throws -> [String : AnyObject] ``` |
| To | ``` class func metadataForPersistentStore(with url: URL) throws -> [String : Any] ``` |

Modified [NSPersistentStore.migrationManagerClass() -> Swift.AnyClass [class]](https://developer.apple.com/documentation/coredata/nspersistentstore/1506361-migrationmanagerclass)

|  | Declaration |
| --- | --- |
| From | ``` class func migrationManagerClass() -> AnyClass ``` |
| To | ``` class func migrationManagerClass() -> Swift.AnyClass ``` |

Modified [NSPersistentStore.options](https://developer.apple.com/documentation/coredata/nspersistentstore/1506821-options)

|  | Declaration |
| --- | --- |
| From | ``` var options: [NSObject : AnyObject]? { get } ``` |
| To | ``` var options: [AnyHashable : Any]? { get } ``` |

Modified [NSPersistentStore.setMetadata(_: [String : Any]?, forPersistentStoreAt: URL) throws [class]](https://developer.apple.com/documentation/coredata/nspersistentstore/1506824-setmetadata)

|  | Declaration |
| --- | --- |
| From | ``` class func setMetadata(_ metadata: [String : AnyObject]?, forPersistentStoreWithURL url: NSURL) throws ``` |
| To | ``` class func setMetadata(_ metadata: [String : Any]?, forPersistentStoreAt url: URL) throws ``` |

Modified [NSPersistentStore.url](https://developer.apple.com/documentation/coredata/nspersistentstore/1506700-url)

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL? ``` |
| To | ``` var url: URL? ``` |

Modified [NSPersistentStore.willRemove(from: NSPersistentStoreCoordinator?)](https://developer.apple.com/documentation/coredata/nspersistentstore/1506731-willremove)

|  | Declaration |
| --- | --- |
| From | ``` func willRemoveFromPersistentStoreCoordinator(_ coordinator: NSPersistentStoreCoordinator?) ``` |
| To | ``` func willRemove(from coordinator: NSPersistentStoreCoordinator?) ``` |

Modified [NSPersistentStoreAsynchronousResult](https://developer.apple.com/documentation/coredata/nspersistentstoreasynchronousresult)

|  | Declaration |
| --- | --- |
| From | ``` class NSPersistentStoreAsynchronousResult : NSPersistentStoreResult {     var managedObjectContext: NSManagedObjectContext { get }     var operationError: NSError? { get }     var progress: NSProgress? { get }     func cancel() } ``` |
| To | ``` class NSPersistentStoreAsynchronousResult : NSPersistentStoreResult {     var managedObjectContext: NSManagedObjectContext { get }     var operationError: Error? { get }     var progress: Progress? { get }     func cancel() } ``` |

Modified [NSPersistentStoreAsynchronousResult.operationError](https://developer.apple.com/documentation/coredata/nspersistentstoreasynchronousresult/1404904-operationerror)

|  | Declaration |
| --- | --- |
| From | ``` var operationError: NSError? { get } ``` |
| To | ``` var operationError: Error? { get } ``` |

Modified [NSPersistentStoreAsynchronousResult.progress](https://developer.apple.com/documentation/coredata/nspersistentstoreasynchronousresult/1404920-progress)

|  | Declaration |
| --- | --- |
| From | ``` var progress: NSProgress? { get } ``` |
| To | ``` var progress: Progress? { get } ``` |

Modified [NSPersistentStoreCoordinator](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSPersistentStoreCoordinator : NSObject, NSLocking {     init(managedObjectModel model: NSManagedObjectModel)     var managedObjectModel: NSManagedObjectModel { get }     var persistentStores: [NSPersistentStore] { get }     var name: String?     func persistentStoreForURL(_ URL: NSURL) -> NSPersistentStore?     func URLForPersistentStore(_ store: NSPersistentStore) -> NSURL     func setURL(_ url: NSURL, forPersistentStore store: NSPersistentStore) -> Bool     func addPersistentStoreWithType(_ storeType: String, configuration configuration: String?, URL storeURL: NSURL?, options options: [NSObject : AnyObject]?) throws -> NSPersistentStore     func removePersistentStore(_ store: NSPersistentStore) throws     func setMetadata(_ metadata: [String : AnyObject]?, forPersistentStore store: NSPersistentStore)     func metadataForPersistentStore(_ store: NSPersistentStore) -> [String : AnyObject]     func managedObjectIDForURIRepresentation(_ url: NSURL) -> NSManagedObjectID?     func executeRequest(_ request: NSPersistentStoreRequest, withContext context: NSManagedObjectContext) throws -> AnyObject     class func registeredStoreTypes() -> [String : NSValue]     class func registerStoreClass(_ storeClass: AnyClass, forStoreType storeType: String)     class func metadataForPersistentStoreOfType(_ storeType: String, URL url: NSURL, options options: [NSObject : AnyObject]?) throws -> [String : AnyObject]     class func setMetadata(_ metadata: [String : AnyObject]?, forPersistentStoreOfType storeType: String, URL url: NSURL, options options: [NSObject : AnyObject]?) throws     class func metadataForPersistentStoreOfType(_ storeType: String?, URL url: NSURL) throws -> [String : AnyObject]     class func setMetadata(_ metadata: [String : AnyObject]?, forPersistentStoreOfType storeType: String?, URL url: NSURL) throws     class func removeUbiquitousContentAndPersistentStoreAtURL(_ storeURL: NSURL, options options: [NSObject : AnyObject]?) throws     func migratePersistentStore(_ store: NSPersistentStore, toURL URL: NSURL, options options: [NSObject : AnyObject]?, withType storeType: String) throws -> NSPersistentStore     func destroyPersistentStoreAtURL(_ url: NSURL, withType storeType: String, options options: [NSObject : AnyObject]?) throws     func replacePersistentStoreAtURL(_ destinationURL: NSURL, destinationOptions destinationOptions: [NSObject : AnyObject]?, withPersistentStoreFromURL sourceURL: NSURL, sourceOptions sourceOptions: [NSObject : AnyObject]?, storeType storeType: String) throws     func performBlock(_ block: () -> Void)     func performBlockAndWait(_ block: () -> Void)     func lock()     func unlock()     func tryLock() -> Bool } ``` | NSLocking |
| To | ``` class NSPersistentStoreCoordinator : NSObject, NSLocking {     init(managedObjectModel model: NSManagedObjectModel)     var managedObjectModel: NSManagedObjectModel { get }     var persistentStores: [NSPersistentStore] { get }     var name: String?     func persistentStore(for URL: URL) -> NSPersistentStore?     func url(for store: NSPersistentStore) -> URL     func setURL(_ url: URL, for store: NSPersistentStore) -> Bool     func addPersistentStore(ofType storeType: String, configurationName configuration: String?, at storeURL: URL?, options options: [AnyHashable : Any]? = nil) throws -> NSPersistentStore     func addPersistentStore(with storeDescription: NSPersistentStoreDescription, completionHandler block: @escaping (NSPersistentStoreDescription, Error?) -> Swift.Void)     func remove(_ store: NSPersistentStore) throws     func setMetadata(_ metadata: [String : Any]?, for store: NSPersistentStore)     func metadata(for store: NSPersistentStore) -> [String : Any]     func managedObjectID(forURIRepresentation url: URL) -> NSManagedObjectID?     func execute(_ request: NSPersistentStoreRequest, with context: NSManagedObjectContext) throws -> Any     class var registeredStoreTypes: [String : NSValue] { get }     class func registerStoreClass(_ storeClass: Swift.AnyClass, forStoreType storeType: String)     class func metadataForPersistentStore(ofType storeType: String, at url: URL, options options: [AnyHashable : Any]? = nil) throws -> [String : Any]     class func setMetadata(_ metadata: [String : Any]?, forPersistentStoreOfType storeType: String, at url: URL, options options: [AnyHashable : Any]? = nil) throws     func migratePersistentStore(_ store: NSPersistentStore, to URL: URL, options options: [AnyHashable : Any]? = nil, withType storeType: String) throws -> NSPersistentStore     func destroyPersistentStore(at url: URL, ofType storeType: String, options options: [AnyHashable : Any]? = nil) throws     func replacePersistentStore(at destinationURL: URL, destinationOptions destinationOptions: [AnyHashable : Any]? = nil, withPersistentStoreFrom sourceURL: URL, sourceOptions sourceOptions: [AnyHashable : Any]? = nil, ofType storeType: String) throws     func perform(_ block: @escaping () -> Swift.Void)     func performAndWait(_ block: @escaping () -> Swift.Void)     func lock()     func unlock()     func tryLock() -> Bool     class func metadataForPersistentStore(ofType storeType: String?, at url: URL) throws -> [String : Any]     class func setMetadata(_ metadata: [String : Any]?, forPersistentStoreOfType storeType: String?, at url: URL) throws     class func removeUbiquitousContentAndPersistentStore(at storeURL: URL, options options: [AnyHashable : Any]? = nil) throws     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSPersistentStoreCoordinator : CVarArg { } extension NSPersistentStoreCoordinator : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSLocking |

Modified [NSPersistentStoreCoordinator.addPersistentStore(ofType: String, configurationName: String?, at: URL?, options: [AnyHashable : Any]?) throws -> NSPersistentStore](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468860-addpersistentstore)

|  | Declaration |
| --- | --- |
| From | ``` func addPersistentStoreWithType(_ storeType: String, configuration configuration: String?, URL storeURL: NSURL?, options options: [NSObject : AnyObject]?) throws -> NSPersistentStore ``` |
| To | ``` func addPersistentStore(ofType storeType: String, configurationName configuration: String?, at storeURL: URL?, options options: [AnyHashable : Any]? = nil) throws -> NSPersistentStore ``` |

Modified [NSPersistentStoreCoordinator.destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable : Any]?) throws](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468888-destroypersistentstoreaturl)

|  | Declaration |
| --- | --- |
| From | ``` func destroyPersistentStoreAtURL(_ url: NSURL, withType storeType: String, options options: [NSObject : AnyObject]?) throws ``` |
| To | ``` func destroyPersistentStore(at url: URL, ofType storeType: String, options options: [AnyHashable : Any]? = nil) throws ``` |

Modified [NSPersistentStoreCoordinator.execute(_: NSPersistentStoreRequest, with: NSManagedObjectContext) throws -> Any](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468872-execute)

|  | Declaration |
| --- | --- |
| From | ``` func executeRequest(_ request: NSPersistentStoreRequest, withContext context: NSManagedObjectContext) throws -> AnyObject ``` |
| To | ``` func execute(_ request: NSPersistentStoreRequest, with context: NSManagedObjectContext) throws -> Any ``` |

Modified [NSPersistentStoreCoordinator.managedObjectID(forURIRepresentation: URL) -> NSManagedObjectID?](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468882-managedobjectidforurirepresentat)

|  | Declaration |
| --- | --- |
| From | ``` func managedObjectIDForURIRepresentation(_ url: NSURL) -> NSManagedObjectID? ``` |
| To | ``` func managedObjectID(forURIRepresentation url: URL) -> NSManagedObjectID? ``` |

Modified [NSPersistentStoreCoordinator.metadata(for: NSPersistentStore) -> [String : Any]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468911-metadata)

|  | Declaration |
| --- | --- |
| From | ``` func metadataForPersistentStore(_ store: NSPersistentStore) -> [String : AnyObject] ``` |
| To | ``` func metadata(for store: NSPersistentStore) -> [String : Any] ``` |

Modified [NSPersistentStoreCoordinator.metadataForPersistentStore(ofType: String?, at: URL) throws -> [String : Any] [class]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468804-metadataforpersistentstoreoftype)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataForPersistentStoreOfType(_ storeType: String?, URL url: NSURL) throws -> [String : AnyObject] ``` |
| To | ``` class func metadataForPersistentStore(ofType storeType: String?, at url: URL) throws -> [String : Any] ``` |

Modified [NSPersistentStoreCoordinator.metadataForPersistentStore(ofType: String, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any] [class]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468778-metadataforpersistentstoreoftype)

|  | Declaration |
| --- | --- |
| From | ``` class func metadataForPersistentStoreOfType(_ storeType: String, URL url: NSURL, options options: [NSObject : AnyObject]?) throws -> [String : AnyObject] ``` |
| To | ``` class func metadataForPersistentStore(ofType storeType: String, at url: URL, options options: [AnyHashable : Any]? = nil) throws -> [String : Any] ``` |

Modified [NSPersistentStoreCoordinator.migratePersistentStore(_: NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468927-migratepersistentstore)

|  | Declaration |
| --- | --- |
| From | ``` func migratePersistentStore(_ store: NSPersistentStore, toURL URL: NSURL, options options: [NSObject : AnyObject]?, withType storeType: String) throws -> NSPersistentStore ``` |
| To | ``` func migratePersistentStore(_ store: NSPersistentStore, to URL: URL, options options: [AnyHashable : Any]? = nil, withType storeType: String) throws -> NSPersistentStore ``` |

Modified [NSPersistentStoreCoordinator.perform(_: () -> Swift.Void)](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468794-perform)

|  | Declaration |
| --- | --- |
| From | ``` func performBlock(_ block: () -> Void) ``` |
| To | ``` func perform(_ block: @escaping () -> Swift.Void) ``` |

Modified [NSPersistentStoreCoordinator.performAndWait(_: () -> Swift.Void)](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468862-performandwait)

|  | Declaration |
| --- | --- |
| From | ``` func performBlockAndWait(_ block: () -> Void) ``` |
| To | ``` func performAndWait(_ block: @escaping () -> Swift.Void) ``` |

Modified [NSPersistentStoreCoordinator.persistentStore(for: URL) -> NSPersistentStore?](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468824-persistentstore)

|  | Declaration |
| --- | --- |
| From | ``` func persistentStoreForURL(_ URL: NSURL) -> NSPersistentStore? ``` |
| To | ``` func persistentStore(for URL: URL) -> NSPersistentStore? ``` |

Modified [NSPersistentStoreCoordinator.registerStoreClass(_: Swift.AnyClass, forStoreType: String) [class]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468786-registerstoreclass)

|  | Declaration |
| --- | --- |
| From | ``` class func registerStoreClass(_ storeClass: AnyClass, forStoreType storeType: String) ``` |
| To | ``` class func registerStoreClass(_ storeClass: Swift.AnyClass, forStoreType storeType: String) ``` |

Modified [NSPersistentStoreCoordinator.remove(_: NSPersistentStore) throws](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468907-removepersistentstore)

|  | Declaration |
| --- | --- |
| From | ``` func removePersistentStore(_ store: NSPersistentStore) throws ``` |
| To | ``` func remove(_ store: NSPersistentStore) throws ``` |

Modified [NSPersistentStoreCoordinator.removeUbiquitousContentAndPersistentStore(at: URL, options: [AnyHashable : Any]?) throws [class]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468923-removeubiquitouscontentandpersis)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` class func removeUbiquitousContentAndPersistentStoreAtURL(_ storeURL: NSURL, options options: [NSObject : AnyObject]?) throws ``` | iOS 7.0 | -- |
| To | ``` class func removeUbiquitousContentAndPersistentStore(at storeURL: URL, options options: [AnyHashable : Any]? = nil) throws ``` | iOS 5.0 | iOS 10.0 |

Modified [NSPersistentStoreCoordinator.replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, ofType: String) throws](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468917-replacepersistentstoreaturl)

|  | Declaration |
| --- | --- |
| From | ``` func replacePersistentStoreAtURL(_ destinationURL: NSURL, destinationOptions destinationOptions: [NSObject : AnyObject]?, withPersistentStoreFromURL sourceURL: NSURL, sourceOptions sourceOptions: [NSObject : AnyObject]?, storeType storeType: String) throws ``` |
| To | ``` func replacePersistentStore(at destinationURL: URL, destinationOptions destinationOptions: [AnyHashable : Any]? = nil, withPersistentStoreFrom sourceURL: URL, sourceOptions sourceOptions: [AnyHashable : Any]? = nil, ofType storeType: String) throws ``` |

Modified [NSPersistentStoreCoordinator.setMetadata(_: [String : Any]?, for: NSPersistentStore)](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468899-setmetadata)

|  | Declaration |
| --- | --- |
| From | ``` func setMetadata(_ metadata: [String : AnyObject]?, forPersistentStore store: NSPersistentStore) ``` |
| To | ``` func setMetadata(_ metadata: [String : Any]?, for store: NSPersistentStore) ``` |

Modified [NSPersistentStoreCoordinator.setMetadata(_: [String : Any]?, forPersistentStoreOfType: String?, at: URL) throws [class]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468897-setmetadata)

|  | Declaration |
| --- | --- |
| From | ``` class func setMetadata(_ metadata: [String : AnyObject]?, forPersistentStoreOfType storeType: String?, URL url: NSURL) throws ``` |
| To | ``` class func setMetadata(_ metadata: [String : Any]?, forPersistentStoreOfType storeType: String?, at url: URL) throws ``` |

Modified [NSPersistentStoreCoordinator.setMetadata(_: [String : Any]?, forPersistentStoreOfType: String, at: URL, options: [AnyHashable : Any]?) throws [class]](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468893-setmetadata)

|  | Declaration |
| --- | --- |
| From | ``` class func setMetadata(_ metadata: [String : AnyObject]?, forPersistentStoreOfType storeType: String, URL url: NSURL, options options: [NSObject : AnyObject]?) throws ``` |
| To | ``` class func setMetadata(_ metadata: [String : Any]?, forPersistentStoreOfType storeType: String, at url: URL, options options: [AnyHashable : Any]? = nil) throws ``` |

Modified [NSPersistentStoreCoordinator.setURL(_: URL, for: NSPersistentStore) -> Bool](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468858-seturl)

|  | Declaration |
| --- | --- |
| From | ``` func setURL(_ url: NSURL, forPersistentStore store: NSPersistentStore) -> Bool ``` |
| To | ``` func setURL(_ url: URL, for store: NSPersistentStore) -> Bool ``` |

Modified [NSPersistentStoreCoordinator.url(for: NSPersistentStore) -> URL](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468865-urlforpersistentstore)

|  | Declaration |
| --- | --- |
| From | ``` func URLForPersistentStore(_ store: NSPersistentStore) -> NSURL ``` |
| To | ``` func url(for store: NSPersistentStore) -> URL ``` |

Modified [NSPersistentStoreRequest](https://developer.apple.com/documentation/coredata/nspersistentstorerequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSPersistentStoreRequest : NSObject, NSCopying {     var affectedStores: [NSPersistentStore]?     var requestType: NSPersistentStoreRequestType { get } } ``` | NSCopying |
| To | ``` class NSPersistentStoreRequest : NSObject, NSCopying {     var affectedStores: [NSPersistentStore]?     var requestType: NSPersistentStoreRequestType { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSPersistentStoreRequest : CVarArg { } extension NSPersistentStoreRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [NSPersistentStoreRequestType [enum]](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype)

|  | Declaration |
| --- | --- |
| From | ``` enum NSPersistentStoreRequestType : UInt {     case FetchRequestType     case SaveRequestType     case BatchUpdateRequestType     case BatchDeleteRequestType } ``` |
| To | ``` enum NSPersistentStoreRequestType : UInt {     case fetchRequestType     case saveRequestType     case batchUpdateRequestType     case batchDeleteRequestType } ``` |

Modified [NSPersistentStoreRequestType.batchDeleteRequestType](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype/batchdeleterequesttype)

|  | Declaration |
| --- | --- |
| From | ``` case BatchDeleteRequestType ``` |
| To | ``` case batchDeleteRequestType ``` |

Modified [NSPersistentStoreRequestType.batchUpdateRequestType](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype/batchupdaterequesttype)

|  | Declaration |
| --- | --- |
| From | ``` case BatchUpdateRequestType ``` |
| To | ``` case batchUpdateRequestType ``` |

Modified [NSPersistentStoreRequestType.fetchRequestType](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype/fetchrequesttype)

|  | Declaration |
| --- | --- |
| From | ``` case FetchRequestType ``` |
| To | ``` case fetchRequestType ``` |

Modified [NSPersistentStoreRequestType.saveRequestType](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype/saverequesttype)

|  | Declaration |
| --- | --- |
| From | ``` case SaveRequestType ``` |
| To | ``` case saveRequestType ``` |

Modified [NSPersistentStoreResult](https://developer.apple.com/documentation/coredata/nspersistentstoreresult)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSPersistentStoreResult : NSObject { } ``` | -- |
| To | ``` class NSPersistentStoreResult : NSObject {     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSPersistentStoreResult : CVarArg { } extension NSPersistentStoreResult : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NSPersistentStoreUbiquitousTransitionType [enum]](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` enum NSPersistentStoreUbiquitousTransitionType : UInt {     case AccountAdded     case AccountRemoved     case ContentRemoved     case InitialImportCompleted } ``` | -- |
| To | ``` enum NSPersistentStoreUbiquitousTransitionType : UInt {     case accountAdded     case accountRemoved     case contentRemoved     case initialImportCompleted } ``` | iOS 10.0 |

Modified [NSPersistentStoreUbiquitousTransitionType.accountAdded](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype/accountadded)

|  | Declaration |
| --- | --- |
| From | ``` case AccountAdded ``` |
| To | ``` case accountAdded ``` |

Modified [NSPersistentStoreUbiquitousTransitionType.accountRemoved](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype/accountremoved)

|  | Declaration |
| --- | --- |
| From | ``` case AccountRemoved ``` |
| To | ``` case accountRemoved ``` |

Modified [NSPersistentStoreUbiquitousTransitionType.contentRemoved](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype/contentremoved)

|  | Declaration |
| --- | --- |
| From | ``` case ContentRemoved ``` |
| To | ``` case contentRemoved ``` |

Modified [NSPersistentStoreUbiquitousTransitionType.initialImportCompleted](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype/initialimportcompleted)

|  | Declaration |
| --- | --- |
| From | ``` case InitialImportCompleted ``` |
| To | ``` case initialImportCompleted ``` |

Modified [NSPropertyDescription](https://developer.apple.com/documentation/coredata/nspropertydescription)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSPropertyDescription : NSObject, NSCoding, NSCopying {     unowned(unsafe) var entity: NSEntityDescription { get }     var name: String     var optional: Bool     var transient: Bool     var validationPredicates: [NSPredicate] { get }     var validationWarnings: [AnyObject] { get }     func setValidationPredicates(_ validationPredicates: [NSPredicate]?, withValidationWarnings validationWarnings: [String]?)     var userInfo: [NSObject : AnyObject]?     var indexed: Bool     @NSCopying var versionHash: NSData { get }     var versionHashModifier: String?     var indexedBySpotlight: Bool     var storedInExternalRecord: Bool     var renamingIdentifier: String? } ``` | NSCoding, NSCopying |
| To | ``` class NSPropertyDescription : NSObject, NSCoding, NSCopying {     unowned(unsafe) var entity: NSEntityDescription { get }     var name: String     var isOptional: Bool     var isTransient: Bool     var validationPredicates: [NSPredicate] { get }     var validationWarnings: [Any] { get }     func setValidationPredicates(_ validationPredicates: [NSPredicate]?, withValidationWarnings validationWarnings: [String]?)     var userInfo: [AnyHashable : Any]?     var isIndexed: Bool     var versionHash: Data { get }     var versionHashModifier: String?     var isIndexedBySpotlight: Bool     var isStoredInExternalRecord: Bool     var renamingIdentifier: String?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSPropertyDescription : CVarArg { } extension NSPropertyDescription : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying |

Modified [NSPropertyDescription.isIndexed](https://developer.apple.com/documentation/coredata/nspropertydescription/1506669-isindexed)

|  | Declaration |
| --- | --- |
| From | ``` var indexed: Bool ``` |
| To | ``` var isIndexed: Bool ``` |

Modified [NSPropertyDescription.isIndexedBySpotlight](https://developer.apple.com/documentation/coredata/nspropertydescription/1506784-indexedbyspotlight)

|  | Declaration |
| --- | --- |
| From | ``` var indexedBySpotlight: Bool ``` |
| To | ``` var isIndexedBySpotlight: Bool ``` |

Modified [NSPropertyDescription.isOptional](https://developer.apple.com/documentation/coredata/nspropertydescription/1506735-isoptional)

|  | Declaration |
| --- | --- |
| From | ``` var optional: Bool ``` |
| To | ``` var isOptional: Bool ``` |

Modified [NSPropertyDescription.isStoredInExternalRecord](https://developer.apple.com/documentation/coredata/nspropertydescription/1506260-storedinexternalrecord)

|  | Declaration |
| --- | --- |
| From | ``` var storedInExternalRecord: Bool ``` |
| To | ``` var isStoredInExternalRecord: Bool ``` |

Modified [NSPropertyDescription.isTransient](https://developer.apple.com/documentation/coredata/nspropertydescription/1506766-transient)

|  | Declaration |
| --- | --- |
| From | ``` var transient: Bool ``` |
| To | ``` var isTransient: Bool ``` |

Modified [NSPropertyDescription.userInfo](https://developer.apple.com/documentation/coredata/nspropertydescription/1506833-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]? ``` |
| To | ``` var userInfo: [AnyHashable : Any]? ``` |

Modified [NSPropertyDescription.validationWarnings](https://developer.apple.com/documentation/coredata/nspropertydescription/1506886-validationwarnings)

|  | Declaration |
| --- | --- |
| From | ``` var validationWarnings: [AnyObject] { get } ``` |
| To | ``` var validationWarnings: [Any] { get } ``` |

Modified [NSPropertyDescription.versionHash](https://developer.apple.com/documentation/coredata/nspropertydescription/1506198-versionhash)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var versionHash: NSData { get } ``` |
| To | ``` var versionHash: Data { get } ``` |

Modified [NSPropertyMapping](https://developer.apple.com/documentation/coredata/nspropertymapping)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class NSPropertyMapping : NSObject {     var name: String?     var valueExpression: NSExpression?     var userInfo: [NSObject : AnyObject]? } ``` | -- |
| To | ``` class NSPropertyMapping : NSObject {     var name: String?     var valueExpression: NSExpression?     var userInfo: [AnyHashable : Any]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension NSPropertyMapping : CVarArg { } extension NSPropertyMapping : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [NSPropertyMapping.userInfo](https://developer.apple.com/documentation/coredata/nspropertymapping/1506516-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [NSObject : AnyObject]? ``` |
| To | ``` var userInfo: [AnyHashable : Any]? ``` |

Modified [NSRelationshipDescription](https://developer.apple.com/documentation/coredata/nsrelationshipdescription)

|  | Declaration |
| --- | --- |
| From | ``` class NSRelationshipDescription : NSPropertyDescription {     unowned(unsafe) var destinationEntity: NSEntityDescription?     unowned(unsafe) var inverseRelationship: NSRelationshipDescription?     var maxCount: Int     var minCount: Int     var deleteRule: NSDeleteRule     var toMany: Bool { get }     @NSCopying var versionHash: NSData { get }     var ordered: Bool } ``` |
| To | ``` class NSRelationshipDescription : NSPropertyDescription {     unowned(unsafe) var destinationEntity: NSEntityDescription?     unowned(unsafe) var inverseRelationship: NSRelationshipDescription?     var maxCount: Int     var minCount: Int     var deleteRule: NSDeleteRule     var isToMany: Bool { get }     var versionHash: Data { get }     var isOrdered: Bool } ``` |

Modified [NSRelationshipDescription.isOrdered](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/1506382-ordered)

|  | Declaration |
| --- | --- |
| From | ``` var ordered: Bool ``` |
| To | ``` var isOrdered: Bool ``` |

Modified [NSRelationshipDescription.isToMany](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/1506560-tomany)

|  | Declaration |
| --- | --- |
| From | ``` var toMany: Bool { get } ``` |
| To | ``` var isToMany: Bool { get } ``` |

Modified [NSRelationshipDescription.versionHash](https://developer.apple.com/documentation/coredata/nsrelationshipdescription/1506791-versionhash)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var versionHash: NSData { get } ``` |
| To | ``` var versionHash: Data { get } ``` |

Modified [NSSaveChangesRequest](https://developer.apple.com/documentation/coredata/nssavechangesrequest)

|  | Declaration |
| --- | --- |
| From | ``` class NSSaveChangesRequest : NSPersistentStoreRequest {     init(insertedObjects insertedObjects: Set<NSManagedObject>?, updatedObjects updatedObjects: Set<NSManagedObject>?, deletedObjects deletedObjects: Set<NSManagedObject>?, lockedObjects lockedObjects: Set<NSManagedObject>?)     var insertedObjects: Set<NSManagedObject>? { get }     var updatedObjects: Set<NSManagedObject>? { get }     var deletedObjects: Set<NSManagedObject>? { get }     var lockedObjects: Set<NSManagedObject>? { get } } ``` |
| To | ``` class NSSaveChangesRequest : NSPersistentStoreRequest {     init(inserted insertedObjects: Set<NSManagedObject>?, updated updatedObjects: Set<NSManagedObject>?, deleted deletedObjects: Set<NSManagedObject>?, locked lockedObjects: Set<NSManagedObject>?)     var insertedObjects: Set<NSManagedObject>? { get }     var updatedObjects: Set<NSManagedObject>? { get }     var deletedObjects: Set<NSManagedObject>? { get }     var lockedObjects: Set<NSManagedObject>? { get } } ``` |

Modified [NSSaveChangesRequest.init(inserted: Set<NSManagedObject>?, updated: Set<NSManagedObject>?, deleted: Set<NSManagedObject>?, locked: Set<NSManagedObject>?)](https://developer.apple.com/documentation/coredata/nssavechangesrequest/1500418-init)

|  | Declaration |
| --- | --- |
| From | ``` init(insertedObjects insertedObjects: Set<NSManagedObject>?, updatedObjects updatedObjects: Set<NSManagedObject>?, deletedObjects deletedObjects: Set<NSManagedObject>?, lockedObjects lockedObjects: Set<NSManagedObject>?) ``` |
| To | ``` init(inserted insertedObjects: Set<NSManagedObject>?, updated updatedObjects: Set<NSManagedObject>?, deleted deletedObjects: Set<NSManagedObject>?, locked lockedObjects: Set<NSManagedObject>?) ``` |

Modified [NSSnapshotEventType [struct]](https://developer.apple.com/documentation/coredata/nssnapshoteventtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSSnapshotEventType : OptionSetType {     init(rawValue rawValue: UInt)     static var UndoInsertion: NSSnapshotEventType { get }     static var UndoDeletion: NSSnapshotEventType { get }     static var UndoUpdate: NSSnapshotEventType { get }     static var Rollback: NSSnapshotEventType { get }     static var Refresh: NSSnapshotEventType { get }     static var MergePolicy: NSSnapshotEventType { get } } ``` | OptionSetType |
| To | ``` struct NSSnapshotEventType : OptionSet {     init(rawValue rawValue: UInt)     static var undoInsertion: NSSnapshotEventType { get }     static var undoDeletion: NSSnapshotEventType { get }     static var undoUpdate: NSSnapshotEventType { get }     static var rollback: NSSnapshotEventType { get }     static var refresh: NSSnapshotEventType { get }     static var mergePolicy: NSSnapshotEventType { get }     func intersect(_ other: NSSnapshotEventType) -> NSSnapshotEventType     func exclusiveOr(_ other: NSSnapshotEventType) -> NSSnapshotEventType     mutating func unionInPlace(_ other: NSSnapshotEventType)     mutating func intersectInPlace(_ other: NSSnapshotEventType)     mutating func exclusiveOrInPlace(_ other: NSSnapshotEventType)     func isSubsetOf(_ other: NSSnapshotEventType) -> Bool     func isDisjointWith(_ other: NSSnapshotEventType) -> Bool     func isSupersetOf(_ other: NSSnapshotEventType) -> Bool     mutating func subtractInPlace(_ other: NSSnapshotEventType)     func isStrictSupersetOf(_ other: NSSnapshotEventType) -> Bool     func isStrictSubsetOf(_ other: NSSnapshotEventType) -> Bool } extension NSSnapshotEventType {     func union(_ other: NSSnapshotEventType) -> NSSnapshotEventType     func intersection(_ other: NSSnapshotEventType) -> NSSnapshotEventType     func symmetricDifference(_ other: NSSnapshotEventType) -> NSSnapshotEventType } extension NSSnapshotEventType {     func contains(_ member: NSSnapshotEventType) -> Bool     mutating func insert(_ newMember: NSSnapshotEventType) -> (inserted: Bool, memberAfterInsert: NSSnapshotEventType)     mutating func remove(_ member: NSSnapshotEventType) -> NSSnapshotEventType?     mutating func update(with newMember: NSSnapshotEventType) -> NSSnapshotEventType? } extension NSSnapshotEventType {     convenience init()     mutating func formUnion(_ other: NSSnapshotEventType)     mutating func formIntersection(_ other: NSSnapshotEventType)     mutating func formSymmetricDifference(_ other: NSSnapshotEventType) } extension NSSnapshotEventType {     convenience init<S : Sequence where S.Iterator.Element == NSSnapshotEventType>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: NSSnapshotEventType...)     mutating func subtract(_ other: NSSnapshotEventType)     func isSubset(of other: NSSnapshotEventType) -> Bool     func isSuperset(of other: NSSnapshotEventType) -> Bool     func isDisjoint(with other: NSSnapshotEventType) -> Bool     func subtracting(_ other: NSSnapshotEventType) -> NSSnapshotEventType     var isEmpty: Bool { get }     func isStrictSuperset(of other: NSSnapshotEventType) -> Bool     func isStrictSubset(of other: NSSnapshotEventType) -> Bool } ``` | OptionSet |

Modified [NSSnapshotEventType.mergePolicy](https://developer.apple.com/documentation/coredata/nssnapshoteventtype/nssnapshoteventmergepolicy)

|  | Declaration |
| --- | --- |
| From | ``` static var MergePolicy: NSSnapshotEventType { get } ``` |
| To | ``` static var mergePolicy: NSSnapshotEventType { get } ``` |

Modified [NSSnapshotEventType.refresh](https://developer.apple.com/documentation/coredata/nssnapshoteventtype/1506602-refresh)

|  | Declaration |
| --- | --- |
| From | ``` static var Refresh: NSSnapshotEventType { get } ``` |
| To | ``` static var refresh: NSSnapshotEventType { get } ``` |

Modified [NSSnapshotEventType.rollback](https://developer.apple.com/documentation/coredata/nssnapshoteventtype/nssnapshoteventrollback)

|  | Declaration |
| --- | --- |
| From | ``` static var Rollback: NSSnapshotEventType { get } ``` |
| To | ``` static var rollback: NSSnapshotEventType { get } ``` |

Modified [NSSnapshotEventType.undoDeletion](https://developer.apple.com/documentation/coredata/nssnapshoteventtype/nssnapshoteventundodeletion)

|  | Declaration |
| --- | --- |
| From | ``` static var UndoDeletion: NSSnapshotEventType { get } ``` |
| To | ``` static var undoDeletion: NSSnapshotEventType { get } ``` |

Modified [NSSnapshotEventType.undoInsertion](https://developer.apple.com/documentation/coredata/nssnapshoteventtype/nssnapshoteventundoinsertion)

|  | Declaration |
| --- | --- |
| From | ``` static var UndoInsertion: NSSnapshotEventType { get } ``` |
| To | ``` static var undoInsertion: NSSnapshotEventType { get } ``` |

Modified [NSSnapshotEventType.undoUpdate](https://developer.apple.com/documentation/coredata/nssnapshoteventtype/nssnapshoteventundoupdate)

|  | Declaration |
| --- | --- |
| From | ``` static var UndoUpdate: NSSnapshotEventType { get } ``` |
| To | ``` static var undoUpdate: NSSnapshotEventType { get } ``` |

Modified [NSFetchRequestExpressionType](https://developer.apple.com/documentation/coredata/nsfetchrequestexpressiontype)

|  | Declaration |
| --- | --- |
| From | ``` let NSFetchRequestExpressionType: NSExpressionType ``` |
| To | ``` let NSFetchRequestExpressionType: NSExpression.ExpressionType ``` |

Modified [NSPersistentStoreAsynchronousFetchResultCompletionBlock](https://developer.apple.com/documentation/coredata/nspersistentstoreasynchronousfetchresultcompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias NSPersistentStoreAsynchronousFetchResultCompletionBlock = (NSAsynchronousFetchResult) -> Void ``` |
| To | ``` typealias NSPersistentStoreAsynchronousFetchResultCompletionBlock = (NSAsynchronousFetchResult<NSFetchRequestResult>) -> Swift.Void ``` |

Modified [NSPersistentStoreRebuildFromUbiquitousContentOption](https://developer.apple.com/documentation/coredata/nspersistentstorerebuildfromubiquitouscontentoption)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [NSPersistentStoreRemoveUbiquitousMetadataOption](https://developer.apple.com/documentation/coredata/nspersistentstoreremoveubiquitousmetadataoption)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [NSPersistentStoreUbiquitousContainerIdentifierKey](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitouscontaineridentifierkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [NSPersistentStoreUbiquitousContentNameKey](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitouscontentnamekey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [NSPersistentStoreUbiquitousContentURLKey](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitouscontenturlkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [NSPersistentStoreUbiquitousPeerTokenOption](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitouspeertokenoption)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [NSPersistentStoreUbiquitousTransitionTypeKey](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontypekey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
