---
title: PHPhotosError.Code.networkAccessRequired
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phphotoserror-swift.struct/code/networkaccessrequired
source_url: 'https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/code/networkaccessrequired'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotoserror-swift.struct/code/networkaccessrequired.json'
content_hash: 'sha256:f06aa5867796f0c2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Photos](../../../photos.md) · [PHPhotosError](../../phphotoserror-swift.struct.md) · [Code](../code.md)

# PHPhotosError.Code.networkAccessRequired

<sub>Case</sub>

An error that indicates the request for an asset resource fails because it requires network access.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case networkAccessRequired
```

## Discussion

Set [networkAccessAllowed](../../phassetresourcerequestoptions/isnetworkaccessallowed.md) to `true` to enable network access.

## See Also

### Error Codes

- [PHPhotosErrorAccessRestricted](accessrestricted.md) — An error that indicates the system configuration restricts access to the asset.
- [PHPhotosErrorAccessUserDenied](accessuserdenied.md) — An error that indicates the user denies access.
- [PHPhotosErrorChangeNotSupported](changenotsupported.md) — An error that indicates the system doesn’t support the change request configuration.
- [PHPhotosErrorIdentifierNotFound](identifiernotfound.md) — An error that indicates an identifier doesn’t exist.
- [PHPhotosErrorInternalError](internalerror.md) — An error that indicates an internal error occurs.
- [invalid](invalid.md) — An error that indicates the operation isn’t valid. _(deprecated)_
- [PHPhotosErrorInvalidResource](invalidresource.md) — An error that indicates the asset resource validation fails.
- [PHPhotosErrorLibraryVolumeOffline](libraryvolumeoffline.md) — An error that indicates the photo library isn’t available because the file system volume that stores it isn’t mounted.
- [PHPhotosErrorLibraryInFileProviderSyncRoot](libraryinfileprovidersyncroot.md) — An error that indicates the Photos library bundle is in a file provider sync directory, and the framework doesn’t support it.
- [PHPhotosErrorLimitExceeded](limitexceeded.md) — An error that indicates the request exceeds a limit.
- [PHPhotosErrorMissingResource](missingresource.md) — An error that indicates a missing asset resource.
- [PHPhotosErrorMultipleIdentifiersFound](multipleidentifiersfound.md) — An error that indicates that more than one identifier exists.
- [PHPhotosErrorNetworkError](networkerror.md) — An error that indicates the request for an asset resource fails because of a network connection error.
- [PHPhotosErrorNotEnoughSpace](notenoughspace.md) — An error that indicates there’s not enough space to perform the requested change.
- [PHPhotosErrorOperationInterrupted](operationinterrupted.md) — An error that indicates an interruption occurs and the operation can’t complete.
