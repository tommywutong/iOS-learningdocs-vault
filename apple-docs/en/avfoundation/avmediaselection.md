---
title: AVMediaSelection
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselection
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselection.json'
content_hash: 'sha256:2def4ca8e32d80e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMediaSelection

<sub>Class</sub>

An object that represents a complete rendition of media selection options on an asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMediaSelection
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVMutableMediaSelection](avmutablemediaselection.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting the media selection

- [- selectedMediaOptionInMediaSelectionGroup:](<avmediaselection/selectedmediaoption(in_).md>) — Returns the media selection option that’s currently selected in the specified group.
- [- mediaSelectionCriteriaCanBeAppliedAutomaticallyToMediaSelectionGroup:](<avmediaselection/mediaselectioncriteriacanbeappliedautomatically(to_).md>) — Indicates whether the specified media selection group is subject to automatic media selection.

### Accessing the asset

- [asset](avmediaselection/asset.md) — The asset associated with the media selection.

## See Also

### Media selection

- [Selecting subtitles and alternative audio tracks](selecting-subtitles-and-alternative-audio-tracks.md) — Extend your app’s appeal to users by adding subtitles and alternative audio tracks in their native language.
- [AVMediaSelectionGroup](avmediaselectiongroup.md) — An object that represents a collection of mutually exclusive options for the presentation of media within an asset.
- [AVMediaSelectionOption](avmediaselectionoption.md) — An object that represents a specific option for the presentation of media within a group of options.
- [AVMutableMediaSelection](avmutablemediaselection.md) — A mutable object that represents a complete rendition of media selection options on an asset.
- [AVPlayerMediaSelectionCriteria](avplayermediaselectioncriteria.md) — An object that specifies the preferred languages and media characteristics for a player.
- [AVCustomMediaSelectionScheme](avcustommediaselectionscheme.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.
- [AVMediaPresentationSelector](avmediapresentationselector.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSelector represents a collection of mutually exclusive settings.
- [AVMediaPresentationSetting](avmediapresentationsetting.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSetting represents a selectable setting for controlling the presentation of the media.
