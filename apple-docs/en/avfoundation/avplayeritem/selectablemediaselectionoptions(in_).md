---
title: 'selectableMediaSelectionOptions(in:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/selectablemediaselectionoptions(in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/selectablemediaselectionoptions(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/selectablemediaselectionoptions%28in%3A%29.json'
content_hash: 'sha256:1659450f47da4916'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# selectableMediaSelectionOptions(in:)

<sub>Instance Method</sub>

Returns the media selection options in the specified media selection group that can produce content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func selectableMediaSelectionOptions(in mediaSelectionGroup: AVMediaSelectionGroup) -> [AVMediaSelectionOption]
```

## Parameters

- `mediaSelectionGroup` — A media selection group obtained from the receiver’s asset.

## Return Value

An array containing the media selection options from the group that can produce content. Options in the group that are not in this array can still be selected, but will produce no content.

## Discussion

Some media selection options depend on other options to produce content. For example, a subtitle option generated via audio transcription may require that the source audio option is currently selected. This method filters the options in the specified group to only those that can produce content given the current state of the player item’s media selection.
