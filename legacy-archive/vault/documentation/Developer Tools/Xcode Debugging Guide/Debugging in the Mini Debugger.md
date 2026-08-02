---
title: Xcode Debugging Guide
apple_id: TP40007057
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeDebugging/120-Debugging_in_the_Mini_Debugger/debugging_in_mini_debugger.html
archived_at: '2026-07-15T07:27:53.970831Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Debugging Guide](Introduction.md)


[Next](Debugging%20in%20the%20Console.md)[Previous](Debugging%20in%20the%20Text%20Editor.md)

# Debugging in the Mini Debugger

The mini debugger is a floating window that provides debugging controls similar to those of the text editor (see [Debugging in the Text Editor](Debugging%20in%20the%20Text%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqnbnknltc)) and the debugger (see [Debugging in the Debugger](Debugging%20in%20the%20Debugger.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqnrnknltc)), but that don’t require your switching back and forth between your application and Xcode.

The mini debugger has two modes, depending on whether the debugged process is running or stopped. When the process is running, the mini debugger provides controls to pause and stop the process, display the program’s Xcode project, and activate or deactivate breakpoints. When the program is stopped (after reaching a breakpoint, for example), the mini debugger provides a debugging experience similar to the one provided by the text editor. In fact, when the your program is stopped, the mini debugger’s entire content is made up of a text editor, although you cannot edit the source files it displays.

To show the mini debugger while running your application, choose Run > Mini Debugger.

Figure 4-1 shows the mini debugger with a running program.

__Figure 4-1__  Mini debugger with the program running

!

You can tell Xcode to always open the mini debugger when you debug a product using the On Start menu in Xcode Preferences > Debugging. See Debugging Preferences for more information.

These are the icons the mini debugger shows when the program is running:

- __Stop:__ Terminates the program.
- __Pause:__ Pauses the program.
- __Project:__ Opens the program’s Xcode project.
- __Breakpoints:__ Activates/deactivates breakpoints.

Figure 4-2 shows the mini debugger after the program stops.

__Figure 4-2__  Mini debugger with the program stopped

!

For more information about debugging in the mini debugger, see [Debugging in the Text Editor](Debugging%20in%20the%20Text%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqnbnknltc). Keep in mind that the text editor in the mini debugger doesn’t allow you to edit source files.

[Next](Debugging%20in%20the%20Console.md)[Previous](Debugging%20in%20the%20Text%20Editor.md)

