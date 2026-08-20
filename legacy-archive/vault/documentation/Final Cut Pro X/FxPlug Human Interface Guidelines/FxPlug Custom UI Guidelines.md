---
title: FxPlug Human Interface Guidelines
apple_id: TP40013782
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2013-12-18'
source_url: https://developer.apple.com/library/archive/documentation/FinalCutProX/Conceptual/FxPlugHIG/FxPlugCustomUIGuidelines/FxPlugCustomUIGuidelines.html
archived_at: '2026-07-15T07:32:30.169091Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [FxPlug Human Interface Guidelines](About%20the%20FxPlug%20Human%20Interface%20Guidelines.md)


[Next](Text%20Style%20Guidelines.md)[Previous](FxPlug%20UI%20Element%20Guidelines-%20Controls.md)

# FxPlug Custom UI Guidelines

You can embed custom UI elements in your FxPlug plug-in in the Inspector. In general, try to match the design of these elements to that of the built-in elements and controls of FxPlug plug-ins, such as the color scheme, size, and general layout.

Follow these guidelines when creating custom Inspector UI elements.

__If possible, use the multicolumn layout, with labels.__ A custom UI element that takes over the entire width of the Inspector could distract from the rest of the UI, as well as from other plug-ins. When possible, use a right-aligned text label to the left, with the custom UI controls aligned with the standard controls to the right.

__Place the custom Inspector UI within a parameter group if possible.__ If your custom UI element is the primary feature that the user needs to interact with your plug-in, then position that element at the top level. Otherwise, place it in a folder to better differentiate it from the standard controls.

__Avoid branding in the Inspector.__ Placing graphical logos and other nonfunctional custom UI inline with the Inspector takes up valuable UI space that you could use for other controls or plug-ins. If you must incorporate branding, use a custom UI panel instead.

You invoke a custom UI panel by clicking a button in the plug-in to call a floating window with a custom UI. Use a custom UI panel when your plug-in has unique requirements that cannot be accommodated within the space of the Inspector, onscreen control, or HUD of the FxPlug host application. Make your custom UI panel a completely unique environment, but follow the guidelines and principles described in _OS X Human Interface Guidelines_ for the best user experience.

[Next](Text%20Style%20Guidelines.md)[Previous](FxPlug%20UI%20Element%20Guidelines-%20Controls.md)

