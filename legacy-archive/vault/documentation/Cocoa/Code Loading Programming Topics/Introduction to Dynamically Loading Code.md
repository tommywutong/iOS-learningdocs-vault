---
title: Code Loading Programming Topics
apple_id: 10000052i
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingCode/LoadingCode.html
archived_at: '2026-07-15T07:16:28.677309Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Loadable%20Bundles.md)

# Introduction to Dynamically Loading Code

This programming topic describes the available techniques for loading executable code while an application is running.

To learn about the concepts related to dynamic loading, read the following articles:

- [About Loadable Bundles](About%20Loadable%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3dqlkcineuiqsbivfa) describes how loadable bundles are structured and when you should use them.
- [Loadable Bundles in Cocoa](Loadable%20Bundles%20in%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3dslkciffegskbjbaq) describes features specific to loadable bundles in Cocoa.
- [CFBundle and NSBundle](CFBundle%20and%20NSBundle.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3talkcineuiqsbivfa) describes the relationship between the Core Foundation CFBundle opaque type and the Cocoa NSBundle class.
- [Multi-Bundle Applications](Multi-Bundle%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tclkcineuiqsbivfa) explains how to organize your application into multiple bundles for increased modularity and extensibility.
- [Plug-in Architectures](Plug-in%20Architectures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3telkcineuiqsbivfa) describes the plug-in concept and how to architect an application around plug-ins.

The following tasks are covered:

- [Loading Bundles](Loading%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tglkdjjbeircdifba)
- [Creating Loadable Bundles](Creating%20Loadable%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tilkdjjbeircdifba)
- [Building Applications with Multiple Bundles](Building%20Applications%20with%20Multiple%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tklkdjjbeircdifba)
- [Creating Plug-in Architectures](Creating%20Plug-in%20Architectures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tmlkdjjbeircdifba)
- [Preventing Name Conflicts](Preventing%20Name%20Conflicts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3tolkdjjbemr2di5dq)
- [Loading Objective-C Libraries From Java](Loading%20Objective-C%20Libraries%20From%20Java.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhezdglkciffegskjjjcq) describes how to load an Objective-C dynamic library into a Java application.

It is recommended that you read _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_ as a prerequisite; this document provides an overview to bundles, including their purpose, types, structure, and the API for accessing bundle resources. _[Resource Programming Guide](../Resource%20Programming%20Guide/About%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2i)_, which is a document related to _Dynamically Loading Code_, describes how to access non-code bundle resources, particularly those in nib files. [Core Foundation CFPlugIn](Plug-in%20Architectures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3teljzhaydcmq) in this document gives a summary of the Core Foundation CFPlugin API architecture.

[Next](About%20Loadable%20Bundles.md)

