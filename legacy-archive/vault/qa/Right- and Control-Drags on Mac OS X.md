---
title: Right- and Control-Drags on Mac OS X
apple_id: DTS10003369
resource_type: QA
platform: Java
topic: Cross Platform
technology: null
published: '2005-06-29'
source_url: https://developer.apple.com/library/archive/qa/qa1362/_index.html
archived_at: '2026-07-18T02:30:26.249692Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1362

# Right- and Control-Drags on Mac OS X

## Q:  My Mac OS X Java application is not receiving drag actions when I start a drag using the Control key on a standard Apple mouse, or a right mouse button. Is this a bug?

A: This may seem like a problem with the Java implementation on Mac OS X, but it is in fact a platform difference that you need to be aware of as a developer. On Mac OS X, Control-clicking (or right-clicking, depending on your mouse) is the trigger for contextual menus. This is not unusual, but the platform difference is that the trigger occurs when the mouse is pressed, as opposed to released (the latter being the behavior on Windows). As soon as you press the left mouse button with the Control key held down, or press the right mouse button, the system recognizes it as a contextual menu trigger, never the beginning of a drag operation. This makes a Ctrl-drag (or right drag) impossible on Mac OS X. Note that this is for all environments: the Java AWT, built on top of Cocoa, simply inherits the behavior.

If your application supports multiple drag operations, we suggest first exhausting the other event masks (Alt/Option, Shift, Meta/Command) as well as combinations of those masks on Mac OS X. You can either do this conditionally for the Mac OS X platform (see [Technical Note 2110](https://developer.apple.com/technotes/tn2002/tn2110.html)), or make a conscious design decision for all platforms.

The `popupTrigger` issue described here, along with other differences that you may want to be aware of as a Mac OS X Java developer, is documented in the "Native Platform Integration: Making User Interface Decisions" section of [Java 1.4 Development for Mac OS X](https://developer.apple.com/documentation/Java/Conceptual/Java141Development/). For more on how users can change the context of a drag on Mac OS X, please see the [Drag and Drop](http://developer/documentation/UserExperience/Conceptual/OSXHIGuidelines/XHIGDragDrop/chapter_12_section_1.html#//apple_ref/doc/uid/TP30000364) section of the Apple Human Interface Guidelines.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-06-29 | Minor editorial changes |
| 2004-08-31 | New document that describes a difference in Drag and Drop on Mac OS X that affects all cross-platform Java applications |

