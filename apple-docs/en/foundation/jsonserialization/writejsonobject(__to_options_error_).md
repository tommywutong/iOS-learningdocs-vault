---
title: 'writeJSONObject(_:to:options:error:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/jsonserialization/writejsonobject(_:to:options:error:)'
source_url: 'https://developer.apple.com/documentation/foundation/jsonserialization/writejsonobject(_:to:options:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonserialization/writejsonobject%28_%3Ato%3Aoptions%3Aerror%3A%29.json'
content_hash: 'sha256:62d23526a4d46c27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONSerialization](../jsonserialization.md)

# writeJSONObject(_:to:options:error:)

<sub>Type Method</sub>

Writes a given JSON object to a stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func writeJSONObject(_ obj: Any, to stream: OutputStream, options opt: JSONSerialization.WritingOptions = [], error: NSErrorPointer) -> Int
```

## Parameters

- `obj` — The object to write to `stream`.

- `stream` — The stream to which to write. The stream should be open and configured.

- `opt` — Options for writing the JSON data. See [WritingOptions](writingoptions.md) for possible values.

- `error` — If an error occurs, upon return contains an `NSError` object with code [NSPropertyListWriteInvalidError](../nspropertylistwriteinvaliderror-swift.var.md) that describes the problem.

## Return Value

The number of bytes written to the stream, or `0` if an error occurs.

## See Also

### Creating JSON Data

- [+ dataWithJSONObject:options:error:](<data(withjsonobject_options_).md>) — Returns JSON data from a Foundation object.
- [WritingOptions](writingoptions.md) — Options for writing JSON data.
- [+ isValidJSONObject:](<isvalidjsonobject(__).md>) — Returns a Boolean value that indicates whether the serializer can convert a given object to JSON data.
