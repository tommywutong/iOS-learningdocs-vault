---
title: Editing Request Info Keys
framework: Photos
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photokit/editing-request-info-keys
source_url: 'https://developer.apple.com/documentation/photokit/editing-request-info-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photokit/editing-request-info-keys.json'
content_hash: 'sha256:4df1c9a4c308e6a5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotoKit](../photokit.md) · [Photos](../photos.md) · [PHAsset](../photos/phasset.md)

# Editing Request Info Keys

<sub>API Collection</sub>

Keys indicating the status of an asset content editing request, used in the completion handler of the [- requestContentEditingInputWithOptions:completionHandler:](<../photos/phasset/requestcontenteditinginput(with_completionhandler_).md>) method.

## Topics

### Constants

- [PHContentEditingInputResultIsInCloudKey](../photos/phcontenteditinginputresultisincloudkey.md) — A Boolean value indicating whether the asset data is stored on the local device or must be downloaded from iCloud. (`NSNumber`)
- [PHContentEditingInputCancelledKey](../photos/phcontenteditinginputcancelledkey.md) — A Boolean value indicating whether the image request was canceled. (`NSNumber`)
- [PHContentEditingInputErrorKey](../photos/phcontenteditinginputerrorkey.md) — An error that occurred while attempting to load the asset data. (`NSError`)

## See Also

### Editing an Asset

- [Editing Asset Content](editing-asset-content.md) — Make a request to modify and save a photo or video asset.
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
