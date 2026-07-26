---
title: 'init(path:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/init(path:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/init(path:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/init%28path%3A%29.json'
content_hash: 'sha256:0f93df6005c64e9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# init(path:)

<sub>Initializer</sub>

Returns an `NSBundle` object initialized to correspond to the specified directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(path: String)
```

## Parameters

- `path` — The path to a directory. This must be a full pathname for a directory; if it contains any symbolic links, they must be resolvable.

## Return Value

An `NSBundle` object initialized to correspond to `fullPath`. This method initializes and returns a new instance only if there is no existing bundle associated with `fullPath`, otherwise it deallocates `self` and returns the existing object. If `fullPath` doesn’t exist or the user doesn’t have access to it, returns `nil`.

## Discussion

It’s not necessary to allocate and initialize an instance for the main bundle; use the [mainBundle](main.md) class method to get this instance. You can also use the [bundleWithPath:](../nsbundle/bundlewithpath_.md) class method to obtain a bundle identified by its directory path.

## See Also

### Creating and initializing a bundle

- [+ bundleWithURL:](<init(url_)-a2t0.md>) — Returns an `NSBundle` object that corresponds to the specified file URL.
- [+ bundleForClass:](<init(for_).md>) — Returns the `NSBundle` object with which the specified class is associated.
- [+ bundleWithIdentifier:](<init(identifier_).md>) — Returns the `NSBundle` instance that has the specified bundle identifier.
