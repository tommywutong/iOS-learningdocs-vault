---
title: Dialogs and Special Panels
apple_id: 10000071i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Dialog/Articles/CustomAlertDialogs.html
archived_at: '2026-07-15T07:14:41.456771Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dialogs and Special Panels](Introduction%20to%20Dialogs%20and%20Special%20Panels.md)


[Next](Displaying%20Alert%20Help.md)[Previous](Displaying%20Alert%20Dialogs.md)

# Customizing Alert Dialogs

Beginning with OS X v10.5 (Leopard), [NSAlert](https://developer.apple.com/documentation/appkit/nsalert) includes methods for displaying and managing accessory views and managing the suppression check box. The following sections describe how to use these features.

An alert may have an accessory view, a view that contains controls and possibly other objects related to the alert. For example, an alert could warn a user that the file they’re copying will replace an existing file of the same name; it might have a checkbox for an accessory view that, if checked, results in the application saving the existing file under a slightly different name (for example, by appending “_save” to the filename).

You set an alert dialog’s accessory view using the [setAccessoryView:](https://developer.apple.com/documentation/appkit/nsalert/1530575-accessoryview) method. You may create the view programmatically, but a more common approach is to compose the view in Interface Builder. In the header file for the custom class, declare an outlet for the accessory view, and then connect this outlet in Interface Builder. By default, `NSAlert` positions the accessory view below the alert’s informative text and the suppression button (if any) and above the alert buttons, left-aligned with the informative text.

Listing 1 illustrates how to display an alert dialog that has both an accessory view and a suppression button, and how to handle the user’s response in both cases. Comments call out lines that are of particular interest to one or the other feature. (You can learn about suppression buttons in [Managing the Suppression Button](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcmjqfvjvona).)

__Listing 1__  Displaying an alert with an accessory view and a suppression button

```objc
static BOOL runAgain = YES; // Suppression button: static var holds current value of suppression button

- (void)showRecordDeleteAlert:(id)sender {
    if (runAgain == NO) // Suppression button: if user doesn't want to see alert, return
        return;
    NSAlert *alert = [[NSAlert alloc] init];
    [alert addButtonWithTitle:@"Delete"];
    [alert addButtonWithTitle:@"Extend"];
    [alert setMessageText:@"Delete the record?"];
    [alert setInformativeText:@"Deleted records cannot be restored.
           You may extend the valid-until date if you wish."];
    [alert setAlertStyle:NSWarningAlertStyle];
    [alert setShowsSuppressionButton:YES]; // Suppression button: show it
    [alert setAccessoryView:myView];  // Accessory view: "my" accessed via an outlet connection
    NSInteger result = [alert runModal];

    if ( result == NSAlertFirstButtonReturn ) {
        // "Delete" clicked
        [self deleteRecord:currentRec];

    } else if ( result == NSAlertSecondButtonReturn ) {  // Accessory view: handle user-specified data
        // "Extend" clicked
        NSDate *chosenDate = [myDatePicker dateValue];
        if ([chosenDate laterDate:[NSDate date]] == chosenDate) {
            [self setValidDate:chosenDate ofRecord:currentRec];
        }
    }
    runAgain = (BOOL)![[alert suppressionButton] state]; // Suppression button: get state of button
    [alert release];
}
```

If you want to customize the location of the accessory view, first call [layout](https://developer.apple.com/documentation/appkit/nsalert/1526747-layout) and then do any special positioning and sizing of the accessory view prior to running the alert. This sequence overrides the default behavior where `NSAlert` lazily lays out the accessory view just before showing the panel. You should call `layout` only after you have finished configuring the alert with message, informative text, buttons, and, if desired, suppression button. If you do any custom layouts, be advised that the default layout of the alert could change in future releases.

Alert dialogs may include a suppression button, which is a checkbox with a default title (localized) of “Do not show this message again.” (A checkbox is a type of button.) If the user selects the checkbox, the application should not display the alert again during the current application session. The suppression button is a feature intended to improve the user experience by allowing the application to suppress alerts about relatively trivial matters. The application is responsible for determining whether an alert should be displayed based on the user’s choice; in other words, suppression doesn’t happen automatically.

You add a suppression button to an alert dialog by sending the `NSAlert` object a [setShowsSuppressionButton:](https://developer.apple.com/documentation/appkit/nsalert/1535196-showssuppressionbutton) message with an argument of `YES`. Before running the alert dialog, you can fetch the suppression button by calling [suppressionButton](https://developer.apple.com/documentation/appkit/nsalert/1532209-suppressionbutton) and customize the button in certain ways. For example, you could customize the default title using the following nested message expression:

```
[[alert suppressionButton] setTitle:@"My new button title."];
```

You can also call `suppressionButton` and then set the initial state of the button or fetch its current state using the [setState:](https://developer.apple.com/documentation/appkit/nsbutton/1528907-state) and [state](https://developer.apple.com/documentation/appkit/nsbutton/1528907-state) methods of `NSButton`. After an alert is dismissed, you use the latter method to determine whether the user checked the suppression checkbox. The code example in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcmjqfvjvomq) illustrates a simple way—that is, the use of a static variable—to record the value of the suppression button and later check it before running the alert dialog again. However, a more useful approach might be to store the state of the suppression button in user defaults and later check it before showing the alert again.

By default, the suppression button is positioned below the informative text and above the accessory view (if any) and the alert buttons; it is left-aligned with the informative text. However do not count on the placement of this button, since it might change in the future. If you need a checkbox for purposes other than alert suppression, it is recommended you create an accessory view that is, or contains, a checkbox.

[Next](Displaying%20Alert%20Help.md)[Previous](Displaying%20Alert%20Dialogs.md)

