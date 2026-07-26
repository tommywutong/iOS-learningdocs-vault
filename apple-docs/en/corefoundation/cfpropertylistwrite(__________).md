---
title: 'CFPropertyListWrite(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpropertylistwrite(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpropertylistwrite(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpropertylistwrite%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:22954b80d855cc51'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPropertyListWrite(_:_:_:_:_:)

<sub>Function</sub>

Write the bytes of a serialized property list out to a stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPropertyListWrite(_ propertyList: CFPropertyList!, _ stream: CFWriteStream!, _ format: CFPropertyListFormat, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFIndex
```

## Parameters

- `propertyList` — The property list to write out.

- `stream` — The CFWriteStream to which to write the data. The stream must be opened and configured.

- `format` — A CFPropertyListFormat constant to specify the data format. See [CFPropertyListFormat](cfpropertylistformat.md) for possible values.

- `options` — This parameter is currently unused and should be set to `0`.

- `error` — If this parameter is non-NULL, if an error occurs, on return this will contain a CFError error describing the problem. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Return Value

The number of bytes written to `stream`. If an error occurs, returns `0`.

## See Also

### Exporting a Property List

- [CFPropertyListCreateData](<cfpropertylistcreatedata(__________).md>) — Returns a CFData object containing a serialized representation of a given property list in a specified format.
- [CFPropertyListCreateXMLData](<cfpropertylistcreatexmldata(____).md>) — Creates an XML representation of the specified property list. _(deprecated)_
- [CFPropertyListWriteToStream](<cfpropertylistwritetostream(________).md>) — Writes the bytes of a property list serialization out to a stream. _(deprecated)_
