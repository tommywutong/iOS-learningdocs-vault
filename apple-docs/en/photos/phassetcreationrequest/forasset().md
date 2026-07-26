---
title: forAsset()
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetcreationrequest/forasset()
source_url: 'https://developer.apple.com/documentation/photos/phassetcreationrequest/forasset()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcreationrequest/forasset%28%29.json'
content_hash: 'sha256:2e1ac0db5e931532'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCreationRequest](../phassetcreationrequest.md)

# forAsset()

<sub>Type Method</sub>

Creates a request for adding a new asset to the Photos library using asset resources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func forAsset() -> Self
```

## Return Value

An asset creation request.

## Discussion

Call this method within a photo library change block to create a new asset. For details on change blocks, see [PHPhotoLibrary](../phphotolibrary.md). After calling this method, and before returning from the change block use the methods listed in Providing Data Resources for the New Asset to specify one or more data resources for the asset.

To set metadata properties of the newly created asset, use the corresponding properties of the change request (provided by the superclass [PHAssetChangeRequest](../phassetchangerequest.md) and listed in Modifying Assets). To reference the newly created asset later in the same change block or after the change block completes, use the [placeholderForCreatedAsset](../phassetchangerequest/placeholderforcreatedasset.md) property to retrieve a placeholder object.
