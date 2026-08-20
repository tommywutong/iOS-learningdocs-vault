---
title: Automator Programming Guide
apple_id: TP40001450
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: Automator
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/AutomatorConcepts/Articles/AutomatorPropRef.html
archived_at: '2026-07-15T05:16:26.127801Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Automator Programming Guide](Introduction%20to%20Automator%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Defining%20Your%20Own%20Data%20Types.md)

# Automator Action Property Reference

When you develop an action for Automator, one of the steps is specifying the properties of the action in its information property list (see [Specifying Action Properties](Developing%20an%20Action.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjrfuytamrsga3q)). Automator uses these properties for various purposes, among them determining the types of data the action can accept and produce, setting the initial parameters on the action’s user interface, and getting the action’s name, icon, associated application, and category. The following sections document the Automator properties and describe the UTI-based type identifiers that you use to specify the types of data an action provides and accepts.

You must specify some of the Automator properties described below in an action project’s information property list (`Info.plist`), and optionally may specify the others. The `Info.plist` file in the project template includes, with the exception of `AMRequiredResources`, the Automator properties (with comments for values).

__`AMAccepts`__: A dictionary that describes the data that the action will accept. This required property has three subproperties:

- `Container`—A string that specifies how multiple inputs are passed. Currently this should have the default value (`List`).
- `Optional`—A Boolean that indicates whether input is optional for this action. If your action can function properly without input, specify `<true/>`; if it requires input, specify `<false/>`. If this property is not specified, Automator assumes a default of `</false>`.
- `Types`—An array of type identifiers indicating the types of data that your action can accept as valid input.

Example:

```
<key>AMAccepts</key>
    <dict>
        <key>Container</key>
        <string>List</string>
        <key>Optional</key>
        <true/>
        <key>Types</key>
        <array>
            <string>com.apple.textedit.document-object</string>
            <string>public.text</string>
            <string>public.item</string>
        </array>
    </dict>
```

For information on valid type identifiers, including the use of `'*'` to signify that an action can accept any data type, refer to [Type Identifiers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjvfuytamjygazq). See also the corresponding property `AMProvides`.

__`AMApplication`__: A string that identifies the primary application that the action uses to do its work. For example, if your action controls the Finder application with AppleScript commands, you would specify “Finder” for this property. Automator uses this property as a filter and as a search criterion. Examples of possible values are Address Book, iCal, and Xcode.

Example:

```
<key>AMApplication</key>
<string>Finder</string>
```

__`AMCanShowSelectedItemsWhenRun`__: A Boolean that controls whether the action allows the presentation of selected parts of its user interface for the Show When Run feature. If this property is set to `<true/>` (the default), the parts of the action’s view (either automatically or manually generated) appear as items in the table view exposed under the Options button. If it is set to `<false/>`, only the “Show Action When Run” check box is presented (assuming that the `AMCanShowWhenRun` property is set to `<true/>`).

__`AMCanShowWhenRun`__: A Boolean that controls whether the Show When Run feature is enabled for the action. By default, it is set to `<true/>`, causing the Options button to be displayed in the lower-left corner of the action view. When the button is clicked, the view is extended to expose a “Show Action When Run” check box and, optionally, controls for selecting parts of the action view to present to work flow users (see the description of `AMCanShowSelectedItemsWhenRun`). Setting the `AMCanShowWhenRun` to `<false/>` removes the Options button from the action view.

__`AMCategory`__: A string (or array of strings) that Automator uses to group the action with similar actions in terms of their effects or the objects they operate on. Automator presents categories in its user interface and also uses an action’s category as a search criterion.

__Note:__ Automator does not show categories in its user interface in OS X version 10.4, though it does use them in searches.

In OS X v10.4, category names were simply strings (or arrays of strings), with values such as Find, Music, Pictures, System, Terminal, Text, and Utility. You could also specify names for new categories.

Example (OS X v10.4):

```
<key>AMCategory</key>
<string>Pictures</string>
```

Starting in OS X v10.5, category names represent codes (or arrays of codes), and you should use the code names shown in [Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjvfvjvomi).

Example (OS X v10.5):

```
<key>AMCategory</key>
<string>AMCategoryPhotos</string>
```

For actions brought forward from OS X v10.4, Automator will attempt to categorize the action appropriately. For example, an action with the category name of “Power Point” will be placed in the Presentations category (`AMCategoryPresentations`). An action with an unrecognized category name will be placed in the generic Other category.

If you rebuild an older action in OS X v10.5 without changing the category name value, it will still build and work, but you will get a warning from `amlint` that you are not using one of the predefined values.

An action compiled in OS X v10.5 will not work in v10.4 due to binary incompatibility.

__Table 1__  AMCategory code names available in OS X version 10.5

| Code name | Category |
| `AMCategoryCalendar` | Calendar |
| `AMCategoryChat` | Chat |
| `AMCategoryContacts` | Contacts |
| `AMCategoryDeveloper` | Developer |
| `AMCategoryDocuments` | Documents |
| `AMCategoryFilesAndFolders` | Files and folders |
| `AMCategoryFonts` | Fonts |
| `AMCategoryInternet` | Internet |
| `AMCategoryMail` | Mail |
| `AMCategoryMovies` | Movies |
| `AMCategoryMusic` | Music |
| `AMCategoryPDFs` | PDF files |
| `AMCategoryPhotos` | Photos |
| `AMCategoryPresentations` | Presentations |
| `AMCategorySystem` | System |
| `AMCategoryText` | Text |
| `AMCategoryUtilities` | Utilities |

__`AMDefaultParameters`__: A dictionary containing default values for the user-interface elements managed by Cocoa bindings. The keys are the names of the user-interface elements entered as attributes of the Parameters instance (NSObjectController) in Interface Builder. The values should be contained in elements identifying the type of data; boolean is used for check boxes, integer for pop-up item index, and string for text fields. This property is required for actions that have parameters.

Example:

```
<key>AMDefaultParameters</key>
<dict>
    <key>fromChoice</key>
    <integer>1</integer>
    <key>replaceExisting</key>
    <boolean>No</boolean>
    <key>toChoice</key>
    <integer>0</integer>
    <key>toDirectory</key>
    <string></string>
</dict>
```

__`AMDescription`__: A dictionary that specifies the content of an action description, which appears in the lower-left view of Automator when the action is selected. The description’s icon and title are derived from the `AMIconName` and `AMName` properties, respectively. The `AMDescription` dictionary has the following keys (the values for which are all strings):

- `AMDSummary`—A succinct description of what the action does. It appears directly under the action title. This text is required.
- `AMDInput`—The types of data the action accepts. If this subproperty is not specified, Automator uses default text corresponding to the type identifiers specified for `AMAccepts`. he subheading “Input:” precedes this text in the displayed description.
- `AMDResult`—The types of data the action provides. If this subproperty is not specified, Automator uses default text corresponding to the type identifiers specified for `AMProvides`. The subheading “Result:” precedes this text in the displayed description.
- `AMDOptions`—Describes what can be set in the action’s user interface. The subheading “Options:” precedes this text in the displayed description. Use this subproperty only for explaining aspects of the action’s user interface that aren’t readily apparent.
- `AMDAlert`—Points out a important possible consequence of the action, such as overwriting a file. The subheading “Alert:” precedes this text in the displayed description.
- `AMDNote`—Additional information that the user should know (but not as critical as an alert). The subheading “Note:” precedes this text in the displayed description.
- `AMDRequires`—Anything this action requires in order to work properly, such a web page displayed or a local printer connected. The subheading “Requires:” precedes this text in the displayed description.
- `AMDRelatedActions`—Specify the bundle IDs of actions that are especially related to this action. (You can look at the `Info.plist` file inside an action bundle to find out its bundle ID.) There can be at least three kinds of relationships among actions based on what function they perform:

  - Connected function: the actions are likely to be used in the same workflow, such as New Message and Send Outgoing Messages.
  - Parallel function: the actions perform the same general task, but in slightly different manners or using different applications, such as Send Mail Message and Send iChat Message.
  - Opposing function: one of the actions undoes an effect of the other one, such as Connect to Servers and Eject Disk.

Example:

```
<key>AMDescription</key>
    <dict>
        <key>AMDInput</key>
        <string>Project file from the previous action.</string>
        <key>AMDOptions</key>
        <string>Set, retrieve, increment, tag, submit, get
            marketing version, set marketing version. </string>
        <key>AMDResult</key>
        <string>Pass information to next action or to a log
            file.</string>
        <key>AMDSummary</key>
        <string>This action changes the version information of
            an Xcode project. It uses the agvtool shell tool, and
            allows you to set most all of the options of that
            tool.</string>
    </dict>
```

__`AMIconName`__: In OS X version 10.4, this is a string that specifies a file that contains the 16-by-16 pixel icon that Automator displays to the left of the action name in its user interface. The icon name string should not include the extension, but the file itself must have an extension of `.tiff`. It can refer to an icon file in Automator or to a custom icon file in the action bundle.

Example:

```
<key>AMIconName</key>
<string>MyApp</string>
```

Also in OS X v10.4, you can store in the action bundle a large (32-by-32 pixel) version of the same icon for Automator to display in the action description. This icon file should have a name of the form _Name_`Large.tiff`. In the property example above, this file would have a name such as `MyAppLarge.tiff`.

Starting in OS X v10.5, the icon name string can refer to an image file in any of the basic formats that Cocoa supports, such as Icon File, TIFF, JPEG, and PNG, with all the standard variations of filename extensions (`.icns`, `.tiff`, `.tif`, `.jpg`, `.jpeg`, and so on). As in the earlier version, you don't include the extension as part of the icon name. You can supply both a 16-by-16 and a 32-by-32 pixel icon in the same image file. For backward compatibility, the use of `.tiff` files is still supported, and you must supply icons in the previously described format for an action that needs to work in earlier versions of the OS.

__`AMKeywords`__: An array of strings that give Automator keywords for identifying the action in searches. Keywords are not shown in the Automator user interface but are used in searches. Note that Automator automatically uses words in the names of actions as keywords, so there is no reason to repeat them in this property. Examples keywords are Change, Folder, and Label.

Example:

```
<key>AMKeywords</key>
    <array>
        <string>Add</string>
        <string>Spotlight</string>
        <string>File</string>
    </array>
```

__`AMName`__: A string giving the name of the action to be displayed in the Automator user interface. This property is required. Example names are “Add Attachments to Front Message”, “Copy Files”, and “Profile Executable”.

Example:

```
<key>AMName</key>
<string>Copy Files</string>
```

See the guidelines for naming actions in [Design Guidelines for Actions](Design%20Guidelines%20for%20Actions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjqfvbecsseirfecqq).

__`AMProvides`__: A dictionary that describes the data that the action will generate as output. This required property has two subproperties:

- `Container`—A string that specifies how multiple outputs are passed. Currently this should have the default value (`List`).
- `Types`—An array of type identifiers indicating the types of data that your action can provide as valid input.

Example:

```
key>AMProvides</key>
    <dict>
        <key>Container</key>
        <string>List</string>
        <key>Types</key>
        <array>
            <string>public.item</string>
        </array>
    </dict>
```

For information on valid type identifiers, refer to [Type Identifiers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjvfuytamjygazq). See also the corresponding property `AMAccepts`.

__`AMRequiredResources`__: An array of dictionaries that describes the applications, files, or other resources that the action requires to work properly. If the specified resource is not available when the bundle is loaded, Automator warns the user. If the resource is not available when the action’s workflow executes, Automator asks the user locate the missing resource. If the user does not find the resource, the workflow stops executing. This property has four subproperties for each dictionary:

- `Display Name`—A string that identifies the name of the resource as displayed in Finder, for example “iPhoto”. Leave this value blank if the `Type` key is set to “file”.
- `Resource`—A string identifying the required resource. The format of the resource is indicated by the `Type` subproperty (see note below).
- `Type`—A string indicating the type of the resource identifier given as the value of `Resource`: “application”, “creator code”, or “file”.
- `Version`—A string specifying the minimum version of the resource required by the stage in _n_`.`_n_`.`_n_ format (for example, “4.0.1”).

__Note:__ The value for the `Resource` dictionary key depends on the value for `Type`. If the type is “application”, the resource is specified by the application’s bundle identifier; if the type is “creator code”, the resource is specified by a four-character creator code; if the type is “file”, the resource is specified by full file-system path.

Examples:

```
<key>AMRequiredResources</key>
    <array>
        <dict>
            <key>Display Name</key>
            <string>iTunes</string>
            <key>Resource</key>
            <string>com.apple.iTunes</string>
            <key>Type</key>
            <string>application</string>
            <key>Version</key>
            <string>4.6</string>
        </dict>

        <dict>
            <key>Display Name</key>
            <string></string>
            <key>Resource</key>
            <string>/usr/bin/otool</string>
            <key>Type</key>
            <string>file</string>
            <key>Version</key>
            <string>10.3.5</string>
        </dict>
    </array>
```

__`AMWarning`__: If the action can potentially lose data, specify in this dictionary a set of subproperties that cause Automator to display a warning when the action is added to a workflow. The information in the warning comes from the `AMWarning` subproperties. Optionally, this property can allow the user to insert another action before this one to protect against data loss. A common warning in Automator adds the Copy Files action before the current action. As a result, the action alters copies of files rather than the originals. This property is required but only the value for the `Level` key needs to be specified (and is set to a default of 0 in the project templates).

- `Action`—A string that specifies the bundle identifier of an action to be inserted (if the user agrees) in the workflow before this action. Leave this value blank if you just want to warn the user. If you do not specify a value for this key, the `ApplyButton` string is used for the button title but the `IgnoreButton` value is ignored.
- `ApplyButton`—A string that is the title for the button that adds the proposed action or, if no action is specified, that continues the workflow. Examples are “Add” and “Continue”.
- `IgnoreButton`—A string that is the title for the button for rejecting the proposed action or, if no action is specified, for canceling the workflow. Examples are “Don’t Add” and “Cancel”.
- `Level`—An integer that specifies the level of the warning:

  - 0: Safe operation (default)
  - 1: Makes reversible changes, for example Flip Images
  - 2: Makes irreversible changes, for example Crop Images

  This is the only required value of the `AMWarning` dictionary. If you specify level 1 or 2 you must also specify a `Message` string.
- `Message`—A string that is the warning presented to users in the sheet.

The following example shows an `AMWarning` property that simply warns the user without offering a prior action:

```
<key>AMWarning</key>
    <dict>
        <key>Action</key>
        <string></string>
        <key>ApplyButton</key>
        <string>Continue</string>
        <key>IgnoreButton</key>
        <string>Cancel</string>
        <key>Level</key>
        <integer>2</integer>
        <key>Message</key>
        <string>This action will update the connected iPod. It cannot be undone.</string>
```

In this example, the property proposes a prior action:

```
<key>AMWarning</key>
    <dict>
        <key>Action</key>
        <string>com.apple.Automator.CopyFiles</string>
        <key>ApplyButton</key>
        <string>Add</string>
        <key>IgnoreButton</key>
        <string>Don’t Add</string>
        <key>Level</key>
        <integer>2</integer>
        <key>Message</key>
        <string>This action will change the image files passed into it. Would you like to add a Copy Files action so that the originals are preserved?</string>
```


The Automator `AMAccepts` and `AMProvides` properties use type identifiers to specify the types of data for action inputs and outputs. Automator uses the text in the Description column in Table 2 and Table 4 in its user interface to designate the types of input data and output data for the actions in a workflow.

Automator actions can use public type identifiers in three categories. The first is specific to the technologies or applications of Apple. Table 2 lists the current identifiers in this category.

__Table 2__  Type identifiers internally defined by Apple

| Type Identifier | Description |
| `com.apple.applescript.object` | Object (in the AppleScript domain) |
| `com.apple.applescript.data-object` | Data |
| `com.apple.applescript.url-object` | URL |
| `com.apple.applescript.text-object` | Text |
| `com.apple.applescript.alias-object.pdf` | PDF files |
| `com.apple.applescript.alias-object.movie` | QuickTime movie files |
| `com.apple.applescript.alias-object.image` | Image files |
| `com.apple.applescript.alias-object` | Files/Folders |
| `com.apple.finder.file-or-folder-object` | Finder file or folder |
| `com.apple.idvd.menu-object` | iDVD menu |
| `com.apple.idvd.slideshow-object` | iDVD slideshow |
| `com.apple.iphoto.item-object` | iPhoto item |
| `com.apple.iphoto.album-object` | iPhoto album |
| `com.apple.iphoto.photo-object` | iPhoto photo |
| `com.apple.itunes.item-object` | iTunes item |
| `com.apple.itunes.source-object` | iTunes source |
| `com.apple.itunes.playlist-object` | iTunes playlist |
| `com.apple.itunes.track-object` | iTunes track (song) |
| `com.apple.safari.document-object` | Safari document |
| `com.apple.textedit.document-object` | TextEdit document |
| `com.apple.mail.item-object` | Mail item |
| `com.apple.mail.message-object` | Mail message |
| `com.apple.mail.mailbox-object` | Mail mailbox |
| `com.apple.mail.account-object` | Mail account |
| `com.apple.addressbook.item-object` | Address Book item |
| `com.apple.addressbook.group-object` | Address Book group |
| `com.apple.addressbook.person-object` | Address Book person |
| `com.apple.ical.item-object` | iCal item |
| `com.apple.ical.event-object` | iCal event |
| `com.apple.ical.calendar-object` | iCal calendar |
| `com.apple.ical.todo-object` | iCal to do |

A special subset of the type identifiers defined by Apple are those reserved for Objective-C actions, which are described in Table 3.

__Table 3__  Objective-C type identifiers

| Type identifier | Description | Comments |
| `com.apple.cocoa.path` | File | An NSString object representing a POSIX-style path. |
| `com.apple.cocoa.url` | URL | An NSURL object representing a URL |
| `com.apple.cocoa.string` | Text | An NSString object. |

The final category of type identifier includes externally defined UTIs. Table 4 lists these public identifiers.

__Table 4__  Externally defined type identifiers

| Type identifier | Comments |
| `public.data` | Data |
| `public.url` | URL |
| `public.text` | Text |
| `public.image` | Image file |
| `public.item` | File/Folder |
| `com.apple.quicktime-movie` | QuickTime movie |

You can convert between type identifiers—and most importantly between externally and internally defined identifiers—using a special kind of action called a conversion action. See [Creating a Conversion Action](Creating%20a%20Conversion%20Action.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjufvbeeq2kivauqsi) for details.

[Next](Document%20Revision%20History.md)[Previous](Defining%20Your%20Own%20Data%20Types.md)

