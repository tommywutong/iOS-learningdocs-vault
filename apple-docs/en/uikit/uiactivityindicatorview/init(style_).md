---
title: 'init(style:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiactivityindicatorview/init(style:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityindicatorview/init(style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityindicatorview/init%28style%3A%29.json'
content_hash: 'sha256:c25cb67a0e71e475'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityIndicatorView](../uiactivityindicatorview.md)

# init(style:)

<sub>Initializer</sub>

Creates an activity indicator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(style: UIActivityIndicatorView.Style)
```

## Parameters

- `style` — A constant that specifies the style of the object to be created. See [Style](style-swift.enum.md) for descriptions of the style constants.

## Return Value

An initialized [UIActivityIndicatorView](../uiactivityindicatorview.md) object.

## Discussion

[UIActivityIndicatorView](../uiactivityindicatorview.md) sizes the returned instance according to the specified `style`. You can set and retrieve the style of an activity indicator through the [activityIndicatorViewStyle](style-swift.property.md) property.

## See Also

### Creating an activity indicator

- [- initWithFrame:](<init(frame_).md>) — Creates an activity indicator with the specified frame rectangle.
- [- initWithCoder:](<init(coder_).md>) — Creates an activity indicator from data in an unarchiver.
