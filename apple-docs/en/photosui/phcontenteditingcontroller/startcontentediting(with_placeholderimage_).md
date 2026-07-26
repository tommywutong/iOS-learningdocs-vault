---
title: 'startContentEditing(with:placeholderImage:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.11+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phcontenteditingcontroller/startcontentediting(with:placeholderimage:)'
source_url: 'https://developer.apple.com/documentation/photosui/phcontenteditingcontroller/startcontentediting(with:placeholderimage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phcontenteditingcontroller/startcontentediting%28with%3Aplaceholderimage%3A%29.json'
content_hash: 'sha256:9b82a708d119b8f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHContentEditingController](../phcontenteditingcontroller.md)

# startContentEditing(with:placeholderImage:)

<sub>Instance Method</sub>

Tells your extension that asset data is available for editing.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func startContentEditing(with contentEditingInput: PHContentEditingInput, placeholderImage: UIImage)
```

<sub>macOS</sub>

```swift
func startContentEditing(with contentEditingInput: PHContentEditingInput, placeholderImage: NSImage)
```

## Parameters

- `contentEditingInput` — An object that describes the asset to be edited.

- `placeholderImage` — An image representing the current state of the asset suitable for temporarily displaying in your extension’s UI.

## Discussion

Photos calls this method before your extension view controller’s view appears.

For a photo asset, use the [displaySizeImage](../../photos/phcontenteditinginput/displaysizeimage.md) property of the provided [PHContentEditingInput](../../photos/phcontenteditinginput.md) object to perform editing in your extension’s UI. If your extension returned `true` from the [- canHandleAdjustmentData:](<canhandle(__).md>) method, this image represents the previous version of the asset—you need to use the [adjustmentData](../../photos/phcontenteditinginput/adjustmentdata.md) object to reconstruct the last edit made to the asset. Because asynchronously rendering the results of the previous edit may take some time, you can display the `placeholderImage` until your extension is ready to begin editing.

You don’t need to use the content editing input’s [fullSizeImageURL](../../photos/phcontenteditinginput/fullsizeimageurl.md) property until the user has finished editing and you need to render final output.

For a video asset, use the [PHContentEditingInput](../../photos/phcontenteditinginput.md) object to retrieve AVFoundation objects for editing audio and video content.

## See Also

### Performing an Edit

- [- finishContentEditingWithCompletionHandler:](<finishcontentediting(completionhandler_).md>) — Asks your extension for edited asset data to finish the editing session.
