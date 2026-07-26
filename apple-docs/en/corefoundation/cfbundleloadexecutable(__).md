---
title: 'CFBundleLoadExecutable(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundleloadexecutable(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundleloadexecutable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundleloadexecutable%28_%3A%29.json'
content_hash: 'sha256:fb0d78c988b240e7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleLoadExecutable(_:)

<sub>Function</sub>

Loads a bundle’s main executable code into memory and dynamically links it into the running application.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleLoadExecutable(_ bundle: CFBundle!) -> Bool
```

## Parameters

- `bundle` — The bundle whose main executable you want to load.

## Return Value

`true` if the executable was successfully loaded, otherwise `false`.

## Discussion

You should typically try to avoid using this function, but instead use [CFBundleGetFunctionPointerForName](<cfbundlegetfunctionpointerforname(____).md>) and related functions since these make memory management of the bundle easier.

## See Also

### Loading and Unloading a Bundle

- [CFBundleIsExecutableLoaded](<cfbundleisexecutableloaded(__).md>) — Obtains information about the load status for a bundle’s main executable.
- [CFBundlePreflightExecutable](<cfbundlepreflightexecutable(____).md>) — Returns a Boolean value that indicates whether a given bundle is loaded or appears to be loadable.
- [CFBundleLoadExecutableAndReturnError](<cfbundleloadexecutableandreturnerror(____).md>) — Returns a Boolean value that indicates whether a given bundle is loaded, attempting to load it if necessary.
- [CFBundleUnloadExecutable](<cfbundleunloadexecutable(__).md>) — Unloads the main executable for the specified bundle.
