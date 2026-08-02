---
title: Code Loading Programming Topics
apple_id: 10000052i
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingCode/Concepts/Plugins.html
archived_at: '2026-07-15T07:16:28.366633Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Loading Programming Topics](Introduction%20to%20Dynamically%20Loading%20Code.md)


[Next](Loading%20Bundles.md)[Previous](Multi-Bundle%20Applications.md)

# Plug-in Architectures

This section describes how to architect an application for extensibility through plug-ins. If you want to make your application modular, customizable, and easily extensible, you should read this section to learn about the different ways to build a plug-in architecture.

Plug-in architectures are an attractive solution for developers seeking to build applications that are modular, customizable, and easily extensible. What began as a clever way to allow third parties to add features to an application without access to source code has, for many developers, evolved into a full-blown methodology for application development.

Structuring an application as a well-designed host framework and a set of plug-ins gives you many benefits as an application developer:

- You can implement and incorporate application features very quickly.
- Because plug-ins are separate modules with well-defined interfaces, you can quickly isolate and solve problems.
- You can create custom versions of an application without source code modifications.
- Third parties can develop additional features without any effort on the part of the original application developer.
- Plug-in interfaces can be used to wrap legacy code written in different languages.

End-users also benefit from using applications with a plug-in architecture:

- They can customize feature sets to particular workflows.
- They can disable unwanted features, potentially simplifying the application’s user interface, reducing memory footprint, and improving performance.

A _plug-in_ is a bundle that adds functionality to an application, called the _host application_, through some well-defined architecture for extensibility. This allows third-party developers to add functionality to an application without having access to the source code. This also allows users to add new features to an application just by installing a new bundle in the appropriate folder. Screen saver modules, preference panes, and Interface Builder palettes, Adobe Photoshop graphics filters, and iTunes music visualizers are all examples of plug-ins. You use them whenever you want to add multiple instances of a particular type of module that provides a well-defined unit of functionality, such as a new export filter in a graphics program, a new transition style in a video editing program, or other type of feature.

You can think of a host application as a kind of jigsaw puzzle with an infinite number of places to put new pieces. Plug-ins are additional pieces to attach to the puzzle and the plug-in architecture determines the shape of allowable puzzle pieces. If a plug-in has the wrong shape, it can’t join the rest of the puzzle. [Figure 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3teljzha3dqnrnijbegqscivduq) illustrates this metaphor: pieces that fit contribute their functionality to the application; pieces that don’t fit are left dangling on the sidelines.

__Figure 1__  Plug-in architecture as an endless jigsaw puzzle

!

The plug-in architecture typically takes the form either of a list of methods or functions that plug-ins must implement or of a base class that plug-ins must use, but this is not enough. As a host application developer, you must document explicitly not only the form of the plug-in, but also the function, by detailing what type of behavior each method or function must exhibit to behave correctly in the application’s plug-in environment.

Plug-ins are usually loadable bundles with executable code that defines the new functionality for the application. Plug-ins may or may not contain resources—in some instances only code is necessary. In rare cases, a plug-in might add resources but no code—such as the `.slideSaver` modules for the OS X screen saver.

Plug-ins are normally installed in one of several standard locations. You can load them from anywhere, but the OS X API layers include support for finding these standard paths.

The standard paths are as follows (where _applicationSupportDirectory_ is the directory containing your application’s support files):

- ~/`Library/Application Support/`_applicationSupportDirectory_`/PlugIns`
- /`Library/Application Support/`_applicationSupportDirectory_`/PlugIns`
- _applicationBundleDirectory_`/Contents/PlugIns`

If you want your application to support plug-ins, you need to define a plug-in architecture so that third-party developers—or developers internal to your organization—have a well-defined interface to implement. The plug-in architecture is up to the developer. The specific architecture that makes sense depends largely on the application. However, most plug-in architectures share the same basic plan.

In object-oriented languages, application developers define the plug-in architecture—the shape of allowed puzzle pieces—by specifying the requirements for a custom class. These requirements typically take the form of an abstract base class or a list of methods (such as an Objective-C protocol). This custom class, known as the _principal class_, is included as part of the plug-in bundle, along with other support code and resources. When it’s time to load a plug-in, the host application checks to see if it conforms to the requirements. If the piece fits, then the application asks the class—a factory for instances—to generate an instance. If a plug-in doesn’t conform to the architecture, its code is loaded, but the invalid factory never produces an instance.

The C language does not directly support object-oriented concepts, but you can define a plug-in architecture based on entry-point and callback functions for communication with plug-in “objects.” Instead of defining the requirements for a plug-in class, the application developer defines a set of functions for plug-ins to implement, and a mechanism for registering callback functions for different types of messages. The application queries a plug-in to see if it implements the necessary entry-point functions. If it does, the application calls those functions to invoke the plug-in’s capabilities. Within the entry points, the plug-in can register callback functions to respond to other types of messages.

For more sophisticated behavior in Carbon applications, you can use the Core Foundation CFPlugIn opaque type to define an “object-oriented” architecture that works with both C and C++ plug-ins.

You can define an architecture for plug-ins in a number of different ways, each appropriate to different programming environments and plug-in types:

- Define an Objective-C protocol for plug-ins to adopt
- Define an abstract base class for plug-ins to inherit from
- Define C functions for plug-ins to implement and a mechanism for registering callback functions
- Define a plug-in interface with Core Foundation CFPlugIn opaque type

It is easiest to define your plug-in interface in the same language that your application is written in, but this is not necessary. For example, if you are writing an Objective-C Cocoa application, it makes the most sense to use an Objective-C plug-in architecture based on either protocols or base classes. However, you can also provide a C-based architecture for non-Cocoa plug-ins, either with CFPlugIn or with a simple set of predefined callback functions.

If you are writing a truly object-oriented plug-in architecture, you need to decide whether to provide parts of the implementation for plug-ins in a base class or to simply define a set of methods or functions for plug-ins to implement. If plug-ins share a significant amount of functionality, and it would be inconvenient to provide that functionality in the main application code, then using a base class is the best way to go. The OS X screen saver and preference pane architectures both define abstract base classes that provide some basic functionality for plug-ins. Other plug-ins, such as data processing modules, may not require any base functionality and can simply implement a standard set of methods.

The following sections discuss the plug-in models available to Mac apps, and more details on when you should use them.

Objective-C has the notion of an abstract list of methods separate from the class inheritance hierarchy. This lets a developer define a related set of functionality without defining a class or an implementation for the methods. This way, any class can implement the methods, regardless of its place in the inheritance hierarchy. In Objective-C, these lists are called _protocols_. In C++, abstract classes containing only pure virtual functions accomplish essentially the same goal as protocols through a different mechanism.

You can use a protocol to define a plug-in architecture. Plug-in developers then write a class that adopts the protocol and use this class as the plug-in bundle’s principal class. At runtime, the host application can check to see if the plug-in conforms to the protocol before using it.

You should use a protocol for your plug-in architecture when at least one of these three conditions is met:

1. Different plug-ins are unlikely to share much code, so a base class would consist of little more than a list of methods.
2. Plug-in developers may want to derive plug-in principal classes from a variety of base classes.
3. The application supports a number of different types of plug-ins, and plug-in developers may want to write a single plug-in that performs the jobs of several different plug-in types.

If plug-ins need to share a core set of code (the first condition), then you might want to define a base class for plug-in principal classes to inherit from. If you need to share code among plug-ins but also want to support different base classes or multiple plug-in types for one plug-in, you should put this code in the application and provide hooks for plug-ins to access it or create a separate class that plug-ins can use as a member.

Cocoa differentiates between _formal protocols_ and _informal protocols_. You can use either type of protocol to define a plug-in architecture depending on your needs. When a class adopts a formal protocol, it is in essence “signing an agreement” that it implements all the methods in the protocol. If a class adopts a protocol but fails to implement all its methods, the compiler will give a warning and runtime errors will occur if an unimplemented method is called. Formal protocols are defined with the Objective-C syntax used in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3teljzhe2dinznijbegssjirfes), with method prototypes between `@protocol` and `@end`:

__Listing 1__  A simple formal protocol

```objc
@protocol MyStringProcessing

- (NSString *)processString:(NSString *)aString;

@end
```

An informal protocol, on the other hand, is a list of optional methods. Informal protocols are usually implemented as categories on NSObject, so that any Cocoa class can implement its methods, as shown in [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3teljzhe2timjnijbegssgivees). If a class omits an informal protocol method from its implementation, no compile-time warning will be given. However, if a class expects a particular method to be implemented but it is not, a runtime error will occur.

__Listing 2__  A simple informal protocol

```objc
@interface NSObject(MyStringProcessing)

- (NSString *)processString:(NSString *)aString;

@end
```

If your host application needs every plug-in to implement a strict set of methods, then you should define the plug-in architecture with a formal protocol. If some or all methods are optional, then use an informal protocol and check at runtime what methods the principal class responds to. If some methods are required and some are not, you can define the architecture as an informal protocol, as long as you clearly document for plug-in authors what methods must be implemented and what methods can be left out.

Some classes are never meant to be instantiated, but serve as base classes for other classes to inherit from. These _abstract classes_ group methods and instance variables that will be used by a number of different subclasses into a common definition. The abstract class is incomplete by itself, but may contain useful code that reduces the implementation burden of its subclasses.

A host application’s plug-ins often share some common functionality, so many plug-in architectures are defined by an abstract class that the principal class of a plug-in inherits from. The base class and related code are typically packaged in a framework. Plug-in developers can then link against the framework in their applications and include the appropriate header.

The screen saver architecture in OS X is a good example of using an abstract base class. All screen savers do essentially the same thing: they draw some kind of animation on the screen. Much of the code needed to draw on the screen is already handled by the NSView class in the Application Kit, so screen savers should not have to reimplement this behavior. Additionally, all screen savers need code to handle animation timing, fading in and out, and other behavior. Accordingly, all OS X screen savers inherit from the ScreenSaverView class, which adds screen saver-specific functionality to the NSView class.

If you are writing a Carbon application in C, the simplest way to define a plug-in architecture is to define a set of functions that plug-ins must implement. This is akin to an Objective-C protocol, but there are no classes involved and the list of functions is not defined explicitly in any header file, but only in the documentation for the plug-in architecture. For all but the simplest plug-in situations, you should consider using the Core Foundation CFPlugIn opaque type.

Many plug-in architectures define a single plug-in entry point, which the application uses to send messages to the plug-in. In response to these messages, the plug-in can register callback functions to handle various facets of its operation.

For example, iTunes visual plug-ins receive initialization, clean-up, and idle messages through the main entry point. In the initialization phase, plug-ins register a callback function to handle messages related to visualization. Through the callback, iTunes informs the plug-in when a song is played or paused and when other changes of state occur, asks the plug-in to perform drawing, and sends other visualization-related messages.

Host applications need a way to actually find the entry point function or functions to a plug-in. This is done by defining a standard name for entry point functions, and looking up a function pointer for the function with the appropriate signature at runtime. You can use the Core Foundation CFBundle opaque type to translate between function names and function pointers.

For information about using CFBundle to load plug-ins and look up functions, see the Core Foundation Programming Topic _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_.

If you are a Carbon host application developer, you should consider using the Core Foundation CFPlugIn opaque type for all but the simplest plug-in situations. CFPlugIn frees you from having to design, implement, and test a new plug-in model yourself, because CFPlugIn handles all the basic plug-in functionality for you.

Core Foundation’s CFPlugIn is compatible with the basics of Microsoft’s Component Object Model (COM) architecture. In this model, the host application defines one or more types that each consists of one or more interfaces. A plug-in implements all of the functions in all of the interfaces for each type the plug-in supports, as well as a “factory function” for generating instances of the type. CFPlugIn has an advantage over Cocoa of using Universally Unique Identifiers (UUIDs) to uniquely identify types, interfaces, and factories, which eliminates name and version conflicts.

Extensibility of any sort is cause for concern when it comes to security. Because plug-ins run their own code in your host application’s address space, there are essentially no theoretical limits on what they do with your application’s address space.

There are, however, a few things you can do to prevent accidental misuse or abuse of your plug-in architecture:

- Warn your users about installing plug-ins from third parties and the side effects they may cause. What software is installed is really up to them, so be sure they know the implications.
- Limit direct access by plug-ins to your application code and data. Do not provide the plug-in with pointers to your application controller objects, application data, or other information that could be accidentally misused or intentionally abused.

Because there is no easy way to tell well-written, well-intentioned code from badly written or ill-intentioned code, you cannot do much more than warn your users and not directly give out to plug-ins sensitive application data. By implementing a plug-in architecture, you are paving the way to have your application behave in ways you did not expect, both positive and negative.

[Next](Loading%20Bundles.md)[Previous](Multi-Bundle%20Applications.md)

