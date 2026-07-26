---
title: 'Hidden Xcode build, debug and template settings | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/06/hidden-xcode-build-debug-and-template.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:9c3ed1dc77e5abf8'
translated: false
---

> 原文：[Hidden Xcode build, debug and template settings | Cocoa with Love](https://www.cocoawithlove.com/2008/06/hidden-xcode-build-debug-and-template.html)　·　Cocoa with Love (Matt Gallagher)

This is a collection of the most useful hidden and hard-to-find settings in Xcode related to building, debugging and file templates.

This post is about hard-to-find settings in Xcode that most programmers can't live without. I felt strange writing a post on this topic since most of this information is documented elsewhere. But I still find myself forgetting and needing to rediscover these tidbits (even though I've been using ProjectBuilder/Xcode for 7 years and should remember), so I think that it's probably information worth reinforcing.

I'll cover:

- [Custom compiler flags for GCC](#compilersettings)
- [Pre and post build scripts](#buildscripts)
- [Changing the name of the built program](#buildname)
- [Replacing the annoying "__MyCompanyName__" placeholder in file templates](#mycompanyname)
- [Completely customizing the file templates](#filetemplates)
- [Customizing, altering and adding autocomplete "Text Macros"](#textmacros)
- [Configuring environment variables and executable arguments for Debugging](#environmentvariables)

## Custom compiler settings

The default compiler settings in Xcode projects are pretty good. Even so, it's a programmer's mission to play with everything and playing with the compiler settings is at the heart of a programming project.

Custom compile settings are buried pretty deep in Xcode. To access the custom compiler settings, you must:

1. Have a project window or project-contained document window frontmost in Xcode.
2. Select the menu item "Edit Project Settings" from the "Project" menu in the menubar   
  **_or_**  
   Right-click the project icon in the "Groups & Files" tree-view of the Project window and select "Get Info" from the popup menu (the project's icon is a blue document icon located at the very top of this tree-view by default).
3. Select the "Build" tab at the top of the Project Info window that appears.
4. Set the "Configuration" to "Debug", "Release" or "All Configurations" from the popup menu at the top of the tab panel (compile settings will only be changed for the configuration that you select).
5. Scroll down to the heading named "GCC 4.0 - Language".
6. Each of these checkboxes allow customization of build settings. If you want to know what setting each will affect, click on the row and show the "Research Assistant" (Control-Command-?).

Completely custom command line settings can be passed to the compiler using the "Other C Flags" line (for C and Objective-C) or the "Other C++ Flags" (for C++).

More on Xcode's build settings can be found in the "[Xcode Build Setting Reference](http://developer.apple.com/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/Introduction/Introduction.html)".

## Post or pre build scripts

Build phases are how Xcode performs the different steps in a build. If you expand one of the targets in the "Targets" node of the "Groups & Files" tree-view of the Project window, you can see the different steps in the build. For a normal "Cocoa Application", the steps will be "Copy Bundle Resources", "Compile Sources" and "Link Binary with Libraries".

You can add a new build stage to a target by right-clicking the target and selecting the build phase you want from the "Add" submenu of the popup menu.

You can also choose one of the options in the "New Build Phase" submenu of the "Project" menu in the menubar to add a build phase to the current target.

To add a "script" build stage, select "New Run Script Build Phase". This will add a new script as the last phase of the build. If you want the script to be a "pre-build" script, you must drag it to the top of the list of build phases shown for the target in the "Targets" node of the "Groups & Files" tree-view of the Project window. An "inter build" script would also be possible by dragging to a location between other stages.

Finally, you must enter the script itself. Select the build phase and choose "Get Info" from the "File" menu in the menubar. Select the "General" tab and you can enter the script in the "Script" field.

A list of variables you can use in your script is listed on the [Run Script Build Phase](http://developer.apple.com/documentation/DeveloperTools/Conceptual/XcodeUserGuide/Contents/Resources/en.lproj/05_03_bs_build_phases/chapter_32_section_9.html) page of the Xcode documentation.

## Changing the built program's name

This can be a little tricky to find since the the built program's name ("MyProgram.app" for example) does not exist in any complete form in Xcode.

1. Have a project window or project-contained document window frontmost in Xcode with the "Active Target" set to the target whose product you'd like to rename.
2. Select the menu item "Edit Active Target '...'" from the "Project" menu in the menubar   
  **_or_**  
   Right-click the target's name under "Targets" in the "Groups & Files" tree-view of the Project window and select "Get Info" from the popup menu.
3. Select the "Build" tab at the top of the Project Info window that appears.
4. Set the "Configuration" to "Debug", "Release" or "All Configurations" from the popup menu at the top of the tab panel (compile settings will only be changed for the configuration that you select).
5. Scroll down to the heading named "Packaging".

The name of the application will be a combination of the "Executable Prefix" (normally empty), the "Product Name" (initially the same as the Project's name), the "Executable Prefix", and the "Wrapper Extension" (normally ".app" for Applications).

In short, most of the time you will just need to change the "Product Name" field.

## Replacing __MyCompanyName__ in the new file templates

Enter the following line:

```objc
defaults write com.apple.Xcode PBXCustomTemplateMacroDefinitions '{ "ORGANIZATIONNAME" = "Your Company Name" ; }'
```

into a Terminal window, replacing "Your Company Name" with whatever you choose.

You can also open the file at ~/Library/Preferences/com.apple.Xcode in "Property List Editor" and insert your company name as a string value for the key "ORGANIZATIONNAME" under the dictionary "PBXCustomTemplateMacroDefinitions". You may need to create "PBXCustomTemplateMacroDefinitions" at the top level if it doesn't already exist.

## Changing the new file templates

The complete set of file templates that Xcode uses for new files can be found at "/Developer/Library/Xcode/File Templates/", sorted by API (we love Cocoa the best).

You can add or modify them as you choose, although it's a good idea to backup changed files at a different location since "/Developer/Library/Xcode/File Templates/" may be lost if you move your account to a new computer or reinstall Xcode.

## Text macros

The "Text macros" in Xcode are a great time saver. You can find them under "Insert Text Macro" in the "Edit" menu but they are most useful when you know their shortcuts. Type the shortcut in a document in Xcode when you're editing, hit "F5" to autocomplete and it expands the macro to its full form, complete with variable locations.

For a full list of the default text macros and their shortcuts, visit Apple's "[Xcode User Guide: Repeating Code](http://developer.apple.com/mac/library/documentation/DeveloperTools/Conceptual/XcodeWorkspace/100-The_Text_Editor/text_editor.html#//apple_ref/doc/uid/TP40002679-SW43)".

The first way to customize text macros are to create entries for "BlockSeparator", "IndentedBlockSeparator", "InExpressionsSpacing", "PostBlockSeparator" and "PreExpressionsSpacing" in the "XCCodeSenseFormattingOptions" dictionary in your "com.apple.Xcode" preferences file.

As before, you can do that like this:

```objc
defaults write com.apple.Xcode XCCodeSenseFormattingOptions '{ "BlockSeparator" = "\n" ; }'
```

or by editing the "~/Library/Preferences/com.apple.Xcode" file directly.

You may also want to add completely new macros or customise more than these variables will allow. The best way to do this is to copy the "TextMacros.xctxtmacro" directory from:

```objc
/Developer/Applications/Xcode/Contents/PlugIns
```

to

```objc
~/Library/Application Support/Developer/Shared/Xcode/Specifications
```

and modify or add to the macros that Apple provide.

It is not advisable to edit the original "TextMacros.xctxtmacro" definitions contained inside Xcode.app directly. We copy them to our own Library since the Xcode.app versions will be replaced without warning every time you update Xcode.

> **Note**: the destination path to which you should copy "TextMacros.xctxtmacro" is correct here but wrong in the Apple-provided "Repeating Code" documentation linked above (the documentation currently omits the "Xcode" directory between "Shared" and "Specifications").

Macros are sorted by programming language. I'll leave you to work out exactly how the macros are formatted. I'm not aware of any formal documentation for the xctxtmacro file format but it's plain text in a "Property List"-style format so you shouldn't find it too hard to decipher.

## Environment Variables and Executable Arguments

With the desired Project and Target selected, choose "Edit Active Executable ..." from the "Project" menu in the menubar. The environment variables and executable arguments can be chosen on the "Arguments" tab.

The following environment variables are of particular importance when programming in Cocoa:

- NSDebugEnabled set to value YES — turns on extra debug information in Foundation
- NSZombieEnabled set to value YES — notifies when messages are incorrectly sent to deallocated objects allowing better debugging of this problem

For more debugging environment variables, check the "[Technical Note TN2124: Mac OS X Debugging Magic](http://developer.apple.com/technotes/tn2004/tn2124.html#SECFOUNDATION)" page from Apple.
