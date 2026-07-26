---
title: PHLivePhotoFrameProcessingBlock
framework: Photos
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoframeprocessingblock
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoframeprocessingblock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoframeprocessingblock.json'
content_hash: 'sha256:05b603775adc59e4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHLivePhotoFrameProcessingBlock

<sub>Type Alias</sub>

The signature for a block Photos calls to process Live Photo frames.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias PHLivePhotoFrameProcessingBlock = (any PHLivePhotoFrame, NSErrorPointer) -> CIImage?
```

## Discussion

To apply edits to a Live Photo, define a block with this signature and assign it to the [frameProcessor](phlivephotoeditingcontext/frameprocessor.md) property of a Live Photo editing context. Then call the [- initWithLivePhotoEditingInput:](<phlivephotoeditingcontext/init(livephotoeditinginput_).md>) to prepare a preview-quality version of your edits for display, or the [- saveLivePhotoToOutput:options:completionHandler:](<phlivephotoeditingcontext/savelivephoto(to_options_completionhandler_).md>) method to produce full-quality final output. When you call one of those methods, Photos calls your frame processor block repeatedly—processing each frame of the Live Photo’s video content as well as its still photo content—to render the output.

This block takes the following parameters:

- **frame** — A [PHLivePhotoFrame](phlivephotoframe.md) object describing the frame image to be processed.
- **error** — If your block cannot successfully process the frame, set this pointer to an error object describing the failure.

Your block should return a [CIImage](../coreimage/ciimage.md) object representing the result of your edits, or `nil` to indicate that your image processing has failed and the Live Photo edit should be aborted. Use the `frame` parameter’s [image](phlivephotoframe/image.md) property to access the image to be edited.

## See Also

### Preparing an Editing Context for Processing

- [frameProcessor](phlivephotoeditingcontext/frameprocessor.md) — A block to be called by Photos for processing each frame of the Live Photo’s visual content.
- [audioVolume](phlivephotoeditingcontext/audiovolume.md) — The audio gain to apply to the processed Live Photo.
