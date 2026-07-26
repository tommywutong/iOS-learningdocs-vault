---
title: accessibilityAttributedPageContent()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilityreadingcontent/accessibilityattributedpagecontent()
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilityattributedpagecontent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityreadingcontent/accessibilityattributedpagecontent%28%29.json'
content_hash: 'sha256:92af9f15cffb1403'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityReadingContent](../uiaccessibilityreadingcontent.md)

# accessibilityAttributedPageContent()

<sub>Instance Method</sub>

Returns the styled text displayed on the current page.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor optional func accessibilityAttributedPageContent() -> NSAttributedString?
```

## Return Value

An attributed string that contains the text displayed on the current page.

## Discussion

The system tries to call this method before calling the [- accessibilityPageContent](<accessibilitypagecontent().md>) method.

## See Also

### Accessing the content on a page

- [- accessibilityLineNumberForPoint:](<accessibilitylinenumber(for_).md>) — Returns the line number that contains the specified point.
- [- accessibilityAttributedContentForLineNumber:](<accessibilityattributedcontent(forlinenumber_).md>) — Returns the styled text associated with the specified line number.
- [- accessibilityContentForLineNumber:](<accessibilitycontent(forlinenumber_).md>) — Returns the text associated with the specified line number.
- [- accessibilityFrameForLineNumber:](<accessibilityframe(forlinenumber_).md>) — Returns the onscreen frame associated with the specified line number.
- [- accessibilityPageContent](<accessibilitypagecontent().md>) — Returns the text displayed on the current page.
