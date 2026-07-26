---
title: 'formatted(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/personnamecomponents/formatted(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponents/formatted(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponents/formatted%28_%3A%29.json'
content_hash: 'sha256:db41da631ffd37d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PersonNameComponents](../personnamecomponents.md)

# formatted(_:)

<sub>Instance Method</sub>

Generates a locale-aware string representation of an instance of person name components using the provided format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted<S>(_ style: S) -> S.FormatOutput where S : FormatStyle, S.FormatInput == PersonNameComponents
```

## Parameters

- `style` — Specifies the [FormatStyle](formatstyle.md) applied to the person name components.

## Return Value

A string, formatted according to the provided style.

## Discussion

Use the [formatted(_:)](<formatted(__).md>) method to create a string representation of a person’s name with a customized length for specific uses. You can use the [FormatStyle](formatstyle.md) static factory method [name(style:)](<../formatstyle/name(style_).md>) to create a custom format style as a parameter to the method.

For example:

```swift
var tlc = PersonNameComponents()
tlc.familyName = "Clark"
tlc.givenName = "Thomas"
tlc.middleName = "Louis"
tlc.namePrefix = "Dr."
tlc.nickname = "Tom"
tlc.nameSuffix = "Esq."

tlc.formatted(.name(style: .long))
// Dr. Thomas Louis Clark Esq.

tlc.formatted(.name(style: .medium))
// Thomas Clark

tlc.formatted(.name(style: .short))
// Tom

tlc.formatted(.name(style: .abbreviated))
// TC
```

## See Also

### Formatting Person Name Components

- [formatted()](<formatted().md>) — Generates a locale-aware string representation of an instance of person name components using the default format style.
- [FormatStyle](formatstyle.md) — A type used to format a person’s name with a style appropriate for the given locale.
