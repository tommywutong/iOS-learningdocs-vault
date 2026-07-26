---
title: propertyList()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/propertylist()
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/propertylist()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/propertylist%28%29.json'
content_hash: 'sha256:b9a235a25bceeccc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# propertyList()

<sub>Instance Method</sub>

Parses the receiver as a text representation of a property list, returning an `NSString`, `NSData`, `NSArray`, or `NSDictionary` object, according to the topmost element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func propertyList() -> Any
```

## Return Value

A property list representation of returning an `NSString`, `NSData`, `NSArray`, or `NSDictionary` object, according to the topmost element.

## Discussion

The receiver must contain a string in a property list format. For a discussion of property list formats, see [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i).

> [!important] Important
> Raises an `NSParseErrorException` if the receiver cannot be parsed as a property list.

## See Also

### Related Documentation

- [+ stringWithContentsOfFile:](<string(withcontentsoffile_).md>) — Returns a string created by reading data from the file named by a given path. _(deprecated)_

### Converting String Contents Into a Property List

- [- propertyListFromStringsFileFormat](<propertylistfromstringsfileformat().md>) — Returns a dictionary object initialized with the keys and values found in the receiver.
