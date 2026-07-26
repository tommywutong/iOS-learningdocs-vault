---
title: 'saveLivePhoto(to:options:completionHandler:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phlivephotoeditingcontext/savelivephoto(to:options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/savelivephoto(to:options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoeditingcontext/savelivephoto%28to%3Aoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:7333a2e3a8459ac7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhotoEditingContext](../phlivephotoeditingcontext.md)

# saveLivePhoto(to:options:completionHandler:)

<sub>Instance Method</sub>

Processes and saves a full-quality Live Photo as the output of your editing session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func saveLivePhoto(to output: PHContentEditingOutput, options: [String : Any]? = nil, completionHandler handler: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func saveLivePhoto(to output: PHContentEditingOutput, options: [String : Any]? = nil) async throws
```

## Parameters

- `output` — The photo editing output to receive the rendered Live Photo, created from the same [PHContentEditingInput](../phcontenteditinginput.md) object you used to begin this Live Photo editing context.

- `options` — Options that affect Live Photo rendering. See `Live Photo Processing Options`.

- `handler` — A block that Photos calls on the main queue after rendering is complete. The block takes the following parameters: - **success** — `true` if rendering succeeds; otherwise `false`. - **error** — If rendering succeeds, this parameter is `nil`. If rendering fails, this parameter contains an error object describing the failure.

## Discussion

Use this method when you have finished an editing session and need to provide rendered output in a [PHContentEditingOutput](../phcontenteditingoutput.md) object. Unlike when rendering output for a photo or video asset, you don’t need to provide rendered output using the [renderedContentURL](../phcontenteditingoutput/renderedcontenturl.md) property of the editing output object. Instead, create a [PHContentEditingOutput](../phcontenteditingoutput.md) object using the [- initWithContentEditingInput:](<../phcontenteditingoutput/init(contenteditinginput_).md>) initializer, passing the same [PHContentEditingInput](../phcontenteditinginput.md) object you used in the [PHLivePhotoFrameProcessingBlock](../phlivephotoframeprocessingblock.md) initializer to start this Live Photo editing context. Then pass that editing output object to this method, and Photos renders the Live Photo and provides it to the editing output.

> [!note] Note
> Don’t forget to describe your edits in a [PHAdjustmentData](../phadjustmentdata.md) object and provide that to the [adjustmentData](../phcontenteditingoutput/adjustmentdata.md) property of your content editing output. Providing adjustment data allows your app (or photo editing extension) to non-destructively resume working with an edit later, whether on the same device or on another Mac or iOS device using iCloud Photo Library.

After this method’s completion handler signals successful rendering, you use the content editing output to complete the edit. In an app using the Photos framework, create a [PHAssetChangeRequest](../phassetchangerequest.md) object inside a [PHPhotoLibrary](../phphotolibrary.md) `performChanges` block, and set its [contentEditingOutput](../phassetchangerequest/contenteditingoutput.md) property to your editing output. In a photo editing extension running in the Photos app, your main view controller provides content editing output when requested by the [- finishContentEditingWithCompletionHandler:](<../../photosui/phcontenteditingcontroller/finishcontentediting(completionhandler_).md>) method.

## See Also

### Processing an Editing Context’s Live Photo

- [- prepareLivePhotoForPlaybackWithTargetSize:options:completionHandler:](<preparelivephotoforplayback(withtargetsize_options_completionhandler_).md>) — Processes a Live Photo with your edits for viewing.
- [PHLivePhotoEditingOption](../phlivephotoeditingoption.md) — Keys for the `options` dictionary used with the methods listed in Processing an Editing Context’s Live Photo.
- [- cancel](<cancel().md>) — Aborts any Live Photo processing in progress.
