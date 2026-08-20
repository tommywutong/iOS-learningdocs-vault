---
title: Xcode Debugging Guide
apple_id: TP40007057
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeDebugging/140-Debugging_in_the_Console/debugging_in_console.html
archived_at: '2026-07-15T07:27:55.118101Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Debugging Guide](Introduction.md)


[Next](Debugging%20Preferences.md)[Previous](Debugging%20in%20the%20Mini%20Debugger.md)

# Debugging in the Console

Xcode’s graphical interface for GDB, the GNU debugger, lets you perform most necessary debugging tasks. You may, however, encounter situations—such as working with watchpoints in GDB—that require you to interact directly with the debugger on the command line. Using the console window, you can:

- View the commands that Xcode sends to GDB or the Java command-line debugger
- Send commands directly to GDB or the Java command-line debugger (limited support)
- View the debugger output for those commands
- See debugging messages printed to `stderr` by your program or by system frameworks
- Debug a command-line program that requires input from `stdin`

If you are debugging a command-line program that requires input from `stdin`, you must use the console to communicate with your program when it is running in the debugger. This window is only available when your program is running under the debugger.

To open the Console window, choose Run > Console.

To enter commands, click in the console window and type at the `gdb` or `JavaBug` prompt. To get help with GDB and Java debugging commands, enter `help` at the console. To learn more about command-line debugging with GDB, see _[Debugging with GDB](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_toc.html#//apple_ref/doc/uid/TP40000996)_.

To make the Console text easily readable, Xcode lets you choose the text colors and fonts used in the console window. You can use different fonts and colors for the text you type in the console, the text the debugger writes to the console, and the debug console’s prompt. To change the colors used for text in the console window, use the Fonts and Colors group in Xcode > Preferences > Debugging. See Debugging Preferences for more information.

Note that Xcode uses an executable environment to determine how to launch your program. To specify command-line arguments and environment variables to use when launching your program from Xcode, edit the executable environment; you cannot alter this environment from the `gdb` command-line in the console window. See [Configuring Executable Environments](../Xcode%20Project%20Management%20Guide/Defining%20Executable%20Environments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojyfvbuuqsdijdecri) to learn more about configuring an executable environment.

[Next](Debugging%20Preferences.md)[Previous](Debugging%20in%20the%20Mini%20Debugger.md)

