---
title: Text Input Management
apple_id: 10000065i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-06-02'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/InputManager/InputManager.html
archived_at: '2026-07-15T07:16:07.582748Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Text%20Input%20Management%20Architecture.md)

# Introduction to Text Input Management

The text input management system provides Cocoa applications with a wide variety of text input capabilities. This document describes the Cocoa classes related to text input management and explains how to use them.

Read this document if you want to create a custom input server for your Cocoa application or if you want to implement text input capabilities in a view.

The text input management system is described in the following
articles:

- [Text Input Management Architecture](Text%20Input%20Management%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgaztmlkciffegrsjizda) provides
  an overview of the text input management system.
- [About Key Bindings](About%20Key%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dsmbsfvbecssdirdemsi) explains
  how the text input management system binds keystrokes to character
  data.

Detailed information about creating and delivering a custom
input server is covered in the following articles:

- [Creating Input Servers](Creating%20Input%20Servers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgaztqlkciffeqssbizea) explains
  how to implement an input server.
- [Deploying Input Servers](Deploying%20Input%20Servers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgaztslkcineusqkfirca) explains
  how to install an input server.

If you want to create a custom view to handle text input capabilities,
read this article:

- [Creating Custom Views](Creating%20Custom%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dsmbrfvbegskdivdeori) explains
  how to add keyboard input capabilities to a custom view.

For more information, refer to the following documents:

- _[Text Editing Programming Guide](../Text%20Editing%20Programming%20Guide/Introduction%20to%20Text%20Editing%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2to2i)_ describes
  the text-editing process, including text-input key event processing
  through the input management system.
- NSInputServer, NSInputManager,
  and [NSTextView](https://developer.apple.com/documentation/appkit/nstextview) are
  the primary classes that interact to provide text input management
  for Cocoa applications.
[Next](Text%20Input%20Management%20Architecture.md)

