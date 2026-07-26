---
title: executableURL
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/executableurl
source_url: 'https://developer.apple.com/documentation/foundation/bundle/executableurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/executableurl.json'
content_hash: 'sha256:7ae5add11c8e65b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# executableURL

<sub>Instance Property</sub>

The file URL of the receiver’s executable file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var executableURL: URL? { get }
```

## See Also

### Getting the standard bundle directories

- [resourceURL](resourceurl.md) — The file URL of the bundle’s subdirectory containing resource files.
- [privateFrameworksURL](privateframeworksurl.md) — The file URL of the bundle’s subdirectory containing private frameworks.
- [sharedFrameworksURL](sharedframeworksurl.md) — The file URL of the receiver’s subdirectory containing shared frameworks.
- [builtInPlugInsURL](builtinpluginsurl.md) — The file URL of the receiver’s subdirectory containing plug-ins.
- [- URLForAuxiliaryExecutable:](<url(forauxiliaryexecutable_).md>) — Returns the file URL of the executable with the specified name in the receiver’s bundle.
- [sharedSupportURL](sharedsupporturl.md) — The file URL of the bundle’s subdirectory containing shared support files.
- [appStoreReceiptURL](appstorereceipturl.md) — The file URL for the bundle’s App Store receipt. _(deprecated)_
- [resourcePath](resourcepath.md) — The full pathname of the bundle’s subdirectory containing resources.
- [executablePath](executablepath.md) — The full pathname of the receiver’s executable file.
- [privateFrameworksPath](privateframeworkspath.md) — The full pathname of the bundle’s subdirectory containing private frameworks.
- [sharedFrameworksPath](sharedframeworkspath.md) — The full pathname of the bundle’s subdirectory containing shared frameworks.
- [builtInPlugInsPath](builtinpluginspath.md) — The full pathname of the receiver’s subdirectory containing plug-ins.
- [- pathForAuxiliaryExecutable:](<path(forauxiliaryexecutable_).md>) — Returns the full pathname of the executable with the specified name in the receiver’s bundle.
- [sharedSupportPath](sharedsupportpath.md) — The full pathname of the bundle’s subdirectory containing shared support files.
