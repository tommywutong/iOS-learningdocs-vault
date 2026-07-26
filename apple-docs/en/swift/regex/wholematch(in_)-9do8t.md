---
title: 'wholeMatch(in:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regex/wholematch(in:)-9do8t'
source_url: 'https://developer.apple.com/documentation/swift/regex/wholematch(in:)-9do8t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/wholematch%28in%3A%29-9do8t.json'
content_hash: 'sha256:21eb9cc8c9038654'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# wholeMatch(in:)

<sub>Instance Method</sub>

Returns a match if this regex matches the given string in its entirety.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func wholeMatch(in string: String) throws -> Regex<Output>.Match?
```

## Parameters

- `string` — The string to match this regular expression against.

## Return Value

The match, if this regex matches the entirety of `string`; otherwise, `nil`.

## Discussion

Call this method if you want the regular expression to succeed only when it matches the entire string you pass as `string`. The following example shows matching a regular expression that only matches digits, with different candidate strings.

```swift
let digits = /[0-9]+/

if let digitsMatch = try digits.wholeMatch(in: "2022") {
    print(digitsMatch.0)
} else {
    print("No match.")
}
// Prints "2022"

if let digitsMatch = try digits.wholeMatch(in: "The year is 2022.") {
    print(digitsMatch.0)
} else {
    print("No match.")
}
// Prints "No match."
```

The `wholeMatch(in:)` method can throw an error if this regex includes a transformation closure that throws an error.
