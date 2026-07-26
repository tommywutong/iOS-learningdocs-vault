---
title: 'init(progressViewStyle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprogressview/init(progressviewstyle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprogressview/init(progressviewstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprogressview/init%28progressviewstyle%3A%29.json'
content_hash: 'sha256:a30fe4a754d0af99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIProgressView](../uiprogressview.md)

# init(progressViewStyle:)

<sub>Initializer</sub>

Creates a progress view with the specified style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(progressViewStyle style: UIProgressView.Style)
```

## Parameters

- `style` — A constant that specifies the style of the object to be created. See [Style](style.md) for descriptions of the style constants.

## Return Value

An initialized [UIProgressView](../uiprogressview.md) object.

## Discussion

[UIProgressView](../uiprogressview.md) sets the height of the returned view according to the specified `style`. You can set and retrieve the style of a progress view through the [progressViewStyle](progressviewstyle.md) property.

## See Also

### Creating a progress view

- [- initWithFrame:](<init(frame_).md>) — Creates a progress view with the specified frame rectangle.
- [- initWithCoder:](<init(coder_).md>) — Creates a progress view from data in an unarchiver.
