---
title: UITableViewCell.FocusStyle.custom
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/focusstyle-swift.enum/custom
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/focusstyle-swift.enum/custom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/focusstyle-swift.enum/custom.json'
content_hash: 'sha256:1c1f0a6158d23354'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITableViewCell](../../uitableviewcell.md) · [FocusStyle](../focusstyle-swift.enum.md)

# UITableViewCell.FocusStyle.custom

<sub>Case</sub>

The cell doesn’t alter its appearance automatically when it becomes focused.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case custom
```

## Discussion

Specifying this style allows you to create your own custom appearance for the cell. It’s recommended that you create custom-looking cells by subclassing [UITableViewCell](../../uitableviewcell.md) and overriding [- didUpdateFocusInContext:withAnimationCoordinator:](<../../uifocusenvironment/didupdatefocus(in_with_).md>).

## See Also

### Constants

- [UITableViewCellFocusStyleDefault](default.md) — The cell alters its appearance in a standard, system-defined way when it becomes focused.
