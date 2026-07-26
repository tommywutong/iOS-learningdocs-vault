---
title: 'CFBundleCreate(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlecreate(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlecreate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlecreate%28_%3A_%3A%29.json'
content_hash: 'sha256:9aa8efa398aabc9c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleCreate(_:_:)

<sub>Function</sub>

Creates a CFBundle object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleCreate(_ allocator: CFAllocator!, _ bundleURL: CFURL!) -> CFBundle!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `bundleURL` — The location of the bundle for which to create a CFBundle object.

## Return Value

A CFBundle object created from the bundle at `bundleURL`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Returns `NULL` if there was a memory allocation problem. May return an existing CFBundle object with the reference count incremented. May return `NULL` if the bundle doesn’t exist at `bundleURL` (see Discussion).

## Discussion

Once a bundle has been created, it is cached; the bundle cache is flushed only periodically. `CFBundleCreate` does not check that a cached bundle still exists in the filesystem. If a bundle is deleted from the filesystem, it is therefore possible for `CFBundleCreate` to return a cached bundle that has actually been deleted.

## See Also

### Creating and Accessing Bundles

- [CFBundleCreateBundlesFromDirectory](<cfbundlecreatebundlesfromdirectory(______).md>) — Searches a directory and constructs an array of CFBundle objects from all valid bundles in the specified directory.
- [CFBundleGetAllBundles](<cfbundlegetallbundles().md>) — Returns an array containing all of the bundles currently open in the application.
- [CFBundleGetBundleWithIdentifier](<cfbundlegetbundlewithidentifier(__).md>) — Locate a bundle given its program-defined identifier.
- [CFBundleGetMainBundle](<cfbundlegetmainbundle().md>) — Returns an application’s main bundle.
