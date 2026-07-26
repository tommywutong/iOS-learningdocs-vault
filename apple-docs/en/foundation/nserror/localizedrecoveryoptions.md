---
title: localizedRecoveryOptions
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nserror/localizedrecoveryoptions
source_url: 'https://developer.apple.com/documentation/foundation/nserror/localizedrecoveryoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nserror/localizedrecoveryoptions.json'
content_hash: 'sha256:8f106c40d609d1c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSError](../nserror.md)

# localizedRecoveryOptions

<sub>Instance Property</sub>

An array containing the localized titles of buttons appropriate for displaying in an alert panel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var localizedRecoveryOptions: [String]? { get }
```

## Discussion

The object in the user info dictionary for the key [NSLocalizedRecoveryOptionsErrorKey](../nslocalizedrecoveryoptionserrorkey.md). If the user info dictionary doesn’t contain a value for [NSLocalizedRecoveryOptionsErrorKey](../nslocalizedrecoveryoptionserrorkey.md), this property is `nil`.

The first string is the title of the right-most and default button, the second the one to the left of that, and so on. The recovery options should be appropriate for the  [localizedRecoverySuggestion](localizedrecoverysuggestion.md) property. If the user info dictionary doesn’t contain a value for [NSLocalizedRecoveryOptionsErrorKey](../nslocalizedrecoveryoptionserrorkey.md), only an OK button is displayed.

## See Also

### Getting a Localized Error Description

- [localizedDescription](localizeddescription.md) — A string containing the localized description of the error.
- [localizedRecoverySuggestion](localizedrecoverysuggestion.md) — A string containing the localized recovery suggestion for the error.
- [localizedFailureReason](localizedfailurereason.md) — A string containing the localized explanation of the reason for the error.
