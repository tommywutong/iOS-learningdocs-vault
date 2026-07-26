---
title: 'readLine(strippingNewline:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/readline(strippingnewline:)'
source_url: 'https://developer.apple.com/documentation/swift/readline(strippingnewline:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/readline%28strippingnewline%3A%29.json'
content_hash: 'sha256:df7df8ee2fe7a98f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# readLine(strippingNewline:)

<sub>Function</sub>

Returns a string read from standard input through the end of the current line or until EOF is reached.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func readLine(strippingNewline: Bool = true) -> String?
```

## Parameters

- `strippingNewline` — If `true`, newline characters and character combinations are stripped from the result; otherwise, newline characters or character combinations are preserved. The default is `true`.

## Return Value

The string of characters read from standard input. If EOF has already been reached when `readLine()` is called, the result is `nil`.

## Discussion

Standard input is interpreted as `UTF-8`. Invalid bytes are replaced by Unicode [replacement characters](https://unicode.org/glossary/#replacement_character).

## See Also

### Command Line Input

- [CommandLine](commandline.md) — Command-line arguments for the current process.
