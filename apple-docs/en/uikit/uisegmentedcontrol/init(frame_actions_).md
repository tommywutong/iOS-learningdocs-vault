---
title: 'init(frame:actions:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/init(frame:actions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/init(frame:actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/init%28frame%3Aactions%3A%29.json'
content_hash: 'sha256:6b5a6b5d55fdbde9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# init(frame:actions:)

<sub>Initializer</sub>

Creates a segmented control with the given frame and adds segments for the actions you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(frame: CGRect, actions: [UIAction])
```

## Parameters

- `frame` — A rectangle that specifies the segmented control’s frame in a superview’s coordinate system.

- `actions` — An array of [UIAction](../uiaction.md) objects.

## Discussion

Segments prefer images over titles when the action contains both. Selecting a segment invokes the action’s [UIActionHandler](../uiactionhandler.md), as well as handlers for the [UIControlEventValueChanged](../uicontrol/event/valuechanged.md) and [UIControlEventPrimaryActionTriggered](../uicontrol/event/primaryactiontriggered.md) control events.

## See Also

### Creating a segmented control

- [- initWithItems:](<init(items_).md>) — Creates a segmented control with segments having the given titles or images.
- [- initWithFrame:](<init(frame_).md>) — Creates an empty segmented control with the frame you specify.
- [- initWithCoder:](<init(coder_).md>) — Creates a segmented control with data from an unarchiver.
