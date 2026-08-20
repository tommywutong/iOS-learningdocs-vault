---
title: Sheet Programming Topics
apple_id: 10000002i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-05-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sheets/Tasks/UsingAppModalDialogs.html
archived_at: '2026-07-15T07:19:06.989709Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sheet Programming Topics](Introduction%20to%20Sheets.md)


[Next](Document%20Revision%20History.md)[Previous](Positioning%20Sheets.md)

# Using Application-Modal Dialogs

You may occasionally find it necessary to use an application-modal dialog rather than a document-modal sheet. Recall that an application-modal dialog prevents the user from doing anything else within the owning application, although the user can switch to another application.

Working with application-modal dialogs is very similar to working with custom sheets. When working with application-modal dialogs, you are responsible for displaying as well as dismissing the dialog. You display a dialog with the `beginSheet:...` method, and you end an application-modal dialog with the `endSheet:` method. Between these two methods, your dialog is operating application modally.

You create your dialog using Interface Builder. It is important to remember to include a button to allow the user to dismiss the dialog when they are finished with it.

This discussion assumes that the dialog is in a separate nib file called `MyCustomDialog`. A Close button is defined on the dialog. The Close button is set to perform the `closeMyCustomDialog:` method when clicked.

The `showCustomDialog:` method displays the dialog modal to the window passed as a parameter. The arguments to `beginSheet:modalForWindow:modalDelegate:didEndSelector:contextInfo:` are similar to those for the `NSBeginAlertSheet` function, but the Close button on the dialog controls dismissing the dialog. After calling `beginSheet...`, the application continues to execute until it encounters `runModalForWindow:`. The user is still allowed to interact with the application-modal dialog (it wouldn’t make sense not to allow this), but activity in the rest of the application is suspended while this dialog is presented.

__Listing 1__  Displaying an application-modal dialog

```objc
- (void)showCustomDialog: (NSWindow *)window
// User has asked to see the dialog. Display it.
{
    if (!myCustomDialog)
        [NSBundle loadNibNamed: @"MyCustomDialog" owner: self];

    [NSApp beginSheet: myCustomDialog
            modalForWindow: window
            modalDelegate: nil
            didEndSelector: nil
            contextInfo: nil];
    [NSApp runModalForWindow: myCustomDialog];
    // Dialog is up here.
    [NSApp endSheet: myCustomDialog];
    [myCustomDialog orderOut: self];
}
```

When the user clicks the Close button, the following method is executed (this was specified in the nib file when creating the dialog), which stops the application’s modal display of the application-modal dialog.

__Listing 2__  Closing an application-modal dialog

```objc
- (IBAction)closeMyCustomDialog: (id)sender
{
    [NSApp stopModal];
}
```

Control is returned to `showCustomDialog:`, which cleans up by closing the dialog. It is important to call `orderOut:` when finished with your dialog, or it is not removed from the screen.

[Next](Document%20Revision%20History.md)[Previous](Positioning%20Sheets.md)

