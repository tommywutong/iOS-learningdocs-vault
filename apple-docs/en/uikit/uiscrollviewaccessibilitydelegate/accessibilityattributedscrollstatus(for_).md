---
title: 'accessibilityAttributedScrollStatus(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollviewaccessibilitydelegate/accessibilityattributedscrollstatus(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollviewaccessibilitydelegate/accessibilityattributedscrollstatus(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollviewaccessibilitydelegate/accessibilityattributedscrollstatus%28for%3A%29.json'
content_hash: 'sha256:63bde0f55e125e63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollViewAccessibilityDelegate](../uiscrollviewaccessibilitydelegate.md)

# accessibilityAttributedScrollStatus(for:)

<sub>Instance Method</sub>

Returns an attributed string describing the content at the current offset in the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func accessibilityAttributedScrollStatus(for scrollView: UIScrollView) -> NSAttributedString?
```

## Parameters

- `scrollView` — The scroll view containing the content.

## Return Value

An attributed string describing the content.

## Discussion

Your implementation of this method returns a description of the content that’s currently visible in the scroll view. Use this method (instead of the [- accessibilityScrollStatusForScrollView:](<accessibilityscrollstatus(for_).md>) method) when you want to include attributes that specify which language to use when speaking the text. For more information, see [UIAccessibilitySpeechAttributeLanguage](../uiaccessibilityspeechattributelanguage.md).

## See Also

### Providing descriptive information

- [- accessibilityScrollStatusForScrollView:](<accessibilityscrollstatus(for_).md>) — Returns a string describing the content at the current offset in the scroll view.
