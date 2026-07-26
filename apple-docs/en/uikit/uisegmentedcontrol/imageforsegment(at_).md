---
title: 'imageForSegment(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/imageforsegment(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/imageforsegment(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/imageforsegment%28at%3A%29.json'
content_hash: 'sha256:d8ed5758c2640da4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# imageForSegment(at:)

<sub>Instance Method</sub>

Returns the image for a specific segment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func imageForSegment(at segment: Int) -> UIImage?
```

## Parameters

- `segment` — An index number identifying a segment in the control. It must be a number between 0 and the number of segments ([numberOfSegments](numberofsegments.md)) minus 1; the segmented control pins values exceeding this upper range to the last segment.

## Return Value

Returns the image assigned to the receiver as content. If there is no image, it returns `nil`.

## See Also

### Managing segment content

- [- setImage:forSegmentAtIndex:](<setimage(__forsegmentat_).md>) — Sets the content of a segment to a given image.
- [- setTitle:forSegmentAtIndex:](<settitle(__forsegmentat_).md>) — Sets the title of a segment.
- [- titleForSegmentAtIndex:](<titleforsegment(at_).md>) — Returns the title of the specified segment.
