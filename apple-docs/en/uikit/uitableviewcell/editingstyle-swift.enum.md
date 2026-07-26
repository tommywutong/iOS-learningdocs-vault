---
title: UITableViewCell.EditingStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/editingstyle-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/editingstyle-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/editingstyle-swift.enum.json'
content_hash: 'sha256:30139d395af2573a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# UITableViewCell.EditingStyle

<sub>Enumeration</sub>

The editing control used by a cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum EditingStyle
```

## Overview

Use these constants with the [editingStyle](editingstyle-swift.property.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UITableViewCellEditingStyleNone](editingstyle-swift.enum/none.md) — The cell has no editing control.
- [UITableViewCellEditingStyleDelete](editingstyle-swift.enum/delete.md) — The cell has the delete editing control; this control is a red circle enclosing a minus sign.
- [UITableViewCellEditingStyleInsert](editingstyle-swift.enum/insert.md) — The cell has the insert editing control; this control is a green circle enclosing a plus sign.

### Initializers

- [init(rawValue:)](<editingstyle-swift.enum/init(rawvalue_).md>)

## See Also

### Editing the cell

- [editing](isediting.md) — A Boolean value that indicates whether the cell is in an editable state.
- [- setEditing:animated:](<setediting(__animated_).md>) — Toggles the cell into and out of editing mode.
- [editingStyle](editingstyle-swift.property.md) — The editing style of the cell.
- [showingDeleteConfirmation](showingdeleteconfirmation.md) — A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.
- [showsReorderControl](showsreordercontrol.md) — A Boolean value that determines whether the cell shows the reordering control.
