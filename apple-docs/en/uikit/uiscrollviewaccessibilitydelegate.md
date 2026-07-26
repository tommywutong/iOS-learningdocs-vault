---
title: UIScrollViewAccessibilityDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollviewaccessibilitydelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollviewaccessibilitydelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollviewaccessibilitydelegate.json'
content_hash: 'sha256:87f300c4d8902db3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIScrollViewAccessibilityDelegate

<sub>Protocol</sub>

A set of methods you can implement to provide accessibility information for a scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIScrollViewAccessibilityDelegate : UIScrollViewDelegate
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIScrollViewDelegate](uiscrollviewdelegate.md)

## Topics

### Providing descriptive information

- [- accessibilityScrollStatusForScrollView:](<uiscrollviewaccessibilitydelegate/accessibilityscrollstatus(for_).md>) — Returns a string describing the content at the current offset in the scroll view.
- [- accessibilityAttributedScrollStatusForScrollView:](<uiscrollviewaccessibilitydelegate/accessibilityattributedscrollstatus(for_).md>) — Returns an attributed string describing the content at the current offset in the scroll view.

## See Also

### Elements

- [UIAccessibilityElement](uiaccessibilityelement.md) — An element that should be accessible to users with disabilities, but that isn’t accessible by default.
- [UIPickerViewAccessibilityDelegate](uipickerviewaccessibilitydelegate.md) — A set of methods you can implement to provide accessibility information for individual components of a picker view.
