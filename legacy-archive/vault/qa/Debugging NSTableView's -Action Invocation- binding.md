---
title: Debugging NSTableView's "Action Invocation" binding
apple_id: DTS10004129
resource_type: QA
platform: macOS
topic: User Experience
technology: AppKit
published: '2006-11-13'
source_url: https://developer.apple.com/library/archive/qa/qa1472/_index.html
archived_at: '2026-07-18T02:30:57.211036Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1472

# Debugging NSTableView's "Action Invocation" binding

## Q:  Why is my `NSTableView`'s "Action Invocation" binding not working?

A: Why is my `NSTableView`'s "Action Invocation" binding not working?

There could be several reasons why your action method is not being called:

- You may have not included a ":" with the selector name for the appropriate bindings.
- Some or all of the columns in the `NSTableView` are editable. This prevents the double-click action.
- Your `NSArrayController` might not be properly bound to the content of `NSTableView`.

The "Action Invocation" of `NSTableView` involves two different bindings: `doubleClickArgument` and `doubleClickTarget`.

The binding `doubleClickArgument` is a multiple-value binding that specifies the object passed as a parameter to the selector when `NSTableView` receives a double click. The binding `doubleClickTarget` is an object that receives a message corresponding to the selector name.

If your action method is defined in the Application's delegate, for example, use the following bindings for `NSTableView` using InterfaceBuilder:

Double Click Target

- bind to = Application delegate object
- model key path = `self`
- selector name = `clickAction:`

Double Click Argument

- bind to = array controller
- controller key = `selectedObjects`
- selector name = `clickAction:`

Content

- bind to = array controller
- controller key = `arrangedObjects`

Selection Indexes

- bind to = array controller
- controller key = `selectedIndexes`

Write your action method with its argument as an `NSArray` of "`selectedObjects`".

__Listing 1__  Example action method.

```objc
- (void)clickAction:(NSArray*)selectedObjects {     NSLog(@"double-click"); }
```


For detailed information on `NSTableView` bindings refer to:

[Cocoa Bindings Reference - NSTableView Bindings](https://developer.apple.com/documentation/Cocoa/Reference/CocoaBindingsRef/BindingsText/NSTableView.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-11-13 | New document that discusses the issues and factors that affect NSTableView's "Action Invocation" binding. |

