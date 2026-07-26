---
title: 'init(primaryItem:time:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayerinterstitialevent/init(primaryitem:time:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/init(primaryitem:time:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/init%28primaryitem%3Atime%3A%29.json'
content_hash: 'sha256:9b950a6f3567e764'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# init(primaryItem:time:)

<sub>Initializer</sub>

Creates an interstitial event for the specified time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(primaryItem: AVPlayerItem, time: CMTime)
```

## Parameters

- `primaryItem` — A player item that provides the primary playback content. It defines the timeline during which an interstitial event occurs. The item must have an asset that provides an intrinsic mapping from its timeline to real-time dates.

- `time` — A time within the timeline of the primary item at which to temporarily suspend playback of primary content, and play interstitial content instead.

## See Also

### Creating an event

- [+ interstitialEventWithPrimaryItem:date:](<init(primaryitem_date_).md>) — Creates an interstitial event for the specified date.
- [init(primaryItem:identifier:time:templateItems:restrictions:resumptionOffset:playoutLimit:userDefinedAttributes:)](<init(primaryitem_identifier_time_templateitems_restrictions_resumptionoffset_playoutlimit_userdefinedattributes_).md>) — Creates an interstitial event, with user-defined attributes, for the specified time.
- [init(primaryItem:identifier:date:templateItems:restrictions:resumptionOffset:playoutLimit:userDefinedAttributes:)](<init(primaryitem_identifier_date_templateitems_restrictions_resumptionoffset_playoutlimit_userdefinedattributes_).md>) — Creates an interstitial event, with user-defined attributes, for the specified date.
