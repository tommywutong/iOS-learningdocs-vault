---
title: 'initWithCustomViewProvider:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarviewdecoration/initwithcustomviewprovider:'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarviewdecoration/initwithcustomviewprovider:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarviewdecoration/initwithcustomviewprovider%3A.json'
content_hash: 'sha256:fac047366491978b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [Decoration](../uicalendarview/decoration.md)

# initWithCustomViewProvider:

<sub>Instance Method</sub>

Creates a new calendar view decoration with a custom view, using your view provider.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithCustomViewProvider:(UIView * (^)()) customViewProvider;
```

## Parameters

- `customViewProvider` — A block of code that creates and returns a calendar view decoration.

## Return Value

A calendar view decoration.

## Discussion

Create and return a decoration view for the calendar view in your `customViewProvider` block. The calendar view will clip the decoration view to its parent’s bounds. The decoration view may not have any interactions.

## See Also

### Creating a Custom Decoration View

- [+ decorationWithCustomViewProvider:](<../uicalendarview/decoration/customview(__).md>) — Creates a new calendar view decoration with a custom view, using your view provider.
