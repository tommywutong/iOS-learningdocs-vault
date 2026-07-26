---
title: 'init(_:as:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regex/init(_:as:)-2ucu7'
source_url: 'https://developer.apple.com/documentation/swift/regex/init(_:as:)-2ucu7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/init%28_%3Aas%3A%29-2ucu7.json'
content_hash: 'sha256:3d0953e38281ca31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# init(_:as:)

<sub>Initializer</sub>

Creates a regular expression with a strongly-typed capture list from the given regular expression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ regex: Regex<AnyRegexOutput>, as outputType: Output.Type = Output.self)
```

## Parameters

- `regex` — A regular expression to convert to use a strongly-typed capture list.

- `outputType` — The capture structure to use.

## Discussion

You can use this initializer to convert a regular expression with a dynamic capture list to one with a strongly-typed capture list. If the type you provide as `outputType` doesn’t match the capture structure of `regex`, the initializer returns `nil`.

```swift
let dynamicRegex = try Regex("(.+?): (.+)")
if let stronglyTypedRegex = Regex(dynamicRegex, as: (Substring, Substring, Substring).self) {
    print("Converted properly")
}
// Prints "Converted properly"
```
