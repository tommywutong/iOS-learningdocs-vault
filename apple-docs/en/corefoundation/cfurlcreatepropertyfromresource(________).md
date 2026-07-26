---
title: 'CFURLCreatePropertyFromResource(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfurlcreatepropertyfromresource(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcreatepropertyfromresource(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcreatepropertyfromresource%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8aab9cb10609b754'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCreatePropertyFromResource(_:_:_:_:)

<sub>Function</sub>

Returns a given property specified by a given URL and property string.

> [!warning] Deprecated
> For file resource properties, use CFURLCopyResourcePropertyForKey.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func CFURLCreatePropertyFromResource(_ alloc: CFAllocator!, _ url: CFURL!, _ property: CFString!, _ errorCode: UnsafeMutablePointer<Int32>!) -> CFTypeRef!
```

## Parameters

- `alloc` — The allocator to use to to allocate memory for the new `CFType` object for the requested property. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `url` — The `CFURL` object referring to the resource whose properties are loaded.

- `property` — The name of the property you wish to load. Pass one of the provided string constants indicating the property. See [File URL Properties](file-url-properties.md) and [HTTP URL Properties](http-url-properties.md) for the list of available properties.

- `errorCode` — On return, `0` if successful, otherwise an error code indicating the nature of the problem. See [CFURLError](cfurlerror.md) for a list of possible error codes.

## Return Value

If successful, the requested property as a `CFType` object, `NULL` otherwise. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This is a convenience function for retrieving individual property values which calls through to [CFURLCreateDataAndPropertiesFromResource](<cfurlcreatedataandpropertiesfromresource(____________).md>).

## See Also

### Core Foundation URL Access Utilities Miscellaneous Functions

- [CFURLCreateDataAndPropertiesFromResource](<cfurlcreatedataandpropertiesfromresource(____________).md>) — Loads the data and properties referred to by a given URL. _(deprecated)_
- [CFURLDestroyResource](<cfurldestroyresource(____).md>) — Destroys a resource indicated by a given URL. _(deprecated)_
- [CFURLWriteDataAndPropertiesToResource](<cfurlwritedataandpropertiestoresource(________).md>) — Writes the given data and properties to a given URL. _(deprecated)_
