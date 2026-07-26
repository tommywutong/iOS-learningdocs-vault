---
title: 'propertyListFromData(_:mutabilityOption:format:errorDescription:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/propertylistserialization/propertylistfromdata(_:mutabilityoption:format:errordescription:)'
source_url: 'https://developer.apple.com/documentation/foundation/propertylistserialization/propertylistfromdata(_:mutabilityoption:format:errordescription:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistserialization/propertylistfromdata%28_%3Amutabilityoption%3Aformat%3Aerrordescription%3A%29.json'
content_hash: 'sha256:e2935a23854b29f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListSerialization](../propertylistserialization.md)

# propertyListFromData(_:mutabilityOption:format:errorDescription:)

<sub>Type Method</sub>

This method is deprecated. Use [+ dataWithPropertyList:format:options:error:](<data(frompropertylist_format_options_).md>) instead.

> [!warning] Deprecated
> Use [+ propertyListWithData:options:format:error:](<propertylist(from_options_format_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func propertyListFromData(_ data: Data, mutabilityOption opt: PropertyListSerialization.MutabilityOptions = [], format: UnsafeMutablePointer<PropertyListSerialization.PropertyListFormat>?, errorDescription errorString: UnsafeMutablePointer<NSString?>?) -> Any?
```

## Parameters

- `data` — A data object containing a serialized property list.

- `opt` — The options used to create the property list. For possible values, see [MutabilityOptions](mutabilityoptions.md).

- `format` — If the property list is valid, upon return contains the format. `format` can be `nil`, in which case the property list format is not returned. For possible values, see [PropertyListFormat](propertylistformat.md).

- `errorString` — Upon return, if the conversion is successful, `errorString` is `nil`. If the conversion fails, upon return contains a string describing the nature of the error.

## Return Value

A property list object corresponding to the representation in `data`. If data is not in a supported format, returns `nil`.

## See Also

### Related Documentation

- [+ propertyListWithData:options:format:error:](<propertylist(from_options_format_).md>) — Creates and returns a property list from the specified data.

### Obsolete Methods

- [+ dataFromPropertyList:format:errorDescription:](<datafrompropertylist(__format_errordescription_).md>) — This method is obsolete and will be deprecated soon. _(deprecated)_
