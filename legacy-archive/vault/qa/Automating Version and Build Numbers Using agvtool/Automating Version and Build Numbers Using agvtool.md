---
title: Automating Version and Build Numbers Using agvtool
apple_id: DTS40014500
resource_type: QA
platform: iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2014-05-12'
source_url: https://developer.apple.com/library/archive/qa/qa1827/_index.html
archived_at: '2026-07-18T02:35:00.227699Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1827

# Automating Version and Build Numbers Using agvtool

## Q:  How do I auto-increment my build and version numbers using `agvtool`?

A: The version and build number keys respectively specify the marketing and internal versions of your application. [agvtool](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/agvtool.1.html) is a command-line tool that allows you to automatically increment these numbers to the next highest number or to a specific number. This document provides step-by-step instructions for updating your build and version numbers using `agvtool`. The "Xcode" and "Command Line" sections indicate the steps to be respectively performed in Xcode and the command line.

The build number identifies an unreleased or released version of your application. It is stored in your application’s Info.plist as `CFBundleVersion` (`Bundle version`). See the [Information Property List Key Reference](https://developer.apple.com/library/mac/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/TP40009249-SW1) for more information about these keys.

See Figure 1 for an example showing the version number and the build number of the App Store app, which are respectively 1.3 and 201.4.

__Figure 1__  App Store application's version and build numbers

!

You must complete the following steps in your Xcode project.

Navigate to the Build Settings pane of your target, then update it for all your build configurations as follows:

- Set `Current Project Version`  to a value of your choosing.

  Your Xcode project data file, `project.pbxproj`, includes a `CURRENT_PROJECT_VERSION` (`Current Project Version`) build setting, which specifies the current version of your project. `agvtool` searches `project.pbxproj` for `CURRENT_PROJECT_VERSION`. It continues running if `CURRENT_PROJECT_VERSION` exists and stops running, otherwise. Its value is used to update the build number.
- Set `Versioning System` to `Apple Generic`.

  By default, Xcode does not use any versioning system. Setting `Versioning System` to `Apple Generic` ensures that Xcode will include all `agvtool`-generated version information in your project.

__Figure 2__  Setting up the Current Project Version and Versioning System build settings

!

`agvtool` searches your application’s Info.plist for your version and build numbers. It updates them if they exist and does nothing, otherwise. Make sure that the `CFBundleVersion` (`Bundle version`) and `CFBundleShortVersionString` (`Bundle versions string, short`) keys exist in your Info.plist as seen in Figure 3.

__Figure 3__  Version and build numbers in the Info pane

!!

Quit Xcode, then navigate to the directory containing your `.xcodeproj` project file in the Terminal application before running any of the following commands. The `.xcodeproj` project file contains `project.pbxproj`, which is used by `agvtool`.

To update the version number to a specific version, run


```
agvtool new-marketing-version <your_specific_version>
```

where <your_specific_version> is a number of your choosing as seen in Listing 1.

__Listing 1__  Update the version number to 2.0

```
$ xcrun agvtool new-marketing-version 2.0
Setting CFBundleShortVersionString of project MyProject to:
    2.0.

Updating CFBundleShortVersionString in Info.plist(s)...

Updated CFBundleShortVersionString in "MyProject.xcodeproj/../MyProject/MyProject-Info.plist" to 2.0
```


- To automatically increment your build number, run


```
agvtool next-version -all
```


  __Listing 2__  Auto-increment the build number to the next highest integer

```
$ xcrun agvtool next-version -all
Setting version of project MyProject to:
    2.

Also setting CFBundleVersion key (assuming it exists)

Updating CFBundleVersion in Info.plist(s)...

Updated CFBundleVersion in "MyProject.xcodeproj/../MyProject/MyProject-Info.plist" to 2
```
- To set the build number of your application to a specific version, run


```
agvtool new-version -all <your_specific_version>
```

  where <your_specific_version> is a number of your choosing.

  __Listing 3__  Set the build number to 2.6.9

```
$ xcrun agvtool new-version -all 2.6.9
Setting version of project MyProject to:
    2.6.9

Also setting CFBundleVersion key (assuming it exists)

Updating CFBundleVersion in Info.plist(s)...

Updated CFBundleVersion in "MyProject.xcodeproj/../MyProject/MyProject-Info.plist" to 2.6.9
```


- To view the current version number, run


```
agvtool what-marketing-version
```


  __Listing 4__  Display the current version number

```
$ xcrun agvtool what-marketing-version
No marketing version number (CFBundleShortVersionString) found for Jambase targets.

Looking for marketing version in native targets...
Looking for marketing version (CFBundleShortVersionString) in native targets...

Found CFBundleShortVersionString of "2.0" in "MyProject.xcodeproj/../MyProject/MyProject-Info.plist"
```
- To view the current build number, run


```
agvtool what-version
```


  __Listing 5__  Display the current build number

```
$ xcrun agvtool what-version
Current version of project MyProject is:
    2.2
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-05-12 | New document that describes how to auto-increment build and version numbers using agvtool. |

