---
title: selectedElementDidChangeHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessorypopupmenu/selectedelementdidchangehandler
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessorypopupmenu/selectedelementdidchangehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessorypopupmenu/selectedelementdidchangehandler.json'
content_hash: 'sha256:5f4dcbdd075fcf42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessoryPopUpMenu](../uicellaccessorypopupmenu.md)

# selectedElementDidChangeHandler

<sub>Instance Property</sub>

An optional closure that the system calls when a user selects an element in the menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) void (^selectedElementDidChangeHandler)(UIMenu *menu);
```

## See Also

### Accessing configuration options

- [menu](menu.md) — The menu to display when a user taps the popup menu accessory.
