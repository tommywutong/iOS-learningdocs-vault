---
title: 'uppercased(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/uppercased(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/uppercased(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/uppercased%28with%3A%29.json'
content_hash: 'sha256:26ddc7c95fdf3617'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# uppercased(with:)

<sub>Instance Method</sub>

Returns a version of the string with all letters converted to uppercase, taking into account the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func uppercased(with locale: Locale?) -> String
```

## Parameters

- `locale` — The locale. For strings presented to users, pass the current locale ([[NSLocale](../nslocale.md) [currentLocale](../nslocale/current.md)]). To use the system locale, pass `nil`.

## Return Value

An uppercase string using the `locale`.

## See Also

### Changing Case

- [lowercaseString](lowercased.md) — A lowercase representation of the string.
- [localizedLowercaseString](localizedlowercase.md) — Returns a version of the string with all letters converted to lowercase, taking into account the current locale.
- [- lowercaseStringWithLocale:](<lowercased(with_).md>) — Returns a version of the string with all letters converted to lowercase, taking into account the specified locale.
- [uppercaseString](uppercased.md) — An uppercase representation of the string.
- [localizedUppercaseString](localizeduppercase.md) — Returns a version of the string with all letters converted to uppercase, taking into account the current locale.
- [capitalizedString](capitalized.md) — A capitalized representation of the string.
- [localizedCapitalizedString](localizedcapitalized.md) — Returns a capitalized representation of the receiver using the current locale.
- [- capitalizedStringWithLocale:](<capitalized(with_).md>) — Returns a capitalized representation of the receiver using the specified locale.
