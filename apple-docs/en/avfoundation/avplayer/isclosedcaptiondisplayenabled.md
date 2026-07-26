---
title: isClosedCaptionDisplayEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（11.0 起废弃）, iPadOS 4.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.13 起废弃）, tvOS 9.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayer/isclosedcaptiondisplayenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/isclosedcaptiondisplayenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/isclosedcaptiondisplayenabled.json'
content_hash: 'sha256:d7644f1e16edceb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# isClosedCaptionDisplayEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the player uses closed captioning.

> [!warning] Deprecated
> Let a player enable closed captions automatically according to user preferences by setting the value of the [appliesMediaSelectionCriteriaAutomatically](appliesmediaselectioncriteriaautomatically.md) property to [true](../../swift/true.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isClosedCaptionDisplayEnabled: Bool { get set }
```

## Discussion

The player displays closed captions in the following cases:

- Closed captions are present in the media and the value of `closedCaptionDisplayEnabled` is [true](../../swift/true.md), or
- A media selection option representing a stream of closed captions is selected in the legible media selection group.

> [!note] Note
> It’s strongly recommended that you don’t rely on this property to control the display of closed captions and instead use the media selection capabilities of [AVPlayer](../avplayer.md) and [AVPlayerItem](../avplayeritem.md). The media selection API works equally well for displaying SDH subtitles as well as other kinds of content offering accessibility features. See [- selectMediaOption:inMediaSelectionGroup:](<../avplayeritem/select(__in_).md>) for more details.
