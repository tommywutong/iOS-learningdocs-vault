---
title: 'init(frame:style:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/init(frame:style:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/init(frame:style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/init%28frame%3Astyle%3A%29.json'
content_hash: 'sha256:bd5d7fbcb12f4774'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# init(frame:style:)

<sub>Initializer</sub>

Creates and returns a table view with the specified frame and style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(frame: CGRect, style: UITableView.Style)
```

## Parameters

- `frame` — A rectangle specifying the initial location and size of the table view in its superview’s coordinates. The frame of the table view changes as table cells are added and deleted.

- `style` — A constant that specifies the style of the table view. For a list of valid styles, see [Style](style-swift.enum.md).

## Return Value

Returns an initialized [UITableView](../uitableview.md) object.

## Discussion

You must specify the style of a table view when you create it, and you can’t change that style later. If you initialize the table view with the [UIView](https://developer.apple.com/library/archive/releasenotes/iPhone/RN-iPhoneSDK/index.html#//apple_ref/doc/uid/TP40007428-CH1-SW18) method [- initWithFrame:](<../uiview/init(frame_).md>), the [UITableViewStylePlain](style-swift.enum/plain.md) style is used as a default.

## See Also

### Creating a table view

- [- initWithCoder:](<init(coder_).md>) — Creates a table view object from data in an unarchiver.
