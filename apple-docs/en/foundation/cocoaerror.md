---
title: CocoaError
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/cocoaerror
source_url: 'https://developer.apple.com/documentation/foundation/cocoaerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/cocoaerror.json'
content_hash: 'sha256:4bdb88b479e650d0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# CocoaError

<sub>Structure</sub>

Describes errors within the Cocoa error domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CocoaError
```

## Relationships

- **Conforms To**: [CustomNSError](customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Structures

- [Code](cocoaerror/code.md) — The error code itself.

### Instance Properties

- [affectedObjects](cocoaerror/affectedobjects.md)
- [affectedStores](cocoaerror/affectedstores.md)
- [filePath](cocoaerror/filepath.md) — The file path associated with the error, if any.
- [isCoderError](cocoaerror/iscodererror.md)
- [isExecutableError](cocoaerror/isexecutableerror.md)
- [isFileError](cocoaerror/isfileerror.md)
- [isFontError](cocoaerror/isfonterror.md)
- [isFormattingError](cocoaerror/isformattingerror.md)
- [isPropertyListError](cocoaerror/ispropertylisterror.md)
- [isServiceError](cocoaerror/isserviceerror.md)
- [isSharingServiceError](cocoaerror/issharingserviceerror.md)
- [isTextReadWriteError](cocoaerror/istextreadwriteerror.md)
- [isUbiquitousFileError](cocoaerror/isubiquitousfileerror.md)
- [isUserActivityError](cocoaerror/isuseractivityerror.md)
- [isValidationError](cocoaerror/isvalidationerror.md)
- [isXPCConnectionError](cocoaerror/isxpcconnectionerror.md)
- [persistentStoreSaveConflicts](cocoaerror/persistentstoresaveconflicts-swift.property.md)
- [stringEncoding](cocoaerror/stringencoding.md) — The string encoding associated with this error, if any.
- [underlying](cocoaerror/underlying.md) — The underlying error behind this error, if any.
- [underlyingErrors](cocoaerror/underlyingerrors.md) — A list of underlying errors, if any. It includes the values of both NSUnderlyingErrorKey and NSMultipleUnderlyingErrorsKey. If there are no underlying errors, returns an empty array.
- [url](cocoaerror/url.md) — The URL associated with this error, if any.
- [validationKey](cocoaerror/validationkey.md)
- [validationObject](cocoaerror/validationobject.md)
- [validationPredicate](cocoaerror/validationpredicate.md)
- [validationValue](cocoaerror/validationvalue.md)

### Type Properties

- [ServiceApplicationLaunchFailedError](cocoaerror/serviceapplicationlaunchfailederror-4hf03.md) _(deprecated)_
- [ServiceApplicationNotFoundError](cocoaerror/serviceapplicationnotfounderror-9j679.md) _(deprecated)_
- [ServiceInvalidPasteboardDataError](cocoaerror/serviceinvalidpasteboarddataerror-4tjaw.md) _(deprecated)_
- [ServiceMalformedServiceDictionaryError](cocoaerror/servicemalformedservicedictionaryerror-5cpn1.md) _(deprecated)_
- [ServiceMiscellaneousError](cocoaerror/servicemiscellaneouserror-3ti3r.md) _(deprecated)_
- [ServiceRequestTimedOutError](cocoaerror/servicerequesttimedouterror-7kzoa.md) _(deprecated)_
- [SharingServiceNotConfiguredError](cocoaerror/sharingservicenotconfigurederror-5lamn.md) _(deprecated)_
- [TextReadInapplicableDocumentTypeError](cocoaerror/textreadinapplicabledocumenttypeerror-9o1dx.md) _(deprecated)_
- [TextWriteInapplicableDocumentTypeError](cocoaerror/textwriteinapplicabledocumenttypeerror-4aoa6.md) _(deprecated)_
- [coderInvalidValue](cocoaerror/coderinvalidvalue.md)
- [coderReadCorrupt](cocoaerror/coderreadcorrupt.md)
- [coderReadCorruptError](cocoaerror/coderreadcorrupterror.md) _(deprecated)_
- [coderValueNotFound](cocoaerror/codervaluenotfound.md)
- [coderValueNotFoundError](cocoaerror/codervaluenotfounderror.md) _(deprecated)_
- [coreData](cocoaerror/coredata.md)
- [coreDataError](cocoaerror/coredataerror.md) _(deprecated)_
- [entityMigrationPolicy](cocoaerror/entitymigrationpolicy.md)
- [entityMigrationPolicyError](cocoaerror/entitymigrationpolicyerror.md) _(deprecated)_
- [executableArchitectureMismatch](cocoaerror/executablearchitecturemismatch.md)
- [executableArchitectureMismatchError](cocoaerror/executablearchitecturemismatcherror.md) _(deprecated)_
- [executableLink](cocoaerror/executablelink.md)
- [executableLinkError](cocoaerror/executablelinkerror.md) _(deprecated)_
- [executableLoad](cocoaerror/executableload.md)
- [executableLoadError](cocoaerror/executableloaderror.md) _(deprecated)_
- [executableNotLoadable](cocoaerror/executablenotloadable.md)
- [executableNotLoadableError](cocoaerror/executablenotloadableerror.md) _(deprecated)_
- [executableRuntimeMismatch](cocoaerror/executableruntimemismatch.md)
- [executableRuntimeMismatchError](cocoaerror/executableruntimemismatcherror.md) _(deprecated)_
- [externalRecordImport](cocoaerror/externalrecordimport.md)
- [externalRecordImportError](cocoaerror/externalrecordimporterror.md) _(deprecated)_
- [featureUnsupported](cocoaerror/featureunsupported.md)
- [featureUnsupportedError](cocoaerror/featureunsupportederror.md) _(deprecated)_
- [fileLocking](cocoaerror/filelocking.md)
- [fileLockingError](cocoaerror/filelockingerror.md) _(deprecated)_
- [fileManagerUnmountBusy](cocoaerror/filemanagerunmountbusy.md)
- [fileManagerUnmountBusyError](cocoaerror/filemanagerunmountbusyerror.md) _(deprecated)_
- [fileManagerUnmountUnknown](cocoaerror/filemanagerunmountunknown.md)
- [fileManagerUnmountUnknownError](cocoaerror/filemanagerunmountunknownerror.md) _(deprecated)_
- [fileNoSuchFile](cocoaerror/filenosuchfile.md)
- [fileNoSuchFileError](cocoaerror/filenosuchfileerror.md) _(deprecated)_
- [fileReadCorruptFile](cocoaerror/filereadcorruptfile.md)
- [fileReadCorruptFileError](cocoaerror/filereadcorruptfileerror.md) _(deprecated)_
- [fileReadInapplicableStringEncoding](cocoaerror/filereadinapplicablestringencoding.md)
- [fileReadInapplicableStringEncodingError](cocoaerror/filereadinapplicablestringencodingerror.md) _(deprecated)_
- [fileReadInvalidFileName](cocoaerror/filereadinvalidfilename.md)
- [fileReadInvalidFileNameError](cocoaerror/filereadinvalidfilenameerror.md) _(deprecated)_
- [fileReadNoPermission](cocoaerror/filereadnopermission.md)
- [fileReadNoPermissionError](cocoaerror/filereadnopermissionerror.md) _(deprecated)_
- [fileReadNoSuchFile](cocoaerror/filereadnosuchfile.md)
- [fileReadNoSuchFileError](cocoaerror/filereadnosuchfileerror.md) _(deprecated)_
- [fileReadTooLarge](cocoaerror/filereadtoolarge.md)
- [fileReadTooLargeError](cocoaerror/filereadtoolargeerror.md) _(deprecated)_
- [fileReadUnknown](cocoaerror/filereadunknown.md)
- [fileReadUnknownError](cocoaerror/filereadunknownerror.md) _(deprecated)_
- [fileReadUnknownStringEncoding](cocoaerror/filereadunknownstringencoding.md)
- [fileReadUnknownStringEncodingError](cocoaerror/filereadunknownstringencodingerror.md) _(deprecated)_
- [fileReadUnsupportedScheme](cocoaerror/filereadunsupportedscheme.md)
- [fileReadUnsupportedSchemeError](cocoaerror/filereadunsupportedschemeerror.md) _(deprecated)_
- [fileWriteFileExists](cocoaerror/filewritefileexists.md)
- [fileWriteFileExistsError](cocoaerror/filewritefileexistserror.md) _(deprecated)_
- [fileWriteInapplicableStringEncoding](cocoaerror/filewriteinapplicablestringencoding.md)
- [fileWriteInapplicableStringEncodingError](cocoaerror/filewriteinapplicablestringencodingerror.md) _(deprecated)_
- [fileWriteInvalidFileName](cocoaerror/filewriteinvalidfilename.md)
- [fileWriteInvalidFileNameError](cocoaerror/filewriteinvalidfilenameerror.md) _(deprecated)_
- [fileWriteNoPermission](cocoaerror/filewritenopermission.md)
- [fileWriteNoPermissionError](cocoaerror/filewritenopermissionerror.md) _(deprecated)_
- [fileWriteOutOfSpace](cocoaerror/filewriteoutofspace.md)
- [fileWriteOutOfSpaceError](cocoaerror/filewriteoutofspaceerror.md) _(deprecated)_
- [fileWriteUnknown](cocoaerror/filewriteunknown.md)
- [fileWriteUnknownError](cocoaerror/filewriteunknownerror.md) _(deprecated)_
- [fileWriteUnsupportedScheme](cocoaerror/filewriteunsupportedscheme.md)
- [fileWriteUnsupportedSchemeError](cocoaerror/filewriteunsupportedschemeerror.md) _(deprecated)_
- [fileWriteVolumeReadOnly](cocoaerror/filewritevolumereadonly.md)
- [fileWriteVolumeReadOnlyError](cocoaerror/filewritevolumereadonlyerror.md) _(deprecated)_
- [fontAssetDownloadError](cocoaerror/fontassetdownloaderror.md)
- [formatting](cocoaerror/formatting.md)
- [formattingError](cocoaerror/formattingerror.md) _(deprecated)_
- [inferredMappingModel](cocoaerror/inferredmappingmodel.md)
- [inferredMappingModelError](cocoaerror/inferredmappingmodelerror.md) _(deprecated)_
- [keyValueValidation](cocoaerror/keyvaluevalidation.md)
- [keyValueValidationError](cocoaerror/keyvaluevalidationerror.md) _(deprecated)_
- [managedObjectConstraintMerge](cocoaerror/managedobjectconstraintmerge.md)
- [managedObjectConstraintMergeError](cocoaerror/managedobjectconstraintmergeerror.md) _(deprecated)_
- [managedObjectContextLocking](cocoaerror/managedobjectcontextlocking.md)
- [managedObjectContextLockingError](cocoaerror/managedobjectcontextlockingerror.md) _(deprecated)_
- [managedObjectExternalRelationship](cocoaerror/managedobjectexternalrelationship.md)
- [managedObjectExternalRelationshipError](cocoaerror/managedobjectexternalrelationshiperror.md) _(deprecated)_
- [managedObjectMerge](cocoaerror/managedobjectmerge.md)
- [managedObjectMergeError](cocoaerror/managedobjectmergeerror.md) _(deprecated)_
- [managedObjectReferentialIntegrity](cocoaerror/managedobjectreferentialintegrity.md)
- [managedObjectReferentialIntegrityError](cocoaerror/managedobjectreferentialintegrityerror.md) _(deprecated)_
- [managedObjectValidation](cocoaerror/managedobjectvalidation.md)
- [managedObjectValidationError](cocoaerror/managedobjectvalidationerror.md) _(deprecated)_
- [migration](cocoaerror/migration.md)
- [migrationCancelled](cocoaerror/migrationcancelled.md)
- [migrationCancelledError](cocoaerror/migrationcancellederror.md) _(deprecated)_
- [migrationError](cocoaerror/migrationerror.md) _(deprecated)_
- [migrationManagerDestinationStore](cocoaerror/migrationmanagerdestinationstore.md)
- [migrationManagerDestinationStoreError](cocoaerror/migrationmanagerdestinationstoreerror.md) _(deprecated)_
- [migrationManagerSourceStore](cocoaerror/migrationmanagersourcestore.md)
- [migrationManagerSourceStoreError](cocoaerror/migrationmanagersourcestoreerror.md) _(deprecated)_
- [migrationMissingMappingModel](cocoaerror/migrationmissingmappingmodel.md)
- [migrationMissingMappingModelError](cocoaerror/migrationmissingmappingmodelerror.md) _(deprecated)_
- [migrationMissingSourceModel](cocoaerror/migrationmissingsourcemodel.md)
- [migrationMissingSourceModelError](cocoaerror/migrationmissingsourcemodelerror.md) _(deprecated)_
- [persistentStoreCoordinatorLocking](cocoaerror/persistentstorecoordinatorlocking.md)
- [persistentStoreCoordinatorLockingError](cocoaerror/persistentstorecoordinatorlockingerror.md) _(deprecated)_
- [persistentStoreIncompatibleSchema](cocoaerror/persistentstoreincompatibleschema.md)
- [persistentStoreIncompatibleSchemaError](cocoaerror/persistentstoreincompatibleschemaerror.md) _(deprecated)_
- [persistentStoreIncompatibleVersionHash](cocoaerror/persistentstoreincompatibleversionhash.md)
- [persistentStoreIncompatibleVersionHashError](cocoaerror/persistentstoreincompatibleversionhasherror.md) _(deprecated)_
- [persistentStoreIncompleteSave](cocoaerror/persistentstoreincompletesave.md)
- [persistentStoreIncompleteSaveError](cocoaerror/persistentstoreincompletesaveerror.md) _(deprecated)_
- [persistentStoreInvalidType](cocoaerror/persistentstoreinvalidtype.md)
- [persistentStoreInvalidTypeError](cocoaerror/persistentstoreinvalidtypeerror.md) _(deprecated)_
- [persistentStoreOpen](cocoaerror/persistentstoreopen.md)
- [persistentStoreOpenError](cocoaerror/persistentstoreopenerror.md) _(deprecated)_
- [persistentStoreOperation](cocoaerror/persistentstoreoperation.md)
- [persistentStoreOperationError](cocoaerror/persistentstoreoperationerror.md) _(deprecated)_
- [persistentStoreSave](cocoaerror/persistentstoresave.md)
- [persistentStoreSaveConflicts](cocoaerror/persistentstoresaveconflicts-swift.type.property.md)
- [persistentStoreSaveConflictsError](cocoaerror/persistentstoresaveconflictserror.md) _(deprecated)_
- [persistentStoreSaveError](cocoaerror/persistentstoresaveerror.md) _(deprecated)_
- [persistentStoreTimeout](cocoaerror/persistentstoretimeout.md)
- [persistentStoreTimeoutError](cocoaerror/persistentstoretimeouterror.md) _(deprecated)_
- [persistentStoreTypeMismatch](cocoaerror/persistentstoretypemismatch.md)
- [persistentStoreTypeMismatchError](cocoaerror/persistentstoretypemismatcherror.md) _(deprecated)_
- [persistentStoreUnsupportedRequestType](cocoaerror/persistentstoreunsupportedrequesttype.md)
- [persistentStoreUnsupportedRequestTypeError](cocoaerror/persistentstoreunsupportedrequesttypeerror.md) _(deprecated)_
- [propertyListReadCorrupt](cocoaerror/propertylistreadcorrupt.md)
- [propertyListReadCorruptError](cocoaerror/propertylistreadcorrupterror.md) _(deprecated)_
- [propertyListReadStream](cocoaerror/propertylistreadstream.md)
- [propertyListReadStreamError](cocoaerror/propertylistreadstreamerror.md) _(deprecated)_
- [propertyListReadUnknownVersion](cocoaerror/propertylistreadunknownversion.md)
- [propertyListReadUnknownVersionError](cocoaerror/propertylistreadunknownversionerror.md) _(deprecated)_
- [propertyListWriteInvalid](cocoaerror/propertylistwriteinvalid.md)
- [propertyListWriteInvalidError](cocoaerror/propertylistwriteinvaliderror.md) _(deprecated)_
- [propertyListWriteStream](cocoaerror/propertylistwritestream.md)
- [propertyListWriteStreamError](cocoaerror/propertylistwritestreamerror.md) _(deprecated)_
- [serviceApplicationLaunchFailed](cocoaerror/serviceapplicationlaunchfailed.md)
- [serviceApplicationLaunchFailedError](cocoaerror/serviceapplicationlaunchfailederror-44r3b.md) _(deprecated)_
- [serviceApplicationNotFound](cocoaerror/serviceapplicationnotfound.md)
- [serviceApplicationNotFoundError](cocoaerror/serviceapplicationnotfounderror-2vdab.md) _(deprecated)_
- [serviceInvalidPasteboardData](cocoaerror/serviceinvalidpasteboarddata.md)
- [serviceInvalidPasteboardDataError](cocoaerror/serviceinvalidpasteboarddataerror-49mrz.md) _(deprecated)_
- [serviceMalformedServiceDictionary](cocoaerror/servicemalformedservicedictionary.md)
- [serviceMalformedServiceDictionaryError](cocoaerror/servicemalformedservicedictionaryerror-3wvlr.md) _(deprecated)_
- [serviceMiscellaneous](cocoaerror/servicemiscellaneous.md)
- [serviceMiscellaneousError](cocoaerror/servicemiscellaneouserror-18rwt.md) _(deprecated)_
- [serviceRequestTimedOut](cocoaerror/servicerequesttimedout.md)
- [serviceRequestTimedOutError](cocoaerror/servicerequesttimedouterror-30ucb.md) _(deprecated)_
- [sharingServiceNotConfigured](cocoaerror/sharingservicenotconfigured.md)
- [sharingServiceNotConfiguredError](cocoaerror/sharingservicenotconfigurederror-1xm1e.md) _(deprecated)_
- [sqlite](cocoaerror/sqlite.md)
- [sqliteError](cocoaerror/sqliteerror.md) _(deprecated)_
- [textReadInapplicableDocumentType](cocoaerror/textreadinapplicabledocumenttype.md)
- [textReadInapplicableDocumentTypeError](cocoaerror/textreadinapplicabledocumenttypeerror-5hv73.md) _(deprecated)_
- [textWriteInapplicableDocumentType](cocoaerror/textwriteinapplicabledocumenttype.md)
- [textWriteInapplicableDocumentTypeError](cocoaerror/textwriteinapplicabledocumenttypeerror-tfdf.md) _(deprecated)_
- [ubiquitousFileNotUploadedDueToQuota](cocoaerror/ubiquitousfilenotuploadedduetoquota.md)
- [ubiquitousFileNotUploadedDueToQuotaError](cocoaerror/ubiquitousfilenotuploadedduetoquotaerror.md) _(deprecated)_
- [ubiquitousFileUbiquityServerNotAvailable](cocoaerror/ubiquitousfileubiquityservernotavailable.md)
- [ubiquitousFileUnavailable](cocoaerror/ubiquitousfileunavailable.md)
- [ubiquitousFileUnavailableError](cocoaerror/ubiquitousfileunavailableerror.md) _(deprecated)_
- [userActivityConnectionUnavailable](cocoaerror/useractivityconnectionunavailable.md)
- [userActivityConnectionUnavailableError](cocoaerror/useractivityconnectionunavailableerror.md) _(deprecated)_
- [userActivityHandoffFailed](cocoaerror/useractivityhandofffailed.md)
- [userActivityHandoffFailedError](cocoaerror/useractivityhandofffailederror.md) _(deprecated)_
- [userActivityHandoffUserInfoTooLarge](cocoaerror/useractivityhandoffuserinfotoolarge.md)
- [userActivityHandoffUserInfoTooLargeError](cocoaerror/useractivityhandoffuserinfotoolargeerror.md) _(deprecated)_
- [userActivityRemoteApplicationTimedOut](cocoaerror/useractivityremoteapplicationtimedout.md)
- [userActivityRemoteApplicationTimedOutError](cocoaerror/useractivityremoteapplicationtimedouterror.md) _(deprecated)_
- [userCancelled](cocoaerror/usercancelled.md)
- [userCancelledError](cocoaerror/usercancellederror.md) _(deprecated)_
- [validationDateTooLate](cocoaerror/validationdatetoolate.md)
- [validationDateTooLateError](cocoaerror/validationdatetoolateerror.md) _(deprecated)_
- [validationDateTooSoon](cocoaerror/validationdatetoosoon.md)
- [validationDateTooSoonError](cocoaerror/validationdatetoosoonerror.md) _(deprecated)_
- [validationInvalidDate](cocoaerror/validationinvaliddate.md)
- [validationInvalidDateError](cocoaerror/validationinvaliddateerror.md) _(deprecated)_
- [validationMissingMandatoryProperty](cocoaerror/validationmissingmandatoryproperty.md)
- [validationMissingMandatoryPropertyError](cocoaerror/validationmissingmandatorypropertyerror.md) _(deprecated)_
- [validationMultipleErrors](cocoaerror/validationmultipleerrors.md)
- [validationMultipleErrorsError](cocoaerror/validationmultipleerrorserror.md) _(deprecated)_
- [validationNumberTooLarge](cocoaerror/validationnumbertoolarge.md)
- [validationNumberTooLargeError](cocoaerror/validationnumbertoolargeerror.md) _(deprecated)_
- [validationNumberTooSmall](cocoaerror/validationnumbertoosmall.md)
- [validationNumberTooSmallError](cocoaerror/validationnumbertoosmallerror.md) _(deprecated)_
- [validationRelationshipDeniedDelete](cocoaerror/validationrelationshipdenieddelete.md)
- [validationRelationshipDeniedDeleteError](cocoaerror/validationrelationshipdenieddeleteerror.md) _(deprecated)_
- [validationRelationshipExceedsMaximumCount](cocoaerror/validationrelationshipexceedsmaximumcount.md)
- [validationRelationshipExceedsMaximumCountError](cocoaerror/validationrelationshipexceedsmaximumcounterror.md) _(deprecated)_
- [validationRelationshipLacksMinimumCount](cocoaerror/validationrelationshiplacksminimumcount.md)
- [validationRelationshipLacksMinimumCountError](cocoaerror/validationrelationshiplacksminimumcounterror.md) _(deprecated)_
- [validationStringPatternMatching](cocoaerror/validationstringpatternmatching.md)
- [validationStringPatternMatchingError](cocoaerror/validationstringpatternmatchingerror.md) _(deprecated)_
- [validationStringTooLong](cocoaerror/validationstringtoolong.md)
- [validationStringTooLongError](cocoaerror/validationstringtoolongerror.md) _(deprecated)_
- [validationStringTooShort](cocoaerror/validationstringtooshort.md)
- [validationStringTooShortError](cocoaerror/validationstringtooshorterror.md) _(deprecated)_
- [xpcConnectionInterrupted](cocoaerror/xpcconnectioninterrupted.md)
- [xpcConnectionInvalid](cocoaerror/xpcconnectioninvalid.md)
- [xpcConnectionReplyInvalid](cocoaerror/xpcconnectionreplyinvalid.md)

### Type Methods

- [error(_:userInfo:url:)](<cocoaerror/error(__userinfo_url_).md>)

## See Also

### Error Codes

- [MachError](macherror.md) — Describes an error in the Mach error domain.
- [POSIXError](posixerror.md) — Describes an error in the POSIX error domain.
- [NSError Codes](1448136-nserror-codes.md) — Error codes in the Cocoa error domain.
