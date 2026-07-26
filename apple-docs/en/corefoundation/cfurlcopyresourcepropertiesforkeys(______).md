---
title: 'CFURLCopyResourcePropertiesForKeys(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcopyresourcepropertiesforkeys(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcopyresourcepropertiesforkeys(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcopyresourcepropertiesforkeys%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:bd9abef77b36b0dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCopyResourcePropertiesForKeys(_:_:_:)

<sub>Function</sub>

Returns the resource values for the properties identified by specified array of keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCopyResourcePropertiesForKeys(_ url: CFURL!, _ keys: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!
```

## Parameters

- `url` — The URL.

- `keys` — An array of property keys for the desired resource properties.

- `error` — The error that occurred if one or more resource values could not be retrieved.  This parameter is optional. If you are not interested in receiving error information, you can pass `nil`.

## Return Value

A dictionary of resource values indexed by key, or `NULL` if an error occurs.

## Discussion

This function first checks if the URL object already caches the specified resource values. If so, it returns the cached resource values to the caller. If not, then this function synchronously obtains the resource values from the backing store, adds the resource values to the URL object’s cache, and returns the resource values to the caller.

The type of the returned resource value varies by resource property; for details, see the documentation for the key you want to access.

If the result dictionary does not contain a resource value for one or more of the requested resource keys, it means those resource properties are not available for the specified URL, and no errors occurred when determining those resource properties were not available.

If an error occurs, this function returns `NULL` and populates the object pointer referenced by `error` with additional information.

> [!note] Note
> This method applies only to URLs that represent file system resources.

## See Also

### Related Documentation

- [CFURL](cfurl.md)

### Getting and Setting File System Resource Properties

- [CFURLClearResourcePropertyCache](<cfurlclearresourcepropertycache(__).md>) — Removes all cached resource values and temporary resource values from the URL object.
- [CFURLClearResourcePropertyCacheForKey](<cfurlclearresourcepropertycacheforkey(____).md>) — Removes the cached resource value identified by a given key from the URL object.
- [CFURLCopyResourcePropertyForKey](<cfurlcopyresourcepropertyforkey(________).md>) — Returns the value of a given resource property of a given URL.
- [CFURLCreateResourcePropertiesForKeysFromBookmarkData](<cfurlcreateresourcepropertiesforkeysfrombookmarkdata(______).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [CFURLCreateResourcePropertyForKeyFromBookmarkData](<cfurlcreateresourcepropertyforkeyfrombookmarkdata(______).md>) — Returns the value of a resource property from specified bookmark data.
- [CFURLSetResourcePropertiesForKeys](<cfurlsetresourcepropertiesforkeys(______).md>) — Sets the URL’s resource properties for a given set of keys to a given set of values.
- [CFURLSetResourcePropertyForKey](<cfurlsetresourcepropertyforkey(________).md>) — Sets the URL’s resource property for a given key to a given value.
- [CFURLSetTemporaryResourcePropertyForKey](<cfurlsettemporaryresourcepropertyforkey(______).md>) — Sets a temporary resource value on the URL.
