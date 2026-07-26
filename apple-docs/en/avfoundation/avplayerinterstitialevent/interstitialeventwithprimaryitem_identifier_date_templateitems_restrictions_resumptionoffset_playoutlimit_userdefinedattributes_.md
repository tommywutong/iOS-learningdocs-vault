---
title: 'interstitialEventWithPrimaryItem:identifier:date:templateItems:restrictions:resumptionOffset:playoutLimit:userDefinedAttributes:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+（18.0 起废弃）, iPadOS 15.0+（18.0 起废弃）, Mac Catalyst 15.0+（18.0 起废弃）, macOS 12.0+（15.0 起废弃）, tvOS 15.0+（18.0 起废弃）, watchOS 8.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avplayerinterstitialevent/interstitialeventwithprimaryitem:identifier:date:templateitems:restrictions:resumptionoffset:playoutlimit:userdefinedattributes:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/interstitialeventwithprimaryitem:identifier:date:templateitems:restrictions:resumptionoffset:playoutlimit:userdefinedattributes:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/interstitialeventwithprimaryitem%3Aidentifier%3Adate%3Atemplateitems%3Arestrictions%3Aresumptionoffset%3Aplayoutlimit%3Auserdefinedattributes%3A.json'
content_hash: 'sha256:a58c2a9d3d661271'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# interstitialEventWithPrimaryItem:identifier:date:templateItems:restrictions:resumptionOffset:playoutLimit:userDefinedAttributes:

<sub>Type Method</sub>

Creates an interstitial event, with user-defined attributes, for the specified date.

> [!warning] Deprecated
> Use [+ interstitialEventWithPrimaryItem:date:](<init(primaryitem_date_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) interstitialEventWithPrimaryItem:(AVPlayerItem *) primaryItem identifier:(NSString *) identifier date:(NSDate *) date templateItems:(NSArray<AVPlayerItem *> *) templateItems restrictions:(AVPlayerInterstitialEventRestrictions) restrictions resumptionOffset:(CMTime) resumptionOffset playoutLimit:(CMTime) playoutLimit userDefinedAttributes:(NSDictionary *) userDefinedAttributes;
```

## Parameters

- `primaryItem` — The player item that represents the primary content. The item must contain an [AVAsset](../avasset.md) that provides intrinsic mappings from its timeline to real-time dates.

- `identifier` — An external identifier for the event.

- `date` — A date within the date range of the primary item that playback of interstitial content begins.

- `templateItems` — An array of player item configurations to use as templates for player items that play interstitial content.

- `restrictions` — Restrictions on access to playback controls during the event.

- `resumptionOffset` — The time offset for resuming playback of the primary content after interstital content finishes. You can specify a definite time, or specify [indefinite](../../coremedia/cmtime/indefinite.md) to indicate that the effective resumption time offset needs to align with time elapsed during interstitial playback.

- `playoutLimit` — The time offset from the beginning of the interstitial when interstitial playback needs to end, if interstitial assets are longer. Pass a positive numeric value, or [invalid](../../coremedia/cmtime/invalid.md) to indicate no playout limit.

- `userDefinedAttributes` — Custom attributes to add to the event.

## See Also

### Creating an event

- [+ interstitialEventWithPrimaryItem:time:](<init(primaryitem_time_).md>) — Creates an interstitial event for the specified time.
- [+ interstitialEventWithPrimaryItem:date:](<init(primaryitem_date_).md>) — Creates an interstitial event for the specified date.
- [interstitialEventWithPrimaryItem:identifier:time:templateItems:restrictions:resumptionOffset:playoutLimit:userDefinedAttributes:](interstitialeventwithprimaryitem_identifier_time_templateitems_restrictions_resumptionoffset_playoutlimit_userdefinedattributes_.md) — Creates an interstitial event, with user-defined attributes, for the specified time. _(deprecated)_
