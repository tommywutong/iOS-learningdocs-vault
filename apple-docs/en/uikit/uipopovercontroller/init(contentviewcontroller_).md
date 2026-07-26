---
title: 'init(contentViewController:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipopovercontroller/init(contentviewcontroller:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontroller/init(contentviewcontroller:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontroller/init%28contentviewcontroller%3A%29.json'
content_hash: 'sha256:08efd58f7017da8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverController](../uipopovercontroller.md)

# init(contentViewController:)

<sub>Initializer</sub>

Returns an initialized popover controller object.

> [!warning] Deprecated
> For more information, see [UIPopoverController](../uipopovercontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
init(contentViewController viewController: UIViewController)
```

## Parameters

- `viewController` — The view controller for managing the popover’s content. This parameter must not be `nil`.

## Return Value

An initialized popover controller object.

## Discussion

When initializing a popover controller, you must specify the view controller object whose content is to be displayed in the popover. You can change this view controller later by modifying the [contentViewController](contentviewcontroller.md) property.
