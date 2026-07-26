---
title: PHLivePhotoFrame
framework: Photos
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoframe
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoframe.json'
content_hash: 'sha256:0d24e1fb72eb377c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHLivePhotoFrame

<sub>Protocol</sub>

A container that provides image content for a single frame of a Live Photo in an editing context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol PHLivePhotoFrame
```

## Overview

You don’t create classes that implement this protocol. Instead, you provide a [frameProcessor](phlivephotoeditingcontext/frameprocessor.md) block when editing a Live Photo with the [PHLivePhotoEditingContext](phlivephotoeditingcontext.md) class. When you process your edits for output or display, Photos calls your block repeatedly to process each frame of the Live Photo’s video and still photo content. On each call, Photos provides the frame’s image content and associated information in an object that adopts this protocol. In that block, you use that object’s [image](phlivephotoframe/image.md) property to access the image to be edited, then perform your edits and return another [CIImage](../coreimage/ciimage.md) object representing the result of processing the input image.

## Topics

### Editing the Frame Image

- [image](phlivephotoframe/image.md) — The image content of the frame to be processed.

### Getting Information About the Frame

- [renderScale](phlivephotoframe/renderscale.md) — The scale factor of the frame image relative to the Live Photo’s photo content.
- [time](phlivephotoframe/time.md) — The time offset, in seconds, of this frame relative to the start of the Live Photo.
- [type](phlivephotoframe/type.md) — The type of image content in this frame.
- [PHLivePhotoFrameType](phlivephotoframetype.md) — Identifiers for the type of frame image to be processed. Used with the [type](phlivephotoframe/type.md) property.

## See Also

### Editing an Asset

- [Editing Asset Content](../photokit/editing-asset-content.md) — Make a request to modify and save a photo or video asset.
- [PHContentEditingInput](phcontenteditinginput.md) — A container that provides information about and access to the image, video, or Live Photo content of an asset to be edited.
- [PHContentEditingOutput](phcontenteditingoutput.md) — A container to which you provide the results of editing the photo, video, or Live Photo content of a Photos asset.
- [PHAdjustmentData](phadjustmentdata.md) — A description of the edits made to an asset’s photo, video, or Live Photo content, which allows your app to reconstruct or revert the effects of prior editing sessions.
- [PHContentEditingInputRequestOptions](phcontenteditinginputrequestoptions.md) — A set of options affecting the delivery of image or video data when you request to edit the content of a Photos asset.
- [PHLivePhotoEditingContext](phlivephotoeditingcontext.md) — An editing session for modifying the photo, video, and audio content of a Live Photo.
- [- canPerformEditOperation:](<phasset/canperform(__).md>) — Returns whether the asset supports the specified editing operation.
- [PHAssetEditOperation](phasseteditoperation.md) — Values identifying possible actions an asset can support, used by the [- canPerformEditOperation:](<phasset/canperform(__).md>) method.
- [- requestContentEditingInputWithOptions:completionHandler:](<phasset/requestcontenteditinginput(with_completionhandler_).md>) — Requests asset information for beginning a content editing session.
- [- cancelContentEditingInputRequest:](<phasset/cancelcontenteditinginputrequest(__).md>) — Cancels a request for editing the asset’s content.
- [PHContentEditingInputRequestID](phcontenteditinginputrequestid.md) — An identifier for an asset content editing session.
- [OriginalResourceChoice](phasset/originalresourcechoice-swift.enum.md) — A choice of which original resource to use as the unadjusted base when reverting an asset’s content. _(beta)_
- [Editing Request Info Keys](../photokit/editing-request-info-keys.md) — Keys indicating the status of an asset content editing request, used in the completion handler of the [- requestContentEditingInputWithOptions:completionHandler:](<phasset/requestcontenteditinginput(with_completionhandler_).md>) method.
