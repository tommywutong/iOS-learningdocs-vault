---
title: 'navigationItem:shouldEndRenamingWithTitle:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationitemrenamedelegate-96g5t/navigationitem:shouldendrenamingwithtitle:'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-96g5t/navigationitem:shouldendrenamingwithtitle:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitemrenamedelegate-96g5t/navigationitem%3Ashouldendrenamingwithtitle%3A.json'
content_hash: 'sha256:91e5bb0adef59cbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItemRenameDelegate](../uinavigationitemrenamedelegate-96g5t.md)

# navigationItem:shouldEndRenamingWithTitle:

<sub>Instance Method</sub>

Asks the delegate whether to continue or abandon the rename process.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) navigationItem:(UINavigationItem *) navigationItem shouldEndRenamingWithTitle:(NSString *) title;
```

## Parameters

- `navigationItem` — The navigation item attempting to continue the rename process.

- `title` — The new title of the navigation item.

## Return Value

[true](../../swift/true.md) to continue the rename process; [false](../../swift/false.md) to cancel the rename process.

## Discussion

Implement this method to return [false](../../swift/false.md) to prevent renaming.

> [!important] Important
> UIKit might not call this method in certain situations, like when the system pushes a new navigation item onto the navigation bar. In these situations, UIKit calls [navigationItem:didEndRenamingWithTitle:](navigationitem_didendrenamingwithtitle_.md) instead. Therefore, make sure to implement [navigationItem:didEndRenamingWithTitle:](navigationitem_didendrenamingwithtitle_.md) to handle the cases when [navigationItem:shouldEndRenamingWithTitle:](navigationitem_shouldendrenamingwithtitle_.md) returns [false](../../swift/false.md).

## See Also

### Determining rename support

- [navigationItemShouldBeginRenaming:](navigationitemshouldbeginrenaming_.md) — Asks the delegate whether the navigation item supports renaming.
