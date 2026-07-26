---
title: 'accessibilityContent(forLineNumber:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibilityreadingcontent/accessibilitycontent(forlinenumber:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilitycontent(forlinenumber:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityreadingcontent/accessibilitycontent%28forlinenumber%3A%29.json'
content_hash: 'sha256:9b968cd55ae345d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityReadingContent](../uiaccessibilityreadingcontent.md)

# accessibilityContent(forLineNumber:)

<sub>Instance Method</sub>

Returns the text associated with the specified line number.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityContent(forLineNumber lineNumber: Int) -> String?
```

## Parameters

- `lineNumber` — A line number in the receiver’s content.

## Return Value

A string containing the text that is associated with the specified line number, or `nil` if the line number is invalid. By default, this function returns `nil`.

## Discussion

The system tries to call the [- accessibilityAttributedContentForLineNumber:](<accessibilityattributedcontent(forlinenumber_).md>) method before calling this method.

## See Also

### Accessing the content on a page

- [- accessibilityLineNumberForPoint:](<accessibilitylinenumber(for_).md>) — Returns the line number that contains the specified point.
- [- accessibilityAttributedContentForLineNumber:](<accessibilityattributedcontent(forlinenumber_).md>) — Returns the styled text associated with the specified line number.
- [- accessibilityFrameForLineNumber:](<accessibilityframe(forlinenumber_).md>) — Returns the onscreen frame associated with the specified line number.
- [- accessibilityAttributedPageContent](<accessibilityattributedpagecontent().md>) — Returns the styled text displayed on the current page.
- [- accessibilityPageContent](<accessibilitypagecontent().md>) — Returns the text displayed on the current page.
