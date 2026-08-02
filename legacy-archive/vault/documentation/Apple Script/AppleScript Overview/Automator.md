---
title: AppleScript Overview
apple_id: 10000156i
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptX/Concepts/automator.html
archived_at: '2026-07-15T05:19:33.998024Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Overview](Introduction%20to%20AppleScript%20Overview.md)


[Next](AppleScript%20Utilities%20and%20Applications.md)[Previous](Scripting%20Bridge.md)

# Automator

Automator is a workflow automation application, first available in OS X version 10.4. Automator, which is located in `/Applications`, lets you create complex workflows using a graphical interface that does not require any knowledge of scripting languages. A workflow consists of one or more actions, executed sequentially, with each action typically taking the output of the previous action as its input. An action performs a distinct operation, such as copying a file, cropping a photo, or sending an email message. You can run a workflow in Automator or save it as a standalone application.

Starting in OS X version 10.5, you can also embed and execute Automator workflows in your application.

Automator includes actions for many Apple applications, including Finder, Mail, Safari, Xcode, iPhoto, iTunes, and QuickTime Player, and you can write actions that make features of your applications available in Automator. You use Xcode and Interface Builder to put together actions, using the Action project template (also available starting in OS X v10.4). Actions are implemented as plug-ins and you can write them using AppleScript (for scriptable applications) or Objective-C.

For information on using the Automator application, choose Help in Automator or Help > Mac Help in the Finder and search for “Automator”. For information on creating actions, see _[Automator Programming Guide](../../Apple%20Applications/Automator%20Programming%20Guide/Introduction%20to%20Automator%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinjq)_ and _[Automator Framework Reference](https://developer.apple.com/documentation/automator)_. For information on using workflows in your application, see _[Automation Release Notes for OS X v10.7](https://developer.apple.com/library/archive/releasenotes/AppleApplications/RN-Automator/index.html#//apple_ref/doc/uid/TP40001840)_, as well as the class descriptions for [AMWorkflow](https://developer.apple.com/documentation/automator/amworkflow), [AMWorkflowView](https://developer.apple.com/documentation/automator/amworkflowview), and [AMWorkflowController](https://developer.apple.com/documentation/automator/amworkflowcontroller) in _[Automator Framework Reference](https://developer.apple.com/documentation/automator)_

[Next](AppleScript%20Utilities%20and%20Applications.md)[Previous](Scripting%20Bridge.md)

