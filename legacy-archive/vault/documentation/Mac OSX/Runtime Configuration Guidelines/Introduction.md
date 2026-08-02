---
title: Runtime Configuration Guidelines
apple_id: 10000170i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: null
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPRuntimeConfig/000-Introduction/introduction.html
archived_at: '2026-07-15T08:16:27.200514Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Information%20Property%20List%20Files.md)

# Introduction

Dynamic configuration is a convenient way to adjust the properties of your executable without recompiling your code. Rather than relying on hardcoded information, your application implements slightly different behaviors based on external settings. There are several ways to record these settings, ranging from user preferences to [property lists](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) stored with your [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4).

Bundles use property lists extensively to store information about the bundle and its contents. macOS and iOS use the information in these property lists to determine an application properties such as its icon and whether to show the status bar (for iPhone applications).

You should read this document to learn about the properties you can use to configure application behavior and specify how macOS or iOS handle your application.

This document contains the following articles:

- [Information Property List Files](Information%20Property%20List%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4tclkdjjbeuskfirea) provides an introduction to information property list files and how they are used by the system.
- [The Preferences System](The%20Preferences%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4telkcineuuqsdinda) discusses the role and scope of user preferences and describes the use of the `defaults` tool for accessing preferences.
- [Environment Variables](Environment%20Variables.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4tglkcineuuskkijea) discusses the role of environment variables in configuring applications. This section also covers some of the ways you can establish environment variables for a given user session or process.
- [Additional Configuration Tips](Additional%20Configuration%20Tips.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4tilkcijbuuqsijbcq) lists the required and recommended configuration options for applications. This article also describes additional ways to configure both bundled and non-bundled applications.

For information about the keys and values you can include in an information property list file, see _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

For additional information about the preferences system, see _[Preferences and Settings Programming Guide](../../Cocoa/Preferences%20and%20Settings%20Programming%20Guide/About%20Preferences%20and%20Settings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2ts2i)_ or _[Preferences Programming Topics for Core Foundation](../../Core%20Foundation/Preferences%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Preferences%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezds2i)_.

[Next](Information%20Property%20List%20Files.md)

