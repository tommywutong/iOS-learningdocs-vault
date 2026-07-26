---
title: Displaying Live Photos
framework: PhotosUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photokit/displaying-live-photos
source_url: 'https://developer.apple.com/documentation/photokit/displaying-live-photos'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photokit/displaying-live-photos.json'
content_hash: 'sha256:afd4fe044b30ffc2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotoKit](../photokit.md)

# Displaying Live Photos

<sub>Article</sub>

Provide the same interactive playback of Live Photos as in the iOS Photos app.

## Overview

The [PHLivePhotoView](../photosui/phlivephotoview.md) class provides a way to display Live Photos—pictures, taken on compatible hardware, that include motion and sound from the moments just before and after their capture. A Live Photo view provides the same interactive playback features found in the Photos app.

In iOS and tvOS, you can fetch Live Photo objects to display in a Live Photo view with the [PHLivePhoto](../photos/phlivephoto.md) class in the Photos framework. In macOS, the [PHLivePhoto](../photos/phlivephoto.md) class provides access to Live Photos being edited in a photo editing extension for the Photos app.

To display Live Photo content on the web, use the [LivePhotosKit JS](../livephotoskitjs.md) framework.

### Control Live Photo Playback

After obtaining a [PHLivePhoto](../photos/phlivephoto.md) object, use a Live Photo view to display the photo and control playback of its motion and sound content. In iOS and tvOS, you can obtain Live Photos from the user’s photo library using the [UIImagePickerController](../uikit/uiimagepickercontroller.md), [PHAsset](../photos/phasset.md), and [PHImageManager](../photos/phimagemanager.md) classes, or by creating one from asset resources exported from a photo library. In macOS, Live Photos are available only when editing Live Photo content in a photo editing extension that runs in the Photos app—see the [PHContentEditingInput](../photos/phcontenteditinginput.md) class to access Live Photos in an editing session.

> [!note] Note
> For guidance on how to integrate Live Photos with your app’s user experience, see [Live Photos](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/MobileHIG/LivePhotos.html#//apple_ref/doc/uid/TP40006556-CH74) in [iOS Human Interface Guidelines](https://developer.apple.com/ios/human-interface-guidelines/).

By default, a Live Photo view uses its own gesture recognizer to allow the user to play the motion and sound content of a Live Photo with the same interactions and visual effects seen in the Photos app. To customize this gesture recognizer—for example, to install it on a different view for proper event handling in your app’s view hierarchy—use the [playbackGestureRecognizer](../photosui/phlivephotoview/playbackgesturerecognizer.md) property.

Typically, an app doesn’t need to directly control Live Photo playback. In some situations, however, it can be useful to briefly animate the view to indicate to the user that a picture is a Live Photo. To do this, use the [- startPlaybackWithStyle:](<../photosui/phlivephotoview/startplayback(with_).md>) method with the [PHLivePhotoViewPlaybackStyleHint](../photosui/phlivephotoviewplaybackstyle/hint.md) option.

## See Also

### Articles

- [Delivering an Enhanced Privacy Experience in Your Photos App](delivering-an-enhanced-privacy-experience-in-your-photos-app.md) — Adopt the latest privacy enhancements to deliver advanced user-privacy controls.
- [Fetching Objects and Requesting Changes](fetching-objects-and-requesting-changes.md) — Get assets, asset collections, and collection lists matching a specified query.
- [Loading and Caching Assets and Thumbnails](loading-and-caching-assets-and-thumbnails.md) — Request image, video, or Live Photos content, and cache for quick reuse.
- [Creating Photo Editing Extensions](creating-photo-editing-extensions.md) — Provide custom functionality in the Photos app by bundling an app extension.
