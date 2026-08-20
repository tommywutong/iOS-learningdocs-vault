---
title: Carbon Developer Tools Release Notes
apple_id: TP40001364
resource_type: Release Note
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/releasenotes/Carbon/RN-CarbonTools/index.html
archived_at: '2026-07-18T02:50:21.914136Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Carbon Developer Tools Release Notes for Mac OS X v10.5

> [!IMPORTANT]
> 

This release note describes changes in the developer tools in the `/Developer/Tools` directory that assist in the development and debugging of Carbon applications. This release note covers Xcode 2.2 through 3.0.

#### Contents:

- [Carbon Developer Tools moved to /Developer/usr/bin](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrufvcg63tujruw422fnrsw2zlooreuixzr)
- [Rez and DeRez](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrufvcg63tujruw422fnrsw2zlooreuixzs)
- [ResMerger](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrufvcg63tujruw422fnrsw2zlooreuixzt)
- [CpMac and MvMac](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrufvcg63tujruw422fnrsw2zlooreuixzu)
- [RezDet](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrufvcg63tujruw422fnrsw2zlooreuixzv)
- [SetFile and GetFileInfo](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrufvcg63tujruw422fnrsw2zlooreuixzw)
- [SplitForks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnrufvcg63tujruw422fnrsw2zlooreuixzx)

### Carbon Developer Tools moved to /Developer/usr/bin

The `Rez`, `DeRez`, `ResMerger`, `RezDet`, `RezWack`, `UnRezWack`, `CpMac`, `SetFile`, `GetFileInfo`, `SplitForks`, `PPCExplain`, and `MergePef` tools have moved to the `/usr/bin` folder in the Developer directory, and Xcode has been updated to use Rez in its new location. Symbolic links to the Carbon Developer Tools are provided in the the `/Tools` directory of the Developer folder so that scripts in a Run Script Build Phase or a custom Build Rule will find them.

If you move or rename the Developer directory, Xcode and associated tools will find them there automatically. If you use these tools from your own scripts, you may need to use the `${DEVELOPER_DIR}` environment variable and/or `xcode-select` to find the Carbon Developer Tools.

### Rez and DeRez

In Xcode 2.2 and later, Rez and DeRez accept pathnames longer than 255 characters, and can handle UTF-8 characters in pathnames.

In Xcode 2.2 and later, `Rez` accepts a new `-arch` command-line option, and uses its argument to define the macro `__arch__`. Xcode passes the value of `$(ARCH)`, so your resource headers can conditionalize resource building with `#ifdef __ppc__` and `#ifdef __i386__`, just as in source and headers.

File type and creator codes are not byte-flipped correctly using Xcode 2.2 and earlier on Developer Transition Kit seed machines. They are correct using Xcode 2.2.1 on production Intel-based Macintosh models.

DeRez results were incorrect on Intel-based Macintosh models with Xcode 2.2. They are correct with Xcode 2.2.1 and later.

In Xcode 2.3 and later, Rez will look in both the resource and data forks of files incliuded via #include and $$READ directives.

In Xcode 2.3 and later, DeRez reports the value of "point" and "rect" structures correctly on Intel-based Macintosh models. In 2.2.1 on Intel, the h, v, top, bottom, left, and right values were byte-flipped (e.g. a value of 1 would be printed as 512).

In Xcode 2.5, 3.0, and later, Rez accepts the new `-isysroot` command-line flag with a path to an SDK as the argument. Rez will use this path as the starting point to find any subpath that begins with `/System`, `/Library`, or `/Developer`. Xcode now passes `-isysroot $(SDKROOT)` when building against an SDK to allow the ResourceManager Resources build phase to build against the resource headers in the SDK instead of the base system.

### ResMerger

In Xcode 2.3 and later, ResMerger supports the `-skip` option. Using this option causes the given resources to be omitted from the merged destination file.

### CpMac and MvMac

The `CpMac` and `MvMac` tools are provided only for legacy script support. Since Mac OS X 10.4 the standard Unix `cp` utility copies Finder information, resource forks, and HFS metadata, and is preferred for speed, versatility, and robustness. `CpMac` and `MvMac` are deprecated and will be removed in a future version of Mac OS X.

### RezDet

A new tool, `RezDet`, has been added to the Carbon Developer Tools. This is a port of the MPW tool that investigates the resource fork of the specified files for damage or inconsistencies. See the man page for details on use.

### SetFile and GetFileInfo

As of Xcode 2.2, `SetFile` and `GetFileInfo` now each take a `-P` command-line option that causes symbolic links to not be followed. This enables you to read or set the HFS metadata properties of symbolic links themselves. `SetFile` and `GetFileInfo` never follow alias files.

### SplitForks

In Xcode 2.3 and later, `SplitForks` correctly copies the POSIX metadata of the original file to the AppleDouble file. In previous versions, the AppleDouble file would inherit the group, owner, and permissions of the parent directory rather than those of the original file.
