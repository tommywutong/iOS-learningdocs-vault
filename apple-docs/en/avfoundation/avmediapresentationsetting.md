---
title: AVMediaPresentationSetting
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediapresentationsetting
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediapresentationsetting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediapresentationsetting.json'
content_hash: 'sha256:52f2bde612297b9c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMediaPresentationSetting

<sub>Class</sub>

For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSetting represents a selectable setting for controlling the presentation of the media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMediaPresentationSetting
```

## Overview

Each selectable setting is associated with a media characteristic that one or more of the AVMediaSelectionOptions in the AVMediaSelectionGroup possesses. By selecting a setting in a user interface that offers AVMediaPresentationSettings, users are essentially indicating a preference for the media characteristic of the selected setting. Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying the setting

- [mediaCharacteristic](avmediapresentationsetting/mediacharacteristic.md) — Provides the media characteristic that corresponds to the selectable setting.
- [- displayNameForLocaleIdentifier:](<avmediapresentationsetting/displayname(forlocaleidentifier_).md>) — Returns the display name for the selectable setting that best matches the specified locale identifier.

## See Also

### Media selection

- [Selecting subtitles and alternative audio tracks](selecting-subtitles-and-alternative-audio-tracks.md) — Extend your app’s appeal to users by adding subtitles and alternative audio tracks in their native language.
- [AVMediaSelection](avmediaselection.md) — An object that represents a complete rendition of media selection options on an asset.
- [AVMediaSelectionGroup](avmediaselectiongroup.md) — An object that represents a collection of mutually exclusive options for the presentation of media within an asset.
- [AVMediaSelectionOption](avmediaselectionoption.md) — An object that represents a specific option for the presentation of media within a group of options.
- [AVMutableMediaSelection](avmutablemediaselection.md) — A mutable object that represents a complete rendition of media selection options on an asset.
- [AVPlayerMediaSelectionCriteria](avplayermediaselectioncriteria.md) — An object that specifies the preferred languages and media characteristics for a player.
- [AVCustomMediaSelectionScheme](avcustommediaselectionscheme.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.
- [AVMediaPresentationSelector](avmediapresentationselector.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSelector represents a collection of mutually exclusive settings.
