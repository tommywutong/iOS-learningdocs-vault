---
title: 'init(style:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontroller/init(style:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/init(style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/init%28style%3A%29.json'
content_hash: 'sha256:9be9dd7dde58843b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# init(style:)

<sub>Initializer</sub>

Creates a split view controller with the specified column style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(style: UISplitViewController.Style)
```

## Parameters

- `style` — The split view controller’s style, which describes how many columns the split view controller displays. You can pass in any of the [Style](style-swift.enum.md) values except [UISplitViewControllerStyleUnspecified](style-swift.enum/unspecified.md).

## See Also

### Creating a split view controller

- [- initWithNibName:bundle:](<init(nibname_bundle_).md>) — Creates a split view controller with the nib file in the specified bundle.
- [- initWithCoder:](<init(coder_).md>) — Creates a split view controller from data in an unarchiver.
