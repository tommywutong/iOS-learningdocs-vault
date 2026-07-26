---
title: 'CFBundleLoadExecutableAndReturnError(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbundleloadexecutableandreturnerror(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbundleloadexecutableandreturnerror(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbundleloadexecutableandreturnerror%28_%3A_%3A%29.json'
content_hash: 'sha256:b426ba29d99dc845'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBundleLoadExecutableAndReturnError(_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a given bundle is loaded, attempting to load it if necessary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBundleLoadExecutableAndReturnError(_ bundle: CFBundle!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

## Parameters

- `bundle` — The bundle to examine.

- `error` — Upon return, if an error occurs contains a CFError that describes the problem. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Return Value

If `bundle` is already loaded, returns `true`. If `bundle` is not already loaded, attempts to load `bundle`; if that attempt succeeds returns `true`, otherwise returns `false`.

## See Also

### Loading and Unloading a Bundle

- [CFBundleIsExecutableLoaded](<cfbundleisexecutableloaded(__).md>) — Obtains information about the load status for a bundle’s main executable.
- [CFBundlePreflightExecutable](<cfbundlepreflightexecutable(____).md>) — Returns a Boolean value that indicates whether a given bundle is loaded or appears to be loadable.
- [CFBundleLoadExecutable](<cfbundleloadexecutable(__).md>) — Loads a bundle’s main executable code into memory and dynamically links it into the running application.
- [CFBundleUnloadExecutable](<cfbundleunloadexecutable(__).md>) — Unloads the main executable for the specified bundle.
