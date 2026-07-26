---
title: 'name(style:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/parseableformatstyle/name(style:)'
source_url: 'https://developer.apple.com/documentation/foundation/parseableformatstyle/name(style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/parseableformatstyle/name%28style%3A%29.json'
content_hash: 'sha256:bdf71abcdcd503d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ParseableFormatStyle](../parseableformatstyle.md)

# name(style:)

<sub>Type Method</sub>

Returns a format style to use the given name style for formatting a name from its components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func name(style: PersonNameComponents.FormatStyle.Style) -> Self
```

## Parameters

- `style` — A name-formatting style, such as [PersonNameComponents.FormatStyle.Style.long](../personnamecomponents/formatstyle/style-swift.enum/long.md) or [PersonNameComponents.FormatStyle.Style.abbreviated](../personnamecomponents/formatstyle/style-swift.enum/abbreviated.md).

## Return Value

A name format style.

## Discussion

Use the dot-notation form of this type method when the call point allows the use of [FormatStyle](../personnamecomponents/formatstyle.md). You typically do this when calling the [formatted(_:)](<../personnamecomponents/formatted(__).md>) method of [PersonNameComponents](../personnamecomponents.md).

The following example shows the effect of creating and using different person name format styles.

```swift
let name = PersonNameComponents(namePrefix: "Dr.",
                                givenName: "Thomas",
                                middleName: "Louis",
                                familyName: "Clark",
                                nameSuffix: "Jr.",
                                nickname: "Tom")
let longFormattedName = name.formatted(.name(style: .long)) // "Dr. Thomas Louis Clark Jr."
let mediumFormattedName = name.formatted(.name(style: .medium)) // "Thomas Clark"
let shortFormattedName = name.formatted(.name(style: .short)) // "Tom"
let abbreviatedFormattedName = name.formatted(.name(style: .abbreviated)) // "TC"
```
