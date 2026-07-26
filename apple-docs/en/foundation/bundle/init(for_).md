---
title: 'init(for:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/init(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/init(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/init%28for%3A%29.json'
content_hash: 'sha256:ddae553146c13e88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# init(for:)

<sub>Initializer</sub>

Returns the `NSBundle` object with which the specified class is associated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(for aClass: AnyClass)
```

## Parameters

- `aClass` — A class.

## Return Value

The `NSBundle` object that dynamically loaded `aClass` (a loadable bundle), the `NSBundle` object for the framework in which `aClass` is defined, or the main bundle object if `aClass` was not dynamically loaded or is not defined in a framework. This method creates and returns a new `NSBundle` object if there is no existing bundle associated with `aClass`. Otherwise, the existing instance is returned.

## See Also

### Related Documentation

- [mainBundle](main.md) — Returns the bundle object that contains the current executable.

### Creating and initializing a bundle

- [+ bundleWithURL:](<init(url_)-a2t0.md>) — Returns an `NSBundle` object that corresponds to the specified file URL.
- [+ bundleWithIdentifier:](<init(identifier_).md>) — Returns the `NSBundle` instance that has the specified bundle identifier.
- [- initWithPath:](<init(path_).md>) — Returns an `NSBundle` object initialized to correspond to the specified directory.
