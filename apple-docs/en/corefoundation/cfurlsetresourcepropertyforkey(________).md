---
title: 'CFURLSetResourcePropertyForKey(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlsetresourcepropertyforkey(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlsetresourcepropertyforkey(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlsetresourcepropertyforkey%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:9b692f98bec411ea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLSetResourcePropertyForKey(_:_:_:_:)

<sub>Function</sub>

Sets the URL’s resource property for a given key to a given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLSetResourcePropertyForKey(_ url: CFURL!, _ key: CFString!, _ propertyValue: CFTypeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

## Parameters

- `url` — The URL.

- `key` — The name of one of the URL’s resource properties.

- `propertyValue` — The value for the resource property defined by `key`.

- `error` — The error that occurred if the resource value could not be set.

## Return Value

`true`  if the resource property named `key` is successfully set to `value`; otherwise, `false`.

## Discussion

This function synchronously writes the new resource value out to disk. Attempts to set a read-only resource property or to set a resource property that is not supported by the resource are ignored and are not considered errors.

If an error occurs, this method returns `false` and populates the object pointer referenced by `error` with additional information.

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
- [CFURLSetResourcePropertiesForKeys](<cfurlsetresourcepropertiesforkeys(______).md>) — Sets the URL’s resource properties for a given set of keys to a given set of values.
- [CFURLSetTemporaryResourcePropertyForKey](<cfurlsettemporaryresourcepropertyforkey(______).md>) — Sets a temporary resource value on the URL.
