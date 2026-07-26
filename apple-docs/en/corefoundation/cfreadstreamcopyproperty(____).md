---
title: 'CFReadStreamCopyProperty(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfreadstreamcopyproperty(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfreadstreamcopyproperty(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfreadstreamcopyproperty%28_%3A_%3A%29.json'
content_hash: 'sha256:c9deabb597a25daa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFReadStreamCopyProperty(_:_:)

<sub>Function</sub>

Returns the value of a property for a stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFReadStreamCopyProperty(_ stream: CFReadStream!, _ propertyName: CFStreamPropertyKey!) -> CFTypeRef!
```

## Parameters

- `stream` — The stream to examine.

- `propertyName` — The name of the stream property to obtain. The available properties for standard Core Foundation streams are listed in [CFStream](cfstream.md).

## Return Value

The value of the property `propertyName`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Each type of stream can define a set of properties that either describe or configure individual streams. A property can be any information about a stream, other than the actual data the stream handles. Examples include the headers from an HTTP transmission, the expected number of bytes, file permission information, and so on. Use [CFReadStreamSetProperty](<cfreadstreamsetproperty(______).md>) to modify the value of a property, although some properties are read-only.

## See Also

### Examining Stream Properties

- [CFReadStreamGetBuffer](<cfreadstreamgetbuffer(______).md>) — Returns a pointer to a stream’s internal buffer of unread data, if possible.
- [CFReadStreamCopyError](<cfreadstreamcopyerror(__).md>) — Returns the error associated with a stream.
- [CFReadStreamGetError](<cfreadstreamgeterror(__).md>) — Returns the error status of a stream. _(deprecated)_
- [CFReadStreamGetStatus](<cfreadstreamgetstatus(__).md>) — Returns the current state of a stream.
- [CFReadStreamHasBytesAvailable](<cfreadstreamhasbytesavailable(__).md>) — Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.
