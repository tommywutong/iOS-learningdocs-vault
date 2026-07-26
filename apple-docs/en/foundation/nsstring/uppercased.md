---
title: uppercased
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/uppercased
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/uppercased'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/uppercased.json'
content_hash: 'sha256:eefc8d88529e4448'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# uppercased

<sub>Instance Property</sub>

An uppercase representation of the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var uppercased: String { get }
```

## Discussion

This property performs the canonical (non-localized) mapping. It is suitable for programming operations that require stable results not depending on the current locale.

Case transformations aren’t guaranteed to be symmetrical or to produce strings of the same lengths as the originals. See [lowercaseString](lowercased.md) for an example.

> [!important] Important
> When working with text that’s presented to the user, use [localizedUppercaseString](localizeduppercase.md) or [- uppercaseStringWithLocale:](<uppercased(with_).md>) instead.

## See Also

### Changing Case

- [lowercaseString](lowercased.md) — A lowercase representation of the string.
- [localizedLowercaseString](localizedlowercase.md) — Returns a version of the string with all letters converted to lowercase, taking into account the current locale.
- [- lowercaseStringWithLocale:](<lowercased(with_).md>) — Returns a version of the string with all letters converted to lowercase, taking into account the specified locale.
- [localizedUppercaseString](localizeduppercase.md) — Returns a version of the string with all letters converted to uppercase, taking into account the current locale.
- [- uppercaseStringWithLocale:](<uppercased(with_).md>) — Returns a version of the string with all letters converted to uppercase, taking into account the specified locale.
- [capitalizedString](capitalized.md) — A capitalized representation of the string.
- [localizedCapitalizedString](localizedcapitalized.md) — Returns a capitalized representation of the receiver using the current locale.
- [- capitalizedStringWithLocale:](<capitalized(with_).md>) — Returns a capitalized representation of the receiver using the specified locale.
