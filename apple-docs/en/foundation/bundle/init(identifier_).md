---
title: 'init(identifier:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/init(identifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/init(identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/init%28identifier%3A%29.json'
content_hash: 'sha256:af48b4c6710f02e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# init(identifier:)

<sub>Initializer</sub>

Returns the `NSBundle` instance that has the specified bundle identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(identifier: String)
```

## Parameters

- `identifier` — The identifier for an existing `NSBundle` instance.

## Return Value

The `NSBundle` object with the bundle identifier `identifier`, or `nil` if the requested bundle is not found on the system. This method creates and returns a new `NSBundle` object if there is no existing bundle associated with `identifier`. Otherwise, the existing instance is returned.

## Discussion

This method is typically used by frameworks and plug-ins to locate their own bundle at runtime. This method may be somewhat more efficient than trying to locate the bundle using the [+ bundleForClass:](<init(for_).md>) method. However, if the initial lookup of an already loaded and cached bundle with the specified identifier fails, this method uses potentially time-consuming heuristics to attempt to locate the bundle. As an optimization, you can use the [bundleWithPath:](../nsbundle/bundlewithpath_.md) or [+ bundleWithURL:](<init(url_)-a2t0.md>) method instead to avoid file system traversal.

## See Also

### Creating and initializing a bundle

- [+ bundleWithURL:](<init(url_)-a2t0.md>) — Returns an `NSBundle` object that corresponds to the specified file URL.
- [+ bundleForClass:](<init(for_).md>) — Returns the `NSBundle` object with which the specified class is associated.
- [- initWithPath:](<init(path_).md>) — Returns an `NSBundle` object initialized to correspond to the specified directory.
