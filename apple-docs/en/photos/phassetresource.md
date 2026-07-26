---
title: PHAssetResource
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresource
source_url: 'https://developer.apple.com/documentation/photos/phassetresource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresource.json'
content_hash: 'sha256:f85db6257f28f3f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetResource

<sub>Class</sub>

An underlying data resource associated with a photo, video, or Live Photo asset in the Photos library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHAssetResource
```

## Overview

Each [PHAsset](phasset.md) object references one or more resources. Use these objects to work with those resources directly, like when backing up or restoring assets.

- A photo asset can contain both JPEG and RAW files representing the same photo.
- A Live Photo asset contains both still photo and video resources.
- An edited asset contains resources representing asset content before and after the edit, as well as a resource corresponding to the [PHAdjustmentData](phadjustmentdata.md) object that describes the edit.

To work with the data contained in an asset resource, fetch it using the [PHAssetResourceManager](phassetresourcemanager.md) class.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Retrieving an Asset’s Data Resources

- [+ assetResourcesForAsset:](<phassetresource/assetresources(for_)-27o4l.md>) — Returns the list of data resources associated with an asset.
- [+ assetResourcesForLivePhoto:](<phassetresource/assetresources(for_)-2fedw.md>) — Returns the list of data resources associated with a Live Photo object.

### Inspecting an Asset Resource

- [type](phassetresource/type.md) — The relationship of an asset resource to its owning asset.
- [PHAssetResourceType](phassetresourcetype.md) — Describes the relationship of an asset resource to its owning asset.
- [contentType](phassetresource/contenttype.md) — The content type of the data associated with this asset resource (the data can be retrieved via `PHAssetResourceManager`)
- [assetLocalIdentifier](phassetresource/assetlocalidentifier.md) — The unique identifier the system associates for a local asset object.
- [uniformTypeIdentifier](phassetresource/uniformtypeidentifier.md) — The uniform type identifier for the asset resource’s image or video data. _(deprecated)_
- [originalFilename](phassetresource/originalfilename.md) — The original filename of the asset resource from when it was created or imported.
- [pixelHeight](phassetresource/pixelheight.md) — The height of the resource, in pixels.
- [pixelWidth](phassetresource/pixelwidth.md) — The width of the resource, in pixels.

### Instance Properties

- [dataSize](phassetresource/datasize-5lxva.md) — The size of the resource in bytes if known, `nil` if unavailable (may not be available until resource download/processing is complete)

### Type Methods

- [+ assetResourceForUploadJob:](<phassetresource/assetresource(foruploadjob_).md>) — Returns the asset resource associated with the given upload job. _(beta)_

## See Also

### Asset resource management

- [PHAssetCreationRequest](phassetcreationrequest.md) — A request to create a new Photos asset from underlying data resources, for use in a photo library change block.
- [PHAssetResourceCreationOptions](phassetresourcecreationoptions.md) — A set of options affecting the creation of a new Photos asset from underlying resources.
- [PHAssetResourceManager](phassetresourcemanager.md) — A resource manager for the data storage underlying a Photos asset.
- [PHAssetResourceRequestOptions](phassetresourcerequestoptions.md) — A set of options affecting the delivery of underlying asset data that you request from the asset resource manager.
