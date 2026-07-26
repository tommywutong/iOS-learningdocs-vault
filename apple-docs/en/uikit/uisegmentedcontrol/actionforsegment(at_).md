---
title: 'actionForSegment(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/actionforsegment(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/actionforsegment(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/actionforsegment%28at%3A%29.json'
content_hash: 'sha256:355c26eac6ae7e20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# actionForSegment(at:)

<sub>Instance Method</sub>

Fetches the action of the segment at the index you specify, if one exists.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func actionForSegment(at segment: Int) -> UIAction?
```

## Parameters

- `segment` — An integer value index of a segment.

## Return Value

The [UIAction](../uiaction.md) for the segment at the index you specify, or `nil` if the segment doesn’t have an action assigned.

## See Also

### Managing segment actions

- [- setAction:forSegmentAtIndex:](<setaction(__forsegmentat_).md>) — Sets the action for the segment at the index you specify.
