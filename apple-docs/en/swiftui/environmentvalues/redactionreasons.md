---
title: redactionReasons
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/redactionreasons
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/redactionreasons'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/redactionreasons.json'
content_hash: 'sha256:dccb8a91004e30d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# redactionReasons

<sub>Instance Property</sub>

The current redaction reasons applied to the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var redactionReasons: RedactionReasons { get set }
```

## See Also

### Redacting private content

- [Designing your app for the Always On state](../../watchos-apps/designing-your-app-for-the-always-on-state.md) — Customize your watchOS app’s user interface for continuous display.
- [Protecting sensitive content when screen sharing and remote control are active](../protecting-sensitive-content-when-screen-sharing.md) — Detect active screen capture sessions and respond appropriately to protect sensitive content in your app.
- [privacySensitive(_:)](<../view/privacysensitive(__).md>) — Marks the view as containing sensitive, private user data.
- [redacted(reason:)](<../view/redacted(reason_).md>) — Adds a reason to apply a redaction to this view hierarchy.
- [unredacted()](<../view/unredacted().md>) — Removes any reason to apply a redaction to this view hierarchy.
- [isSceneCaptured](isscenecaptured.md) — The current capture state.
- [RedactionReasons](../redactionreasons.md) — The reasons to apply a redaction to data displayed on screen.
