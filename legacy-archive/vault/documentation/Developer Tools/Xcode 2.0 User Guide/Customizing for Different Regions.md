---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/ed_localize/ed_localize.html
archived_at: '2026-07-15T07:29:46.845641Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Version%20Control.md)[Previous](Using%20an%20External%20Editor.md)

# Customizing for Different Regions

Xcode lets you create applications, bundles,
and frameworks that are customized for different regions. Generally,
you’ll start by creating a variant for one particular region, called
the development region, and add more variants later.

In the Groups & Files list, a file customized for different
regions appears as a localized group, which has a file icon with
a triangle beside it. To see the file’s variants, click the triangle.
To add and remove variants, select the localized group, open the
inspector window, and use the two buttons at the bottom of the General
pane, as shown in the following figure.

__Figure 19-1__  Inspecting
a localized group

!

For more information on localizing your product for different
regions, see _[Internationalization and Localization Guide](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_.

To mark files for localization, select the files, open the
inspector, and click the Make File Localizable button. Xcode moves
the files into the development region's `.lproj` folder.
If a file was already in another `.lproj` folder,
Xcode copies it to the development region’s `.lproj` folder.

Xcode creates a localized group in the Groups & Files
list, with the file’s name and icon. To view the individual localization
variants, click the disclosure triangle next to the localized group
icon. The following figure shows the localized group for an application’s main
nib file in the Groups & Files list.

__Figure 19-2__  A
localized group in the Groups & Files list

!

You can inspect any of the localized variants individually
or you can inspect the localized group as a whole.

To remove files from localization, select the files, open
the inspector, and click the Remove All Localizations button. Xcode
moves the files from the development region’s `.lproj` folder into
the folder for nonlocalized resources. Other localized versions
of the files are removed from the project but are not deleted from
the disk.

To add files for a region, select the file or localized group
for which you want to add another region, open the inspector window,
and click the Add Localization button. Xcode queries you for the
name of the localization region and copies the development region’s version
of the files to the new region’s `.lproj` folder.

[Next](Version%20Control.md)[Previous](Using%20an%20External%20Editor.md)

