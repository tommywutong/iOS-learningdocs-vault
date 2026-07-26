---
title: Editing Asset Content
framework: Photos
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photokit/editing-asset-content
source_url: 'https://developer.apple.com/documentation/photokit/editing-asset-content'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photokit/editing-asset-content.json'
content_hash: 'sha256:c59a039f2ac34082'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotoKit](../photokit.md) · [Photos](../photos.md) · [PHAsset](../photos/phasset.md)

# Editing Asset Content

<sub>Article</sub>

Make a request to modify and save a photo or video asset.

## Overview

For each photo asset, Photos keeps a previous and a current version of its image data, as well as a [PHAdjustmentData](../photos/phadjustmentdata.md) object that describes the last edit the user made to each asset’s content. Your app uses this information to support _resumable editing_.

When you begin editing an asset, Photos first asks whether your app can interpret the adjustment data from the most recent edit. If so, Photos provides the previous version of the asset as input for your editing session. After you read the adjustment data and reconstruct the edit it describes, your app might let the user alter or revert the last edit or make further changes. For example, adjustment data may describe filters applied to a photo. Your app reapplies those filters and allows the user to change filter parameters, add new filters, or remove filters.

If your app doesn’t support an asset’s adjustment data, Photos provides the current version of the asset as input to your editing session. The current version contains the rendered output of all past edits, so your app can further edit the asset but cannot alter or revert most recent edit.

To support continuity of editing between different apps and extensions, Photos keeps the current and previous versions of each asset, along with a [PHAdjustmentData](../photos/phadjustmentdata.md) object that describes the last edit. If your app supports the adjustment data from a previous edit, you can allow the user to revert or alter the edit.

> [!note] Note
> For video assets, Photos doesn’t store a previous version. If your app cannot read a video asset’s adjustment data, you must work with the current version of the video. Future versions won’t be able to make use of your app’s adjustment data.

### Request a Content Editing Input

Call the asset’s [- requestContentEditingInputWithOptions:completionHandler:](<../photos/phasset/requestcontenteditinginput(with_completionhandler_).md>) method. The [PHContentEditingInputRequestOptions](../photos/phcontenteditinginputrequestoptions.md) object you provide for the `options` parameter controls whether your app can handle the asset’s adjustment data. Photos calls your `completionHandler` block, providing a [PHContentEditingInput](../photos/phcontenteditinginput.md) object you can use for retrieving the image or video data to be edited.

### Apply Your Edits Through a Content Editing Output

Apply your edits to the asset. To allow a user to continue working with your edits later, create a new [PHAdjustmentData](../photos/phadjustmentdata.md) object describing the changes.

### Create a Content Editing Output

Initialize a [PHContentEditingOutput](../photos/phcontenteditingoutput.md) object. For photo- or video-only assets, use the editing output’s properties to provide edited asset data. For Live Photo assets, create a [PHLivePhotoEditingContext](../photos/phlivephotoeditingcontext.md) object to edit the Live Photo content.

### Commit Your Completed Edits

Commit your edits to the photo library by posting a change block to the shared [PHPhotoLibrary](../photos/phphotolibrary.md) object. In the block, create a [PHAssetChangeRequest](../photos/phassetchangerequest.md) object and set its [contentEditingOutput](../photos/phassetchangerequest/contenteditingoutput.md) property to the editing output that you created.

Each [PHPhotoLibrary](../photos/phphotolibrary.md) `performChanges` call prompts the user for permission to edit the contents of the photo library. To edit multiple assets in one batch, create multiple [PHAssetChangeRequest](../photos/phassetchangerequest.md) objects within the same change block, each with its own corresponding [PHContentEditingOutput](../photos/phcontenteditingoutput.md) object.

## See Also

### Editing an Asset

- [PHContentEditingInput](../photos/phcontenteditinginput.md) — A container that provides information about and access to the image, video, or Live Photo content of an asset to be edited.
- [PHContentEditingOutput](../photos/phcontenteditingoutput.md) — A container to which you provide the results of editing the photo, video, or Live Photo content of a Photos asset.
- [PHAdjustmentData](../photos/phadjustmentdata.md) — A description of the edits made to an asset’s photo, video, or Live Photo content, which allows your app to reconstruct or revert the effects of prior editing sessions.
- [PHContentEditingInputRequestOptions](../photos/phcontenteditinginputrequestoptions.md) — A set of options affecting the delivery of image or video data when you request to edit the content of a Photos asset.
- [PHLivePhotoEditingContext](../photos/phlivephotoeditingcontext.md) — An editing session for modifying the photo, video, and audio content of a Live Photo.
- [PHLivePhotoFrame](../photos/phlivephotoframe.md) — A container that provides image content for a single frame of a Live Photo in an editing context.
- [- canPerformEditOperation:](<../photos/phasset/canperform(__).md>) — Returns whether the asset supports the specified editing operation.
- [PHAssetEditOperation](../photos/phasseteditoperation.md) — Values identifying possible actions an asset can support, used by the [- canPerformEditOperation:](<../photos/phasset/canperform(__).md>) method.
- [- requestContentEditingInputWithOptions:completionHandler:](<../photos/phasset/requestcontenteditinginput(with_completionhandler_).md>) — Requests asset information for beginning a content editing session.
- [- cancelContentEditingInputRequest:](<../photos/phasset/cancelcontenteditinginputrequest(__).md>) — Cancels a request for editing the asset’s content.
- [PHContentEditingInputRequestID](../photos/phcontenteditinginputrequestid.md) — An identifier for an asset content editing session.
- [OriginalResourceChoice](../photos/phasset/originalresourcechoice-swift.enum.md) — A choice of which original resource to use as the unadjusted base when reverting an asset’s content. _(beta)_
- [Editing Request Info Keys](editing-request-info-keys.md) — Keys indicating the status of an asset content editing request, used in the completion handler of the [- requestContentEditingInputWithOptions:completionHandler:](<../photos/phasset/requestcontenteditinginput(with_completionhandler_).md>) method.
