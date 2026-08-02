---
title: AppleScript Studio 1.4 Release Notes
apple_id: TP40004606
resource_type: Release Note
platform: macOS
topic: null
technology: null
published: '2007-12-22'
source_url: https://developer.apple.com/library/archive/releasenotes/ScriptingAutomation/RN-AppleScriptStudioOlder/index.html
archived_at: '2026-07-18T02:59:02.304024Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# AppleScript Studio 1.4 Release Notes

> [!IMPORTANT]
> 

This release note provides late-breaking information about enhancements to AppleScript Studio 1.4 (available in Tiger), as well as a list of the more prominent bug fixes.

See notes on "Release when closed” below for information on a bug fix that became available in Mac OS X version 10.4.7.

#### Contents:

- [New Features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmbwfvjvomi)
- [Bug Fixes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmbwfvjvomq)
- [Documentation Bug Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmbwfvjvomy)
- [Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmbwfvjvona)

### New Features

- Data View Improvements

  - The content property now supports both setting and getting data for table and outline views. The format of the data is very flexible. You can set the content as a list of strings, a list of lists, or a list of records. The `table view`, `outline view`, `data source`, `data row`, `data item`, and `data cell` classes all have a content property.

    Here are some examples of setting the content of a table view:

```
set tableView to table view 1 of scroll view 1 of window 1
set content of tableView to {"One", "Two", "Three"} -- This will create three data rows in the first column.
set content of tableView to {{"Red", "Green", "Blue"}, {"Black", "White", "Gray"}} -- This will create two data rows (given a table view with three columns), using columns based on index. This would produce a table view with two rows and three columns.
set content of tableView to {{|name|: "John Smith", |phone|:"222-555-3456"}, {|name|: "Paul Jones", |phone|:"123-456-7890"}} -- This will create two data rows, and it will use the columns with the specified names, compared to columns based on index.
```

    Notice that it isn't necessary to create the data source, data columns or data rows. If the table view doesn't have the necessary data items, it will create them automatically. In this example, a data source, two data columns (named "name" and "phone"), and two data rows are created automatically.

    The following is an example of setting the content of an outline view that contains two data columns: `task` and `completed`:

```
set content of outlineView to {{completed:false, task:"Things to do", |items|:{{completed:true, task:"Work on outline example", |items|:{{completed:true, task:"Make it plain and simple"}, {completed:true, task:"Put it all in an \"on launched'\" event handler"}}}, {completed:true, task:"Put it in my iDisk when done"}}}} 
```

    To designate child items you add an |items| entry in the record that contains its own list of lists or list of records:

```
Put it in my iDisk when done
```
  - You can get data from a data source as either a list of lists or a list of records. The `data source` class has a new boolean property `returns records` that you can set to true to return records when using the `content` property, `false` to return lists. The default setting for this property is true.

    The following are some examples of how to get the content of data views:

```
set tableView to table view 1 of scroll view 1 of window 1
get content of tableView
```

    Returns: `{{completed:"Yes", task:"Work on outline example"}, {completed:"Yes", task:"Make it plain and simple"}, {completed:"Yes", task:"Put it all in an \"on launched\" event handler"}, {completed:"Yes", task:"Put it in my iDisk when done"}}`

```
set returns records of data source of tableView to false
get content of tableView
```

    Returns: `{{"Work on outline example", "Yes"}, {"Make it plain and simple", "Yes"}, {"Put it all in an \"on launched\" event handler", "Yes"}, {"Put it in my iDisk when done", "Yes"}}`

    Here are some examples using an outline view:

```
set outlineView to outline view 1 of scroll view 1 of window 1
get content of outlineView
```

    Returns: `{{completed:"--", task:"Things to do", |items|:{{completed:"Yes", task:"Work on outline example", |items|:{{completed:"Yes", task:"Make it plain and simple"}, {completed:"Yes", task:"Put it all in an \"on launched'\" event handler"}}}, {completed:"Yes", task:"Put it in my iDisk when done"}}}}`

```
set returns records of data source of tableView to false
```

    Returns: `{{"Things to do", "--", {"Work on outline example", "Yes", {"Make it plain and simple", "Yes"}, {"Put it all in an \"on launched'\" event handler", "Yes"}}, {"Put it in my iDisk when done", "Yes"}}}`
  - The `append` command now supports outline views. It uses the same data formats as the `content` property. You can append a list of strings to a table view, or a list of lists or a list of records.
  - You can now use event handlers and a data source for the same data view. In previous versions of AppleScript Studio, table views could either be scripted by using a data source or by using various event handlers. If you used the event handlers, you couldn't use the data source. In this release, you can mix and match data sources and specific event handlers. This provides the best balance of performance and flexibility.

    There are several new event handlers that provide access to important events in a data view:

    - `cell value changed` -- Called when the user edits a cell in a table or outline view.
    - `item value changed` -- Called when the user edits a cell in an outline view.
    - `items changed` -- Called when the number of items in an outline view has changed.
    - `rows changed` -- Called when the number of rows in a table or outline view has changed.

    With these new event handlers, you can use a data source to populate your table view and use the cell `value changed` event handler to inspect or override the value a user types into a cell.
  - Table view columns now support sort indicators. You can turn them on or off by using the `use sort indicators` boolean property of the `table view` class. This only controls the presence of sort indicators. You will still have to detect the click in a table column and change the sort order.

    The Simple Table and Simple Outline examples demonstrate some of the new data view features.
- Drag and Drop Improvements

  - A new property, `allows reordering`, supports automatic reordering of items in data views. Setting `allows reordering` to `true` on a table view allows the user to drag rows up and down within the table view, in effect changing the order. Note, if the data source is sorted, then `allows reordering` is ignored.

    The Outline Reorder and Table Reorder examples demonstrate how to use this feature.
  - You can drag and drop rows or items within a data view. In addition to the automatic support provided by `allows reordering`, you can allow drag and drop of external items into data views, with the additional ability to specify where in the table or outline view to drop items. In order to provide this support there are several new event handlers:

    - `on prepare table drag` -- Called when a drag is about to start in a table view.
    - `on prepare table drop` -- Called while a drop is happening in a table view.
    - `on accept table drop` -- Called when the drop has happened in a table view.
    - `on prepare outline drag` -- Called when a drag is about to start in an outline view.
    - `on prepare outline drop` -- Called while a drop is happening in an outline view.
    - `on accept outline drop` -- Called when the drop has happened in an outline view.

    The Simple Table and Simple Outline examples demonstrate how to use these event handlers.
- New Toolbar Support

  - You can now easily create toolbars in your application. Two new classes have been added: `toolbar` and `toolbar item`. Toolbars can be created and added to a window. To support this, the `window` class has a new `toolbar` property. The toolbar uses string identifiers to identify the toolbar as well as the toolbar items.

    The following example creates a toolbar and attaches it to a window:

```
-- Make the new toolbar, giving it a unique identifier
set documentToolbar to make new toolbar at end with properties {name:"document toolbar", identifier:"document toolbar identifier", allows customization:true, auto sizes cells:true, display mode:default display mode, size mode:default size mode}

-- Set up the allowed and default identifiers.
set allowed identifiers of documentToolbar to {"compile item identifier", "run item identifier", "stop item identifier", "print item identifier", "customize toolbar item identifier", "flexible space item identifier", "space item identifier", "separator item identifier"}
set default identifiers of documentToolbar to {"compile item identifier", "run item identifier", "stop item identifier"}

-- Create the toolbar items, adding them to the toolbar.
make new toolbar item at end of toolbar items of documentToolbar with properties {identifier:"compile item identifier", name:"compile item", label:"Compile", palette label:"Compile", tool tip:"Compile", image name:"CompileScript"}
make new toolbar item at end of toolbar items of documentToolbar with properties {identifier:"run item identifier", name:"run item", label:"Run", palette label:"Run", tool tip:"Run", image name:"RunScript"}
make new toolbar item at end of toolbar items of documentToolbar with properties {identifier:"stop item identifier", name:"stop item", label:"Stop", palette label:"Stop", tool tip:"Stop", image name:"StopScript"}

-- Assign our toolbar to the window
set toolbar of window 1 to documentToolbar
```
  - There are two new event handlers (that can be attached to a window) to provide toolbar support:

    - `on clicked toolbar item` -- Called when the user clicks on a toolbar item.
    - `on update toolbar item` -- Called by the toolbar to update the state of a toolbar item. You must return `true` or `false` to specify the enabled state of the toolbar item: `true` for enabled, `false` for disabled.

    The Simple Toolbar example demonstrates how to use the new toolbar feature.
- New Coordinate System Support

  - In previous versions of AppleScript Studio, all coordinates for windows and views were returned in a list of four numbers, {left, bottom, right, top}. The origin of a window or bounds was in the bottom left corner. Unfortunately this isn't the standard used by AppleScript. It uses a list of four numbers, {left, top, right, bottom} with the top left of the window as the origin. To have a backwards compatible way of providing the proper AppleScript manner of specifying bounds, the application class now has a new enumerated property, `coordinate system`.

    The following are the possible values:

    - `AppleScript coordinate system` -- Defines bounds as {left, top, right, bottom} with the origin in the top left.
    - `classic coordinate system` -- Defines bounds as {left, bottom, right, top} with the origin in the bottom left.
    - `Cocoa coordinate system` -- Defines bounds as {x, y, width, height} with the origin in the bottom left.

    The default coordinate system for this release is the `classic coordinate system`. This is the same system that is used in all previous releases.

    In addition to specifying the coordinate system in a script, you can add the following entry to your application's `Info.plist`:

```
<key>ASKCoordinateSystem</key>
<string>ASKClassicCoordinateSystem</string>
```

    The possible values are `ASKClassicCoordinateSystem`, `ASKAppleScriptCoordinateSystem`, and `ASKCocoaCoordinateSystem`. When the bounds are accessed and no coordinate system has been specified, Studio will look for the ASKCoordinateSystem entry in the main bundle's `Info.plist` and will use the specified value.

    The Coordinate System example demonstrates this feature.
- New Target/Action Support

  - There are new `target` and `action` method properties in key classes that allow you to dynamically change the target or script to be executed during runtime. The following classes each have the `target` and `action` method properties: `cell`, `control`, `menu item`, and `toolbar item`.

    You can dynamically change the target of an action in your application or change the Cocoa method that is executed when the action is triggered. For instance, you could set the target and action of a toolbar item as in the following example:

```
set toolbarItem to toolbar item 1 of toolbar of window 1
set target of toolbarItem to view "webview" of scroll view 1 of window 1
set action method of toolbarItem to "stopLoading:"
```

    Then when you click on the toolbar item, it sends the Cocoa method `stopLoading:` to the target, which in this case is a web view.
- Xcode Improvements

  - Studio projects can now be built using Xcode's new native target support. The older jam-based targets are still supported. All of the examples and templates for Studio have been upgraded to native targets. You can also upgrade your existing projects to use native targets. See the Xcode documentation to learn more about native targets.
  - The code assistant has been improved in this release. Variables and identifiers in the script you are editing are now included in the completion UI in addition to all of the standard terminology available in previous releases. See the release notes for Xcode 2.0 that describes the many UI enhancements made to the code assistant.
  - It is now possible to edit and save compiled scripts from within Xcode. In addition to the support for text scripts (.`applescript` files), you can now also use compiled scripts (`.scpt` files) to build your Studio applications. There are two AppleScript file types, AppleScript Script File (compiled script) and AppleScript Text File (source script). See the notes section on how to enable this support.
  - Xcode has a new dictionary viewer that is based on the new dictionary viewer in Script Editor. It uses the sdef format as its native file format. See the notes section about how to add a reference to `AppleScriptKit.sdef` to your existing projects.
- Interface Builder Improvements

  - Scripts can now be designated to have global, per nib, or per object scope. When attaching scripts and event handlers to objects in the AppleScript inspector in Interface Builder, you can choose the scope of the script using the new Scope popup button in the inspector. When the nib is loaded in your project, the scope will determine how the script is attached. If you designate a script as global, then there will be only one instance of the named script while your application is running. If you choose per nib, every time the nib is loaded a new instance of the script is attached to the specified objects in that nib. If the scope is set to per object, then every designated object gets a new instance of the script.

    This provides a more object oriented approach to structuring your application. For instance, in a document based application you could have a `Document.applescript` file, and when you attach any scripts to the objects in your `Document.nib`, specify the scope of the scripts in the nib to be per nib. Then every time a new document is created you get a new instance of the Document script. In doing this you can have properties or globals defined in the script that are specific to that instance of the document. In previous versions, any properties or globals defined in a script would be shared by every document.

    The new script scopes only work on Mac OS X 10.4 Tiger or later. Therefore, if you want to select per nib or per object scope for a script, you must switch your nib's Oldest Target setting to Mac OS X Version 10.4.
  - There are four new event handlers for Automator action views: `activated`, `opened`, `parameters updated`, and `update parameters`. These event handlers are only called when attached to a view object of an Automator action. See the Automator developer documentation to find out more about how to develop actions for Automator.

### Bug Fixes

- <rdar://problem/3507378> Using the 'on open' event handler can lead to a crash. This problem was manifested if the return value from an open event handler was `false` or 0. The work around was to return true at the end of your open event handler. Studio no longer expects or looks at a return result from this event handler.
- <rdar://problem/3692092> Upgrade Studio templates to use native build system.
- <rdar://problem/3591378> Users need access to the sorted data rows of a data source.You can access the data rows of a data source in their sorted order by using the new `sorted data rows` property of the `data source` class.
- <rdar://problem/3813515> We should upgrade all of the shipping AppleScript Studio Example projects to be native targets. All of the existing Studio examples have been upgraded to use native targets.
- <rdar://problem/3762923> Add an additional (optional) parameter named `in bundle with identifier` to the `localized string` command. You can specify a bundle by identifier to find the specified strings table.

### Documentation Bug Notes

- The documentation for the `localized string` command in _AppleScript Studio Terminology Reference_ contains an error. The name for the `default localized strings` file should be Localizable.strings (not `localized.strings`). Creating a strings file with the wrong name will cause the `localized string` command to fail.

### Notes

- To turn on the functionality in Xcode for editing compiled scripts (.scpt), you will need to add a user default setting, as the support is preliminary and there isn't a switch in the Xcode UI to turn it on. To enable the editing of compiled scripts, execute the following in Terminal:

```
defaults write com.apple.Xcode ASKAllowEditingOfCompiledScripts YES
```

  To disable it, do the following in Terminal:

```
defaults delete com.apple.Xcode ASKAllowEditingOfCompiledScripts
```

  There are several side effects to using compiled scripts for your projects. The first is that cvs cannot diff a compiled script (as it is considered a binary file), so using those tools will be limited if you are using source control. Also, searches across your project will now open and search compiled scripts, and any applications referenced in a tell block in your compiled scripts will be launched.
- The content of the main.m file has changed in this release. It is now:

```
extern void ASKInitialize();
extern int NSApplicationMain(int argc, const char *argv[]);

int main(int argc, const char *argv[])
{
ASKInitialize();

return NSApplicationMain(argc, argv);
}
```

  This change means that the application will only run on a Jaguar (10.2) or later system. It will fail if you attempt to launch it on any earlier system. If you need to have your application run on pre-Jaguar systems, you will need to replace the contents of main.m with the following:

```objc
#import <mach-o/dyld.h>

extern int NSApplicationMain(int argc, const char *argv[]);

int main(int argc, const char *argv[])
{
if (NSIsSymbolNameDefined("_ASKInitialize"))
{
NSSymbol symbol = NSLookupAndBindSymbol("_ASKInitialize");
if (symbol)
{
void (*initializeASKFunc)(void) = NSAddressOfSymbol(symbol);
if (initializeASKFunc)
{
initializeASKFunc();
}
}
}

return NSApplicationMain(argc, argv);
}
```

  You may notice that there is a small difference in this code from that in prior releases. Instead of using NSSymbol \*symbol, which was not correct, this version contains the correct version for you to use.

  Before the Jaguar release of Studio, `main.m` files contained the following:

```
extern int NSApplicationMain(int argc, const char *argv[]);

int main(int argc, const char *argv[])
{
return NSApplicationMain(argc, argv);
}
```

  If your project is still using a main.m that looks like this, you will not be able to use any of the new features added to Studio from Jaguar on. Please replace your main.m with the contents of either of the two versions shown, based on the minimum system version you need.
- In Tiger v10.4.0 through v10.4.6, the "Release when closed” NSWindow attribute in Interface Builder is not honored. The window object is always released regardless of how this attribute is set.

  The workaround (which is not needed starting in Mac OS X version 10.4.7) is to not close the window, but instead to hide it if you want to keep it around. You can do this by adding an `on should close` handler to your application as shown in the following example:

```
on choose menu item theObject
   show window "Main"
end choose menu item

on should close theObject
    hide window "Main"
    return false
end should close
```
- The `.asdictionary` format is not supported by the new dictionary viewer, as the new dictionary viewer's native file format is sdef. All of the examples and palettes in this release of Studio contain a reference to `AppleScriptKit.sdef`. Clicking on this reference will open a dictionary viewer showing Studio's terminology. In your existing projects, you will need to remove the existing `AppleScriptKit.asdictionary`, making sure to only remove the reference, not the file, and then add a reference to the AppleScriptKit.sdef. To add the reference, choose the "Add to Project:…" menu item from the Project menu, navigate to `/System/Library/Frameworks/AppleScriptKit.framework/Resources`, choose the `AppleScriptKit.sdef` file, and then click the "Add" button. When the sheet appears to ask which target to add the file to, make sure none of the targets is checked. This will add the file as a reference and ensure that it is not included as part of your application when it is built.
- AppleScript text files newly created in Mac OS X 10.4 or in projects created on Mac OS X 10.3.x or earlier may have the wrong encoding, which may cause file saving to fail or cause the script to compile incorrectly. AppleScript text files should be saved in the default system encoding, commonly "Western (Mac OS Roman)" or "Japanese (Mac OS)". You can change the file's encoding via the Format > File Encoding menu, or via an Inspector.
- There are new examples that demonstrate the new features in this release:

  - Coordinate System - Demonstrates the new coordinate system support.
  - Outline Reorder - Demonstrates how to set the contents of an outline using a single list of records, as well as dynamically turning on or off the automatic reordering support.
  - Simple Outline - Updated to demonstrate the new drag and drop support for data views. Also demonstrates the new change cell value event handler.
  - Simple Table - Demonstrates how to set the contents of a table view using a list of lists of strings, as well as how to use the new drag and drop event handlers for data views.
  - Simple Toolbar - Demonstrates how to create a toolbar in a window and populate it with toolbar items.
  - Table Reorder - Demonstrates how to populate a table view using a list of records, as well as using the automatic reordering support.
