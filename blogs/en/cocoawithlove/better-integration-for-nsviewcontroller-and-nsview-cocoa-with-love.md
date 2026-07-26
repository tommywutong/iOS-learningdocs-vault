---
title: 'Better integration for NSViewController and NSView | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/07/better-integration-for-nsviewcontroller.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:7237662a59980b1a'
translated: false
---

> 原文：[Better integration for NSViewController and NSView | Cocoa with Love](https://www.cocoawithlove.com/2008/07/better-integration-for-nsviewcontroller.html)　·　Cocoa with Love (Matt Gallagher)

NSViewController simplifies loading an NSView from a NIB file. But it has some limitations compared to NSWindowController (its window loading/managing equivalent). In this post, I'll explain the limitations and present options for overcoming them.

## Window and View Controllers

In a clean Model-View-Controller application design (I know, it's never clean but let's pretend), the views in your windows know how to do their own work but are ignorant of any greater application context. The context for views comes from higher level objects (controllers) that configure the view state and provide data connections and notifications.

NSWindowController has provided this "higher level context" for windows and their contents since the beginning of Mac OS X. Its primary function is to act as a window-from-NIB loader. Through this role, NSWindowController and the NIB loader provide most of the context to view objects simply through IBOutlet connections and bindings. In addition, NSWindowController is normally the window's delegate and resides in the responder chain immediately after the window — this allows it to perform further arranging actions and higher-level responses to user actions within the window.

From Mac OS X 10.5, NSViewController began offering similar from-NIB loading convenience for NSViews. This allows higher level context and dynamic configuration of regions of a window, rather than purely at the coarse level of the whole window.

## View-Controller integration

NSWindow was written to integrate well with NSWindowController. You can access the NSWindowController from the NSWindow via the windowController method. The NSWindow ensures that the NSWindowController is included in the responder chain shortly after the NSWindow itself. When also the delegate of the NSWindow, NSWindowController is sent messages when certain actions occur, including windowWillClose: and windowDidBecomeMain:, in addition to NSWindowController methods windowDidLoad and windowWillLoad.

Sadly, none of these features exist to integrate an NSView with its NSViewController. This likely derives from the fact that an NSView cannot directly access its NSViewController.

## Adding integration

Adding the same level of integration to NSView and NSViewController requires that the NSView can access its NSViewController.

Where possible, this is best done by using an NSView subclass for the view loaded by the NSViewController. This subclass should have the following member:

```objc
    IBOutlet NSViewController *viewController;
```

which should be connected to the NSViewController in Interface Builder (the File's Owner object).

Once this is done, we can use this value to achieve responder chain integration with methods in the NSView subclass as follows:

```objc
- (void)setViewController:(NSViewController *)newController
{
    if (viewController)
    {
        NSResponder *controllerNextResponder = [viewController nextResponder];
        [super setNextResponder:controllerNextResponder];
        [viewController setNextResponder:nil];
    }

    viewController = newController;
    
    if (newController)
    {
        NSResponder *ownNextResponder = [self nextResponder];
        [super setNextResponder: viewController];
        [viewController setNextResponder:ownNextResponder];
    }
}

- (void)setNextResponder:(NSResponder *)newNextResponder
{
    if (viewController)
    {
        [viewController setNextResponder:newNextResponder];
        return;
    }
    
    [super setNextResponder:newNextResponder];
}
```

The NIB loader will kindly invoke the setViewController: method for us when it establishes the connection from the NIB. Together with the setNextResponder: method, these ensure that any time the viewController is set on the NSView, it is inserted in the responder chain immediately after the NSView.

It can also be useful to override viewDidMoveToSuperview in the NSView subclass and use the override to send a notification to an NSViewController subclass method. This allows delegate-like behavior for the NSViewController similar to that available for windows.

## Other considerations

These changes use a subclass of NSView. For NSWindow, integration with the NSWindowController came for free, without needing a subclass.

With a subclass comes the disadvantage of temptation. Once the NSView is subclassed to integrate with NSViewController, the temptation exists to insert code that is properly controller code into the NSView instead of into the NSViewController where it belongs.

There is also the disadvantage that existing NSView subclasses would all need to be separately subclassed to add this functionality.

These disadvantages could be overcome by inserting the NSView subclass functionality directly into NSView itself. Instead of a per-view instance variable pointing to the view's controller, a global NSMapTable relating any NSViewController to its respective NSView could be used. Similarly, all required methods could be swizzled or patched into NSView and NSViewController directly. I don't do this in my own code because its messier and harder to maintain — but you could do it if you needed.
