---
title: AppleScript Overview
apple_id: 10000156i
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptX/Concepts/scriptable_apps.html
archived_at: '2026-07-15T05:19:35.529035Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Overview](Introduction%20to%20AppleScript%20Overview.md)


[Next](Scripting%20Bridge.md)[Previous](Scripting%20with%20AppleScript.md)

# Scriptable Applications

A _scriptable application_ is one that goes beyond the basics of responding to Apple events sent by the Mac OS to make its most important data and operations available to AppleScript scripts or to other applications. To do this, the application must provide both a terminology for scripters to use and the underlying Apple event code to support it. Both Carbon and Cocoa applications can be scriptable, and the Cocoa framework contains built-in support that minimizes the amount of code you have to write.

Scriptable applications describe the scripting terminology they support by supplying a scripting dictionary. A dictionary specifies the commands and objects an application supports, as well as other information that is used by AppleScript or the application itself, and possibly by other applications or scripts that want to take advantage of the application’s scriptability. For information on designing a scripting terminology, see Technical Note TN2106, [Scripting Interface Guidelines](https://developer.apple.com/technotes/tn2002/tn2106.html).

Users typically examine a dictionary for information on how to control an application in their scripts. You can display the dictionary for a scriptable application or scripting addition with Script Editor, as described in [Displaying Scripting Dictionaries](Scripting%20with%20AppleScript.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknryfuytcnjtgaydm).

There are currently three dictionary formats:

- _sdef:_ “sdef” is short for “scripting definition.” This XML-based format is a superset of the two formats described next and supports new and improved features. Although prior to OS X version 10.4, you could not use an sdef directly in your application, you could convert an sdef into either of the other formats with the `sdp` tool. Starting in OS X v10.4, Cocoa applications can work natively with the sdef format, as described in [Preparing a Scripting Definition File](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_creating_sdef/SAppsCreateSdef.html#//apple_ref/doc/uid/TP40001979) and other chapters in _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_.

  In OS X v10.5 (Leopard), it’s possible to create applications that provide dictionary information solely in sdef format, both for Carbon and Cocoa applications. You can read about additional refinements to sdef usage in Cocoa applications for Leopard in the Scripting section of _[Foundation Release Notes for macOS 10.13 and iOS 11](../../../releasenotes/Foundation/Foundation%20Release%20Notes%20for%20macOS%2010.13%20and%20iOS%2011.md)_.

  For documentation on the sdef format, including a change history, see the `sdef`(5) man page. [Scripting Interface Guidelines](https://developer.apple.com/technotes/tn2002/tn2106.html) also includes information on working with sdefs. For documentation on the `sdp` tool, see the man page for `sdp`(1), as well as [Evolution of Cocoa Scriptability Information](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_evolution/SAppsEvolution.html#//apple_ref/doc/uid/TP40002164-CH19) in _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_. For an example of how to use an sdef file, see the Sketch sample application. For other examples, see the sample code projects listed in [Support for Cocoa Applications](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknrzfuytcnjrgu3do).
- _script suite:_ This is the original format used by Cocoa applications and it is still supported for backward compatibility. A script suite contains a pair of information property list (plist) files that provide both AppleScript information and information used by the application. An application can contain multiple script suites.

  For documentation, see [Script Suite and Script Terminology Files](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_suites/SAppsSuites.html#//apple_ref/doc/uid/20001241) in _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_.
- _aete:_ This is the original dictionary format, and is still used in Carbon applications. The name comes from the Resource Manager resource type in which the information is stored (`'aete'`). An aete is useful in 10.4 and earlier, in both Carbon and Cocoa applications, to provide a dictionary that scripting languages can use without launching the application.

In designing a scriptable application, it’s a good idea to provide access to all of the application’s main features, though it may make sense to start with just a key subset. You don’t typically make your application’s user interface directly scriptable. A good design allows users to script your application’s model objects (which represent data and basic behaviors) rather than its user interface (which presents information to the user).

For example, the scripting support for a drawing application might allow a script to rotate an image, but not to perform the user interface operation of clicking a Rotate button. Some applications provide additional capabilities through their scripting interface that aren’t otherwise available.

For design information, see “Learning How to Make an Application Scriptable” in _Getting Started with AppleScript_ and Technical Note TN2106, [Scripting Interface Guidelines](https://developer.apple.com/technotes/tn2002/tn2106.html).

For information on how to support printing in a scriptable application, see _[The Enhanced Print Apple Event](https://developer.apple.com/library/archive/technotes/tn2002/tn2082.html#//apple_ref/doc/uid/DTS10003113)_.

A scriptable application typically responds to a set of common commands, such as `get data`, `set data`, `delete`, and `save`, as well as to other commands that support operations specific to the application. Commands are represented in Apple events by constants defined in framework or application headers. To support a command, an application registers an event handler routine with the Apple Event Manager to handle Apple events it receives that specify that command. The Apple Event Manager dispatches received events to the handlers registered for them.

For more information on creating and registering event handlers, see [Apple Event Dispatching](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/dispatch_aes_aepg/dispatch_aes_aepg.html#//apple_ref/doc/uid/TP40001449-CH204) and [Responding to Apple Events](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/responding_aepg/responding_aepg.html#//apple_ref/doc/uid/TP40001449-CH206) in _[Apple Events Programming Guide](../Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_.

Apple events often specify items in the application. For example, a `get data` event might ask for the text of a paragraph in an open document. A distinct item in an application that can be specified in an Apple event is known as an _Apple event object_. (The term object does not imply that the items must be represented internally as objects in an object-oriented programming language.) All such objects are considered to be contained in other objects, with the application itself serving as the ultimate container. For a given application, the _AppleScript object model_ (also called the Apple event object model) specifies the classes of objects a scripter can work with in scripts, the accessible properties of those objects, and the inheritance and containment relationships for those objects.

The structures within an Apple event that identify objects are referred to as _object specifiers_. Finding the Apple event objects they specify is known as resolving the object specifiers. To resolve object specifiers, an application must include functions that are able to find objects within their containers. The application registers these functions with the Apple Event Manager, and works with the Apple Event Manager to call them at the appropriate time to obtain the objects they specify.

For Cocoa applications, Cocoa scripting support does much of the work of resolving object specifiers, but a scriptable application must still supply methods that can locate an object within its object model containment hierarchy.

For an example of an AppleScript object model, see [Overview of Cocoa Support for Scriptable Applications](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_about_apps/SAppsAboutApps.html#//apple_ref/doc/uid/TP40001976); for information on how Cocoa applications resolve objects, see [Object Specifiers](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_object_specifiers/SAppsObjectSpecifiers.html#//apple_ref/doc/uid/TP40002164-CH3); both are in _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_.

A recordable application is one that sends Apple events to itself when a user performs actions with the application. If the user has turned on recording in the Script Editor application (with Script > Record), actions that generate Apple events are recorded into an AppleScript script.

Applications that support recording typically:

- Factor code that implements the user interface from code that actually performs operations (a standard approach for applications that follow the model-view-controller design paradigm).
- Send Apple events within the application to connect those two parts of the application. The Apple Event Manager provides a mechanism for doing this with a minimum of overhead, described in “Addressing an Apple Event for Direct Dispatching” in [Creating and Sending Apple Events](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/create_send_aepg/create_send_aepg.html#//apple_ref/doc/uid/TP40001449-CH209) in _[Apple Events Programming Guide](../Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_.
- Make sure that any significant action or series of related actions within the application generates an Apple event.

The Finder application in OS X is recordable. Starting in OS X version 10.5, the [Automator](Automator.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinrzfvjvomi) application has a separate Record mechanism that lets users record actions into an Automator workflow.

An application can create and send Apple events directly. This is usually done either to send internal Apple events, as described in [Recording](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknzrfuytcnjtha4dq), to obtain services from a scriptable application, or to communicate directly with another application. The Open Scripting Architecture provides various mechanisms for creating and sending Apple events.

Starting in OS X version 10.5, applications can use [Scripting Bridge](Scripting%20Bridge.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinrxfvjvomi) to obtain services from scriptable applications. Scripting Bridge lets you work efficiently in a high-level language (Objective-C) without having to handle the details of sending and receiving Apple events. (See also [Support for Cocoa Applications](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknrzfuytcnjrgu3do) for related information.)

When you really do need to send an Apple event directly, see [Building an Apple Event](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/building_aes_aepg/building_aes_aepg.html#//apple_ref/doc/uid/TP40001449-CH203) and [Creating and Sending Apple Events](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/create_send_aepg/create_send_aepg.html#//apple_ref/doc/uid/TP40001449-CH209) in _[Apple Events Programming Guide](../Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_.

To execute scripts, an application establishes a connection with the AppleScript scripting component. It can then:

- Use the standard scripting component routines to manipulate scripts associated with any part of the application or its documents.
- Let users record and edit scripts.
- Compile and execute scripts.

An application can store and execute scripts regardless of whether it is scriptable or recordable. If an application is scriptable, however, it can execute scripts that control its own behavior, thus acting as both the client application and the server application for the corresponding Apple events. For more information, see _Open Scripting Architecture Reference_.

In Cocoa, the `NSAppleScript` class, described in _[NSAppleScript Class Reference](https://developer.apple.com/documentation/foundation/nsapplescript)_, provides a high-level wrapper for executing AppleScript scripts from applications. For more information, see [Support for Cocoa Applications](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknrzfuytcnjrgu3do).

The following list summarizes how scriptable applications interact with the Open Scripting Architecture to make their features available to scripters.

- The Apple Event Manager defines data structures that are used to construct Apple events.
- The Open Scripting Architecture (OSA) provides a data transport and event dispatching mechanism for Apple events, built on top of lower level protocols.
- AppleScript defines a scripting language, described in [AppleScript Language Guide](https://developer.apple.com/documentation/AppleScript/Conceptual/AppleScriptLangGuide/index.html) (and third-party books) and implemented by the AppleScript component in OS X.
- There is a small set of Apple events sent by the Mac OS, such as `open application`, `quit`, and `open documents` that all applications should be able to respond to. A scriptable application responds to additional common events, such as `get data` and `set data`, as well as to its own specific commands.
- A scriptable application provides a scripting terminology (or dictionary) for the operations it supports. The application can reuse some event constants defined by the OSA or use its own for custom events. (Constants defined by Apple, many of which you can reuse in your applications, are described in _[AppleScript Terminology and Apple Event Codes Reference](https://developer.apple.com/library/archive/releasenotes/AppleScript/ASTerminology_AppleEventCodes/TermsAndCodes.html#//apple_ref/doc/uid/TP40004532)_.)

  The sdef file format provides a mechanism for creating one terminology definition that can be converted for use in different environments.
- Developers design their applications so that key operations can be invoked in response to received Apple events.
- A scriptable application works with the Apple Event Manager to:

  - Register handlers for Apple events it can process.
  - Extract information from received Apple events, then perform requested operations or return requested data.
  - Construct Apple events for replies or other purposes.

  Scriptable Carbon applications work with the Apple Event Manager directly, but for scriptable Cocoa applications, much of this work is handled automatically.
- Scripters write AppleScript scripts that specify scriptable applications and the operations to perform.
- When a script is executed, script statements that target applications are translated by the AppleScript component into Apple events that are sent to those applications.

  Applications can also send Apple events directly to other applications.
- An application responds to the Apple events it receives by performing operations, returning data, or both.

OS X supplies a number of resources that applications can use to work with Apple events and to support scriptability, including the API provided in the following frameworks:

- The underlying support in OS X for creating scriptable applications and working with Apple events is provided by the Open Scripting Architecture, and is described in [The Parts of the Open Scripting Architecture](Open%20Scripting%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknzrfuytcnbxha2ts).
- The _Cocoa framework_ (`Cocoa.framework`) includes the Application Kit and Foundation frameworks, which together provide the building blocks for sophisticated Mac apps. The Cocoa framework includes a great deal of support for creating scriptable applications.

  For specific Cocoa scripting documentation, see _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_.
- Java applications are not typically scriptable, though they can be made AppleScript-aware using the mechanisms described in [OS X Integration for Java](https://developer.apple.com/library/archive/documentation/Java/Conceptual/Java14Development/07-NativePlatformIntegration/NativePlatformIntegration.html#//apple_ref/doc/uid/TP40001909) in _[Java Development Guide for Mac](../../Java/Java%20Development%20Guide%20for%20Mac/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbs)_.

Carbon applications have traditionally worked directly with the Apple Event Manager to create, send, receive, and interpret Apple events. These topics are described in detail in _[Apple Events Programming Guide](../Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_.

For information on making your Carbon application scriptable, see previous sections in this chapter, as well as the learning paths in _Getting Started with AppleScript_.

Carbon applications can use functions such as `OSACompile` and `OSAExecute` from `OpenScripting.framework` to compile and execute scripts. Keep in mind, however, that if you are executing a script merely to send a simple command to another application, it is more efficient to create and send an Apple event directly.

If the purpose for executing a script is just to perform a `do shell script` command, Carbon applications can do so more efficiently using one of the BSD calls `system(3)`, `popen(3)`, or `exec(3)`, which you can read about at their respective man pages.

The Foundation and Application Kit frameworks provide Cocoa applications with automated handling for certain Apple events. This includes events that may be sent by the Mac OS, such as the `open application`, `open documents`, `print documents`, and `quit` Apple events.

In addition, Cocoa provides substantial support for creating scriptable applications. To take advantage of it, applications provide scriptability information in one of the formats described in [Specifying Scripting Terminology](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknrzfuytcnjwge3dk). They also create KVC-compliant accessors for scriptable properties in their scriptable classes. (Key-value coding, or KVC, is described in _[Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_.) Though creating a fully scriptable application is a non-trivial task, an application can support many standard AppleScript commands, such as those for getting and setting properties of application objects, with a relatively small number of additional steps.

Cocoa applications can also use any of the Open Scripting Architecture APIs available to Carbon applications, and in fact, Cocoa links with the Carbon framework. For example, a Cocoa Application might call an Apple Event Manager function to send an Apple event directly (there currently is no Cocoa API to do that).

Starting in OS X version 10.5, the [Scripting Bridge](Scripting%20Bridge.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinrxfvjvomi) technology provides an efficient way for Cocoa applications to interact with scriptable applications at a high level—that is, without having to construct or parse individual Apple events.

Cocoa provides the [NSAppleScript](https://developer.apple.com/documentation/foundation/nsapplescript) class for tasks such as compiling and executing scripts. This gives applications another mechanism to control scriptable applications and take advantage of services they provide. However, you should not use `NSAppleScript` to execute a script merely to result in sending an Apple event, because it is far more expensive than using Scripting Bridge or creating and sending an Apple event directly. And if the purpose for executing a script is to perform a `do shell script` command, Cocoa applications can execute shell commands more efficiently using [NSTask](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/cl/NSTask).

The Cocoa framework also includes classes such as [NSAppleEventDescriptor](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor), for working with underlying Apple event data structures, and [NSAppleEventManager](https://developer.apple.com/documentation/foundation/nsappleeventmanager), for accessing certain Apple Event Manager functions.

Cocoa support for handling Apple events and creating scriptable applications is documented in _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_. For related information, see “Framework and Language Support” in [About Apple Events](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleEvents/about_aes_aepg/about_aes_aepg.html#//apple_ref/doc/uid/TP40001449-CH202) in _[Apple Events Programming Guide](../Apple%20Events%20Programming%20Guide/Introduction%20to%20Apple%20Events%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbz)_. For introductory sample code, see _[SimpleScripting](../../../samplecode/SimpleScripting/SimpleScripting.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrtha)_, _[SimpleScriptingProperties](../../../samplecode/SimpleScriptingProperties/SimpleScriptingProperties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimruga)_, _[SimpleScriptingObjects](../../../samplecode/SimpleScriptingObjects/SimpleScriptingObjects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrugq)_, and _[SimpleScriptingVerbs](../../../samplecode/SimpleScriptingVerbs/SimpleScriptingVerbs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrthe)_. For a more complex example, see the Sketch sample application.

[Next](Scripting%20Bridge.md)[Previous](Scripting%20with%20AppleScript.md)

