---
title: 'CFPropertyListWriteToStream(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfpropertylistwritetostream(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpropertylistwritetostream(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpropertylistwritetostream%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:59e0166c940b2e72'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPropertyListWriteToStream(_:_:_:_:)

<sub>Function</sub>

Writes the bytes of a property list serialization out to a stream.

> [!warning] Deprecated
> Use CFPropertyListWrite instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPropertyListWriteToStream(_ propertyList: CFPropertyList!, _ stream: CFWriteStream!, _ format: CFPropertyListFormat, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFIndex
```

## Parameters

- `propertyList` — The property list to write out.

- `stream` — The stream to write to. The stream must be opened and configured—this function simply writes bytes to the stream.

- `format` — A constant that specifies the format used to write `propertyList`. See [CFPropertyListFormat](cfpropertylistformat.md) for possible values.

- `errorString` — On return, `NULL` if the conversion is successful, otherwise a string that describes the nature of the errors. Error messages are not localized, but may be in the future, so they are not currently suitable for comparison. Pass `NULL` if you do not wish to receive an error string. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Return Value

The number of bytes written, or `0` if an error occurred. If `0` is returned, `errorString` will contain an error message.

## Discussion

This function leaves the stream open after reading the content. When reading a property list, this function expects the reading stream to end wherever the writing ended, so that the end of the property list data can be identified.

### Special Considerations

> [!warning] Warning
> This function is obsolete and will be deprecated soon. Use [CFPropertyListWrite](<cfpropertylistwrite(__________).md>) instead.

## See Also

### Exporting a Property List

- [CFPropertyListCreateData](<cfpropertylistcreatedata(__________).md>) — Returns a CFData object containing a serialized representation of a given property list in a specified format.
- [CFPropertyListWrite](<cfpropertylistwrite(__________).md>) — Write the bytes of a serialized property list out to a stream.
- [CFPropertyListCreateXMLData](<cfpropertylistcreatexmldata(____).md>) — Creates an XML representation of the specified property list. _(deprecated)_
