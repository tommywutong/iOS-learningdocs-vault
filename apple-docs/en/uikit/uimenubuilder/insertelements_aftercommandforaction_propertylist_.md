---
title: 'insertElements:afterCommandForAction:propertyList:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/insertelements:aftercommandforaction:propertylist:'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/insertelements:aftercommandforaction:propertylist:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/insertelements%3Aaftercommandforaction%3Apropertylist%3A.json'
content_hash: 'sha256:8c1420d87ca04f9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# insertElements:afterCommandForAction:propertyList:

<sub>Instance Method</sub>

Insert elements after an identified command.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) insertElements:(NSArray<UIMenuElement *> *) insertedElements afterCommandForAction:(SEL) siblingAction propertyList:(id) siblingPropertyList;
```

## Parameters

- `insertedElements` — The elements to insert.

- `siblingAction` — The action of the command to insert elements after.

- `siblingPropertyList` — Property list object to distinguish commands, if needed.
