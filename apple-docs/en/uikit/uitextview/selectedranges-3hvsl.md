---
title: selectedRanges
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/selectedranges-3hvsl
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/selectedranges-3hvsl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/selectedranges-3hvsl.json'
content_hash: 'sha256:0d6245ceb256c60a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# selectedRanges

<sub>Instance Property</sub>

The `NSRange`s of the selection. In most cases, there will only be a single selected range. For cases where bidirectional text is selected, there may be multiple discontiguous ranges. These selected ranges will always be in the normal form, which means they are sorted in ascending order and there are no overlaps. The selected ranges will always be converted to its normal form when they are set. There will always be at least one selected range in this array. So if this array is set to an empty array then the selection will be cleared and a single selected range will be left behind where the length will be 0 and the location will be the location at the end of the selection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nonnull) NSArray<NSValue *> * selectedRanges;
```
