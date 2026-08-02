---
title: Interface Builder User Guide
apple_id: TP40005344
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/IB_UserGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:25:01.102081Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Interface%20Builder%20Quick%20Start.md)

# Introduction

Interface Builder is a visual design tool you use to create the user interfaces of your iOS and Mac OS X applications. Using the graphical environment of Interface Builder, you assemble windows, views, controls, menus, and other elements from a library of configurable objects. You arrange these items, set their attributes, establish connections between them, and then save them in a special type of resource file, called a _nib file_. (The term “nib” is historical and is an acronym for “NextSTEP Interface Builder.“) A nib file stores your objects, including their configuration and layout information, in a format that at runtime can be used to recreate the actual objects.

This document discusses the features of Interface Builder 3.2 and also describes the nib file design process. User interface designers should read this document to learn how to use Interface Builder to create the desired look of their application. Programmers should also read this document to understand what program-level information needs to be created in Xcode.

This document contains the following chapters:

- [Interface Builder Quick Start](Interface%20Builder%20Quick%20Start.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmrsfvjvomi) gives you a quick tour of Interface Builder, including a hands-on tutorial.
- [Interface Builder Basic Concepts](Interface%20Builder%20Basic%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmznknltc) provides an overview of Interface Builder and the role of nib files in your applications.
- [Xcode Integration](Xcode%20Integration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmjyfvjvomi) provides an overview of how nib files integrate with your Xcode projects.
- [Nib File Management](Nib%20File%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmjrfvjvomi) shows you how to create and save nib files and how to work with them in your projects.
- [Nib Objects](Nib%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmjsfvjvomi) describes the types of objects you can add to nib files and when you might want to do so.
- [Interface Layout](Interface%20Layout.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmjzfvjvomi) describes techniques for organizing window and view hierarchies and for adjusting the layout of individual objects.
- [Object Attributes](Object%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmrqfvjvomi) describes the techniques for configuring the objects in your nib file with custom attributes.
- [Connections and Bindings](Connections%20and%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqnznknltc) describes the role of connections in nib files and how to configure outlets, actions, and bindings.
- [Testing and Validation](Testing%20and%20Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmrrfvjvomi) describes the tools available for testing your nib file contents and ensuring your nib file works properly with your Xcode project.
- [Localization](Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmjtfvjvomi) describes the tools and processes for localizing the contents of a nib file.
- [Interface Builder Customization](Interface%20Builder%20Customization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmjwfvjvomi) describes the ways in which you can change the Interface Builder environment to suit your personal tastes.
- [Interface Builder Gesture Guide](Interface%20Builder%20Gesture%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmrtfvjvomi) summarizes the keyboard and mouse actions you can use to make connections, execute commands, and so on.

The Glossary at the end contains a list of Interface Builder terms and their definitions.

Although sometimes thought of as a tool for designing Cocoa application interfaces, Interface Builder lets you create nib files for both Objective-C and C-based applications in iOS and Mac OS X. All developers can take advantage of Interface Builder’s visual environment for assembling, laying out, and configuring windows and menus. If you are developing applications based on the AppKit or UIKit frameworks, you can also use Interface Builder to interconnect the objects in your nib file and application to facilitate the passing of messages. These connections reduce the amount of code that you need to write and, because they are made using Interface Builder, are easy to change later.

Interface Builder’s support for Cocoa in Mac OS X extends beyond just the Objective-C language. You can also use the Cocoa scripting bridge support to create interfaces for applications written using the Ruby or Python scripting languages. For more information about Interface Builder’s support for these languages, see [Interface Builder Documents](Interface%20Builder%20Basic%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmznknltcmi).

Most of the chapters in this book cover features that are common to the development of all types of applications. Chapters and sections that are specific to one development environment or another are called out as such.

Apple provides a comprehensive suite of developer tools (including Interface Builder) for creating iOS and Mac OS X software. The Xcode tools include applications to help you design, create, debug, and optimize your software. This suite also includes header files, sample code, and documentation for Apple technologies. You can download Xcode from the members area of the Apple Developer Connection (ADC) website ([http://connect.apple.com/](http://connect.apple.com/)). Registration is required but free.

If you encounter bugs in Apple software or documentation, you are encouraged to report them to Apple. You can also file enhancement requests to indicate features you would like to see in future revisions of a product or document. To file bugs or enhancement requests, go to the Bug Reporting page of the ADC website, which is at the following URL:

[http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/)

You must have a valid ADC login name and password to file bugs. You can obtain a login name for free by following the instructions found on the Bug Reporting page.

For information on how to use nib files at runtime, including how to load them from your code, see _[Resource Programming Guide](../../Cocoa/Resource%20Programming%20Guide/About%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2i)_.

[Next](Interface%20Builder%20Quick%20Start.md)

