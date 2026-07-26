---
title: 'titleForSegment(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/titleforsegment(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/titleforsegment(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/titleforsegment%28at%3A%29.json'
content_hash: 'sha256:0969e039a7719062'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# titleForSegment(at:)

<sub>Instance Method</sub>

Returns the title of the specified segment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func titleForSegment(at segment: Int) -> String?
```

## Parameters

- `segment` — An index number identifying a segment in the control. It must be a number between 0 and the number of segments ([numberOfSegments](numberofsegments.md)) minus 1; the segmented control pins values exceeding this upper range to the last segment.

## Return Value

Returns the string (title) assigned to the receiver as content. If there is no title, it returns `nil`.

## See Also

### Managing segment content

- [- setImage:forSegmentAtIndex:](<setimage(__forsegmentat_).md>) — Sets the content of a segment to a given image.
- [- imageForSegmentAtIndex:](<imageforsegment(at_).md>) — Returns the image for a specific segment.
- [- setTitle:forSegmentAtIndex:](<settitle(__forsegmentat_).md>) — Sets the title of a segment.
