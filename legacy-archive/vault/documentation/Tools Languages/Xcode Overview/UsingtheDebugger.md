---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/UsingtheDebugger.html
archived_at: '2026-07-27T06:57:08.123341Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](ExaminingtheViewHierarchy.md)[Previous](ManagingSchemes.md)

## Using the Debugger

After you click the Run button in the workspace toolbar and your app builds successfully, Xcode runs your app and starts a debugging session. You can debug your app directly within the source editor with graphical tools such as data tips and Quick Look for the value of variables.

The debug area and the debug navigator let you inspect the current state of your running app and control its execution.

（原归档配图获取待重试：`XC_O_DebugFeatures_2x.png`）

Creating a quality app requires that you minimize your app’s impact on your users’ systems. Use the debug gauges in the debug navigator to gain insight into your app’s resource consumption, and when you spot a problem, use Instruments to measure and analyze your app’s performance. Use the energy guides to minimize your impact on battery life. For more information, see _[Energy Efficiency Guide for iOS Apps](../../Performance/Energy%20Efficiency%20Guide%20for%20iOS%20Apps/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbt)_ and _[Energy Efficiency Guide for Mac Apps](../../Performance/Energy%20Efficiency%20Guide%20for%20Mac%20Apps/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrz)_.

If you are developing an iOS or watchOS app, use Simulator to find major problems during design and early testing.

You can configure Xcode to help you focus on your debugging tasks. For example, when your code hits a breakpoint, you can make Xcode automatically play an alert sound and create a window tab named Debug, where Xcode displays the debug area, the debug navigator, and your code at the breakpoint.

### Controlling Execution

Xcode lets you step through your code line by line to view your program’s state at a particular stage of execution. Use the debug area to control the execution of your code, view program variables and registers, view its console output, and interact with the debugger. You can also use the debug area to navigate the OpenGL calls that render a frame and to view the rendering-state information at a particular call.

Display the debug area by clicking the center button (（原归档配图未能恢复：`XC_O_debug_button_2x.png`）) in the view selector in the workspace window toolbar.

（原归档配图未能恢复：`XC_O_DebugArea_2x.png`）

You can suspend the execution of your app by clicking the pause button (which toggles between （原归档配图获取待重试：`DebugPause_2x.png`） to pause and （原归档配图获取待重试：`DebugRun_2x.png`） to continue) in the debug area toolbar. To set a breakpoint, open a source code file and click the gutter next to the line where you want execution to pause. A blue arrow (（原归档配图获取待重试：`breakpoint_icon_2x.png`）) in the gutter indicates the breakpoint. For more information on breakpoints, including how to set breakpoint actions and the different kinds of breakpoints, see [Xcode Help](https://help.apple.com/xcode).

When your app is paused, the currently executing line of code is highlighted in green. You can step through execution of your code using the Step Over (（原归档配图未能恢复：`IB_Debug_StepOver_2x.png`）), Step Into (（原归档配图获取待重试：`IB_Debug_StepInto_2x.png`）), and Step Out (（原归档配图未能恢复：`IB_Debug_StepOut_2x.png`）) buttons located in the bar at the top of the debug area. Step over will execute the current line of code, including any methods. If the current line of code calls a method, step into starts execution at the current line, and then stops when it reaches the first line of the called method. Step out executes the rest of the current method or function.

### Viewing State Information

When execution pauses, the debug navigator opens to display a stack trace. Select an item in the debug navigator to view information about the item in the editor area and in the debug area. As you debug, expand or collapse threads to show or hide stack frames.

（原归档配图获取待重试：`DebugNavigator_2x.png`）

Hover over any variable in the source code editor to see a data tip displaying the value for the variable. Click the Inspector icon (（原归档配图未能恢复：`QuickLookInspectorIcon_2x.png`）) next to the variable to print the Objective-C description of the object to the debug area console and to display that description in an additional popover.

（原归档配图获取待重试：`DataTipInspector_2x.png`）

Click the Quick Look icon (（原归档配图未能恢复：`QuickLookVarIcon_2x.png`）) to see a graphical display of the variable’s contents. You can implement a custom Quick Look display for your own objects. See _[Quick Look for Custom Types in the Xcode Debugger](../../IDEs/Quick%20Look%20for%20Custom%20Types%20in%20the%20Xcode%20Debugger/About%20Variables%20Quick%20Look%20for%20Custom%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dambr)_.

（原归档配图未能恢复：`DataTipQuickLook_2x.png`）

### Finding Memory Corruption

Memory corruption crashes can be hard to reproduce and even harder to find. Address sanitizer adds instrumentation to your app that enables Xcode to stop your app where the corruption happens. Address sanitizer finds problems such as accessing deallocated pointers, buffer overflow and underflow of the heap and stack, and other memory issues.

（原归档配图未能恢复：`Address_Sanitizer_2x.png`）

To use address sanitizer, enable it in the debug scheme for your target, then run and use the app. Xcode monitors memory use and stops your app on the line of code causing the problem and opens the debugger. Use the debugger to isolate the cause.

（原归档配图未能恢复：`Address_Sanitizer_enable_2x.png`）

For more information on using address sanitizer, see [Using the Address Sanitizer](../../Developer%20Tools/Debugging%20with%20Xcode/Specialized%20Debugging%20Workflows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tamrsfvbuqojnknltemy)

### Debugging Metal

Metal takes full advantage of modern GPUs so your apps can give the best user experience. You can use Metal to accelerate both graphics and computation, all using a streamlined API. For information on debugging Metal, see [Metal Tips and Techniques](../../Miscellaneous/Metal%20Programming%20Guide/Metal%20Tools.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqoa). For general information, see [Metal for Developers](https://developer.apple.com/metal/) on the developer website and _[Metal Programming Guide](../../Miscellaneous/Metal%20Programming%20Guide/About%20Metal%20and%20This%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrr)_.

### Debugging OpenGL

When you build and run an OpenGL ES app on a connected device, the debug area toolbar includes a Frame Capture button (（原归档配图未能恢复：`CaptureFramebutton.png`）). Click that button to capture a frame. You can use OpenGL ES frame capture to:

- Inspect OpenGL ES state information
- Introspect OpenGL ES objects such as view textures and shaders
- Step through the state calls that precede each draw call and watch the changes with each call
- Step through draw calls to see exactly how the image is constructed
- See in the assistant editor which objects are used by each draw call
- Edit shaders to see the effect upon your app

The screenshot shows the use of the debugger to view components of a rendered frame. The debug navigator on the left shows parts of the rendering tree, and the main debug view shows the color and depth sources for the rendered frame as well as other image sources.

（原归档配图获取待重试：`gputrace-after_2x.png`）

For more help debugging OpenGL ES, see related items in [Xcode Help](https://help.apple.com/xcode) and [Xcode Help](https://help.apple.com/xcode).

[Managing Schemes](ManagingSchemes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnjwfvjvomi)

[Examining the View Hierarchy](ExaminingtheViewHierarchy.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnjyfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](ExaminingtheViewHierarchy.md)[Previous](ManagingSchemes.md)
