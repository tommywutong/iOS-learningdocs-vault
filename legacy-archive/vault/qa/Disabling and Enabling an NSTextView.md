---
title: Disabling and Enabling an NSTextView
apple_id: DTS10004071
resource_type: QA
platform: macOS
topic: Data Management
technology: AppKit
published: '2006-09-11'
source_url: https://developer.apple.com/library/archive/qa/qa1461/_index.html
archived_at: '2026-07-18T02:30:52.620604Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1461

# Disabling and Enabling an NSTextView

## Q:  How do I disable and enable an NSTextView?

A: How do I disable and enable an NSTextView?

Currently there is no direct way to disable and re-enable an NSTextView. However, with a few lines of code you can implement this feature on your own. The sample code below best illustrates this by changing the selectable and editable attributes as well as its text color.

__Listing 1__  Disabling and Enabling NSTextView

```objc
-(void)enableTextView:(BOOL)enableIt {         [textView setSelectable: enableIt];         [textView setEditable: enableIt];         if (enableIt)                 [textView setTextColor: [NSColor controlTextColor]];         else                 [textView setTextColor: [NSColor disabledControlTextColor]]; }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-09-11 | New document that shows how a Cocoa application can disable and enable an NSTextView. |

