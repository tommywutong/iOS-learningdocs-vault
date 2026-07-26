---
title: 'accessibilityFrame(forLineNumber:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibilityreadingcontent/accessibilityframe(forlinenumber:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilityframe(forlinenumber:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityreadingcontent/accessibilityframe%28forlinenumber%3A%29.json'
content_hash: 'sha256:1d226be8219d0d9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityReadingContent](../uiaccessibilityreadingcontent.md)

# accessibilityFrame(forLineNumber:)

<sub>Instance Method</sub>

Returns the onscreen frame associated with the specified line number.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityFrame(forLineNumber lineNumber: Int) -> CGRect
```

## Parameters

- `lineNumber` — The line number.

## Return Value

The frame in the receiver that contains the specified line number, in screen coordinates. By default, this method returns `CGRectZero`.

## Discussion

To determine the onscreen rectangle (or frame) of a line, you can use code such as the following:

**Swift**

```swift
let lineBounds: CGRect = // the bounds of the line in view space
let view: UIView = // the relevant view
return UIAccessibilityConvertFrameToScreenCoordinates(lineBounds, view)
```

**Objective-C**

```objc
CGRect lineBounds = // The bounds of the line in view space.
UIView *view = // The relevant view.
return UIAccessibilityConvertFrameToScreenCoordinates(lineBounds, view);
```

## See Also

### Related Documentation

- [UIAccessibilityConvertFrameToScreenCoordinates](<../uiaccessibility/converttoscreencoordinates(__in_)-9ziiu.md>) — Converts the specified rectangle from view coordinates to screen coordinates.

### Accessing the content on a page

- [- accessibilityLineNumberForPoint:](<accessibilitylinenumber(for_).md>) — Returns the line number that contains the specified point.
- [- accessibilityAttributedContentForLineNumber:](<accessibilityattributedcontent(forlinenumber_).md>) — Returns the styled text associated with the specified line number.
- [- accessibilityContentForLineNumber:](<accessibilitycontent(forlinenumber_).md>) — Returns the text associated with the specified line number.
- [- accessibilityAttributedPageContent](<accessibilityattributedpagecontent().md>) — Returns the styled text displayed on the current page.
- [- accessibilityPageContent](<accessibilitypagecontent().md>) — Returns the text displayed on the current page.
