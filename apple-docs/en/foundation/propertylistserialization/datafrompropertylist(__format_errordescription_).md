---
title: 'dataFromPropertyList(_:format:errorDescription:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/propertylistserialization/datafrompropertylist(_:format:errordescription:)'
source_url: 'https://developer.apple.com/documentation/foundation/propertylistserialization/datafrompropertylist(_:format:errordescription:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistserialization/datafrompropertylist%28_%3Aformat%3Aerrordescription%3A%29.json'
content_hash: 'sha256:9300951a0f8917b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListSerialization](../propertylistserialization.md)

# dataFromPropertyList(_:format:errorDescription:)

<sub>Type Method</sub>

This method is obsolete and will be deprecated soon.

> [!warning] Deprecated
> Use [+ dataWithPropertyList:format:options:error:](<data(frompropertylist_format_options_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func dataFromPropertyList(_ plist: Any, format: PropertyListSerialization.PropertyListFormat, errorDescription errorString: UnsafeMutablePointer<NSString?>?) -> Data?
```

## Parameters

- `plist` — A property list object.

- `format` — A property list format. For possible values, see [PropertyListFormat](propertylistformat.md).

- `errorString` — Upon return, if the conversion is successful, `errorString` is `nil`. If the conversion fails, upon return contains a string describing the nature of the error.

## Return Value

An `NSData` object containing `plist` in the format specified by `format`.

## Discussion

This method is obsolete and will be deprecated soon. Use [+ dataWithPropertyList:format:options:error:](<data(frompropertylist_format_options_).md>) instead.

## See Also

### Related Documentation

- [+ dataWithPropertyList:format:options:error:](<data(frompropertylist_format_options_).md>) — Returns an `NSData` object containing a given property list in a specified format.

### Obsolete Methods

- [+ propertyListFromData:mutabilityOption:format:errorDescription:](<propertylistfromdata(__mutabilityoption_format_errordescription_).md>) — This method is deprecated. Use [+ dataWithPropertyList:format:options:error:](<data(frompropertylist_format_options_).md>) instead. _(deprecated)_
