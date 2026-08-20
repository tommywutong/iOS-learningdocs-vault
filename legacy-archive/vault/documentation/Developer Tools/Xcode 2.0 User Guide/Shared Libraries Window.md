---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/db_shared_libs/db_symbols.html
archived_at: '2026-07-15T07:29:23.925437Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Using%20Fix%20and%20Continue.md)[Previous](Examining%20Program%20Data%20and%20Information.md)

# Shared Libraries Window

The Shared Libraries window lets you see which
libraries have been loaded by an executable running in Xcode’s
debugger. To open the Shared Libraries window, choose Debug >
Tools > Shared Libraries.

The Module Information table lists all of the individual libraries
that the executable links against. In this table, you can see the
name and address of each shared library, as well as which symbols
the debugger has loaded for that library. The Starting column shows
which symbols the debugger loads by default for a given library
when the current executable is running. The Current Level column
shows which symbols the debugger has loaded for the library during
the current debugging session. When an entry has a value in the
Address and Current Level columns, the library has been loaded in
the debugging session.

The path at the bottom of the window shows where the currently
selected library is located in the file system. You can quickly
locate a particular library by using the search field to filter
the list of libraries by name. You can add and delete libraries
from this list using the ‘+’ and ‘-’ buttons.

Using the Shared Libraries window you can also choose which
symbols the debugger loads for a shared library. This can help the
debugger load your project faster. You can specify a default symbol
level for all system and user libraries; you can also change which symbols
the debugger loads for individual libraries.

For any shared library, you can choose one of three levels
of debugging information:

- All loads
  all debugging information, including all symbol names and the line numbers
  for your source code.
- External loads only the names of the symbols declared external.
- None loads no information.

You can specify a different symbol level for system libraries
and user libraries. User libraries are any libraries produced by
a target in the current project. System libraries are all other
libraries.

By default, the debugger loads only external symbols for system
and user libraries and automatically loads additional symbols as
needed, as described in [Lazy Symbol Loading](Running%20in%20Xcode%E2%80%99s%20Debugger.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrthewugrkhineucrsc). Disabling
the "Load symbols lazily" option, described in [Debugging Preferences](Xcode%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrwgewugskiircusssj),
changes the default symbol level for User Libraries to “All.”
This is a per-user setting and affects all executables you define.
You can also customize the default symbol level settings for system
and user libraries on a per-executable basis, using the Default
Level pop-up menus in the Shared Libraries window.

For some special cases—applications with a large number
of symbols—you may wish to customize the default symbol level
for individual libraries when running with a particular executable.
To set the initial symbol level to a value other than the default,
make a selection in the Starting column. While debugging you can
increase the symbol level using the Current Level column. This can
be useful if you need more symbol information while using GDB commands
in the Console. Clicking Reset sets all of the starting symbol levels for
the libraries in the Module Information table back to the Default
value.

[Next](Using%20Fix%20and%20Continue.md)[Previous](Examining%20Program%20Data%20and%20Information.md)

