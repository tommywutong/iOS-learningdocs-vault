---
title: 'panel:compareFilename:with:caseSensitive:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.6 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/panel:comparefilename:with:casesensitive:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/panel:comparefilename:with:casesensitive:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/panel%3Acomparefilename%3Awith%3Acasesensitive%3A.json'
content_hash: 'sha256:9b8c8ca1140c8784'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# panel:compareFilename:with:caseSensitive:

<sub>实例方法</sub>

控制由指定的 `NSSavePanel` 对象呈现的文件的排序。

> [!warning] 已废弃
> There is no replacement.

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSComparisonResult) panel:(id) sender compareFilename:(NSString *) name1 with:(NSString *) name2 caseSensitive:(BOOL) caseSensitive;
```

## 参数

- `sender` — Panel requesting the ordering.

- `name1` — String representing the first filename to order.

- `name2` — String representing the second filename to order.

- `caseSensitive` — 若为 [YES](../yes.md)，则排序区分大小写；若为 [NO](../no.md)，则不区分。

## 返回值

One of the following:

## 讨论

- `NSOrderedAscending` if `fileName1` should precede `fileName2`
- `NSOrderedSame` if the two names are equivalent
- `NSOrderedDescending` if `fileName2` should precede `fileName1`

## 讨论

没有充分理由时不要重新排序“存储”面板中的文件名，因为若某个“存储”面板或“打开”面板中的文件排序与其他此类面板或 Finder 中的不同，可能会让用户感到困惑。“存储”和“打开”面板的默认行为是按文件在 Finder 中出现的顺序排序。另请注意，实现此方法会降低面板的运行性能。
