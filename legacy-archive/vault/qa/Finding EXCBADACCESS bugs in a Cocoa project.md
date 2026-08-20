---
title: Finding EXC_BAD_ACCESS bugs in a Cocoa project
apple_id: DTS10003384
resource_type: QA
platform: macOS
topic: Performance
technology: Foundation
published: '2006-10-10'
source_url: https://developer.apple.com/library/archive/qa/qa1367/_index.html
archived_at: '2026-07-18T02:30:26.479744Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1367

# Finding EXC_BAD_ACCESS bugs in a Cocoa project

## Q:  How do I find `EXC_BAD_ACCESS` bugs in a Cocoa project?

A: How do I find `EXC_BAD_ACCESS` bugs in a Cocoa project?

This kind of problem is usually the result of over-releasing an object. It can be very confusing, since the failure tends to occur well after the mistake is made. The crash can also occur while the program is deep in framework code, often with none of your own code visible in the stack.

To avoid problems like this, you must follow the Cocoa memory management rules. Refer to ADC's document "[Memory Management Programming Guide for Cocoa](https://developer.apple.com/documentation/Cocoa/Conceptual/MemoryMgmt/index.html)". The section “Object Ownership and Disposal” describes the primary policy.

- If you directly allocate, copy, or retain an object, you are responsible for releasing the newly created object with `release` or `autorelease`. Any other time you receive an object, you are not responsible for releasing it.
- A returned object is normally guaranteed to remain valid within the method it was received in (exceptions include multithreaded applications and some Distributed Objects situations). That method may also safely return the object to its invoker.
- If you need to store a returned object in an instance variable, you must retain or copy it.
- Use `retain` and `autorelease` when needed to prevent an object from being invalidated as a normal side-effect of a message.
- If you instantiate an object using a convenience method, the object is already slated for `autorelease`. Do not send a `release` or an `autorelease` message to this object.
- Never send a `dealloc` message to the object. This may dispose of the object but it does so regardless of the current reference count. Any other object that has retained the deallocated object is left with an invalid reference.
- Never make any assumptions on how or in what order autoreleased objects are disposed.

For information on a debugging tool called `NSZombieEnabled` to help isolate this kind problem, as well as other debugging tips, refer to:

[Technical Note 2124 Mac OS X Debugging Magic](https://developer.apple.com/technotes/tn2004/tn2124.html)

This topic is also mentioned in the ADC Reference Library documentation:

[Memory Management Rules](https://developer.apple.com/documentation/Cocoa/Conceptual/MemoryMgmt/index.html)

For an overview of Cocoa objects and their life cycles refer to the following guide:

[The Life Cycle of a Cocoa Object](https://developer.apple.com/documentation/Cocoa/Conceptual/CocoaFundamentals/CocoaObjects/chapter_3_section_5.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-10-10 | New document that discusses how to find memory protection violations or EXC_BAD_ACCESS bugs in Cocoa projects. |

