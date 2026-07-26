---
title: 'mediaSelectionOptions(in:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetcache/mediaselectionoptions(in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetcache/mediaselectionoptions(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetcache/mediaselectionoptions%28in%3A%29.json'
content_hash: 'sha256:5876dff53b42eb0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetCache](../avassetcache.md)

# mediaSelectionOptions(in:)

<sub>Instance Method</sub>

Returns an array of locally cached media selection options that are available for offline use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mediaSelectionOptions(in mediaSelectionGroup: AVMediaSelectionGroup) -> [AVMediaSelectionOption]
```

## Parameters

- `mediaSelectionGroup` — The containing media selection group.

## Return Value

The array of media selection options, or an empty array if none are available.

## See Also

### Inspecting the cached media

- [playableOffline](isplayableoffline.md) — A Boolean value that indicates whether the asset is playable without an internet connection.
- [- mediaPresentationLanguagesForMediaSelectionGroup:](<mediapresentationlanguages(for_).md>) — Returns an array of extended language tags for languages that can be selected for offline operations via use of the AVMediaSelectionGroup’s AVCustomMediaSelectionScheme.
- [- mediaPresentationSettingsForMediaSelectionGroup:](<mediapresentationsettings(for_).md>) — For each AVMediaPresentationSelector defined by the AVCustomMediaSelectionScheme of an AVMediaSelectionGroup, returns the AVMediaPresentationSettings that can be satisfied for offline operations, e.g. playback.
