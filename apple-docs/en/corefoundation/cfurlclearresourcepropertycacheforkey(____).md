---
title: 'CFURLClearResourcePropertyCacheForKey(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlclearresourcepropertycacheforkey(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlclearresourcepropertycacheforkey(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlclearresourcepropertycacheforkey%28_%3A_%3A%29.json'
content_hash: 'sha256:c8c315710de3c1a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLClearResourcePropertyCacheForKey(_:_:)

<sub>Function</sub>

Removes the cached resource value identified by a given key from the URL object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLClearResourcePropertyCacheForKey(_ url: CFURL!, _ key: CFString!)
```

## Parameters

- `url` — The URL.

- `key` — The resource value key whose cached values you want to remove.

## Discussion

Removing a cached resource value may remove other cached resource values because some resource values are cached as a set of values, and because some resource values depend on other resource values. (Temporary resource values have no dependencies.)

This method is currently applicable only to URLs for file system resources.

> [!note] Note
> The caching behavior of the `NSURL` and `CFURL` APIs differ. For `NSURL`, all cached values (not temporary values) are automatically removed after each pass through the run loop. You only need to call the [CFURL](cfurl.md) method when you want to clear the cache within a single execution of the run loop. The `CFURL` functions, on the other hand, do not automatically clear cached resource values. The client has complete control over the cache lifetimes, and you must use [CFURLClearResourcePropertyCacheForKey](<cfurlclearresourcepropertycacheforkey(____).md>) or [CFURLClearResourcePropertyCache](<cfurlclearresourcepropertycache(__).md>) to clear cached resource values.

## See Also

### Getting and Setting File System Resource Properties

- [CFURLClearResourcePropertyCache](<cfurlclearresourcepropertycache(__).md>) — Removes all cached resource values and temporary resource values from the URL object.
- [CFURLCopyResourcePropertiesForKeys](<cfurlcopyresourcepropertiesforkeys(______).md>) — Returns the resource values for the properties identified by specified array of keys.
- [CFURLCopyResourcePropertyForKey](<cfurlcopyresourcepropertyforkey(________).md>) — Returns the value of a given resource property of a given URL.
- [CFURLCreateResourcePropertiesForKeysFromBookmarkData](<cfurlcreateresourcepropertiesforkeysfrombookmarkdata(______).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [CFURLCreateResourcePropertyForKeyFromBookmarkData](<cfurlcreateresourcepropertyforkeyfrombookmarkdata(______).md>) — Returns the value of a resource property from specified bookmark data.
- [CFURLSetResourcePropertiesForKeys](<cfurlsetresourcepropertiesforkeys(______).md>) — Sets the URL’s resource properties for a given set of keys to a given set of values.
- [CFURLSetResourcePropertyForKey](<cfurlsetresourcepropertyforkey(________).md>) — Sets the URL’s resource property for a given key to a given value.
- [CFURLSetTemporaryResourcePropertyForKey](<cfurlsettemporaryresourcepropertyforkey(______).md>) — Sets a temporary resource value on the URL.
