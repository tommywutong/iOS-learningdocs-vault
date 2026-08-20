---
title: Preference Pane Programming Guide
apple_id: 10000110i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PreferencePanes/Tasks/HelpMenu.html
archived_at: '2026-07-18T02:12:30.983912Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Preference Pane Programming Guide](Introduction.md)


[Next](Creating%20a%20Preference%20Pane%20Bundle.md)[Previous](Communicating%20With%20the%20Target%20Application.md)

# Implementing a Preference Pane Help Menu

This section takes you through the steps to add context-sensitive Help menu entries for a preference pane. You can implement Help Viewer anchors in two different ways, both which can provide your user with specific assistance accessible from their Help menu. If you have already created a skeletal preference pane as described in [Creating a Preference Pane Bundle](Creating%20a%20Preference%20Pane%20Bundle.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydslkcifbemq2bijfa), you can use it here. Or, you can create a fresh preference pane and refer to the following instructions where appropriate.

One method of offering help to your preference pane user is by adding help menu items that become available whenever your preference pane is loaded. Upon selection of your preference pane, the System Preferences application will automatically add the Help menu items as described by a static array in the pane’s `Info.plist` file. Once the preference pane is deselected, the System Preferences application will remove them from the menu.

First, you need to create some help material, unless you are linking to existing material on the system. If you are not familiar with creating content for the Mac OS X Help Viewer, refer to _[Apple Help Programming Guide](../../Carbon/Apple%20Help%20Programming%20Guide/Introduction%20to%20Apple%20Help%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbt)_.

Second, you need to add entries to the array values of the `NSPrefPaneHelpAnchors` key in your `Info.plist` file. You will statically define each anchor with an associated title. The title represents the string value of the menu item which will display the help book specified by the anchor. For example, if you wanted to add a “Sample Help” item in the Help menu for your preference pane, which will open a book marked by the `SMPL001` anchor, add this to your `Info.plist` file:

__Listing 1__  Info.plst entry for the SMPL001 Help menu item

```
<key>NSPrefPaneHelpAnchors</key>
<array>
    <dict>
        <key>title</key>
        <string>Sample Help</string>
        <key>anchor</key>
        <string>SMPL001</string>
    </dict>
</array>
```

Once the preference pane is loaded by the System Preferences application, a new menu item in the Help menu called “Sample Help” will appear. When selected, it will load the Help book specified by the `SMPL001` anchor.

You can also localize the Help menu item for your preference pane. In the example above, you would replace the “Sample Help” string with some internal string, such as `SAMPLE_PREFPANE_MENU_TITLE`. Then in the Localizable.strings file for all your languages, you would add the appropriate entry to override this internal string:

__Listing 2__  English Localizable.strings entry for the SMPL001 Help menu item

```
"SAMPLE_PREFPANE_MENU_TITLE" = "Sample Help";
```


__Listing 3__  French Localizable.strings entry for the SMPL001 Help menu item

```
"SAMPLE_PREFPANE_MENU_TITLE" = "Aide Sample";
```


Often, you want the items in your preference pane’s Help menu to show or hide based off context—for example, if you have multiple subpanes in your preference pane’s main view, you may want to add a Help menu item for one subpane, and hide the menu items for the others.

You can accomplish this with the method `updateHelpMenuWithArray:`. This method, implemented in the PreferencePanes framework, is called with one argument, an array of dictionaries corresponding to the same format as the array and dictionaries in [Adding Global Help Menu Items](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi2tcljrgiytknjr). Instead of adding the items statically in the `Info.plist` file, you create dynamic NSArray and NSDictionary objects and pass those into this method, which will update the Help menu accordingly.

The code in Listing 4 shows you how to construct a help menu that changes its menu item title based off the identifier of the selected tab.

__Listing 4__  Dynamic help menu for a tab view

```objc
- (void)tabView:(NSTabView *)tabView didSelectTabViewItem:(NSTabViewItem  *)tabViewItem
{
    NSDictionary *dictionary = [NSDictionary dictionaryWithObjectsAndKeys:
        [tabViewItem identifier], @"title",
        @"SMPL001", @"anchor",
        NULL];

    NSArray *array = [NSArray arrayWithObject:dictionary];

    [self updateHelpMenuWithArray:array];
}
```

Note that the title string used in this method call is not localizable with the Localizable.strings file. If you want to localize the title of the help menu item, you must do so programatically or using identifiers from the language-specific nib file, demonstrated in the example above.

[Next](Creating%20a%20Preference%20Pane%20Bundle.md)[Previous](Communicating%20With%20the%20Target%20Application.md)

