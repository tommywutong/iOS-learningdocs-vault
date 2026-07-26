---
title: 'CFBundleCreateBundlesFromDirectory(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlecreatebundlesfromdirectory(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlecreatebundlesfromdirectory(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlecreatebundlesfromdirectory%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:649b17940b66a425'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCreateBundlesFromDirectory(_:_:_:)

<sub>Function</sub>

Searches a directory and constructs an array of CFBundle objects from all valid bundles in the specified directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleCreateBundlesFromDirectory(_ allocator: CFAllocator!, _ directoryURL: CFURL!, _ bundleType: CFString!) -> CFArray!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `directoryURL` — The location of the directory to search for valid bundles.

- `bundleType` — The abstract type of the bundles to locate and create. The type is expressed as a filename extension, such as `bundle`. Pass `NULL` to create CFBundle objects for bundles of any type.

## Return Value

A CFArray object containing CFBundle objects created from the contents of the specified directory. Returns an empty array if no bundles exist at `directoryURL`, and `NULL` if there was a memory allocation problem. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The array returned by this function will not contain stale CFBundle references.

### Special Considerations

The [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029) applies both to the array returned and to the bundles in the array. In order to properly dispose of the returned value, you must release the array _and_ any bundles returned in the array.

## See Also

### Creating and Accessing Bundles

- [CFBundleCreate](<cfbundlecreate(____).md>) — Creates a CFBundle object.
- [CFBundleGetAllBundles](<cfbundlegetallbundles().md>) — Returns an array containing all of the bundles currently open in the application.
- [CFBundleGetBundleWithIdentifier](<cfbundlegetbundlewithidentifier(__).md>) — Locate a bundle given its program-defined identifier.
- [CFBundleGetMainBundle](<cfbundlegetmainbundle().md>) — Returns an application’s main bundle.
