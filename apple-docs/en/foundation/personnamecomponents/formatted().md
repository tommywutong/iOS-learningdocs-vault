---
title: formatted()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/personnamecomponents/formatted()
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponents/formatted()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponents/formatted%28%29.json'
content_hash: 'sha256:7a67e6a1d36579b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PersonNameComponents](../personnamecomponents.md)

# formatted()

<sub>Instance Method</sub>

Generates a locale-aware string representation of an instance of person name components using the default format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted() -> String
```

## Return Value

A string, formatted according to the default style.

## Discussion

The [formatted()](<formatted().md>) method creates a string representation of a person’s name suitable for most uses.

```swift
var tlc = PersonNameComponents()
tlc.familyName = "Clark"
tlc.givenName = "Thomas"
tlc.middleName = "Louis"
tlc.namePrefix = "Dr."
tlc.nickname = "Tom"
tlc.nameSuffix = "Esq."

tlc.formatted()
// Thomas Clark
```

If you want more control over the length and formatting of the name string, consider using the [formatted(_:)](<formatted(__).md>) method and including a format style.

## See Also

### Formatting Person Name Components

- [formatted(_:)](<formatted(__).md>) — Generates a locale-aware string representation of an instance of person name components using the provided format style.
- [FormatStyle](formatstyle.md) — A type used to format a person’s name with a style appropriate for the given locale.
