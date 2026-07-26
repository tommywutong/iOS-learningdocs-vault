---
title: 'path(forAuxiliaryExecutable:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/path(forauxiliaryexecutable:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/path(forauxiliaryexecutable:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/path%28forauxiliaryexecutable%3A%29.json'
content_hash: 'sha256:294dd85d144fdff6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# path(forAuxiliaryExecutable:)

<sub>Instance Method</sub>

Returns the full pathname of the executable with the specified name in the receiver’s bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func path(forAuxiliaryExecutable executableName: String) -> String?
```

## Parameters

- `executableName` — The name of an executable file.

## Return Value

The full pathname of the executable `executableName` in the receiver’s bundle.

## Discussion

This method returns the appropriate path for modern application and framework bundles. This method may not return a path for non-standard bundle formats or for some older bundle formats.

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
- [sharedSupportPath](sharedsupportpath.md) — The full pathname of the bundle’s subdirectory containing shared support files.
