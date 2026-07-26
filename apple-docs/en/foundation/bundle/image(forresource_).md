---
title: 'image(forResource:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/image(forresource:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/image(forresource:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/image%28forresource%3A%29.json'
content_hash: 'sha256:e933cd59493e96b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# image(forResource:)

<sub>Instance Method</sub>

Returns an `NSImage` instance associated with the specified name, which can be backed by multiple files representing different resolution versions of the image.

<sub>macOS</sub>

```swift
func image(forResource name: NSImage.Name) -> NSImage?
```

## Parameters

- `name` — The filename of the image resource file. Including a filename extension is optional.

## Return Value

The `NSImage` object associated with the specified name, or `nil` if no file is found.

## Discussion

This method accommodates Apple’s naming conventions for high-resolution versions of the image. For example, if your bundle contains files named `button.png`, `button@2x.png`, and `button.pdf` then `imageForResource:@"button"` returns an `NSImage` object backed by all three files. Each time the `NSImage` object is drawn, it selects the representation best for the drawing context.

Images requested using this method whose name ends in the word `Template` are automatically marked as template images.

This method does not look up images based on [setName(_:)](<../../appkit/nsimage/setname(__).md>) or get named system images. Use [init(named:)](<../../appkit/nsimage/init(named_).md>) for that purpose.

This method does not cache its search results.

## See Also

### Related Documentation

- [init(named:)](<../../appkit/nsimage/init(named_).md>) — Returns the image object associated with the specified name.

### Finding image resources

- [- URLForImageResource:](<urlforimageresource(__).md>) — Returns the location of the specified image resource as an NSURL.
- [- pathForImageResource:](<pathforimageresource(__).md>) — Returns the location of the specified image resource file.
