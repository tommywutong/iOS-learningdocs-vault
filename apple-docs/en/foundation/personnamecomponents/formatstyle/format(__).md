---
title: 'format(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/personnamecomponents/formatstyle/format(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponents/formatstyle/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponents/formatstyle/format%28_%3A%29.json'
content_hash: 'sha256:11e5fd3e6cca8a10'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [PersonNameComponents](../../personnamecomponents.md) · [FormatStyle](../formatstyle.md)

# format(_:)

<sub>Instance Method</sub>

Creates a string representation from a person name components value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ value: PersonNameComponents) -> String
```

## Parameters

- `value` — The person name components object to format.

## Return Value

A string representation of the person name components.

## Discussion

The [format(_:)](<format(__).md>) instance method applies the style to an instance of `PersonNameComponent`. After creating a style, you can use it to format multiple instances of person name components. For example:

```swift
let customPersonFormatStyle = PersonNameComponents.FormatStyle(style: .medium, locale: Locale(identifier: "us_EN"))

var person1 = PersonNameComponents()
person1.familyName = "Clark"
person1.givenName = "Thomas"
person1.middleName = "Louis"
person1.namePrefix = "Dr."
person1.nickname = "Tom"
person1.nameSuffix = "Esq."

let customPersonString1 = 
customPersonFormatStyle.format(person1)
// Thomas Clark

let customPersonString2 = 
customPersonFormatStyle.format(person2)
// Maria Ruiz
```
