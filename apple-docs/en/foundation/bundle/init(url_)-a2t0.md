---
title: 'init(url:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/init(url:)-a2t0'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/init(url:)-a2t0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/init%28url%3A%29-a2t0.json'
content_hash: 'sha256:d2794b4a91a5cb4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# init(url:)

<sub>Initializer</sub>

Returns an `NSBundle` object that corresponds to the specified file URL.

<sub>visionOS</sub>

```swift
convenience init?(url: URL)
```

## Parameters

- `url` — The URL to a directory. This must be a URL for a directory; if it contains any symbolic links, they must be resolvable.

## Return Value

The `NSBundle` object that corresponds to `url`, or `nil` if `url` does not identify an accessible bundle directory.

## Discussion

This method allocates and initializes the returned object if there is no existing `NSBundle` associated with `url`, in which case it returns the existing object.

## See Also

### Creating and initializing a bundle

- [+ bundleForClass:](<init(for_).md>) — Returns the `NSBundle` object with which the specified class is associated.
- [+ bundleWithIdentifier:](<init(identifier_).md>) — Returns the `NSBundle` instance that has the specified bundle identifier.
- [- initWithPath:](<init(path_).md>) — Returns an `NSBundle` object initialized to correspond to the specified directory.
