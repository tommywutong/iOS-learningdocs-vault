---
title: 'navigationItemShouldBeginRenaming(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitemshouldbeginrenaming(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitemshouldbeginrenaming(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitemshouldbeginrenaming%28_%3A%29.json'
content_hash: 'sha256:96a93229ad612d54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItemRenameDelegate](../uinavigationitemrenamedelegate-5j4ws.md)

# navigationItemShouldBeginRenaming(_:)

<sub>Instance Method</sub>

Asks the delegate whether the navigation item supports renaming.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency func navigationItemShouldBeginRenaming(_: UINavigationItem) -> Bool
```

## Return Value

[true](../../swift/true.md) to support renaming and show Rename in the title menu; otherwise, [false](../../swift/false.md).

## Discussion

UIKit calls this method when the navigation bar’s title menu becomes visible to validate whether to show Rename as part of that menu. Implement this method to determine whether to display the Rename menu element and support the rename process.

## Default Implementations

### UINavigationItemRenameDelegate Implementations

- [navigationItemShouldBeginRenaming(_:)](<navigationitemshouldbeginrenaming(__)-7kane.md>)

## See Also

### Determining rename support

- [navigationItem(_:shouldEndRenamingWith:)](<navigationitem(__shouldendrenamingwith_).md>) — Asks the delegate whether to continue or abandon the rename process.
