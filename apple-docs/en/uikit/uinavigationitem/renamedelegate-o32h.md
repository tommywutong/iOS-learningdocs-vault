---
title: renameDelegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/renamedelegate-o32h
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/renamedelegate-o32h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/renamedelegate-o32h.json'
content_hash: 'sha256:23c7b5ae008741a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# renameDelegate

<sub>Instance Property</sub>

The delegate for renaming the navigation item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, weak, readwrite) id<UINavigationItemRenameDelegate> renameDelegate;
```

## Discussion

If you assign a non-`nil` value to this property, UIKit shows an inline text field UI for changing the navigation item’s title. This UI appears when either you or the system calls [- rename:](<../uiresponderstandardeditactions/rename(__).md>) on the navigation controller, which occurs when a person taps Rename in the title menu or when you call [- rename:](<../uiresponderstandardeditactions/rename(__).md>) explicitly.

To show Rename in the navigation item’s title menu, include the Rename menu element in the menu you return from [titleMenuProvider](titlemenuprovider.md). UIKit includes Rename in the set of menu element suggestions it passes in to this closure.

If you only want to show Rename in the title menu, assign a [renameDelegate](renamedelegate-o32h.md) without setting a [titleMenuProvider](titlemenuprovider.md). In this case, UIKit automatically generates a title menu containing the Rename menu element only.

If you set this property to `nil` while a rename operation is in progress, the operation cancels immediately.

## See Also

### Renaming documents

- [UINavigationItemRenameDelegate](../uinavigationitemrenamedelegate-96g5t.md) — Methods an object implements to rename a navigation item.
