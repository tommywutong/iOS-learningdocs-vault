---
title: 'photoLibraryDidChange(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phphotolibrarychangeobserver/photolibrarydidchange(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrarychangeobserver/photolibrarydidchange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrarychangeobserver/photolibrarydidchange%28_%3A%29.json'
content_hash: 'sha256:65f5b475a5892aa7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibraryChangeObserver](../phphotolibrarychangeobserver.md)

# photoLibraryDidChange(_:)

<sub>Instance Method</sub>

Tells your observer that a set of changes has occurred in the Photos library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func photoLibraryDidChange(_ changeInstance: PHChange)
```

## Parameters

- `changeInstance` — An object representing the changes.

## Discussion

Use the provided [PHChange](../phchange.md) object to find out which, if any, of the albums or collections you’re interested in have changed and get detailed change information. Call the change object’s [changeDetailsForObject:](../phchange/changedetailsforobject_.md) method to get information about changes to an asset’s contents or metadata properties or about a collection’s metadata properties. Call the change object’s [changeDetails(for:)](<../phchange/changedetails(for_)-33a6n.md>) to get information about changes to a collection’s list of members (or to any other fetch result).

Photos calls this method on an arbitrary queue. If you need to update your app’s UI as a result of the change, dispatch to the main queue.
