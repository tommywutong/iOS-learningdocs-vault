---
title: 'firstMatch(in:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regex/firstmatch(in:)-45hz7'
source_url: 'https://developer.apple.com/documentation/swift/regex/firstmatch(in:)-45hz7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/firstmatch%28in%3A%29-45hz7.json'
content_hash: 'sha256:3e2eca8cadb2db1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# firstMatch(in:)

<sub>Instance Method</sub>

Returns the first match for this regex found in the given substring.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func firstMatch(in string: Substring) throws -> Regex<Output>.Match?
```

## Parameters

- `string` — The substring to match this regular expression against.

## Return Value

The match, if one is found; otherwise, `nil`.

## Discussion

Use the `firstMatch(in:)` method to search for the first occurrence of this regular expression in `string`. This example searches for the first sequence of digits that occurs in a string:

```swift
let digits = /[0-9]+/

if let digitsMatch = try digits.firstMatch(in: "The year is 2022; last year was 2021.") {
    print(digitsMatch.0)
} else {
    print("No match.")
}
// Prints "2022"
```

The `firstMatch(in:)` method can throw an error if this regex includes a transformation closure that throws an error.
