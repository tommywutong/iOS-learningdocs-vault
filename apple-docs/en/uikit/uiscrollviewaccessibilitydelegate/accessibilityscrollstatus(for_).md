---
title: 'accessibilityScrollStatus(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollviewaccessibilitydelegate/accessibilityscrollstatus(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollviewaccessibilitydelegate/accessibilityscrollstatus(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollviewaccessibilitydelegate/accessibilityscrollstatus%28for%3A%29.json'
content_hash: 'sha256:910f2b62f6c265e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollViewAccessibilityDelegate](../uiscrollviewaccessibilitydelegate.md)

# accessibilityScrollStatus(for:)

<sub>Instance Method</sub>

Returns a string describing the content at the current offset in the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func accessibilityScrollStatus(for scrollView: UIScrollView) -> String?
```

## Parameters

- `scrollView` — The scroll view containing the content.

## Return Value

A custom status string for the current offset.

## Discussion

For example, in a user interface that scrolls through the books in a bookcase, you could return “Books 10 through 20”. By default, VoiceOver announces “Page _X_ of _Y_” while scrolling.

Use the [- accessibilityAttributedScrollStatusForScrollView:](<accessibilityattributedscrollstatus(for_).md>) method if portions of your string should be spoken in a different language.

## See Also

### Providing descriptive information

- [- accessibilityAttributedScrollStatusForScrollView:](<accessibilityattributedscrollstatus(for_).md>) — Returns an attributed string describing the content at the current offset in the scroll view.
