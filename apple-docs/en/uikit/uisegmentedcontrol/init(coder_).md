---
title: 'init(coder:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/init(coder:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/init%28coder%3A%29.json'
content_hash: 'sha256:ba01742ef9c7f4e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# init(coder:)

<sub>Initializer</sub>

Creates a segmented control with data from an unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init?(coder: NSCoder)
```

## Parameters

- `coder` — The unarchiver to read data from.

## See Also

### Creating a segmented control

- [- initWithItems:](<init(items_).md>) — Creates a segmented control with segments having the given titles or images.
- [- initWithFrame:actions:](<init(frame_actions_).md>) — Creates a segmented control with the given frame and adds segments for the actions you specify.
- [- initWithFrame:](<init(frame_).md>) — Creates an empty segmented control with the frame you specify.
