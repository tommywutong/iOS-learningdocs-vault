---
title: recoveryAttempter
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nserror/recoveryattempter
source_url: 'https://developer.apple.com/documentation/foundation/nserror/recoveryattempter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nserror/recoveryattempter.json'
content_hash: 'sha256:2b5ab52b4512d751'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSError](../nserror.md)

# recoveryAttempter

<sub>Instance Property</sub>

The object in the user info dictionary corresponding to the [NSRecoveryAttempterErrorKey](../nsrecoveryattemptererrorkey.md) key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var recoveryAttempter: Any? { get }
```

## Discussion

The recovery attempter must be an instance of a class that conforms to the [NSSecureCoding](../nssecurecoding.md) and NSErrorRecoveryAttempting protocols. It must also be able to correctly interpret an index in the [localizedRecoveryOptions](localizedrecoveryoptions.md) property.

If [userInfo](userinfo.md) doesn’t contain a value for [NSRecoveryAttempterErrorKey](../nsrecoveryattemptererrorkey.md), this property is `nil`.

## See Also

### Related Documentation

- [localizedRecoveryOptions](localizedrecoveryoptions.md) — An array containing the localized titles of buttons appropriate for displaying in an alert panel.

### Getting the Error Recovery Attempter

- [NSErrorRecoveryAttempting](../nserrorrecoveryattempting.md) — A set of methods that provide options to recover from an error.
