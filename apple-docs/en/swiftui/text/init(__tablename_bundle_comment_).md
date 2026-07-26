---
title: 'init(_:tableName:bundle:comment:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/init(_:tablename:bundle:comment:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/init(_:tablename:bundle:comment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/init%28_%3Atablename%3Abundle%3Acomment%3A%29.json'
content_hash: 'sha256:b9c87f8fe8acf754'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# init(_:tableName:bundle:comment:)

<sub>Initializer</sub>

Creates a text view that displays localized content identified by a key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ key: LocalizedStringKey, tableName: String? = nil, bundle: Bundle? = nil, comment: StaticString? = nil)
```

## Parameters

- `key` — The key for a string in the table identified by `tableName`.

- `tableName` — The name of the string table to search. If `nil`, use the table in the `Localizable.strings` file.

- `bundle` — The bundle containing the strings file. If `nil`, use the main bundle.

- `comment` — Contextual information about this key-value pair.

## Discussion

Use this initializer to look for the `key` parameter in a localization table and display the associated string value in the initialized text view. If the initializer can’t find the key in the table, or if no table exists, the text view displays the string representation of the key instead.

```swift
Text("pencil") // Localizes the key if possible, or displays "pencil" if not.
```

When you initialize a text view with a string literal, the view triggers this initializer because it assumes you want the string localized, even when you don’t explicitly specify a table, as in the above example. If you haven’t provided localization for a particular string, you still get reasonable behavior, because the initializer displays the key, which typically contains the unlocalized string.

If you initialize a text view with a string variable rather than a string literal, the view triggers the [init(_:)](<init(__)-9d1g4.md>) initializer instead, because it assumes that you don’t want localization in that case. If you do want to localize the value stored in a string variable, you can choose to call the `init(_:tableName:bundle:comment:)` initializer by first creating a [LocalizedStringKey](../localizedstringkey.md) instance from the string variable:

```swift
Text(LocalizedStringKey(someString)) // Localizes the contents of `someString`.
```

If you have a string literal that you don’t want to localize, use the [init(verbatim:)](<init(verbatim_).md>) initializer instead.

### Styling localized strings with markdown

If the localized string or the fallback key contains Markdown, the view displays the text with appropriate styling. For example, consider an app with the following entry in its Spanish localization file:

```swift
"_Please visit our [website](https://www.example.com)._" = "_Visita nuestro [sitio web](https://www.example.com)._";
```

You can create a `Text` view with the Markdown-formatted base language version of the string as the localization key, like this:

```swift
Text("_Please visit our [website](https://www.example.com)._")
```

When viewed in a Spanish locale, the view uses the Spanish text from the strings file, applying the Markdown styling.

![A text view that says Visita nuestro sitio web, with all text](../../../../attachments/49483ef3dd9a6c9cd4fb66cf99757e69/SwiftUI-Text-init-localized@2x.png)

> [!important] Important
> `Text` doesn’t render all styling possible in Markdown. It doesn’t support line breaks, soft breaks, or any style of paragraph- or block-based formatting like lists, block quotes, code blocks, or tables. It also doesn’t support the [imageURL](../../foundation/attributescopes/foundationattributes/imageurl.md) attribute. Parsing with SwiftUI treats any whitespace in the Markdown string as described by the [AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnlyPreservingWhitespace](../../foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/inlineonlypreservingwhitespace.md) parsing option.

## See Also

### Creating a text view

- [init(_:)](<init(__).md>) — Creates a text view that displays styled attributed content.
- [init(verbatim:)](<init(verbatim_).md>) — Creates a text view that displays a string literal without localization.
- [init(_:style:)](<init(__style_).md>) — Creates an instance that displays localized dates and times using a specific style.
- [init(_:format:)](<init(__format_).md>) — Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.
- [init(_:formatter:)](<init(__formatter_).md>) — Creates a text view that displays the formatted representation of a Foundation object.
- [init(timerInterval:pauseTime:countsDown:showsHours:)](<init(timerinterval_pausetime_countsdown_showshours_).md>) — Creates an instance that displays a timer counting within the provided interval.
