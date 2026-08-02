---
title: Dialogs and Special Panels
apple_id: 10000071i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Dialog/Tasks/UsingAlerts.html
archived_at: '2026-07-15T07:14:43.792854Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dialogs and Special Panels](Introduction%20to%20Dialogs%20and%20Special%20Panels.md)


[Next](Customizing%20Alert%20Dialogs.md)[Previous](Types%20of%20Alerts.md)

# Displaying Alert Dialogs

Alert dialogs inform the user of an event and present buttons that let the user choose how to proceed. You may implement alert dialogs by invoking methods of the [NSAlert](https://developer.apple.com/documentation/appkit/nsalert) class and by calling special functions.

Using the NSAlert API is the preferred approach if you are writing applications that run on Mac OS v10.3 (or later). You thereby gain the advantages of an object-oriented model as well as additional features, such as the ability to display help information related to the alert dialog.

Using the `NSAlert` API to display an alert dialog involves three simple steps: creating and initializing an `NSAlert` instance, running the dialog, and interpreting and acting on the user’s choice.

1. Create the `NSAlert` object though the standard Objective-C `alloc`-and-`init` procedure. Then send the required `NSAlert` “setter” messages to initialize the alert. [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3tcljrgi4tambzfvbegskgifauksq) gives an example of this.

   __Listing 1__  Creating and initializing the NSAlert object

```
NSAlert *alert = [[NSAlert alloc] init];
[alert addButtonWithTitle:@"OK"];
[alert addButtonWithTitle:@"Cancel"];
[alert setMessageText:@"Delete the record?"];
[alert setInformativeText:@"Deleted records cannot be restored."];
[alert setAlertStyle:NSWarningAlertStyle];
```
2. Invoke the [runModal](https://developer.apple.com/documentation/appkit/nsalert/1535441-runmodal) method on the `NSAlert` object.
3. Test the result return from `runModal` and proceed accordingly.

   [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3tcljrgi4tcnjrfvbegskkjbeecqi) illustrates the last two steps.

   __Listing 2__  Running the dialog and interpreting the result

```
if ([alert runModal] == NSAlertFirstButtonReturn) {
    // OK clicked, delete the record
    [self deleteRecord:currentRec];
}
[alert release];
```

   The return code is an `enum` constant identifying the button on the dialog that the user clicked. The first button added to the dialog (which, in left-to-right scripts, is the one closest to the right edge) is identified by `NSAlertFirstButtonReturn`. The second button that is added appears just to the left of the first and is identified by `NSAlertSecondButtonReturn` —and so forth for the third button.

   Make sure that you release the `NSAlert` instance.

You can also create an `NSAlert` object directly from an [NSError](https://developer.apple.com/documentation/foundation/nserror) object using the [alertWithError:](https://developer.apple.com/documentation/appkit/nsalert/1531823-init) method. You can then modally run the alert, thereby presenting the error information to the user. The method uses the localized description, recovery suggestion, and recovery options encapsulated by the `NSError` object for the alert's message text, informative text, and button titles, respectively.

As a convenience for compatibility with the older functional API (see [Using the Functional APIs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3tcljrgi4tiobx)), you can create `NSAlert` objects with the class factory method [alertWithMessageText:defaultButton:alternateButton:otherButton:informativeTextWithFormat:](https://developer.apple.com/documentation/appkit/nsalert/1550982-alertwithmessagetext). This method allows you to retain the earlier constants used to identify the button clicked. Here is an example of how you might invoke this method (with the previous example in mind):

```
NSAlert *alert = [NSAlert alertWithMessageText:@"Delete the record?"
    defaultButton:@"OK" alternateButton:@"Cancel"
    otherButton:nil informativeTextWithFormat:
    @"Deleted records cannot be restored."];
```


You can also call functions to create and display alerts. There are three kinds of functions:

- To create and run an alert panel, use [NSRunAlertPanel](https://developer.apple.com/documentation/appkit/1540934-nsrunalertpanel), [NSRunCriticalAlertPanel](https://developer.apple.com/documentation/appkit/1540943-nsruncriticalalertpanel), or [NSRunInformationalAlertPanel](https://developer.apple.com/documentation/appkit/1540926-nsruninformationalalertpanel).
- To create and run an alert sheet, use [NSBeginAlertSheet](https://developer.apple.com/documentation/appkit/1540941-nsbeginalertsheet), [NSBeginCriticalAlertSheet](https://developer.apple.com/documentation/appkit/1540925-nsbegincriticalalertsheet), or [NSBeginInformationalAlertSheet](https://developer.apple.com/documentation/appkit/1540936-nsbegininformationalalertsheet).
- To create an alert panel, use [NSGetAlertPanel](https://developer.apple.com/documentation/appkit/1540947-nsgetalertpanel), [NSGetCriticalAlertPanel](https://developer.apple.com/documentation/appkit/1540932-nsgetcriticalalertpanel), or [NSGetInformationalAlertPanel](https://developer.apple.com/documentation/appkit/1540937-nsgetinformationalalertpanel).

[Next](Customizing%20Alert%20Dialogs.md)[Previous](Types%20of%20Alerts.md)

