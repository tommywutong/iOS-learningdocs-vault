---
title: How to create a Cocoa Disclosure Button Control
apple_id: DTS10004018
resource_type: QA
platform: macOS
topic: User Experience
technology: AppKit
published: '2006-08-01'
source_url: https://developer.apple.com/library/archive/qa/qa1485/_index.html
archived_at: '2026-07-18T02:31:24.925821Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1485

# How to create a Cocoa Disclosure Button Control

## Q:  How do I create a "disclosure button control" in Cocoa like the one found on the save dialog?

A: Even though disclosure button controls are not immediately available on an Interface Builder palette, they can still be created easily by changing the attributes of an ordinary NSButton of type "Disclosure". Instantiate a disclosure NSButton in your window's nib, create an outlet like 'disclosureButton' in an appropriate controller class. Connect the outlet to the NSButton.

In a nib-loading method such as `-awakeFromNib` or `-windowControllerDidLoadNib` in an `NSDocumentController`, send messages to set the bezel style of the control to `NSDisclosureBezelStyle` and the button type to `NSPushOnPushOffButton`.

__Listing 1__  Programatically Set the Bezel Style and Button Type

```
 [disclosureButton setBezelStyle: NSRoundedDisclosureBezelStyle];
    [disclosureButton setButtonType: NSPushOnPushOffButton];
```

For more information on disclosure controls, refer to "Controls > View Controls" section of the Apple Human Interface Guidelines, available at ADC Reference Library > User Experience > Fundamentals"

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-08-01 | New document that explains how to create a disclosure button control in Cocoa, not immediately available in Interface Builder. |

