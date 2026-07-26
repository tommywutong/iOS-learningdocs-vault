---
title: PHLivePhoto
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephoto
source_url: 'https://developer.apple.com/documentation/photos/phlivephoto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephoto.json'
content_hash: 'sha256:7ff00d2d51a4d3f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHLivePhoto

<sub>Class</sub>

A displayable representation of a Live Photo—a picture that includes motion and sound from the moments just before and after its capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHLivePhoto
```

## Overview

In iOS and tvOS, you can use this class to reference Live Photos from the user’s library (fetched with the [PHAsset](phasset.md) and [PHImageManager](phimagemanager.md) classes), to load displayable Live Photo objects from data obtained elsewhere (such as pictures shared through a social network), and to assign Live Photos to [PHLivePhotoView](../photosui/phlivephotoview.md) objects for display.

In iOS, tvOS, and macOS, you can use this class to display edits in progress for Live Photo content in a photo editing extension.

> [!note] Note
> For guidance on how to integrate Live Photos with your app’s user experience, see [Live Photos](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/MobileHIG/LivePhotos.html#//apple_ref/doc/uid/TP40006556-CH74) in [iOS Human Interface Guidelines](https://developer.apple.com/ios/human-interface-guidelines/).

The [PHLivePhoto](phlivephoto.md) class serves in much the same role for Live Photos as the [UIImage](../uikit/uiimage.md) or [NSImage](../appkit/nsimage.md) class serves for static images. A [UIImage](../uikit/uiimage.md) or [NSImage](../appkit/nsimage.md) object represents not the data file an image is loaded from, but instead a ready-to-use image that can be displayed in a view—similarly, a [PHLivePhoto](phlivephoto.md) object represents a Live Photo ready to display with motion and sound using a [PHLivePhotoView](../photosui/phlivephotoview.md) object, not an entry in the Photos library or the data resources that constitute a Live Photo. (To work with Live Photos as elements of the Photos library, use the [PHAsset](phasset.md) class. To work with the data files that constitute a Live Photo, use the [PHAssetResource](phassetresource.md) class.)

> [!tip] Tip
> To display Live Photo content on the web, use the [LivePhotosKit JS](../livephotoskitjs.md) framework.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSItemProviderReading](../foundation/nsitemproviderreading.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Transferable](../coretransferable/transferable.md)

## Topics

### Inspecting a Live Photo

- [size](phlivephoto/size.md) — The size, in pixels, of the Live Photo.

### Loading a Live Photo from Data Files

- [+ requestLivePhotoWithResourceFileURLs:placeholderImage:targetSize:contentMode:resultHandler:](<phlivephoto/request(withresourcefileurls_placeholderimage_targetsize_contentmode_resulthandler_).md>) — Asynchronously loads a Live Photo from the specified resource files.
- [+ cancelLivePhotoRequestWithRequestID:](<phlivephoto/cancelrequest(withrequestid_).md>) — Cancels an asynchronous request

### Constants

- [PHLivePhotoRequestID](phlivephotorequestid.md) — A numeric identifier for an asynchronous Live Photo loading request.
- [Image Request Identifiers](../photokit/image-request-identifiers.md) — Special values for the Live Photo request ID that are returned by asynchronous requests.
- [Result Handler Info Dictionary Keys](../photokit/result-handler-info-dictionary-keys.md) — Info describing an attempt to load a Live Photo.

### Initializers

- [init(coder:)](<phlivephoto/init(coder_).md>)
