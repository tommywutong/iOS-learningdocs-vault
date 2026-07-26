---
title: 'init(items:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/init(items:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/init(items:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/init%28items%3A%29.json'
content_hash: 'sha256:db7b2acfd72b260e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# init(items:)

<sub>Initializer</sub>

Creates a segmented control with segments having the given titles or images.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(items: [Any]?)
```

## Parameters

- `items` — An array of [NSString](../../foundation/nsstring.md) objects (for segment titles), [UIImage](../uiimage.md) objects (for segment images), or in iOS 14.0 and later [UIAction](../uiaction.md) objects.

## Return Value

A `UISegmentedControl` object or `nil` if there was a problem in initializing the object.

## Discussion

The system automatically sizes the returned segmented control to fit its content within the width of its superview.

## See Also

### Creating a segmented control

- [- initWithFrame:actions:](<init(frame_actions_).md>) — Creates a segmented control with the given frame and adds segments for the actions you specify.
- [- initWithFrame:](<init(frame_).md>) — Creates an empty segmented control with the frame you specify.
- [- initWithCoder:](<init(coder_).md>) — Creates a segmented control with data from an unarchiver.
