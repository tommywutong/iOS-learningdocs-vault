---
title: AVMediaSelectionGroup
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselectiongroup
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectiongroup.json'
content_hash: 'sha256:f5012bd13e03325d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMediaSelectionGroup

<sub>Class</sub>

An object that represents a collection of mutually exclusive options for the presentation of media within an asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMediaSelectionGroup
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVAssetWriterInputGroup](avassetwriterinputgroup.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing media selection options

- [options](avmediaselectiongroup/options.md) — A collection of mutually exclusive media selection options
- [- mediaSelectionOptionWithPropertyList:](<avmediaselectiongroup/mediaselectionoption(withpropertylist_).md>) — Returns the media selection options that match the given property list.
- [defaultOption](avmediaselectiongroup/defaultoption.md) — The default option in the group.

### Configuring empty selection behavior

- [allowsEmptySelection](avmediaselectiongroup/allowsemptyselection.md) — A Boolean value that indicates whether it’s possible to present none of the options in the group when an associated player item is played.

### Filtering selection options

- [+ playableMediaSelectionOptionsFromArray:](<avmediaselectiongroup/playablemediaselectionoptions(from_).md>) — Returns an array containing the media selection options from a given array that are playable.
- [+ mediaSelectionOptionsFromArray:withLocale:](<avmediaselectiongroup/mediaselectionoptions(from_with_).md>) — Returns an array containing the media selection options from a given array that match the specified locale.
- [+ mediaSelectionOptionsFromArray:withMediaCharacteristics:](<avmediaselectiongroup/mediaselectionoptions(from_withmediacharacteristics_).md>) — Returns an array containing the media selection options from a given array that match given media characteristics.
- [+ mediaSelectionOptionsFromArray:withoutMediaCharacteristics:](<avmediaselectiongroup/mediaselectionoptions(from_withoutmediacharacteristics_).md>) — Returns an array containing the media selection options from a given array that do not match given media characteristics.
- [+ mediaSelectionOptionsFromArray:filteredAndSortedAccordingToPreferredLanguages:](<avmediaselectiongroup/mediaselectionoptions(from_filteredandsortedaccordingtopreferredlanguages_).md>) — Returns an array of media selection options, filtering them according to whether their locales match one of the specified languages.
- [customMediaSelectionScheme](avmediaselectiongroup/custommediaselectionscheme.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.

### Creating a Now Playing language option group

- [- makeNowPlayingInfoLanguageOptionGroup](<avmediaselectiongroup/makenowplayinginfolanguageoptiongroup().md>) — Creates a language option group from the media selection group.

## See Also

### Media selection

- [Selecting subtitles and alternative audio tracks](selecting-subtitles-and-alternative-audio-tracks.md) — Extend your app’s appeal to users by adding subtitles and alternative audio tracks in their native language.
- [AVMediaSelection](avmediaselection.md) — An object that represents a complete rendition of media selection options on an asset.
- [AVMediaSelectionOption](avmediaselectionoption.md) — An object that represents a specific option for the presentation of media within a group of options.
- [AVMutableMediaSelection](avmutablemediaselection.md) — A mutable object that represents a complete rendition of media selection options on an asset.
- [AVPlayerMediaSelectionCriteria](avplayermediaselectioncriteria.md) — An object that specifies the preferred languages and media characteristics for a player.
- [AVCustomMediaSelectionScheme](avcustommediaselectionscheme.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.
- [AVMediaPresentationSelector](avmediapresentationselector.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSelector represents a collection of mutually exclusive settings.
- [AVMediaPresentationSetting](avmediapresentationsetting.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSetting represents a selectable setting for controlling the presentation of the media.
