---
title: 'cancelContentEditingInputRequest(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phasset/cancelcontenteditinginputrequest(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phasset/cancelcontenteditinginputrequest(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasset/cancelcontenteditinginputrequest%28_%3A%29.json'
content_hash: 'sha256:e0203513fa1c7556'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAsset](../phasset.md)

# cancelContentEditingInputRequest(_:)

<sub>Instance Method</sub>

Cancels a request for editing the asset’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func cancelContentEditingInputRequest(_ requestID: PHContentEditingInputRequestID)
```

## Parameters

- `requestID` — The numeric identifier of the request to be canceled.

## Discussion

When you request asset editing information with the [- requestContentEditingInputWithOptions:completionHandler:](<requestcontenteditinginput(with_completionhandler_).md>) method, the asset returns a numeric identifier for the request. To cancel the request before it completes, provide this identifier when calling the [- cancelContentEditingInputRequest:](<cancelcontenteditinginputrequest(__).md>) method.

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
- [- requestContentEditingInputWithOptions:completionHandler:](<requestcontenteditinginput(with_completionhandler_).md>) — Requests asset information for beginning a content editing session.
- [PHContentEditingInputRequestID](../phcontenteditinginputrequestid.md) — An identifier for an asset content editing session.
- [OriginalResourceChoice](originalresourcechoice-swift.enum.md) — A choice of which original resource to use as the unadjusted base when reverting an asset’s content. _(beta)_
- [Editing Request Info Keys](../../photokit/editing-request-info-keys.md) — Keys indicating the status of an asset content editing request, used in the completion handler of the [- requestContentEditingInputWithOptions:completionHandler:](<requestcontenteditinginput(with_completionhandler_).md>) method.
