---
title: Automator Programming Guide
apple_id: TP40001450
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: Automator
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/AutomatorConcepts/Automator.html
archived_at: '2026-07-15T05:16:49.748598Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Automator%20and%20the%20Developer.md)

# Introduction to Automator Programming Guide

Automator is an application from Apple that automates repetitive procedures performed on a computer. With Automator users can construct arbitrarily complex workflows from modular units called actions. An action performs a discrete task, such as opening a file, cropping an image, or sending a message. A workflow is a number of actions in a particular sequence; when the workflow executes, data is piped from one action to the next until the desired result is achieved.

Apple includes a suite of ready-made actions with Automator, but developers are encouraged to contribute their own actions. You can create actions—which are implemented as loadable bundles—using either AppleScript, Objective-C, or a combination of the two languages. You can also create actions using shell scripts or other scripting languages such as Perl and Python.

Automator was introduced in OS X version 10.4. It does not run on earlier systems. The development features of Automator were introduced with Xcode 2.0. Additional development features have been added in Xcode 2.1. This document notes these newer features when it mentions them.

Any developer can create actions for Automator, as indeed can system administrators or “power users” who are familiar with AppleScript. But application developers have a particular motivation for developing actions. They can create actions that access the features of their applications, and then install these actions along with their applications. Users of Automator can then become aware of the applications and what they have to offer.

Developers can also contribute to Automator by making their applications scriptable or by providing a programmatic interface (via a framework) that developers use to create their actions.

_Automator Programming Guide_ consists of the following articles:

- [Automator and the Developer](Automator%20and%20the%20Developer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmbyfvbegskkifdeqsa) describes what Automator can do and discusses the characteristics and types of actions,
- [How Automator Works](How%20Automator%20Works.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmbzfvbecssjizcesri) gives an overview of the loadable-bundle architecture of Automator and the Objective-C classes of the Automator framework.
- [Design Guidelines for Actions](Design%20Guidelines%20for%20Actions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjqfvbecsseirfecqq) lists guidelines for action development, including recommendations regarding I/O, naming, and the user interface.
- [Developing an Action](Developing%20an%20Action.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjrfvbecsscjfbuosa) guides you through the major steps required to develop an action.
- [Show When Run](Show%20When%20Run.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytknrxfvbecssfi5eeurq) describes the Show When Run feature of actions and explains how you can customize it.
- [Implementing an AppleScript Action](Implementing%20an%20AppleScript%20Action.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjsfvbuuqskivfeeri) states the requirements for developing an action using AppleScript, suggests approaches you might take, and discusses hybrid actions—that is, actions based on both AppleScript and Objective-C code.
- [Implementing an Objective-C Action](Implementing%20an%20Objective-C%20Action.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjtfvbegskdincugqy) explains how to create an action implemented with Objective-C code.
- [Creating Shell Script Actions](Creating%20Shell%20Script%20Actions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanzyfvbegskcifcucqy) describes the steps required to create an action using a shell script or a scripting language such as Perl or Python.
- [Creating a Conversion Action](Creating%20a%20Conversion%20Action.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjufvbeeq2kivauqsi) describes what is required to create actions whose only purpose is to convert between types of input and output data.
- [Defining Your Own Data Types](Defining%20Your%20Own%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjtfvjvomjq) discusses custom data types and explains when and how you should define them.
- [Automator Action Property Reference](Automator%20Action%20Property%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmjvfvbegskkjbbeuqy) defines the types and expected values for the Automator properties specified in an action’s information property list (`Info.plist`).

- [Automator Framework Reference](https://developer.apple.com/documentation/AppleApplications/Reference/AutomatorReference/index.html?http://developer.apple.com/documentation/AppleApplications/Reference/AutomatorReference/AutomatorReference.html) provides an overview of the reference material available for developing with Automator, with links to specific class reference and constants documents.
- [Automator Constants Reference](https://developer.apple.com/documentation/AppleApplications/Reference/Automator_constants/index.html#//apple_ref/doc/uid/TP40004647) describes Automator programming constants.
- _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_ presents an overview of the Xcode integrated development environment.
- _[AppleScript Overview](../../Apple%20Script/AppleScript%20Overview/Introduction%20to%20AppleScript%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tm2i)_ introduces the technology for creating and controlling scriptable applications.
- _[The Objective-C Programming Language](../../Cocoa/The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_ describes the Objective-C programming language and how you use it to create object-oriented programs.
- _[Cocoa Bindings Programming Topics](../../Cocoa/Cocoa%20Bindings%20Programming%20Topics/Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3do2i)_ discusses the Cocoa bindings mechanism and how you can incorporate it in your programs.
[Next](Automator%20and%20the%20Developer.md)

