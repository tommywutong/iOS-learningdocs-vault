---
title: 'init(url:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/init(url:)-3n9rf'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/init(url:)-3n9rf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/init%28url%3A%29-3n9rf.json'
content_hash: 'sha256:4813e080317a7ceb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# init(url:)

<sub>Initializer</sub>

Returns an `NSBundle` object initialized to correspond to the specified file URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
convenience init?(url: URL)
```

## Parameters

- `url` — The file URL to a directory. This must be a full URL for a directory; if it contains any symbolic links, they must be resolvable.

## Return Value

An `NSBundle` object initialized to correspond to @c url, or @c nil if @c url doesn’t exist or the user doesn’t have access to it.

## Discussion

This method initializes and returns a new instance only if there is no existing bundle associated with @c url, otherwise it deallocates @c self and returns the existing object.
