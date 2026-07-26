---
title: 'mediaPresentationSettings(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetcache/mediapresentationsettings(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetcache/mediapresentationsettings(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetcache/mediapresentationsettings%28for%3A%29.json'
content_hash: 'sha256:1c252aeb27af381d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetCache](../avassetcache.md)

# mediaPresentationSettings(for:)

<sub>Instance Method</sub>

For each AVMediaPresentationSelector defined by the AVCustomMediaSelectionScheme of an AVMediaSelectionGroup, returns the AVMediaPresentationSettings that can be satisfied for offline operations, e.g. playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mediaPresentationSettings(for mediaSelectionGroup: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : [AVMediaPresentationSetting]]
```

## See Also

### Inspecting the cached media

- [playableOffline](isplayableoffline.md) — A Boolean value that indicates whether the asset is playable without an internet connection.
- [- mediaSelectionOptionsInMediaSelectionGroup:](<mediaselectionoptions(in_).md>) — Returns an array of locally cached media selection options that are available for offline use.
- [- mediaPresentationLanguagesForMediaSelectionGroup:](<mediapresentationlanguages(for_).md>) — Returns an array of extended language tags for languages that can be selected for offline operations via use of the AVMediaSelectionGroup’s AVCustomMediaSelectionScheme.
