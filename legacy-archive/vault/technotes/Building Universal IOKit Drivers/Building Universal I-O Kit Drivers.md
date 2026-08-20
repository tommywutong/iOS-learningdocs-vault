---
title: Building Universal IOKit Drivers
apple_id: DTS10003874
resource_type: Technical Note
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/technotes/tn2163/_index.html
archived_at: '2026-07-26T19:54:08.764914Z'
---
> 导航：[总目录](../../README.md) · [technotes](../../_indexes/technotes.md)



# Retired Document

__Important:__
Retired Document: This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2163

# Building Universal I/O Kit Drivers

Describes the steps for configuring an Xcode I/O Kit kernel driver project to produce a universal driver. Also discusses common problems when loading universal drivers.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgqwugsbrfvjukq2ujfhu4mi)[Which Xcode and Mac OS X SDK Versions to Use](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgqwugsbrfvjukq2ujfhu4mq)[Building for Intel-based Mac computers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgqwugsbrfvjvkqstivbviskpjyza)[Building for PowerPC-based Mac computers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgqwugsbrfvjvkqstivbviskpjyzq)[Preparing Your Project to Build an Universal Driver](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgqwugsbrfvjukq2ujfhu4oa)[Xcode 2.x Build Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgqwugsbrfvjvkqstivbviskpjy4a)[Xcode 3.0 Build Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgqwugsbrfvjvkqstivbviskpjy4q)[Xcode 3.1 Build Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgqwugsbrfvjvkqstivbviskpjyyta)[Common Problems with Universal I/O Kit Drivers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgqwugsbrfvjukq2ujfhu4mjs)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobxgqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Building universal I/O Kit drivers is very similar to building universal applications, but there are critical differences that can affect a driver's binary compatibility. This technical note describes the steps for configuring an Xcode I/O Kit kernel driver project to produce a universal driver and discusses common binary compatibility problems with universal drivers.

[Back to Top](#)

## Which Xcode and Mac OS X SDK Versions to Use

Xcode 2.2.1 is the oldest version of Xcode that can be used to build universal I/O Kit drivers.

### Building for Intel-based Mac computers

The Intel side of your I/O Kit KEXT must be built using GCC 4.0 and the Mac OS X 10.4u (Universal) SDK or later. Use the SDK representing the oldest version of Mac OS X you wish to support, keeping in mind that the first version of Mac OS X to be shipped on Intel-based systems was Mac OS X 10.4.4.

### Building for PowerPC-based Mac computers

The PowerPC side of your KEXT should be built using the Mac OS X SDK representing the oldest version of Mac OS X you wish to support.

#### Building for PowerPC-based Mac computers: Targeting Versions of Mac OS X Earlier than 10.4

Building for versions of Mac OS X prior to 10.4 also requires you to build using GCC 3.3.

#### Building for PowerPC-based Mac computers: Targeting Mac OS X 10.4.x Using Xcode 2.2.x or Xcode 2.3

When using Xcode 2.2.x or 2.3, I/O Kit drivers targeting Mac OS X 10.4.x on PowerPC-based systems must be built using the Mac OS X 10.4.0 (not Universal) SDK. This is different from universal applications where the 10.4u (Universal) SDK can be used on both architectures.

The 10.4.0 SDK is available as a stand-alone installer from the [Apple Developer Connection web site](http://connect.apple.com/cgi-bin/WebObjects/MemberSite.woa/wa/getSoftware?fileID=20243). A [read me](http://connect.apple.com/cgi-bin/WebObjects/MemberSite.woa/wa/getSoftware?fileID=20244) file is available for the SDK installer.

The 10.4.0 SDK can also be installed from the Xcode 2.0 installer, located on the Mac OS X 10.4 install DVD. It can be found in the Xcode custom installs under Cross Development.

#### Building for PowerPC-based Mac computers: Targeting Mac OS X 10.4.x Using Xcode 2.4 or Later

Beginning with Xcode 2.4 there is another option, which is to define the preprocessor symbol `KPI_10_4_0_PPC_COMPAT` when building for the PowerPC architecture. When this preprocessor symbol is defined, the 10.4u (Universal) SDK will give the same results as using the 10.4.0 SDK. The same SDK can then be used for both PowerPC and Intel architectures.

__Important:__ If you are using the class `IOSCSIParallelInterfaceController` in your driver and you are targeting Mac OS X 10.4.x on PowerPC-based Macs, using `KPI_10_4_0_PPC_COMPAT` will not work in Xcode 2.x (r. 4802457). You will have to use the 10.4.0 SDK as described earlier in Building for PowerPC-based Mac computers: Targeting Mac OS X 10.4.x Using Xcode 2.2.x or Xcode 2.3. This problem was fixed in Xcode 3.0.

If your project is not configured properly you will see the error described later in Common Problems with Universal I/O Kit Drivers when you try to load your driver.

[Back to Top](#)

## Preparing Your Project to Build an Universal Driver

To convert a PowerPC-only Xcode I/O Kit driver project to a universal project, first make sure that all targets in your project are native Xcode targets. You can check this by opening your project in Xcode, then select the `Project` menu and see if the command `Upgrade All Targets in Project to Native` is enabled. If it is, make a backup copy of your project, then use that command to convert all of your legacy targets to native.

Then, make the following changes to the Project or Target Build settings depending on which version of Xcode you're using. Modify the Project settings if you want the settings to apply to all targets in the project. Modify the Target settings if you want just a particular target to produce a universal KEXT.

### Xcode 2.x Build Settings

Using the proper SDK and compiler versions is easily accomplished using Xcode's per-architecture build settings.

1. Set `Architectures` to `ppc i386`. This can be done by double-clicking the word `Architectures` and then selecting both the `PowerPC` and `Intel` checkboxes.
2. Remove any setting for `SDK Path` and `VALID_ARCHS` by selecting the option and then clicking the `-` button at the bottom of the window.
3. Add the custom settings `SDKROOT_i386` and `SDKROOT_ppc`. Set the value of each to the path of the SDK to use to build on each architecture. `SDKROOT_i386` should be set to `/Developer/SDKs/MacOSX10.4u.sdk` and `SDKROOT_ppc` should point to the SDK matching the oldest major Mac OS X release you wish to support, such as `/Developer/SDKs/MacOSX10.2.8.sdk`.
4. Add the settings `GCC_VERSION_i386` and `GCC_VERSION_ppc` that specify the compiler version to use when building for each architecture. `GCC_VERSION_i386` must be set to `4.0` or greater. If you want to support versions of Mac OS X prior to 10.4, `GCC_VERSION_ppc` must be set to `3.3`.
5. If you are using Xcode 2.4, 2.4.1, or 2.5, and the PowerPC side of your KEXT is targeting Mac OS X 10.4.x, add the setting `PER_ARCH_CFLAGS_ppc` that specifies compiler flags to pass to GCC only when building for the PowerPC architecture. Set the value of `PER_ARCH_CFLAGS_ppc` to `-DKPI_10_4_0_PPC_COMPAT`.
6. Set `Mac OS X Deployment Target` to `Compiler Default`.
7. Add the settings `MACOSX_DEPLOYMENT_TARGET_i386` and `MACOSX_DEPLOYMENT_TARGET_ppc`. These settings must have the value of a major Mac OS X release version number such as `10.2` or `10.4`. Do not specify software update versions such as 10.3.9. `MACOSX_DEPLOYMENT_TARGET_i386` must be set to `10.4` or later, and `MACOSX_DEPLOYMENT_TARGET_ppc` should be set to the oldest major Mac OS X release you wish to support.

### Xcode 3.0 Build Settings

Xcode 3.0 provides an improved user interface for per-architecture build settings over Xcode 2.x.

1. Set the `Configuration` menu at the top of the window to `All Configurations`.
2. Single click the value of the build setting `Architectures` and change it to `i386 ppc`.
3. Set `Base SDK` to `/Developer/SDKs/MacOSX10.4u.sdk` if the Intel side of your KEXT is targeting Mac OS X 10.4 or `/Developer/SDKs/MacOSX10.5.sdk` if targeting Mac OS X 10.5.

   If you want to use a different SDK when building for the PowerPC architecture, select the `Base SDK` build setting, then select `Add Per-Architecture Setting For` from the action menu at the lower left corner of the window and select `PowerPC` from the submenu. Change the value of the `PowerPC` setting just added to the path of the desired SDK for the PowerPC architecture, such as `/Developer/SDKs/MacOSX10.3.9.sdk`.
4. Set `Debug Information Format` to `DWARF with dSYM File`.

   If you need to use GCC 3.3 when building for the PowerPC architecture, select the `Debug Information Format` build setting, then select `Add Per-Architecture Setting For` from the action menu at the lower left corner of the window and select `PowerPC` from the submenu. Change the `PowerPC` setting just added to `Stabs` using the popup menu to the right.
5. Add the user-defined setting `GCC_VERSION` and set its value to `4.0`.

   If you want to support versions of Mac OS X prior to 10.4 when building for the PowerPC architecture, select the `GCC_VERSION` build setting, then select `Add Per-Architecture Setting For` from the action menu at the lower left corner of the window and select `PowerPC` from the submenu. Change the value of the `PowerPC` setting just added to `3.3`.
6. Set `Mac OS X Deployment Target` to `Mac OS X 10.4` or later.

   If you want to support versions of Mac OS X prior to 10.4 when building for the PowerPC architecture, select the `Mac OS X Deployment Target` build setting, then select `Add Per-Architecture Setting For` from the action menu at the lower left corner of the window and select `PowerPC` from the submenu. Change the value of the `PowerPC` setting just added to the oldest major Mac OS X release you wish to support using the popup menu to the right.
7. If the PowerPC side of your KEXT is targeting Mac OS X 10.4.x, select the `Other C Flags` build setting, then select `Add Per-Architecture Setting For` from the action menu at the lower left corner of the window and select `PowerPC` from the submenu. Change the value of the `PowerPC` setting just added to `-DKPI_10_4_0_PPC_COMPAT`.

### Xcode 3.1 Build Settings

Xcode 3.1 uses conditional build settings in place of the per-architecture build settings used by Xcode 2.x and 3.0.

To convert a PowerPC-only Xcode I/O Kit driver project to a universal project, first make sure that all targets in your project are native Xcode targets. You can check this by opening your project in Xcode, then select the `Project` menu and see if the command `Upgrade All Targets in Project to Native` is enabled. If it is, make a backup copy of your project, then use that command to convert all of your legacy targets to native.

Then, make the following changes to the Project or Target Build settings. Modify the Project settings if you want the settings to apply to all targets in the project. Modify the Target settings if you want just a particular target to produce a universal KEXT.

1. Set the `Configuration` menu at the top of the window to `All Configurations`.
2. Set `Architectures` to `Standard (32-bit Universal)`.
3. Set `Base SDK` to `10.4` or later.

   If you want to use a different SDK when building for the PowerPC architecture, select the `Base SDK` build setting, then select `Add Build Setting Condition` from the action menu at the lower left corner of the window. Change the `Any Architecture` setting to `PowerPC` and select the desired SDK for the PowerPC architecture from the popup menu to the right.
4. Uncheck the `Build Active Architecture Only` checkbox.
5. Set `Debug Information Format` to `DWARF with dSYM File`.

   If you need to use GCC 3.3 when building for the PowerPC architecture, select the `Debug Information Format` build setting, then select `Add Build Setting Condition` from the action menu at the lower left corner of the window. Change the `Any Architecture` setting to `PowerPC` and select `Stabs` from the popup menu to the right.
6. Set `C/C++ Compiler Version` to `GCC System Version (4.0)`.

   If you want to support versions of Mac OS X prior to 10.4 when building for the PowerPC architecture, select the `C/C++ Compiler Version` build setting, then select `Add Build Setting Condition` from the action menu at the lower left corner of the window. Change the `Any Architecture` setting to `PowerPC` and select `GCC 3.3` from the popup menu to the right.
7. Set `Deployment Target` to `Mac OS X 10.4` or later.

   If you want to support versions of Mac OS X prior to 10.4 when building for the PowerPC architecture, select the `Deployment Target` build setting, then select `Add Build Setting Condition` from the action menu at the lower left corner of the window. Change the `Any Architecture` setting to `PowerPC` and select the oldest major Mac OS X release you wish to support from the popup menu to the right.
8. Check the `Kernel Development Mode` checkbox.
9. If the PowerPC side of your KEXT is targeting Mac OS X 10.4.x, select the `Other C Flags` build setting, then select `Add Build Setting Condition` from the action menu at the lower left corner of the window. Change the `Any Architecture` setting to `PowerPC` and set the value to the right to `-DKPI_10_4_0_PPC_COMPAT`.
[Back to Top](#)

## Common Problems with Universal I/O Kit Drivers

Most problems you'll encounter after building a universal driver will appear when loading it. For example, `kextload` might report the error

```
com.mycompany.driver.MyDriverClass is not compatible with its superclass, <superclass name> superclass changed?
```

The reason for most load-time errors is that the wrong SDK was used when building the driver. For example, the PowerPC side of the driver is targeting Mac OS X 10.3.x but was built using the 10.4u SDK. Refer to the SDK version information shown earlier in Which Xcode and Mac OS X SDK Versions to Use. Then verify that your Xcode project is set up as described earlier in Xcode 2.x Build Settings, Xcode 3.0 Build Settings, or Xcode 3.1 Build Settings.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2018-05-17 | Moved to Retired Documents Library. |
| 2008-08-18 | Updated for Xcode 3.x. |
| 2006-11-10 | Added note about binary compatibility of IOSCSIParallelInterfaceController. |
| 2006-08-25 | Updated for Xcode 2.4. |
| 2006-02-02 | New document that how to build a universal I/O Kit kernel driver while avoiding common pitfalls. |

