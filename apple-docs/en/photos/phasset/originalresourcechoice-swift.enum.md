---
title: PHAsset.OriginalResourceChoice
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/photos/phasset/originalresourcechoice-swift.enum
source_url: 'https://developer.apple.com/documentation/photos/phasset/originalresourcechoice-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasset/originalresourcechoice-swift.enum.json'
content_hash: 'sha256:ee6cd17b18457fec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAsset](../phasset.md)

# PHAsset.OriginalResourceChoice

<sub>Enumeration</sub>

A choice of which original resource to use as the unadjusted base when reverting an asset’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum OriginalResourceChoice
```

## Overview

Applies to RAW+JPEG assets.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Choices

- [PHOriginalResourceChoiceCompressed](originalresourcechoice-swift.enum/compressed.md) — The compressed original resource, such as a JPEG or HEIC, is used.
- [PHOriginalResourceChoiceRaw](originalresourcechoice-swift.enum/raw.md) — The RAW original resource is used.

### Initializers

- [init(rawValue:)](<originalresourcechoice-swift.enum/init(rawvalue_).md>) _(beta)_

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
- [- cancelContentEditingInputRequest:](<cancelcontenteditinginputrequest(__).md>) — Cancels a request for editing the asset’s content.
- [PHContentEditingInputRequestID](../phcontenteditinginputrequestid.md) — An identifier for an asset content editing session.
- [Editing Request Info Keys](../../photokit/editing-request-info-keys.md) — Keys indicating the status of an asset content editing request, used in the completion handler of the [- requestContentEditingInputWithOptions:completionHandler:](<requestcontenteditinginput(with_completionhandler_).md>) method.
