---
title: Sheet Programming Topics
apple_id: 10000002i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-05-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sheets/DisplayAlertHelp.html
archived_at: '2026-07-15T07:19:03.971216Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sheet Programming Topics](Introduction%20to%20Sheets.md)


[Next](Using%20Custom%20Sheets.md)[Previous](Using%20Alert%20Sheets.md)

# Displaying Alert Help

The NSAlert class includes several methods that enable you to display help information related to an alert dialog or sheet. You can either use the application’s NSHelpManager object to find and display information using the Help Viewer application, or you can provide your own means for displaying help information.

An alert dialog or sheet advertises that help is available with a round question-mark button. You request the display of this button by sending `setShowsHelp:` to the NSAlert object with an argument of `YES`. To actually display the help, you have two options:

- Specify a help anchor, which the NSHelpManager object can use to find the help text to display in Help Viewer.

  Specify the help anchor by invoking NSAlert’s `setHelpAnchor:` method.
- Set a delegate for the NSAlert object and implement the delegate method `alertShowHelp:`. The delegate is responsible for displaying help information related to the alert.

Listing 1 shows how you might initialize an NSAlert object for the second help option.

__Listing 1__  Setting the help button and delegate for an alert dialog

```
NSAlert *alert = [[NSAlert alloc] init];
// other initializations here ...
[alert setShowsHelp:YES];
[alert setDelegate:self];
```

Listing 2 illustrates an implementation of the NSAlert `alertShowHelp:` delegate method.

__Listing 2__  Implementing the delegate method for displaying alert help

```objc
- (BOOL)alertShowHelp:(NSAlert *)alert {
    NSString *path = [[NSBundle mainBundle] pathForResource:@"Help" ofType:@"html"];
    BOOL flag = [[NSWorkspace sharedWorkspace] openFile:path];
    return flag;
}
```

If your application has more than one alert dialog or sheet for which it displays help, it should test the NSAlert object passed into this method to determine the help text to display. Always return `YES` unless the display of help did not succeed.

[Next](Using%20Custom%20Sheets.md)[Previous](Using%20Alert%20Sheets.md)

