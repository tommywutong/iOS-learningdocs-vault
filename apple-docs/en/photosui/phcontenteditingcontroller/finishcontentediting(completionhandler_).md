---
title: 'finishContentEditing(completionHandler:)'
framework: PhotosUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.11+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photosui/phcontenteditingcontroller/finishcontentediting(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/photosui/phcontenteditingcontroller/finishcontentediting(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phcontenteditingcontroller/finishcontentediting%28completionhandler%3A%29.json'
content_hash: 'sha256:ec1ef682053204e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHContentEditingController](../phcontenteditingcontroller.md)

# finishContentEditing(completionHandler:)

<sub>Instance Method</sub>

Asks your extension for edited asset data to finish the editing session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func finishContentEditing(completionHandler: @escaping (PHContentEditingOutput?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func finishContentEditing() async -> PHContentEditingOutput?
```

## Parameters

- `completionHandler` — A block for your extension to call when you have finished editing. The block takes the following parameter: - **output** — The [PHContentEditingOutput](../../photos/phcontenteditingoutput.md) object you created and populated before calling the completion handler.

## Discussion

Photos calls this method when the user chooses to end the editing session. Your extension view controller should:

1. Disable UI elements to prevent the user from editing further while you complete the remaining steps on a background queue.
2. Create a [PHContentEditingOutput](../../photos/phcontenteditingoutput.md) object from the [PHContentEditingInput](../../photos/phcontenteditinginput.md) object that Photos provided to your extension in the [- startContentEditingWithInput:placeholderImage:](<startcontentediting(with_placeholderimage_).md>) method.

Use the content editing output to store the rendered photo or video data from the user’s edits and a [PHAdjustmentData](../../photos/phadjustmentdata.md) object describing the edits.

> [!note] Note
> To end editing without committing changes to the asset, leave the content editing output’s [adjustmentData](../../photos/phcontenteditingoutput/adjustmentdata.md) property set to `nil` and do not write to the location specified by its [renderedContentURL](../../photos/phcontenteditingoutput/renderedcontenturl.md) property.

1. Call the `completionHandler` block with your content editing output, to notify Photos that the edit is complete.
2. After the `completionHandler` block finishes executing, you may safely clean up any data or files related to your edit.

## See Also

### Performing an Edit

- [- startContentEditingWithInput:placeholderImage:](<startcontentediting(with_placeholderimage_).md>) — Tells your extension that asset data is available for editing.
