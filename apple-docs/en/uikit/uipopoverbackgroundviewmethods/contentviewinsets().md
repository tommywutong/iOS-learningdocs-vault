---
title: contentViewInsets()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverbackgroundviewmethods/contentviewinsets()
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverbackgroundviewmethods/contentviewinsets()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverbackgroundviewmethods/contentviewinsets%28%29.json'
content_hash: 'sha256:280603665b3bb85a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverBackgroundViewMethods](../uipopoverbackgroundviewmethods.md)

# contentViewInsets()

<sub>Type Method</sub>

The insets for the content portion of the popover.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func contentViewInsets() -> UIEdgeInsets
```

## Discussion

Consider your popover background view without the arrow, and the insets in this property represent the distance from a given edge of your background content to the corresponding edge of the popover’s content view. (This edges of the background content should be flush with the frame rectangle of your view, except on the side containing the arrow, of course.) The popover controller uses these values (in combination with the value returned by the [+ arrowHeight](<arrowheight().md>) method) to determine where to position the popover content view. Because the arrow height is accounted for separately, your implementation of this method should return a set of constant values.

## See Also

### Related Documentation

- [+ arrowHeight](<arrowheight().md>) — The height of the arrow (measured in points) from its base to its tip.
