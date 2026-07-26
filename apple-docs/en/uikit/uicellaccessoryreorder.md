---
title: UICellAccessoryReorder
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessoryreorder
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessoryreorder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessoryreorder.json'
content_hash: 'sha256:18f6486223982ed5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICellAccessoryReorder

<sub>Class</sub>

The reorder system accessory.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UICellAccessoryReorder : UICellAccessory
```

## Overview

A reorder accessory is three horizontal lines with the default system gray color. This accessory appears on the trailing edge of the cell.

If your collection view supports interactive reordering of its cells, a user can drag the cell by its reorder accessory to change the order of the cell in the collection view.

## Relationships

- **Inherits From**: [UICellAccessory](uicellaccessory-c.class.md)

## Topics

### Accessing configuration options

- [showsVerticalSeparator](uicellaccessoryreorder/showsverticalseparator.md) — A Boolean value that determines whether a vertical separator displays before the accessory when it appears after another accessory.

## See Also

### Creating a system accessory

- [UICellAccessoryDisclosureIndicator](uicellaccessorydisclosureindicator.md) — The disclosure indicator system accessory.
- [UICellAccessoryOutlineDisclosure](uicellaccessoryoutlinedisclosure.md) — The outline disclosure system accessory.
- [UICellAccessoryPopUpMenu](uicellaccessorypopupmenu.md) — The popup menu system accessory.
- [UICellAccessoryCheckmark](uicellaccessorycheckmark.md) — The checkmark system accessory.
- [UICellAccessoryDelete](uicellaccessorydelete.md) — The delete system accessory.
- [UICellAccessoryInsert](uicellaccessoryinsert.md) — The insert system accessory.
- [UICellAccessoryMultiselect](uicellaccessorymultiselect.md) — The multiselect system accessory.
- [UICellAccessoryLabel](uicellaccessorylabel.md) — The label system accessory.
- [UICellAccessoryDetail](uicellaccessorydetail.md) — The detail system accessory.
