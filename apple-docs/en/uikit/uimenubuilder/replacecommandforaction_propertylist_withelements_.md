---
title: 'replaceCommandForAction:propertyList:withElements:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/replacecommandforaction:propertylist:withelements:'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/replacecommandforaction:propertylist:withelements:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/replacecommandforaction%3Apropertylist%3Awithelements%3A.json'
content_hash: 'sha256:2ce566ba13df227a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# replaceCommandForAction:propertyList:withElements:

<sub>Instance Method</sub>

Replace an identified command with menu elements.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) replaceCommandForAction:(SEL) replacedAction propertyList:(id) replacedPropertyList withElements:(NSArray<UIMenuElement *> *) replacementElements;
```

## Parameters

- `replacedAction` — The action of the command to be replaced.

- `replacedPropertyList` — Property list object to distinguish commands, if needed.

- `replacementElements` — The replacement elements.
