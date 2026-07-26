---
title: 'navigationItem:willBeginRenamingWithSuggestedTitle:selectedRange:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationitemrenamedelegate-96g5t/navigationitem:willbeginrenamingwithsuggestedtitle:selectedrange:'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-96g5t/navigationitem:willbeginrenamingwithsuggestedtitle:selectedrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitemrenamedelegate-96g5t/navigationitem%3Awillbeginrenamingwithsuggestedtitle%3Aselectedrange%3A.json'
content_hash: 'sha256:d3f26048c59992e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItemRenameDelegate](../uinavigationitemrenamedelegate-96g5t.md)

# navigationItem:willBeginRenamingWithSuggestedTitle:selectedRange:

<sub>Instance Method</sub>

Tells the delegate when the rename process starts.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (NSString *) navigationItem:(UINavigationItem *) navigationItem willBeginRenamingWithSuggestedTitle:(NSString *) title selectedRange:(NSRange *) selectedRange;
```

## Parameters

- `navigationItem` — The navigation item with the changing title.

- `title` — The initial text to appear in the rename text field.

- `selectedRange` — The selected range of the initial text in the rename text field.

## Return Value

A string that contains the initial text that appears in the rename text field, and a range that determines which part of that text has selection.

## Discussion

UIKit calls this method when the rename process begins. Implement this method to customize the initial text and text selection that appears in the rename text field.

## See Also

### Handling the rename process

- [navigationItem:didEndRenamingWithTitle:](navigationitem_didendrenamingwithtitle_.md) — Tells the delegate when the rename process ends.
