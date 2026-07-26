---
title: 'CFBundleUnloadExecutable(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundleunloadexecutable(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundleunloadexecutable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundleunloadexecutable%28_%3A%29.json'
content_hash: 'sha256:c705916e8e69deb8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleUnloadExecutable(_:)

<sub>Function</sub>

Unloads the main executable for the specified bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleUnloadExecutable(_ bundle: CFBundle!)
```

## Parameters

- `bundle` — The bundle whose main executable you want to unload.

## Discussion

You should typically try to avoid using this function, but instead use [CFBundleGetFunctionPointerForName](<cfbundlegetfunctionpointerforname(____).md>) and related functions since these make management of the bundle easier (when the last reference to the CFBundle object is released, and it is finally deallocated, then the code will be unloaded if it is still loaded, and if the executable is of a type that supports unloading).

## See Also

### Loading and Unloading a Bundle

- [CFBundleIsExecutableLoaded](<cfbundleisexecutableloaded(__).md>) — Obtains information about the load status for a bundle’s main executable.
- [CFBundlePreflightExecutable](<cfbundlepreflightexecutable(____).md>) — Returns a Boolean value that indicates whether a given bundle is loaded or appears to be loadable.
- [CFBundleLoadExecutable](<cfbundleloadexecutable(__).md>) — Loads a bundle’s main executable code into memory and dynamically links it into the running application.
- [CFBundleLoadExecutableAndReturnError](<cfbundleloadexecutableandreturnerror(____).md>) — Returns a Boolean value that indicates whether a given bundle is loaded, attempting to load it if necessary.
