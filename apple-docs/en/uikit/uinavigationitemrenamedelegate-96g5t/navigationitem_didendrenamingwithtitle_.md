---
title: 'navigationItem:didEndRenamingWithTitle:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationitemrenamedelegate-96g5t/navigationitem:didendrenamingwithtitle:'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-96g5t/navigationitem:didendrenamingwithtitle:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitemrenamedelegate-96g5t/navigationitem%3Adidendrenamingwithtitle%3A.json'
content_hash: 'sha256:040d27505df42e4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItemRenameDelegate](../uinavigationitemrenamedelegate-96g5t.md)

# navigationItem:didEndRenamingWithTitle:

<sub>Instance Method</sub>

Tells the delegate when the rename process ends.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) navigationItem:(UINavigationItem *) navigationItem didEndRenamingWithTitle:(NSString *) title;
```

## Parameters

- `navigationItem` — The navigation item with the changing title.

- `title` — The new title of the navigation item.

## Discussion

UIKit calls this method after a person finishes renaming the navigation item. Implement this method to update your data model with the new title as needed.

UIKit updates the navigation item’s title automatically. However, if you want to modify the final title that the system passes in to this method, you must update the navigation item’s title manually.

## See Also

### Handling the rename process

- [navigationItem:willBeginRenamingWithSuggestedTitle:selectedRange:](navigationitem_willbeginrenamingwithsuggestedtitle_selectedrange_.md) — Tells the delegate when the rename process starts.
