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
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# tableView:writeRows:toPasteboard:

<sub>实例方法</sub>

将指定行写入指定剪贴板。

> [!warning] 已废弃
> 此方法已弃用。你应改为实现 [tableView(_:writeRowsWith:to:)](<../../appkit/nstableviewdatasource/tableview(__writerowswith_to_).md>)。

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) tableView:(NSTableView *) tableView writeRows:(NSArray *) rows toPasteboard:(NSPasteboard *) pboard;
```

## 参数

- `tableView` — 表格视图。

- `rows` — 行索引数组。

- `pboard` — 剪贴板。

## 返回值

返回 [YES](../yes.md) 以允许拖放；否则返回 [NO](../no.md) 以拒绝拖放。

## 讨论

在已确定应开始拖放、但拖放尚未启动时由 `aTableView` 调用。要拒绝拖放，返回 [NO](../no.md)。要开始拖放，返回 [YES](../yes.md) 并将拖放数据放到 `pboard` 上（数据、所有者等）。一旦此调用返回 [YES](../yes.md)，拖放图像及其他拖放相关信息将由表格视图设置并提供。`rows` 是将参与拖放的行号列表。
