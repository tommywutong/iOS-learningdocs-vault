---
title: 'init(fileWrapper:)'
framework: AppKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nstextattachment/init(filewrapper:)'
source_url: 'https://developer.apple.com/documentation/appkit/nstextattachment/init(filewrapper:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextattachment/init%28filewrapper%3A%29.json'
content_hash: 'sha256:6a5b148e710510e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextAttachment](../nstextattachment.md)

# init(fileWrapper:)

<sub>Initializer</sub>

Creates a text attachment object to contain the specified file wrapper.

<sub>macOS</sub>

```swift
convenience init(fileWrapper: FileWrapper?)
```

## Parameters

- `fileWrapper` — The file wrapper for the attachment.

## Return Value

A new text attachment object initialized with the file wrapper.

## Discussion

This method is the designated initializer for the [NSTextAttachment](../nstextattachment.md) class in macOS.

If `aWrapper` contains an image file that the receiver can interpret as an [NSImage](../nsimage.md) object, this method sets the attachment cell’s image to that image rather than to the icon of `aWrapper`.

## See Also

### Initializing a text attachment

- [- initWithData:ofType:](<init(data_oftype_).md>) — Creates a text attachment object with the specified data.
