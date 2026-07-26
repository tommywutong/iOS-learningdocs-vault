---
title: 'CFWriteStreamCopyProperty(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfwritestreamcopyproperty(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfwritestreamcopyproperty(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfwritestreamcopyproperty%28_%3A_%3A%29.json'
content_hash: 'sha256:f407627791b27780'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFWriteStreamCopyProperty(_:_:)

<sub>Function</sub>

Returns the value of a property for a stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFWriteStreamCopyProperty(_ stream: CFWriteStream!, _ propertyName: CFStreamPropertyKey!) -> CFTypeRef!
```

## Parameters

- `stream` — The stream to examine.

- `propertyName` — The name of the stream property to obtain. The available properties for standard Core Foundation streams are listed in Stream Properties.

## Return Value

The value of the property `propertyName`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Each type of stream can define a set of properties that either describe or configure individual streams. A property can be any interesting information about a stream. Examples include the headers from an HTTP transmission, the expected number of bytes, file permission information, and so on. Use [CFWriteStreamSetProperty](<cfwritestreamsetproperty(______).md>) to modify the value of a property, although some properties are read-only.

## See Also

### Examining Stream Properties

- [CFWriteStreamCanAcceptBytes](<cfwritestreamcanacceptbytes(__).md>) — Returns whether a writable stream can accept new data without blocking.
- [CFWriteStreamCopyError](<cfwritestreamcopyerror(__).md>) — Returns the error associated with a stream.
- [CFWriteStreamGetError](<cfwritestreamgeterror(__).md>) — Returns the error status of a stream. _(deprecated)_
- [CFWriteStreamGetStatus](<cfwritestreamgetstatus(__).md>) — Returns the current state of a stream.
