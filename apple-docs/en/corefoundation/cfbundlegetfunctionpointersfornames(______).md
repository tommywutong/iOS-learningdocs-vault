---
title: 'CFBundleGetFunctionPointersForNames(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlegetfunctionpointersfornames(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlegetfunctionpointersfornames(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlegetfunctionpointersfornames%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:662aeaf033a9d4dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleGetFunctionPointersForNames(_:_:_:)

<sub>Function</sub>

Constructs a function table containing pointers to all of the functions found in a bundle’s main executable code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleGetFunctionPointersForNames(_ bundle: CFBundle!, _ functionNames: CFArray!, _ ftbl: UnsafeMutablePointer<UnsafeMutableRawPointer?>!)
```

## Parameters

- `bundle` — The bundle to examine.

- `functionNames` — A CFArray object containing a list of the function names to locate.

- `ftbl` — A C array into which this function stores the function pointers for the symbols specified in `functionNames`. The array contains `NULL` for any names in `functionNames` that cannot be found.

## Discussion

Calling this function causes the bundle’s code to be loaded if necessary.

## See Also

### Managing Executable Code

- [CFBundleGetDataPointerForName](<cfbundlegetdatapointerforname(____).md>) — Returns a data pointer to a symbol of the given name.
- [CFBundleGetDataPointersForNames](<cfbundlegetdatapointersfornames(______).md>) — Returns a C array of data pointer to symbols of the given names.
- [CFBundleGetFunctionPointerForName](<cfbundlegetfunctionpointerforname(____).md>) — Returns a pointer to a function in a bundle’s executable code using the function name as the search key.
- [CFBundleGetPlugIn](<cfbundlegetplugin(__).md>) — Returns a bundle’s plug-in.
