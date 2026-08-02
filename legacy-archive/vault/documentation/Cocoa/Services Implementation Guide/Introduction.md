---
title: Services Implementation Guide
apple_id: 10000101i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SysServices/introduction.html
archived_at: '2026-07-15T07:19:56.238003Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Services%20Overview.md)

# Introduction

Services are features exported by your application for the benefit of other applications. Services let you share the resources and capabilities of your application with other applications in the system.

Users access services through the Services menu that’s found in every application’s application menu. An application does not need to know in advance what operations are available; the application merely needs to indicate the types of data it uses. The Services menu will make available the operations that apply to those types when they apply.

This document describes how OS X services work, shows some typical Services menus, and provides instructions on how you can use services in your application.

You should read this document if you are a Cocoa application developer and want to provide your application’s services to other applications or make services from other applications available to your application.

Before you read this document, you should be familiar with information property lists. You need to know what they are and how to add properties to a list. For more information, see [Information Property List Files](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPRuntimeConfig/Articles/ConfigFiles.html#//apple_ref/doc/uid/20002091) in _[Runtime Configuration Guidelines](../../Mac%20OSX/Runtime%20Configuration%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3ta2i)_.

For guidelines on naming menu items and for designing the interface for a services application, see _OS X Human Interface Guidelines_.

Read the first three chapters to learn how services work, see examples of services in applications, and learn which properties you use to provide and use services in your applications. The remaining two chapters describe in detail how to provide and use services in your applications.

The Services feature was updated in OS X version 10.6 with the following changes and additions to properties:

- A slash is no longer treated as specifying a submenu with `NSMenuItem`.
- `NSSendTypes` and `NSReturnTypes` no longer need to be specified.
- There are three new properties: `NSSendFileTypes`, `NSServiceDescription`, and `NSRequiredContext`.

[Next](Services%20Overview.md)

