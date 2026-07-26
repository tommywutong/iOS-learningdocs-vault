---
title: PHLivePhotoEditingOption
framework: Photos
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoeditingoption
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoeditingoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoeditingoption.json'
content_hash: 'sha256:2db2ca02289759a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHLivePhotoEditingOption

<sub>Structure</sub>

Keys for the `options` dictionary used with the methods listed in Processing an Editing Context’s Live Photo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct PHLivePhotoEditingOption
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<phlivephotoeditingoption/init(rawvalue_).md>) — Initializes a Live Photo editing option from its raw value.

### Type Properties

- [PHLivePhotoShouldRenderAtPlaybackTime](phlivephotoeditingoption/shouldrenderatplaybacktime.md) — Specifies whether processing should occur during or before playback.

## See Also

### Processing an Editing Context’s Live Photo

- [- saveLivePhotoToOutput:options:completionHandler:](<phlivephotoeditingcontext/savelivephoto(to_options_completionhandler_).md>) — Processes and saves a full-quality Live Photo as the output of your editing session.
- [- prepareLivePhotoForPlaybackWithTargetSize:options:completionHandler:](<phlivephotoeditingcontext/preparelivephotoforplayback(withtargetsize_options_completionhandler_).md>) — Processes a Live Photo with your edits for viewing.
- [- cancel](<phlivephotoeditingcontext/cancel().md>) — Aborts any Live Photo processing in progress.
