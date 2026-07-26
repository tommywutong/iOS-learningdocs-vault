---
title: 'CFURLCreateResourcePropertyForKeyFromBookmarkData(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcreateresourcepropertyforkeyfrombookmarkdata(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcreateresourcepropertyforkeyfrombookmarkdata(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcreateresourcepropertyforkeyfrombookmarkdata%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c6595dee292ed79b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCreateResourcePropertyForKeyFromBookmarkData(_:_:_:)

<sub>Function</sub>

Returns the value of a resource property from specified bookmark data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCreateResourcePropertyForKeyFromBookmarkData(_ allocator: CFAllocator!, _ resourcePropertyKey: CFString!, _ bookmark: CFData!) -> Unmanaged<CFTypeRef>!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new `CFURL` object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `resourcePropertyKey` — The resource property key. See [Common File System Resource Keys](common-file-system-resource-keys.md) for a list of possible keys.

- `bookmark` — The bookmark data the resource value is derived from.

## Return Value

The resource property value.

## Discussion

This function does not attempt to resolve the bookmark data or perform I/O.

## See Also

### Getting and Setting File System Resource Properties

- [CFURLClearResourcePropertyCache](<cfurlclearresourcepropertycache(__).md>) — Removes all cached resource values and temporary resource values from the URL object.
- [CFURLClearResourcePropertyCacheForKey](<cfurlclearresourcepropertycacheforkey(____).md>) — Removes the cached resource value identified by a given key from the URL object.
- [CFURLCopyResourcePropertiesForKeys](<cfurlcopyresourcepropertiesforkeys(______).md>) — Returns the resource values for the properties identified by specified array of keys.
- [CFURLCopyResourcePropertyForKey](<cfurlcopyresourcepropertyforkey(________).md>) — Returns the value of a given resource property of a given URL.
- [CFURLCreateResourcePropertiesForKeysFromBookmarkData](<cfurlcreateresourcepropertiesforkeysfrombookmarkdata(______).md>) — Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [CFURLSetResourcePropertiesForKeys](<cfurlsetresourcepropertiesforkeys(______).md>) — Sets the URL’s resource properties for a given set of keys to a given set of values.
- [CFURLSetResourcePropertyForKey](<cfurlsetresourcepropertyforkey(________).md>) — Sets the URL’s resource property for a given key to a given value.
- [CFURLSetTemporaryResourcePropertyForKey](<cfurlsettemporaryresourcepropertyforkey(______).md>) — Sets a temporary resource value on the URL.
