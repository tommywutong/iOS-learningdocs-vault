---
title: How to Match a Crash Report to a Build
apple_id: DTS40012196
resource_type: QA
platform: iOS|Xcode Developer Tools|macOS
topic: General
technology: null
published: '2013-01-24'
source_url: https://developer.apple.com/library/archive/qa/qa1765/_index.html
archived_at: '2026-07-27T07:25:59.571590Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1765

# How to Match a Crash Report to a Build

## Q:  How can I know if the build that I am testing is the same build that generated a particular crash report?

A: If you have difficulty reproducing a problem the first step is to make sure that you are testing the same build that exhibited the problem.

Every executable has a __build UUID__, that uniquely identifies it. Crash logs include the build UUID of the app that crashed and all libraries that were loaded during the crash. This document describes how to find and compare the build UUID in a crash report and a deployed app. If you received a crash log from App Review, it's important to make sure you are testing the same build you submitted — not testing the build that was submitted is a common reason for App Store rejections.

__Important:__ The build UUID identifies a __build__. Even if a functionally-identical executable is rebuilt from the same source code, with the same compiler settings, it will have a different build UUID. Using Xcode's __Archive__ command, then distributing those same archived build for both testing and final release from the Organizer window is highly recommended. This lets you test and deploy copies of your app without rebuilding.

For more information, see:

__iOS__: [QA1764: How to reproduce bugs reported against App Store submissions](https://developer.apple.com/library/ios/qa/qa1764/)

__OS X__: [QA1778: How to reproduce bugs reported against Mac App Store submissions](https://developer.apple.com/library/ios/qa/qa1778/).

## 1) Find the build UUID in a Crash Report

The first line in the "`Binary Images:`" section of a crash report includes the build UUID, inside <>, of the app that crashed.

The line ends with the full path of the app's executable on the system.

__Note:__ On iOS the path to the app's executable will have the form `/var/mobile/Applications/<CONTAINER_UUID>/<PATH_TO_APP_EXECUTABLE...>`. The `CONTAINER_UUID` is __not__ the UUID you are looking for. To keep apps separate, iOS places them inside their own container directory. To ensure it's unique, the container is given a UUID as a name, which is intentionally unrelated to the app itself. Don't be thrown off by this second UUID, the one you want is inside `<>`.

The last parts of this path, after the `CONTAINER_UUID`, points to the executable inside the app bundle, and will be useful in Step 2.

__Listing 1__  Crash Report Excerpt

```shell
$ grep --after-context=2 "Binary Images:" Example.crash
Binary Images:
   0xb6000 - 0xb7fff +Example armv7 <270a9b9d7a333a4a9f1aaf8186f81394> /var/mobile/Applications/28D4F177-D312-4D3B-A76C-C2ACB4CB7DAD/Example.app/Example
0x2feb5000 - 0x2fed6fff  dyld armv7 <4a817f3e0def30d5ae2032157d889c1d> /usr/lib/dyld
```

Here, the build UUID is __270a9b9d7a333a4a9f1aaf8186f81394__, and the path to the app's executable is __Example.app/Example__. `28D4F177-D312-4D3B-A76C-C2ACB4CB7DAD` is the `CONTAINER_UUID`, and can be ignored.

[Back to Top](#)

## 2) Find the build UUID of an app binary

You can find the build UUID of an executable file using the [dwarfdump](x-man-page://1/dwarfdump) command line tool. These instructions will give you the build UUID of any app. You do not need to a crash log for this step.

__Listing 2__  Terminal command to print an executable's build UUID

```shell
$ xcrun dwarfdump --uuid <PATH_TO_APP_EXECUTABLE>
```

The file at `PATH_TO_APP_EXECUTABLE` must be an executable file, not an .app bundle or .ipa file.

If you have a .ipa file, you need to extract the .app bundle inside of it. Change the file extension from .ipa to .zip, then uncompress the zipped file, and get the .app bundle from the resulting `Payload` directory.

To look inside an .app bundle, right-click it in Finder, and choose "Show Package Contents".

iOS apps usually have their executable file in the first level of their .app bundle. Look for a file with a "Kind" of "Unix Executable File" in Finder.

OS X apps usually have their executable file inside the directory `Contents/MacOS/` inside their .app bundle.

__Listing 3__  Example of finding the build UUID of an IPA file, using Terminal

```shell
$ # Give a copy of the ipa file a .zip extension.
$ cp Example.ipa Example.zip
$
$ # open the zip file
$ unzip Example.zip
Archive: Example.zip
   creating: Payload/
   creating: Payload/Example.app/
   creating: Payload/Example.app/_CodeSignature/
  inflating: Payload/Example.app/_CodeSignature/CodeResources
  inflating: Payload/Example.app/embedded.mobileprovision
   creating: Payload/Example.app/en.lproj/
  inflating: Payload/Example.app/en.lproj/InfoPlist.strings
  inflating: Payload/Example.app/en.lproj/ViewController.nib
  inflating: Payload/Example.app/Example
  inflating: Payload/Example.app/Info.plist
 extracting: Payload/Example.app/PkgInfo
  inflating: Payload/Example.app/ResourceRules.plist
$
$ # go look inside the Payload directory to find the app
$ cd Payload
$ ls
Example.app
$
$ # print the build UUID of the app's executable file
$ xcrun dwarfdump --uuid Example.app/Example
UUID: 270A9B9D-7A33-3A4A-9F1A-AF8186F81394 (armv7) Example.app/Example
```

In this example, the app's build UUID is __270A9B9D-7A33-3A4A-9F1A-AF8186F81394__.

### More Than One Build UUID

You may see `dwarfdump` print more than one build UUID. This means the executable is a __fat binary__ (also known as a "multi-architecture" or "universal" binary). To take advantage of newer CPU optimizations, while staying compatible with older hardware, fat binaries combine different builds (called __slices__) of the app into one executable. Each slice is built differently for each CPU architecture. When a fat binary is run, only one slice from it will actually be executed.

__Important:__ Always test on the same kind of hardware an issue was reported on. Different hardware may run a different slice from a fat binary.

Differences in a how a slice was built can change how a bug behaves. For example, variables may be stored at different offsets in memory when building for different CPUs. So the same bug (accidentally storing one byte past the end of a buffer) could appear to change the value of a different variable, when running a different slice.

`dwarfdump` will print the architecture of a slice, inside `()` next to each slice's build UUID.

__Listing 4__  Example of an app with multiple build UUIDs

```shell
$ xcrun dwarfdump --uuid Example.app/Example
UUID: 270A9B9D-7A33-3A4A-9F1A-AF8186F81394 (armv7) Example.app/Example
UUID: 7711EC60-C0B2-3608-A539-182C77AE01ED (armv7s) Example.app/Example
```

In this example, the app also has a build UUID of __7711EC60-C0B2-3608-A539-182C77AE01ED__ for the __armv7s__ architecture.

If your app has multiple build UUIDs, repeat the next step with each of them to see if any of them match the crash report.

[Back to Top](#)

## 3) Compare Build UUIDs

The UUID printed by `dwarfdump` is in a slightly different format than is used in the crash log, it is UPPERCASE and includes four "-" characters. For your sanity, you may want to convert the strings to the same format before comparing them.

__Listing 5__  Example of using `tr` to print a build UUID in lowercase, without dashes, for comparison

```shell
$ xcrun dwarfdump --uuid Example.app/Example | tr '[:upper:]' '[:lower:]' | tr -d '-'
uuid: 270a9b9d7a333a4a9f1aaf8186f81394 (armv7) example.app/example
$
$ # Now that the build UUID is in the crash log format,
$ # we can just search for it in the crash log to confirm a match
$ grep 270a9b9d7a333a4a9f1aaf8186f81394 Example.crash
   0xb6000 - 0xb7fff +Example armv7 <270a9b9d7a333a4a9f1aaf8186f81394> /var/mobile/Applications/28D4F177-D312-4D3B-A76C-C2ACB4CB7DAD/Example.app/Example
```

In this example, the build UUID was in the crash log, proving that exact build generated the crash log.

If you cannot locate an archived version of the app, you may want to consider making another build by following these steps for [an iOS app](https://developer.apple.com/library/ios/qa/qa1764/), or these steps [a Mac OS X app](https://developer.apple.com/library/ios/qa/qa1778/), and re-testing or resubmitting it.

[Back to Top](#)

## Related Documents

[How to reproduce bugs reported against Mac App Store submissions](https://developer.apple.com/library/ios/qa/qa1778/)

[How to reproduce bugs reported against iOS App Store submissions](https://developer.apple.com/library/ios/qa/qa1764/)

[Testing iOS App Updates](https://developer.apple.com/library/ios/technotes/tn2285/)

[Understanding and Analyzing iOS Application Crash Reports](https://developer.apple.com/library/ios/technotes/tn2151/).

For steps to find iOS crash reports, see [Debugging Deployed iOS Apps](https://developer.apple.com/library/ios/qa/qa1747/).

For more information about application archiving, see the [Distributing Applications](https://developer.apple.com/library/ios/#documentation/ToolsLanguages/Conceptual/Xcode4UserGuide/DistApps/DistApps.html) section of the Xcode 4 User Guide.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-01-24 | The term "build identifier" was used in earlier versions of this document to refer to the "build UUID" of an app. |
| 2012-04-12 | New document that describes how to check what specific build generated a crash report. |
