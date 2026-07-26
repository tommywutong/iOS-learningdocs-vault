---
title: 'navigationItemShouldBeginRenaming:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationitemrenamedelegate-96g5t/navigationitemshouldbeginrenaming:'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-96g5t/navigationitemshouldbeginrenaming:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitemrenamedelegate-96g5t/navigationitemshouldbeginrenaming%3A.json'
content_hash: 'sha256:02726c23f0a19970'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItemRenameDelegate](../uinavigationitemrenamedelegate-96g5t.md)

# navigationItemShouldBeginRenaming:

<sub>Instance Method</sub>

Asks the delegate whether the navigation item supports renaming.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) navigationItemShouldBeginRenaming:(UINavigationItem *) navigationItem;
```

## Parameters

- `navigationItem` — The navigation item asking whether to support renaming.

## Return Value

[true](../../swift/true.md) to support renaming and show Rename in the title menu; otherwise, [false](../../swift/false.md).

## Discussion

UIKit calls this method when the navigation bar’s title menu becomes visible to validate whether to show Rename as part of that menu. Implement this method to determine whether to display the Rename menu element and support the rename process.

## See Also

### Determining rename support

- [navigationItem:shouldEndRenamingWithTitle:](navigationitem_shouldendrenamingwithtitle_.md) — Asks the delegate whether to continue or abandon the rename process.
