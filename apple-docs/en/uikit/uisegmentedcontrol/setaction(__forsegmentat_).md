---
title: 'setAction(_:forSegmentAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/setaction(_:forsegmentat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/setaction(_:forsegmentat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/setaction%28_%3Aforsegmentat%3A%29.json'
content_hash: 'sha256:fae32cf8fba650f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# setAction(_:forSegmentAt:)

<sub>Instance Method</sub>

Sets the action for the segment at the index you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setAction(_ action: UIAction, forSegmentAt segment: Int)
```

## Parameters

- `action` — A [UIAction](../uiaction.md) object to set on the segment at the index you specify.

- `segment` — An integer index of a segment.

## Discussion

Segments prefer images over titles when the action contains both. Selecting a segment invokes the action’s [UIActionHandler](../uiactionhandler.md), as well as handlers for the [UIControlEventValueChanged](../uicontrol/event/valuechanged.md) and [UIControlEventPrimaryActionTriggered](../uicontrol/event/primaryactiontriggered.md) control events.

> [!note] Note
> This method asserts an error if the action’s [Identifier](../uiaction/identifier-swift.struct.md) doesn’t match the action of the existing segment at this index, or isn’t unique within all actions associated with the segmented control.

## See Also

### Managing segment actions

- [- actionForSegmentAtIndex:](<actionforsegment(at_).md>) — Fetches the action of the segment at the index you specify, if one exists.
