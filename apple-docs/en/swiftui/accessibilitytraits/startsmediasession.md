---
title: startsMediaSession
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilitytraits/startsmediasession
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilitytraits/startsmediasession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilitytraits/startsmediasession.json'
content_hash: 'sha256:9b2b89372cb6f480'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityTraits](../accessibilitytraits.md)

# startsMediaSession

<sub>Type Property</sub>

The accessibility element starts a media session when it is activated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let startsMediaSession: AccessibilityTraits
```

## Discussion

Use this trait to silence the audio output of an assistive technology, such as VoiceOver, during a media session that should not be interrupted. For example, you might use this trait to silence VoiceOver speech while the user is recording audio.

## See Also

### Getting traits

- [allowsDirectInteraction](allowsdirectinteraction.md) — The accessibility element allows direct touch interaction for VoiceOver users.
- [causesPageTurn](causespageturn.md) — The accessibility element causes an automatic page turn when VoiceOver finishes reading the text within it.
- [isButton](isbutton.md) — The accessibility element is a button.
- [isHeader](isheader.md) — The accessibility element is a header that divides content into sections, like the title of a navigation bar.
- [isImage](isimage.md) — The accessibility element is an image.
- [isKeyboardKey](iskeyboardkey.md) — The accessibility element behaves as a keyboard key.
- [isLink](islink.md) — The accessibility element is a link.
- [isModal](ismodal.md) — The accessibility element is modal.
- [isSearchField](issearchfield.md) — The accessibility element is a search field.
- [isSelected](isselected.md) — The accessibility element is currently selected.
- [isStaticText](isstatictext.md) — The accessibility element is a static text that cannot be modified by the user.
- [isSummaryElement](issummaryelement.md) — The accessibility element provides summary information when the application starts.
- [isToggle](istoggle.md) — The accessibility element is a toggle.
- [playsSound](playssound.md) — The accessibility element plays its own sound when activated.
- [updatesFrequently](updatesfrequently.md) — The accessibility element frequently updates its label or value.
