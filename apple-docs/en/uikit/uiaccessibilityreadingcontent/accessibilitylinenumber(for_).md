---
title: 'accessibilityLineNumber(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibilityreadingcontent/accessibilitylinenumber(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilitylinenumber(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityreadingcontent/accessibilitylinenumber%28for%3A%29.json'
content_hash: 'sha256:03f228d70505cb13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityReadingContent](../uiaccessibilityreadingcontent.md)

# accessibilityLineNumber(for:)

<sub>Instance Method</sub>

Returns the line number that contains the specified point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityLineNumber(for point: CGPoint) -> Int
```

## Parameters

- `point` — A point within the bounds of the receiver’s view space, in screen coordinates. That is, a point for which `[self pointInside:point withEvent:event] == YES`.

## Return Value

The line number that contains the specified point or `NSNotFound` if the point indicates an empty area within the receiver’s rectangle. By default, this method returns `NSNotFound`.

## Discussion

This method is called only when `point` is within the bounds of the view or element.

## See Also

### Related Documentation

- [UIAccessibilityConvertFrameToScreenCoordinates](<../uiaccessibility/converttoscreencoordinates(__in_)-9ziiu.md>) — Converts the specified rectangle from view coordinates to screen coordinates.

### Accessing the content on a page

- [- accessibilityAttributedContentForLineNumber:](<accessibilityattributedcontent(forlinenumber_).md>) — Returns the styled text associated with the specified line number.
- [- accessibilityContentForLineNumber:](<accessibilitycontent(forlinenumber_).md>) — Returns the text associated with the specified line number.
- [- accessibilityFrameForLineNumber:](<accessibilityframe(forlinenumber_).md>) — Returns the onscreen frame associated with the specified line number.
- [- accessibilityAttributedPageContent](<accessibilityattributedpagecontent().md>) — Returns the styled text displayed on the current page.
- [- accessibilityPageContent](<accessibilitypagecontent().md>) — Returns the text displayed on the current page.
