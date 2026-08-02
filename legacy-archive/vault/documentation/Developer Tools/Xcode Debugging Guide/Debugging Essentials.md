---
title: Xcode Debugging Guide
apple_id: TP40007057
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeDebugging/010-Debugging_Essentials/debugging_essentials.html
archived_at: '2026-07-15T07:27:49.609160Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Debugging Guide](Introduction.md)


[Next](Debugging%20in%20the%20Debugger.md)[Previous](Introduction.md)

# Debugging Essentials

Xcode lets you analyze your code line by line to view your program’s state at a particular stage of execution. This process is called _debugging_. To debug a program, you run it under the control of a _debugger_, which lets you pause programs and examine their state.

You can perform debugging operations in several ways:

- __In the text editor.__ The text editor allows you to perform many debugging operations, such as stepping through code lines and viewing the contents of variables. Debugging in the text editor lets you be close to your code as you debug it.
- __In the mini debugger.__ The mini debugger is a floating window that lets you perform debugging operations in way that is less intrusive to your code than debugging within Xcode. The mini debugger lets you debug your application in an environment that closely resembles the way your customers use your application.
- __In the debugger.__ The Xcode graphical debugger provides a rich, traditional debugging experience.
- __In the console.__ Some debugging operations produce textual output, which is displayed in the console. This window can also be used to issue commands directly to the GDB (The GNU Project Debugger) instead of through the Xcode graphical debugger.

When you debug a product, Xcode opens a debugging session with a debugger and your product’s binary. Before you can debug a program, however, it should contain as much debugging information as possible, so that Xcode can provide you with accurate and useful information during your debugging. See [Building for Debugging](../Xcode%20Project%20Management%20Guide/Building%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojtfvbecqsjindemry) for information about how to build a program to debug.

You may also debug a running process (not launched by Xcode). This operation is known as _attaching_ to a process. You can attach to a program running under Xcode or to any process for which you have a process ID. To attach to a running program use Run > Attach to Process.

This menu lists currently running programs launched from Xcode, identified by the program name and the name of the corresponding Xcode project. (This menu also lists other programs running on the computer.) You can use the menu’s Process ID option to attach to any process using its process ID, which you obtain using UNIX utilities such as `top`.

Before you can take advantage of the source-level debugger, the compiler must collect debugging information. To generate debugging symbols for a product, turn on the Generate Debug Symbols (see [GCC_GENERATE_DEBUGGING_SYMBOLS (Generate Debug Symbols)](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/XcodeBuildSettingRef/1-Build_Setting_Reference/build_setting_ref.html#//apple_ref/doc/uid/TP40003931-CH3-SW102)) build setting and build the product. This setting is turned on by default in the Debug build configuration. If you use this build configuration as the active build configuration when you build your target, the compiler generates the necessary debugging information. For more information about build configurations, see [Build Configurations](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeBuildSystem/400-Build_Configurations/build_configs.html#//apple_ref/doc/uid/TP40002692).

To view the build settings that are set in the Debug build configuration:

1. In the project window, select the target or targets you want to build and bring up the target editor.
2. Click Build to bring up the Build pane.
3. Choose Debug (or Development) from the Configuration pop-up menu at the top of the pane. You should see the Generate Debug Symbols setting in the table of build settings. Make sure that this setting is turned on; if it is, a checkmark appears in the Value column for this setting. Otherwise, turn on the setting by clicking the checkbox in the Value column.

For more information about building and running programs, see _[Xcode Project Management Guide](../Xcode%20Project%20Management%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmjx)_.

[Next](Debugging%20in%20the%20Debugger.md)[Previous](Introduction.md)

