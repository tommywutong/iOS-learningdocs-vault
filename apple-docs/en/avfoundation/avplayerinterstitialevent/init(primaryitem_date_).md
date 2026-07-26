---
title: 'init(primaryItem:date:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayerinterstitialevent/init(primaryitem:date:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/init(primaryitem:date:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/init%28primaryitem%3Adate%3A%29.json'
content_hash: 'sha256:99209bf2d863ccb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# init(primaryItem:date:)

<sub>Initializer</sub>

Creates an interstitial event for the specified date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(primaryItem: AVPlayerItem, date: Date)
```

## Parameters

- `primaryItem` — A player item that provides the primary playback content. It defines the timeline during which an interstitial event occurs. The item must have an asset that provides an intrinsic mapping from its timeline to real-time dates.

- `date` — A date within the timeline of the primary item at which to temporarily suspend playback of primary content, and play interstitial content instead.

## See Also

### Creating an event

- [+ interstitialEventWithPrimaryItem:time:](<init(primaryitem_time_).md>) — Creates an interstitial event for the specified time.
- [init(primaryItem:identifier:time:templateItems:restrictions:resumptionOffset:playoutLimit:userDefinedAttributes:)](<init(primaryitem_identifier_time_templateitems_restrictions_resumptionoffset_playoutlimit_userdefinedattributes_).md>) — Creates an interstitial event, with user-defined attributes, for the specified time.
- [init(primaryItem:identifier:date:templateItems:restrictions:resumptionOffset:playoutLimit:userDefinedAttributes:)](<init(primaryitem_identifier_date_templateitems_restrictions_resumptionoffset_playoutlimit_userdefinedattributes_).md>) — Creates an interstitial event, with user-defined attributes, for the specified date.
