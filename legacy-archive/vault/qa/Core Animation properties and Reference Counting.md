---
title: Core Animation properties and Reference Counting
apple_id: DTS40008096
resource_type: QA
platform: iOS|macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2013-05-16'
source_url: https://developer.apple.com/library/archive/qa/qa1565/_index.html
archived_at: '2026-07-18T02:32:18.486453Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1565

# Core Animation properties and Reference Counting

## Q:  After reading up on properties in Objective-C, I've noticed that a number of properties declared by Core Animation use the default "assign" semantic. However, when I set the property using a Core Foundation object the object is still retained. Why?

A: Core Animation doesn't specify strong reference semantics on its property attributes because those are only valid for Objective-C types. For example:

__Listing 1__  A build error occurs when attempting to leverage the 'strong' attribute for a Core Foundation type.

```objc
@property (strong) CGColorRef myProperty;

"Error: Property with 'retain (or strong)' attribute must be of object type"
```

Core Animation makes use of a number of data types provided by Core Graphics that are derived Core Foundation data types such as CGColorRef and CGPathRef. Since the error above would be flagged if these properties were declared with attributes reserved for Cocoa objects, the property declarations in context omit attributes.

To ensure expected behavior, Core Animation implements strong references or copy semantics where appropriate for all data types that it exposes, but it does that under the hood. So to avoid memory leaks when using these properties you must release owned Core Foundation objects after they are assigned. An example of assigning a CALayer's background color is below:

__Listing 2__  Properly assigning a background color.

```
CGColorRef color = CGColorCreateGenericRGB(1.0, 0.5, 0.25, 1.0);
layer.backgroundColor = color;
CFRelease(color);
```

For more information on properties see [Declared Property](https://developer.apple.com/library/mac/#documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html).

For a guide to using Core Animation, see the [Core Animation Programming Guide](https://developer.apple.com/documentation/Cocoa/Conceptual/CoreAnimation_guide/index.html).

For more information about Automatic Reference Counting, see the [Transitioning to ARC Release Notes](https://developer.apple.com/library/mac/#releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-05-16 | Minor content update. |
| 2008-11-24 | New document that describes a discrepancy between the property declarations in Core Animation and the actual behavior. |

