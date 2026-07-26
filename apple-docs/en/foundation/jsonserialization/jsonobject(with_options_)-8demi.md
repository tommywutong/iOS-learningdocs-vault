---
title: 'jsonObject(with:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/jsonserialization/jsonobject(with:options:)-8demi'
source_url: 'https://developer.apple.com/documentation/foundation/jsonserialization/jsonobject(with:options:)-8demi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonserialization/jsonobject%28with%3Aoptions%3A%29-8demi.json'
content_hash: 'sha256:536c51dbc933047d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONSerialization](../jsonserialization.md)

# jsonObject(with:options:)

<sub>Type Method</sub>

Returns a Foundation object from given JSON data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func jsonObject(with data: Data, options opt: JSONSerialization.ReadingOptions = []) throws -> Any
```

## Parameters

- `data` — A data object containing JSON data.

- `opt` — Options for reading the JSON data and creating the Foundation objects. For possible values, see [ReadingOptions](readingoptions.md).

## Return Value

A Foundation object from the JSON data in `data`, or `nil` if an error occurs.

## Discussion

The data must be in one of the 5 supported encodings listed in the JSON specification: UTF-8, UTF-16LE, UTF-16BE, UTF-32LE, UTF-32BE. The data may or may not have a BOM. The most efficient encoding to use for parsing is UTF-8, so if you have a choice in encoding the data passed to this method, use UTF-8.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [+ dataWithJSONObject:options:error:](<data(withjsonobject_options_).md>) — Returns JSON data from a Foundation object.

### Creating a JSON Object

- [+ JSONObjectWithStream:options:error:](<jsonobject(with_options_)-3afap.md>) — Returns a Foundation object from JSON data in a given stream.
- [ReadingOptions](readingoptions.md) — Options used when creating Foundation objects from JSON data.
