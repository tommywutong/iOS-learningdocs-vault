---
title: Interface Builder
apple_id: 10000179i
resource_type: Guide
platform: Xcode Developer Tools|macOS
topic: null
technology: InterfaceBuilderKit
published: '2007-04-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/IBTips/IBTips.html
archived_at: '2026-07-15T07:24:39.148966Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Compatibility%20Checking.md)

# Introduction to Interface Builder

Interface Builder 2.5 was the Xcode application used to create graphical user interfaces (GUIs) prior to Mac OS X v10.5. This programming topic provides some tips to help you make more effective use of this application and gives pointers to other documentation for Interface Builder.

Before you read this document, you should have basic familiarity with Interface Builder 2.5 and with the Xcode application. This document should be useful to anyone using Interface Builder, no matter whether you are writing Carbon, Cocoa, Java, or AppleScript applications.

This topic consists of several articles and is supplemented by a variety of other documentation as described here.

- [Compatibility Checking](Compatibility%20Checking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4tslkdjbeemskfirda) describes how to make sure your project does not use any interface elements that are not supported by the target version of Mac OS X.
- [Cocoa Custom Views](Cocoa%20Custom%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgeydalkcifbesq2iindq) explains how to use the Custom View widget in Cocoa applications and describes what you can do with a custom view.
- [Making Connections in Cocoa Applications](Making%20Connections%20in%20Cocoa%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgeydclkdjjaugrsijbcq) explains how to make connections between elements of your Cocoa application’s user interface, including widgets, controllers, menus, the Files Owner, and the First Responder. This article also explains the roles of actions and outlets, and tells you where you have to add your own code to make the connections work.
- [Frequently Asked Questions](Frequently%20Asked%20Questions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgeydelkcifbesq2kjjbq) lists a number of questions users have had about Interface Builder and gives brief answers to them.

In Interface Builder, use the Help menu to open Interface Builder online help and release notes. When you install the Xcode tools on your system, the Interface Builder online help is also available in /Developer/Applications/Interface Builder.app/Contents/Resources/English.lproj/InterfaceBuilder_Help.

Developing Cocoa Objective-C Applications: A Tutorial in Cocoa Objective-C Language Documentation shows the development of a simple application using Objective-C and Cocoa and illustrates the use of Interface Builder.

[A Quick Tour of Xcode](../A%20Tour%20of%20Xcode/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqojq) in [Tools Documentation](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000436) includes a tutorial that shows the development of a simple application using Objective-C and Carbon and that illustrates the use of Interface Builder.

Developing Cocoa Java Applications: A Tutorial in Cocoa Java Documentation shows the development of a simple application using Java and Cocoa and illustrates the use of Interface Builder.

Building a Text Editor in 15 Minutes in the Cocoa programming topic Text System Architecture in [Cocoa Text & International Documentation](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000416-TP30000461) shows how to use Interface Builder to add a text view to a window, write a simple controller, and connect the text view to the controller.

_[Resource Programming Guide](../../Cocoa/Resource%20Programming%20Guide/About%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2i)_ provides information about nib files in the runtime environment, including information about the nib-loading process for Carbon and Cocoa applications.

_Interface Builder Services Reference_ in Carbon User Experience Documentation describes the Interface Builder Services manager. This manager provides functions that unarchive interface objects from nib files created using Interface Builder.

_Unarchiving Interface Objects With Interface Builder Services_ in Carbon User Experience Documentation discusses key concepts needed to understand Interface Builder Services and strategies for storing interface objects. This topic also shows you how to unarchive interface objects from a main file, auxilliary nib files, and bundles other than the main bundle.

_Handling Carbon Windows and Controls_ in Carbon User Experience Documentation has a section on Using Interface Builder in the chapter “Window and Control Tasks.” Although geared to Carbon programmers, many of the principles and techniques described here apply to any project that uses Interface Builder.

[Controller Layer](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html#//apple_ref/doc/uid/10000167) in Cocoa Design Guidelines Documentation describes the purpose and use of controller objects and includes tutorials that show how you use Interface Builder to add controller objects to your Cocoa application.

[Building Applications With AppleScript Studio](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/StudioBuildingApps/chapter01/studio_intro_book.html#//apple_ref/doc/uid/20001248) in AppleScript Documentation has a section on Interface Builder Features for AppleScript Studio in the chapter “AppleScript Studio Components.” This document also includes two tutorials with sections that illustrate the use of Interface Builder: “Currency Converter” and “Mail Search.”

[Next](Compatibility%20Checking.md)

