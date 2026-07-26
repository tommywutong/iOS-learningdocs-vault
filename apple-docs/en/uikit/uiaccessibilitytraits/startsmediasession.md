---
title: startsMediaSession
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitytraits/startsmediasession
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/startsmediasession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitytraits/startsmediasession.json'
content_hash: 'sha256:88b9d8492c53e369'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityTraits](../uiaccessibilitytraits.md)

# startsMediaSession

<sub>Type Property</sub>

The accessibility element starts a media session when the user activates it.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated static let startsMediaSession: UIAccessibilityTraits
```

## Discussion

Use this trait to silence the audio output of an assistive app, such as VoiceOver, during a media session that you don’t want to interrupt. For example, you might use this trait to silence VoiceOver speech while the user is recording audio.

## See Also

### Constants

- [UIAccessibilityTraitNone](none.md) — The accessibility element has no traits.
- [UIAccessibilityTraitButton](button.md) — The accessibility element behaves like a button.
- [UIAccessibilityTraitLink](link.md) — The accessibility element behaves like a link.
- [UIAccessibilityTraitImage](image.md) — The accessibility element behaves like an image.
- [UIAccessibilityTraitSearchField](searchfield.md) — The accessibility element behaves like a search field.
- [UIAccessibilityTraitToggleButton](togglebutton.md) — The accessibility element behaves like a toggle button.
- [UIAccessibilityTraitKeyboardKey](keyboardkey.md) — The accessibility element behaves like a keyboard key.
- [UIAccessibilityTraitStaticText](statictext.md) — The accessibility element behaves like static text that can’t change.
- [UIAccessibilityTraitHeader](header.md) — The accessibility element is a header that divides content into sections, such as the title of a navigation bar.
- [UIAccessibilityTraitTabBar](tabbar.md) — The accessibility element behaves like a tab bar.
- [UIAccessibilityTraitSummaryElement](summaryelement.md) — The accessibility element provides summary information when the app starts.
- [UIAccessibilityTraitSelected](selected.md) — The accessibility element is currently in a selected state.
- [UIAccessibilityTraitNotEnabled](notenabled.md) — The accessibility element isn’t in an enabled state and doesn’t respond to user interaction.
- [UIAccessibilityTraitAdjustable](adjustable.md) — The accessibility element allows continuous adjustment through a range of values.
- [UIAccessibilityTraitAllowsDirectInteraction](allowsdirectinteraction.md) — The accessibility element allows direct touch interaction for VoiceOver users.
