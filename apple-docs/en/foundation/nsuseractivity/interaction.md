---
title: interaction
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 12.0+, tvOS 14.0+, visionOS 1.0+, watchOS 3.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/interaction
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/interaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/interaction.json'
content_hash: 'sha256:e6946609d1416370'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# interaction

<sub>Instance Property</sub>

The SiriKit interaction object to use when configuring your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var interaction: INInteraction? { get }
```

## Discussion

When SiriKit launches your app, it fills this property with the intent and response information that are the reason for launching your app. Use the information in this property to configure your app’s interface and show any relevant interaction details. If your app wasn’t launched because of a Siri interaction, the value in this property is `nil`.

## See Also

### Providing SiriKit with activity details

- [suggestedInvocationPhrase](suggestedinvocationphrase.md) — A phrase suggested to the user when they create a shortcut.
- [shortcutAvailability](shortcutavailability.md) — A set of defined contexts in which an intent or activity might be relevant to a user.
