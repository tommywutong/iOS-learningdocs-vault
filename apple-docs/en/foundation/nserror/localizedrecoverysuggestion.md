---
title: localizedRecoverySuggestion
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nserror/localizedrecoverysuggestion
source_url: 'https://developer.apple.com/documentation/foundation/nserror/localizedrecoverysuggestion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nserror/localizedrecoverysuggestion.json'
content_hash: 'sha256:ac997f819977c298'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSError](../nserror.md)

# localizedRecoverySuggestion

<sub>Instance Property</sub>

A string containing the localized recovery suggestion for the error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var localizedRecoverySuggestion: String? { get }
```

## Discussion

The object in the user info dictionary for the key [NSLocalizedRecoverySuggestionErrorKey](../nslocalizedrecoverysuggestionerrorkey.md). If the user info dictionary doesn’t contain a value for [NSLocalizedRecoverySuggestionErrorKey](../nslocalizedrecoverysuggestionerrorkey.md), this property is `nil`.

The returned string is suitable for displaying as the secondary message in an alert panel.

## See Also

### Getting a Localized Error Description

- [localizedDescription](localizeddescription.md) — A string containing the localized description of the error.
- [localizedRecoveryOptions](localizedrecoveryoptions.md) — An array containing the localized titles of buttons appropriate for displaying in an alert panel.
- [localizedFailureReason](localizedfailurereason.md) — A string containing the localized explanation of the reason for the error.
