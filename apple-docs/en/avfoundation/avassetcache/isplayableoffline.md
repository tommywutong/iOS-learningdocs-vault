---
title: isPlayableOffline
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetcache/isplayableoffline
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetcache/isplayableoffline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetcache/isplayableoffline.json'
content_hash: 'sha256:b51aa72cc88e0fed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetCache](../avassetcache.md)

# isPlayableOffline

<sub>Instance Property</sub>

A Boolean value that indicates whether the asset is playable without an internet connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isPlayableOffline: Bool { get }
```

## Discussion

Check the value of this property to determine the asset’s suitability for playback before presenting or attempting to play it.

> [!note] Note
> A property value of [true](../../swift/true.md) doesn’t indicate that all of the asset’s associated media selection options are available for offline playback. Instead, call [- mediaSelectionOptionsInMediaSelectionGroup:](<mediaselectionoptions(in_).md>) to determine which media selections are available.

## See Also

### Inspecting the cached media

- [- mediaSelectionOptionsInMediaSelectionGroup:](<mediaselectionoptions(in_).md>) — Returns an array of locally cached media selection options that are available for offline use.
- [- mediaPresentationLanguagesForMediaSelectionGroup:](<mediapresentationlanguages(for_).md>) — Returns an array of extended language tags for languages that can be selected for offline operations via use of the AVMediaSelectionGroup’s AVCustomMediaSelectionScheme.
- [- mediaPresentationSettingsForMediaSelectionGroup:](<mediapresentationsettings(for_).md>) — For each AVMediaPresentationSelector defined by the AVCustomMediaSelectionScheme of an AVMediaSelectionGroup, returns the AVMediaPresentationSettings that can be satisfied for offline operations, e.g. playback.
