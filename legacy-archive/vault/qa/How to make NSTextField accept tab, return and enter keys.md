---
title: How to make NSTextField accept tab, return and enter keys.
apple_id: DTS10004113
resource_type: QA
platform: macOS
topic: Data Management
technology: AppKit
published: '2014-05-12'
source_url: https://developer.apple.com/library/archive/qa/qa1454/_index.html
archived_at: '2026-07-18T02:30:49.268501Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1454

# How to make NSTextField accept tab, return and enter keys.

## Q:  How do I make NSTextField accept the tab key, as well as return and enter keys as line-breaks?

A: It's worth noting that `NSTextField` supports new line breaks by using Option-Return or Option-Enter. But under most circumstances the easiest solution would be to use `NSTextView` instead.

So you need to ask yourself "why" you want to keep using NSTextField. Here is a list of possible reasons:

- It may not be obvious to users that Option-Return and Option-Enter are available to them.
- You want to keep using the conveniences and features of NSTextField's super class `NSControl`.
- NSTextField is light-weight compared to NSTextView.
- NSTextField supports horizontal scrolling, by default NSTextView does not and requires extra work to avoid text wrapping.
- You want the flexibility of using the target/action scheme, often configured in InterfaceBuilder.
- You may simply want to just allow the tab key and are not concerned with line-breaks.

Should you decide to keep using `NSTextField`, allowing the tab key and/or allowing enter and return keys for line-breaks can be achieved by implementing the following delegate method:

`- (BOOL)control:(NSControl*)control textView:(NSTextView*)textView doCommandBySelector:(SEL)commandSelector;`

The method name `doCommandBySelector` means "attempt to perform the indicated method". It originates or is driven from the `NSResponder` class.

This delegate method is a part of `NSControl`, so it is found in `NSControl.h`, not in `NSTextField.h`.

__Listing 1__  Example delegate method for NSTextField.

```objc
- (BOOL)control:(NSControl*)control textView:(NSTextView*)textView doCommandBySelector:(SEL)commandSelector
{
    BOOL result = NO;

    if (commandSelector == @selector(insertNewline:))
    {
        // new line action:
        // always insert a line-break character and don’t cause the receiver to end editing
        [textView insertNewlineIgnoringFieldEditor:self];
        result = YES;
    }
    else if (commandSelector == @selector(insertTab:))
    {
        // tab action:
        // always insert a tab character and don’t cause the receiver to end editing
        [textView insertTabIgnoringFieldEditor:self];
        result = YES;
    }

    return result;
}
```

For more information on NSTextField and NSTextView refer to [Cocoa Text Architecture Guide](https://developer.apple.com/library/mac/documentation/TextFonts/Conceptual/CocoaTextArchitecture/Introduction/Introduction.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-05-12 | Updated link to Cocoa Text Architecture Guide. |
| 2006-10-09 | New document that describes how to make the NSTextField control accept tab, return and enter keys by using the control's dispatch delegate method. |

