---
title: UICellAccessoryOutlineDisclosure
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessoryoutlinedisclosure
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessoryoutlinedisclosure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessoryoutlinedisclosure.json'
content_hash: 'sha256:8608ce1378eb52f4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICellAccessoryOutlineDisclosure

<sub>Class</sub>

The outline disclosure system accessory.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UICellAccessoryOutlineDisclosure : UICellAccessory
```

## Overview

An outline disclosure is a rotating chevron for use in outlines. In iOS and for headers in Mac Catalyst, this accessory appears on the trailing edge. For cells in Mac Catalyst, this accessory appears on the leading edge.

Use this cell accessory to indicate that an item can expand and collapse, and to enable the user to toggle between the expanded and collapsed states.

## Relationships

- **Inherits From**: [UICellAccessory](uicellaccessory-c.class.md)

## Topics

### Accessing configuration options

- [actionHandler](uicellaccessoryoutlinedisclosure/actionhandler.md) — A handler that the system calls when a user interacts with the accessory.
- [style](uicellaccessoryoutlinedisclosure/style.md) — The style of the outline disclosure accessory.
- [UICellAccessoryOutlineDisclosureStyle](uicellaccessoryoutlinedisclosurestyle.md) — Constants that describe the style of the outline disclosure accessory.

## See Also

### Creating a system accessory

- [UICellAccessoryDisclosureIndicator](uicellaccessorydisclosureindicator.md) — The disclosure indicator system accessory.
- [UICellAccessoryPopUpMenu](uicellaccessorypopupmenu.md) — The popup menu system accessory.
- [UICellAccessoryCheckmark](uicellaccessorycheckmark.md) — The checkmark system accessory.
- [UICellAccessoryDelete](uicellaccessorydelete.md) — The delete system accessory.
- [UICellAccessoryInsert](uicellaccessoryinsert.md) — The insert system accessory.
- [UICellAccessoryReorder](uicellaccessoryreorder.md) — The reorder system accessory.
- [UICellAccessoryMultiselect](uicellaccessorymultiselect.md) — The multiselect system accessory.
- [UICellAccessoryLabel](uicellaccessorylabel.md) — The label system accessory.
- [UICellAccessoryDetail](uicellaccessorydetail.md) — The detail system accessory.
