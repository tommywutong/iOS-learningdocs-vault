---
title: Bundle Programming Guide
apple_id: 10000123i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html
archived_at: '2026-07-15T07:22:12.212707Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Bundles.md)

# Introduction

Bundles are a fundamental technology in macOS and iOS that are used to encapsulate code and resources. Bundles simplify the developer experience by providing known locations for needed resources while alleviating the need to create compound binary files. Instead, bundles use directories and files to provide a more natural type of organization—one that can also be modified easily both during development and after deployment.

To support bundles, both Cocoa and Core Foundation provide programming interfaces for accessing the contents of bundles. Because bundles use an organized structure, it is important that all developers understand the fundamental organizing principles of bundles. This document provides you with the foundation for understanding how bundles work and for how you use them during development to access your resource files.

This document contains the following chapters:

- [About Bundles](About%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2jninedcmbqfvjvomi) introduces the concept of bundles and packages and how they are used by the system.
- [Bundle Structures](Bundle%20Structures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2jninedcmbrfvjvomi) describes the structure and contents of the standard bundle types.
- [Accessing a Bundle's Contents](Accessing%20a%20Bundle%E2%80%99s%20Contents.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2jninedcmbufvjvomi) shows you how to use the Cocoa and Core Foundation interfaces to get information about a bundle and its contents.
- [Document Packages](Document%20Packages.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2jninedcmbwfvjvomi) describes the notion of document packages (which are loosely related to bundles) and how you use them.

Although the information in this document applies to all types of bundles, if you are working with more specialized types of bundles (such as [frameworks](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) and plug-ins), you should also consult the following documents:

- _[Framework Programming Guide](../../Mac%20OSX/Framework%20Programming%20Guide/Introduction%20to%20Framework%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4dg2i)_ provides detailed information about creating and using custom frameworks.
- _[Code Loading Programming Topics](../../Cocoa/Code%20Loading%20Programming%20Topics/Introduction%20to%20Dynamically%20Loading%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2te2i)_ provides information about writing plug-ins using the Objective-C language.
- _[Plug-in Programming Topics](../Plug-in%20Programming%20Topics/Introduction%20to%20Plug-ins.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdq2i)_ provides information about writing plug-ins using the C language.
[Next](About%20Bundles.md)

