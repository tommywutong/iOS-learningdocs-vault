---
title: 'init(pattern:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsregularexpression/init(pattern:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/init(pattern:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/init%28pattern%3Aoptions%3A%29.json'
content_hash: 'sha256:08fdacb736eac873'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRegularExpression](../nsregularexpression.md)

# init(pattern:options:)

<sub>Initializer</sub>

Returns an initialized NSRegularExpression instance with the specified regular expression pattern and options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(pattern: String, options: NSRegularExpression.Options = []) throws
```

## Parameters

- `pattern` — The regular expression pattern to compile.

- `options` — The regular expression options that are applied to the expression during matching. See [Options](options-swift.struct.md) for possible values.

## Return Value

An instance of `NSRegularExpression` for the specified regular expression and options.

## Discussion

> [!note] Handling Errors in Swift
> In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.
