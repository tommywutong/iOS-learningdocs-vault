---
title: 'redacted(reason:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/redacted(reason:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/redacted(reason:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/redacted%28reason%3A%29.json'
content_hash: 'sha256:68c505098e90e4e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# redacted(reason:)

<sub>Instance Method</sub>

Adds a reason to apply a redaction to this view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func redacted(reason: RedactionReasons) -> some View

```

## Discussion

Adding a redaction is an additive process: any redaction provided will be added to the reasons provided by the parent.

## See Also

### Redacting private content

- [Designing your app for the Always On state](../../watchos-apps/designing-your-app-for-the-always-on-state.md) — Customize your watchOS app’s user interface for continuous display.
- [Protecting sensitive content when screen sharing and remote control are active](../protecting-sensitive-content-when-screen-sharing.md) — Detect active screen capture sessions and respond appropriately to protect sensitive content in your app.
- [privacySensitive(_:)](<privacysensitive(__).md>) — Marks the view as containing sensitive, private user data.
- [unredacted()](<unredacted().md>) — Removes any reason to apply a redaction to this view hierarchy.
- [redactionReasons](../environmentvalues/redactionreasons.md) — The current redaction reasons applied to the view hierarchy.
- [isSceneCaptured](../environmentvalues/isscenecaptured.md) — The current capture state.
- [RedactionReasons](../redactionreasons.md) — The reasons to apply a redaction to data displayed on screen.
