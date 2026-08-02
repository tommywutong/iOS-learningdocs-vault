---
title: Online Help
apple_id: 10000009i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2006-06-28'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OnlineHelp/Tasks/SpecifyHelpFile.html
archived_at: '2026-07-15T07:17:34.050815Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Online Help](Introduction%20to%20Online%20Help.md)


[Next](Document%20Revision%20History.md)[Previous](Tooltips.md)

# Specifying the Comprehensive Help File

If you’ve registered your help information in your application’s property list (`Info.plist`), when the user chooses the Help menu item the help file you specified for your application is displayed. This file should be the starting point of your help, and should allow users to access whatever information they might need.

Place a folder containing your help files in the `Resources` folder inside your application’s bundle. An HTML meta tag in must be specified on your help’s title page (the “`AppleTitle`” tag). Use Xcode to specify the two necessary `Info.plist` keys, which are `CFBundleHelpBookFolder` and `CFBundleHelpBookName`.

It’s possible for applications to have more than one command under the Help menu and to have each command open a different help file. To implement this, connect each of the Help menu commands to a different action method. The action methods should call one of the functions from the Apple Help API to display your help.

[Next](Document%20Revision%20History.md)[Previous](Tooltips.md)

