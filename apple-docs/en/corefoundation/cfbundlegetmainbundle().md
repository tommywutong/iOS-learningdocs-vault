---
title: CFBundleGetMainBundle()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbundlegetmainbundle()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlegetmainbundle()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlegetmainbundle%28%29.json'
content_hash: 'sha256:8037d5cbe7500d78'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleGetMainBundle()

<sub>Function</sub>

Returns an application’s main bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleGetMainBundle() -> CFBundle!
```

## Return Value

A CFBundle object representing the application’s main bundle, or `NULL` if it is not possible to create a bundle. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

CFBundle creates a main bundle whenever it possibly can, even for unbundled apps. There are a few situations in which it is not possible, so you should check the return value against `NULL`, but this happens only in exceptional circumstances.

For an explanation of the main bundle, see [Locating and Opening Bundles](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/AccessingaBundlesContents/AccessingaBundlesContents.html#//apple_ref/doc/uid/10000123i-CH104-SW6) in [Bundle Programming Guide](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i).

## See Also

### Creating and Accessing Bundles

- [CFBundleCreate](<cfbundlecreate(____).md>) — Creates a CFBundle object.
- [CFBundleCreateBundlesFromDirectory](<cfbundlecreatebundlesfromdirectory(______).md>) — Searches a directory and constructs an array of CFBundle objects from all valid bundles in the specified directory.
- [CFBundleGetAllBundles](<cfbundlegetallbundles().md>) — Returns an array containing all of the bundles currently open in the application.
- [CFBundleGetBundleWithIdentifier](<cfbundlegetbundlewithidentifier(__).md>) — Locate a bundle given its program-defined identifier.
