---
title: shouldRenderAtPlaybackTime
framework: Photos
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoeditingoption/shouldrenderatplaybacktime
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoeditingoption/shouldrenderatplaybacktime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoeditingoption/shouldrenderatplaybacktime.json'
content_hash: 'sha256:2a1a6111e45fc2a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhotoEditingOption](../phlivephotoeditingoption.md)

# shouldRenderAtPlaybackTime

<sub>Type Property</sub>

Specifies whether processing should occur during or before playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let shouldRenderAtPlaybackTime: PHLivePhotoEditingOption
```

## Discussion

The value for this key is an NSNumber object with a Boolean value. With the default value of `false`, Photos always renders your edits immediately when you call the [- initWithLivePhotoEditingInput:](<../phlivephotoeditingcontext/init(livephotoeditinginput_).md>) method, calling your [frameProcessor](../phlivephotoeditingcontext/frameprocessor.md) block for each frame in the Live Photo’s video and still photo content.

When you specify a value of `true`, Photos can defer rendering until playback time, calling your [frameProcessor](../phlivephotoeditingcontext/frameprocessor.md) block only for photo and video frames that need to be displayed. However, in this case Photos may still choose to pre-render your edits if needed.

This option does not apply when rendering for output with the [- saveLivePhotoToOutput:options:completionHandler:](<../phlivephotoeditingcontext/savelivephoto(to_options_completionhandler_).md>) method.
