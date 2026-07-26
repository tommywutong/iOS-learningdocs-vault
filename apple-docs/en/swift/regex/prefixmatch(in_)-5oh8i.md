---
title: 'prefixMatch(in:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regex/prefixmatch(in:)-5oh8i'
source_url: 'https://developer.apple.com/documentation/swift/regex/prefixmatch(in:)-5oh8i'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/prefixmatch%28in%3A%29-5oh8i.json'
content_hash: 'sha256:5e4f3322a00fae42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# prefixMatch(in:)

<sub>Instance Method</sub>

Returns a match if this regex matches the given string at its start.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func prefixMatch(in string: String) throws -> Regex<Output>.Match?
```

## Parameters

- `string` — The string to match this regular expression against.

## Return Value

The match, if this regex matches at the start of `string`; otherwise, `nil`.

## Discussion

Call this method if you want the regular expression to succeed only when it matches only at the start of the given string. This example uses `prefixMatch(in:)` and a regex that matches a title-case word to search for such a word at the start of different strings:

```swift
let titleCaseWord = /[A-Z][A-Za-z]+/

if let wordMatch = try titleCaseWord.prefixMatch(in: "Searching in a Regex") {
    print(wordMatch.0)
} else {
    print("No match.")
}
// Prints "Searching"

if let wordMatch = try titleCaseWord.prefixMatch(in: "title case word at the End") {
    print(wordMatch.0)
} else {
    print("No match.")
}
// Prints "No match."
```

The `prefixMatch(in:)` method can throw an error if this regex includes a transformation closure that throws an error.
