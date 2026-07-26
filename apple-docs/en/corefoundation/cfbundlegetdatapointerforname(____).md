---
title: 'CFBundleGetDataPointerForName(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlegetdatapointerforname(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlegetdatapointerforname(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlegetdatapointerforname%28_%3A_%3A%29.json'
content_hash: 'sha256:81c850e06cbc09dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleGetDataPointerForName(_:_:)

<sub>Function</sub>

Returns a data pointer to a symbol of the given name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleGetDataPointerForName(_ bundle: CFBundle!, _ symbolName: CFString!) -> UnsafeMutableRawPointer!
```

## Parameters

- `bundle` — The bundle to examine.

- `symbolName` — The name of the symbol you are searching for.

## Return Value

A data pointer to a symbol named `symbolName` in `bundle`, or `NULL` if `symbolName` cannot be found. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Managing Executable Code

- [CFBundleGetDataPointersForNames](<cfbundlegetdatapointersfornames(______).md>) — Returns a C array of data pointer to symbols of the given names.
- [CFBundleGetFunctionPointerForName](<cfbundlegetfunctionpointerforname(____).md>) — Returns a pointer to a function in a bundle’s executable code using the function name as the search key.
- [CFBundleGetFunctionPointersForNames](<cfbundlegetfunctionpointersfornames(______).md>) — Constructs a function table containing pointers to all of the functions found in a bundle’s main executable code.
- [CFBundleGetPlugIn](<cfbundlegetplugin(__).md>) — Returns a bundle’s plug-in.
