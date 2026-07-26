---
title: 'init(size:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextcontainer/init(size:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontainer/init(size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontainer/init%28size%3A%29.json'
content_hash: 'sha256:d88f8075d90f84a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContainer](../nstextcontainer.md)

# init(size:)

<sub>Initializer</sub>

Initializes a text container with a specified bounding rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(size: CGSize)
```

## Parameters

- `size` — The size of the text container’s bounding rectangle.

## Return Value

The size of the text container’s bounding rectangle.

## Discussion

The new text container must be added to an [NSLayoutManager](../nslayoutmanager.md) object before it can be used. The text container must also have an associated [NSTextView](../../appkit/nstextview.md) object for text to be displayed. This method is the designated initializer for the `NSTextContainer` class.

## See Also

### Related Documentation

- [Text Layout Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextLayout/TextLayout.html#//apple_ref/doc/uid/10000158i)
- [Cocoa Text Architecture Guide](https://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009459)
- [- addTextContainer:](<../nslayoutmanager/addtextcontainer(__).md>) — Appends the specified text container to the series of text containers where the layout manager arranges text.
- [Text System Storage Layer Overview](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextStorageLayer/TextStorageLayer.html#//apple_ref/doc/uid/10000087i)

### Creating a text container

- [- initWithCoder:](<init(coder_).md>) — Creates a text container from data in an unarchiver.
