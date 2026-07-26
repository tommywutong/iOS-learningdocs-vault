---
title: suggestedInvocationPhrase
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/suggestedinvocationphrase
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/suggestedinvocationphrase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/suggestedinvocationphrase.json'
content_hash: 'sha256:f472fb27ba9937d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# suggestedInvocationPhrase

<sub>Instance Property</sub>

A phrase suggested to the user when they create a shortcut.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var suggestedInvocationPhrase: String? { get set }
```

## Discussion

The system displays the suggested invocation phrase to the user when they create the shortcut. Use a short, memorable phrase, such as “Soup time”.

![A screenshot of adding a shortcut to Siri for one order of tomato soup.](../../../../attachments/8ba32c1cccce9885aad9bc8ebc40e79e/media-3020431@2x.png)

> [!note] Note
> To access the [suggestedInvocationPhrase](suggestedinvocationphrase.md) property, import the _Intents_ framework.

## See Also

### Providing SiriKit with activity details

- [interaction](interaction.md) — The SiriKit interaction object to use when configuring your app.
- [shortcutAvailability](shortcutavailability.md) — A set of defined contexts in which an intent or activity might be relevant to a user.
