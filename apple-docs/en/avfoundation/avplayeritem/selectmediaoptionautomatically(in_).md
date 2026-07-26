---
title: 'selectMediaOptionAutomatically(in:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/selectmediaoptionautomatically(in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/selectmediaoptionautomatically(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/selectmediaoptionautomatically%28in%3A%29.json'
content_hash: 'sha256:8189b1e5025679d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# selectMediaOptionAutomatically(in:)

<sub>Instance Method</sub>

Selects the media option in the specified media selection group that best matches the receiver’s automatic selection criteria.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func selectMediaOptionAutomatically(in mediaSelectionGroup: AVMediaSelectionGroup)
```

## Parameters

- `mediaSelectionGroup` — The media selection group, obtained from the receiver’s [asset](asset.md), that contains the specified option.

## Discussion

This method has no effect unless the [appliesMediaSelectionCriteriaAutomatically](../avplayer/appliesmediaselectioncriteriaautomatically.md) property of the associated [AVPlayer](../avplayer.md) is [true](../../swift/true.md) and unless automatic media selection has previously been overridden by invoking [- selectMediaOption:inMediaSelectionGroup:](<select(__in_).md>).

## See Also

### Selecting media options

- [- selectMediaPresentationSetting:forMediaSelectionGroup:](<select(__for_).md>) — When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular presentation setting, replacing any previous preference for settings of the same media presentation selector.
- [preferredCustomMediaSelectionSchemes](preferredcustommediaselectionschemes.md) — Indicates the AVCustomMediaSelectionSchemes of AVMediaSelectionGroups of the receiver’s asset with which an associated UI implementation should configure its interface for media selection.
- [- effectiveMediaPresentationSettingsForMediaSelectionGroup:](<effectivemediapresentationsettings(for_).md>) — Indicates the media presentation settings with media characteristics that are possessed by the currently selected AVMediaSelectionOption in the specified AVMediaSelectionGroup.
- [- selectMediaPresentationLanguage:forMediaSelectionGroup:](<selectmediapresentationlanguage(__for_).md>) — When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular language, replacing any previous preference for available languages of the specified group’s custom media selection scheme.
- [- selectedMediaPresentationLanguageForMediaSelectionGroup:](<selectedmediapresentationlanguage(for_).md>) — Returns the selected media presentation language for the specified media selection group, if any language has previously been selected via use of -selectMediaPresentationLanguages:forMediaSelectionGroup:.
- [- selectedMediaPresentationSettingsForMediaSelectionGroup:](<selectedmediapresentationsettings(for_).md>) — Indicates the media presentation settings that have most recently been selected for each AVMediaPresentationSelector of the AVCustomMediaSelectionScheme of the specified AVMediaSelectionGroup.
- [currentMediaSelection](currentmediaselection.md) — The current media selections for each of the receiver’s media selection groups.
- [- selectMediaOption:inMediaSelectionGroup:](<select(__in_).md>) — Selects a media option in a given media selection group and deselects all other options in that group.
