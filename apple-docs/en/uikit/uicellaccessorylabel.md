---
title: UICellAccessoryLabel
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessorylabel
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessorylabel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessorylabel.json'
content_hash: 'sha256:e7073029612a6dd2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICellAccessoryLabel

<sub>Class</sub>

The label system accessory.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UICellAccessoryLabel : UICellAccessory
```

## Overview

A label cell accessory appears on the trailing edge of the cell. Use this cell accessory to display a short string of text, like a small number showing the count for the associated item.

## Relationships

- **Inherits From**: [UICellAccessory](uicellaccessory-c.class.md)

## Topics

### Creating configuration options

- [initWithText:](uicellaccessorylabel/initwithtext_.md) — Creates a label accessory with the specified text.
- [initWithCoder:](uicellaccessorylabel/initwithcoder_.md) — Creates a label accessory from data in an unarchiver.

### Accessing configuration options

- [text](uicellaccessorylabel/text.md) — The text for the label to display.
- [font](uicellaccessorylabel/font.md) — The font for the label.
- [adjustsFontForContentSizeCategory](uicellaccessorylabel/adjustsfontforcontentsizecategory.md) — A Boolean value that determines whether the label automatically adjusts its font according to the content size category.

## See Also

### Creating a system accessory

- [UICellAccessoryDisclosureIndicator](uicellaccessorydisclosureindicator.md) — The disclosure indicator system accessory.
- [UICellAccessoryOutlineDisclosure](uicellaccessoryoutlinedisclosure.md) — The outline disclosure system accessory.
- [UICellAccessoryPopUpMenu](uicellaccessorypopupmenu.md) — The popup menu system accessory.
- [UICellAccessoryCheckmark](uicellaccessorycheckmark.md) — The checkmark system accessory.
- [UICellAccessoryDelete](uicellaccessorydelete.md) — The delete system accessory.
- [UICellAccessoryInsert](uicellaccessoryinsert.md) — The insert system accessory.
- [UICellAccessoryReorder](uicellaccessoryreorder.md) — The reorder system accessory.
- [UICellAccessoryMultiselect](uicellaccessorymultiselect.md) — The multiselect system accessory.
- [UICellAccessoryDetail](uicellaccessorydetail.md) — The detail system accessory.
