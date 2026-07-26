---
title: PHLivePhotoEditingContext
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoeditingcontext
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoeditingcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoeditingcontext.json'
content_hash: 'sha256:b37c0a5dab2c0d1d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHLivePhotoEditingContext

<sub>Class</sub>

An editing session for modifying the photo, video, and audio content of a Live Photo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHLivePhotoEditingContext
```

## Overview

A Live Photo is a picture, captured by a supported iOS device, that includes motion and sound from the moments just before and after it was taken. Editing the content of a Live Photo works much like editing other asset types:

1. In an app using the Photos framework, fetch a [PHAsset](phasset.md) object that represents the Live Photo to edit, and use that object’s [- requestContentEditingInputWithOptions:completionHandler:](<phasset/requestcontenteditinginput(with_completionhandler_).md>) method to retrieve a [PHContentEditingInput](phcontenteditinginput.md) object.

In a photo editing extension that runs within the Photos app, your extension’s main view controller (which adopts the [PHContentEditingController](../photosui/phcontenteditingcontroller.md) protocol) receives a [PHContentEditingInput](phcontenteditinginput.md) object when the user chooses to edit a Live Photo with your extension. 2. Create a Live Photo editing context with the [- initWithLivePhotoEditingInput:](<phlivephotoeditingcontext/init(livephotoeditinginput_).md>) initializer.

You can create a Live Photo editing context only from [PHContentEditingInput](phcontenteditinginput.md) object that represents a Live Photo. Use the [livePhoto](phcontenteditinginput/livephoto.md) property of the editing input to verify that it has live Photo content. 3. Use the [frameProcessor](phlivephotoeditingcontext/frameprocessor.md) property to define a block to be used in processing the Live Photo’s visual content. Photos will call this block repeatedly to process each frame of the Live Photo’s video and still photo content. 4. Create a [PHContentEditingOutput](phcontenteditingoutput.md) object to store the results of your edit, then call the [- saveLivePhotoToOutput:options:completionHandler:](<phlivephotoeditingcontext/savelivephoto(to_options_completionhandler_).md>) to process the Live Photo and save it to your editing output object. This method applies your [frameProcessor](phlivephotoeditingcontext/frameprocessor.md) to each frame.

> [!note] Note
> You can also use the [- prepareLivePhotoForPlaybackWithTargetSize:options:completionHandler:](<phlivephotoeditingcontext/preparelivephotoforplayback(withtargetsize_options_completionhandler_).md>) method to process a preview-quality version of the Live Photo to display in your app’s UI during editing.

1. To allow a user to continue working with the edit later (for example, to adjust the parameters of a filter), create a [PHAdjustmentData](phadjustmentdata.md) object describing your changes, and store it in the [adjustmentData](phcontenteditingoutput/adjustmentdata.md) property of your editing output.
2. In an app using the Photos framework, use a photo library change block to commit the edit. (For details, see [PHPhotoLibrary](phphotolibrary.md).) In the block, create a [PHAssetChangeRequest](phassetchangerequest.md) object and set its [contentEditingOutput](phassetchangerequest/contenteditingoutput.md) property to the editing output that you created.

In a photo editing extension, provide the [PHContentEditingOutput](phcontenteditingoutput.md) object that you created in your main view controller’s [- finishContentEditingWithCompletionHandler:](<../photosui/phcontenteditingcontroller/finishcontentediting(completionhandler_).md>) method.

When you use either of the methods listed in Processing an Editing Context’s Live Photo, Photos calls your [frameProcessor](phlivephotoeditingcontext/frameprocessor.md) block repeatedly to process each frame of the Live Photo’s video and still photo content. In that block, a [PHLivePhotoFrame](phlivephotoframe.md) object provides the Live Photo’s existing content as a [CIImage](../coreimage/ciimage.md) object. You use Core Image to modify the image, then provide the result of your edits by returning a [CIImage](../coreimage/ciimage.md) object representing the result of processing the input image.

> [!tip] Tip
> Core Image provides several ways to process the Live Photo’s visual content. You can use the built-in filters listed in [Core Image Filter Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346) or create [CIFilter](../coreimage/cifilter-swift.class.md) subclasses using custom graphics kernel code. Or, to use other image processing technologies, you can directly access and modify image content in pixel buffers, Metal textures, or `IOSurfaceRef` objects with a custom [CIImageProcessorKernel](../coreimage/ciimageprocessorkernel.md) subclass.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Live Photo Editing Context

- [- initWithLivePhotoEditingInput:](<phlivephotoeditingcontext/init(livephotoeditinginput_).md>) — Creates a Live Photo editing context for the specified editing input.

### Preparing an Editing Context for Processing

- [frameProcessor](phlivephotoeditingcontext/frameprocessor.md) — A block to be called by Photos for processing each frame of the Live Photo’s visual content.
- [PHLivePhotoFrameProcessingBlock](phlivephotoframeprocessingblock.md) — The signature for a block Photos calls to process Live Photo frames.
- [audioVolume](phlivephotoeditingcontext/audiovolume.md) — The audio gain to apply to the processed Live Photo.

### Processing an Editing Context’s Live Photo

- [- saveLivePhotoToOutput:options:completionHandler:](<phlivephotoeditingcontext/savelivephoto(to_options_completionhandler_).md>) — Processes and saves a full-quality Live Photo as the output of your editing session.
- [- prepareLivePhotoForPlaybackWithTargetSize:options:completionHandler:](<phlivephotoeditingcontext/preparelivephotoforplayback(withtargetsize_options_completionhandler_).md>) — Processes a Live Photo with your edits for viewing.
- [PHLivePhotoEditingOption](phlivephotoeditingoption.md) — Keys for the `options` dictionary used with the methods listed in Processing an Editing Context’s Live Photo.
- [- cancel](<phlivephotoeditingcontext/cancel().md>) — Aborts any Live Photo processing in progress.

### Examining an Editing Context’s Live Photo

- [fullSizeImage](phlivephotoeditingcontext/fullsizeimage.md) — The unedited still photo content of the Live Photo.
- [duration](phlivephotoeditingcontext/duration.md) — The duration, in seconds, of the Live Photo.
- [photoTime](phlivephotoeditingcontext/phototime.md) — The offset, in seconds, from the beginning of the Live Photo’s duration to the time corresponding to its still photo.
- [orientation](phlivephotoeditingcontext/orientation.md) — The image orientation of the Live Photo.

### Errors

- [PHLivePhotoEditingErrorDomain](phlivephotoeditingerrordomain.md) — The domain value for error objects produced by a Live Photo editing context. _(deprecated)_
- [PHLivePhotoEditingErrorCode](phlivephotoeditingerrorcode.md) — Error codes for Live Photo editing errors.

## See Also

### Editing an Asset

- [Editing Asset Content](../photokit/editing-asset-content.md) — Make a request to modify and save a photo or video asset.
- [PHContentEditingInput](phcontenteditinginput.md) — A container that provides information about and access to the image, video, or Live Photo content of an asset to be edited.
- [PHContentEditingOutput](phcontenteditingoutput.md) — A container to which you provide the results of editing the photo, video, or Live Photo content of a Photos asset.
- [PHAdjustmentData](phadjustmentdata.md) — A description of the edits made to an asset’s photo, video, or Live Photo content, which allows your app to reconstruct or revert the effects of prior editing sessions.
- [PHContentEditingInputRequestOptions](phcontenteditinginputrequestoptions.md) — A set of options affecting the delivery of image or video data when you request to edit the content of a Photos asset.
- [PHLivePhotoFrame](phlivephotoframe.md) — A container that provides image content for a single frame of a Live Photo in an editing context.
- [- canPerformEditOperation:](<phasset/canperform(__).md>) — Returns whether the asset supports the specified editing operation.
- [PHAssetEditOperation](phasseteditoperation.md) — Values identifying possible actions an asset can support, used by the [- canPerformEditOperation:](<phasset/canperform(__).md>) method.
- [- requestContentEditingInputWithOptions:completionHandler:](<phasset/requestcontenteditinginput(with_completionhandler_).md>) — Requests asset information for beginning a content editing session.
- [- cancelContentEditingInputRequest:](<phasset/cancelcontenteditinginputrequest(__).md>) — Cancels a request for editing the asset’s content.
- [PHContentEditingInputRequestID](phcontenteditinginputrequestid.md) — An identifier for an asset content editing session.
- [OriginalResourceChoice](phasset/originalresourcechoice-swift.enum.md) — A choice of which original resource to use as the unadjusted base when reverting an asset’s content. _(beta)_
- [Editing Request Info Keys](../photokit/editing-request-info-keys.md) — Keys indicating the status of an asset content editing request, used in the completion handler of the [- requestContentEditingInputWithOptions:completionHandler:](<phasset/requestcontenteditinginput(with_completionhandler_).md>) method.
