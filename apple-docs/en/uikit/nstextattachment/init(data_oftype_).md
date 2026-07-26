---
title: 'init(data:ofType:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextattachment/init(data:oftype:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachment/init(data:oftype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachment/init%28data%3Aoftype%3A%29.json'
content_hash: 'sha256:a340a4108daf3532'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachment](../nstextattachment.md)

# init(data:ofType:)

<sub>Initializer</sub>

Creates a text attachment object with the specified data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(data contentData: Data?, ofType uti: String?)
```

## Parameters

- `contentData` — Data to use for the text attachment contents. Can be `nil`.

- `uti` — A uniform type identifier specifying the data type of the attachment contents. Can be `nil`.

## Return Value

A new `NSTextAttachment` object.

## Discussion

This method is the designated initializer for the `NSTextAttachment` class on iOS.

When either `contentData` or `uti` is `nil`, TextKit considers the receiver to be an attachment without document contents. In this case, the `NSAttributedString` external file writing methods try to save the value of the [image](image.md) property instead.

## See Also

### Initializing a text attachment

- [init(fileWrapper:)](<../../appkit/nstextattachment/init(filewrapper_).md>) — Creates a text attachment object to contain the specified file wrapper.
- [+ textAttachmentWithImage:](<init(image_).md>) — Creates a text attachment object to contain the specified image.
