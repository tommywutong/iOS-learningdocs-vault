---
title: Detecting the Caps Lock Key
apple_id: DTS10004250
resource_type: QA
platform: macOS
topic: Data Management
technology: AppKit
published: '2013-01-28'
source_url: https://developer.apple.com/library/archive/qa/qa1519/_index.html
archived_at: '2026-07-18T02:32:05.117271Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1519

# Detecting the Caps Lock Key

## Q:  How do I detect when the caps lock key is turned on or off in my Cocoa application?

A: You must implement `flagsChanged:` in order to detect this key.

`NSResponder` `keyDown:` and `keyUp:` methods do not fire when just a modifier key is pressed. So if you want to catch this event, you will need to override:

`- (void)flagsChanged:(NSEvent*)` and examine the `NSEvent` from there.

The `flagsChanged:` method comes from `NSResponder`, so any responder in the responder chain can react to it.

__Listing 1__  Detecting the caps lock key.

```objc
- (void)flagsChanged:(NSEvent*)event
{
    if ([event keyCode] == 0x39) // 57 = key code for caps lock
    {
        NSUInteger flags = [event modifierFlags];
        if (flags & NSAlphaShiftKeyMask)
            NSLog(@"capsLock on");
        else
            NSLog(@"capsLock off");
    }
}
```


- [Cocoa Event Handling Guide - Handling Key Events](https://developer.apple.com/library/etc/redirect/DTS/HandlingKeyEvents)
- [NSEvent Class Reference - Event Modifier Flags](https://developer.apple.com/library/etc/redreict/DTS/NSEvent)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-01-28 | Repaired outdated links to documentation. |
| 2007-05-11 | New document that explains how to detect when the caps lock key is turned on and off. |

