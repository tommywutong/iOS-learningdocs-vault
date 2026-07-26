---
title: AccessibilityTraits
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilitytraits
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilitytraits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilitytraits.json'
content_hash: 'sha256:687a865a1d987fa4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AccessibilityTraits

<sub>Structure</sub>

A set of accessibility traits that describe how an element behaves.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AccessibilityTraits
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting traits

- [allowsDirectInteraction](accessibilitytraits/allowsdirectinteraction.md) — The accessibility element allows direct touch interaction for VoiceOver users.
- [causesPageTurn](accessibilitytraits/causespageturn.md) — The accessibility element causes an automatic page turn when VoiceOver finishes reading the text within it.
- [isButton](accessibilitytraits/isbutton.md) — The accessibility element is a button.
- [isHeader](accessibilitytraits/isheader.md) — The accessibility element is a header that divides content into sections, like the title of a navigation bar.
- [isImage](accessibilitytraits/isimage.md) — The accessibility element is an image.
- [isKeyboardKey](accessibilitytraits/iskeyboardkey.md) — The accessibility element behaves as a keyboard key.
- [isLink](accessibilitytraits/islink.md) — The accessibility element is a link.
- [isModal](accessibilitytraits/ismodal.md) — The accessibility element is modal.
- [isSearchField](accessibilitytraits/issearchfield.md) — The accessibility element is a search field.
- [isSelected](accessibilitytraits/isselected.md) — The accessibility element is currently selected.
- [isStaticText](accessibilitytraits/isstatictext.md) — The accessibility element is a static text that cannot be modified by the user.
- [isSummaryElement](accessibilitytraits/issummaryelement.md) — The accessibility element provides summary information when the application starts.
- [isToggle](accessibilitytraits/istoggle.md) — The accessibility element is a toggle.
- [playsSound](accessibilitytraits/playssound.md) — The accessibility element plays its own sound when activated.
- [startsMediaSession](accessibilitytraits/startsmediasession.md) — The accessibility element starts a media session when it is activated.
- [updatesFrequently](accessibilitytraits/updatesfrequently.md) — The accessibility element frequently updates its label or value.

### Type Properties

- [isTabBar](accessibilitytraits/istabbar.md) — The accessibility element is a tab bar.

## See Also

### Assigning traits to content

- [accessibilityAddTraits(_:)](<view/accessibilityaddtraits(__).md>) — Adds the given traits to the view.
- [accessibilityRemoveTraits(_:)](<view/accessibilityremovetraits(__).md>) — Removes the given traits from this view.
