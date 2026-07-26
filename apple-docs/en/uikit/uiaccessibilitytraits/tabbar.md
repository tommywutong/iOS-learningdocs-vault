---
title: tabBar
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitytraits/tabbar
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/tabbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitytraits/tabbar.json'
content_hash: 'sha256:9d968f143ff90fe0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityTraits](../uiaccessibilitytraits.md)

# tabBar

<sub>Type Property</sub>

The accessibility element behaves like a tab bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated static let tabBar: UIAccessibilityTraits
```

## Discussion

Use this trait to characterize an accessibility element that represents an ordered list of tabs.

If an accessibility element has this trait, return [false](../../swift/false.md) for [isAccessibilityElement](../../objectivec/nsobject-swift.class/isaccessibilityelement.md).

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
- [UIAccessibilityTraitSummaryElement](summaryelement.md) — The accessibility element provides summary information when the app starts.
- [UIAccessibilityTraitSelected](selected.md) — The accessibility element is currently in a selected state.
- [UIAccessibilityTraitNotEnabled](notenabled.md) — The accessibility element isn’t in an enabled state and doesn’t respond to user interaction.
- [UIAccessibilityTraitAdjustable](adjustable.md) — The accessibility element allows continuous adjustment through a range of values.
- [UIAccessibilityTraitAllowsDirectInteraction](allowsdirectinteraction.md) — The accessibility element allows direct touch interaction for VoiceOver users.
- [UIAccessibilityTraitUpdatesFrequently](updatesfrequently.md) — The accessibility element frequently updates its label or value.
