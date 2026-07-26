---
title: assetContentChanged
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phobjectchangedetails/assetcontentchanged
source_url: 'https://developer.apple.com/documentation/photos/phobjectchangedetails/assetcontentchanged'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phobjectchangedetails/assetcontentchanged.json'
content_hash: 'sha256:bb8d7ee160c25006'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHObjectChangeDetails](../phobjectchangedetails.md)

# assetContentChanged

<sub>Instance Property</sub>

A Boolean value that indicates whether the asset’s photo or video content has changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var assetContentChanged: Bool { get }
```

## Discussion

If this value `true`, you can use the [PHImageManager](../phimagemanager.md) class to retrieve updated content.

This value is `false` if the asset has not changed or if the change details do not refer to a [PHAsset](../phasset.md) object.

## See Also

### Getting Change Information

- [objectWasDeleted](objectwasdeleted.md) — A Boolean value that indicates whether the object has been deleted from the Photos library.
