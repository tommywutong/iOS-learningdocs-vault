---
title: SDK Compatibility Guide
apple_id: 10000163i
resource_type: Guide
platform: Xcode Developer Tools
topic: General
technology: null
published: '2010-11-15'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/cross_development/Overview/overview.html
archived_at: '2026-07-15T07:30:33.214381Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [SDK Compatibility Guide](Introduction.md)


[Next](Configuring%20a%20Project%20for%20SDK-Based%20Development.md)[Previous](Introduction.md)

# Overview of SDK-Based Development

Apple makes SDKs available for specific versions of iOS and OS X. Using these SDKs allows you to build against the headers and libraries of an operating system version other than the one you're running on. For example, you can build for OS X version 10.4 while running on OS X version 10.6.

The OS X SDKs are installed as part of the Xcode Essentials install package with Xcode 3.2 and later. Xcode release notes list the SDKs supported by each release. When developing for iOS, you always use an SDK downloaded from the iOS Dev Center website.

Take advantage of SDK-based development in these ways:

- You can build a target optimized for one version of an operating system and forward-compatible with later versions, but doesn’t take specific advantage of newer features.
- You can build a target for a range of operating system versions, so that it can launch in older versions but can take advantage of features in newer ones. This allows you to deliver software that provides new value to customers who have upgraded to a new system version, but still runs for those who haven’t.

To develop software that can be deployed on, and take advantage of features from, different versions of iOS or OS X, you specify which version—or SDK—of iOS or OS X headers and libraries to build with. You can also specify the oldest iOS or OS X system version on which the software will run. These concepts are described in [Base SDK and Deployment Target Settings](Configuring%20a%20Project%20for%20SDK-Based%20Development.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2jninedclktk4yq).

As frameworks evolve through various releases, APIs are introduced or deprecated and behaviors of existing APIs may occasionally change. Apple makes every effort to minimize changes that may cause incompatibilities, in some cases providing alternate behaviors based on the framework version. In rare cases, your code needs to determine the framework version and adjust accordingly.

As a backward-compatibility mechanism, Apple frameworks sometimes check for the version of the SDK an application is built against, and, if it is an older SDK, modify the behavior for compatibility. This is done in cases where Apple predicts or discovers compatibility problems.

Typically, frameworks detect how an application is built by looking at the version of the system frameworks the application is linked against. Thus, when relinking your application using a newer SDK, you might notice different behaviors—some of which might cause incompatibilities. In these cases, because your application is being rebuilt, you should address these issues at the same time. For this reason, if you are doing a small update of your application, to address a few bugs, for example, it's usually best to continue building with the same build environment and libraries used originally; that is, against the original SDK.

In some cases, frameworks provide defaults settings (preferences) that you can use to get the old or new behavior, independent of the SDK an application is built against. Often these preferences are provided for debugging purposes only; in some cases the preferences can be used globally to modify the behavior of an application by registering the values. If taking advantage of this mechanism, do it very early in your code, using the [NSUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/cl/NSUserDefaults) method [registerDefaults:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/instm/NSUserDefaults/registerDefaults:)).

[Next](Configuring%20a%20Project%20for%20SDK-Based%20Development.md)[Previous](Introduction.md)

