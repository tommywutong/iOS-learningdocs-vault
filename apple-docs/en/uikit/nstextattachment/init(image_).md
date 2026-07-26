---
title: 'init(image:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextattachment/init(image:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachment/init(image:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachment/init%28image%3A%29.json'
content_hash: 'sha256:1cfae2781df15578'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachment](../nstextattachment.md)

# init(image:)

<sub>Initializer</sub>

Creates a text attachment object to contain the specified image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(image: UIImage)
```

## Parameters

- `image` — The image for the attachment.

## Return Value

A new text attachment object initialized with the image.

## Discussion

Attachments created with this method automatically adapt to the surrounding font and color attributes in attributed strings.

For example, the following code creates a text attachment from the [UIImage](../uiimage.md) class using an SF symbol in a blue headline style and embeds it at the end of the [NSMutableAttributedString](../../foundation/nsmutableattributedstring.md) class:

```swift
let content = NSMutableAttributedString(string: "Open ")
guard let lockImage = UIImage(systemName: "lock") else {
    return
}
let attributes: [NSAttributedString.Key: Any] = [
    .foregroundColor: UIColor.blue,
    .font: UIFont.preferredFont(forTextStyle: .headline)
]
let lockSymbol = NSMutableAttributedString(
    attachment: NSTextAttachment(image: lockImage)
)
lockSymbol.addAttributes(attributes, 
                         range: NSRange(location: 0, length: 1))
content.insert(lockSymbol, at: 5)

```

## See Also

### Initializing a text attachment

- [init(fileWrapper:)](<../../appkit/nstextattachment/init(filewrapper_).md>) — Creates a text attachment object to contain the specified file wrapper.
- [- initWithData:ofType:](<init(data_oftype_).md>) — Creates a text attachment object with the specified data.
