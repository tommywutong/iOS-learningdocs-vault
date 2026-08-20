---
title: Cocoa Performance Guidelines
apple_id: TP40001448
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2009-08-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaPerformance/Articles/Bindings.html
archived_at: '2026-07-15T07:13:16.162413Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Performance Guidelines](Introduction%20to%20Cocoa%20Performance%20Guidelines.md)


[Next](Improving%20NSBezierPath%20Rendering%20Times.md)[Previous](Cocoa%20Live%20Window%20Resizing.md)

# Cocoa Bindings Tips

If your application uses Cocoa bindings, you should be aware of the differences between different types of value bindings. If you are using bindings to load images or large amounts of text, using the `data` or `value` bindings can offer significant performance advantages over the `valuePath` or `valueURL` bindings.

When you use the `data` or `value` bindings to load data, the bindings system retrieves the needed data directly from the attached model object, which is usually in memory. Conversely, when you use the `valuePath` and `valueURL` bindings, the system may have to retrieve the data from a hard drive or other slow device where the information resides. Because the bindings system does not know anything about your data model, it cannot effectively cache your data internally; it must retrieve it each time.

During scrolling or window resizing, the system may need to load bound data many times to match the currently visible contents of the window. Retrieving data repeatedly from the hard drive during these operations can slow down your application considerably. Therefore, if your view may be bound to large amounts of data, such as large text blocks or many images, it is better to use the `data` or `value` bindings.

[Next](Improving%20NSBezierPath%20Rendering%20Times.md)[Previous](Cocoa%20Live%20Window%20Resizing.md)

