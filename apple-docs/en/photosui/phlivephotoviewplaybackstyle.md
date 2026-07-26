---
title: PHLivePhotoViewPlaybackStyle
framework: PhotosUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phlivephotoviewplaybackstyle
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotoviewplaybackstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotoviewplaybackstyle.json'
content_hash: 'sha256:4ac4ce549b54a884'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHLivePhotoViewPlaybackStyle

<sub>Enumeration</sub>

Options for how much of the motion and sound content of a Live Photo to play, used in the [- startPlaybackWithStyle:](<phlivephotoview/startplayback(with_).md>) method and in messages to the view’s [delegate](phlivephotoview/delegate.md) object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHLivePhotoViewPlaybackStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [PHLivePhotoViewPlaybackStyleUndefined](phlivephotoviewplaybackstyle/undefined.md) — This value is invalid for use.
- [PHLivePhotoViewPlaybackStyleFull](phlivephotoviewplaybackstyle/full.md) — Plays back the entire motion and sound content of the Live Photo, including transition effects at the start and end.
- [PHLivePhotoViewPlaybackStyleHint](phlivephotoviewplaybackstyle/hint.md) — Plays back only a brief section of the motion content of the Live Photo, without sound.

### Initializers

- [init(rawValue:)](<phlivephotoviewplaybackstyle/init(rawvalue_).md>)

## See Also

### Constants

- [PHLivePhotoBadgeOptions](phlivephotobadgeoptions.md) — Options for the semantic use and display style of icons for badging Live Photo assets, used by the [+ livePhotoBadgeImageWithOptions:](<phlivephotoview/livephotobadgeimage(options_).md>) method.
