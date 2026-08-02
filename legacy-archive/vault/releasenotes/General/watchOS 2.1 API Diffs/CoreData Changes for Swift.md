---
title: watchOS 2.1 API Diffs
apple_id: TP40016636
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS21APIDiffs/Swift/CoreData.html
archived_at: '2026-07-18T02:58:07.810949Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.1 API Diffs](watchOS%202.0%20to%20watchOS%202.1%20API%20Differences.md)


# CoreData Changes for Swift

### CoreData

Removed NSCocoaError.PersistentStoreIncompleteSaveErrorRemoved NSCocoaError.ValidationRelationshipDeniedDeleteErrorAdded NSCocoaError.PersistentStoreIncompvareSaveErrorAdded NSCocoaError.ValidationRelationshipDeniedDevareErrorModified [NSAsynchronousFetchRequest](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSAsynchronousFetchResult](https://developer.apple.com/documentation/coredata/nsasynchronousfetchresult)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSAtomicStore](https://developer.apple.com/documentation/coredata/nsatomicstore)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSAtomicStoreCacheNode](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSAttributeDescription](https://developer.apple.com/documentation/coredata/nsattributedescription)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSAttributeType [enum]](https://developer.apple.com/documentation/coredata/nsattributetype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSBatchDeleteRequest](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSBatchDeleteRequestResultType [enum]](https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSBatchDeleteResult](https://developer.apple.com/documentation/coredata/nsbatchdeleteresult)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSBatchUpdateRequest](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSBatchUpdateRequestResultType [enum]](https://developer.apple.com/documentation/coredata/nsbatchupdaterequestresulttype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSBatchUpdateResult](https://developer.apple.com/documentation/coredata/nsbatchupdateresult)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified NSCocoaError.CoreDataError

|  | Declaration |
| --- | --- |
| From | ``` static let CoreDataError: NSCocoaError ``` |
| To | ``` static var CoreDataError: NSCocoaError { get } ``` |

Modified NSCocoaError.EntityMigrationPolicyError

|  | Declaration |
| --- | --- |
| From | ``` static let EntityMigrationPolicyError: NSCocoaError ``` |
| To | ``` static var EntityMigrationPolicyError: NSCocoaError { get } ``` |

Modified NSCocoaError.ExternalRecordImportError

|  | Declaration |
| --- | --- |
| From | ``` static let ExternalRecordImportError: NSCocoaError ``` |
| To | ``` static var ExternalRecordImportError: NSCocoaError { get } ``` |

Modified NSCocoaError.InferredMappingModelError

|  | Declaration |
| --- | --- |
| From | ``` static let InferredMappingModelError: NSCocoaError ``` |
| To | ``` static var InferredMappingModelError: NSCocoaError { get } ``` |

Modified NSCocoaError.ManagedObjectConstraintMergeError

|  | Declaration |
| --- | --- |
| From | ``` static let ManagedObjectConstraintMergeError: NSCocoaError ``` |
| To | ``` static var ManagedObjectConstraintMergeError: NSCocoaError { get } ``` |

Modified NSCocoaError.ManagedObjectContextLockingError

|  | Declaration |
| --- | --- |
| From | ``` static let ManagedObjectContextLockingError: NSCocoaError ``` |
| To | ``` static var ManagedObjectContextLockingError: NSCocoaError { get } ``` |

Modified NSCocoaError.ManagedObjectExternalRelationshipError

|  | Declaration |
| --- | --- |
| From | ``` static let ManagedObjectExternalRelationshipError: NSCocoaError ``` |
| To | ``` static var ManagedObjectExternalRelationshipError: NSCocoaError { get } ``` |

Modified NSCocoaError.ManagedObjectMergeError

|  | Declaration |
| --- | --- |
| From | ``` static let ManagedObjectMergeError: NSCocoaError ``` |
| To | ``` static var ManagedObjectMergeError: NSCocoaError { get } ``` |

Modified NSCocoaError.ManagedObjectReferentialIntegrityError

|  | Declaration |
| --- | --- |
| From | ``` static let ManagedObjectReferentialIntegrityError: NSCocoaError ``` |
| To | ``` static var ManagedObjectReferentialIntegrityError: NSCocoaError { get } ``` |

Modified NSCocoaError.ManagedObjectValidationError

|  | Declaration |
| --- | --- |
| From | ``` static let ManagedObjectValidationError: NSCocoaError ``` |
| To | ``` static var ManagedObjectValidationError: NSCocoaError { get } ``` |

Modified NSCocoaError.MigrationCancelledError

|  | Declaration |
| --- | --- |
| From | ``` static let MigrationCancelledError: NSCocoaError ``` |
| To | ``` static var MigrationCancelledError: NSCocoaError { get } ``` |

Modified NSCocoaError.MigrationError

|  | Declaration |
| --- | --- |
| From | ``` static let MigrationError: NSCocoaError ``` |
| To | ``` static var MigrationError: NSCocoaError { get } ``` |

Modified NSCocoaError.MigrationManagerDestinationStoreError

|  | Declaration |
| --- | --- |
| From | ``` static let MigrationManagerDestinationStoreError: NSCocoaError ``` |
| To | ``` static var MigrationManagerDestinationStoreError: NSCocoaError { get } ``` |

Modified NSCocoaError.MigrationManagerSourceStoreError

|  | Declaration |
| --- | --- |
| From | ``` static let MigrationManagerSourceStoreError: NSCocoaError ``` |
| To | ``` static var MigrationManagerSourceStoreError: NSCocoaError { get } ``` |

Modified NSCocoaError.MigrationMissingMappingModelError

|  | Declaration |
| --- | --- |
| From | ``` static let MigrationMissingMappingModelError: NSCocoaError ``` |
| To | ``` static var MigrationMissingMappingModelError: NSCocoaError { get } ``` |

Modified NSCocoaError.MigrationMissingSourceModelError

|  | Declaration |
| --- | --- |
| From | ``` static let MigrationMissingSourceModelError: NSCocoaError ``` |
| To | ``` static var MigrationMissingSourceModelError: NSCocoaError { get } ``` |

Modified NSCocoaError.PersistentStoreCoordinatorLockingError

|  | Declaration |
| --- | --- |
| From | ``` static let PersistentStoreCoordinatorLockingError: NSCocoaError ``` |
| To | ``` static var PersistentStoreCoordinatorLockingError: NSCocoaError { get } ``` |

Modified NSCocoaError.PersistentStoreIncompatibleSchemaError

|  | Declaration |
| --- | --- |
| From | ``` static let PersistentStoreIncompatibleSchemaError: NSCocoaError ``` |
| To | ``` static var PersistentStoreIncompatibleSchemaError: NSCocoaError { get } ``` |

Modified NSCocoaError.PersistentStoreIncompatibleVersionHashError

|  | Declaration |
| --- | --- |
| From | ``` static let PersistentStoreIncompatibleVersionHashError: NSCocoaError ``` |
| To | ``` static var PersistentStoreIncompatibleVersionHashError: NSCocoaError { get } ``` |

Modified NSCocoaError.PersistentStoreInvalidTypeError

|  | Declaration |
| --- | --- |
| From | ``` static let PersistentStoreInvalidTypeError: NSCocoaError ``` |
| To | ``` static var PersistentStoreInvalidTypeError: NSCocoaError { get } ``` |

Modified NSCocoaError.PersistentStoreOpenError

|  | Declaration |
| --- | --- |
| From | ``` static let PersistentStoreOpenError: NSCocoaError ``` |
| To | ``` static var PersistentStoreOpenError: NSCocoaError { get } ``` |

Modified NSCocoaError.PersistentStoreOperationError

|  | Declaration |
| --- | --- |
| From | ``` static let PersistentStoreOperationError: NSCocoaError ``` |
| To | ``` static var PersistentStoreOperationError: NSCocoaError { get } ``` |

Modified NSCocoaError.PersistentStoreSaveConflictsError

|  | Declaration |
| --- | --- |
| From | ``` static let PersistentStoreSaveConflictsError: NSCocoaError ``` |
| To | ``` static var PersistentStoreSaveConflictsError: NSCocoaError { get } ``` |

Modified NSCocoaError.PersistentStoreSaveError

|  | Declaration |
| --- | --- |
| From | ``` static let PersistentStoreSaveError: NSCocoaError ``` |
| To | ``` static var PersistentStoreSaveError: NSCocoaError { get } ``` |

Modified NSCocoaError.PersistentStoreTimeoutError

|  | Declaration |
| --- | --- |
| From | ``` static let PersistentStoreTimeoutError: NSCocoaError ``` |
| To | ``` static var PersistentStoreTimeoutError: NSCocoaError { get } ``` |

Modified NSCocoaError.PersistentStoreTypeMismatchError

|  | Declaration |
| --- | --- |
| From | ``` static let PersistentStoreTypeMismatchError: NSCocoaError ``` |
| To | ``` static var PersistentStoreTypeMismatchError: NSCocoaError { get } ``` |

Modified NSCocoaError.PersistentStoreUnsupportedRequestTypeError

|  | Declaration |
| --- | --- |
| From | ``` static let PersistentStoreUnsupportedRequestTypeError: NSCocoaError ``` |
| To | ``` static var PersistentStoreUnsupportedRequestTypeError: NSCocoaError { get } ``` |

Modified NSCocoaError.SQLiteError

|  | Declaration |
| --- | --- |
| From | ``` static let SQLiteError: NSCocoaError ``` |
| To | ``` static var SQLiteError: NSCocoaError { get } ``` |

Modified NSCocoaError.ValidationDateTooLateError

|  | Declaration |
| --- | --- |
| From | ``` static let ValidationDateTooLateError: NSCocoaError ``` |
| To | ``` static var ValidationDateTooLateError: NSCocoaError { get } ``` |

Modified NSCocoaError.ValidationDateTooSoonError

|  | Declaration |
| --- | --- |
| From | ``` static let ValidationDateTooSoonError: NSCocoaError ``` |
| To | ``` static var ValidationDateTooSoonError: NSCocoaError { get } ``` |

Modified NSCocoaError.ValidationInvalidDateError

|  | Declaration |
| --- | --- |
| From | ``` static let ValidationInvalidDateError: NSCocoaError ``` |
| To | ``` static var ValidationInvalidDateError: NSCocoaError { get } ``` |

Modified NSCocoaError.ValidationMissingMandatoryPropertyError

|  | Declaration |
| --- | --- |
| From | ``` static let ValidationMissingMandatoryPropertyError: NSCocoaError ``` |
| To | ``` static var ValidationMissingMandatoryPropertyError: NSCocoaError { get } ``` |

Modified NSCocoaError.ValidationMultipleErrorsError

|  | Declaration |
| --- | --- |
| From | ``` static let ValidationMultipleErrorsError: NSCocoaError ``` |
| To | ``` static var ValidationMultipleErrorsError: NSCocoaError { get } ``` |

Modified NSCocoaError.ValidationNumberTooLargeError

|  | Declaration |
| --- | --- |
| From | ``` static let ValidationNumberTooLargeError: NSCocoaError ``` |
| To | ``` static var ValidationNumberTooLargeError: NSCocoaError { get } ``` |

Modified NSCocoaError.ValidationNumberTooSmallError

|  | Declaration |
| --- | --- |
| From | ``` static let ValidationNumberTooSmallError: NSCocoaError ``` |
| To | ``` static var ValidationNumberTooSmallError: NSCocoaError { get } ``` |

Modified NSCocoaError.ValidationRelationshipExceedsMaximumCountError

|  | Declaration |
| --- | --- |
| From | ``` static let ValidationRelationshipExceedsMaximumCountError: NSCocoaError ``` |
| To | ``` static var ValidationRelationshipExceedsMaximumCountError: NSCocoaError { get } ``` |

Modified NSCocoaError.ValidationRelationshipLacksMinimumCountError

|  | Declaration |
| --- | --- |
| From | ``` static let ValidationRelationshipLacksMinimumCountError: NSCocoaError ``` |
| To | ``` static var ValidationRelationshipLacksMinimumCountError: NSCocoaError { get } ``` |

Modified NSCocoaError.ValidationStringPatternMatchingError

|  | Declaration |
| --- | --- |
| From | ``` static let ValidationStringPatternMatchingError: NSCocoaError ``` |
| To | ``` static var ValidationStringPatternMatchingError: NSCocoaError { get } ``` |

Modified NSCocoaError.ValidationStringTooLongError

|  | Declaration |
| --- | --- |
| From | ``` static let ValidationStringTooLongError: NSCocoaError ``` |
| To | ``` static var ValidationStringTooLongError: NSCocoaError { get } ``` |

Modified NSCocoaError.ValidationStringTooShortError

|  | Declaration |
| --- | --- |
| From | ``` static let ValidationStringTooShortError: NSCocoaError ``` |
| To | ``` static var ValidationStringTooShortError: NSCocoaError { get } ``` |

Modified [NSConstraintConflict](https://developer.apple.com/documentation/coredata/nsconstraintconflict)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSDeleteRule [enum]](https://developer.apple.com/documentation/coredata/nsdeleterule)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSEntityDescription](https://developer.apple.com/documentation/coredata/nsentitydescription)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSFastEnumeration |
| To | NSCoding, NSCopying, NSFastEnumeration |

Modified [NSEntityMapping](https://developer.apple.com/documentation/coredata/nsentitymapping)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSEntityMappingType [enum]](https://developer.apple.com/documentation/coredata/nsentitymappingtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSEntityMigrationPolicy](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSExpressionDescription](https://developer.apple.com/documentation/coredata/nsexpressiondescription)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSFetchedPropertyDescription](https://developer.apple.com/documentation/coredata/nsfetchedpropertydescription)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSFetchedResultsChangeType [enum]](https://developer.apple.com/documentation/coredata/nsfetchedresultschangetype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSFetchedResultsController](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding |
| To | NSCoding |

Modified [NSFetchRequestExpression](https://developer.apple.com/documentation/coredata/nsfetchrequestexpression)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSIncrementalStore](https://developer.apple.com/documentation/coredata/nsincrementalstore)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSIncrementalStoreNode](https://developer.apple.com/documentation/coredata/nsincrementalstorenode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding |
| To | NSCoding |

Modified [NSManagedObjectContextConcurrencyType [enum]](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSManagedObjectID](https://developer.apple.com/documentation/coredata/nsmanagedobjectid)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [NSManagedObjectModel](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying, NSFastEnumeration |
| To | NSCoding, NSCopying, NSFastEnumeration |

Modified [NSMappingModel](https://developer.apple.com/documentation/coredata/nsmappingmodel)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMergeConflict](https://developer.apple.com/documentation/coredata/nsmergeconflict)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMergePolicy](https://developer.apple.com/documentation/coredata/nsmergepolicy)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSMergePolicyType [enum]](https://developer.apple.com/documentation/coredata/nsmergepolicytype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSMigrationManager](https://developer.apple.com/documentation/coredata/nsmigrationmanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSPersistentStore](https://developer.apple.com/documentation/coredata/nspersistentstore)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSPersistentStoreAsynchronousResult](https://developer.apple.com/documentation/coredata/nspersistentstoreasynchronousresult)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSPersistentStoreCoordinator](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSPersistentStoreRequest](https://developer.apple.com/documentation/coredata/nspersistentstorerequest)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [NSPersistentStoreRequestType [enum]](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [NSPersistentStoreResult](https://developer.apple.com/documentation/coredata/nspersistentstoreresult)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSPropertyDescription](https://developer.apple.com/documentation/coredata/nspropertydescription)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSCopying |
| To | NSCoding, NSCopying |

Modified [NSPropertyMapping](https://developer.apple.com/documentation/coredata/nspropertymapping)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSRelationshipDescription](https://developer.apple.com/documentation/coredata/nsrelationshipdescription)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [NSSaveChangesRequest](https://developer.apple.com/documentation/coredata/nssavechangesrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

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
