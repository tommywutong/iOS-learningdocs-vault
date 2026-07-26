---
title: 'associatedMediaSelectionOption(in:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmediaselectionoption/associatedmediaselectionoption(in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/associatedmediaselectionoption(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectionoption/associatedmediaselectionoption%28in%3A%29.json'
content_hash: 'sha256:a0d7d13117a6a720'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionOption](../avmediaselectionoption.md)

# associatedMediaSelectionOption(in:)

<sub>Instance Method</sub>

Returns a media selection option associated with the receiver in a given group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func associatedMediaSelectionOption(in mediaSelectionGroup: AVMediaSelectionGroup) -> AVMediaSelectionOption?
```

## Parameters

- `mediaSelectionGroup` — A media selection group in which an associated option is to be sought.

## Return Value

A media selection option associated with the receiver in `mediaSelectionGroup`, or `nil` if none were found.

## Discussion

Audible media selection options often have associated legible media selection options; in particular, audible options are typically associated with forced-only subtitle options with the same locale. See [AVMediaCharacteristicContainsOnlyForcedSubtitles](../avmediacharacteristic/containsonlyforcedsubtitles.md) for a discussion of forced-only subtitles.
