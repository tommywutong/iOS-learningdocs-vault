---
title: 'pathForImageResource(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/pathforimageresource(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/pathforimageresource(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/pathforimageresource%28_%3A%29.json'
content_hash: 'sha256:96ad71f1676d1923'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# pathForImageResource(_:)

<sub>Instance Method</sub>

Returns the location of the specified image resource file.

<sub>macOS</sub>

```swift
func pathForImageResource(_ name: NSImage.Name) -> String?
```

## Parameters

- `name` — The name of the image resource file, without any pathname information. Including a filename extension is optional.

## Return Value

The absolute pathname of the resource file or `nil` if the file is not found.

## Discussion

Image resources are those files in the bundle that are recognized by the `NSImage` class, including those that can be converted using the Image IO framework.

## See Also

### Related Documentation

- [- pathForResource:ofType:](<path(forresource_oftype_).md>) — Returns the full pathname for the resource identified by the specified name and file extension.

### Finding image resources

- [- URLForImageResource:](<urlforimageresource(__).md>) — Returns the location of the specified image resource as an NSURL.
- [- imageForResource:](<image(forresource_).md>) — Returns an `NSImage` instance associated with the specified name, which can be backed by multiple files representing different resolution versions of the image.
