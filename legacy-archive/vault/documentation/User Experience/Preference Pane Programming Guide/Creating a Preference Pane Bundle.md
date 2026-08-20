---
title: Preference Pane Programming Guide
apple_id: 10000110i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PreferencePanes/Tasks/Creation.html
archived_at: '2026-07-18T02:12:30.424061Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Preference Pane Programming Guide](Introduction.md)


[Next](Implementing%20a%20Simple%20Preference%20Pane.md)[Previous](Implementing%20a%20Preference%20Pane%20Help%20Menu.md)

# Creating a Preference Pane Bundle

This section takes you through the steps to create and install a preference pane bundle for use by System Preferences. You need to perform these actions for every preference pane you create. It is assumed that you are already familiar with Xcode and Interface Builder. For help using these development tools, see the Currency Converter tutorial for Cocoa.

This section describes how to create the preference pane project and add the Preference Panes framework.

1. Start Xcode.
2. Choose New Project from the File menu.
3. Select the Cocoa Bundle project type and create the project.
4. Choose Add Frameworks from the Project menu. If the selection is not already there, go to the `/System/Library/Frameworks` directory. Select `PreferencePanes.framework`.

This section describes how to create a simple preference pane nib file and add it to the preference pane project.

1. While Xcode is still running with your project open, start Interface Builder.
2. Create an empty Cocoa nib.
3. Create a window and resize it to a suitable size. For System Preferences, the window should not be more than 595 pixels wide. As the window itself is not used by the preference pane, only its contents, you do not need to specify a window title nor localize the title.
4. Build the user interface in the window.
5. Return to Xcode and locate the `NSPreferencePane.h` header file in `PreferencePanes.framework`. Drag the header file to the nib’s main window in Interface Builder.
6. In the Classes pane, select the NSPreferencePane class and create a subclass of it. Rename it to whatever you want. This is a global property within the preference application, so include a unique prefix in the name as described in [Preventing Name Conflicts](Preventing%20Name%20Conflicts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydmlkciffesqkhizca).
7. With the subclass selected, go to the Attributes pane of the Info window. Create any outlets or actions you need for the user interface.
8. In the Instances pane, select the File’s Owner object. In the Custom Class pane of the Info window, select your preference pane class.
9. Draw a connection (Control-drag) between the File’s Owner object and the window object. Connect the window to the `_window` outlet.
10. Connect the remaining outlets and actions needed for the user interface.
11. Save the nib file into the `English.lproj` directory of your project. When asked whether to add it to the project, click the Add button.

This section describes how to create the initial source files and to insert the preference pane’s icon into the project.

1. In Interface Builder, with the nib file open, click the Classes tab and select your preference pane subclass.
2. Choose Create Files from the Classes menu. Save the files in your project folder and make sure the “Insert into targets” checkbox is checked.
3. In Xcode, edit the header file of your preference pane subclass. After the line importing `Cocoa.h`, add the line

```objc
#import <PreferencePanes/NSPreferencePane.h>
```
4. Add your preference pane icon to the project’s Resources folder.

This section describes how to modify the default project settings to produce a custom preference pane bundle. This mostly involves assigning values to the necessary keys in the bundle’s information property list.

1. Choose Edit Active Target from the Project menu and go to the Bundle Settings pane.
2. Change the “Identifier” field to an appropriate unique value for the `CFBundleIdentifier` key. The value should be prefixed by the reverse domain name of your organization (see [Preventing Name Conflicts](Preventing%20Name%20Conflicts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydmlkciffesqkhizca)).
3. Change the “Principal class” field in the Cocoa-specific section to the name of your preference pane subclass. This is the `NSPrincipalClass` key.
4. Change the “Main nib file” field to the name of your nib file. Do not include the `.nib` extension. This is the `NSMainNibFile` key.
5. Enter Expert mode by clicking the Expert button at the top of the Bundle Settings window. Create a new key by clicking the New Sibling button. Rename the new key `NSPrefPaneIconFile` and set its value to the name of your icon file.
6. Go to the Build Settings pane, scroll to the bottom of the window, and change the `WRAPPER_EXTENSION` entry value to `prefPane`.
7. Select the `InfoPlist.strings` file in the project’s Resources folder. Update the `CFBundleName` value if it should be different from the project name. Alternatively, you can add an entry for `NSPrefPaneIconLabel`, if you need to split the name between two lines.

This section describes how to make the preference pane available to System Preferences.

1. Build the project.
2. In Finder, locate the `build` directory for the project. The default location is inside the project folder. The preference pane is in this folder.
3. Move the preference pane into one of the `PreferencePanes` family of folders listed in [Where Preference Panes Live](Anatomy%20of%20a%20Preference%20Pane%20Bundle.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydkljzg4ydoma). For testing, use the `PreferencePanes` folder in `~/Library`. You may need to create the `PreferencePanes` folder.

When you run System Preferences you should now see your preference pane at the bottom of the window in the “Other” category.

[Next](Implementing%20a%20Simple%20Preference%20Pane.md)[Previous](Implementing%20a%20Preference%20Pane%20Help%20Menu.md)

