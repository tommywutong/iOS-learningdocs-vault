---
title: MethodReplacement
apple_id: DTS10004023
resource_type: Sample Code
platform: macOS
topic: Languages & Utilities
technology: null
published: '2006-08-01'
source_url: https://developer.apple.com/library/archive/samplecode/MethodReplacement/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:14:59.257202Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MethodReplacement](MethodReplacement.md)


[Next](main.m.md)[Previous](MethodReplacement.md)

# ReadMe.txt

```
Sample Code for WWDC 2006 session 302.

Objective C 2.0 Compatible class_poseAs() replacement. This demonstrates how to replace a method in an existing Objective C class, and how to call the old version without having to store IMP function pointers in a global. The trick is to define a category on the class whose method you want to replace. In the category, declare and implement a method with the same signature as the replaced method. In the +load method of the category, look up the original and replacement methods using class_getInstanceMethod(), then call method_exchangeImplementations(). Subsequent calls to the original method will call the replacement method, and an apparently recursive call to the replacement method will call the original method. Voila.

In this specific example, the method -[NSWindow sendEvent:] is being replaced by the category method -[NSWindow (TestMethodReplacement) TestMethodReplacement_sendEvent:]. Because the method implementations are swapped, the call to [self TestMethodReplacement_sendEvent:] actually calls the original -[NSWindow sendEvent:] implementation.
```

[Next](main.m.md)[Previous](MethodReplacement.md)

