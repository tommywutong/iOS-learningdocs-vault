---
title: 'propertyList(with:options:format:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/propertylistserialization/propertylist(with:options:format:)'
source_url: 'https://developer.apple.com/documentation/foundation/propertylistserialization/propertylist(with:options:format:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistserialization/propertylist%28with%3Aoptions%3Aformat%3A%29.json'
content_hash: 'sha256:d75702428d9cc002'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListSerialization](../propertylistserialization.md)

# propertyList(with:options:format:)

<sub>Type Method</sub>

Creates and returns a property list by reading from the specified stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func propertyList(with stream: InputStream, options opt: PropertyListSerialization.ReadOptions = [], format: UnsafeMutablePointer<PropertyListSerialization.PropertyListFormat>?) throws -> Any
```

## Parameters

- `stream` — An `NSStream` object. The stream should be open and configured for reading.

- `opt` — The options used to create the property list. For possible values, see [MutabilityOptions](mutabilityoptions.md).

- `format` — Upon return, contains the format that the property list was stored in. Pass `nil` if you do not need to know the format.

## Return Value

A property list object corresponding to the representation in `data`. If data is not in a supported format, returns `nil`.

## Discussion

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Deserializing a Property List

- [+ propertyListWithData:options:format:error:](<propertylist(from_options_format_).md>) — Creates and returns a property list from the specified data.
