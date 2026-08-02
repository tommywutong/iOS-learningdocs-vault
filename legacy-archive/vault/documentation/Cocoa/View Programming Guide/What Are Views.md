---
title: View Programming Guide
apple_id: TP40002978
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaViewsGuide/WhatAreViews/WhatAreViews.html
archived_at: '2026-07-15T07:13:23.485899Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [View Programming Guide](Introduction%20to%20View%20Programming%20Guide%20for%20Cocoa.md)


[Next](View%20Geometry.md)[Previous](Introduction%20to%20View%20Programming%20Guide%20for%20Cocoa.md)

# What Are Views?

In Cocoa, a view is a rectangular section of the screen contained in a window. It is responsible for handling all drawing and user-initiated events within its frame. Cocoa provides the `NSView` class as an abstract view implementation that subclasses use as the basis for implementing custom display and user interaction.

Cocoa provides a high-level class, `NSView`, that implements the fundamental view behavior. An `NSView` instance defines the rectangular location of the view, referred to as its frame rectangle, and takes responsibility for rendering a visual representation of its data within that area. In addition to drawing, a view takes responsibility for handling user events directed towards the view.

`NSView` is an abstract class that provides the underlying mechanisms for concrete subclasses to implement their own behavior. It provides methods that can be overridden to support drawing and printing. `NSView` is a subclass of `NSResponder` and, as a result, also provides methods that can be overridden to respond to user-initiated mouse and keyboard events.

In addition to drawing content and responding to user events, `NSView` instances act as containers for other views. By nesting views within other views, an application creates a hierarchy of views. This view hierarchy provides a clearly defined structure for how views draw relative to each other and pass messages from one view to another, up to the enclosing window, and on to the application for processing.

In addition to the `NSView` class, Cocoa provides a number of view subclasses that provide the user interface elements common to many applications. Your application can use these views classes directly, subclass them to provide additional functionality, or create entirely new custom view classes. Other frameworks provide additional views that can be used in Cocoa applications, including Web Kit, QuickTime Kit, and Quartz Composer.

The Cocoa view subclasses can be classified into several groups: container views, views that are part of the text system, user controls, and views that support non-Quartz graphics environments.

Container views enhance the function of other views, or provide additional visual separation of the content. The `NSBox` class provides visual separation of groups of subviews that are related in their function. The `NSTabView` class provides a way to swap different views into and out of its content view, so that the tab view's content area can be reused by multiple sets of views. The `NSSplitView` class allows an application to stack multiple views horizontally or vertically, divided by a separator bar that the user can drag to resize the views.

The `NSScrollView` class displays a portion of the contents of a view that’s too large to be displayed in a window. It coordinates a number of other views and controls to provide its functionality. A scroll view's scrollers, instances of the `NSScroller` class, allow the user to scroll the document. The scroll view's content view, an instance of the `NSClipView` class, actually manages positioning and redrawing the content view as the scroll view content scrolls. The `NSRulerView` class provides horizontal and vertical rulers that follow the scrolling of the document view. All these views work together to provide scrolling to an application.

The `NSTextView` class is the front-end to the Cocoa text system. It draws the text managed by several underlying model and controller classes and handles user events to select and modify its text. The text classes exceed most other classes in the Application Kit in the richness and complexity of their interface. `NSTextView` is a subclass of `NSText`, which is in turn a subclass of `NSView`. Applications use the `NSTextView` class rather than `NSText`. See _[Cocoa Text Architecture Guide](../../Cocoa%20Text%20Architecture%20Guide/About%20the%20Cocoa%20Text%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinjz)_ for more information on the Cocoa text system.

When used in a view hierarchy, an `NSTextView` instance is usually set as the document view of a scroll view. For simple text-field style interface items, Cocoa defines a number of simpler text controls, including the `NSTextField` class.

Typically, the majority of an application's user interface is created using controls. As a descendent of `NSView`, controls are responsible for drawing their content and handling user-initiated events. Controls typically display a specific value and allow the user to change that value. Individual controls provide value editing out of context; it's the overall user interface that puts that data into context.

Controls act as containers for lightweight objects called cells. Cells are actually responsible for the majority of the visual representation and event handling that controls provide. This delegation allows cells to be reused in more complex user interface objects. For example, an instance of the `NSTextFieldCell` class is used by an `NSTextField` instance to display text and respond to user edits. That same `NSTextFieldCell` class is also used by an `NSTableView` instance to allow editing of data within a column. This delegation of responsibility is one of the key distinctions between controls and views.

Controls also support the target-action paradigm. Controls send target objects an action message in response to user actions. For example, clicking a button results in the action message being sent to the button's target object, if set, or up the responder chain if a specific target object is not specified.

Some control subclasses actually have “view” in their name, which can be confusing. The `NSImageView`, `NSTableView`, and `NSOutlineView` classes are all subclasses of `NSControl`, although they inherit indirectly from `NSView`. It's because these objects rely on cells to provide much of their functionality that they are subclasses of `NSControl` rather than `NSView`. Note that the `NSTableView` and `NSOutlineView` classes do not provide their scrolling directly; they are set as the document view of a scroll view.

The `NSView` class supports the standard drawing environment in OS X, the Quartz graphic environment. However, Cocoa also supports several non-Quartz drawing environments for additional functionality and compatibility. The `NSOpenGLView` class allows an application to render content using OpenGL. An application subclasses `NSOpenGLView` and overrides the `drawRect:` method to display the OpenGL content. Unlike its superclass, the `NSOpenGLView` class does not support subviews. `QTMovieView` is a subclass of `NSView` that can be used to display, edit, and control QuickTime movies. The `QTMovieView` class is part of the QuickTime Kit framework rather than the Cocoa framework.

[Next](View%20Geometry.md)[Previous](Introduction%20to%20View%20Programming%20Guide%20for%20Cocoa.md)

