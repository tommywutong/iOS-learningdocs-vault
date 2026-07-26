---
title: 'data(withJSONObject:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/jsonserialization/data(withjsonobject:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/jsonserialization/data(withjsonobject:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonserialization/data%28withjsonobject%3Aoptions%3A%29.json'
content_hash: 'sha256:5adcf502e018c727'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONSerialization](../jsonserialization.md)

# data(withJSONObject:options:)

<sub>Type Method</sub>

Returns JSON data from a Foundation object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func data(withJSONObject obj: Any, options opt: JSONSerialization.WritingOptions = []) throws -> Data
```

## Parameters

- `obj` — The object from which to generate JSON data. Must not be `nil`.

- `opt` — Options for creating the JSON data. See [WritingOptions](writingoptions.md) for possible values.

## Return Value

JSON data for `obj`, or `nil` if an internal error occurs. The resulting data is encoded in UTF-8.

## Discussion

If `obj` can’t produce valid JSON, [JSONSerialization](../jsonserialization.md) throws an exception. This exception occurs prior to parsing and represents a programming error, not an internal error. Before calling this method, you should check whether the input can produce valid JSON by using [+ isValidJSONObject:](<isvalidjsonobject(__).md>).

Setting the [NSJSONWritingPrettyPrinted](writingoptions/prettyprinted.md) option generates JSON with white space designed to make the output more readable. If this option isn’t set, [JSONSerialization](../jsonserialization.md) generates the most compact possible JSON.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Creating JSON Data

- [+ writeJSONObject:toStream:options:error:](<writejsonobject(__to_options_error_).md>) — Writes a given JSON object to a stream.
- [WritingOptions](writingoptions.md) — Options for writing JSON data.
- [+ isValidJSONObject:](<isvalidjsonobject(__).md>) — Returns a Boolean value that indicates whether the serializer can convert a given object to JSON data.
