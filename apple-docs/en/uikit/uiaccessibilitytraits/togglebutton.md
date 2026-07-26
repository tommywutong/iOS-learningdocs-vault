---
title: toggleButton
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitytraits/togglebutton
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/togglebutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitytraits/togglebutton.json'
content_hash: 'sha256:a252044b882d9854'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityTraits](../uiaccessibilitytraits.md)

# toggleButton

<sub>Type Property</sub>

The accessibility element behaves like a toggle button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated static let toggleButton: UIAccessibilityTraits
```

## Discussion

Use this trait to characterize an accessibility element that represents a button that toggles a value on, off, or mixed status. VoiceOver will describe the options offered by the toggle button.

> [!note] Note
> If you want VoiceOver to describe the toggle as a switch button, combine the toggle trait with a button trait.

## See Also

### Constants

- [UIAccessibilityTraitNone](none.md) — The accessibility element has no traits.
- [UIAccessibilityTraitButton](button.md) — The accessibility element behaves like a button.
- [UIAccessibilityTraitLink](link.md) — The accessibility element behaves like a link.
- [UIAccessibilityTraitImage](image.md) — The accessibility element behaves like an image.
- [UIAccessibilityTraitSearchField](searchfield.md) — The accessibility element behaves like a search field.
- [UIAccessibilityTraitKeyboardKey](keyboardkey.md) — The accessibility element behaves like a keyboard key.
- [UIAccessibilityTraitStaticText](statictext.md) — The accessibility element behaves like static text that can’t change.
- [UIAccessibilityTraitHeader](header.md) — The accessibility element is a header that divides content into sections, such as the title of a navigation bar.
- [UIAccessibilityTraitTabBar](tabbar.md) — The accessibility element behaves like a tab bar.
- [UIAccessibilityTraitSummaryElement](summaryelement.md) — The accessibility element provides summary information when the app starts.
- [UIAccessibilityTraitSelected](selected.md) — The accessibility element is currently in a selected state.
- [UIAccessibilityTraitNotEnabled](notenabled.md) — The accessibility element isn’t in an enabled state and doesn’t respond to user interaction.
- [UIAccessibilityTraitAdjustable](adjustable.md) — The accessibility element allows continuous adjustment through a range of values.
- [UIAccessibilityTraitAllowsDirectInteraction](allowsdirectinteraction.md) — The accessibility element allows direct touch interaction for VoiceOver users.
- [UIAccessibilityTraitUpdatesFrequently](updatesfrequently.md) — The accessibility element frequently updates its label or value.
