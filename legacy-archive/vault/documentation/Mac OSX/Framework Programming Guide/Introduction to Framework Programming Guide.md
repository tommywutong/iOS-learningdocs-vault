---
title: Framework Programming Guide
apple_id: 10000183i
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Frameworks.html
archived_at: '2026-07-15T08:15:41.360273Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](What%20are%20Frameworks.md)

# Introduction to Framework Programming Guide

OS X makes extensive use of frameworks to distribute shared code and resources, such as the interfaces to the system itself. You can create frameworks of your own to provide shared code and resources to one or more of your company’s applications. You can also create frameworks containing class libraries or add-on modules with the intention of distributing them to other developers.

The information in this document provides the background you need to create frameworks and the steps needed to create them in Xcode. Although creating frameworks is not difficult, there are some guidelines you should follow when doing so. Xcode simplifies the creation process by helping you create the framework bundle and manage the information and placement of files in that bundle. However, this document also provides additional information about how to perform many less obvious tasks.

This document contains the following articles:

- [What are Frameworks?](What%20are%20Frameworks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydglkcijbukskkizeq) provides background information about what frameworks are and how they’re used.
- [Anatomy of Framework Bundles](Anatomy%20of%20Framework%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tglkciffeksskifba) describes the basic structure of frameworks, including umbrella frameworks.
- [Framework Versions](Framework%20Versions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tklkcineukq2birca) describes the system used to manage different framework versions and how you specify version information when you create a framework.
- [Frameworks and Binding](Frameworks%20and%20Binding.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tmlkciffesq2circa) explains how framework symbols are bound to an application at runtime. It also explains how to improve the load time of your framework through the use of prebinding.
- [Frameworks and Weak Linking](Frameworks%20and%20Weak%20Linking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3tqlkcijbuuskdivbq) explains the concept of “weak-linking” for framework symbols and shows you how to use this feature with both your own frameworks and third-party frameworks.
- [Guidelines for Creating Frameworks](Guidelines%20for%20Creating%20Frameworks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tilkciffeqr2hi5aq) provides guidelines on the best practices to use for creating frameworks.
- [Creating a Framework](Creating%20a%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tqlkciffeisceifda) shows how to create public frameworks and private embedded frameworks using Xcode.
- [Initializing a Framework at Runtime](Initializing%20a%20Framework%20at%20Runtime.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tslkcircusrcejjdq) shows how to create a load-time initialization routine for your framework.
- [Exporting Your Framework Interface](Exporting%20Your%20Framework%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dalkcijbuuskdivbq) shows how to limit the symbols exported by your framework to the exact set you want.
- [Installing Your Framework](Installing%20Your%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dclkcijbugrscjjaq) explains the conventions for where to install your custom frameworks.
- [Including Frameworks](Including%20Frameworks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tolkciffeuqscjbfa) shows the basic ways to use frameworks in applications.

[Next](What%20are%20Frameworks.md)

