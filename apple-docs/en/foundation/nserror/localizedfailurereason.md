---
title: localizedFailureReason
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nserror/localizedfailurereason
source_url: 'https://developer.apple.com/documentation/foundation/nserror/localizedfailurereason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nserror/localizedfailurereason.json'
content_hash: 'sha256:5b236f7624dbeef4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSError](../nserror.md)

# localizedFailureReason

<sub>Instance Property</sub>

A string containing the localized explanation of the reason for the error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var localizedFailureReason: String? { get }
```

## Discussion

The object in the user info dictionary for the key [NSLocalizedFailureReasonErrorKey](../nslocalizedfailurereasonerrorkey.md).

## See Also

### Related Documentation

- [domain](domain.md) — A string containing the error domain.
- [code](code.md) — The error code.
- [userInfo](userinfo.md) — The user info dictionary.

### Getting a Localized Error Description

- [localizedDescription](localizeddescription.md) — A string containing the localized description of the error.
- [localizedRecoveryOptions](localizedrecoveryoptions.md) — An array containing the localized titles of buttons appropriate for displaying in an alert panel.
- [localizedRecoverySuggestion](localizedrecoverysuggestion.md) — A string containing the localized recovery suggestion for the error.
