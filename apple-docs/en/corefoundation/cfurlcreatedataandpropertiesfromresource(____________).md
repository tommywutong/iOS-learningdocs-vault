---
title: 'CFURLCreateDataAndPropertiesFromResource(_:_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfurlcreatedataandpropertiesfromresource(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcreatedataandpropertiesfromresource(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcreatedataandpropertiesfromresource%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ddb51375fe9406a6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCreateDataAndPropertiesFromResource(_:_:_:_:_:_:)

<sub>Function</sub>

Loads the data and properties referred to by a given URL.

> [!warning] Deprecated
> For resource data, use the CFReadStream API. For file resource properties, use CFURLCopyResourcePropertiesForKeys.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func CFURLCreateDataAndPropertiesFromResource(_ alloc: CFAllocator!, _ url: CFURL!, _ resourceData: UnsafeMutablePointer<Unmanaged<CFData>?>!, _ properties: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!, _ desiredProperties: CFArray!, _ errorCode: UnsafeMutablePointer<Int32>!) -> Bool
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new `CFData` and `CFDictionary` objects returned in `resourceData` and `properties`. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `url` — The URL referring to the data and/or properties you wish to load.

- `resourceData` — On return, contains a `CFData` object containing the data referred to by `url`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

- `properties` — On return, a pointer to a `CFDictionary` object containing the resource properties referred to by `url`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

- `desiredProperties` — A list of the properties you wish to obtain and return in `properties`. See [File URL Properties](file-url-properties.md) and [HTTP URL Properties](http-url-properties.md) for the list of available properties.

- `errorCode` — `0` if successful, otherwise an error code indicating the nature of the problem. See [CFURLError](cfurlerror.md) for a list of possible error codes.

## Return Value

`true` if successful, `false` otherwise.

## Discussion

If you are interested in loading only the resource data or the resource’s properties, pass `NULL` for the one you don’t want. If `properties` is non-`NULL` and `desiredProperties` is `NULL` then all properties are fetched. Note that as much work as possible is done even if `false` is returned. For instance, if one property is not available, the others are fetched anyway. This function is intended for convenience, not performance.

## See Also

### Core Foundation URL Access Utilities Miscellaneous Functions

- [CFURLCreatePropertyFromResource](<cfurlcreatepropertyfromresource(________).md>) — Returns a given property specified by a given URL and property string. _(deprecated)_
- [CFURLDestroyResource](<cfurldestroyresource(____).md>) — Destroys a resource indicated by a given URL. _(deprecated)_
- [CFURLWriteDataAndPropertiesToResource](<cfurlwritedataandpropertiestoresource(________).md>) — Writes the given data and properties to a given URL. _(deprecated)_
