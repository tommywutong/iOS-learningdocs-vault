---
title: 'unregisterChangeObserver(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/unregisterchangeobserver(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/unregisterchangeobserver(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/unregisterchangeobserver%28_%3A%29.json'
content_hash: 'sha256:5815bc4d6cf33ca8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# unregisterChangeObserver(_:)

<sub>Instance Method</sub>

Unregisters an object so that it no longer receives change messages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func unregisterChangeObserver(_ observer: any PHPhotoLibraryChangeObserver)
```

## Parameters

- `observer` — An object currently registered to receive change messages.

## See Also

### Observing Library Changes

- [Observing Changes in the Photo Library](../../photokit/observing-changes-in-the-photo-library.md) — Register an observer to be notified of changes to the photo library.
- [- registerChangeObserver:](<register(__)-6y3b9.md>) — Registers an object to receive messages when objects in the photo library change.
- [PHPhotoLibraryChangeObserver](../phphotolibrarychangeobserver.md) — A protocol to adopt to have the system notify your app of changes to the photo library.
- [PHChange](../phchange.md) — A description of a change that occurred in the photo library.
- [PHObjectChangeDetails](../phobjectchangedetails.md) — A description of changes that occurred in an asset or collection object.
- [PHFetchResultChangeDetails](../phfetchresultchangedetails.md) — A description of changes that occurred in the set of asset or collection objects listed in a fetch result.
