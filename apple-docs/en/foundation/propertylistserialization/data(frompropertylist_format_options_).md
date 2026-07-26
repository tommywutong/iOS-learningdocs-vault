---
title: 'data(fromPropertyList:format:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/propertylistserialization/data(frompropertylist:format:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/propertylistserialization/data(frompropertylist:format:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistserialization/data%28frompropertylist%3Aformat%3Aoptions%3A%29.json'
content_hash: 'sha256:527f9bc0b8ab40f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListSerialization](../propertylistserialization.md)

# data(fromPropertyList:format:options:)

<sub>Type Method</sub>

Returns an `NSData` object containing a given property list in a specified format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func data(fromPropertyList plist: Any, format: PropertyListSerialization.PropertyListFormat, options opt: PropertyListSerialization.WriteOptions) throws -> Data
```

## Parameters

- `plist` — A property list object.

- `format` — A property list format. For possible values, see [PropertyListFormat](propertylistformat.md).

- `opt` — The `opt` parameter is currently unused. No options should be specified.

## Return Value

An `NSData` object containing `plist` in the format specified by `format`.

## Discussion

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
- [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i)

### Serializing a Property List

- [+ writePropertyList:toStream:format:options:error:](<writepropertylist(__to_format_options_error_).md>) — Writes a property list to the specified stream.
- [WriteOptions](writeoptions.md)
