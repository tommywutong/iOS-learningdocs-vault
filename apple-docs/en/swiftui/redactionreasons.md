---
title: RedactionReasons
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/redactionreasons
source_url: 'https://developer.apple.com/documentation/swiftui/redactionreasons'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/redactionreasons.json'
content_hash: 'sha256:16dc5c2faef24d93'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# RedactionReasons

<sub>Structure</sub>

The reasons to apply a redaction to data displayed on screen.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RedactionReasons
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting redaction reasons

- [invalidated](redactionreasons/invalidated.md) — Displayed data should appear as invalidated and pending a new update.
- [placeholder](redactionreasons/placeholder.md) — Displayed data should appear as generic placeholders.
- [privacy](redactionreasons/privacy.md) — Displayed data should be obscured to protect private information.

### Creating redaction reasons

- [init(rawValue:)](<redactionreasons/init(rawvalue_).md>) — Creates a new set from a raw value.
- [rawValue](redactionreasons/rawvalue.md) — The raw value.

## See Also

### Redacting private content

- [Designing your app for the Always On state](../watchos-apps/designing-your-app-for-the-always-on-state.md) — Customize your watchOS app’s user interface for continuous display.
- [Protecting sensitive content when screen sharing and remote control are active](protecting-sensitive-content-when-screen-sharing.md) — Detect active screen capture sessions and respond appropriately to protect sensitive content in your app.
- [privacySensitive(_:)](<view/privacysensitive(__).md>) — Marks the view as containing sensitive, private user data.
- [redacted(reason:)](<view/redacted(reason_).md>) — Adds a reason to apply a redaction to this view hierarchy.
- [unredacted()](<view/unredacted().md>) — Removes any reason to apply a redaction to this view hierarchy.
- [redactionReasons](environmentvalues/redactionreasons.md) — The current redaction reasons applied to the view hierarchy.
- [isSceneCaptured](environmentvalues/isscenecaptured.md) — The current capture state.
