---
title: 'setImage(_:forSegmentAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/setimage(_:forsegmentat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/setimage(_:forsegmentat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/setimage%28_%3Aforsegmentat%3A%29.json'
content_hash: 'sha256:6815bfc2d9c0380c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# setImage(_:forSegmentAt:)

<sub>Instance Method</sub>

Sets the content of a segment to a given image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setImage(_ image: UIImage?, forSegmentAt segment: Int)
```

## Parameters

- `image` — An image object to display in the segment.

- `segment` — An index number identifying a segment in the control. It must be a number between 0 and the number of segments ([numberOfSegments](numberofsegments.md)) minus 1; the segmented control pins values exceeding this upper range to the last segment.

## Discussion

A segment can have only an image or a title; it can’t have both. There’s no default image.

## See Also

### Managing segment content

- [- imageForSegmentAtIndex:](<imageforsegment(at_).md>) — Returns the image for a specific segment.
- [- setTitle:forSegmentAtIndex:](<settitle(__forsegmentat_).md>) — Sets the title of a segment.
- [- titleForSegmentAtIndex:](<titleforsegment(at_).md>) — Returns the title of the specified segment.
