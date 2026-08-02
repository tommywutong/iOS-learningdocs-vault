---
title: Adding and removing a submenu from a menu in Cocoa
apple_id: DTS10004127
resource_type: QA
platform: macOS
topic: User Experience
technology: AppKit
published: '2007-09-10'
source_url: https://developer.apple.com/library/archive/qa/qa1420/_index.html
archived_at: '2026-07-18T02:30:35.616726Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1420

# Adding and removing a submenu from a menu in Cocoa

## Q:  How do I add or remove a submenu from a menu in Cocoa?

A: How do I add or remove a submenu from a menu in Cocoa?

Use `NSMenu` methods like `insertItem:atIndex:` or `removeItemAtIndex:` to add or remove the `NSMenuItem` to which the "submenu" in question is attached.

A "submenu" in Cocoa is just an instance of `NSMenu`, it just happens to be attached to an item in a higher level menu. In other words, menus are hierarchical, and a submenu is any menu other than the "top level" menu. When you want to add or remove a submenu, simply use the `NSMenu` methods to add or remove the `NSMenuItem` itself. It does not matter whether that item has a submenu attached (`hasSubmenu`). See the [NSMenu](https://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/Classes/NSMenu_Class/Reference/Reference.html) and [NSMenuItem](https://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/Classes/NSMenuItem_Class/Reference/Reference.html) Class References for these and additional methods.

Note that the application's menu bar itself is an instance of `NSMenu` in Cocoa. It is an example of a top level menu, and its standard "File", "Edit", and "Window" entries are menu items with a submenu attached.

To give an example of adding and removing a submenu, let's assume you want to make an additional submenu of adminstrative tools available based on some condition. Figure 1 shows the addition of an `NSMenuItem` "Admin Tools" with an `NSMenu` attached to it, itself containing three NSMenuItems.

__Figure 1__  A submenu of administrative items.

!

One option is to programatically allocate the "Admin Tools" `NSMenuItem`, the `NSMenu` "submenu" and then attach it using `setSubmenu:`. However, this example shows the more typically case: just create the whole submenu in Interface Builder and connect an outlet (here, `adminMenuItem`) to refer to it. The whole item could then be added or removed based on some condition, such as successful authentication.

__Figure 2__  Connecting the menu outlet in Interface Builder.

!!

The following code shows how to set the initial state by removing the item when the nib file is loaded and provides methods to add or remove it as needed. This example controller preserves the index where the menu is found in `adminMenuItemIndex` so it may later be restored in the same location.

__Listing 1__  Removing the menu initially when the nib file loads.

```objc
- (void) awakeFromNib {     adminMenuItemIndex = [[NSApp mainMenu] indexOfItem: adminMenuItem];     [self removeAdminMenuItem]; }
```


__Listing 2__  Removing the submenu by using its outlet.

```objc
- (void) removeAdminMenuItem {     [adminMenuItem retain]; // ensure item and its submenu aren't dealloc'd when removed from mainMenu     [[NSApp mainMenu] removeItem: adminMenuItem];  }
```


__Listing 3__  Adding a submenu to the application's menu bar.

```objc
- (void) addAdminMenuItem {     [[NSApp mainMenu]insertItem: adminMenuItem atIndex:adminMenuItemIndex];      [adminMenuItem release]; // maintain accurate retainCount since mainMenu will retain on insert }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-09-10 | Editorial corrections. |
| 2007-08-30 | New document that explains how to dynamically add and remove menus in a Cocoa application. |

