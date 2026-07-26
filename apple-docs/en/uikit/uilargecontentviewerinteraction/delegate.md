---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilargecontentviewerinteraction/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uilargecontentviewerinteraction/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilargecontentviewerinteraction/delegate.json'
content_hash: 'sha256:097903520d7ef0bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILargeContentViewerInteraction](../uilargecontentviewerinteraction.md)

# delegate

<sub>Instance Property</sub>

An object that can fine-tune the large content viewer interactions, especially in the presence of other gesture recognizers.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UILargeContentViewerInteractionDelegate)? { get }
```

## See Also

### Customizing large content viewer interactions

- [gestureRecognizerForExclusionRelationship](gesturerecognizerforexclusionrelationship.md) — A gesture recognizer that you can use to set up simultaneous recognition or failure relationships with other gesture recognizers.
