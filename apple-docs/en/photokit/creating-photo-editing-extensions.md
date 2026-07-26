---
title: Creating Photo Editing Extensions
framework: PhotosUI
symbol_kind: article
role: article
role_heading: Article
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.11+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photokit/creating-photo-editing-extensions
source_url: 'https://developer.apple.com/documentation/photokit/creating-photo-editing-extensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photokit/creating-photo-editing-extensions.json'
content_hash: 'sha256:5089e4b0cf5b4268'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotoKit](../photokit.md)

# Creating Photo Editing Extensions

<sub>Article</sub>

Provide custom functionality in the Photos app by bundling an app extension.

## Overview

You can incorporate your app’s features directly into the Photos app in iOS or macOS by building an app extension. A photo-editing app extension can enable people to edit media, apply your app’s filter effects, build slideshows, books, or custom content, such as a collage,  right in Photos app using code that you supply.

## Implement and bundle the app extension

Adopt the [PHContentEditingController](../photosui/phcontenteditingcontroller.md) protocol to create an app extension that adds to the photo editing options and capabilities in the Photos app. Creating such an extension also requires using the following classes from the Photos framework:

- [PHContentEditingInput](../photos/phcontenteditinginput.md)—To reference the photo or video to be edited
- [PHContentEditingOutput](../photos/phcontenteditingoutput.md)—To save the results of an edit
- [PHAdjustmentData](../photos/phadjustmentdata.md)—To describe an edit operation

Include the app extension in your app bundle and the system installs it in Photos at the same time someone installs your app.

> [!note] Note
> If your app runs on a platform other than those listed above, the platform ignores your app extension.

## See Also

### Articles

- [Delivering an Enhanced Privacy Experience in Your Photos App](delivering-an-enhanced-privacy-experience-in-your-photos-app.md) — Adopt the latest privacy enhancements to deliver advanced user-privacy controls.
- [Fetching Objects and Requesting Changes](fetching-objects-and-requesting-changes.md) — Get assets, asset collections, and collection lists matching a specified query.
- [Loading and Caching Assets and Thumbnails](loading-and-caching-assets-and-thumbnails.md) — Request image, video, or Live Photos content, and cache for quick reuse.
- [Displaying Live Photos](displaying-live-photos.md) — Provide the same interactive playback of Live Photos as in the iOS Photos app.
