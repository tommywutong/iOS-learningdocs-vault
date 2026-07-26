---
title: PHContentEditingInput
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditinginput
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginput.json'
content_hash: 'sha256:96973672170f414a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHContentEditingInput

<sub>Class</sub>

A container that provides information about and access to the image, video, or Live Photo content of an asset to be edited.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHContentEditingInput
```

## Overview

To edit an asset’s photo or video content:

1. Fetch a [PHAsset](phasset.md) object that represents the photo or video to be edited.
2. Call the asset’s [- requestContentEditingInputWithOptions:completionHandler:](<phasset/requestcontenteditinginput(with_completionhandler_).md>) method to retrieve a [PHContentEditingInput](phcontenteditinginput.md) object.
3. Apply your edits to the asset. To allow a user to continue working with the edit later (for example, to adjust the parameters of a photo filter), create a [PHAdjustmentData](phadjustmentdata.md) object describing the changes.
4. Initialize a [PHContentEditingOutput](phcontenteditingoutput.md) object. For photo- or video-only assets, use the editing output’s properties to provide edited asset data. For Live Photo assets, create a [PHLivePhotoEditingContext](phlivephotoeditingcontext.md) object to edit the Live Photo content.
5. Use a photo library change block to commit the edit. In the block, create a [PHAssetChangeRequest](phassetchangerequest.md) object and set its [contentEditingOutput](phassetchangerequest/contenteditingoutput.md) property to the editing output that you created. For more details, see [PHPhotoLibrary](phphotolibrary.md).

You can also edit assets from photo editing extensions. In this case, instead of working with a [PHAsset](phasset.md) object, you implement methods in the [PHContentEditingController](../photosui/phcontenteditingcontroller.md) protocol. Photos provides a [PHContentEditingInput](phcontenteditinginput.md) object when your extension begins editing. When editing is complete, Photos requests a [PHContentEditingOutput](phcontenteditingoutput.md) object that contains the edited asset content.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting Information About the Asset

- [mediaType](phcontenteditinginput/mediatype.md) — The type of the asset, such as video or audio.
- [PHAssetMediaType](phassetmediatype.md) — Identifies the general type of an asset, such as image or video.
- [mediaSubtypes](phcontenteditinginput/mediasubtypes.md) — The subtypes of the asset, identifying special kinds of assets such as a panoramic photo or a high-frame-rate video.
- [PHAssetMediaSubtype](phassetmediasubtype.md) — Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video.
- [creationDate](phcontenteditinginput/creationdate.md) — The date and time when the asset was originally created.
- [location](phcontenteditinginput/location.md) — The location information that was saved with the asset.
- [uniformTypeIdentifier](phcontenteditinginput/uniformtypeidentifier.md) — The uniform type identifier for the asset’s image or video data. _(deprecated)_

### Working with Previous Edits

- [adjustmentData](phcontenteditinginput/adjustmentdata.md) — An object that describes the most recent edit to the asset’s content.

### Working with Photo Assets

- [displaySizeImage](phcontenteditinginput/displaysizeimage.md) — An image of the asset’s contents, appropriately sized for display.
- [fullSizeImageOrientation](phcontenteditinginput/fullsizeimageorientation.md) — The Exif display orientation of the full-size image file.
- [fullSizeImageURL](phcontenteditinginput/fullsizeimageurl.md) — The URL to a file that contains the full-sized image data.

### Working with Video Assets

- [audiovisualAsset](phcontenteditinginput/audiovisualasset.md) — The video asset, as an `AVAsset` object.
- [avAsset](phcontenteditinginput/avasset.md) — The video asset, as an `AVAsset` object. _(deprecated)_

### Working with Live Photo Assets

- [livePhoto](phcontenteditinginput/livephoto.md) — The unedited Live Photo content of the editing input.
- [playbackStyle](phcontenteditinginput/playbackstyle.md) — The style in which to present this content to the user.
- [PlaybackStyle](phasset/playbackstyle-swift.enum.md) — An enumeration of asset playback styles that dictate how to present an asset to the user.

### Instance Properties

- [contentType](phcontenteditinginput/contenttype.md) — The type of data provided as the asset’s content editing input image or video.

## See Also

### Editing an Asset

- [Editing Asset Content](../photokit/editing-asset-content.md) — Make a request to modify and save a photo or video asset.
- [PHContentEditingOutput](phcontenteditingoutput.md) — A container to which you provide the results of editing the photo, video, or Live Photo content of a Photos asset.
- [PHAdjustmentData](phadjustmentdata.md) — A description of the edits made to an asset’s photo, video, or Live Photo content, which allows your app to reconstruct or revert the effects of prior editing sessions.
- [PHContentEditingInputRequestOptions](phcontenteditinginputrequestoptions.md) — A set of options affecting the delivery of image or video data when you request to edit the content of a Photos asset.
- [PHLivePhotoEditingContext](phlivephotoeditingcontext.md) — An editing session for modifying the photo, video, and audio content of a Live Photo.
- [PHLivePhotoFrame](phlivephotoframe.md) — A container that provides image content for a single frame of a Live Photo in an editing context.
- [- canPerformEditOperation:](<phasset/canperform(__).md>) — Returns whether the asset supports the specified editing operation.
- [PHAssetEditOperation](phasseteditoperation.md) — Values identifying possible actions an asset can support, used by the [- canPerformEditOperation:](<phasset/canperform(__).md>) method.
- [- requestContentEditingInputWithOptions:completionHandler:](<phasset/requestcontenteditinginput(with_completionhandler_).md>) — Requests asset information for beginning a content editing session.
- [- cancelContentEditingInputRequest:](<phasset/cancelcontenteditinginputrequest(__).md>) — Cancels a request for editing the asset’s content.
- [PHContentEditingInputRequestID](phcontenteditinginputrequestid.md) — An identifier for an asset content editing session.
- [OriginalResourceChoice](phasset/originalresourcechoice-swift.enum.md) — A choice of which original resource to use as the unadjusted base when reverting an asset’s content. _(beta)_
- [Editing Request Info Keys](../photokit/editing-request-info-keys.md) — Keys indicating the status of an asset content editing request, used in the completion handler of the [- requestContentEditingInputWithOptions:completionHandler:](<phasset/requestcontenteditinginput(with_completionhandler_).md>) method.
