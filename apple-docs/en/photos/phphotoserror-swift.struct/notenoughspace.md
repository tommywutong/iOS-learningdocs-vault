---
title: notEnoughSpace
framework: Photos
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phphotoserror-swift.struct/notenoughspace
source_url: 'https://developer.apple.com/documentation/photos/phphotoserror-swift.struct/notenoughspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotoserror-swift.struct/notenoughspace.json'
content_hash: 'sha256:4d8b66f1ef8b1e07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotosError](../phphotoserror-swift.struct.md)

# notEnoughSpace

<sub>Type Property</sub>

An error that indicates insufficient space to perform the change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var notEnoughSpace: PHPhotosError.Code { get }
```

## See Also

### Constants

- [accessRestricted](accessrestricted.md) — An error that indicates the system configuration restricts access to the asset.
- [accessUserDenied](accessuserdenied.md) — An error that indicates the user denied access.
- [changeNotSupported](changenotsupported.md) — An error that indicates the system doesn’t support the change request configuration.
- [identifierNotFound](identifiernotfound.md) — An error that indicates an identifier doesn’t exist.
- [internalError](internalerror.md) — An error that indicates an internal error occurs.
- [invalidResource](invalidresource.md) — An error that indicates the asset resource validation failed.
- [libraryVolumeOffline](libraryvolumeoffline.md) — An error that indicates the photo library isn’t available because the file system volume that stores it isn’t mounted.
- [libraryInFileProviderSyncRoot](libraryinfileprovidersyncroot.md) — An error that indicates the Photos library bundle is in a file provider sync directory, and the framework doesn’t support it.
- [limitExceeded](limitexceeded.md) — An error that indicates the request exceeds a limit.
- [missingResource](missingresource.md) — An error that indicates a missing asset resource.
- [multipleIdentifiersFound](multipleidentifiersfound.md) — An error that indicates that more than one identifier exists.
- [networkAccessRequired](networkaccessrequired.md) — An error that indicates the request for an asset resource failed because it requires network access.
- [networkError](networkerror.md) — An error that indicates the request for an asset resource fails because of a network connection error.
- [operationInterrupted](operationinterrupted.md) — An error that indicates an interruption occurs and the operation can’t complete.
- [persistentChangeDetailsUnavailable](persistentchangedetailsunavailable.md) — An error that indicates the change details aren’t available for the persistent change.
