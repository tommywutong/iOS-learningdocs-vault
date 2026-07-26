---
title: AVMediaPresentationSelector
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediapresentationselector
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediapresentationselector'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediapresentationselector.json'
content_hash: 'sha256:5b76dc9ef7c8ca43'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMediaPresentationSelector

<sub>Class</sub>

For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSelector represents a collection of mutually exclusive settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMediaPresentationSelector
```

## Overview

Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying the selector

- [identifier](avmediapresentationselector/identifier.md) — Provides the authored identifier for the selector.
- [- displayNameForLocaleIdentifier:](<avmediapresentationselector/displayname(forlocaleidentifier_).md>) — Returns the display name for the selector that best matches the specified locale identifier.

### Accessing settings

- [settings](avmediapresentationselector/settings.md) — Provides selectable mutually exclusive settings for the selector.

## See Also

### Media selection

- [Selecting subtitles and alternative audio tracks](selecting-subtitles-and-alternative-audio-tracks.md) — Extend your app’s appeal to users by adding subtitles and alternative audio tracks in their native language.
- [AVMediaSelection](avmediaselection.md) — An object that represents a complete rendition of media selection options on an asset.
- [AVMediaSelectionGroup](avmediaselectiongroup.md) — An object that represents a collection of mutually exclusive options for the presentation of media within an asset.
- [AVMediaSelectionOption](avmediaselectionoption.md) — An object that represents a specific option for the presentation of media within a group of options.
- [AVMutableMediaSelection](avmutablemediaselection.md) — A mutable object that represents a complete rendition of media selection options on an asset.
- [AVPlayerMediaSelectionCriteria](avplayermediaselectioncriteria.md) — An object that specifies the preferred languages and media characteristics for a player.
- [AVCustomMediaSelectionScheme](avcustommediaselectionscheme.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.
- [AVMediaPresentationSetting](avmediapresentationsetting.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSetting represents a selectable setting for controlling the presentation of the media.
