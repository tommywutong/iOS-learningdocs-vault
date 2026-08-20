---
title: Token Field Programming Guide
apple_id: TP40006555
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TokenField_Guide/ImplTokenFieldMenus/ImplTokenFieldMenus.html
archived_at: '2026-07-15T07:20:41.269549Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Token Field Programming Guide](Introduction%20to%20Token%20Field%20Programming%20Guide%20for%20Cocoa.md)


[Next](Document%20Revision%20History.md)[Previous](Getting%20and%20Setting%20Token-Field%20Values.md)

# Implementing Menus for Tokens

If you want tokens in a token field to have menus, you must implement the [tokenField:hasMenuForRepresentedObject:](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1533494-tokenfield) and [tokenField:menuForRepresentedObject:](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1528750-tokenfield) delegation methods. A token field invokes the former method just before it displays a token to find out if it should draw a discovery triangle. It invokes the latter method when the user clicks the triangle.

Listing 1 gives a sample implementation of these methods. Note that it sets the token’s represented object as the represented object of the menu item that invokes an action method. The target of the action method fetches the represented object from the menu item to act upon it.

__Listing 1__  Implementing the menu delegation methods

```objc
- (BOOL)tokenField:(NSTokenField *)tokenField hasMenuForRepresentedObject:(id)representedObject {
    return YES;
}

- (NSMenu *)tokenField:(NSTokenField *)tokenField menuForRepresentedObject:(id)representedObject {

    NSMenu *tokenMenu = [[[NSMenu alloc] init] autorelease];

    if (![representedObject exists])
        return nil;

    NSMenuItem *artistItem = [[[NSMenuItem alloc] init] autorelease];
    [artistItem setTitle:[representedObject artist]];
    [tokenMenu addItem:artistItem];

    NSMenuItem *albumItem = [[[NSMenuItem alloc] init] autorelease];
    [albumItem setTitle:[NSString stringWithFormat:@"Album: %@", [representedObject album]]];
    [tokenMenu addItem:albumItem];

    NSMenuItem *durationItem = [[[NSMenuItem alloc] init] autorelease];
    [durationItem setTitle:[NSString stringWithFormat:@"Time: %@", [representedObject time]]];
    [tokenMenu addItem:durationItem];

    NSMenuItem *mItem = [[[NSMenuItem alloc] initWithTitle:@"Show Album Art" action:@selector(showAlbumArt:) keyEquivalent:@""] autorelease];
    [mItem setTarget:self];
    [mItem setRepresentedObject:representedObject];
    [tokenMenu addItem:mItem];

    return tokenMenu;
}
```

[Next](Document%20Revision%20History.md)[Previous](Getting%20and%20Setting%20Token-Field%20Values.md)

