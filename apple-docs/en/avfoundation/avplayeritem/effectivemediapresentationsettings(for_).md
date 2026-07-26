---
title: 'effectiveMediaPresentationSettings(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/effectivemediapresentationsettings(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/effectivemediapresentationsettings(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/effectivemediapresentationsettings%28for%3A%29.json'
content_hash: 'sha256:5f9d7edd05204bf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# effectiveMediaPresentationSettings(for:)

<sub>Instance Method</sub>

Indicates the media presentation settings with media characteristics that are possessed by the currently selected AVMediaSelectionOption in the specified AVMediaSelectionGroup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func effectiveMediaPresentationSettings(for mediaSelectionGroup: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : Any]
```

## Parameters

- `mediaSelectionGroup` — An AVMediaSelectionGroup obtained from the receiver’s asset for which the currently effective media presentation settings are desired.

## Return Value

A dictionary with AVMediaPresentationSelectors as keys and AVMediaPresentationSettings as values, unless the AVMediaSelectionOption currently selected in the group possesses none of the characteristics associated with the selector’s settings. In that case the dictionary value will be NSNull.

## Discussion

Effective media presentation settings can differ from the currently effective media presentation settings if no AVMediaSelectionOption of the specified AVMediaSelectionGroup with the currently selected media presentation language possesses all of the characteristics associated with the currently selected settings. A value of NSNull for an AVMediaPresentationSelector can occur if either the content is inappropriately authored for the use of the AVCustomMediaSelectionScheme or if the currently selected AVMediaSelectionOption has been selected by means other than through the use of AVMediaPresentationSettings.

## See Also

### Selecting media options

- [- selectMediaPresentationSetting:forMediaSelectionGroup:](<select(__for_).md>) — When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular presentation setting, replacing any previous preference for settings of the same media presentation selector.
- [preferredCustomMediaSelectionSchemes](preferredcustommediaselectionschemes.md) — Indicates the AVCustomMediaSelectionSchemes of AVMediaSelectionGroups of the receiver’s asset with which an associated UI implementation should configure its interface for media selection.
- [- selectMediaPresentationLanguage:forMediaSelectionGroup:](<selectmediapresentationlanguage(__for_).md>) — When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular language, replacing any previous preference for available languages of the specified group’s custom media selection scheme.
- [- selectedMediaPresentationLanguageForMediaSelectionGroup:](<selectedmediapresentationlanguage(for_).md>) — Returns the selected media presentation language for the specified media selection group, if any language has previously been selected via use of -selectMediaPresentationLanguages:forMediaSelectionGroup:.
- [- selectedMediaPresentationSettingsForMediaSelectionGroup:](<selectedmediapresentationsettings(for_).md>) — Indicates the media presentation settings that have most recently been selected for each AVMediaPresentationSelector of the AVCustomMediaSelectionScheme of the specified AVMediaSelectionGroup.
- [currentMediaSelection](currentmediaselection.md) — The current media selections for each of the receiver’s media selection groups.
- [- selectMediaOption:inMediaSelectionGroup:](<select(__in_).md>) — Selects a media option in a given media selection group and deselects all other options in that group.
- [- selectMediaOptionAutomaticallyInMediaSelectionGroup:](<selectmediaoptionautomatically(in_).md>) — Selects the media option in the specified media selection group that best matches the receiver’s automatic selection criteria.
