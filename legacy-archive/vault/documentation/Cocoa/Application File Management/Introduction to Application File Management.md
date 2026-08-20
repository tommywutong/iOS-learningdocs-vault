---
title: Application File Management
apple_id: 10000056i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AppFileMgmt/AppFileMgmt.html
archived_at: '2026-07-15T05:25:31.408995Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](The%20Save%20and%20Open%20Panels.md)

# Introduction to Application File Management

This topic describes the Application Kit’s facilities for representing file system objects (files and directories) and allowing users to interact with the file system.

This document has the following articles:

- Concepts

  - [File Wrappers](File%20Wrappers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43tglkcijbumrchizbq) describes the object that encapsulates a file, directory, or link.
  - [The Save and Open Panels](The%20Save%20and%20Open%20Panels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43tclkcijbumrchizbq) describes the panels that you run to let users specify files (and sometimes directories) to save and open.
- Tasks

  - [Working With File Wrappers](Working%20With%20File%20Wrappers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43tklkciffemqsbifea) describes how to make and manage file wrappers.
  - [Working With Directory Wrappers](Working%20With%20Directory%20Wrappers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43tmlkciffemqsbifea) describes how to make and manage directory wrappers.
  - [Using a Save Panel](Using%20a%20Save%20Panel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43tilkciffemqsbifea) explains how to create and display a save panel.
  - [Using an Open Panel](Using%20an%20Open%20Panel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43tolkciffemqsbifea) explains how to create and display an open panel.
  - [Getting the Current Selection](Getting%20the%20Current%20Selection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmrvfvjvomi) describes how to find out what the currently selected file or directory is.
  - [Filtering Out Browser Items](Filtering%20Out%20Browser%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmrwfvjvomi) explains how to make specific items in the browser unselectable.
  - [Configuring a Choose Dialog](Configuring%20a%20Choose%20Dialog.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmrxfvjvomi) describes how to configure an Open panel as a Choose dialog.
  - [Managing Accessory Views](Managing%20Accessory%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmrrfvjvomi) explains how to make, add, and manage accessory views.
- See Also

  - _Document-Based Applications Overview_
  - _[Low-Level File Management Programming Topics](../Low-Level%20File%20Management%20Programming%20Topics/Introduction%20to%20Low-Level%20File%20Management%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tk2i)_

[Next](The%20Save%20and%20Open%20Panels.md)

