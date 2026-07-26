---
title: Loading and Caching Assets and Thumbnails
framework: Photos
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photokit/loading-and-caching-assets-and-thumbnails
source_url: 'https://developer.apple.com/documentation/photokit/loading-and-caching-assets-and-thumbnails'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photokit/loading-and-caching-assets-and-thumbnails.json'
content_hash: 'sha256:e9105273f727fe92'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotoKit](../photokit.md)

# Loading and Caching Assets and Thumbnails

<sub>Article</sub>

Request image, video, or Live Photos content, and cache for quick reuse.

## Overview

Photos automatically downloads or generates images to your specification, caching them for quick reuse. Use the [PHImageManager](../photos/phimagemanager.md) class to request images of assets at a specified size, or AVFoundation objects to work with video assets. When working with large numbers of assets—for example, when populating a collection view with thumbnails—preload images in batches using the [PHCachingImageManager](../photos/phcachingimagemanager.md) subclass.

## See Also

### Articles

- [Delivering an Enhanced Privacy Experience in Your Photos App](delivering-an-enhanced-privacy-experience-in-your-photos-app.md) — Adopt the latest privacy enhancements to deliver advanced user-privacy controls.
- [Fetching Objects and Requesting Changes](fetching-objects-and-requesting-changes.md) — Get assets, asset collections, and collection lists matching a specified query.
- [Displaying Live Photos](displaying-live-photos.md) — Provide the same interactive playback of Live Photos as in the iOS Photos app.
- [Creating Photo Editing Extensions](creating-photo-editing-extensions.md) — Provide custom functionality in the Photos app by bundling an app extension.
