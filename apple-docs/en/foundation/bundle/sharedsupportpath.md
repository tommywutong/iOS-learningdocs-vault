---
title: sharedSupportPath
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/sharedsupportpath
source_url: 'https://developer.apple.com/documentation/foundation/bundle/sharedsupportpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/sharedsupportpath.json'
content_hash: 'sha256:d32c0d1d2755a0aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# sharedSupportPath

<sub>Instance Property</sub>

The full pathname of the bundle’s subdirectory containing shared support files.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sharedSupportPath: String? { get }
```

## Discussion

This property contains the appropriate path for modern application and framework bundles. This property may not contain a path for non-standard bundle formats or for some older bundle formats.

## See Also

### Getting the standard bundle directories

- [resourceURL](resourceurl.md) — The file URL of the bundle’s subdirectory containing resource files.
- [executableURL](executableurl.md) — The file URL of the receiver’s executable file.
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
