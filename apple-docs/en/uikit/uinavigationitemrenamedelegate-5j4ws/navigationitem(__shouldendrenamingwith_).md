---
title: 'navigationItem(_:shouldEndRenamingWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitem(_:shouldendrenamingwith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitem(_:shouldendrenamingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitemrenamedelegate-5j4ws/navigationitem%28_%3Ashouldendrenamingwith%3A%29.json'
content_hash: 'sha256:b46145d3b31f2235'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItemRenameDelegate](../uinavigationitemrenamedelegate-5j4ws.md)

# navigationItem(_:shouldEndRenamingWith:)

<sub>Instance Method</sub>

Asks the delegate whether to continue or abandon the rename process.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency func navigationItem(_: UINavigationItem, shouldEndRenamingWith title: String) -> Bool
```

## Parameters

- `_` — The navigation item attempting to continue the rename process.

- `title` — The new title of the navigation item.

## Return Value

[true](../../swift/true.md) to continue the rename process; [false](../../swift/false.md) to cancel the rename process.

## Discussion

Implement this method to return [false](../../swift/false.md) to prevent renaming.

> [!important] Important
> UIKit might not call this method in certain situations, like when the system pushes a new navigation item onto the navigation bar. In these situations, UIKit calls [navigationItem(_:didEndRenamingWith:)](<navigationitem(__didendrenamingwith_).md>) instead. Therefore, make sure to implement [navigationItem(_:didEndRenamingWith:)](<navigationitem(__didendrenamingwith_).md>) to handle the cases when [navigationItem(_:shouldEndRenamingWith:)](<navigationitem(__shouldendrenamingwith_).md>) returns [false](../../swift/false.md).

## Default Implementations

### UINavigationItemRenameDelegate Implementations

- [navigationItem(_:shouldEndRenamingWith:)](<navigationitem(__shouldendrenamingwith_)-5ld6b.md>)

## See Also

### Determining rename support

- [navigationItemShouldBeginRenaming(_:)](<navigationitemshouldbeginrenaming(__).md>) — Asks the delegate whether the navigation item supports renaming.
