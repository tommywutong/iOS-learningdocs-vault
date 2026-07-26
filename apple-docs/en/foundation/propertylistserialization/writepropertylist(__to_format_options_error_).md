---
title: 'writePropertyList(_:to:format:options:error:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/propertylistserialization/writepropertylist(_:to:format:options:error:)'
source_url: 'https://developer.apple.com/documentation/foundation/propertylistserialization/writepropertylist(_:to:format:options:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistserialization/writepropertylist%28_%3Ato%3Aformat%3Aoptions%3Aerror%3A%29.json'
content_hash: 'sha256:22a232f6bd3b67fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListSerialization](../propertylistserialization.md)

# writePropertyList(_:to:format:options:error:)

<sub>Type Method</sub>

Writes a property list to the specified stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func writePropertyList(_ plist: Any, to stream: OutputStream, format: PropertyListSerialization.PropertyListFormat, options opt: PropertyListSerialization.WriteOptions, error: NSErrorPointer) -> Int
```

## Parameters

- `plist` — The property list that you want to write out.

- `stream` — An [OutputStream](../outputstream.md) instance that is open and ready to receive the property list data.

- `format` — One of the property list formats defined in [PropertyListFormat](propertylistformat.md).

- `opt` — Currently unused. Set to `0`.

- `error` — A pointer that the function may set to an [NSError](../nserror.md) object when an error occurs to provide additional information about the error.

## Return Value

The number of bytes written to the stream. A return value of `0` indicates that an error occurred.

## See Also

### Serializing a Property List

- [+ dataWithPropertyList:format:options:error:](<data(frompropertylist_format_options_).md>) — Returns an `NSData` object containing a given property list in a specified format.
- [WriteOptions](writeoptions.md)
