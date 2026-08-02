---
title: Button Programming Topics
apple_id: 10000019i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Button/Tasks/SubclassingNSButton.html
archived_at: '2026-07-15T07:11:47.171785Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Button Programming Topics](Introduction%20to%20Buttons.md)


[Next](Document%20Revision%20History.md)[Previous](Setting%20a%20Button%E2%80%99s%20Key%20Equivalent.md)

# Subclassing NSButton

Override the designated initializer (NSView’s `initWithFrame:` method) if you create a subclass of NSButton that performs its own initialization. If you want to use a custom NSButtonCell subclass with your subclass of NSButton, you have to override the `cellClass:` method, as described in [Subclassing NSControl](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ControlCell/Tasks/SubclassingNSControl.html#//apple_ref/doc/uid/20000730).

[Next](Document%20Revision%20History.md)[Previous](Setting%20a%20Button%E2%80%99s%20Key%20Equivalent.md)

