---
title: 'CFBundleGetDataPointersForNames(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundlegetdatapointersfornames(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundlegetdatapointersfornames(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundlegetdatapointersfornames%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4fc9eeb619edb4a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleGetDataPointersForNames(_:_:_:)

<sub>Function</sub>

Returns a C array of data pointer to symbols of the given names.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleGetDataPointersForNames(_ bundle: CFBundle!, _ symbolNames: CFArray!, _ stbl: UnsafeMutablePointer<UnsafeMutableRawPointer?>!)
```

## Parameters

- `bundle` — The bundle to examine.

- `symbolNames` — A CFArray object containing CFString objects representing the symbol names to search for.

- `stbl` — A C array into which this function stores the data pointers for the symbols specified in `symbolNames`. The array contains `NULL` for any names in `symbolNames` that cannot be found.

## See Also

### Managing Executable Code

- [CFBundleGetDataPointerForName](<cfbundlegetdatapointerforname(____).md>) — Returns a data pointer to a symbol of the given name.
- [CFBundleGetFunctionPointerForName](<cfbundlegetfunctionpointerforname(____).md>) — Returns a pointer to a function in a bundle’s executable code using the function name as the search key.
- [CFBundleGetFunctionPointersForNames](<cfbundlegetfunctionpointersfornames(______).md>) — Constructs a function table containing pointers to all of the functions found in a bundle’s main executable code.
- [CFBundleGetPlugIn](<cfbundlegetplugin(__).md>) — Returns a bundle’s plug-in.
