---
title: Sheet Programming Topics
apple_id: 10000002i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-05-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sheets/Tasks/UsingCustomSheets.html
archived_at: '2026-07-15T07:19:08.492229Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sheet Programming Topics](Introduction%20to%20Sheets.md)


[Next](Presenting%20a%20Series%20of%20Sheets.md)[Previous](Displaying%20Alert%20Help.md)

# Using Custom Sheets

One type of sheet is an alert sheet, which was discussed in [Using Alert Sheets](Using%20Alert%20Sheets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2dklkcifbemskcjfaq). If the type of information presented in alert sheets is not suitable for your application, you can create and present a custom sheet.

When working with custom sheets, you are responsible for displaying as well as dismissing the sheet. You display a sheet with the `beginSheet:...` method, and you end a sheet with the `endSheet:` method. Between these two methods, your sheet is operating modally.

You create your custom sheet using Interface Builder. It is important to remember to include a button to allow the user to dismiss the sheet when they are finished with it.

This discussion assumes that the sheet is in a separate nib file called `MyCustomSheet`. A Close button is defined on the sheet. The Close button is set to perform the `closeCustomSheet:` method when clicked.

The `showCustomSheet:` method displays the custom sheet modal to the window passed as a parameter. The arguments to `beginSheet:modalForWindow:modalDelegate:didEndSelector:contextInfo:` are similar to those for the `NSBeginAlertSheet` function, but the Close button on the custom sheet controls dismissing the sheet. A did-end selector is specified to handle any activity necessary before dismissing the sheet.

__Listing 1__  Displaying a custom sheet

```objc
- (void)showCustomSheet: (NSWindow *)window

// User has asked to see the custom display. Display it.
{
    if (!myCustomSheet)
//Check the myCustomSheet instance variable to make sure the custom sheet does not already exist.
        [NSBundle loadNibNamed: @"MyCustomSheet" owner: self];

    [NSApp beginSheet: myCustomSheet
            modalForWindow: window
            modalDelegate: self
            didEndSelector: @selector(didEndSheet:returnCode:contextInfo:)
            contextInfo: nil];

    // Sheet is up here.
    // Return processing to the event loop
}
```

When the user clicks the Close button, the following method is executed (this was specified in the nib file when creating the sheet).

__Listing 2__  Closing a custom sheet

```objc
- (IBAction)closeMyCustomSheet: (id)sender
{
    [NSApp endSheet:myCustomSheet];
}
```

Control is sent to the did-end selector, which cleans up by closing the custom sheet. It is important to call `orderOut:` when finished with your sheet, or it is not removed from the screen.

__Listing 3__  Did-end selector

```objc
- (void)didEndSheet:(NSWindow *)sheet returnCode:(NSInteger)returnCode contextInfo:(void *)contextInfo
{
    [sheet orderOut:self];
}
```

[Next](Presenting%20a%20Series%20of%20Sheets.md)[Previous](Displaying%20Alert%20Help.md)

