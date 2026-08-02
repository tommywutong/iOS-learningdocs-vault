---
title: Carbon Porting Guide
apple_id: TP30000991
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-12-01'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/carbon_porting_guide/cpg_buildstruct/cpg_build_struct.html
archived_at: '2026-07-15T05:24:53.488811Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Carbon Porting Guide](Introduction%20to%20Carbon%20Porting%20Guide.md)


[Next](A%20Porting%20Example.md)[Previous](Preparing%20Your%20Code%20for%20Carbon.md)

# Building Carbon Applications

This chapter describes how to use the tools and libraries provided with the Mac OS X Developer Tools CD to build Carbon applications for both Mac OS 9 and Mac OS X. You can also install the Carbon system extension, `CarbonLib`, to run Carbon applications on Mac OS versions 8.1 and later.

If you plan to build, run, and debug Carbon applications for both Mac OS 9 and Mac OS X on a single system, the Mac OS X application `Classic.app` provides a convenient environment for running your development system. You can easily switch between the two environments, and launch applications in either.

If you prefer to develop on a native Mac OS 9 system (that is, on a computer running Mac OS 9 instead of Mac OS X), you’ll need to reboot to run Mac OS X and test your Carbon application in that environment.

If you have two computers, you might want to run Mac OS 9 on one computer and Mac OS X on the other. To transfer files between them, you can use one of the following methods:

- Enable file sharing on one of the machines and copy the files directly.
- Copy the files using FTP.
- Activate the Metrowerks remote debugger and select “Debug”. (Doing so transfers the file to Mac OS X and begins a debugging session. After transfer, you can quit the debugging session, leaving the file ready for launch, or perhaps GDB debugging.)

There are a number of tools and processes you can use to build and debug Carbon applications. This section describes three scenarios that Apple recommends, and the advantages of each.

This is the most likely scenario if you’re porting an existing Mac OS 9 application to Carbon, especially if you’re already using CodeWarrior. You’ll continue to use the Mac OS development tools and processes you’re familiar with, and you’ll create CFM applications that can run on both Mac OS 9 and Mac OS X. The only difference is that you’ll include the `CarbonLib` stub library in your CodeWarrior project.

Metrowerks CodeWarrior Pro version 8.0 and later has support to build Mach-O applications on Mac OS 9, as well as build and debug applications on Mac OS X. If you have a second computer, you may also want to investigate whether Metrowerks’ two-machine debugger suits your needs, as it can debug CFM applications on both platforms. Contact Metrowerks for information about these products.

Project Builder is Apple’s integrated development environment (IDE) for Mac OS X. It offers a comprehensive feature set that includes source-level debugging. Project Builder is a good choice if your application will run only on Mac OS X, and you want to take advantage of features available only on that platform. However, you can’t use Project Builder to build a CFM application, so if you want your program to run on both platforms you’ll either need to use CodeWarrior or other tools to create a CFM version for Mac OS 9.

See the Project Builder online help documentation for more information about creating Mach-O Carbon applications.

If you plan to use Metrowerks CodeWarrior, CodeWarrior Pro version 8.0 or later is recommended. You can run CodeWarrior natively on Mac OS 9 or Mac OS X.

Before you start Carbon development with CodeWarrior, you’ll need to install the tools and libraries provided with the Mac OS X Developer Tools CD or the Carbon SDK.

1. Copy the Carbon Support folder to the Metrowerks CodeWarrior folder on your hard disk. The Carbon Support folder should reside in the same folder as the CodeWarrior IDE application.
2. Copy the appropriate Carbon system extension (`CarbonLib` or `DebuggingCarbonLib`) from the Carbon Support:CarbonLib folder to your Extensions folder. You should keep only one Carbon extension in your Extensions folder at any time.

   - `CarbonLib` is the standard implementation of Carbon for Mac OS 8.1 or later.
   - `DebuggingCarbonLib` is a debugging version of CarbonLib.
3. `CarbonLib` is included in all versions of Mac OS 9 as well as the Classic environment on Mac OS X. However, to make sure you are using the latest version, you should replace the default `CarbonLib` with the latest one available (in this case version 1.6).
4. To avoid the potential for data loss in the event that you need to reinstall Mac OS X, ensure that your CodeWarrior project files and source code reside on a separate hard disk.

To build a Carbon version of your application, you’ll need to make the following changes to your CodeWarrior project.

1. Add the following statement to one of your source files before including any of the Carbon headers:

```
#define TARGET_API_MAC_CARBON 1
```

   This conditional specifies that the included header files should allow only Carbon-compatible APIs and data structures. You can include the conditional in a prefix file if you wish.
2. Add the `CarbonLibStub` stub file to your project.
3. Ensure that your project is not linking to any libraries that are not Carbon compatible. For example, the MPW ANSI C library is not Carbon compatible. Note that you should not directly link to `InterfaceLib` when you are linking with `CarbonLib`. On Classic Mac OS, `CarbonLib` will return an error to the Code Fragment Manager if your application attempts to link to both `CarbonLib` and `InterfaceLib`, causing the application launch to fail.
4. Ensure that your CodeWarrior access paths and other target settings are correctly specified. See the sample code included with the Carbon SDK for examples of how to do this.

You can launch your application from the Finder on a Mac OS 9 system by double-clicking its icon. To run Carbon applications on Mac OS 8 (version 8.1 or later), you must install the `CarbonLib` or `DebugCarbonLib` extension in the Extensions folder.

As long as your application resides on an HFS Plus disk, you can launch it by double-clicking its icon.You cannot launch applications from a standard HFS format disk on Mac OS X.

You can also use the command-line tool LaunchCFMApp to launch CFM applications from a terminal window in Mac OS X. If the CFM application is in the current working directory, the command is:

`/System/Library/Frameworks/Carbon.framework/Versions/A/Support/LaunchCFMApp`_filename_

If the application is in a different directory, you must specify the path.

Note that if your application does not contain a `'plst'` resource, a bundled `Info.plist` file, or a `'carb'` resource, Mac OS X opens the application in the Classic compatibility environment. To ensure that Mac OS X properly recognizes your application, it must include a resource of type `'plst'` with ID 0, a bundled `Info.plist` file, or a resource of type `'carb'` with ID 0.

Before building a Mach-O version of your application with CodeWarrior, you should follow the instructions in the previous section for building a CFM Carbon application. After you’ve successfully built and tested a CFM version of your application on Mac OS 9, you can use CodeWarrior to build a Mach-O version for debugging on Mac OS X.

Metrowerks CodeWarrior Pro 8.0 and later has support for Mach-O applications. See the Metrowerks documentation for more information.

Refer to your Metrowerks CodeWarrior documentation for instructions on building Mach-O versions of your application.

CodeWarrior creates an executable Mach-O binary that includes a resource fork. As long as this file resides on an HFS Plus disk, the resource fork remains intact and you can launch the application by double-clicking its icon.

Project Builder is included on the Mac OS X Developer Tools CD. Instructions for building Mach-O Carbon applications are available in Project Builder’s online help documentation.

An alternative to using CodeWarrior or ProjectBuilder for CFM applications is to use Apple’s MPW development environment, which is now available as a free download from the following website:

[http://developer.apple.com/tools/mpw-tools/](https://developer.apple.com/tools/mpw-tools/)

You should place the `CarbonLibStub` stub file in the folder `Interfaces and Libraries:Libraries:SharedLibraries`, while the Carbon version of the Universal Headers should be placed in `Interfaces and Libraries:Interfaces:CIncludes`.

You compile your application and link against `CarbonLibStub` just as you would when using CodeWarrior. Note however that Carbon applications must contain a `‘SIZE’` resource, and the resource must have the `acceptSuspendResumeEvents` flag set. While CodeWarrior adds a `‘SIZE’` resource automatically, you must create your own when building with MPW.

In addition, you need to override your default entry point (by using the `-m` option in PPCLink) with one of the following:

- `main` if your application does not call `exit()` and does not expect any exit procedures to run.
- `__appstart` if you want the functionality previously supplied by `__start`. `__appstart` is a stripped-down version of `__start` that initializes the environment, but does not provide support for MPW tools. To use `__appstart`, you need to link with `StdCRuntime.o` and `StdCLib` in addition to CarbonLib.

The version of `StdCRuntime.o` containing `__appstart`, as well as a Carbon-friendly version of the CreateMake tool, will be available from the following web site:

[http://developer.apple.com/tools/mpw-tools/updates.html](https://developer.apple.com/tools/mpw-tools/updates.html)

You should also examine the PackageTool sample application in the Sample Code folder of the CarbonLib SDK and the MPW release notes for more specifics about the build process.

You can debug Carbon applications on Mac OS 9 or Mac OS X using the Metrowerks debugger. You can use also this debugger with two networked machines (for example, one running Mac OS 9 and the other running Mac OS X). Contact Metrowerks for more information.

You can also debug Carbon applications on Mac OS X using GDB, which you can run from a terminal window. Although GDB cannot directly debug a CFM application at this time, there is a workaround that lets you perform low-level debugging on a CFM application. You’ll use GDB to debug LaunchCFMApp, a Mach-O program that launches CFM applications.

This workaround has the following features and limitations:

- You can set breakpoints at Mach-O functions. Since the Carbon library is Mach-O code, you can set breakpoints at Carbon functions. However, you cannot set breakpoints at CFM functions, including those in your application.
- You can examine the memory contents at any address with the `x` command. However, you cannot view variables or expressions, since GDB cannot use the symbol names in a CFM application.
- You cannot step through your application’s code.

To debug your CFM application:

1. Launch the Terminal application: `/Applications/Utilities/Terminal.app`.
2. Enter `gdb /System/Library/Frameworks/Carbon.framework/Versions/A/Support/LaunchCFMApp`.

   GDB loads the LaunchCFMApp program.
3. If you want, set breakpoints at any Carbon function with the `br` command.

   For example, you may want to set a breakpoint at the `DebugStr` function, because `DebugStr` prints its argument without stopping the program’s execution. Enter `br DebugStr` at the GDB prompt.
4. At the GDB prompt, enter `r <app-pathname>`, where `<app-pathname>` is the full pathname for your CFM application.

   To enter the application’s pathname, drag the application’s icon to the Terminal window.

   LaunchCFMApp launches your application.

To pause your application’s execution at any time, press Control-C in the Terminal application. To continue your application, enter `cont`. For more information on GDB, enter `help`.

Here are some additional hints that you might find useful:

- From the terminal window, entering `setenv CFMDebugFull 1` directs LaunchCFMApp to display debugging information at application launch time.
- Entering `setenv USERBREAK 1` enables GDB to catch C++ exceptions.
- You can set the environment variable `DYLD_IMAGE_SUFFIX` to specify an optional suffix to add to Mach-O libraries when they are loaded. For example, entering `setenv DYLD_IMAGE_SUFFIX _debug` provides an easy way to link to the debug versions of the various frameworks. You can easily toggle between the normal and debug versions of these libraries without having to rebuild your application each time. The debug versions often perform more assertions, parameter checks, and so on, which may simplify debugging.
- You can call functions in Mach-O libraries directly from the GDB command line, as long as they were explicitly or implicitly loaded. For example, you could call the `CFShow` function, which shows the contents of various Core Foundation and Cocoa objects. Because the Carbon framework is built as Mach-O binaries, you can call Carbon functions from GDB, even those not directly called by your application.
- The remote debugger nub has some command line options which you can view by entering `/usr/libexec/gdb/DebugNub -help`
- If you want to examine parameter values for CFM applications in GDB, you can do so by examining register values. For example, given a function

```
void loofah (int x, int y, int z);
```

  then `print $r3` from the GDB command line obtains the value of x (passed in GPR3). Remember that the usual calling conventions apply in determining which parameters are passed in which registers. See _Mac OS Runtime Architectures_ for more information about PowerPC calling conventions.

[Next](A%20Porting%20Example.md)[Previous](Preparing%20Your%20Code%20for%20Carbon.md)

