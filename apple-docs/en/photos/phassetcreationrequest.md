---
title: PHAssetCreationRequest
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetcreationrequest
source_url: 'https://developer.apple.com/documentation/photos/phassetcreationrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcreationrequest.json'
content_hash: 'sha256:60dbd403b1407bbb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetCreationRequest

<sub>Class</sub>

A request to create a new Photos asset from underlying data resources, for use in a photo library change block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHAssetCreationRequest
```

## Overview

A [PHAssetCreationRequest](phassetcreationrequest.md) object, used within a photo library change block, constructs a new photo or video asset from data resources, and adds it to the Photos library. This class works in terms of the raw data resources that together form an asset, so you can use it together with the [PHAssetResource](phassetresource.md) class to perform a complete copy (or backup and restore) of an asset’s underlying resources. To instead simply create a new asset from an image object, image file, or video file, see the superclass [PHAssetChangeRequest](phassetchangerequest.md).

To create a new asset from data resources, first start a change block using the shared [PHPhotoLibrary](phphotolibrary.md) method [- performChanges:completionHandler:](<phphotolibrary/performchanges(__completionhandler_).md>) or [- performChangesAndWait:error:](<phphotolibrary/performchangesandwait(__).md>). Then, within the change block:

1. Within the change block, create a new asset creation request with the [+ creationRequestForAsset](<phassetcreationrequest/forasset().md>) method.
2. Add image, video, or data resources using the methods in the Providing Data Resources for the New Asset section below.
3. (Optional.) Set metadata for the new asset using methods and properties of the superclass [PHAssetChangeRequest](phassetchangerequest.md).

After Photos runs the change block and calls your completion handler, the new asset is created in the Photos library.

If you instantiate or use this class outside a photo library change block, Photos throws an exception. For details on change blocks, see [PHPhotoLibrary](phphotolibrary.md).

## Relationships

- **Inherits From**: [PHAssetChangeRequest](phassetchangerequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Requesting Asset Creation

- [+ creationRequestForAsset](<phassetcreationrequest/forasset().md>) — Creates a request for adding a new asset to the Photos library using asset resources.

### Preflighting a Request

- [+ supportsAssetResourceTypes:](<phassetcreationrequest/supportsassetresourcetypes(__).md>) — Returns a Boolean value indicating whether Photos supports creating an asset with the specified combination of resource types.

### Providing Data Resources for the New Asset

- [- addResourceWithType:data:options:](<phassetcreationrequest/addresource(with_data_options_).md>) — Adds a data resource to the asset being created, using the specified data.
- [- addResourceWithType:fileURL:options:](<phassetcreationrequest/addresource(with_fileurl_options_).md>) — Adds a data resource to the asset being created, using the file at the specified URL.

### Instance Properties

- [originalResourceChoice](phassetcreationrequest/originalresourcechoice.md) — The original resource to use as the unadjusted base for rendering derivatives of the new asset. _(beta)_

## See Also

### Asset resource management

- [PHAssetResource](phassetresource.md) — An underlying data resource associated with a photo, video, or Live Photo asset in the Photos library.
- [PHAssetResourceCreationOptions](phassetresourcecreationoptions.md) — A set of options affecting the creation of a new Photos asset from underlying resources.
- [PHAssetResourceManager](phassetresourcemanager.md) — A resource manager for the data storage underlying a Photos asset.
- [PHAssetResourceRequestOptions](phassetresourcerequestoptions.md) — A set of options affecting the delivery of underlying asset data that you request from the asset resource manager.
