---
title: AVMediaSelectionOption
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselectionoption
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectionoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectionoption.json'
content_hash: 'sha256:afb4b8e130157dfb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMediaSelectionOption

<sub>Class</sub>

An object that represents a specific option for the presentation of media within a group of options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMediaSelectionOption
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing media information

- [mediaType](avmediaselectionoption/mediatype.md) — The media type of the media data.
- [mediaSubTypes](avmediaselectionoption/mediasubtypes.md) — The media sub-types of the media data associated with the option.
- [- hasMediaCharacteristic:](<avmediaselectionoption/hasmediacharacteristic(__).md>) — Returns a Boolean value that indicates whether the receiver has media with the given media characteristic.

### Managing metadata

- [commonMetadata](avmediaselectionoption/commonmetadata.md) — An array of metadata items for each common metadata key for which a value is available.
- [availableMetadataFormats](avmediaselectionoption/availablemetadataformats.md) — The metadata formats that contain metadata associated with the option.
- [- metadataForFormat:](<avmediaselectionoption/metadata(forformat_).md>) — Returns an array of metadata items—one for each metadata item in the container of a given format.

### Determining playability

- [playable](avmediaselectionoption/isplayable.md) — A Boolean value that indicates whether the media selection option is playable.

### Getting the language and locale settings

- [displayName](avmediaselectionoption/displayname.md) — A string suitable for display using the current system locale.
- [- displayNameWithLocale:](<avmediaselectionoption/displayname(with_).md>) — Returns a string suitable for display using the specified locale.
- [locale](avmediaselectionoption/locale.md) — The locale for which the media option was authored.
- [extendedLanguageTag](avmediaselectionoption/extendedlanguagetag.md) — The IETF BCP 47 language tag associated with the option

### Getting the associated media selection option

- [- associatedMediaSelectionOptionInMediaSelectionGroup:](<avmediaselectionoption/associatedmediaselectionoption(in_).md>) — Returns a media selection option associated with the receiver in a given group.

### Creating a Now Playing language option

- [- makeNowPlayingInfoLanguageOption](<avmediaselectionoption/makenowplayinginfolanguageoption().md>) — Creates a language option for a media selection option.

### Creating a property list representation

- [- propertyList](<avmediaselectionoption/propertylist().md>) — Returns a serializable property list that’s sufficient to identify the option within its group.

## See Also

### Media selection

- [Selecting subtitles and alternative audio tracks](selecting-subtitles-and-alternative-audio-tracks.md) — Extend your app’s appeal to users by adding subtitles and alternative audio tracks in their native language.
- [AVMediaSelection](avmediaselection.md) — An object that represents a complete rendition of media selection options on an asset.
- [AVMediaSelectionGroup](avmediaselectiongroup.md) — An object that represents a collection of mutually exclusive options for the presentation of media within an asset.
- [AVMutableMediaSelection](avmutablemediaselection.md) — A mutable object that represents a complete rendition of media selection options on an asset.
- [AVPlayerMediaSelectionCriteria](avplayermediaselectioncriteria.md) — An object that specifies the preferred languages and media characteristics for a player.
- [AVCustomMediaSelectionScheme](avcustommediaselectionscheme.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.
- [AVMediaPresentationSelector](avmediapresentationselector.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSelector represents a collection of mutually exclusive settings.
- [AVMediaPresentationSetting](avmediapresentationsetting.md) — For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSetting represents a selectable setting for controlling the presentation of the media.
