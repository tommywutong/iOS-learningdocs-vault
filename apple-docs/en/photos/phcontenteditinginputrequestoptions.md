---
title: PHContentEditingInputRequestOptions
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditinginputrequestoptions
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginputrequestoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginputrequestoptions.json'
content_hash: 'sha256:56b3928a3d0ccc66'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHContentEditingInputRequestOptions

<sub>Class</sub>

A set of options affecting the delivery of image or video data when you request to edit the content of a Photos asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHContentEditingInputRequestOptions
```

## Overview

You use the [PHContentEditingInputRequestOptions](phcontenteditinginputrequestoptions.md) class with the [- requestContentEditingInputWithOptions:completionHandler:](<phasset/requestcontenteditinginput(with_completionhandler_).md>) method for editing the contents of a [PHAsset](phasset.md) object.

This class doesn’t affect photo editing extensions.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying Edting Request Options

- [canHandleAdjustmentData](phcontenteditinginputrequestoptions/canhandleadjustmentdata.md) — A block to be called when Photos needs to determine whether your app can continue previous edits made to an asset.
- [originalResourceChoice](phcontenteditinginputrequestoptions/originalresourcechoice.md) — The original resource to use as the unadjusted base when fulfilling the request. _(beta)_
- [skipsDisplaySizeImage](phcontenteditinginputrequestoptions/skipsdisplaysizeimage.md) — Set this value to `true` if you don’t want a `displaySizeImage` on the `PHContentEditingInput`. This can give performance wins when the image will not be used. _(beta)_

### Fetching Asset Data from iCloud

- [networkAccessAllowed](phcontenteditinginputrequestoptions/isnetworkaccessallowed.md) — A Boolean value that specifies whether Photos can download the asset from iCloud.
- [progressHandler](phcontenteditinginputrequestoptions/progresshandler.md) — A block Photos calls periodically while downloading the asset.

## See Also

### Editing an Asset

- [Editing Asset Content](../photokit/editing-asset-content.md) — Make a request to modify and save a photo or video asset.
- [PHContentEditingInput](phcontenteditinginput.md) — A container that provides information about and access to the image, video, or Live Photo content of an asset to be edited.
- [PHContentEditingOutput](phcontenteditingoutput.md) — A container to which you provide the results of editing the photo, video, or Live Photo content of a Photos asset.
- [PHAdjustmentData](phadjustmentdata.md) — A description of the edits made to an asset’s photo, video, or Live Photo content, which allows your app to reconstruct or revert the effects of prior editing sessions.
- [PHLivePhotoEditingContext](phlivephotoeditingcontext.md) — An editing session for modifying the photo, video, and audio content of a Live Photo.
- [PHLivePhotoFrame](phlivephotoframe.md) — A container that provides image content for a single frame of a Live Photo in an editing context.
- [- canPerformEditOperation:](<phasset/canperform(__).md>) — Returns whether the asset supports the specified editing operation.
- [PHAssetEditOperation](phasseteditoperation.md) — Values identifying possible actions an asset can support, used by the [- canPerformEditOperation:](<phasset/canperform(__).md>) method.
- [- requestContentEditingInputWithOptions:completionHandler:](<phasset/requestcontenteditinginput(with_completionhandler_).md>) — Requests asset information for beginning a content editing session.
- [- cancelContentEditingInputRequest:](<phasset/cancelcontenteditinginputrequest(__).md>) — Cancels a request for editing the asset’s content.
- [PHContentEditingInputRequestID](phcontenteditinginputrequestid.md) — An identifier for an asset content editing session.
- [OriginalResourceChoice](phasset/originalresourcechoice-swift.enum.md) — A choice of which original resource to use as the unadjusted base when reverting an asset’s content. _(beta)_
- [Editing Request Info Keys](../photokit/editing-request-info-keys.md) — Keys indicating the status of an asset content editing request, used in the completion handler of the [- requestContentEditingInputWithOptions:completionHandler:](<phasset/requestcontenteditinginput(with_completionhandler_).md>) method.
