---
title: A Tour of Xcode
apple_id: TP30000890
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-01-21'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/A_Tour_of_Xcode/030-Recommended_Reading/Resources.html
archived_at: '2026-07-15T07:24:15.420404Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [A Tour of Xcode](Introduction.md)


[Next](Finding%20and%20Viewing%20Documentation.md)[Previous](Xcode%20Workflow%20Tutorial.md)

# Recommended Reading

The ADC reference libraries contain API reference documentation, programming guides, tutorials, technical Q&As, sample code, and more. As a new Xcode user, the amount of information available can be overwhelming. This chapter points out some of the most important resources for each phase of development—from the design of your software product  to its delivery.

You may want to take a look at these documents before you create an Xcode project and start writing code:

- _Apple Human Interface Guidelines_. Use these guidelines to develop products that provide users with a consistent visual and behavioral experience across applications and the operating system. Make your application intuitive, friendly, and elegant.
- _Document-Based Applications Overview_. Read this overview if you want to create applications such as word processors, spreadsheets, image processors, and sound editors. Using a document-based application users can create identically contained, but uniquely composed, sets of data that can be stored in files.
- _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_. Consider using the Core Data framework if your application stores and accesses data. Using it, you quickly define your application's data model in a graphic way and easily access the data model from your code. Core Data provides an infrastructure to deal with common functionality such as undo and redo and data persistence, allowing you to focus on adding innovative features to your application.

When you are in the coding phase of your product, you might find these resources helpful:

- _[Xcode Workspace Guide](../Xcode%20Workspace%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmrq)_. Read this document to find out how to customize your development environment to suit your work style. You can control the layout of the project window, the workings of the text editor, the content that appears in Quick Help, and many more aspects of the environment.
- _[Xcode Unit Testing Guide](../Xcode%20Unit%20Testing%20Guide/About%20Unit%20Testing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnbt)_. Writing and performing unit tests as you write code can ensure that no errors or bugs are introduced as you make changes and improvements to your application’s functionality. Find out how to use the unit-test environment of Xcode for testing Objective-C and C++ code.
- _[Interface Builder User Guide](../Interface%20Builder%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbu)_. Consult this document for in-depth information on using Apple’s graphical tool to create your application’s user interface. You’ll see how to assemble user interface elements from a library of configurable objects and then connect those objects to your code.
- _[SDK Compatibility Guide](../SDK%20Compatibility%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2i)_. Do you need to develop software that can be deployed on, and take advantage of, features from specific versions of Mac OS X, including versions different from the one you are developing on? If so, consult this guide.

When you are ready to have Xcode translate the source files and the instructions in a target into a product, the following guides and reference might be of value:

- _[Xcode Project Management Guide](../Xcode%20Project%20Management%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmjx)_. Get an orientation to the Xcode build system by reading the [Building Products](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeProjectManagement/210-Building_Products/building.html#//apple_ref/doc/uid/TP40002693) chapter, which describes the most typical building tasks including how to:

  - View and change build settings
  - Build projects with single or multiple targets
  - Create a shared build directory
  - Set per-compiler flags
- _[Xcode Build System Guide](../Xcode%20Build%20System%20Guide%20%282016%29.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsmzr)_. When you want to know more about a particular build setting, you can look up its definition in this document. You’ll see how a target’s build settings affect a build and how each setting relates to other settings.
- _[Xcode Build System Guide](../Xcode%20Build%20System%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmbu)_. Read this for a deep understanding of the Xcode build system and when you need to customize the build process. It describes how to use advanced features such as distributed builds and predictive compilation.

Finding and eliminating bugs in your code is a critical phase of the development process.

- _[Xcode Debugging Guide](../Xcode%20Debugging%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjx)_. Find out how to debug from each of the following:

  - The text editor
  - The mini debugger, which is a small window that’s not too intrusive on the running application
  - The Debugger window, which is a specialized, traditional-style debugging environment
  - The GDB debugger console

Tools that gather performance data can help you to improve your application’s performance.

- _[Instruments User Guide](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/index.html#//apple_ref/doc/uid/TP40004652)_. Learn how to peer into your code as it’s running and gather metrics about what it’s doing. You can view and analyze the data Instruments collects in real time, or you can save that data and analyze it later. You can collect data about your application’s use of the CPU, memory, file system, and the network, among other resources.
- _[Shark User Guide](../Shark%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temzt)_. Track down performance bottlenecks in your code. Use Shark to produce profiles of hardware and software performance events. You can analyze the profiles to get a better understanding of how your code works and interacts with the operating system.

When your product is ready, it’s time to package it for installation on a user’s computer.

- _Software Delivery Guide_. Find out how to deliver software through either manual or managed installations.

[Next](Finding%20and%20Viewing%20Documentation.md)[Previous](Xcode%20Workflow%20Tutorial.md)

