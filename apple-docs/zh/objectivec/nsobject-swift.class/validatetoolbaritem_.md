---
title: 'validateToolbarItem:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/validatetoolbaritem:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/validatetoolbaritem:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/validatetoolbaritem%3A.json'
content_hash: 'sha256:69dc5eaf422031cf'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# validateToolbarItem:

<sub>实例方法</sub>

若实现此方法并返回 `false`，NSToolbar 将禁用 `theItem`；返回 `true` 会使 `theItem` 启用。

<sub>macOS</sub>

```objc
- (BOOL) validateToolbarItem:(NSToolbarItem *) item;
```

## 讨论

NSToolbar 仅对图像项调用此方法。

> [!note] 注意
> [validateToolbarItem:](validatetoolbaritem_.md) 被非常频繁地调用，因此必须高效。

若接收者是多个工具栏项操作的 `target`，则有必要通过测试 `itemIdentifier` 来确定 `theItem` 指的是哪个工具栏项。

```objc
-(BOOL)validateToolbarItem:(NSToolbarItem *)toolbarItem
{
    BOOL enable = NO;
    if ([[toolbarItem itemIdentifier] isEqual:SaveDocToolbarItemIdentifier]) {
        // We will return YES (enable the save item)
        // only when the document is dirty and needs saving
        enable = [self isDocumentEdited];
    } else if ([[toolbarItem itemIdentifier] isEqual:NSToolbarPrintItemIdentifier]) {
        // always enable print for this window
        enable = YES;
    }
    return enable;
}
```

## 另请参阅

### 相关文档

- [validateVisibleItems()](<../../appkit/nstoolbar/validatevisibleitems().md>) — 在窗口更新期间验证工具栏的可见项。
- [action](../../appkit/nstoolbaritem/action.md) — 有人点击工具栏项时要调用的操作方法。
- [target](../../appkit/nstoolbaritem/target.md) — 定义工具栏项在被点击时调用的操作方法的对象。
- [Toolbar Programming Topics for Cocoa](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Toolbars/Toolbars.html#//apple_ref/doc/uid/10000109i)
- [validate()](<../../appkit/nstoolbaritem/validate().md>) — 验证工具栏项的菜单及其执行操作的能力。
