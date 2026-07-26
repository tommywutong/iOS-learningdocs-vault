---
title: 'CFBundleGetFunctionPointerForName(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlegetfunctionpointerforname(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlegetfunctionpointerforname(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlegetfunctionpointerforname%28_%3A_%3A%29.json'
content_hash: 'sha256:a1682953b564e32e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleGetFunctionPointerForName(_:_:)

<sub>Function</sub>

Returns a pointer to a function in a bundle’s executable code using the function name as the search key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleGetFunctionPointerForName(_ bundle: CFBundle!, _ functionName: CFString!) -> UnsafeMutableRawPointer!
```

## Parameters

- `bundle` — The bundle to examine.

- `functionName` — The name of the function to locate.

## Return Value

A pointer to a function in a `bundle`’s executable code, or `NULL` if `functionName` cannot be found. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

Calling this function will cause the bundle’s code to be loaded if necessary.

## See Also

### Managing Executable Code

- [CFBundleGetDataPointerForName](<cfbundlegetdatapointerforname(____).md>) — Returns a data pointer to a symbol of the given name.
- [CFBundleGetDataPointersForNames](<cfbundlegetdatapointersfornames(______).md>) — Returns a C array of data pointer to symbols of the given names.
- [CFBundleGetFunctionPointersForNames](<cfbundlegetfunctionpointersfornames(______).md>) — Constructs a function table containing pointers to all of the functions found in a bundle’s main executable code.
- [CFBundleGetPlugIn](<cfbundlegetplugin(__).md>) — Returns a bundle’s plug-in.
