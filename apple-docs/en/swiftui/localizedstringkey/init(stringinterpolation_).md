---
title: 'init(stringInterpolation:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/localizedstringkey/init(stringinterpolation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/localizedstringkey/init(stringinterpolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/localizedstringkey/init%28stringinterpolation%3A%29.json'
content_hash: 'sha256:03f6de89536d04ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LocalizedStringKey](../localizedstringkey.md)

# init(stringInterpolation:)

<sub>Initializer</sub>

Creates a localized string key from the given string interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(stringInterpolation: LocalizedStringKey.StringInterpolation)
```

## Parameters

- `stringInterpolation` — The string interpolation to use as the localization key.

## Discussion

To create a localized string key from a string interpolation, use the `\()` string interpolation syntax. Swift matches the parameter types in the expression to one of the `appendInterpolation` methods in [StringInterpolation](stringinterpolation.md). The interpolated types can include numeric values, Foundation types, and SwiftUI [Text](../text.md) and [Image](../image.md) instances.

The following example uses a string interpolation with two arguments: an unlabeled [Date](../../foundation/date.md) and a [DateStyle](../text/datestyle.md) labeled `style`. The compiler maps these to the method [appendInterpolation(_:style:)](<stringinterpolation/appendinterpolation(__style_).md>) as it builds the string that it creates the [LocalizedStringKey](../localizedstringkey.md) with.

```swift
let key = LocalizedStringKey("Date is \(company.foundedDate, style: .offset)")
let text = Text(key) // Text contains "Date is +45 years"
```

You can write this example more concisely, implicitly creating a [LocalizedStringKey](../localizedstringkey.md) as the parameter to the [Text](../text.md) initializer:

```swift
let text = Text("Date is \(company.foundedDate, style: .offset)")
```

## See Also

### Creating a key from an interpolation

- [StringInterpolation](stringinterpolation.md) — Represents the contents of a string literal with interpolations while it’s being built, for use in creating a localized string key.
