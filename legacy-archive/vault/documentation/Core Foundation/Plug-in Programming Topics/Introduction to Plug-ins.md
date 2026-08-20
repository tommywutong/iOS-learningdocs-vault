---
title: Plug-in Programming Topics
apple_id: 10000128i
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2005-03-03'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPlugIns/CFPlugIns.html
archived_at: '2026-07-15T07:22:35.624964Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Plug-ins.md)

# Introduction to Plug-ins

Plug-in architectures are an attractive solution for developers seeking to build applications that are modular, customizable, and easily extensible. What began as a clever way to allow third parties to add features to an application without access to source code has, for many developers, evolved into a full-blown component architecture. Core Foundation Plug-ins uses the basic code-loading facility of Core Foundation bundles to provide a standard plug-in architecture for OS X applications. Although this section is addressed primarily to host application developers, plug-in developers also need to read it in order to fully understand and make use of the CFPlugIn opaque type.

The examples in this section demonstrate how to create and work with CFPlugIn objects. The error-checking code has been removed for clarity. In practice, it is _vital_ that you check for errors because passing bad parameters into Core Foundation routines can cause your application to crash.

These articles discuss the plug-in architecture and how they work:

- [About Plug-ins](About%20Plug-ins.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge2tmlkdjjbeksscjbea)
- [Plug-in Architecture](Plug-in%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge2tolkdjjbeksscjbea)
- [Anatomy of a Plug-in](Anatomy%20of%20a%20Plug-in.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge2tslkdjjbeksscjbea)
- [Conceptual Building Blocks](Conceptual%20Building%20Blocks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dalkdjjbeksscjbea)
- [Plug-in Registration](Plug-in%20Registration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dclkdjjbeksscjbea)

These articles contain examples on how to create and use plug-ins:

- [Defining Types and Interfaces](Defining%20Types%20and%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dglkdjjbekscbifdq)
- [Implementing a Plug-in](Implementing%20a%20Plug-in.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dilkdjjbekscbifdq)
- [Loading and Using a Plug-in](Loading%20and%20Using%20a%20Plug-in.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dklkdjjbekscbifdq)

To generate UUIDs programmatically see:

- [Generating a UUID Programmatically](Generating%20a%20UUID%20Programmatically.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dmlkdjjbekscbifdq)

[Next](About%20Plug-ins.md)

