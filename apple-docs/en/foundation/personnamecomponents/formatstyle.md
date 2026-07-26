---
title: PersonNameComponents.FormatStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/personnamecomponents/formatstyle
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponents/formatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponents/formatstyle.json'
content_hash: 'sha256:4d247840585ff1d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PersonNameComponents](../personnamecomponents.md)

# PersonNameComponents.FormatStyle

<sub>Structure</sub>

A type used to format a person’s name with a style appropriate for the given locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FormatStyle
```

## Overview

Personal names deserve careful and respectful treatment in your apps. Each locale has its own set of rules and conventions to construct and represent personal names. These rules vary widely across different locales in several ways, including the sort and display order of given and family names, the use of salutations and honorifics, and other concerns related to the grammar, spelling, punctuation, and formatting.

A `PersonNameComponents.FormatStyle` creates human readable text from an instance of [PersonNameComponents](../personnamecomponents.md). You can customize the formatting using the [style](formatstyle/style-swift.property.md) and [locale](formatstyle/locale.md) properties. The system automatically caches instances with unique configurations of the format style to enhance performance.

### Format Styles

You can configure a `PersonNameComponents.FormatStyle` to represent names in a variety of styles:

- Long ([PersonNameComponents.FormatStyle.Style.long](formatstyle/style-swift.enum/long.md))
- Medium ([PersonNameComponents.FormatStyle.Style.medium](formatstyle/style-swift.enum/medium.md))
- Short ([PersonNameComponents.FormatStyle.Style.short](formatstyle/style-swift.enum/short.md))
- Abbreviated ([PersonNameComponents.FormatStyle.Style.abbreviated](formatstyle/style-swift.enum/abbreviated.md))

When determining how to represent a name in a particular style, a number of factors determine the final format. In order of priority:

1. Script derived behaviors — Scripts may specify a strict sort or display order of given and family names, and the availability of styles. The format style assigns an “Unknown” script, which has its own set of behaviors and characteristics, to a name that contains more than one script (for example, given name: John; family name: 王).
2. User specified preferences —  Users can enable and configure the display of short names, as well as whether to display nicknames when available. Users can also override the default sort and display order of given and family names for their current locale.
3. Locale derived defaults — Locales specify a default sort and display order for given and family names.
4. Developer specified configuration — The style property value set for the `PersonNameComponent.FormatStyle`.

In the case of a conflict, the format style uses the factor with the highest precedence. For example, the U.S. English (`en-US`) style formats names in “given name followed by the family name” (for example, Anne Johnson). This behavior would be overridden if the user changed their system preferences to have names displayed as family name followed by given name (for example, Johnson, Anne), because user-specified preferences take precedence over locale-derived defaults. Furthermore, if the name to be formatted were Japanese (for example, given name: 泰夫; family name: 木田), the behavior derived for the name’s script (CJK, for Chinese, Japanese, and Korean languages) would take precedence over any locale-derived defaults or user-specified preferences to have the name displayed as family name followed by given name (for example, 木田 泰夫).

These considerations extend to the availability of certain format styles as well. Because developer-specified configurations have the lowest precedence, the value set for the formatter’s style property is invalidated if it isn’t supported for the locale, user preferences, or script. If the specified style isn’t available, it uses the next longest valid style. For example, a name in Arabic script (for example, أحمد الراجحي) doesn’t support the Abbreviated style, so it uses the Short style instead.

For more information and examples, see [style](formatstyle/style-swift.property.md).

### Formatting Person Name Components

Use either [formatted()](<formatted().md>) or [formatted(_:)](<formatted(__).md>), both instance methods of [PersonNameComponents](../personnamecomponents.md), to create a string representation of a name.

The [formatted()](<../../swift/sequence/formatted().md>) method to applies the default format style to a name. For example:

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

The [formatted(_:)](<formatted(__).md>) method applies a custom format style to a name. You can use the static factory method [name(style:)](<../formatstyle/name(style_).md>) to create a custom format style as a parameter to the method. For example:

```swift
tlc.formatted(.name(style: .long))
// Dr. Thomas Louis Clark Esq.

tlc.formatted(.name(style: .medium))
// Thomas Clark

tlc.formatted(.name(style: .short))
// Tom

tlc.formatted(.name(style: .abbreviated))
// TC
```

You can create and reuse a format style instance to format multiple names. For example:

```swift
let customPersonFormatStyle = PersonNameComponents.FormatStyle(style: .medium, locale: Locale(identifier: "en_US"))

tlc.formatted(customPersonFormatStyle)
// Thomas Clark

mlr.formatted(customPersonFormatStyle)
// Maria Ruiz
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [FormatStyle](../formatstyle.md), [Hashable](../../swift/hashable.md), [ParseableFormatStyle](../parseableformatstyle.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a Format Style

- [init(style:locale:)](<formatstyle/init(style_locale_).md>) — Creates an instance using the provided format style and locale.

### Parsing Person Name Components

- [init(_:)](<init(__).md>) — Creates a person name components object from a given string.
- [init(_:strategy:)](<init(__strategy_).md>) — Creates a person name components object from a given string by applying the provided parsing strategy.
- [parseStrategy](formatstyle/parsestrategy.md) — The strategy used to parse a string into person name components.

### Modifying a Format Style

- [style](formatstyle/style-swift.property.md) — Specifies the style of the formatted result.
- [Style](formatstyle/style-swift.enum.md) — The type that represents the style of the formatted result.
- [locale](formatstyle/locale.md) — The locale to use when formatting the person name components.
- [attributed](formatstyle/attributed.md) — The style used to create a locale-aware attributed string representation of an instance of person name components.
- [locale(_:)](<formatstyle/locale(__).md>) — Modifies the person name components format style to use the specified locale.

### Applying a Format Style

- [format(_:)](<formatstyle/format(__).md>) — Creates a string representation from a person name components value.

### Default Implementations

- [ParseableFormatStyle Implementations](formatstyle/parseableformatstyle-implementations.md)

## See Also

### Formatting Person Name Components

- [formatted()](<formatted().md>) — Generates a locale-aware string representation of an instance of person name components using the default format style.
- [formatted(_:)](<formatted(__).md>) — Generates a locale-aware string representation of an instance of person name components using the provided format style.
