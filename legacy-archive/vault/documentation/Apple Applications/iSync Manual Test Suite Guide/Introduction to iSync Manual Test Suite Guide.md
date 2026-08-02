---
title: iSync Manual Test Suite Guide
apple_id: TP40004484
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-06-13'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/iSyncManualTestSuiteRef/Introduction/Introduction.html
archived_at: '2026-07-15T05:19:24.113902Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Common%20Steps.md)

# Introduction to iSync Manual Test Suite Guide

iSync is an application that allows users to sync their devices with data on their computers. iSync Plug-in Maker is a developer tool that allows you to build, test, and release iSync device plug-ins. iSync Plug-in Maker contains automated tests that communicate directly with the device. However, you must also run the manual tests described in this document to fully qualify your iSync plug-in before shipping. These manual tests involve adding, modify, and deleting records on both the device and computer. You use Apple applications to modify records on the computer and development tools to help set up certain scenarios.

You should read this document if you are building an iSync device plug-in using iSync Plug-in Maker. After editing, testing, and exporting your plug-in using iSync Plug-in Maker, use this guide to run manual test suites. You should be familiar with end-user applications on the computer to run these tests and the Syncrospector developer tool.

The tests in this document are organized by categories from general purpose tests to specific database tests. There are also categories for sync modes and stress testing. The document contains the following chapters:

- [Common Steps](Common%20Steps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diobufvbuqmjrfvjvomi) contains common set up and steps used by most tests. Read this chapter first.
- [General Tests](General%20Tests.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diobufvbuqmznknltc) contains tests that pertain to all devices regardless of the SyncML features they support.
- [Initial Sync Tests](Initial%20Sync%20Tests.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diobufvbuqnbnknltc) contains tests that pertain to the first time the device syncs.
- [Sync Mode Tests](Sync%20Mode%20Tests.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diobufvbuqnjnknltc) contains tests that pertain to different sync modes.
- [Cancellation Tests](Cancellation%20Tests.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diobufvbuqnrnknltc) contains tests that cancel syncing.
- [Stress Tests](Stress%20Tests.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diobufvbuqnznknltc) contains tests that exceed the limits of the capacity of the device.
- [Calendar Tests](Calendar%20Tests.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diobufvbuqobnknltc) contains tests specific to the Calendars database.
- [Contacts Tests](Contacts%20Tests.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diobufvbuqojnknltc) contains tests specific to the Contacts database.
- [Miscellaneous Tests](Miscellaneous%20Tests.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diobufvbuqmjqfvjvomi) contains miscellaneous tests that do not fit into any of the above categories.

If you need to build an iSync plug-in, read _[iSync Plug-in Maker User Guide](../../Syncing/iSync%20Plug-in%20Maker%20User%20Guide/Introduction%20to%20iSync%20Plug-in%20Maker%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsmrr)_ before reading this document.

If you use Syncrospector to test your plug-in, read _Sync Services Tutorial_ to learn more about how to use this tool.

[Next](Common%20Steps.md)

