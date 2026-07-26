---
title: CFBundleGetAllBundles()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbundlegetallbundles()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlegetallbundles()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlegetallbundles%28%29.json'
content_hash: 'sha256:0c952b2a21cfd965'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleGetAllBundles()

<sub>Function</sub>

Returns an array containing all of the bundles currently open in the application.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleGetAllBundles() -> CFArray!
```

## Return Value

A CFArray object containing CFBundle objects for each open bundle in the application. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

This function is potentially expensive and not thread-safe. It’s best used for debugging or other diagnostics purposes rather than as part of the main execution path of production code.

## See Also

### Creating and Accessing Bundles

- [CFBundleCreate](<cfbundlecreate(____).md>) — Creates a CFBundle object.
- [CFBundleCreateBundlesFromDirectory](<cfbundlecreatebundlesfromdirectory(______).md>) — Searches a directory and constructs an array of CFBundle objects from all valid bundles in the specified directory.
- [CFBundleGetBundleWithIdentifier](<cfbundlegetbundlewithidentifier(__).md>) — Locate a bundle given its program-defined identifier.
- [CFBundleGetMainBundle](<cfbundlegetmainbundle().md>) — Returns an application’s main bundle.
