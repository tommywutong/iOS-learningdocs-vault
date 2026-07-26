---
title: PHContentEditingOutput
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditingoutput
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditingoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditingoutput.json'
content_hash: 'sha256:0d47196bd23d1aea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHContentEditingOutput

<sub>Class</sub>

A container to which you provide the results of editing the photo, video, or Live Photo content of a Photos asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHContentEditingOutput
```

## Overview

To edit an asset’s photo or video content:

1. Fetch a [PHAsset](phasset.md) object that represents the photo or video to be edited.
2. Call the asset’s [- requestContentEditingInputWithOptions:completionHandler:](<phasset/requestcontenteditinginput(with_completionhandler_).md>) method to retrieve a [PHContentEditingInput](phcontenteditinginput.md) object. This object provides information about the asset, the asset data to be edited, and a preview image for display.
3. Apply your edits to the asset. To allow a user to continue working with the edit later (for example, to adjust the parameters of a photo filter), create a [PHAdjustmentData](phadjustmentdata.md) object describing the changes.
4. Initialize a [PHContentEditingOutput](phcontenteditingoutput.md) object. For photo- or video-only assets, provide the edited content with the [renderedContentURL](phcontenteditingoutput/renderedcontenturl.md) property. For Live Photo assets, create a [PHLivePhotoEditingContext](phlivephotoeditingcontext.md) object to edit the Live Photo content and pass your content editing output to the [- saveLivePhotoToOutput:options:completionHandler:](<phlivephotoeditingcontext/savelivephoto(to_options_completionhandler_).md>) method.

For all asset types, provide your adjustment data with the [adjustmentData](phcontenteditingoutput/adjustmentdata.md) property of the content editing output. 5. Use a photo library change block to commit the edit. (For details, see [PHPhotoLibrary](phphotolibrary.md).) In the block, create a [PHAssetChangeRequest](phassetchangerequest.md) object and set its [contentEditingOutput](phassetchangerequest/contenteditingoutput.md) property to the editing output that you created.

Each [PHPhotoLibrary](phphotolibrary.md) `performChanges` call prompts the user for permission to edit the contents of the photo library—to edit multiple assets in one batch, create multiple [PHAssetChangeRequest](phassetchangerequest.md) objects within the same change block, each with its own corresponding [PHContentEditingOutput](phcontenteditingoutput.md) object.

You can also edit assets from photo editing extensions. In this case, instead of working with a [PHAsset](phasset.md) object, you implement methods in the [PHContentEditingController](../photosui/phcontenteditingcontroller.md) protocol. Photos provides a [PHContentEditingOutput](phcontenteditingoutput.md) object when your extension begins editing. When editing is complete, Photos requests a [PHContentEditingOutput](phcontenteditingoutput.md) object that contains the edited asset content.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an Output Object to Edit an Existing Asset

- [- initWithContentEditingInput:](<phcontenteditingoutput/init(contenteditinginput_).md>) — Creates an editing output from the specified editing input.

### Creating an Output Object to Edit a Newly Created Asset

- [- initWithPlaceholderForCreatedAsset:](<phcontenteditingoutput/init(placeholderforcreatedasset_).md>) — Creates an editing output for use in adding a new asset to the photo library.

### Providing Edit and Adjustment Data

- [adjustmentData](phcontenteditingoutput/adjustmentdata.md) — An object describing the changes made to the asset.
- [renderedContentURL](phcontenteditingoutput/renderedcontenturl.md) — The URL at which to write a file containing edited asset content.

### Instance Properties

- [defaultRenderedContentType](phcontenteditingoutput/defaultrenderedcontenttype.md)
- [supportedRenderedContentTypes](phcontenteditingoutput/supportedrenderedcontenttypes.md)

### Instance Methods

- [- renderedContentURLForType:error:](<phcontenteditingoutput/renderedcontenturl(for_).md>)

## See Also

### Editing an Asset

- [Editing Asset Content](../photokit/editing-asset-content.md) — Make a request to modify and save a photo or video asset.
- [PHContentEditingInput](phcontenteditinginput.md) — A container that provides information about and access to the image, video, or Live Photo content of an asset to be edited.
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
