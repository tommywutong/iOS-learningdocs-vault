---
title: SwiftDataError
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/swiftdataerror
source_url: 'https://developer.apple.com/documentation/swiftdata/swiftdataerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/swiftdataerror.json'
content_hash: 'sha256:1e5713d7a6321b79'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# SwiftDataError

<sub>Structure</sub>

A type that describes a SwiftData error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SwiftDataError
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Fetch errors

- [includePendingChangesWithBatchSize](swiftdataerror/includependingchangeswithbatchsize.md)
- [sortingPendingChangesWithIdentifiers](swiftdataerror/sortingpendingchangeswithidentifiers.md)
- [unsupportedKeyPath](swiftdataerror/unsupportedkeypath.md)
- [unsupportedPredicate](swiftdataerror/unsupportedpredicate.md)
- [unsupportedSortDescriptor](swiftdataerror/unsupportedsortdescriptor.md)
- [historyTokenExpired](swiftdataerror/historytokenexpired.md)
- [invalidTransactionFetchRequest](swiftdataerror/invalidtransactionfetchrequest.md)

### Configuration errors

- [configurationFileNameContainsInvalidCharacters](swiftdataerror/configurationfilenamecontainsinvalidcharacters.md)
- [configurationFileNameTooLong](swiftdataerror/configurationfilenametoolong.md)
- [configurationSchemaNotFoundInContainerSchema](swiftdataerror/configurationschemanotfoundincontainerschema.md)
- [duplicateConfiguration](swiftdataerror/duplicateconfiguration.md)

### Container errors

- [loadIssueModelContainer](swiftdataerror/loadissuemodelcontainer.md)

### Context errors

- [modelValidationFailure](swiftdataerror/modelvalidationfailure.md)
- [missingModelContext](swiftdataerror/missingmodelcontext.md)

### Migration errors

- [backwardMigration](swiftdataerror/backwardmigration.md)
- [unknownSchema](swiftdataerror/unknownschema.md)

### Schema errors

- [unknownDataStoreSchema](swiftdataerror/unknowndatastoreschema.md) — An error that indicates the data store’s schema is not recognized.

### Operators

- [~=(_:_:)](<swiftdataerror/~=(____).md>)

## See Also

### Errors

- [DataStoreError](datastoreerror.md) — A type that describes a data store error.
