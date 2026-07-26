---
title: PHLivePhotoBadgeOptions
framework: PhotosUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phlivephotobadgeoptions
source_url: 'https://developer.apple.com/documentation/photosui/phlivephotobadgeoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phlivephotobadgeoptions.json'
content_hash: 'sha256:260ee6af0f59e94b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PhotosUI](../photosui.md)

# PHLivePhotoBadgeOptions

<sub>Structure</sub>

Options for the semantic use and display style of icons for badging Live Photo assets, used by the [+ livePhotoBadgeImageWithOptions:](<phlivephotoview/livephotobadgeimage(options_).md>) method.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct PHLivePhotoBadgeOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<phlivephotobadgeoptions/init(rawvalue_).md>) — Creates Live Photo badge options from a raw value.

### Constants

- [PHLivePhotoBadgeOptionsLiveOff](phlivephotobadgeoptions/liveoff.md) — Return an icon for identifying assets whose additional Live Photo content is disabled.
- [PHLivePhotoBadgeOptionsOverContent](phlivephotobadgeoptions/overcontent.md) — Return a variant icon for use on a variable background such as an animating Live Photo view.

## See Also

### Constants

- [PHLivePhotoViewPlaybackStyle](phlivephotoviewplaybackstyle.md) — Options for how much of the motion and sound content of a Live Photo to play, used in the [- startPlaybackWithStyle:](<phlivephotoview/startplayback(with_).md>) method and in messages to the view’s [delegate](phlivephotoview/delegate.md) object.
