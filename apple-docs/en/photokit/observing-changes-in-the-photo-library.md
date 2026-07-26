---
title: Observing Changes in the Photo Library
framework: Photos
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photokit/observing-changes-in-the-photo-library
source_url: 'https://developer.apple.com/documentation/photokit/observing-changes-in-the-photo-library'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photokit/observing-changes-in-the-photo-library.json'
content_hash: 'sha256:2afe5769df6b24eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotoKit](../photokit.md) · [Photos](../photos.md) · [PHPhotoLibrary](../photos/phphotolibrary.md)

# Observing Changes in the Photo Library

<sub>Article</sub>

Register an observer to be notified of changes to the photo library.

## Overview

To be notified of changes to the photo library, use the [- registerChangeObserver:](<../photos/phphotolibrary/register(__)-6y3b9.md>) method to designate an observer object. Whenever you use a fetch method, such as [+ fetchAssetsWithOptions:](<../photos/phasset/fetchassets(with_).md>), to retrieve assets or collections, Photos automatically registers your interest in observing changes to those items. After you perform a fetch, Photos sends messages to your observer through the [PHPhotoLibraryChangeObserver](../photos/phphotolibrarychangeobserver.md) protocol whenever the items in the resulting fetch request change. For example, you’ll get notified when changes add items, remove items, or reorder the list of items in the fetch result. Update your user interface based on the details you receive from [PHChange](../photos/phchange.md) objects.

Use the shared [PHPhotoLibrary](../photos/phphotolibrary.md) object to register a change handler for the assets and collections you fetch. Photos tells your app whenever another app or device changes the content or metadata of an asset or the list of assets in a collection. [PHChange](../photos/phchange.md) objects provide information about object state before and after each change with semantics that make it easy to update a collection view or similar interface.

For information about handling changes, see the [PHPhotoLibraryChangeObserver](../photos/phphotolibrarychangeobserver.md) protocol.

## See Also

### Observing Library Changes

- [- registerChangeObserver:](<../photos/phphotolibrary/register(__)-6y3b9.md>) — Registers an object to receive messages when objects in the photo library change.
- [- unregisterChangeObserver:](<../photos/phphotolibrary/unregisterchangeobserver(__).md>) — Unregisters an object so that it no longer receives change messages.
- [PHPhotoLibraryChangeObserver](../photos/phphotolibrarychangeobserver.md) — A protocol to adopt to have the system notify your app of changes to the photo library.
- [PHChange](../photos/phchange.md) — A description of a change that occurred in the photo library.
- [PHObjectChangeDetails](../photos/phobjectchangedetails.md) — A description of changes that occurred in an asset or collection object.
- [PHFetchResultChangeDetails](../photos/phfetchresultchangedetails.md) — A description of changes that occurred in the set of asset or collection objects listed in a fetch result.
