---
title: 'insertElements:beforeCommandForAction:propertyList:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/insertelements:beforecommandforaction:propertylist:'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/insertelements:beforecommandforaction:propertylist:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/insertelements%3Abeforecommandforaction%3Apropertylist%3A.json'
content_hash: 'sha256:23244bf3633fcc73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# insertElements:beforeCommandForAction:propertyList:

<sub>Instance Method</sub>

Insert elements before an identified command.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) insertElements:(NSArray<UIMenuElement *> *) insertedElements beforeCommandForAction:(SEL) siblingAction propertyList:(id) siblingPropertyList;
```

## Parameters

- `insertedElements` — The elements to insert.

- `siblingAction` — The action of the command to insert elements before.

- `siblingPropertyList` — Property list object to distinguish commands, if needed.
