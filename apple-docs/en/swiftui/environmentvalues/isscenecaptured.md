---
title: isSceneCaptured
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/isscenecaptured
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/isscenecaptured'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/isscenecaptured.json'
content_hash: 'sha256:36597f93d093dca5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# isSceneCaptured

<sub>Instance Property</sub>

The current capture state.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isSceneCaptured: Bool { get set }
```

## Discussion

Use this value to determine whether the scene is actively being cloned to another destination (like during AirPlay) or is being mirrored or recorded.

Your app can respond to changes in this value to take appropriate action, like obscuring content.

## See Also

### Redacting private content

- [Designing your app for the Always On state](../../watchos-apps/designing-your-app-for-the-always-on-state.md) — Customize your watchOS app’s user interface for continuous display.
- [Protecting sensitive content when screen sharing and remote control are active](../protecting-sensitive-content-when-screen-sharing.md) — Detect active screen capture sessions and respond appropriately to protect sensitive content in your app.
- [privacySensitive(_:)](<../view/privacysensitive(__).md>) — Marks the view as containing sensitive, private user data.
- [redacted(reason:)](<../view/redacted(reason_).md>) — Adds a reason to apply a redaction to this view hierarchy.
- [unredacted()](<../view/unredacted().md>) — Removes any reason to apply a redaction to this view hierarchy.
- [redactionReasons](redactionreasons.md) — The current redaction reasons applied to the view hierarchy.
- [RedactionReasons](../redactionreasons.md) — The reasons to apply a redaction to data displayed on screen.
