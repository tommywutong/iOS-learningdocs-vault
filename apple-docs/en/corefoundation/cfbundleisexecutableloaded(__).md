---
title: 'CFBundleIsExecutableLoaded(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundleisexecutableloaded(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundleisexecutableloaded(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundleisexecutableloaded%28_%3A%29.json'
content_hash: 'sha256:99123a058fb14372'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleIsExecutableLoaded(_:)

<sub>Function</sub>

Obtains information about the load status for a bundle’s main executable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleIsExecutableLoaded(_ bundle: CFBundle!) -> Bool
```

## Parameters

- `bundle` — The bundle to examine.

## Return Value

`true` if `bundle`’s main executable has been loaded, otherwise `false`.

## See Also

### Loading and Unloading a Bundle

- [CFBundlePreflightExecutable](<cfbundlepreflightexecutable(____).md>) — Returns a Boolean value that indicates whether a given bundle is loaded or appears to be loadable.
- [CFBundleLoadExecutable](<cfbundleloadexecutable(__).md>) — Loads a bundle’s main executable code into memory and dynamically links it into the running application.
- [CFBundleLoadExecutableAndReturnError](<cfbundleloadexecutableandreturnerror(____).md>) — Returns a Boolean value that indicates whether a given bundle is loaded, attempting to load it if necessary.
- [CFBundleUnloadExecutable](<cfbundleunloadexecutable(__).md>) — Unloads the main executable for the specified bundle.
