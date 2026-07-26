---
title: 'selectedMediaPresentationSettings(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/selectedmediapresentationsettings(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/selectedmediapresentationsettings(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/selectedmediapresentationsettings%28for%3A%29.json'
content_hash: 'sha256:a44e53dabda297c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# selectedMediaPresentationSettings(for:)

<sub>Instance Method</sub>

Indicates the media presentation settings that have most recently been selected for each AVMediaPresentationSelector of the AVCustomMediaSelectionScheme of the specified AVMediaSelectionGroup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func selectedMediaPresentationSettings(for mediaSelectionGroup: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : Any]
```

## Parameters

- `mediaSelectionGroup` — An AVMediaSelectionGroup obtained from the receiver’s asset for which the currently selected media presentation settings are desired.

## Return Value

A dictionary with AVMediaPresentationSelectors as keys and AVMediaPresentationSettings as values, providing the most recently selected setting for each selector or, if no setting has previously been selected, NSNull.

## See Also

### Selecting media options

- [- selectMediaPresentationSetting:forMediaSelectionGroup:](<select(__for_).md>) — When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular presentation setting, replacing any previous preference for settings of the same media presentation selector.
- [preferredCustomMediaSelectionSchemes](preferredcustommediaselectionschemes.md) — Indicates the AVCustomMediaSelectionSchemes of AVMediaSelectionGroups of the receiver’s asset with which an associated UI implementation should configure its interface for media selection.
- [- effectiveMediaPresentationSettingsForMediaSelectionGroup:](<effectivemediapresentationsettings(for_).md>) — Indicates the media presentation settings with media characteristics that are possessed by the currently selected AVMediaSelectionOption in the specified AVMediaSelectionGroup.
- [- selectMediaPresentationLanguage:forMediaSelectionGroup:](<selectmediapresentationlanguage(__for_).md>) — When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular language, replacing any previous preference for available languages of the specified group’s custom media selection scheme.
- [- selectedMediaPresentationLanguageForMediaSelectionGroup:](<selectedmediapresentationlanguage(for_).md>) — Returns the selected media presentation language for the specified media selection group, if any language has previously been selected via use of -selectMediaPresentationLanguages:forMediaSelectionGroup:.
- [currentMediaSelection](currentmediaselection.md) — The current media selections for each of the receiver’s media selection groups.
- [- selectMediaOption:inMediaSelectionGroup:](<select(__in_).md>) — Selects a media option in a given media selection group and deselects all other options in that group.
- [- selectMediaOptionAutomaticallyInMediaSelectionGroup:](<selectmediaoptionautomatically(in_).md>) — Selects the media option in the specified media selection group that best matches the receiver’s automatic selection criteria.
