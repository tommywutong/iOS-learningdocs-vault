---
title: cancel()
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoeditingcontext/cancel()
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoeditingcontext/cancel%28%29.json'
content_hash: 'sha256:27faf68b2fe7d7d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhotoEditingContext](../phlivephotoeditingcontext.md)

# cancel()

<sub>Instance Method</sub>

Aborts any Live Photo processing in progress.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func cancel()
```

## Discussion

This method applies only after you’ve begun processing a Live Photo for display or output with the [- initWithLivePhotoEditingInput:](<init(livephotoeditinginput_).md>) or [- saveLivePhotoToOutput:options:completionHandler:](<savelivephoto(to_options_completionhandler_).md>) method. After you call this method, Photos calls your completion handler and provides an error with the [PHLivePhotoEditingErrorCodeAborted](../phlivephotoeditingerrorcode/aborted.md) error code.

## See Also

### Processing an Editing Context’s Live Photo

- [- saveLivePhotoToOutput:options:completionHandler:](<savelivephoto(to_options_completionhandler_).md>) — Processes and saves a full-quality Live Photo as the output of your editing session.
- [- prepareLivePhotoForPlaybackWithTargetSize:options:completionHandler:](<preparelivephotoforplayback(withtargetsize_options_completionhandler_).md>) — Processes a Live Photo with your edits for viewing.
- [PHLivePhotoEditingOption](../phlivephotoeditingoption.md) — Keys for the `options` dictionary used with the methods listed in Processing an Editing Context’s Live Photo.
