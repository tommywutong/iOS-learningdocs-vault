---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Concepts/UsingWindowController.html
archived_at: '2026-07-15T07:21:11.360475Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Opening%20and%20Closing%20Windows.md)[Previous](How%20Panels%20Work.md)

# How Window Controllers Work

A [controller object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) (in this case, an instance of the [NSWindowController](https://developer.apple.com/documentation/appkit/nswindowcontroller) class) manages a window; this object is usually stored in a nib file. This management entails the following:

- Loading and displaying the window
- Closing the window when appropriate
- Customizing the window’s title
- Storing the window’s frame (size and location) in the defaults database
- Cascading the window in relation to other document windows of the application

A window controller can manage a window by itself or as a participant in AppKit’s document-based architecture, which also includes the [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) and [NSDocumentController](https://developer.apple.com/documentation/appkit/nsdocumentcontroller) classes. In this architecture, a window controller is created and managed by a document (an instance of an `NSDocument` subclass) and, in turn, keeps a reference to the document. For a discussion of this architecture, see _[Document-Based App Programming Guide for Mac](../../Data%20Management/Document-Based%20App%20Programming%20Guide%20for%20Mac/About%20the%20Cocoa%20Document%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzz)_.

The relationship between a window controller and a nib file is important. Although a window controller can manage a programmatically created window, it usually manages a window in a nib file. The nib file can contain other top-level objects, including other windows, but the window controller’s responsibility is this primary window. The window controller is usually the owner of the nib file, even when it is part of a document-based application.

For simple documents—that is, documents with only one nib file containing a window—you need do little directly with [NSWindowController](https://developer.apple.com/documentation/appkit/nswindowcontroller) objects. AppKit creates one for you. However, if the default window controller is not sufficient, you can create a custom subclass of `NSWindowController`.

For documents with multiple windows or panels, your document must create separate instances of `NSWindowController` (or of custom subclasses of `NSWindowController`), one for each window or panel. An example is a CAD application that has different windows for side, top, and front views of drawn objects. What you do in your `NSDocument` subclass determines whether the default `NSWindowController` object or separately created and configured `NSWindowController` objects are used.

When a window is closed and it is part of a document-based application, the document removes the window’s window controller from its list of window controllers. This results in the system [deallocating](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27) the window controller and the window, and possibly the `NSDocument` object itself. When a window controller is not part of a document-based application, closing the window does not by default result in the deallocation of the window or window controller. This is the desired behavior for a window controller that manages something like an inspector; you shouldn’t have to load the nib file again and re-create the objects the next time the user requests the inspector.

If you want the closing of a window to make both window and window controller go away when it isn’t part of a document, your subclass of `NSWindowController` can observe the [NSWindowWillCloseNotification](https://developer.apple.com/documentation/appkit/nswindowwillclosenotification) notification or, as the window delegate, implement the [windowWillClose:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419605-windowwillclose) method.

[Next](Opening%20and%20Closing%20Windows.md)[Previous](How%20Panels%20Work.md)

