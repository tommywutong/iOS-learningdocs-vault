---
title: AVPlayerMediaSelectionCriteria
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayermediaselectioncriteria
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayermediaselectioncriteria.json'
content_hash: 'sha256:c57abb39fbdd8e59'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerMediaSelectionCriteria

<sub>Class</sub>

An object that specifies the preferred languages and media characteristics for a player.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPlayerMediaSelectionCriteria
```

## Overview

An instance of this object represents the languages and media characteristics of assets that contain media selection options that a player attempts to select automatically when preparing and playing items. It lists the languages and media characteristics in their preferred order.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating media selection criteria

- [- initWithPreferredLanguages:preferredMediaCharacteristics:](<avplayermediaselectioncriteria/init(preferredlanguages_preferredmediacharacteristics_).md>) — Creates media selection criteria with the preferred languages and media characteristics.
- [- initWithPrincipalMediaCharacteristics:preferredLanguages:preferredMediaCharacteristics:](<avplayermediaselectioncriteria/init(principalmediacharacteristics_preferredlanguages_preferredmediacharacteristics_).md>) — Creates media selection criteria with the principal media characteristics, and preferred languages and media characteristics.

### Retrieving selection criteria settings

- [preferredLanguages](avplayermediaselectioncriteria/preferredlanguages.md) — An array of language identifiers in preferred order.
- [preferredMediaCharacteristics](avplayermediaselectioncriteria/preferredmediacharacteristics.md) — An array of media characteristics in preferred order.
- [principalMediaCharacteristics](avplayermediaselectioncriteria/principalmediacharacteristics.md) — An array of media characteristics that are essential to select when choosing media with a particular characteristic.

## See Also

### Media selection

- [Selecting subtitles and alternative audio tracks](selecting-subtitles-and-alternative-audio-tracks.md) — Extend your app’s appeal to users by adding subtitles and alternative audio tracks in their native language.
- [AVMediaSelection](avmediaselection.md) — An object that represents a complete rendition of media selection options on an asset.
- [AVMediaSelectionGroup](avmediaselectiongroup.md) — An object that represents a collection of mutually exclusive options for the presentation of media within an asset.
- [AVMediaSelectionOption](avmediaselectionoption.md) — An object that represents a specific option for the presentation of media within a group of options.
- [AVMutableMediaSelection](avmutablemediaselection.md) — A mutable object that represents a complete rendition of media selection options on an asset.
- [AVCustomMediaSelectionScheme](avcustommediaselectionscheme.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.
- [AVMediaPresentationSelector](avmediapresentationselector.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSelector represents a collection of mutually exclusive settings.
- [AVMediaPresentationSetting](avmediapresentationsetting.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSetting represents a selectable setting for controlling the presentation of the media.
