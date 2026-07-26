---
title: UIAccessibility.DirectTouchOptions
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/directtouchoptions
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/directtouchoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/directtouchoptions.json'
content_hash: 'sha256:c643b1875c4388a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# UIAccessibility.DirectTouchOptions

<sub>Structure</sub>

Constants that configure how VoiceOver produces audio for direct touch areas.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct DirectTouchOptions
```

## Overview

_Direct touch areas_ are regions of the screen where VoiceOver passes gestures directly to the app instead of interpreting them as VoiceOver commands.

Examples of direct touch areas include:

- A keyboard in a music-creation app
- A player view in a game that produces sounds
- An area where you sign your name in a document

If an element doesn’t use `UIAccessibility.DirectTouchOptions`, VoiceOver speaks the element and immediately starts sending touch events to the app.

Specify `DirectTouchOptions` to customize VoiceOver regions using these two constants:

- Use [silentOnTouch](../../swiftui/accessibilitydirecttouchoptions/silentontouch.md) to ensure VoiceOver is silent when a person touches the direct touch area. In this region, the app produces its own audio feedback without conflicting with VoiceOver audio.
- Use [requiresActivation](../../swiftui/accessibilitydirecttouchoptions/requiresactivation.md) to ensure a person interacts with the user interface element before a touch passes through to the element. This is useful for scenarios where an errant touch may produce undesired input, such as a signature field.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<directtouchoptions/init(rawvalue_).md>) — Creates a new direct touch options structure using an unsigned integer.

### Type Properties

- [UIAccessibilityDirectTouchOptionRequiresActivation](directtouchoptions/requiresactivation.md) — Inhibits passthrough to the direct touch area until a person double-taps the element.
- [UIAccessibilityDirectTouchOptionSilentOnTouch](directtouchoptions/silentontouch.md) — Allows a direct touch area to immediately receive touch events without triggering VoiceOver audio.

## See Also

### Configuring behavior

- [accessibilityCustomRotors](../../objectivec/nsobject-swift.class/accessibilitycustomrotors.md)
- [accessibilityElementsHidden](../../objectivec/nsobject-swift.class/accessibilityelementshidden.md)
- [accessibilityRespondsToUserInteraction](../../objectivec/nsobject-swift.class/accessibilityrespondstouserinteraction.md)
- [accessibilityViewIsModal](../../objectivec/nsobject-swift.class/accessibilityviewismodal.md)
- [shouldGroupAccessibilityChildren](../../objectivec/nsobject-swift.class/shouldgroupaccessibilitychildren.md)
- [accessibilityDirectTouchOptions](../../objectivec/nsobject-swift.class/accessibilitydirecttouchoptions.md)
