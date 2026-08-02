---
title: Obtaining and Using Icons With Icon Services
apple_id: TP40000916
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2003-02-01'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Icon_Service_nd_Utilities/03tasks/tasks.html
archived_at: '2026-07-15T05:23:11.746549Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Obtaining and Using Icons With Icon Services](Introduction%20to%20Obtaining%20and%20Using%20Icons%20With%20Icon%20Services.md)


[Next](Document%20Revision%20History.md)[Previous](Icon%20Services%20Concepts.md)

# Icon Services Tasks

This chapter outlines basic and advanced tasks that you can perform using Icon Services.

This section describes basic tasks you can perform with Icon Services.

In order to call Icon Services functions, your application must obtain an `IconRef` for the icon data you want to use. There are three functions you can use to accomplish this task; the one you choose depends on how much information you have about the icon you wish to use. If you need an icon from the desktop database or a registered icon (an icon that has been previously identified to Icon Services), the simplest and fastest way to obtain an `IconRef` is to use the function `GetIconRef`. Icon Services defines a number of constants for non-fileFinder icons, which makes it simple to use the `GetIconRef` function to obtain an `IconRef` for one of these icons. Listing 3-1 shows an example of how to obtain an `IconRef` for the standard Help icon:

__Listing 2-1__  Obtaining an IconRef for the standard help icon

```
err = GetIconRef(kOnSystemDisk, kSystemIconsCreator, kHelpIcon,                &iconRef);
```

If you need an `IconRef` for a folder that you know has no custom icons associated with it, use the function `GetIconRefFromFolder`. If you need an `IconRef` for a file object for which you don’t have any information, use the function `GetIconRefFromFile`.

Once you obtain a valid `IconRef`, you can use Icon Services functions to accomplish two major types of tasks. The first type of task is to draw an icon of the appropriate size and type in a specified area. The second task is checking to see whether the user has clicked on or selected an icon (also known as hit-testing). These functions are designed to be similar to familiar Icon Utilities functions.

Icon Services provides two basic drawing functions. For the task of drawing an icon directly to the screen, use the function `PlotIconRef`. If you need to convert icon data into a QuickDraw region, use the function `IconRefToRgn`.

Icon Services provides several ways to determine whether a user has interacted with an icon. To determine whether a user has clicked on an icon, use the function `PtInIconRef`. If you need to determine whether an icon falls with a given rectangle (like a selection rectangle, for example), use the function `RectInIconRef`. You can also use the function `IconRefToRgn` to do hit-testing.

Icon Services gives you several ways to modify the icon data used by Icon Services. You can add icon data to the Icon Services cache by registering icon data with the functions `RegisterIconRefFromIconFamily` or `RegisterIconRefFromIconFile`. You can also release registered data by using the function `UnregisterIconRef`. You can override existing data in an `IconRef` and replace it with custom data by using the functions `OverrideIconRef` or `OverrideIconRefFromResource`. You can also restore the original data in an `IconRef` by using the function `RemoveIconOverride`.

You can speed up access to frequently-used icon data by registering icons. The preferred way of registering icons is to use the function `RegisterIconRefFromIconFile`. This will make the icon data purgeable if you need to free up memory later. If you can’t use the `RegisterIconRefFromResource` function, you can use the function `RegisterIconRefFromIconFamily`. To unregister icon data, use the function `UnregisterIconRef`.

If you need to refresh icon data without releasing an `IconRef`, you can use the function `UpdateIconRef` to obtain current icon data. This might be useful after you have changed a file’s custom icon, for example.

You may wish to redraw icons on a temporary basis without going to the trouble of obtaining a new `IconRef`. One example of this is when a user has started to download a file and you want to use partial file icons to represent the various stages of the download process. Icon Services provides two functions to temporarily override the data in an `IconRef`; the one you choose depends on the source of the data you will use for the override. If you obtain the source data from another `IconRef`, use the function `OverrideIconRef`. If the source data is contained in a resource, use the function `OverrideIconRefFromResource`. You can restore the original icon data by using the function `RemoveIconOverride`.

You may find it useful to modify the reference count of an `IconRef` in preference to obtaining multiple `IconRefs` to the same data. This might be useful when your application maintains multiple instances of the same icon data, such as multiple file-copying operations. Use the function `AcquireIconRef` to increment the reference count for an `IconRef`. This allows you to keep the icon data in the cache without going through the trouble of obtaining additional `IconRefs`. If you modify the reference count directly, be sure to decrement the reference count as needed by using the function `ReleaseIconRef`.

When you want to free up memory by releasing purgeable icon data from the cache, the preferred method is to use the function `FlushIconRefs`. You may also use the function `FlushIconRefsByVolume`, but this has two potential problems:

1. The additional scope of the `FlushIconRefsByVolume` function means it will take longer to complete.
2. Using the the `FlushIconRefsByVolume` function makes the icon data of all currently used `IconRefs` non-purgeable. This means any subsequent efforts to flush icon data will be much less effective.

A badge is an overlay or replacement for an icon. You can use a badge to signify that a folder contains special files, for example. Badges are described by a `'badg'` resource you store in a file’s resource fork or a folder’s invisible icon file. Figure 3-1 shows a folder alias icon displayed in standard form and with a badge.

__Figure 2-1__  Folder icons displayed in standard form and with a badge

![Folder icons displayed in standard form and with a badge](attachments/art/iss01.gif)

There are two steps required to use a custom badge with a file object.

- Clear the `kExtendedFlagsAreInvalid` bit and set the `kExtendedFlagHasCustomBadge` bit in the `extendedFinderFlags` field of the `ExtendedFileInfo` structure (if the object is a file) or the `ExtendedFolderInfo` structure (if the object is a folder).
- Add a resource of type `kCustomBadgeResourceType` (`'badg'`) and ID `kCustomBadgeResourceID` to a file’s resource fork or a folder’s icon file.

There are three ways to use the data from a `'badg'` resource.

1. The `customBadgeType` and `customBadgeCreator` fields let you designate a custom badge to display on top of another icon, as shown in [Figure 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjwfuzs2qscineucqsdie).
2. The `windowBadgeType` and `windowBadgeCreator` fields let you designate which icon to display in Finder window header of the badged file or folder.
3. The `overrideType` and `overrideCreator` fields let you designate the badge as a replacement for the standard icon for this file or folder.

The type and creator codes specified in a`'badg'` resource must be registered with Icon Services before you can use the badge. For more information, see [Registering Icon Data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjwfuzs2qscineuisckje).

If you supply a custom icon resource for a badge, Icon Services will use it in preference to other available data. For a complete description of the badge resource, see `'badg'`.

Here are some guidelines to follow if you choose to design custom icons for use with Icon Services.

- You must provide at least one of the following icon types: `'ICN#'`, `'ics#'`, or `'icl#'`.
- If you provide a deep mask, all of the non-transparent pixels in the deep mask should correspond to a black pixel in the black-and-white mask. This is important for hit-testing and proper erasing and drawing of the icon.
- If you provide 32-bit icon data, you should also provide an 8-bit version of the icon. This ensures that the icon can be displayed on an 8-bit display without unwanted dithering.
- 8-bit icon data is no longer limited to the 34 colors of the classic icon color palette. All 256 colors from the System palette are available.
- 4-bit icons are still supported. However, the 4-bit display configuration is rarely used and often unsupported, so we recommend that you do not provide 4-bit icon data. If you don’t provide 4-bit icon data, Icon Services will use black-and-white icon data instead.

[Next](Document%20Revision%20History.md)[Previous](Icon%20Services%20Concepts.md)

