---
title: causesPageTurn
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitytraits/causespageturn
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/causespageturn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitytraits/causespageturn.json'
content_hash: 'sha256:8f7e793d349086c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityTraits](../uiaccessibilitytraits.md)

# causesPageTurn

<sub>Type Property</sub>

The accessibility element causes an automatic page turn when VoiceOver finishes reading the text within it.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated static let causesPageTurn: UIAccessibilityTraits
```

## Discussion

Use this trait to characterize an accessibility element that represents a page of content within a set of pages, such as a view that represents a page in a book. When VoiceOver finishes reading the content in the current page, it calls [accessibilityScroll(_:)](<../../objectivec/nsobject-swift.class/accessibilityscroll(__).md>) with [UIAccessibilityScrollDirectionNext](../uiaccessibilityscrolldirection/next.md) to scroll to the next content page. If VoiceOver detects that the new content doesn’t differ from the previous content, it stops scrolling.

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
