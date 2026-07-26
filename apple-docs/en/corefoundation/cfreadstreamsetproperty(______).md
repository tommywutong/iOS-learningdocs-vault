---
title: 'CFReadStreamSetProperty(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfreadstreamsetproperty(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfreadstreamsetproperty(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfreadstreamsetproperty%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:559ad9f6730ce235'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFReadStreamSetProperty(_:_:_:)

<sub>Function</sub>

Sets the value of a property for a stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFReadStreamSetProperty(_ stream: CFReadStream!, _ propertyName: CFStreamPropertyKey!, _ propertyValue: CFTypeRef!) -> Bool
```

## Parameters

- `stream` — The stream to modify.

- `propertyName` — The name of the property to set. The available properties for standard Core Foundation streams are listed in [CFStream](cfstream.md).

- `propertyValue` — The value to which to set the property `propertyName` for `stream`. The allowed data type of the value depends on the property being set.

## Return Value

`TRUE` if `stream` recognizes and accepts the given property-value pair, otherwise`FALSE`.

## Discussion

Each type of stream can define a set of properties that either describe or configure individual streams. A property can be any interesting information about a stream. Examples include the headers from an HTTP transmission, the expected number of bytes, file permission information, and so on. Properties that can be set configure the behavior of the stream and may be modifiable only at particular times, such as before the stream has been opened. (In fact, you should assume that you can set properties only before opening the stream, unless otherwise noted.) To read the value of a property use [CFReadStreamCopyProperty](<cfreadstreamcopyproperty(____).md>), although some properties are write-only.

## See Also

### Setting Stream Properties

- [CFReadStreamSetClient](<cfreadstreamsetclient(________).md>) — Assigns a client to a stream, which receives callbacks when certain events occur.
