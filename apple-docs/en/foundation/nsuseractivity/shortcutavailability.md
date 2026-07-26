---
title: shortcutAvailability
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/shortcutavailability
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/shortcutavailability'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/shortcutavailability.json'
content_hash: 'sha256:8b5bec1a4daf174c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# shortcutAvailability

<sub>Instance Property</sub>

A set of defined contexts in which an intent or activity might be relevant to a user.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
var shortcutAvailability: INShortcutAvailabilityOptions { get set }
```

## Discussion

When you donate an activity, include a set of relevant [INShortcutAvailabilityOptions](../../intents/inshortcutavailabilityoptions.md) to describe appropriate categories for offering a shortcut to the activity.

If none of the availability options apply to your intent, use the empty set. The empty set is the default value for this property.

> [!note] Note
> To access the `suggestedInvocationPhrase` property, import the Intents framework.

## See Also

### Providing SiriKit with activity details

- [interaction](interaction.md) — The SiriKit interaction object to use when configuring your app.
- [suggestedInvocationPhrase](suggestedinvocationphrase.md) — A phrase suggested to the user when they create a shortcut.
