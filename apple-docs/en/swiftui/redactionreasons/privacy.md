---
title: privacy
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/redactionreasons/privacy
source_url: 'https://developer.apple.com/documentation/swiftui/redactionreasons/privacy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/redactionreasons/privacy.json'
content_hash: 'sha256:32fb669a8fb1b40f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [RedactionReasons](../redactionreasons.md)

# privacy

<sub>Type Property</sub>

Displayed data should be obscured to protect private information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let privacy: RedactionReasons
```

## Discussion

Views marked with [privacySensitive(_:)](<../view/privacysensitive(__).md>) will be automatically redacted using a standard styling. To apply a custom treatment the redaction reason can be read out of the environment.

```swift
struct BankingContentView: View {
    @Environment(\.redactionReasons) var redactionReasons

    var body: some View {
        if redactionReasons.contains(.privacy) {
            FullAppCover()
        } else {
            AppContent()
        }
    }
}
```

## See Also

### Getting redaction reasons

- [invalidated](invalidated.md) — Displayed data should appear as invalidated and pending a new update.
- [placeholder](placeholder.md) — Displayed data should appear as generic placeholders.
