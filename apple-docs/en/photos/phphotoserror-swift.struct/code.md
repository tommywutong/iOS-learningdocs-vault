---
title: PHPhotosError.Code
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phphotoserror-swift.struct/code
source_url: 'https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotoserror-swift.struct/code.json'
content_hash: 'sha256:ccea4ccfe637a9c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotosError](../phphotoserror-swift.struct.md)

# PHPhotosError.Code

<sub>Enumeration</sub>

Error codes for framework operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Error Codes

- [PHPhotosErrorAccessRestricted](code/accessrestricted.md) — An error that indicates the system configuration restricts access to the asset.
- [PHPhotosErrorAccessUserDenied](code/accessuserdenied.md) — An error that indicates the user denies access.
- [PHPhotosErrorChangeNotSupported](code/changenotsupported.md) — An error that indicates the system doesn’t support the change request configuration.
- [PHPhotosErrorIdentifierNotFound](code/identifiernotfound.md) — An error that indicates an identifier doesn’t exist.
- [PHPhotosErrorInternalError](code/internalerror.md) — An error that indicates an internal error occurs.
- [invalid](code/invalid.md) — An error that indicates the operation isn’t valid. _(deprecated)_
- [PHPhotosErrorInvalidResource](code/invalidresource.md) — An error that indicates the asset resource validation fails.
- [PHPhotosErrorLibraryVolumeOffline](code/libraryvolumeoffline.md) — An error that indicates the photo library isn’t available because the file system volume that stores it isn’t mounted.
- [PHPhotosErrorLibraryInFileProviderSyncRoot](code/libraryinfileprovidersyncroot.md) — An error that indicates the Photos library bundle is in a file provider sync directory, and the framework doesn’t support it.
- [PHPhotosErrorLimitExceeded](code/limitexceeded.md) — An error that indicates the request exceeds a limit.
- [PHPhotosErrorMissingResource](code/missingresource.md) — An error that indicates a missing asset resource.
- [PHPhotosErrorMultipleIdentifiersFound](code/multipleidentifiersfound.md) — An error that indicates that more than one identifier exists.
- [PHPhotosErrorNetworkAccessRequired](code/networkaccessrequired.md) — An error that indicates the request for an asset resource fails because it requires network access.
- [PHPhotosErrorNetworkError](code/networkerror.md) — An error that indicates the request for an asset resource fails because of a network connection error.
- [PHPhotosErrorNotEnoughSpace](code/notenoughspace.md) — An error that indicates there’s not enough space to perform the requested change.
- [PHPhotosErrorOperationInterrupted](code/operationinterrupted.md) — An error that indicates an interruption occurs and the operation can’t complete.
- [PHPhotosErrorPersistentChangeDetailsUnavailable](code/persistentchangedetailsunavailable.md) — An error that indicates the change details aren’t available for the persistent change.
- [PHPhotosErrorPersistentChangeTokenExpired](code/persistentchangetokenexpired.md) — An error that indicates the library state is older than the available history of persistent changes.
- [PHPhotosErrorRelinquishingLibraryBundleToWriter](code/relinquishinglibrarybundletowriter.md) — An error that indicates the photo library isn’t available because the user moves, renames, or deletes the system’s photo library.
- [PHPhotosErrorRequestNotSupportedForAsset](code/requestnotsupportedforasset.md) — An error that indicates the system doesn’t support the request for the specified asset.
- [PHPhotosErrorSwitchingSystemPhotoLibrary](code/switchingsystemphotolibrary.md) — An error that indicates the photo library isn’t available because the user switches the system’s photo library.
- [PHPhotosErrorUserCancelled](code/usercancelled.md) — An error that indicates the user cancels the asset retrieval or editing request.

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Inspecting an Error

- [errorDomain](errordomain.md)
- [Error Constants](../../photokit/error-constants.md) — Error code constants for framework operations.
- [PHLocalIdentifiersErrorKey](../phlocalidentifierserrorkey.md) — An error key that retrieves an array of string values representing local identifiers matched to a cloud identifier.
