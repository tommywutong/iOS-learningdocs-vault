---
title: Xcode Debugging Guide
apple_id: TP40007057
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeDebugging/400-Mac_OS_X_Low-Level_Debugging/mac_os_low-level_debugging.html
archived_at: '2026-07-15T07:28:00.985661Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Debugging Guide](Introduction.md)


[Next](Debug%20Information%20Format.md)[Previous](Debugging%20Programs%20Remotely.md)

# Mac OS X Low-Level Debugging

Many of the subsystems in Mac OS X include debugging facilities that can help you in your debugging tasks. You can use most of these debugging facilities along with Xcode. Many debugging facilities are enabled or disabled by setting an environment variable; you can modify the executable environment to set these environment variables from Xcode. Xcode also includes several options for enabling specific debugging options, such as `libgmalloc` (Guard Malloc), loading debug library variants, and stopping on Core Services debugging functions (described in [Pausing on Core Services Debugging Functions](Managing%20Program%20Execution.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqobninfeqrkdincuq)). For more on the many debugging facilities available in Mac OS X, see _TN2124: Mac OS X Debugging Magic._

Many Mac OS X system frameworks include debug versions in addition to the production version. These library variants are identified by their `_debug` suffix. Debug variants of the system frameworks usually include debugging symbols, extra assertions, and often extra debugging facilities. You can modify the executable environment to have Xcode use the debug variants for libraries that your program loads.

To use the debug variant of a library, open the Info window for the executable environment that you use to run your program. In the General pane, choose “debug” from the menu “Use [_suffix_] suffix when loading frameworks.”

Xcode also integrates Guard Malloc ( `libgmalloc` ) into the debugger interface. Guard Malloc helps you debug memory problems by causing your program to crash on memory access errors. Because Guard Malloc causes your program to crash, you should use Guard Malloc with the debugger. When a memory access error occurs and your program crashes, you can look at the stack trace, determine exactly where the error occurred, and jump to the location of the problem.

To enable debugging with Guard Malloc from Xcode, choose Debug > Enable Guard Malloc before starting the debugging session. You can also use Guard Malloc with GDB from the command line, by setting the `DYLD_INSERT_LIBRARIES` environment variable, as described in the man page for `libgmalloc`. To learn how to set environment variables for development, see [Configuring Executable Environments](../Xcode%20Project%20Management%20Guide/Defining%20Executable%20Environments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojyfvbuuqsdijdecri).

Guard Malloc has a number of additional options available. You can take advantage of these by setting the appropriate environment variables on the executable. In the inspector window for the executable, open the Arguments pane and add the environment variables to the environment variables table at the bottom of the window. See the man page for `libgmalloc` for additional details and information.

[Next](Debug%20Information%20Format.md)[Previous](Debugging%20Programs%20Remotely.md)

