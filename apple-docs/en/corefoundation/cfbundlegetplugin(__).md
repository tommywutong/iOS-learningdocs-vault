---
title: 'CFBundleGetPlugIn(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlegetplugin(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlegetplugin(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlegetplugin%28_%3A%29.json'
content_hash: 'sha256:b237370e4719717e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleGetPlugIn(_:)

<sub>Function</sub>

Returns a bundle’s plug-in.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleGetPlugIn(_ bundle: CFBundle!) -> CFPlugIn!
```

## Parameters

- `bundle` — The bundle to examine.

## Return Value

The plug-in for `bundle`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Managing Executable Code

- [CFBundleGetDataPointerForName](<cfbundlegetdatapointerforname(____).md>) — Returns a data pointer to a symbol of the given name.
- [CFBundleGetDataPointersForNames](<cfbundlegetdatapointersfornames(______).md>) — Returns a C array of data pointer to symbols of the given names.
- [CFBundleGetFunctionPointerForName](<cfbundlegetfunctionpointerforname(____).md>) — Returns a pointer to a function in a bundle’s executable code using the function name as the search key.
- [CFBundleGetFunctionPointersForNames](<cfbundlegetfunctionpointersfornames(______).md>) — Constructs a function table containing pointers to all of the functions found in a bundle’s main executable code.
