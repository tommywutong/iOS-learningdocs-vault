---
title: 'register(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phphotolibrary/register(_:)-6y3b9'
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary/register(_:)-6y3b9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary/register%28_%3A%29-6y3b9.json'
content_hash: 'sha256:34808dacf1418f5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHPhotoLibrary](../phphotolibrary.md)

# register(_:)

<sub>Instance Method</sub>

Registers an object to receive messages when objects in the photo library change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func register(_ observer: any PHPhotoLibraryChangeObserver)
```

## Parameters

- `observer` — An object for receiving change messages.

## Discussion

You implicitly declare interest in change messages whenever you use a fetch method (such as [+ fetchAssetsWithOptions:](<../phasset/fetchassets(with_).md>)) to retrieve assets or collections. After you perform a fetch, Photos automatically sends change messages whenever the objects in the resulting fetch request change—including when changes happen that add to, remove from, or reorder the list of objects in the fetch result.

## See Also

### Observing Library Changes

- [Observing Changes in the Photo Library](../../photokit/observing-changes-in-the-photo-library.md) — Register an observer to be notified of changes to the photo library.
- [- unregisterChangeObserver:](<unregisterchangeobserver(__).md>) — Unregisters an object so that it no longer receives change messages.
- [PHPhotoLibraryChangeObserver](../phphotolibrarychangeobserver.md) — A protocol to adopt to have the system notify your app of changes to the photo library.
- [PHChange](../phchange.md) — A description of a change that occurred in the photo library.
- [PHObjectChangeDetails](../phobjectchangedetails.md) — A description of changes that occurred in an asset or collection object.
- [PHFetchResultChangeDetails](../phfetchresultchangedetails.md) — A description of changes that occurred in the set of asset or collection objects listed in a fetch result.
