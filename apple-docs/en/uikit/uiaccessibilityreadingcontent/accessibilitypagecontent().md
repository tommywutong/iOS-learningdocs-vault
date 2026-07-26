---
title: accessibilityPageContent()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilityreadingcontent/accessibilitypagecontent()
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent/accessibilitypagecontent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityreadingcontent/accessibilitypagecontent%28%29.json'
content_hash: 'sha256:368c84d736d57738'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityReadingContent](../uiaccessibilityreadingcontent.md)

# accessibilityPageContent()

<sub>Instance Method</sub>

Returns the text displayed on the current page.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityPageContent() -> String?
```

## Return Value

A string that contains the text displayed on the current page.

## Discussion

The system tries to call the [- accessibilityAttributedPageContent](<accessibilityattributedpagecontent().md>) method before calling this method.

## See Also

### Accessing the content on a page

- [- accessibilityLineNumberForPoint:](<accessibilitylinenumber(for_).md>) — Returns the line number that contains the specified point.
- [- accessibilityAttributedContentForLineNumber:](<accessibilityattributedcontent(forlinenumber_).md>) — Returns the styled text associated with the specified line number.
- [- accessibilityContentForLineNumber:](<accessibilitycontent(forlinenumber_).md>) — Returns the text associated with the specified line number.
- [- accessibilityFrameForLineNumber:](<accessibilityframe(forlinenumber_).md>) — Returns the onscreen frame associated with the specified line number.
- [- accessibilityAttributedPageContent](<accessibilityattributedpagecontent().md>) — Returns the styled text displayed on the current page.
