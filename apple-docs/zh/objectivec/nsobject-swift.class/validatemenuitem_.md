---
title: 'validateMenuItem:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/validatemenuitem:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/validatemenuitem:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/validatemenuitem%3A.json'
content_hash: 'sha256:7e9de0bebb8dd03f'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# validateMenuItem:

<sub>实例方法</sub>

实现以覆盖启用或禁用特定菜单项的默认操作。

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) validateMenuItem:(NSMenuItem *) menuItem;
```

## 参数

- `menuItem` — 表示菜单项的 NSMenuItem 对象。

## 返回值

[YES](../yes.md) 以启用 `menuItem`，[NO](../no.md) 以禁用它。

## 讨论

实现此方法的对象必须是 `menuItem` 的目标。你可以通过查询其标记或操作来确定 `menuItem` 是哪个菜单项。

以下示例在表视图中的所选行为最后一行时禁用与 `nextRecord` 操作方法关联的菜单项；相反，当所选行为表视图中的第一行时，禁用操作方法为 `priorRecord` 的菜单项。（`countryKeys` 数组包含出现在表视图中的名称。）

```objc
- (BOOL)validateMenuItem:(NSMenuItem *)item {
    int row = [tableView selectedRow];
    if ([item action] == @selector(nextRecord) &&
        (row == [countryKeys indexOfObject:[countryKeys lastObject]])) {
        return NO;
    }
    if ([item action] == @selector(priorRecord) && row == 0) {
        return NO;
    }
    return YES;
}
```
