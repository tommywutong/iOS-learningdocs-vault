---
title: UIAccessibilityReadingContent
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilityreadingcontent
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityreadingcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityreadingcontent.json'
content_hash: 'sha256:106af19a95f0293a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityReadingContent

<sub>Protocol</sub>

Methods to implement for an object that represents content that users read, such as a book or an article.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol UIAccessibilityReadingContent
```

## Overview

To give VoiceOver users a superior, continuous reading experience, you can implement this protocol on an element that represents readable content, characterize it with the [UIAccessibilityTraitCausesPageTurn](uiaccessibilitytraits/causespageturn.md) trait, and use the [UIAccessibilityScrollDirectionNext](uiaccessibilityscrolldirection/next.md) and [UIAccessibilityScrollDirectionPrevious](uiaccessibilityscrolldirection/previous.md) constants to enable page turning.

## Topics

### Accessing the content on a page

- [- accessibilityLineNumberForPoint:](<uiaccessibilityreadingcontent/accessibilitylinenumber(for_).md>) — Returns the line number that contains the specified point.
- [- accessibilityAttributedContentForLineNumber:](<uiaccessibilityreadingcontent/accessibilityattributedcontent(forlinenumber_).md>) — Returns the styled text associated with the specified line number.
- [- accessibilityContentForLineNumber:](<uiaccessibilityreadingcontent/accessibilitycontent(forlinenumber_).md>) — Returns the text associated with the specified line number.
- [- accessibilityFrameForLineNumber:](<uiaccessibilityreadingcontent/accessibilityframe(forlinenumber_).md>) — Returns the onscreen frame associated with the specified line number.
- [- accessibilityAttributedPageContent](<uiaccessibilityreadingcontent/accessibilityattributedpagecontent().md>) — Returns the styled text displayed on the current page.
- [- accessibilityPageContent](<uiaccessibilityreadingcontent/accessibilitypagecontent().md>) — Returns the text displayed on the current page.

## See Also

### Behaviors

- [UIAccessibilityFocus](../objectivec/uiaccessibilityfocus.md) — An informal protocol that provides a way to determine whether an assistive app, such as VoiceOver, has focus on an accessible element.
- [UIAccessibilityIdentification](uiaccessibilityidentification.md) — Methods that associate a unique identifier with elements in your user interface.
- [UIAccessibilityContentSizeCategoryImageAdjusting](uiaccessibilitycontentsizecategoryimageadjusting.md) — Methods to determine when to adjust images for different content size categories.
- [UIAccessibilityTextualContext](uiaccessibilitytextualcontext.md) — Constants that describe a named context that helps identify and classify the type of text inside an element.
