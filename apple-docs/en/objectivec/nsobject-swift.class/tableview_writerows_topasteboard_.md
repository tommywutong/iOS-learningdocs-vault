---
title: 'tableView:writeRows:toPasteboard:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/tableview:writerows:topasteboard:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/tableview:writerows:topasteboard:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/tableview%3Awriterows%3Atopasteboard%3A.json'
content_hash: 'sha256:f951107f30909649'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# tableView:writeRows:toPasteboard:

<sub>Instance Method</sub>

Writes the specified rows to the specified pasteboard.

> [!warning] Deprecated
> This method has been deprecated. You should implement [tableView(_:writeRowsWith:to:)](<../../appkit/nstableviewdatasource/tableview(__writerowswith_to_).md>) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) tableView:(NSTableView *) tableView writeRows:(NSArray *) rows toPasteboard:(NSPasteboard *) pboard;
```

## Parameters

- `tableView` — The table view.

- `rows` — An array of row indexes.

- `pboard` — The pasteboard.

## Return Value

Return [YES](../yes.md) to allow the drag: otherwise [NO](../no.md) to refuse the drag.

## Discussion

Invoked by `aTableView` after it has been determined that a drag should begin, but before the drag has been started. To refuse the drag, return [NO](../no.md). To start a drag, return [YES](../yes.md) and place the drag data onto `pboard` (data, owner, and so on). The drag image and other drag-related information will be set up and provided by the table view once this call returns with [YES](../yes.md). `rows` is the list of row numbers that will be participating in the drag.
