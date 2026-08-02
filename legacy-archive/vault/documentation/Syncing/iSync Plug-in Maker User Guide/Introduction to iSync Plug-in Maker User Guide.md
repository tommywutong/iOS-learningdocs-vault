---
title: iSync Plug-in Maker User Guide
apple_id: TP40003921
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2011-06-13'
source_url: https://developer.apple.com/library/archive/documentation/Syncing/Conceptual/TramontanePluginBuilderUserGuide/Introduction/Introduction.html
archived_at: '2026-07-18T02:07:49.949640Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20Creating%20Plug-ins.md)

# Introduction to iSync Plug-in Maker User Guide

iSync Plug-in Maker is a developer tool that allows you to build, test, and release device plug-ins. With iSync Plug-in Maker, you can create plug-ins according to the specific features supported by a device. This includes the ability to write modem scripts for using the device to connect to the Internet. You can also use the tool to run a suite of standard automated tests, even if you didn’t use the tool to create the plug-in. The tool reports error details so you can detect and fix bugs in the plug-in before shipping.

This document describes the iSync Plug-in Maker application and how you use it to develop iSync device plug-ins for Mac OS X. It provides a comprehensive guide to using the tool through each stage of the process: editing, testing, and exporting plug-ins.

iSync Plug-in Maker also includes documentation of numerous manual tests that should be run to fully test your plug-in. The manual tests contain steps that use Apple applications and iSync to modify and sync records—these steps cannot be automated. The manual tests are not described in this document. Read _[iSync Manual Test Suite Guide](../../Apple%20Applications/iSync%20Manual%20Test%20Suite%20Guide/Introduction%20to%20iSync%20Manual%20Test%20Suite%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diobu)_ for information on manual tests.

You should read this document if you are a phone manufacturer supplying iSync plug-ins or a third party that builds iSync plug-ins for Mac OS X. This document assumes you are familiar with handheld device technologies such as USB, Bluetooth, and SyncML. It assumes you know how syncing works in general, but not specifically how it works on Mac OS X. You do not need to know how to use the Sync Services framework in Mac OS X to use iSync Plug-in Maker. However, an overview of this technology is useful.

Read this chapter first for an overview of the process involved in creating and testing iSync plug-ins:

- [Overview of Creating Plug-ins](Overview%20of%20Creating%20Plug-ins.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsmrrfvbuqnbnknltc) describes the process of building and testing iSync plug-ins.

Read these chapters in sequence to learn how to use the iSync Plug-in Maker tool:

- [Editing Plug-ins](Editing%20Plug-ins.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsmrrfvbuqmznknltc) explains how to configure the settings for a particular device. Configuration may include writing JavaScript functions as necessary for communicating over USB or Bluetooth using SyncML. You can also import and edit a modem script.
- [Testing Plug-ins](Testing%20Plug-ins.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsmrrfvbuqnjnknltc) explains how to run the automated test scenarios built into iSync Plug-in Maker. The testing mode helps you QA your plug-in by locating errors in your configuration or device.
- [Exporting Plug-ins](Exporting%20Plug-ins.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsmrrfvbuqnrnknltc) explains how to export your plug-in and modem script for shipping independent of iSync releases.

Read _[iSync Manual Test Suite Guide](../../Apple%20Applications/iSync%20Manual%20Test%20Suite%20Guide/Introduction%20to%20iSync%20Manual%20Test%20Suite%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diobu)_ for detailed descriptions of the manual tests that you should run before shipping your plug-in.

If you need to write JavaScript functions in iSync Plug-in Maker, read this document:

- _iSync JavaScript Reference_ describes a few classes used to write JavaScript functions in iSync Plug-in Maker.

If you need to learn more about what SyncML commands iSync supports, read these document:

- _[iSync SyncML Guide](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/iSyncSyncMLGuide/iSyncSyncMLGuide.pdf)_ and _iSync SyncML Reference_ describes the SyncML commands supported by iSync.

If you need to debug a sync session using Syncrospector, read this document:

- _Sync Services Tutorial_ provides an introduction to testing syncing applications using Syncrospector.

If you need to know more about the schemas used by Apple applications, read this document:

- _Apple Applications Schema Reference_

For an overview of Sync Services on Mac OS X, read these documents:

- The chapter [Sync Services Overview](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/SyncOverview.html#//apple_ref/doc/uid/TP40001151) in _[Sync Services Programming Guide](../../Cocoa/Sync%20Services%20Programming%20Guide/Introduction%20to%20Sync%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnzy)_ describes the Sync Services architecture and core classes.
- The chapter [Managing Your Sync Session](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/SessionManagement.html#//apple_ref/doc/uid/TP40001162) in _[Sync Services Programming Guide](../../Cocoa/Sync%20Services%20Programming%20Guide/Introduction%20to%20Sync%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnzy)_ describes the phases of syncing: negotiating, pushing, mingling, and pulling. Note that the terms used by Sync Services differ slightly from the terms used by SyncML.
[Next](Overview%20of%20Creating%20Plug-ins.md)

