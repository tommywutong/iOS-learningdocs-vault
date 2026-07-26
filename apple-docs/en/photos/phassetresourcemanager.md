---
title: PHAssetResourceManager
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourcemanager
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcemanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcemanager.json'
content_hash: 'sha256:0f8d19cb49e99909'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetResourceManager

<sub>Class</sub>

A resource manager for the data storage underlying a Photos asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHAssetResourceManager
```

## Overview

An asset can have multiple underlying data resources—for example, both original and edited versions—each of which is represented by a [PHAssetResource](phassetresource.md) object. Unlike the [PHImageManager](phimagemanager.md) class, which provides and caches the primary representations of assets as thumbnails, image objects, or video objects, the asset resource manager provides direct access to these underlying data resources.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the Asset Resource Manager

- [+ defaultManager](<phassetresourcemanager/default().md>) — Returns the shared asset resource manager object.

### Requesting Resources

- [- requestDataForAssetResource:options:dataReceivedHandler:completionHandler:](<phassetresourcemanager/requestdata(for_options_datareceivedhandler_completionhandler_).md>) — Requests the underlying data for the specified asset resource, to be delivered asynchronously.
- [- cancelDataRequest:](<phassetresourcemanager/canceldatarequest(__).md>) — Cancels an asynchronous request.
- [- writeDataForAssetResource:toFile:options:completionHandler:](<phassetresourcemanager/writedata(for_tofile_options_completionhandler_).md>) — Requests the underlying data for the specified asset resource, to be asynchronously written to a local file.

### Constants

- [PHAssetResourceDataRequestID](phassetresourcedatarequestid.md) — A numeric identifier for an asynchronous asset resource loading request.
- [Resource Loading Request Identifiers](../photokit/resource-loading-request-identifiers.md) — Special values for the [PHAssetResourceDataRequestID](phassetresourcedatarequestid.md) identifier that are returned by asynchronous requests.

### Instance Methods

- [exportedAssetID(for:)](<phassetresourcemanager/exportedassetid(for_).md>) — Returns the exported asset ID for the specified asset resource.

## See Also

### Asset resource management

- [PHAssetResource](phassetresource.md) — An underlying data resource associated with a photo, video, or Live Photo asset in the Photos library.
- [PHAssetCreationRequest](phassetcreationrequest.md) — A request to create a new Photos asset from underlying data resources, for use in a photo library change block.
- [PHAssetResourceCreationOptions](phassetresourcecreationoptions.md) — A set of options affecting the creation of a new Photos asset from underlying resources.
- [PHAssetResourceRequestOptions](phassetresourcerequestoptions.md) — A set of options affecting the delivery of underlying asset data that you request from the asset resource manager.
