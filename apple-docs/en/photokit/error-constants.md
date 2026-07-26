---
title: Error Constants
framework: Photos
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photokit/error-constants
source_url: 'https://developer.apple.com/documentation/photokit/error-constants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photokit/error-constants.json'
content_hash: 'sha256:2e7d9a0287ca6490'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotoKit](../photokit.md) · [Photos](../photos.md) · [PHPhotosError](../photos/phphotoserror-swift.struct.md)

# Error Constants

<sub>API Collection</sub>

Error code constants for framework operations.

## Topics

### Constants

- [accessRestricted](../photos/phphotoserror-swift.struct/accessrestricted.md) — An error that indicates the system configuration restricts access to the asset.
- [accessUserDenied](../photos/phphotoserror-swift.struct/accessuserdenied.md) — An error that indicates the user denied access.
- [changeNotSupported](../photos/phphotoserror-swift.struct/changenotsupported.md) — An error that indicates the system doesn’t support the change request configuration.
- [identifierNotFound](../photos/phphotoserror-swift.struct/identifiernotfound.md) — An error that indicates an identifier doesn’t exist.
- [internalError](../photos/phphotoserror-swift.struct/internalerror.md) — An error that indicates an internal error occurs.
- [invalidResource](../photos/phphotoserror-swift.struct/invalidresource.md) — An error that indicates the asset resource validation failed.
- [libraryVolumeOffline](../photos/phphotoserror-swift.struct/libraryvolumeoffline.md) — An error that indicates the photo library isn’t available because the file system volume that stores it isn’t mounted.
- [libraryInFileProviderSyncRoot](../photos/phphotoserror-swift.struct/libraryinfileprovidersyncroot.md) — An error that indicates the Photos library bundle is in a file provider sync directory, and the framework doesn’t support it.
- [limitExceeded](../photos/phphotoserror-swift.struct/limitexceeded.md) — An error that indicates the request exceeds a limit.
- [missingResource](../photos/phphotoserror-swift.struct/missingresource.md) — An error that indicates a missing asset resource.
- [multipleIdentifiersFound](../photos/phphotoserror-swift.struct/multipleidentifiersfound.md) — An error that indicates that more than one identifier exists.
- [networkAccessRequired](../photos/phphotoserror-swift.struct/networkaccessrequired.md) — An error that indicates the request for an asset resource failed because it requires network access.
- [networkError](../photos/phphotoserror-swift.struct/networkerror.md) — An error that indicates the request for an asset resource fails because of a network connection error.
- [notEnoughSpace](../photos/phphotoserror-swift.struct/notenoughspace.md) — An error that indicates insufficient space to perform the change.
- [operationInterrupted](../photos/phphotoserror-swift.struct/operationinterrupted.md) — An error that indicates an interruption occurs and the operation can’t complete.
- [persistentChangeDetailsUnavailable](../photos/phphotoserror-swift.struct/persistentchangedetailsunavailable.md) — An error that indicates the change details aren’t available for the persistent change.
- [persistentChangeTokenExpired](../photos/phphotoserror-swift.struct/persistentchangetokenexpired.md) — An error that indicates the library state is older than the available history of persistent changes.
- [relinquishingLibraryBundleToWriter](../photos/phphotoserror-swift.struct/relinquishinglibrarybundletowriter.md) — An error that indicates the photo library isn’t available because the user moves, renames, or deletes the system’s photo library.
- [requestNotSupportedForAsset](../photos/phphotoserror-swift.struct/requestnotsupportedforasset.md) — An error that indicates the system doesn’t support the request for the asset.
- [switchingSystemPhotoLibrary](../photos/phphotoserror-swift.struct/switchingsystemphotolibrary.md) — An error that indicates the photo library isn’t available because the user switched the system’s photo library.
- [userCancelled](../photos/phphotoserror-swift.struct/usercancelled.md) — An error that indicates the user cancels the asset retrieval or editing request.
- [invalid](../photos/phphotoserror-swift.struct/code/invalid.md) — An error that indicates the operation isn’t valid. _(deprecated)_

## See Also

### Inspecting an Error

- [errorDomain](../photos/phphotoserror-swift.struct/errordomain.md)
- [Code](../photos/phphotoserror-swift.struct/code.md) — Error codes for framework operations.
- [PHLocalIdentifiersErrorKey](../photos/phlocalidentifierserrorkey.md) — An error key that retrieves an array of string values representing local identifiers matched to a cloud identifier.
