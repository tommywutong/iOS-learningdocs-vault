---
title: 'urlForImageResource(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.6+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/urlforimageresource(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/urlforimageresource(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/urlforimageresource%28_%3A%29.json'
content_hash: 'sha256:f6bec1735e1be127'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# urlForImageResource(_:)

<sub>Instance Method</sub>

Returns the location of the specified image resource as an NSURL.

<sub>macOS</sub>

```swift
func urlForImageResource(_ name: NSImage.Name) -> URL?
```

## Parameters

- `name` — The name of the image resource file. Including a filename extension is optional.

## Return Value

An `NSURL` for the resource file or `nil` if the file was not found.

## See Also

### Finding image resources

- [- pathForImageResource:](<pathforimageresource(__).md>) — Returns the location of the specified image resource file.
- [- imageForResource:](<image(forresource_).md>) — Returns an `NSImage` instance associated with the specified name, which can be backed by multiple files representing different resolution versions of the image.
