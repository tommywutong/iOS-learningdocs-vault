---
title: 'prepareLivePhotoForPlayback(withTargetSize:options:completionHandler:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phlivephotoeditingcontext/preparelivephotoforplayback(withtargetsize:options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/preparelivephotoforplayback(withtargetsize:options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoeditingcontext/preparelivephotoforplayback%28withtargetsize%3Aoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:6fbe26822978d38c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhotoEditingContext](../phlivephotoeditingcontext.md)

# prepareLivePhotoForPlayback(withTargetSize:options:completionHandler:)

<sub>Instance Method</sub>

Processes a Live Photo with your edits for viewing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func prepareLivePhotoForPlayback(withTargetSize targetSize: CGSize, options: [String : Any]? = nil, completionHandler handler: @escaping @Sendable (PHLivePhoto?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func livePhotoForPlayback(targetSize: CGSize, options: [String : Any]? = nil) async throws -> PHLivePhoto
```

## Parameters

- `targetSize` — The size of the view in which you plan to preview the edited Live Photo output.

- `options` — Options that affect Live Photo rendering. See `Live Photo Processing Options`.

- `handler` — A block that Photos calls on the main queue after processing is complete. The block takes the following parameters: - **livePhoto** — The rendered Live Photo, suitable for displaying in a [PHLivePhotoView](../../photosui/phlivephotoview.md) object. - **error** — If preparing the edited Live Photo for display succeeds, this parameter is `nil`. If processing fails, the `livePhoto` parameter is `nil`, and this parameter contains an error object describing the failure.

## Discussion

Use this method to generate preview versions of the edited Live Photo—for example, to display in your editing UI.

> [!note] Note
> This method does not guarantee performance appropriate for interactive editing. Instead, you might preview edits interactively using a still image (see the [fullSizeImage](fullsizeimage.md) property), and use this method to produce animated reviews upon the user’s request.

## See Also

### Processing an Editing Context’s Live Photo

- [- saveLivePhotoToOutput:options:completionHandler:](<savelivephoto(to_options_completionhandler_).md>) — Processes and saves a full-quality Live Photo as the output of your editing session.
- [PHLivePhotoEditingOption](../phlivephotoeditingoption.md) — Keys for the `options` dictionary used with the methods listed in Processing an Editing Context’s Live Photo.
- [- cancel](<cancel().md>) — Aborts any Live Photo processing in progress.
