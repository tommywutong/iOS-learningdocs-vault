---
title: Preference Pane Programming Guide
apple_id: 10000110i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PreferencePanes/Tasks/OtherApps.html
archived_at: '2026-07-18T02:12:31.797945Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Preference Pane Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Implementing%20a%20Simple%20Preference%20Pane.md)

# Using Preference Panes in Other Applications

The NSPreferencePane class is not restricted to use only by System Preferences. Your own application can use it as well. You can reuse preference panes intended for System Preferences just like the Mac OS X Setup Assistant does with the Date & Time preference pane. Or, you can write preference panes for use exclusively by your own application.

Embedding a preference pane into your own application is largely a matter of adding the preference pane’s main view into a window and sending the proper information messages to the preference pane object. The preference pane object is responsible for accessing and saving user preferences. The procedure is as follows.

1. Initialize the preference pane. If you have the path to the preference pane bundle, load and initialize the preference pane object with the following lines of code.

```
NSBundle *prefBundle = [NSBundle bundleWithPath: pathToPrefPaneBundle];
Class prefPaneClass = [prefBundle principalClass];
NSPreferencePane *prefPaneObject = [[prefPaneClass alloc]
            initWithBundle:prefBundle];
```

   For preference panes stored within the application’s bundle, use one of the NSBundle `pathForResource` methods to obtain the path to the preference pane. For example, if the preference panes are stored in a subdirectory named `PreferencePanes` in the application’s `Resources` directory, the full path can be obtained using

```
pathToPrefPaneBundle = [[NSBundle mainBundle]
            pathForResource: @”NameOfPane” ofType: @”prefPane”
            inDirectory: @”PreferencePanes”];
```
2. Select the preference pane. When you are ready to display the preference pane, send it a `loadMainView` message. Its return value is the preference pane’s main view if successful; on failure it returns `nil`. Next, notify the preference pane that it is about to be displayed by sending it a `willSelect` message. Because this method may potentially alter the preference pane’s main view, get the main view again with the `mainView` message. Now add the view into your window. Center the preference pane view horizontally, but resize the window vertically to accommodate the view. Finally, send the preference pane object a `didSelect` message.

   The code for selecting the preference pane looks like the following.

```
NSView *prefView;
if ( [prefPaneObject loadMainView] ) {
    [prefPaneObject willSelect];
    prefView = [prefPaneObject mainView];
    /* Add view to window */
    [prefPaneObject didSelect];
} else {
    /* loadMainView failed -- handle error */
}
```
3. Deselect the preference pane. The application is required to deselect the preference pane before any of the following actions occur:

   - the window switches to a different view
   - the preference pane’s window closes
   - the application quits

   The application is required to release the object only when quitting the application; for the other events, the preference pane object can be reselected at a later time.

   The first step is to ask the preference pane object whether it is willing to be deselected by sending it a `shouldUnselect` message. The object can refuse to be deselected if one of the user preferences has an unacceptable value. The method returns one of the values from [Table 1](Life%20Cycle%20of%20a%20Preference%20Pane.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydiljrgiydcmzu) to indicate its willingness to be deselected. If the preference pane object returns `NSUnselectLater`, it is indicating that it needs to obtain some more information from the user before it knows what action to take. When the preference pane object is ready, it posts one of the following two notifications to indicate whether it is now OK to continue or you should abort the deselection.

|  |  |
| --- | --- |
| `NSPreferencePaneDoUnselectNotification` | Do the deselection |
| `NSPreferencePaneCancelUnselectNotification` | Cancel the deselection |

   When `NSUnselectLater` is returned, register for these two notifications coming from the preference pane object and temporarily abort the deselection. Continue as appropriate after receiving one of these notifications.

   When the preference pane object indicates it can be deselected, send it a `willUnselect` message. Next, perform the appropriate action causing the deselection: remove the view, close the window, or prepare to exit. Finally, send the object a `didUnselect` message.

   If you do not expect to use the preference pane object again in your application, release it to reclaim the memory resources it consumed.

A large application probably has a large number of preferences. Although you can use an NSTabView to associate closely related preferences into a single preference pane object, you may need to create multiple preference panes. Your application needs to provide a user interface for selecting the panes.

If you have a small number of preference panes, place their icons into a fixed-size view at the top of the window and place the preference panes’ views into the bottom of the window as each is selected. See the Mail application for an example.

If you have more preference panes than can fit into the width of your window, provide an additional “Show All” icon in the top–left corner. The icon should be the application icon to which the preferences are applied (not necessarily the preference application’s own icon). Selecting this icon presents a two-dimensional matrix of all the preference pane icons from which the user can select. Also provide a view to the right of the “Show All” icon into which users can drag their favorite preference panes. The user’s favorite preference panes should be stored as part of the preference application’s own user preferences. See the System Preferences application for an example.

[Next](Document%20Revision%20History.md)[Previous](Implementing%20a%20Simple%20Preference%20Pane.md)

