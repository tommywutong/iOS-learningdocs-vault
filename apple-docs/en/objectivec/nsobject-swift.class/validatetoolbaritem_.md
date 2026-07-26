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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# validateToolbarItem:

<sub>Instance Method</sub>

If this method is implemented and returns `false`, NSToolbar will disable `theItem`; returning `true` causes `theItem` to be enabled.

<sub>macOS</sub>

```objc
- (BOOL) validateToolbarItem:(NSToolbarItem *) item;
```

## Discussion

NSToolbar only calls this method for image items.

> [!note] Note
> [validateToolbarItem:](validatetoolbaritem_.md) is called very frequently, so it must be efficient.

If the receiver is the `target` for the actions of multiple toolbar items, it’s necessary to determine which toolbar item `theItem` refers to by testing the `itemIdentifier`.

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

## See Also

### Related Documentation

- [validateVisibleItems()](<../../appkit/nstoolbar/validatevisibleitems().md>) — Validates the toolbar’s visible items during a window update.
- [action](../../appkit/nstoolbaritem/action.md) — The action method to call when someone clicks on the toolbar item.
- [target](../../appkit/nstoolbaritem/target.md) — The object that defines the action method the toolbar item calls when clicked.
- [Toolbar Programming Topics for Cocoa](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Toolbars/Toolbars.html#//apple_ref/doc/uid/10000109i)
- [validate()](<../../appkit/nstoolbaritem/validate().md>) — Validates the toolbar item’s menu and its ability to perfrom its action.
