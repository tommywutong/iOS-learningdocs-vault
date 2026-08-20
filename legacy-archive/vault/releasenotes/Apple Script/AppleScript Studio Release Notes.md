---
title: AppleScript Studio Release Notes
apple_id: TP40000984
resource_type: Release Note
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/releasenotes/AppleScript/RN-AppleScriptStudio/index.html
archived_at: '2026-07-18T02:50:21.216832Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# AppleScript Studio 1.5 Release Notes

> [!IMPORTANT]
> 

This release note provides the latest information about AppleScript Studio 1.5, which ships with Mac OS X version 10.5, as well as a list of the more prominent bug fixes. Note that there was no new terminology added to AppleScript Studio 1.5. For older release notes, see _[AppleScript Studio 1.4 Release Notes](../Scripting%20Automation/AppleScript%20Studio%201.4%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmbw)_.

#### Contents:

- [New Version Number](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobufvcg63tujruw422fnrsw2zlooreuixzr)
- [Tiger AppleScript Xcode Plug-ins Must be Updated for Leopard](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobufvcg63tujruw422fnrsw2zlooreuixzs)
- [Bug Fixes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobufvcg63tujruw422fnrsw2zlooreuixzt)
- [Known Bugs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobufvcg63tujruw422fnrsw2zlooreuixzu)
- [AppleScript Studio Version 1.4 Release Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobufvjvomi)

### New Version Number

AppleScript Studio has the version number 1.5 in Mac OS X version 10.5 (Leopard). For information about the version number and how to check for it, see the section “Version Information” in Terminology Fundamentals in _AppleScript Studio Terminology Reference_.

### Tiger AppleScript Xcode Plug-ins Must be Updated for Leopard

Existing Tiger AppleScript Xcode plug-ins will not work in Leopard. To work around this problem, you can recreate your plug-in using the Leopard based "AppleScript Xcode Plugin" template. As part of rebuilding the plug-in you will have to attach your plug-in’s event handlers in Interface Builder.

Or, you can do the following to your Tiger "AppleScript Xcode Plugin" project:

1. Change your project product installation path to: `/Developer/Library/Xcode/Plug-ins`. (The Tiger installation path is `/Library/Application Support/Apple/Developer Tools/Plug-ins/`, which will no longer work in Leopard.)
2. Add a key `XCGCReady` with the string value `"YES"` to your project's `Info.plist`.
3. Enable the `GC` (Garbage Collection) build setting.
4. In Interface Builder, re-attach your event handlers to your project scripts.

### Bug Fixes

- Disabling the "Release when closed" `NSWindow` attribute in IB is not honored in Tiger. [4097479]

  In Mac OS X v10.4.0 through v10.4.6, the "Release when closed” `NSWindow` attribute in Interface Builder is not honored. The window object is always released regardless of how this attribute is set. This is fixed in versions of Tiger after v10.4.6, and in Leopard.
- Applescript Studio `outline view` does not respond to Data View events. [5232287]

  This bug has not been fixed, but _AppleScript Studio Terminology Reference_ has been modified to note that an `outline view` object does not respond to events from the Data View suite, such as `column clicked`, `column moved`, and `selection changed`. This limits the tasks you can accomplish with an `outline view` object.
- Memory leak associated with `set script` in AppleScript Studio. [4667798]

  Calling `set script` to set the `script` property of a `menu item` object (or of an object of any class that inherits the `script` property from the `item` class) resulted in a memory leak. This has been fixed.
- Mail Search doesn't show any local mailboxes. [4102626]

  The Mail Search sample application did not show local mailboxes—this has been fixed.
- TableView -- drag of row to same position removes row. [4589247]

  Dragging a row in a table view and dropping it slightly above its current position could result in the row being deleted. This has been fixed.
- The `isSeparatorItem` property of a `menu item` is not marked as read only. [5329608]

  This bug has been fixed, and _AppleScript Studio Terminology Reference_ has been modified to note that the `separator item` property of `menu item` is read only.

### Known Bugs

`path for resource` doesn't work for files without an extension. [3464005]

The following statement will work to find the path to `Contents/Resources/foo.sh`:

```
     set myPath to path for resource "foo" extension "sh"
```

But if the resource does not have an extension, the following statement results in an error, "The variable myPath is not defined (-2753)"

```
     set myPath to path for resource "foo"
```

Therefore, if you must access a resource with `path for resource`, give the resource an extension.

### AppleScript Studio Version 1.4 Release Notes

Previous release notes are available here: _[AppleScript Studio 1.4 Release Notes](../Scripting%20Automation/AppleScript%20Studio%201.4%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmbw)_.
