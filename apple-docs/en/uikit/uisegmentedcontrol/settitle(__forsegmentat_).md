---
title: 'setTitle(_:forSegmentAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/settitle(_:forsegmentat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/settitle(_:forsegmentat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/settitle%28_%3Aforsegmentat%3A%29.json'
content_hash: 'sha256:b111bb10227eb487'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# setTitle(_:forSegmentAt:)

<sub>Instance Method</sub>

Sets the title of a segment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setTitle(_ title: String?, forSegmentAt segment: Int)
```

## Parameters

- `title` — A string to display in the segment as its title.

- `segment` — An index number identifying a segment in the control. It must be a number between 0 and the number of segments ([numberOfSegments](numberofsegments.md)) minus 1; the segmented control pins values exceeding this upper range to the last segment.

## Discussion

A segment can have only an image or a title; it can’t have both. There’s no default title.

## See Also

### Managing segment content

- [- setImage:forSegmentAtIndex:](<setimage(__forsegmentat_).md>) — Sets the content of a segment to a given image.
- [- imageForSegmentAtIndex:](<imageforsegment(at_).md>) — Returns the image for a specific segment.
- [- titleForSegmentAtIndex:](<titleforsegment(at_).md>) — Returns the title of the specified segment.
