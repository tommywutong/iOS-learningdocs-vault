---
title: 'privacySensitive(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/privacysensitive(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/privacysensitive(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/privacysensitive%28_%3A%29.json'
content_hash: 'sha256:099bf62b46d9e71b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# privacySensitive(_:)

<sub>Instance Method</sub>

Marks the view as containing sensitive, private user data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func privacySensitive(_ sensitive: Bool = true) -> some View

```

## Discussion

SwiftUI redacts views marked with this modifier when you apply the [privacy](../redactionreasons/privacy.md) redaction reason.

```swift
struct BankAccountView: View {
    var body: some View {
        VStack {
            Text("Account #")

            Text(accountNumber)
                .font(.headline)
                .privacySensitive() // Hide only the account number.
        }
    }
}
```

## See Also

### Redacting private content

- [Designing your app for the Always On state](../../watchos-apps/designing-your-app-for-the-always-on-state.md) — Customize your watchOS app’s user interface for continuous display.
- [Protecting sensitive content when screen sharing and remote control are active](../protecting-sensitive-content-when-screen-sharing.md) — Detect active screen capture sessions and respond appropriately to protect sensitive content in your app.
- [redacted(reason:)](<redacted(reason_).md>) — Adds a reason to apply a redaction to this view hierarchy.
- [unredacted()](<unredacted().md>) — Removes any reason to apply a redaction to this view hierarchy.
- [redactionReasons](../environmentvalues/redactionreasons.md) — The current redaction reasons applied to the view hierarchy.
- [isSceneCaptured](../environmentvalues/isscenecaptured.md) — The current capture state.
- [RedactionReasons](../redactionreasons.md) — The reasons to apply a redaction to data displayed on screen.
