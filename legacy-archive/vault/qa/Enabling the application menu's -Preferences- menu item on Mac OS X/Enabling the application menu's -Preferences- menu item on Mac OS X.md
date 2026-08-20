---
title: Enabling the application menu's "Preferences" menu item on Mac OS X
apple_id: DTS10004459
resource_type: QA
platform: macOS
topic: User Experience
technology: AppKit
published: '2008-01-21'
source_url: https://developer.apple.com/library/archive/qa/qa1552/_index.html
archived_at: '2026-07-18T02:32:16.080937Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1552

# Enabling the application menu's "Preferences" menu item on Mac OS X

## Q:  How do I enable the application menu's "Preferences" menu item on Mac OS X?

A: How do I enable the application menu's "Preferences" menu item on Mac OS X?

For the "Preferences" menu item to be enabled in a Cocoa application you must setup the target-action mechanism or the communication between the `NSMenuItem` and your controller object.

To enable this menu item two conditions must be met:

- Your controller object needs to declare and implement an `IBAction` or action method.
- The `NSMenuItem` must be "connected" to the action method of your controller object. You can do this in Interface Builder or programatically.

If you do not meet both conditions, then the Preferences menu item will remain disabled.

The action is the message your `NSMenuItem` sends to the target or, from the perspective of the target, the method it implements to respond to the action. You need to declare this method in your .h header file and implement it in your .m source file.

__Listing 1__  Example action method

```objc
-(IBAction)openPreferences:(id)sender { }
```


__Figure 1__  Connecting `NSMenuItem` to your `IBAction` method: control drag from the menu item to your object.

!

Although using Interface Builder is the straight forward way, you can do the same thing using code.

__Listing 2__  Setting the target and action with code.

```
NSMenu *menu = [[[[NSApplication sharedApplication] mainMenu] itemAtIndex:0] submenu];  NSString *prefsTitle = [NSString stringWithFormat:@"Preferences%C", (unichar)0x2026]; NSMenuItem *prefsMenuItem = [menu itemWithTitle:prefsTitle]; if (prefsMenuItem) {     [prefsMenuItem setTarget:self];     [prefsMenuItem setAction:@selector(openPreferences:)]; }
```


- For the same issue with Carbon applications please refer to: [Technical Q&A 1079](https://developer.apple.com/qa/qa2001/qa1079.html).
- [Cocoa Fundamentals Guide : Communicating With Objects](https://developer.apple.com/documentation/Cocoa/Conceptual/CocoaFundamentals/)
- [Introduction to Application Menus and Pop-up Lists](https://developer.apple.com/documentation/Cocoa/Conceptual/MenuList/index.html), specifically the "Enabling Menu Items" section.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-01-21 | New document that describes the two things you need to implement to enable the "Preferences" menu item on Mac OS X. |

