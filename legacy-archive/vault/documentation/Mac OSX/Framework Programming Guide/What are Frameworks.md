---
title: Framework Programming Guide
apple_id: 10000183i
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/WhatAreFrameworks.html
archived_at: '2026-07-15T08:15:41.326202Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Framework Programming Guide](Introduction%20to%20Framework%20Programming%20Guide.md)


[Next](Anatomy%20of%20Framework%20Bundles.md)[Previous](Introduction%20to%20Framework%20Programming%20Guide.md)

# What are Frameworks?

A _framework_ is a hierarchical directory that encapsulates shared resources, such as a dynamic shared library, nib files, image files, localized strings, header files, and reference documentation in a single package. Multiple applications can use all of these resources simultaneously. The system loads them into memory as needed and shares the one copy of the resource among all applications whenever possible.

A framework is also a bundle and its contents can be accessed using Core Foundation Bundle Services or the Cocoa NSBundle class. However, unlike most bundles, a framework bundle does not appear in the Finder as an opaque file. A framework bundle is a standard directory that the user can navigate. This makes it easier for developers to browse the framework contents and view any included documentation and header files.

Frameworks serve the same purpose as static and dynamic shared libraries, that is, they provide a library of routines that can be called by an application to perform a specific task. For example, the Application Kit and Foundation frameworks provide the programmatic interfaces for the Cocoa classes and methods. Frameworks offer the following advantages over static-linked libraries and other types of dynamic shared libraries:

- Frameworks group related, but separate, resources together. This grouping makes it easier to install, uninstall, and locate those resources.
- Frameworks can include a wider variety of resource types than libraries. For example, a framework can include any relevant header files and documentation.
- Multiple versions of a framework can be included in the same bundle. This makes it possible to be backward compatible with older programs.
- Only one copy of a framework’s read-only resources reside physically in-memory at any given time, regardless of how many processes are using those resources. This sharing of resources reduces the memory footprint of the system and helps improve performance.

The Darwin layer contains many static and dynamic libraries but otherwise, most OS X interfaces are packaged as frameworks. Some key frameworks—including Carbon, Cocoa, Application Services, and Core Services—provide convenient groupings of several smaller but related frameworks. These framework groups are called _umbrella frameworks_ and they act as an abstraction layer between a technology and the subframeworks that implement that technology.

In addition to using the system frameworks, you can create your own frameworks and use them privately for your own applications or make them publicly available to other developers. Private frameworks are appropriate for code modules you want to use in your own applications but do not want other developers to use. Public frameworks are intended for use by other developers and usually include headers and documentation defining the framework’s public interface.

[Next](Anatomy%20of%20Framework%20Bundles.md)[Previous](Introduction%20to%20Framework%20Programming%20Guide.md)

