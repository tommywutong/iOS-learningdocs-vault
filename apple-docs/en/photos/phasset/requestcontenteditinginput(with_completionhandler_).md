---
title: 'requestContentEditingInput(with:completionHandler:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phasset/requestcontenteditinginput(with:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/photos/phasset/requestcontenteditinginput(with:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasset/requestcontenteditinginput%28with%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:3d54fcc06efb7079'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAsset](../phasset.md)

# requestContentEditingInput(with:completionHandler:)

<sub>Instance Method</sub>

Requests asset information for beginning a content editing session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func requestContentEditingInput(with options: PHContentEditingInputRequestOptions?, completionHandler: @escaping (PHContentEditingInput?, [AnyHashable : Any]) -> Void) -> PHContentEditingInputRequestID
```

## Parameters

- `options` — Options affecting how Photos handles an edit session request.

- `completionHandler` — A block that Photos calls when the requested asset editing information is ready. The block takes the following parameters: - **contentEditingInput** — An object that describes the asset for editing and provides methods for loading the image or video content to be edited. - **info** — A dictionary providing information about the status of the request. See [Editing Request Info Keys](../../photokit/editing-request-info-keys.md) for possible keys and values. In iOS 10.0, tvOS 10.0, and later, Photos always calls this block on the main queue. In earlier releases, Photos calls this block on an arbitrary serial queue—if your block needs to update the UI, dispatch that work to the main queue.

## Return Value

A numeric identifier for the request. Pass this identifier to the [- cancelContentEditingInputRequest:](<cancelcontenteditinginputrequest(__).md>) method if you need to cancel the request before it completes.

## Discussion

When you call this method, Photos downloads the asset’s image or video data (if necessary) and prepares it for editing, then calls your `completionHandler` block to provide a [PHContentEditingInput](../phcontenteditinginput.md) object you use for editing.

To complete the edit, create a [PHContentEditingOutput](../phcontenteditingoutput.md) object from the editing input to provide the edited asset data. Then, commit the edit by posting a change block to the shared [PHPhotoLibrary](../phphotolibrary.md) object. In the block, create a [PHAssetChangeRequest](../phassetchangerequest.md) object and set its [contentEditingOutput](../phassetchangerequest/contenteditingoutput.md) property to the editing output you created.

## See Also

### Editing an Asset

- [Editing Asset Content](../../photokit/editing-asset-content.md) — Make a request to modify and save a photo or video asset.
- [PHContentEditingInput](../phcontenteditinginput.md) — A container that provides information about and access to the image, video, or Live Photo content of an asset to be edited.
- [PHContentEditingOutput](../phcontenteditingoutput.md) — A container to which you provide the results of editing the photo, video, or Live Photo content of a Photos asset.
- [PHAdjustmentData](../phadjustmentdata.md) — A description of the edits made to an asset’s photo, video, or Live Photo content, which allows your app to reconstruct or revert the effects of prior editing sessions.
- [PHContentEditingInputRequestOptions](../phcontenteditinginputrequestoptions.md) — A set of options affecting the delivery of image or video data when you request to edit the content of a Photos asset.
- [PHLivePhotoEditingContext](../phlivephotoeditingcontext.md) — An editing session for modifying the photo, video, and audio content of a Live Photo.
- [PHLivePhotoFrame](../phlivephotoframe.md) — A container that provides image content for a single frame of a Live Photo in an editing context.
- [- canPerformEditOperation:](<canperform(__).md>) — Returns whether the asset supports the specified editing operation.
- [PHAssetEditOperation](../phasseteditoperation.md) — Values identifying possible actions an asset can support, used by the [- canPerformEditOperation:](<canperform(__).md>) method.
- [- cancelContentEditingInputRequest:](<cancelcontenteditinginputrequest(__).md>) — Cancels a request for editing the asset’s content.
- [PHContentEditingInputRequestID](../phcontenteditinginputrequestid.md) — An identifier for an asset content editing session.
- [OriginalResourceChoice](originalresourcechoice-swift.enum.md) — A choice of which original resource to use as the unadjusted base when reverting an asset’s content. _(beta)_
- [Editing Request Info Keys](../../photokit/editing-request-info-keys.md) — Keys indicating the status of an asset content editing request, used in the completion handler of the [- requestContentEditingInputWithOptions:completionHandler:](<requestcontenteditinginput(with_completionhandler_).md>) method.
