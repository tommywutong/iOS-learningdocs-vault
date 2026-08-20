---
title: AppleScript Overview
apple_id: 10000156i
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptX/Concepts/scripting_bridge.html
archived_at: '2026-07-15T05:19:35.998455Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Overview](Introduction%20to%20AppleScript%20Overview.md)


[Next](Automator.md)[Previous](Scriptable%20Applications.md)

# Scripting Bridge

Scripting Bridge, introduced in OS X version 10.5, provides an automated process for creating an Objective-C interface to scriptable applications. This allows Cocoa applications and other Objective-C code to efficiently access features of scriptable applications, using native Objective-C syntax. Some other scripting languages, such as Ruby and Python, can use also Scripting Bridge (they also have open-source software bridges to scriptable applications—RubyOSA and py-appscript). For more information, see _[Ruby and Python Programming Topics for Mac](../../Cocoa/Ruby%20and%20Python%20Programming%20Topics%20for%20Mac/Introduction%20to%20Ruby%20and%20Python%20Programming%20Topics%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzw)_.

To use Scripting Bridge, you add the Scripting Bridge framework to your application project and use command-line tools to generate the interface files for the scriptable application you want to target. Then in your application code, you obtain a reference to an application object for the targeted scriptable application and send Objective-C messages to it.

For details, see _[Scripting Bridge Programming Guide](../../Cocoa/Scripting%20Bridge%20Programming%20Guide/Introduction%20to%20Scripting%20Bridge%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbu)_ and _[Scripting Bridge Framework Reference](https://developer.apple.com/documentation/scriptingbridge)_. For related sample code, see _[ScriptingBridgeFinder](../../../samplecode/ScriptingBridgeFinder/ScriptingBridgeFinder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrygm)_.

[Next](Automator.md)[Previous](Scriptable%20Applications.md)

