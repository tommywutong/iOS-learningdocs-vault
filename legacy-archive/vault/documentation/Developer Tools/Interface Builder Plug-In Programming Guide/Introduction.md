---
title: Interface Builder Plug-In Programming Guide
apple_id: TP40004323
resource_type: Guide
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/IBPlugInGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:24:30.636451Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Anatomy%20of%20a%20Plug-In.md)

# Introduction

Although Mac OS X provides many useful views and controls for creating user interfaces, there may be times when you need to extend the basic set to achieve an appearance or behavior that is more appropriate for your application. The problem with custom views is that you generally cannot see how they will look in your user interface until that part of your application is running. Even when your application is running, making changes to the attributes of custom views requires modifying your code and rebuilding your application before you can see those changes. For large applications, turning around such changes can be slow and frustrating. Luckily, Interface Builder provides a way for you to integrate custom controls into the Interface Builder environment, build those controls into your application’s user interface, and see the results immediately.

The infrastructure for integrating custom controls in Interface Builder version 3.0 has improved significantly over previous versions of the application. The current infrastructure makes it possible to integrate new controls quickly and add support for more advanced features, such as inspectors, in stages. The process for creating inspectors has also improved dramatically and lets you focus on the new attributes exposed by your custom objects.

You integrate controls through the use of plug-ins. Each plug-in provides Interface Builder with design-time information about one or more custom objects, including where to find them and how to change their attributes. Upon loading your plug-in, designers can then drag your custom controls from the Interface Builder library window and use them to build their interfaces. Your controls can also be saved in the resulting nib file and instantiated at runtime.

This document guides you through the process of creating plug-ins for use with Interface Builder version 3.0. The chapters in this book are intended to be read more or less in order. Early chapters provide basic information that all plug-in developers need to know, while later chapters provide more advanced topics.

- [Anatomy of a Plug-In](Anatomy%20of%20a%20Plug-In.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmrtfvbuqnbnknltc) provides an overview of Interface Builder plug-ins, discussing their structure and how they interact with other code modules.
- [Plug-in Quick Start](Plug-in%20Quick%20Start.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmrtfvbuqojnknltc) provides a quick tutorial of how to build a basic plug-in.
- [Preparing Your Custom Objects](Preparing%20Your%20Custom%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmrtfvbuqmznknltc) describes the steps you need to take to prepare your custom controls, views, and objects for incorporation into the Interface Builder environment.
- [The Plug-in Object](The%20Plug-in%20Object.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmrtfvbuqmjqfvjvomi) describes the purpose of the plug-in object and how you tailor it for use with your custom objects.
- [Inspector Objects](Inspector%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmrtfvbuqnrnknltc) describes the process for creating inspectors, which are used to modify the attributes of your objects in the Interface Builder application.
- [Advanced Techniques](Advanced%20Techniques.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmrtfvbuqobnknltc) describes additional tasks associated with integrating more complex objects and views into Interface Builder.

[Next](Anatomy%20of%20a%20Plug-In.md)

