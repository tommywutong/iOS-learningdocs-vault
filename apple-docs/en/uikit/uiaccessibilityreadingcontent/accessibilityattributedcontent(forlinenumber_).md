---
title: 'accessibilityAttributedContent(forLineNumber:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibilityreadingcontent/accessibilityattributedcontent(forlinenumber:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilityattributedcontent(forlinenumber:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityreadingcontent/accessibilityattributedcontent%28forlinenumber%3A%29.json'
content_hash: 'sha256:6e32fbf738d778cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityReadingContent](../uiaccessibilityreadingcontent.md)

# accessibilityAttributedContent(forLineNumber:)

<sub>Instance Method</sub>

Returns the styled text associated with the specified line number.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor optional func accessibilityAttributedContent(forLineNumber lineNumber: Int) -> NSAttributedString?
```

## Parameters

- `lineNumber` — A line number in the receiver’s content.

## Return Value

An attributed string containing the text that is associated with the specified line number, or `nil` if the line number is invalid. By default, this function returns `nil`.

## Discussion

The system tries to call this method before calling the [- accessibilityContentForLineNumber:](<accessibilitycontent(forlinenumber_).md>) method.

## See Also

### Accessing the content on a page

- [- accessibilityLineNumberForPoint:](<accessibilitylinenumber(for_).md>) — Returns the line number that contains the specified point.
- [- accessibilityContentForLineNumber:](<accessibilitycontent(forlinenumber_).md>) — Returns the text associated with the specified line number.
- [- accessibilityFrameForLineNumber:](<accessibilityframe(forlinenumber_).md>) — Returns the onscreen frame associated with the specified line number.
- [- accessibilityAttributedPageContent](<accessibilityattributedpagecontent().md>) — Returns the styled text displayed on the current page.
- [- accessibilityPageContent](<accessibilitypagecontent().md>) — Returns the text displayed on the current page.
