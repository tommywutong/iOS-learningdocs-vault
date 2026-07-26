---
title: UIAccessibilityTraits
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitytraits
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitytraits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitytraits.json'
content_hash: 'sha256:c3ec9bccbf9b3ac6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityTraits

<sub>Structure</sub>

Constants that describe how an accessibility element behaves.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct UIAccessibilityTraits
```

## Overview

Set these traits to tell an assistive app how an accessibility element behaves or how to treat it.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Hashable](../swift/hashable.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [UIAccessibilityTraitNone](uiaccessibilitytraits/none.md) — The accessibility element has no traits.
- [UIAccessibilityTraitButton](uiaccessibilitytraits/button.md) — The accessibility element behaves like a button.
- [UIAccessibilityTraitLink](uiaccessibilitytraits/link.md) — The accessibility element behaves like a link.
- [UIAccessibilityTraitImage](uiaccessibilitytraits/image.md) — The accessibility element behaves like an image.
- [UIAccessibilityTraitSearchField](uiaccessibilitytraits/searchfield.md) — The accessibility element behaves like a search field.
- [UIAccessibilityTraitToggleButton](uiaccessibilitytraits/togglebutton.md) — The accessibility element behaves like a toggle button.
- [UIAccessibilityTraitKeyboardKey](uiaccessibilitytraits/keyboardkey.md) — The accessibility element behaves like a keyboard key.
- [UIAccessibilityTraitStaticText](uiaccessibilitytraits/statictext.md) — The accessibility element behaves like static text that can’t change.
- [UIAccessibilityTraitHeader](uiaccessibilitytraits/header.md) — The accessibility element is a header that divides content into sections, such as the title of a navigation bar.
- [UIAccessibilityTraitTabBar](uiaccessibilitytraits/tabbar.md) — The accessibility element behaves like a tab bar.
- [UIAccessibilityTraitSummaryElement](uiaccessibilitytraits/summaryelement.md) — The accessibility element provides summary information when the app starts.
- [UIAccessibilityTraitSelected](uiaccessibilitytraits/selected.md) — The accessibility element is currently in a selected state.
- [UIAccessibilityTraitNotEnabled](uiaccessibilitytraits/notenabled.md) — The accessibility element isn’t in an enabled state and doesn’t respond to user interaction.
- [UIAccessibilityTraitAdjustable](uiaccessibilitytraits/adjustable.md) — The accessibility element allows continuous adjustment through a range of values.
- [UIAccessibilityTraitAllowsDirectInteraction](uiaccessibilitytraits/allowsdirectinteraction.md) — The accessibility element allows direct touch interaction for VoiceOver users.
- [UIAccessibilityTraitUpdatesFrequently](uiaccessibilitytraits/updatesfrequently.md) — The accessibility element frequently updates its label or value.
- [UIAccessibilityTraitCausesPageTurn](uiaccessibilitytraits/causespageturn.md) — The accessibility element causes an automatic page turn when VoiceOver finishes reading the text within it.
- [UIAccessibilityTraitPlaysSound](uiaccessibilitytraits/playssound.md) — The accessibility element plays its own sound when the user activates it.
- [UIAccessibilityTraitStartsMediaSession](uiaccessibilitytraits/startsmediasession.md) — The accessibility element starts a media session when the user activates it.
- [UIAccessibilityTraitSupportsZoom](uiaccessibilitytraits/supportszoom.md) — The accessibility element supports zooming in and out on its content.

## See Also

### Supporting basic accessibility

- [isAccessibilityElement](../objectivec/nsobject-swift.class/isaccessibilityelement.md)
- [accessibilityLabel](../objectivec/nsobject-swift.class/accessibilitylabel.md)
- [accessibilityValue](../objectivec/nsobject-swift.class/accessibilityvalue.md)
- [accessibilityHint](../objectivec/nsobject-swift.class/accessibilityhint.md)
- [accessibilityTraits](../objectivec/nsobject-swift.class/accessibilitytraits.md)
