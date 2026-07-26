---
title: 'select(_:in:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritem/select(_:in:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/select(_:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/select%28_%3Ain%3A%29.json'
content_hash: 'sha256:e45d9270589cbb4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# select(_:in:)

<sub>Instance Method</sub>

Selects a media option in a given media selection group and deselects all other options in that group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func select(_ mediaSelectionOption: AVMediaSelectionOption?, in mediaSelectionGroup: AVMediaSelectionGroup)
```

## Parameters

- `mediaSelectionOption` — The option to select. If the value of the [allowsEmptySelection](../avmediaselectiongroup/allowsemptyselection.md) property of `mediaSelectionGroup` is [true](../../swift/true.md), you can pass `nil` to deselect all media selection options in the group.

- `mediaSelectionGroup` — The media selection group, obtained from the receiver’s asset, that contains `mediaSelectionOption`.

## Discussion

If `mediaSelectionOption` isn’t a member of the `mediaSelectionGroup`, no change in presentation state will result.

If multiple options within a group meet your criteria for selection according to locale or other considerations, and if these options are otherwise indistinguishable to you according to media characteristics that are meaningful for your application, content is typically authored so that the first available option that meets your criteria is appropriate for selection.

## See Also

### Selecting media options

- [- selectMediaPresentationSetting:forMediaSelectionGroup:](<select(__for_).md>) — When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular presentation setting, replacing any previous preference for settings of the same media presentation selector.
- [preferredCustomMediaSelectionSchemes](preferredcustommediaselectionschemes.md) — Indicates the AVCustomMediaSelectionSchemes of AVMediaSelectionGroups of the receiver’s asset with which an associated UI implementation should configure its interface for media selection.
- [- effectiveMediaPresentationSettingsForMediaSelectionGroup:](<effectivemediapresentationsettings(for_).md>) — Indicates the media presentation settings with media characteristics that are possessed by the currently selected AVMediaSelectionOption in the specified AVMediaSelectionGroup.
- [- selectMediaPresentationLanguage:forMediaSelectionGroup:](<selectmediapresentationlanguage(__for_).md>) — When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular language, replacing any previous preference for available languages of the specified group’s custom media selection scheme.
- [- selectedMediaPresentationLanguageForMediaSelectionGroup:](<selectedmediapresentationlanguage(for_).md>) — Returns the selected media presentation language for the specified media selection group, if any language has previously been selected via use of -selectMediaPresentationLanguages:forMediaSelectionGroup:.
- [- selectedMediaPresentationSettingsForMediaSelectionGroup:](<selectedmediapresentationsettings(for_).md>) — Indicates the media presentation settings that have most recently been selected for each AVMediaPresentationSelector of the AVCustomMediaSelectionScheme of the specified AVMediaSelectionGroup.
- [currentMediaSelection](currentmediaselection.md) — The current media selections for each of the receiver’s media selection groups.
- [- selectMediaOptionAutomaticallyInMediaSelectionGroup:](<selectmediaoptionautomatically(in_).md>) — Selects the media option in the specified media selection group that best matches the receiver’s automatic selection criteria.
