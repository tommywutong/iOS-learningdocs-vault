---
title: 'CFBundleGetBundleWithIdentifier(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlegetbundlewithidentifier(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlegetbundlewithidentifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlegetbundlewithidentifier%28_%3A%29.json'
content_hash: 'sha256:9add578dada55bad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleGetBundleWithIdentifier(_:)

<sub>Function</sub>

Locate a bundle given its program-defined identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleGetBundleWithIdentifier(_ bundleID: CFString!) -> CFBundle!
```

## Parameters

- `bundleID` — The identifier of the bundle to locate. Note that identifier names are case-sensitive.

## Return Value

A CFBundle object, or `NULL` if the bundle was not found. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

For a bundle to be located using its identifier, the bundle must already have been loaded. The principal purpose for locating bundles by identifier is for code in frameworks or plugins to find its own bundle.

Bundle identifiers are created by entering a value for the key `CFBundleIdentifier` in the bundle’s `Info.plist` file.

To ensure uniqueness, you should create bundle identifiers with the form of reverse-DNS naming style package names, such as `com.MyCompany.MyApp.bundleName`.

### Special Considerations

If a bundle object is created and the bundle file structure later deleted from the filesystem, this function will still return the original bundle object.

## See Also

### Creating and Accessing Bundles

- [CFBundleCreate](<cfbundlecreate(____).md>) — Creates a CFBundle object.
- [CFBundleCreateBundlesFromDirectory](<cfbundlecreatebundlesfromdirectory(______).md>) — Searches a directory and constructs an array of CFBundle objects from all valid bundles in the specified directory.
- [CFBundleGetAllBundles](<cfbundlegetallbundles().md>) — Returns an array containing all of the bundles currently open in the application.
- [CFBundleGetMainBundle](<cfbundlegetmainbundle().md>) — Returns an application’s main bundle.
