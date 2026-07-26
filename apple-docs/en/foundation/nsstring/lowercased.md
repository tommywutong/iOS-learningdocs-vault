---
title: lowercased
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/lowercased
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/lowercased'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/lowercased.json'
content_hash: 'sha256:ac9034616ec303bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# lowercased

<sub>Instance Property</sub>

A lowercase representation of the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var lowercased: String { get }
```

## Discussion

This property performs the canonical (non-localized) mapping. It is suitable for programming operations that require stable results not depending on the current locale.

Case transformations aren’t guaranteed to be symmetrical or to produce strings of the same lengths as the originals. That is, the result of this statement:

```objc
lcString = [myString lowercaseString];
```

…might not be equal to this statement:

```objc
lcString = [[myString uppercaseString] lowercaseString];
```

For example, the uppercase form of “ß” in German is “SS”, so converting “Straße” to uppercase, then lowercase, produces this sequence of strings:

- “Straße”
- “STRASSE”
- “strasse”

> [!important] Important
> When working with text that’s presented to the user, use [localizedLowercaseString](localizedlowercase.md) or [- lowercaseStringWithLocale:](<lowercased(with_).md>) instead.

## See Also

### Changing Case

- [localizedLowercaseString](localizedlowercase.md) — Returns a version of the string with all letters converted to lowercase, taking into account the current locale.
- [- lowercaseStringWithLocale:](<lowercased(with_).md>) — Returns a version of the string with all letters converted to lowercase, taking into account the specified locale.
- [uppercaseString](uppercased.md) — An uppercase representation of the string.
- [localizedUppercaseString](localizeduppercase.md) — Returns a version of the string with all letters converted to uppercase, taking into account the current locale.
- [- uppercaseStringWithLocale:](<uppercased(with_).md>) — Returns a version of the string with all letters converted to uppercase, taking into account the specified locale.
- [capitalizedString](capitalized.md) — A capitalized representation of the string.
- [localizedCapitalizedString](localizedcapitalized.md) — Returns a capitalized representation of the receiver using the current locale.
- [- capitalizedStringWithLocale:](<capitalized(with_).md>) — Returns a capitalized representation of the receiver using the specified locale.
