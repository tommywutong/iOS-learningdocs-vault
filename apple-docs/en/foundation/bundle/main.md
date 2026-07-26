---
title: main
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/main
source_url: 'https://developer.apple.com/documentation/foundation/bundle/main'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/main.json'
content_hash: 'sha256:68e149c881392c42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# main

<sub>Type Property</sub>

Returns the bundle object that contains the current executable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var main: Bundle { get }
```

## Return Value

The `NSBundle` object corresponding to the bundle directory that contains the current executable. This method may return a valid bundle object even for unbundled apps. It may also return `nil` if the bundle object could not be created, so always check the return value.

## Discussion

The main bundle lets you access the resources in the same directory as the currently running executable. For a running app or code running in a framework, the main bundle offers access to the app’s bundle directory.

## See Also

### Related Documentation

- [Resource Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Introduction/Introduction.html#//apple_ref/doc/uid/10000051i)
- [+ bundleForClass:](<init(for_).md>) — Returns the `NSBundle` object with which the specified class is associated.
- [Bundle Programming Guide](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i)

### Getting standard bundle objects

- [allFrameworks](allframeworks.md) — Returns an array of all of the application’s bundles that represent frameworks.
- [allBundles](allbundles.md) — Returns an array of all the application’s non-framework bundles.
