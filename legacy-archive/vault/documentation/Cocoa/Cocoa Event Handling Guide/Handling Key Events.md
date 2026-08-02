---
title: Cocoa Event Handling Guide
apple_id: 10000060i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/HandlingKeyEvents/HandlingKeyEvents.html
archived_at: '2026-07-15T07:15:35.439281Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Event Handling Guide](Introduction.md)


[Next](Using%20Tracking-Area%20Objects.md)[Previous](Handling%20Mouse%20Events.md)

# Handling Key Events

An OS X system generates key events when a user presses a key on a keyboard or presses several keys simultaneously. When more than one key is pressed, one or more of those keys modifies the significance of the “main” key that is pressed. The most commonly used modifier keys are the Command, Control, Option (Alt), and Shift keys. In certain contexts and combinations, key presses represent commands to the operating system or the frontmost application and not characters to be inserted into text.

This chapter discusses how you handle key events, particularly key-down events.

The salient facts about key events, as presented in [Key Events](Event%20Objects%20and%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedilktk42q) and [The Path of Key Events](Event%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedglktk4yta), are the following:

- Key events are of three specific types ([NSEventType](https://developer.apple.com/documentation/appkit/nsevent/eventtype)), each of which is associated with an [NSResponder](https://developer.apple.com/documentation/appkit/nsresponder) method:

| Event-type constant | Event method |
| --- | --- |
| [NSKeyDown](https://developer.apple.com/documentation/appkit/nskeydown) | [keyDown:](https://developer.apple.com/documentation/appkit/nsresponder/1525805-keydown) |
| [NSKeyUp](https://developer.apple.com/documentation/appkit/nskeyup) | [keyUp:](https://developer.apple.com/documentation/appkit/nsresponder/1527436-keyup) |
| [NSFlagsChanged](https://developer.apple.com/documentation/appkit/nsflagschanged) | [flagsChanged:](https://developer.apple.com/documentation/appkit/nsresponder/1527647-flagschanged) |

  The `flagsChanged:` method can be useful for detecting the pressing of modifier keys without any other key being pressed simultaneously. For example, if the user presses the Option key by itself, your responder object can detect this in its implementation of `flagsChanged:`.
- _Most_ key events—that is, those representing characters to be inserted as text—are dispatched by the [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) object associated with the key window to the first responder.
- If the first responder does not handle the event, it passes the event up the responder chain (see [The Responder Chain](Event%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedglktk4za)).
- The delivery path of a key event varies according to whether the event represents a character, a key equivalent, a keyboard action, or a keyboard interface control command. The global application object (`NSApp`) first looks for key equivalents and then keyboard interface control commands and handles them specially (see [The Path of Key Events](Event%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedglktk4yta) for details). If the event is neither of these, it dispatches it to the `NSWindow` object representing the key window, which in turn dispatches the event to the first responder in a [keyDown:](https://developer.apple.com/documentation/appkit/nsresponder/1525805-keydown) message.
- The responder object determines what the key event represents and handles it appropriately. At this point, the key event could represent any one of the following things:

  - A keyboard action, which is a key or key combination bound to an action-message selector in a key bindings dictionary (see [Key Bindings](Text%20System%20Defaults%20and%20Key%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgq3dqljwgeytambv)).
  - An application-specific command or action (one not using the key bindings dictionary)
  - A character or characters to insert into text

  See [Overriding the keyDown: Method](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedolktk4za) for more information.
- As with key event messages, a keyboard action message is passed up the responder chain if the first responder does not handle it.

Most responder objects (such as custom views) handle key events by overriding the [keyDown:](https://developer.apple.com/documentation/appkit/nsresponder/1525805-keydown) method declared by `NSResponder`. The object can handle the event in any way it sees fit. A text object typically interprets the message as a request to insert text, while a drawing object might only be interested in a few keys, such as Delete and the arrow keys as commands to delete and move selected items. As with mouse events, a responder object often wants to query the passed-in [NSEvent](https://developer.apple.com/documentation/appkit/nsevent) object to find out more about the event and obtain the data it needs to handle it. Some of the more useful `NSEvent` methods for key events are the following:

- [characters](https://developer.apple.com/documentation/appkit/nsevent/1534183-characters) and [charactersIgnoringModifiers](https://developer.apple.com/documentation/appkit/nsevent/1524605-charactersignoringmodifiers)—The responder can extract the Unicode character data associated with the event and insert it as text or interpret it as commands. The `charactersIgnoringModifiers` method ignores any modifier keystroke (except for Shift) when returning the character data. Note that both method names are plural because a keystroke can produce more than one character (for example, “à” is composed of ‘a’ and ‘`‘).
- [modifierFlags](https://developer.apple.com/documentation/appkit/nsevent/1534405-modifierflags)—Using this method the responder can determine if any modifier keys were pressed.
- [isARepeat](https://developer.apple.com/documentation/appkit/nsevent/1528049-isarepeat)—This method tells the responder whether the same key was pressed rapidly in succession.

Within an implementation of a `keyDown:` method, a responder can extract the character data contained by the associated `NSEvent` object and insert it into displayed text; or it can interpret the character data as a key or key combination that is either bound to a keyboard action or requests some application-specific behavior. However, the Application Kit provides some convenient shortcuts for doing this, described below.

Responder objects that deal with text, such as text views, have to be prepared to handle key events that can either be characters to insert or keyboard actions. As noted in [The Path of Key Events](Event%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedglktk4yta), keyboard actions are a special kind of action message that depends on the key bindings mechanism, which binds specific keystrokes (for example, Control-e) to specific commands related to the text (for example, move the insertion point to the end of the current line). These commands are implemented in methods defined by `NSResponder` to give per-view functional interpretations of those physical keystrokes.

In handling a key event in `keyDown:`, a view object that expects to insert text first determines whether the character or characters of the `NSEvent` object represent a keyboard action. If they do, it sends the associated action message; if they don’t, it inserts the characters as text. Specifically, the view can do one of two things in its implementation:

- It can extract the event object’s characters using the `characters` method of `NSEvent` and interpret these to see if they are associated with a known keyboard action. If they are, it invokes the appropriate action method in itself or a superview. This approach is discouraged.
- It can pass the event to Cocoa’s text input management system by invoking the `NSResponder` method [interpretKeyEvents:](https://developer.apple.com/documentation/appkit/nsresponder/1531599-interpretkeyevents). The input management system checks the pressed key against entries in all relevant key-binding dictionaries and, if there is a match, sends a `doCommandBySelector:` message back to the view. Otherwise, it sends an `insertText:` message back to the view, and the view implements this method to extract and display the text.

Listing 5-1 shows how the second approach might look in code.

__Listing 5-1__  Using the input management system to interpret a key event

```objc
- (void)keyDown:(NSEvent *)theEvent {
    [self interpretKeyEvents:[NSArray arrayWithObject:theEvent]];
}

// The following action methods are declared in NSResponder.h
- (void)insertTab:(id)sender {
    if ([[self window] firstResponder] == self) {
        [[self window] selectNextKeyView:self];
    }
}

- (void)insertBacktab:(id)sender {
    if ([[self window] firstResponder] == self) {
        [[self window] selectPreviousKeyView:self];
    }
}

- (void)insertText:(id)string {
    [super insertText:string];  // have superclass insert it
}
```

Note that this example includes an override of `insertText:` that simply invokes the superclass implementation. This is done to clarify the role of the input manager but is not really necessary. The default (`NSResponder`) implementation of `doCommandBySelector:` determines if the view responds to the keyboard-action selector and, if the view does respond, it invokes the action method; if the view doesn’t respond, `doCommandBySelector:` is sent to the next responder (and so on up the responder chain). Therefore, a view should only implement the action methods corresponding to the actions that it wants to handle. Another implication of input-manager behavior is that if the key-bindings dictionary matches a physical keystroke with a keyboard action, the responder object simply needs to override the associated action method to handle that keystroke. For example, to handle the default binding of the Escape key, the responder would override the `cancelOperation:` method of `NSResponder`.

A case in point of a superview handling a keyboard-action message initiated by a subview is the way the [NSScrollView](https://developer.apple.com/documentation/appkit/nsscrollview) object handles page-down commands. This scroll-view object is a compound object consisting of a document view, a clip view (an [NSClipView](https://developer.apple.com/documentation/appkit/nsclipview) object) and a scroller (an [NSScroller](https://developer.apple.com/documentation/appkit/nsscroller) object). Because it is the containing or coordinating object, the `NSScrollView` object is the superview of all other objects in this grouping. Now say your custom view is the document view of the scroll view. If you implement `keyDown:` to send `interpretKeyEvents:` to the input manager but do not implement the `scrollPageDown:` action method, the document view will still be scrolled within the scroll view when the user presses the Page Down key (or whatever key binding is in effect for that function). This happens because each next responder in the responder chain is queried to see if it responds to `scrollPageDown:`. The `NSScrollView` class provides a default implementation, so this implementation is invoked.

Applications other that those that deal with text can use the input management system to their benefit. For example, a custom view in a drawing application might use arrow keys to "nudge” graphical objects precise distances. In the standard key bindings dictionary the arrow keys are bound to the `moveUp:`, `moveDown:`, `moveLeft:`, and `moveRight:` methods of `NSResponder`. So code similar to that shown in Listing 5-2 would work to nudge the graphical objects around.

__Listing 5-2__  Handling arrow-key characters using the input management system

```objc
- (void)keyDown:(NSEvent *)theEvent {
    // Arrow keys are associated with the numeric keypad
    if ([theEvent modifierFlags] & NSNumericPadKeyMask) {
        [self interpretKeyEvents:[NSArray arrayWithObject:theEvent]];
    } else {
        [super keyDown:theEvent];
    }
}

-(IBAction)moveUp:(id)sender
{
    [self offsetLocationByX:0 andY: 10.0];
    [[self window] invalidateCursorRectsForView:self];
}

-(IBAction)moveDown:(id)sender
{
    [self offsetLocationByX:0 andY:-10.0];
    [[self window] invalidateCursorRectsForView:self];
}

-(IBAction)moveLeft:(id)sender
{
    [self offsetLocationByX:-10.0 andY:0.0];
    [[self window] invalidateCursorRectsForView:self];
}

-(IBAction)moveRight:(id)sender
{
    [self offsetLocationByX:10.0 andY:0.0];
    [[self window] invalidateCursorRectsForView:self];
}
```

In most instances, the `interpretKeyEvents:` approach is preferable to the interpret-yourself approach. This recommendation is particularly true for those custom views in applications such as word processors and graphical editors that do the lion’s share of the work. The major factor favoring the use of the text input management system is that, with it, you don’t need to hard-wire function to physical key. What if the user is using a portable computer that is lacking a function key hard-wired by the application? The better, more flexible approach is to specify alternative key bindings in a dictionary. Another advantage of the text input management system is that it allows key events to be interpreted as text not directly available on the keyboard, such as Kanji and some accented characters.

Although using the text input management system is advantageous, you can interpret physical keys yourself in `keyDown:` and handle them in an application-specific way. The [NSEvent](https://developer.apple.com/documentation/appkit/nsevent) class declares dozens of constants that identify particular keys either by key symbol or key function; Constants in the reference documentation for that class describes these constants. Listing 5-3 shows a sampling.

__Listing 5-3__  Some key constants defined by NSResponder

```
enum {
    NSUpArrowFunctionKey            = 0xF700,
    NSDownArrowFunctionKey          = 0xF701,
    NSLeftArrowFunctionKey          = 0xF702,
    NSRightArrowFunctionKey         = 0xF703,
    NSF1FunctionKey                 = 0xF704,
    NSF2FunctionKey                 = 0xF705,
    NSF3FunctionKey                 = 0xF706,
    // other constants here
    NSUndoFunctionKey               = 0xF743,
    NSRedoFunctionKey               = 0xF744,
    NSFindFunctionKey               = 0xF745,
    NSHelpFunctionKey               = 0xF746,
    NSModeSwitchFunctionKey         = 0xF747
};
```

Also, the text system defines constants representing commonly-used Unicode characters, such as tab, delete, and carriage return. For a list of these constants, see Constants in _[NSText Class Reference](https://developer.apple.com/documentation/appkit/nstext)_.

In your implementation of `keyDown:` you can compare one of these constants to the character data of the key-event object to determine if a certain key was pressed and then act accordingly. As you may recall, the [characters](https://developer.apple.com/documentation/appkit/nsevent/1534183-characters) or [charactersIgnoringModifiers](https://developer.apple.com/documentation/appkit/nsevent/1524605-charactersignoringmodifiers) methods return an [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) object for a key value instead of a character because a keystroke might generate multiple characters. (In fact, these methods could even return an empty string if a dead key—a key with no character mapped to it—is pressed.) If your implementation of `keyDown:` is handling a single-character key value, such as an arrow key, you can examine the length of the returned string and, if it is a single character, access that character using the `NSString` method [characterAtIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/characterAtIndex:) with an index of 0. Then test that character against one of the `NSResponder` constants.

Listing 5-4 shows how you might perform the same graphical-object “nudging” as done in [Listing 5-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedolktk42a), but this time the responder object itself determines whether an arrow key was pressed.

__Listing 5-4__  Handling arrow-key characters by interpreting the physical key

```objc
- (void)keyDown:(NSEvent *)theEvent {

    if ([theEvent modifierFlags] & NSNumericPadKeyMask) { // arrow keys have this mask
        NSString *theArrow = [theEvent charactersIgnoringModifiers];
        unichar keyChar = 0;
        if ( [theArrow length] == 0 )
            return;            // reject dead keys
        if ( [theArrow length] == 1 ) {
            keyChar = [theArrow characterAtIndex:0];
            if ( keyChar == NSLeftArrowFunctionKey ) {
                [self offsetLocationByX:-10.0 andY:0.0];
                [[self window] invalidateCursorRectsForView:self];
                return;
            }
            if ( keyChar == NSRightArrowFunctionKey ) {
                [self offsetLocationByX:10.0 andY:0.0];
                [[self window] invalidateCursorRectsForView:self];
                return;
            }
            if ( keyChar == NSUpArrowFunctionKey ) {
                [self offsetLocationByX:0 andY: 10.0];
                [[self window] invalidateCursorRectsForView:self];
                return;
            }
            if ( keyChar == NSDownArrowFunctionKey ) {
                [self offsetLocationByX:0 andY:-10.0];
                [[self window] invalidateCursorRectsForView:self];
                return;
            }
            [super keyDown:theEvent];
        }
    }
    [super keyDown:theEvent];
}
```

You can also convert an `NSResponder` constant to a string object and then compare that object to the value returned by `characters` or `charactersIgnoringModifiers`, as in this example:

```
        unichar la = NSLeftArrowFunctionKey;
        NSString *laStr = [[[NSString alloc] initWithCharacters:&la length:1] autorelease];
        if ([theArrow isEqual:laStr]) {
            [self offsetLocationByX:-10.0 andY:0.0];
            [[self window] invalidateCursorRectsForView:self];
            return;
        }
```

However, this approach is more memory-intensive.

A key equivalent is a character bound to some view in a window. This binding causes that view to perform a specified action when the user types that character, typically while pressing a modifier key (in most cases the Command key). A key equivalent must be a character that can be typed with no modifier keys, or with Shift only.

An application routes a key-equivalent event by sending it first down the view hierarchy of a window. The global `NSApplication` object dispatches events it recognizes as potential key equivalents (based on the presence of modifier flags) in its [sendEvent:](https://developer.apple.com/documentation/appkit/nsapplication/1428359-sendevent) method. It sends a [performKeyEquivalent:](https://developer.apple.com/documentation/appkit/nsresponder/1524690-performkeyequivalent) message to the key [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) object. This object passes key equivalents down its view hierarchy by invoking the `NSView` default implementation of [performKeyEquivalent:](https://developer.apple.com/documentation/appkit/nsview/1483664-performkeyequivalent), which forwards the message to each of its subviews (including contextual and pop-up menus) until one responds `YES`; if none does, it returns `NO`. If no object in the view hierarchy handles the key equivalent, `NSApp` then sends `performKeyEquivalent:` to the menus in the menu bar. `NSWindow` subclasses are discouraged from overriding `performKeyEquivalent:`.

Some Cocoa classes, such as [NSButton](https://developer.apple.com/documentation/appkit/nsbutton), [NSMenu](https://developer.apple.com/documentation/appkit/nsmenu), [NSMatrix](https://developer.apple.com/documentation/appkit/nsmatrix), and [NSSavePanel](https://developer.apple.com/documentation/appkit/nssavepanel), provide default implementations of `performKeyEquivalent:`. For example, you can set the Return key as the key equivalent of an `NSButton` object and, when this key is pressed, the button acts as if it has been clicked. However, subclasses of other Application Kit classes (including custom views) need to provide their own implementations of `performKeyEquivalent:`. The implementation should extract the characters for a key equivalent from the passed-in `NSEvent` object using the [charactersIgnoringModifiers](https://developer.apple.com/documentation/appkit/nsevent/1524605-charactersignoringmodifiers) method and then examine them to determine if they are a key equivalent it recognizes. It handles the key equivalent much as it would handle a key event in `keyDown:` (see [Overriding the keyDown: Method](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedolktk4za)). After handling the key equivalent, the implementation should return `YES`. If it doesn’t handle the key equivalent, it should either invoke the superclass implementation of `performKeyEquivalent:` or (if you know the superclass doesn’t handle the key equivalent) return `NO` to indicate that the key equivalent should be passed further down the view hierarchy or to the menus in the menu bar.

The Cocoa event-dispatch architecture treats certain key events as commands to move control focus to a different user-interface object in a window, to simulate a mouse click on an object, to dismiss modal windows, and to make selections in objects that allow selections. This capability is called keyboard interface control. Most of the user-interface objects involved in keyboard interface control are [NSControl](https://developer.apple.com/documentation/appkit/nscontrol) objects, but objects that aren’t controls can participate as well. When an object has control focus, the Application Kit draws a light-blue key-focus ring around the object’s border. If full keyboard access is enabled, the keys listed in Table 5-1 have the stated effect.

__Table 5-1__  Keys used in keyboard interface control

| Key | Effect |
| Tab | Move to next key view. |
| Shift-Tab | Move to previous key view. |
| Space | Select, as with mouse click in a check box (for example), or toggle state. In selection lists, selects or deselects highlighted item. |
| Arrow keys | Move within compound view, such as [NSForm](https://developer.apple.com/documentation/appkit/nsform) objects. |
| Control-Tab (Control-Shift-Tab) | Go to next (previous) key view from views where tab characters have other significance (for example, [NSTextView](https://developer.apple.com/documentation/appkit/nstextview) objects). |
| Option or Shift | Extend the selection, not affecting other selected items. |

Some objects found on Interface Builder palettes do not participate in keyboard interface control, such as [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview), [WebView](https://developer.apple.com/documentation/webkit/webview), and [PDFView](https://developer.apple.com/documentation/pdfkit/pdfview) objects.

In addition to the key view loop, a window can have a default button cell, which uses the Return (or Enter) key as its key equivalent. Programmatically, you can send [setDefaultButtonCell:](https://developer.apple.com/documentation/appkit/nswindow/1419328-defaultbuttoncell) to an `NSWindow` object to set this button cell; you can also set it in Interface Builder by setting a button cell’s key equivalent to ‘`\r`’ in the Attributes pane of the Get Info window. The default button cell draws itself as a focal element for keyboard interface control unless another button cell is focused on. In this case, it temporarily draws itself as normal and disables its key equivalent. The Escape key is another default key for a keyboard interface control in a window; it immediately aborts a modal loop.

The user-interface objects that are connected together in a window make up the window’s key view loop. A key view loop is a sequence of `NSView` objects connected to each other through their [nextKeyView](https://developer.apple.com/documentation/appkit/nsview/1483465-nextkeyview) property (the [previousKeyView](https://developer.apple.com/documentation/appkit/nsview/1483646-previouskeyview) property when going in reverse direction). The last view in this sequence “loops” back to the first view. By default, `NSWindow` assigns an initial first responder and constructs a key view loop with the objects it finds. If you want greater control over the key view loop you should set it up using Interface Builder. See the Help pages for Interface Builder for details of the procedure.

For its instances to participate in key-view loops, a custom view must return `YES` from [acceptsFirstResponder](https://developer.apple.com/documentation/appkit/nsresponder/1528708-acceptsfirstresponder). By doing so, it affects the value returned by the [canBecomeKeyView](https://developer.apple.com/documentation/appkit/nsview/1483759-canbecomekeyview) method. The [acceptsFirstResponder](https://developer.apple.com/documentation/appkit/nsresponder/1528708-acceptsfirstresponder) method controls whether a responder accepts first responder status when its window asks it to (that is, when makeFirstResponder: is called with the responder as the parameter). The [canBecomeKeyView](https://developer.apple.com/documentation/appkit/nsview/1483759-canbecomekeyview) method controls whether the Application Kit allows tabbing to a view. It calls [acceptsFirstResponder](https://developer.apple.com/documentation/appkit/nsresponder/1528708-acceptsfirstresponder), but it also checks for other information before determining the value to return, such as whether the view is hidden and whether full keyboard access is on. The [canBecomeKeyView](https://developer.apple.com/documentation/appkit/nsview/1483759-canbecomekeyview) method is rarely overridden while [acceptsFirstResponder](https://developer.apple.com/documentation/appkit/nsresponder/1528708-acceptsfirstresponder) is frequently overridden.

The `NSView` and `NSWindow` classes define a number of methods for setting up and traversing the key view loop programmatically. Table 5-2 lists some of the more useful ones.

__Table 5-2__  Some key-view loop methods

| [nextKeyView](https://developer.apple.com/documentation/appkit/nsview/1483465-nextkeyview) (`NSView`)  [previousKeyView](https://developer.apple.com/documentation/appkit/nsview/1483646-previouskeyview) (`NSView`) | Returns the next and previous view objects in the key view loop. |
| [setNextKeyView:](https://developer.apple.com/documentation/appkit/nsview/1483465-nextkeyview) (`NSView`) | Sets the next key view in the loop. |
| [selectNextKeyView:](https://developer.apple.com/documentation/appkit/nswindow/1419715-selectnextkeyview) (`NSWindow`)  [selectPreviousKeyView:](https://developer.apple.com/documentation/appkit/nswindow/1419110-selectpreviouskeyview) (`NSWindow`) | Searches the view hierarchy for a candidate next (previous) key view and, if it finds one, makes it the first responder. |
| [canBecomeKeyView](https://developer.apple.com/documentation/appkit/nsview/1483759-canbecomekeyview) (`NSView`) | Returns whether the receiver can become a key view. |
| [nextValidKeyView](https://developer.apple.com/documentation/appkit/nsview/1483572-nextvalidkeyview) (`NSView`)  [previousValidKeyView](https://developer.apple.com/documentation/appkit/nsview/1483371-previousvalidkeyview) (`NSView`) | Returns the closest view object in the key view loop that follows the receiver and accepts first responder status. |

The code in Listing 5-5 illustrates how one might use some of these methods to manipulate the key-view loop.

__Listing 5-5__  Manipulating the key-view loop

```objc
- (void)textDidEndEditing:(NSNotification *)notification {
    NSTextView *text = [notification object];
    unsigned whyEnd = [[[notification userInfo] objectForKey:@"NSTextMovement"] unsignedIntValue];
    NSTextView *newKeyView = text;

    // Unscroll the previous text.
    [text scrollRangeToVisible:NSMakeRange(0, 0)];

    if (whyEnd == NSTabTextMovement) {
        newKeyView = (NSTextView *)[text nextKeyView];
    } else if (whyEnd == NSBacktabTextMovement) {
        newKeyView = (NSTextView *)[text previousKeyView];
    }

    // Set the new key view and select its whole contents.
    [[text window] makeFirstResponder:newKeyView];
    [newKeyView setSelectedRange:NSMakeRange(0, [[newKeyView textStorage] length])];
}
```

[Next](Using%20Tracking-Area%20Objects.md)[Previous](Handling%20Mouse%20Events.md)

