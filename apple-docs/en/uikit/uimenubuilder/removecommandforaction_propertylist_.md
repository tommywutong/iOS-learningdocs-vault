---
title: 'removeCommandForAction:propertyList:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/removecommandforaction:propertylist:'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/removecommandforaction:propertylist:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/removecommandforaction%3Apropertylist%3A.json'
content_hash: 'sha256:b8972135888be086'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# removeCommandForAction:propertyList:

<sub>Instance Method</sub>

Remove an identified command.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) removeCommandForAction:(SEL) removedAction propertyList:(id) removedPropertyList;
```

## Parameters

- `removedAction` — The action of the command to remove.

- `removedPropertyList` — Property list object to distinguish commands, if needed.
