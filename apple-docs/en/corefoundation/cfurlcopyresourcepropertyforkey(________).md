---
title: 'CFURLCopyResourcePropertyForKey(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcopyresourcepropertyforkey(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcopyresourcepropertyforkey(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcopyresourcepropertyforkey%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:95d5e89f53f01976'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCopyResourcePropertyForKey(_:_:_:_:)

<sub>Function</sub>

Returns the value of a given resource property of a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCopyResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValueTypeRefPtr: UnsafeMutableRawPointer!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

## Parameters

- `url` — The URL.

- `key` — The property value key for the requested value.

- `propertyValueTypeRefPtr` — The output pointer that is populated with the result.

- `error` — The error that occurred if the property’s value could not be obtained. This parameter is optional. If you are not interested in receiving error information, you can pass `NULL`.

## Return Value

`true` if `propertyValueTypeRefPtr` is successfully populated; otherwise, `false`.

## Discussion

This function first checks if the URL object already caches the resource value. If so, it returns the cached resource value to the caller. If not, then this function synchronously obtains the resource value from the backing store, adds the resource value to the URL object’s cache, and returns the resource value to the caller.

The type of the returned resource value varies by resource property; for details, see the documentation for the key you want to access.

If this function returns [true](../swift/true.md) and the propertyValueTypeRefPtr is populated with `nil`, it means that the resource property is not available for the specified resource, and that no errors occurred when determining that the resource property was unavailable.

If this function returns [false](../swift/false.md), an error occurred. the object pointer referenced by `error` is populated with additional information.

> [!note] Note
> This method applies only to URLs that represent file system resources.

## See Also

### Related Documentation

- [CFURL](cfurl.md)

### Getting and Setting File System Resource Properties

- [CFURLClearResourcePropertyCache](<cfurlclearresourcepropertycache(__).md>) — Removes all cached resource values and temporary resource values from the URL object.
- [CFURLClearResourcePropertyCacheForKey](<cfurlclearresourcepropertycacheforkey(____).md>) — Removes the cached resource value identified by a given key from the URL object.
- [CFURLCopyResourcePropertiesForKeys](<cfurlcopyresourcepropertiesforkeys(______).md>) — Returns the resource values for the properties identified by specified array of keys.
- [CFURLCreateResourcePropertiesForKeysFromBookmarkData](<cfurlcreateresourcepropertiesforkeysfrombookmarkdata(______).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [CFURLCreateResourcePropertyForKeyFromBookmarkData](<cfurlcreateresourcepropertyforkeyfrombookmarkdata(______).md>) — Returns the value of a resource property from specified bookmark data.
- [CFURLSetResourcePropertiesForKeys](<cfurlsetresourcepropertiesforkeys(______).md>) — Sets the URL’s resource properties for a given set of keys to a given set of values.
- [CFURLSetResourcePropertyForKey](<cfurlsetresourcepropertyforkey(________).md>) — Sets the URL’s resource property for a given key to a given value.
- [CFURLSetTemporaryResourcePropertyForKey](<cfurlsettemporaryresourcepropertyforkey(______).md>) — Sets a temporary resource value on the URL.
