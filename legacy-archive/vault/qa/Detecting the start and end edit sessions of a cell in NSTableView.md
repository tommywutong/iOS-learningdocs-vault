---
title: Detecting the start and end edit sessions of a cell in NSTableView.
apple_id: DTS40009338
resource_type: QA
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-10-27'
source_url: https://developer.apple.com/library/archive/qa/qa1551/_index.html
archived_at: '2026-07-18T02:32:16.048022Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1551

# Detecting the start and end edit sessions of a cell in NSTableView.

## Q:  How do I detect start and end edit sessions of a cell in `NSTableView`?

A: How do I detect start and end edit sessions of a cell in `NSTableView`?

In order to detect when a user is about to start and end an edit session of a cell in `NSTableView`, you need to be set as the delegate of that table and implement the following `NSControl` delegate methods:

__Listing 1__  `NSControl` delegate methods

```objc
- (BOOL)control:(NSControl *)control textShouldBeginEditing:(NSText *)fieldEditor; - (BOOL)control:(NSControl *)control textShouldEndEditing:(NSText *)fieldEditor;
```

The table forwards the delegate message it is getting from the text view on to your delegate object using the `control:textShouldEndEditing:` method. This way your delegate can be informed of which control the text view field editor is acting on its behalf.

To further detect when editing has completed, you need to register for `NSControlTextDidEndEditingNotification`, and implement a method to catch that notification:

__Listing 2__  `NSControlTextDidEndEditingNotification`

```
[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(editingDidEnd:)         name:NSControlTextDidEndEditingNotification object:nil];  - (void)editingDidEnd:(NSNotification *)notification {     // perform your work here }
```

Try not to equate this with the `NSTableView` text delegate methods:

__Listing 3__  `NSTableView`: Text delegate methods

```objc
- (BOOL)textShouldBeginEditing:(NSText *)textObject; - (BOOL)textShouldEndEditing:(NSText *)textObject;
```

In order to implement these, you need to be a subclass of `NSTableView`. When the user edits a table cell the table puts an `NSTextView` in place of the cell in order to actually perform the editing. This is called the window's "[field editor](https://developer.apple.com/documentation/Cocoa/Conceptual/TextArchitecture/Concepts/TextFieldsAndViews.html)".

The `NSTableView` configures itself as the delegate for the `NSTextView` so that the table gets notified when editing begins and ends. Hence, if you are a subclass of `NSTableView` you can then implement any or all of the text delegate methods described in the `NSTextView` documentation.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-10-27 | New document that describes the proper way to control and detect edit sessions of NSTableView using NSControl's delegate methods and notifications. |

