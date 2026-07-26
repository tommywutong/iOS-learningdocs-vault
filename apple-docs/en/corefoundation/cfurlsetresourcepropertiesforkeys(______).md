---
title: 'CFURLSetResourcePropertiesForKeys(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlsetresourcepropertiesforkeys(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlsetresourcepropertiesforkeys(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlsetresourcepropertiesforkeys%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8dfe8e3409999b04'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLSetResourcePropertiesForKeys(_:_:_:)

<sub>Function</sub>

Sets the URL’s resource properties for a given set of keys to a given set of values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLSetResourcePropertiesForKeys(_ url: CFURL!, _ keyedPropertyValues: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

## Parameters

- `url` — The URL.

- `keyedPropertyValues` — A dictionary of resource values to be set.

- `error` — The error that occurred if one or more resource values could not be set.

## Return Value

`true` if all resource values in `keyedValues` are successfully set; otherwise, `false`.

## Discussion

This function synchronously writes the new resource value out to disk. If an error occurs after some resource properties have been successfully changed, the `userInfo` dictionary in the returned error object contains a `kCFURLKeysOfUnsetValuesKey` key whose value is an array of the resource values that were not successfully set.

Attempts to set a read-only resource property or to set a resource property that is not supported by the resource are ignored and are not considered errors.

The order in which the resource values are set is not defined. If you need to guarantee the order in which resource values are set, you should make multiple requests to this function or [CFURLSetResourcePropertyForKey](<cfurlsetresourcepropertyforkey(________).md>).

> [!note] Note
> This method applies only to URLs for file system resources.

## See Also

### Related Documentation

- [CFURL](cfurl.md)

### Getting and Setting File System Resource Properties

- [CFURLClearResourcePropertyCache](<cfurlclearresourcepropertycache(__).md>) — Removes all cached resource values and temporary resource values from the URL object.
- [CFURLClearResourcePropertyCacheForKey](<cfurlclearresourcepropertycacheforkey(____).md>) — Removes the cached resource value identified by a given key from the URL object.
- [CFURLCopyResourcePropertiesForKeys](<cfurlcopyresourcepropertiesforkeys(______).md>) — Returns the resource values for the properties identified by specified array of keys.
- [CFURLCopyResourcePropertyForKey](<cfurlcopyresourcepropertyforkey(________).md>) — Returns the value of a given resource property of a given URL.
- [CFURLCreateResourcePropertiesForKeysFromBookmarkData](<cfurlcreateresourcepropertiesforkeysfrombookmarkdata(______).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [CFURLCreateResourcePropertyForKeyFromBookmarkData](<cfurlcreateresourcepropertyforkeyfrombookmarkdata(______).md>) — Returns the value of a resource property from specified bookmark data.
- [CFURLSetResourcePropertyForKey](<cfurlsetresourcepropertyforkey(________).md>) — Sets the URL’s resource property for a given key to a given value.
- [CFURLSetTemporaryResourcePropertyForKey](<cfurlsettemporaryresourcepropertyforkey(______).md>) — Sets a temporary resource value on the URL.
