---
title: icon
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filewrapper/icon
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/icon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/icon.json'
content_hash: 'sha256:47d705bde1a4a694'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# icon

<sub>Instance Property</sub>

The icon that represents the file wrapper.

<sub>macOS</sub>

```swift
var icon: NSImage? { get set }
```

## Discussion

You don’t have to use this icon; for example, a file viewer typically looks up icons automatically based on file extensions, and so wouldn’t need this one. Similarly, if a file wrapper represents an image file, you can display the image directly rather than a file icon.

This method may return `nil` if the file wrapper is a child created when its parent was read from the file system, and the child was modified before it was read. Use the `NSFileWrapperReadingImmediate` reading option to reduce the likelihood of that problem.

Because the `NSImage` object that’s returned might be shared by many [FileWrapper](../filewrapper.md) objects, you must not mutate it. If you need to mutate the returned object, make a copy first and mutate the copy instead.
