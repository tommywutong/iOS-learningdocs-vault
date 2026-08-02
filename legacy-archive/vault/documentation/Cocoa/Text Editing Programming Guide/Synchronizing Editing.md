---
title: Text Editing Programming Guide
apple_id: 10000157i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextEditing/Tasks/BatchEditing.html
archived_at: '2026-07-15T07:20:12.386383Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Editing Programming Guide](Introduction%20to%20Text%20Editing%20Programming%20Guide%20for%20Cocoa.md)


[Next](Setting%20Focus%20and%20Selection%20Programmatically.md)[Previous](Creating%20Custom%20Views.md)

# Synchronizing Editing

The editing process involves careful synchronization of the complex interaction of various objects. The text system coordinates event processing, data modification, responder chain management, glyph generation, and layout to maintain consistency in the text data model.

The system provides a rich set of notifications to delegates and observers to enable your code to interact with this logic, as described in [Delegate Messages and Notifications](Delegate%20Messages%20and%20Notifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqheztelkdjjbeuschifdq).

If your code needs to modify the text backing store directly, you should use batch-editing mode; that is, bracket the changes between the `NSMutableAttributedString` methods `beginEditing` and `endEditing`. Although this bracketing is not strictly necessary, it’s good practice, and it’s important for efficiency if you’re making multiple changes in succession. `NSTextView` uses the `beginEditing` and `endEditing` methods to synchronize its editing activity, and you can use the methods directly to control the timing of notifications to delegates, observers, and associated layout managers. When the `NSTextStorage` object is in batch-editing mode, it refrains from informing its layout managers of any editing changes until it receives the `endEditing` message.

The “beginning of editing” means that a series of modifications to the text backing store (`NSTextStorage` for text views and cell values for cells) is about to occur. Bracketing editing between `beginEditing` and `endEditing` locks down the text storage to ensure that text modifications are atomic transactions.

The “end of editing” means that the backing store is in a consistent state after modification. In cells (such as `NSTextFieldCell` objects, which control text editing in text fields), the end of editing coincides with the field editor resigning first responder status, which triggers synchronization of the contents of the field editor and its parent cell.

In addition, the text view sends `NSTextDidEndEditingNotification` when it completes modifying its backing store, regardless of its first responder status. For example, it sends out this notification when the Replace All button is clicked in the Find window, even if the text view is not the first responder.

Listing 1 illustrates a situation in which the `NSTextView` method `scrollRangeToVisible:` forces layout to occur and raises an exception.

__Listing 1__  Forcing layout

```
[[myTextView textStorage] beginEditing];
[[myTextView textStorage] replaceCharactersInRange:NSMakeRange(0,0)
        withString:@"Hello to you!"];
[myTextView scrollrangeToVisible:NSMakeRange(0,13)]; //BOOM
[[myTextView textStorage] endEditing];
```

Scrolling a character range into visibility requires layout to be complete through that range so the text view can know where the range is located. But in Listing 1, the text storage is in batch-editing mode. It is in an inconsistent state, so the layout manager has no way to do layout at this time. Moving the `scrollRangeToVisible:` call after `endEditing` would solve the problem.

There are additional actions that you should take if you implement new user actions in a text view, such as a menu action or key binding method that changes the text. For example, you can modify the selected range of characters using the `NSText` method `setSelectedRange`, depending on the type of change performed by the command, using the results of the `NSTextView` methods `rangeForUserTextChange`, `rangeForUserCharacterAttributeChange`, or `rangeForUserParagraphAttributeChange`. For example, `rangeForUserParagraphAttributeChange` returns the entire paragraph containing the original selection—that is the range affected if your action modifies paragraph attributes. Also, you should call `textView:shouldChangeTextInRange:replacementString:` before you make the change and `didChangeText` afterwards. These actions ensure that the correct text gets changed and the system sends the correct notifications and delegate messages to the text view’s delegate. See [Subclassing NSTextView](Subclassing%20NSTextView.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqheztolkdjjbeuschifdq) for more information.

There may be situations in which you need to force the text system to end editing programmatically so you can take some action dependent on notifications being sent. In such a case, you don’t need to modify the editing mechanism but simply stimulate its normal behavior.

To force the end of editing in a text view, which subsequently sends a `textDidEndEditing:` notification message to its delegate, you can observe the window’s `NSWindowDidResignKey` notification. Then, in the observer method, send `makeFirstResponder:` to the window to finish any editing in progress while the window was active. Otherwise, the control that is currently being edited remains the first responder of the window and does not end editing.

Listing 2 presents an implementation of the `textDidEndEditing:` delegate method that ends editing in an `NSTableView` subclass. By default, when the user is editing a cell in a table view and presses Tab or Return, the field editor ends editing in the current cell and begins editing the next cell. In this case, you want to end editing altogether if the user presses Return. This method distinguishes which key the user pressed; for a Tab it does the normal behavior, and for Return it forces the end of editing completely by making the window first responder.

__Listing 2__  Forcing the end of editing

```objc
- (void)textDidEndEditing:(NSNotification *)notification {
    if([[[notification userInfo] valueForKey:@"NSTextMovement"] intValue] ==
                        NSReturnTextMovement) {
        NSMutableDictionary *newUserInfo;
        newUserInfo = [[NSMutableDictionary alloc]
                            initWithDictionary:[notification userInfo]];
        [newUserInfo setObject:[NSNumber numberWithInt:NSIllegalTextMovement]
                                forKey:@"NSTextMovement"];
        notification = [NSNotification notificationWithName:[notification name]
                                object:[notification object]
                                userInfo:newUserInfo];
        [super textDidEndEditing:notification];
        [newUserInfo release];
        [[self window] makeFirstResponder:self];
    } else {
        [super textDidEndEditing:notification];
    }
}
```

[Next](Setting%20Focus%20and%20Selection%20Programmatically.md)[Previous](Creating%20Custom%20Views.md)

