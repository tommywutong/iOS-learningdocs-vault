---
title: Porting CodeWarrior Projects to Xcode
apple_id: '20001708'
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2009-06-30'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MovingProjectsToXcode/migration_overview/migration_overview.html
archived_at: '2026-07-15T07:25:20.306361Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Xcode%20From%20a%20CodeWarrior%20Perspective.md)

# Introduction to Porting CodeWarrior Projects to Xcode

This document describes how to move Mac OS software projects from CodeWarrior to Xcode, the Apple integrated development environment. It lists similarities and differences between the two environments, describes how to import a CodeWarrior project into Xcode, and provides detailed information on many conversion issues.

The Xcode application is part of the developer tools distributed with Mac OS X version 10.3 and later. It provides a powerful user interface to many industry-standard and open-source tools, including GCC, `javac`, `jikes`, and GDB. Xcode contains templates for creating applications, frameworks, libraries, plug-ins, Java applications and applets, and command-line tools. Xcode supports both Cocoa and Carbon development, using C, C++, Objective-C, and Java.

Although this document generally describes how to convert CodeWarrior projects that build applications, much of the information can be applied to projects that build plug-ins, bundles, frameworks, and other kinds of software.

CodeWarrior descriptions and examples in this document are based on CodeWarrior Pro version 8.3 for Macintosh.

This document is intended for CodeWarrior users, and assumes that you have some familiarity with the Mac OS, including Mac OS X.

- For detailed information on the development tools available with Xcode, see Mac OS X Developer Tools in _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.

  Among other new and revised documents, the Tools Documentation includes updated GCC documentation: _GNU C/C++/Objective-C 4.0 Compiler User Guide_ and _GNU C 4.0 Preprocessor User Guide_.
- For introductory information on Mac OS X, see _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_ .

The primary documentation for performing operations with Xcode is _Xcode 2.2 User Guide_.

The following documents provide information on moving other kinds of software to Mac OS X.

- _UNIX or Linux software_

  - _[Porting UNIX/Linux Applications to OS X](../../Porting/Porting%20UNIX-Linux%20Applications%20to%20OS%20X/Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambt)_.
  - [Technical Note 2071: Porting Command Line UNIX Tools to Mac OS X](https://developer.apple.com/technotes/tn2002/tn2071.html)
- _Windows software_

  - _[Porting to Mac OS X from Windows Win32 API](../../Porting/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4ta2i)_

You can find additional information about porting code to Mac OS X in the [Porting Documentation](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000431) area.

This document contains the following:

- This Introduction describes the audience for the document and summarizes the contents.
- [Xcode From a CodeWarrior Perspective](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslkukbmferkggeydc) describes similarities and differences in key features of Xcode and CodeWarrior. It also describes how to use certain Xcode features.
- [Preparing a CodeWarrior Project for Importing](Preparing%20a%20CodeWarrior%20Project%20for%20Importing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytalkukbmferkggeydc) describes steps you can take to modify your CodeWarrior project before importing it into Xcode.
- [Importing a CodeWarrior Project Into Xcode](Importing%20a%20CodeWarrior%20Project%20Into%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytclkukbmferkggeydc) provides a brief walk-through of importing a CodeWarrior project.
- [After Importing a Project](After%20Importing%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytelkukbmferkggeydc) describes steps you may need to take to successfully build an imported CodeWarrior project in Xcode.
- [Using PowerPlant in Universal Binaries](Using%20PowerPlant%20in%20Universal%20Binaries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzsfvjvomi) describes modification you may need to make to build universal binaries that use PowerPlant.
- [Where to Go From Here](Where%20to%20Go%20From%20Here.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytilkukbmferkggeydc) points to some tools and performance documents you’ll want to consider as you work on your Mac OS X software.

You can get quick answers to your day-to-day Xcode questions by sending email to xcode-users@lists.apple.com. You can become a member of this list at [Apple Mailing Lists](http://lists.apple.com/).

Your feedback and suggestions for Xcode are welcome. For feedback on this document, use the link at the bottom of each page. To request a feature or report a bug in Xcode, use the [Apple Bug Reporter](http://bugreport.apple.com/).

To report bugs or to receive the bi-weekly Apple Developer Connection News email newsletter, you must be a member of Apple Developer Connection (ADC). You can [sign up](http://connect.apple.com/) for a free ADC Online membership.

[Next](Xcode%20From%20a%20CodeWarrior%20Perspective.md)

