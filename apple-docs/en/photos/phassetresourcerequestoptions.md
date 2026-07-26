---
title: PHAssetResourceRequestOptions
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourcerequestoptions
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcerequestoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcerequestoptions.json'
content_hash: 'sha256:b39e811e726d18c1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetResourceRequestOptions

<sub>Class</sub>

A set of options affecting the delivery of underlying asset data that you request from the asset resource manager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHAssetResourceRequestOptions
```

## Overview

You use this class when requesting the underlying data for photo, video, and Live Photo asset resources from a [PHAssetResourceManager](phassetresourcemanager.md) object.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Fetching Resource Data from iCloud

- [networkAccessAllowed](phassetresourcerequestoptions/isnetworkaccessallowed.md) — A Boolean value that specifies whether Photos can download the requested asset resource data from iCloud.
- [progressHandler](phassetresourcerequestoptions/progresshandler.md) — A block that Photos calls periodically while downloading the asset resource data.
- [PHAssetResourceProgressHandler](phassetresourceprogresshandler.md) — The signature for a block that Photos calls while downloading asset resource data from iCloud. Used by the [progressHandler](phassetresourcerequestoptions/progresshandler.md) property.

## See Also

### Asset resource management

- [PHAssetResource](phassetresource.md) — An underlying data resource associated with a photo, video, or Live Photo asset in the Photos library.
- [PHAssetCreationRequest](phassetcreationrequest.md) — A request to create a new Photos asset from underlying data resources, for use in a photo library change block.
- [PHAssetResourceCreationOptions](phassetresourcecreationoptions.md) — A set of options affecting the creation of a new Photos asset from underlying resources.
- [PHAssetResourceManager](phassetresourcemanager.md) — A resource manager for the data storage underlying a Photos asset.
