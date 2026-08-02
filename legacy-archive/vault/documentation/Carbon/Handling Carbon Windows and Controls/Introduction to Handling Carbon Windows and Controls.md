---
title: Handling Carbon Windows and Controls
apple_id: TP30001004
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/HandlingWindowsControls/hitb-wind_cont_intro/hitb-wind_cont_intro.html
archived_at: '2026-07-15T05:23:01.668828Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Window%20and%20Control%20Concepts.md)

# Introduction to Handling Carbon Windows and Controls

Windows and controls are two of the primary means by which users interact with Macintosh computers. Most of the information that the user sees is presented in a window, and the controls within a window let the user interact with the application.

The Window Manager and the Control Manager are the primary programming interfaces for creating and manipulating windows and controls in your application. This document describes the basic types of windows and controls, their suggested usage, and how they interact with the Carbon event model. This document also contains programming examples for creating windows and controls using Interface Builder (or by calling specific functions), sample implementations of controls, and information about how to create your own custom windows or controls.

The concepts and examples in this document assume you are building applications for Mac OS X. However, because the Window Manager and Control Manager are Carbon-compliant, many of the functions described also work with Mac OS 9. This document calls out instances where functionality is available only in Mac OS X.

This document does not describe how to best use or lay out particular windows and controls. For that information, you should refer to _Aqua Human Interface Guidelines_ available in Carbon User Experience documentation.

In fact, you should be familiar with _Aqua Human Interface Guidelines_ to get the most out of this document.

This document also makes references to other Carbon technologies which are needed to implement window or control functionality. For more comprehensive information about these technologies, you should visit the Carbon documentation page at the following site:

[http://developer.apple.com/documentation/Carbon/index.html](https://developer.apple.com/documentation/Carbon/index.html)

[Next](Window%20and%20Control%20Concepts.md)

