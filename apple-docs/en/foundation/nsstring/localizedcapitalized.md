---
title: localizedCapitalized
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/localizedcapitalized
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/localizedcapitalized'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/localizedcapitalized.json'
content_hash: 'sha256:b0be2c65d32a191e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# localizedCapitalized

<sub>Instance Property</sub>

Returns a capitalized representation of the receiver using the current locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var localizedCapitalized: String { get }
```

## Discussion

A capitalized string is a string with the first character in each word changed to its corresponding uppercase value, and all remaining characters set to their corresponding lowercase values. A “word” is any sequence of characters delimited by spaces, tabs, or line terminators (listed under [- getLineStart:end:contentsEnd:forRange:](<getlinestart(__end_contentsend_for_).md>)). Some common word delimiting punctuation isn’t considered, so this property may not generally produce the desired results for multiword strings.

Case transformations aren’t guaranteed to be symmetrical or to produce strings of the same lengths as the originals. See [lowercaseString](lowercased.md) for an example.

## See Also

### Changing Case

- [lowercaseString](lowercased.md) — A lowercase representation of the string.
- [localizedLowercaseString](localizedlowercase.md) — Returns a version of the string with all letters converted to lowercase, taking into account the current locale.
- [- lowercaseStringWithLocale:](<lowercased(with_).md>) — Returns a version of the string with all letters converted to lowercase, taking into account the specified locale.
- [uppercaseString](uppercased.md) — An uppercase representation of the string.
- [localizedUppercaseString](localizeduppercase.md) — Returns a version of the string with all letters converted to uppercase, taking into account the current locale.
- [- uppercaseStringWithLocale:](<uppercased(with_).md>) — Returns a version of the string with all letters converted to uppercase, taking into account the specified locale.
- [capitalizedString](capitalized.md) — A capitalized representation of the string.
- [- capitalizedStringWithLocale:](<capitalized(with_).md>) — Returns a capitalized representation of the receiver using the specified locale.
