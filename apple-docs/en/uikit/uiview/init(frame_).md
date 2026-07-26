---
title: 'init(frame:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/init(frame:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/init(frame:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/init%28frame%3A%29.json'
content_hash: 'sha256:aa66669bfa69a0e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# init(frame:)

<sub>Initializer</sub>

Creates a view with the specified frame rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(frame: CGRect)
```

## Parameters

- `frame` — The frame rectangle for the view, measured in points. The origin of the frame is relative to the superview in which you plan to add it. This method uses the frame rectangle to set the [center](center.md) and [bounds](bounds.md) properties accordingly.

## Return Value

An initialized view object.

## Discussion

The new view object must be inserted into the view hierarchy of a window before it can be used. If you create a view object programmatically, this method is the designated initializer for the [UIView](../uiview.md) class. Subclasses can override this method to perform any custom initialization but must call `super` at the beginning of their implementation.

If you use Interface Builder to design your interface, this method is not called when your view objects are subsequently loaded from the nib file. Objects in a nib file are reconstituted and then initialized using their [- initWithCoder:](<init(coder_).md>) method, which modifies the attributes of the view to match the attributes stored in the nib file. For detailed information about how views are loaded from a nib file, see [Resource Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Introduction/Introduction.html#//apple_ref/doc/uid/10000051i).

## See Also

### Creating a view object

- [- initWithCoder:](<init(coder_).md>) — Creates a view from data in an unarchiver.
