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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# validateMenuItem:

<sub>Instance Method</sub>

Implemented to override the default action of enabling or disabling a specific menu item.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) validateMenuItem:(NSMenuItem *) menuItem;
```

## Parameters

- `menuItem` — An NSMenuItem object that represents the menu item.

## Return Value

[YES](../yes.md) to enable `menuItem`, [NO](../no.md) to disable it.

## Discussion

The object implementing this method must be the target of `menuItem`. You can determine which menu item `menuItem` is by querying it for its tag or action.

The following example disables the menu item associated with the `nextRecord` action method when the selected line in a table view is the last one; conversely, it disables the menu item with `priorRecord` as its action method when the selected row is the first one in the table view. (The `countryKeys` array contains names that appear in the table view.)

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
