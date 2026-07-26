---
title: PHAssetResourceCreationOptions
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourcecreationoptions
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcecreationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcecreationoptions.json'
content_hash: 'sha256:f7e72b9668b4d7f1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetResourceCreationOptions

<sub>Class</sub>

A set of options affecting the creation of a new Photos asset from underlying resources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHAssetResourceCreationOptions
```

## Overview

You use this class when creating an asset for addition to the Photos library with a [PHAssetCreationRequest](phassetcreationrequest.md) object.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Describing a New Asset Resource

- [originalFilename](phassetresourcecreationoptions/originalfilename.md) — The filename for the asset resource being created.
- [uniformTypeIdentifier](phassetresourcecreationoptions/uniformtypeidentifier.md) — The uniform type identifier for the resource. _(deprecated)_
- [contentType](phassetresourcecreationoptions/contenttype.md) — The type of data being provided for this asset resource. If not specified, one will be inferred from the PHAssetResourceType or file URL extension (if provided).

### Managing Resource Files

- [shouldMoveFile](phassetresourcecreationoptions/shouldmovefile.md) — A Boolean value that determines whether Photos moves or duplicates files when creating an asset resource.

## See Also

### Asset resource management

- [PHAssetResource](phassetresource.md) — An underlying data resource associated with a photo, video, or Live Photo asset in the Photos library.
- [PHAssetCreationRequest](phassetcreationrequest.md) — A request to create a new Photos asset from underlying data resources, for use in a photo library change block.
- [PHAssetResourceManager](phassetresourcemanager.md) — A resource manager for the data storage underlying a Photos asset.
- [PHAssetResourceRequestOptions](phassetresourcerequestoptions.md) — A set of options affecting the delivery of underlying asset data that you request from the asset resource manager.
