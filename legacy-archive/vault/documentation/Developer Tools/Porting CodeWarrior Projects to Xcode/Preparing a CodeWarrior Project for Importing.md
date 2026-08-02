---
title: Porting CodeWarrior Projects to Xcode
apple_id: '20001708'
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2009-06-30'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MovingProjectsToXcode/mig_bef_converting/migration_before_convert.html
archived_at: '2026-07-15T07:25:16.781354Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Porting CodeWarrior Projects to Xcode](Introduction%20to%20Porting%20CodeWarrior%20Projects%20to%20Xcode.md)


[Next](Importing%20a%20CodeWarrior%20Project%20Into%20Xcode.md)[Previous](Xcode%20From%20a%20CodeWarrior%20Perspective.md)

# Preparing a CodeWarrior Project for Importing

This section describes steps you can take to modify your CodeWarrior project before importing it into Xcode. Taking an incremental approach should make it easier to get your project building successfully in Xcode.

If you have a classic application—that is, an application designed for versions of the Mac OS earlier than Mac OS X—you should convert your code to use Carbon. Carbon is a set of programming interfaces that allows applications (including those originally designed for Mac OS 8 and 9) to run natively in Mac OS X. If an application uses older Mac OS APIs that aren’t part of Carbon, it cannot run reliably in Mac OS X, except in Classic (or emulation) mode.

The amount of effort required to convert a project to Carbon depends on its complexity and on the programming tactics and Mac OS APIs it uses. For full information, see _[Carbon Porting Guide](../../Carbon/Carbon%20Porting%20Guide/Introduction%20to%20Carbon%20Porting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojr)_.

You should set the Project Type setting for your CodeWarrior project to Application Package. Packaging an application consists of putting the application’s code and resources in prescribed directory locations inside the application bundle.

To build an application as a package, you choose Application Package in the Project Type pop-up in the PPC Target pane. When you create a project from CodeWarrior stationery that uses one of the bundled types, such as “C Toolbox Carbon Bundle,” the Project Type is automatically set to Application Package.

Packaged applications require an information property list, named `Info.plist`. [The Information Property List and .plc Files](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslkcineueq2iinfa) describes this list, as well as differences in how to create it in CodeWarrior and Xcode.

Mach-O is the native executable format in Mac OS X and is the only format supported by Xcode. Applications that use Mach-O format have access to all native Mac OS X APIs, such as Quartz and POSIX, and can more easily support symbolic debugging with GDB. However, Mach-O applications cannot run in earlier versions of the Mac OS. For a summary of the advantages and issues of using Mach-O format, see [Use the Mach-O Binary Format](../../Performance/Performance%20Overview/Basic%20Performance%20Tips.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimjqfvbuqmrqgqwueq2jincugrsd) in _[Performance Overview](../../Performance/Performance%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimjq)_.

If your project currently builds a CFM application or library, you may want to add a target to the project to build a Mach-O version. This will allow you to isolate changes you’ll need for Mach-O before switching to Xcode. And you’ll still benefit from the automated setup performed when you import the project into Xcode. However, for a simple project, you may end up doing extra work.

Conversely, if your CodeWarrior project is not particularly complex, you may want to import it directly into Xcode (and switch to the Mach-O executable format at the same time). If you do, many changes will be handled automatically, including changing your linker settings and moving from MSL libraries to the standard C and C++ libraries. A disadvantage is that you’ll be making more changes in a new environment, where problems may be harder to isolate, so this approach isn’t recommended for more complex projects.

Whichever approach you take, you will still have some work to do after importing, as described in [After Importing a Project](After%20Importing%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytelkukbmferkggeydc).

[C and C++ Libraries](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslkcifbemrcci5aq) describes differences between the CodeWarrior MSL libraries and the standard C and C++ libraries for Mach-O. To build your application in Mach-O format, you’ll need to make these changes:

- On the Target pane of the Target Settings window, change your Linker setting to “Apple Mach-O PowerPC” (preferred) or “Mac OS X PowerPC Mach-O”.

  When you save your settings, CodeWarrior adds a Frameworks tab to your project window, if it didn’t already have one.
- If you load plug-ins via CFM, you’ll need to rewrite that code to use the CFBundle or CFPlugin APIs.

  You can read more about CFBundle in the document _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_.
- If your code makes assumptions about the size of the C++ `bool` type, you may have to make changes: in Mach-O, a `bool` is four bytes wide, not one. See [Make Code Changes for GCC Compatibility](After%20Importing%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytelkdjbceeskhi5ba) for details, and for other possible code issues.

The sections that follow list additional steps you’ll need to take in converting to use Mach-O format.

[Framework-Style Headers](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslkciffeiskkirba) provides background on working with framework-style headers. To continue making the switch to a Mach-O target, you’ll need to take these steps to start using framework headers:

- Remove `{Compiler}MacOS Support` from the Access Paths pane of the Target Settings window.
- Add necessary frameworks to your project. For example, you should include `System.framework`. You’ll probably also want to include `Carbon.framework`, and may need to include other frameworks, such as `CoreAudio.framework` or `OpenGL.framework`, if your project uses the APIs they define.

  Remember that the Carbon framework is an umbrella framework (it includes many other frameworks), so it may include most of the framework headers you need. Look in the header file `Carbon.h` within the framework for a complete list of the frameworks the Carbon framework includes.

  To add a framework, you can drag it from the Finder to the Frameworks tab in your project window. Or you can choose Project > Add Files and navigate to `/System/Library/Frameworks`.

  When you first add a framework such as the Carbon framework, CodeWarrior adds a path like the following to your access paths:

  `{OS X Volume}System/Library/Frameworks`

These steps are recommended, but not required.

- Remove all `#include <MacHeader.h>` statements from your source and header files.
- Use just the statement `#include <Carbon/Carbon.h>` in your prefix file. More information on the prefix file is provided in [Replace Your Prefix File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytalkukbmferkggeztm).

Applications that change from using Universal Interfaces to using framework-style include statements (in either CodeWarrior or Xcode), must conform to the C99 standard, as described in [Conform to the C99 Standard](After%20Importing%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytelkciveekqkfizba). In CodeWarrior, you can select the “Enable C99 Extensions” setting on the C/C++ Language pane in the Target Settings window.

[C and C++ Libraries](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslkcifbemrcci5aq) describes differences between the libraries you use in CodeWarrior and Xcode. To continue the switch to a Mach-O target, perform the following steps to change libraries:

- Remove any MSL libraries (such as `MSL_All_CarbonD.Lib`) from the Libraries folder in the Files tab of your project.
- Remove any access paths to MSL libraries from the Access Paths pane of the Target Settings window for the target.
- Add paths to the Access Paths pane for `{OS X Volume}usr/include` and `{OS X Volume}usr/lib`.
- Add the file `/usr/lib/libSystem.dylib` to your project. This is a symlink that will resolve to the appropriate version of the system library.
- You may need to add the file `crt1.o` (located in `/usr/lib`) to the project and make it the first file in the Link Order settings tab.

[Precompiled Headers and Prefix Files](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslkcifbesskfjfeq) describes differences in how you use prefix files in CodeWarrior and Xcode. To continue the switch to a Mach-O target, you’ll have to move away from the CodeWarrior precompiled headers. You can do that in one of two ways:

- Make your own prefix file and precompile it. As mentioned in a previous section, some projects can use just the statement `#include <Carbon/Carbon.h>` in your prefix file. Of course you may need to construct a more complex prefix file.

  In the C/C++ Language pane of the Target Settings window, enter the name of your file in the Prefix File text field.
- Or you can modify the source for the CodeWarrior precompiled header so that it precompiles against the headers in `/usr/lib`, rather than the MSL headers, then re-precompile it.

At this point you should be ready to test your Mach-O target.

To simplify the conversion process even further, you can make a copy of the project and delete any targets other than the targets you will import into Xcode. That will make importing faster and the resulting project will have just the desired target. Of course, you can also delete unneeded targets after importing into Xcode.

[Next](Importing%20a%20CodeWarrior%20Project%20Into%20Xcode.md)[Previous](Xcode%20From%20a%20CodeWarrior%20Perspective.md)

