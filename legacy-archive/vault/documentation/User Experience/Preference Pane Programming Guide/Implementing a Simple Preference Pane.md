---
title: Preference Pane Programming Guide
apple_id: 10000110i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PreferencePanes/Tasks/Sample.html
archived_at: '2026-07-18T02:12:33.039017Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Preference Pane Programming Guide](Introduction.md)


[Next](Using%20Preference%20Panes%20in%20Other%20Applications.md)[Previous](Creating%20a%20Preference%20Pane%20Bundle.md)

# Implementing a Simple Preference Pane

This section takes you through the steps to create a simple preference pane that interacts with the user preference system. The preference pane stores and retrieves a pair of values using Core Foundation Preference Services. If you have already created a skeletal preference pane as described in [Creating a Preference Pane Bundle](Creating%20a%20Preference%20Pane%20Bundle.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydslkcifbemq2bijfa), you can use it here. Or, you can create a fresh preference pane and refer to the following instructions where appropriate.

The preference pane created in this section consists of a text field and a checkbox illustrating the handling of string and Boolean preferences.

1. Open the nib file in Interface Builder.
2. Drag a text field into the window. Label the field “A string value”.
3. Drag a checkbox into the window. Change its label to “A Boolean value”.
4. In the Classes pane of the main window, select your preference pane subclass.
5. In the Attributes pane of the Info window, add two outlets named `theTextField` and `theCheckbox`.
6. Add an action named `checkboxClicked:`.
7. In the Instances pane of the main window, make connections between the File’s Owner object (representing your preference pane subclass) and the text field and checkbox, connecting them to the `theTextField` and `theCheckbox` outlets.
8. Make a connection between the checkbox and the File’s Owner object, connecting the `checkboxClicked:` target-action method.
9. Save the nib file.
10. With your subclass highlighted in the Classes pane, choose Create Files from the Classes menu. Save the files into your project, overwriting if necessary.

The default preference pane header created by Interface Builder requires a few additions.

1. In Xcode, select the preference pane’s header file.
2. After the line importing `Cocoa.h` add the lines

```objc
#import <PreferencePanes/NSPreferencePane.h>
#import <CoreFoundation/CoreFoundation.h>
```
3. Update the outlet declarations to be

```
IBOutlet NSButton    *theCheckbox;
IBOutlet NSTextField *theTextField;
```
4. Add a new instance variable to hold the application ID of the target application:

```
CFStringRef appID;
```


The preference pane is initialized using the `initWithBundle:` method. Only the `appID` instance variable needs to be initialized here, but when overriding an `init` method, you also need to call the superclasses implementation. Add the following code to the preference pane’s implementation file.

```objc
- (id)initWithBundle:(NSBundle *)bundle
{
    if ( ( self = [super initWithBundle:bundle] ) != nil ) {
        appID = CFSTR(“com.mycompany.example.prefPaneSample”);
    }

    return self;
}
```


Immediately after the nib file has been loaded, the object receives a `mainViewDidLoad` message from the default implementation of `loadMainView`. Here you should initialize the user interface elements to reflect the current preference settings. Add the following code to the implementation file.

```objc
- (void)mainViewDidLoad
{
    CFPropertyListRef value;

    /* Initialize the checkbox */
    value = CFPreferencesCopyAppValue( CFSTR(“Bool Value Key”),  appID );
    if ( value && CFGetTypeID(value) == CFBooleanGetTypeID()  ) {
        [theCheckbox setState:CFBooleanGetValue(value)];
    } else {
        [theCheckbox setState:NO];
    }
    if ( value ) CFRelease(value);

    /* Initialize the text field */
    value = CFPreferencesCopyAppValue( CFSTR(“String Value Key”),  appID );
    if ( value && CFGetTypeID(value) == CFStringGetTypeID()  ) {
        [theTextField setStringValue:(NSString *)value];
    } else {
        [theTextField setStringValue:@””];
    }
    if ( value ) CFRelease(value);
}
```

For each of the two preferences being used, `mainViewDidLoad` requests the preference’s value from Core Foundation Preference Services. If a value is found for the preference (`value` is not `NULL`) and the value is of the correct data type, the preferences value is used to set the value of the appropriate user interface element. If the value does not exist, it initializes the elements with default values.

When the user clicks the checkbox, it sends an action message to the preference pane object. The `checkboxClicked:` method obtains the new state of the checkbox and stores it under the name “Bool Value Key”. Add the following code to the implementation file; an empty method definition should have been created by Interface Builder.

```objc
- (IBAction)checkboxClicked:(id)sender
{
    if ( [sender state] )
        CFPreferencesSetAppValue( CFSTR(“Bool Value Key”),
                    kCFBooleanTrue, appID );
    else
        CFPreferencesSetAppValue( CFSTR(“Bool Value Key”),
                    kCFBooleanFalse, appID );
}
```


When the preference pane gets deselected, either because the application is exiting or another preference pane is selected, it is sent a `didUnselect` message. In this method you want to extract the user’s preferences and save the changes to disk. Since the checkbox gets recorded whenever the user clicks it, only the text field needs to be updated here. After flushing the preferences to the disk, `didUnselect` broadcasts a notification. The notification assumes the target application is implemented to receive this notification and update its preferences while it is running. Add the following code to the implementation file.

```objc
- (void)didUnselect
{
    CFNotificationCenterRef center;

    CFPreferencesSetAppValue( CFSTR(“String Value Key”),
                [theTextField stringValue], appID );
    CFPreferencesAppSynchronize( appID );

    center = CFNotificationCenterGetDistributedCenter();
    CFNotificationCenterPostNotification(center,
            CFSTR(“Preferences Changed”), appID, NULL, TRUE);
}
```

[Next](Using%20Preference%20Panes%20in%20Other%20Applications.md)[Previous](Creating%20a%20Preference%20Pane%20Bundle.md)

