---
title: Application Architecture Overview
apple_id: 10000005i
resource_type: Guide
platform: macOS
topic: General
technology: AppKit
published: '2011-06-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AppArchitecture/AppArchitecture.html
archived_at: '2026-07-15T05:25:28.415900Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Features%20of%20a%20Cocoa%20Application.md)

# Introduction to Application Architecture

This document describes the essential components of a Cocoa application and how they work together. It also discusses features of Cocoa applications and the principles related to their design.

Every developer who creates Cocoa applications should read this document.

To understand the information in this document you should have a general knowledge of Cocoa programming paradigms, which are described in the _[Cocoa Fundamentals Guide](../Cocoa%20Fundamentals%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzu)_.

Three important features of the Cocoa frameworks—the document architecture, scripting, and undo and redo—have a great deal in common conceptually. This document explains their shared conceptual underpinnings. It does not go into great detail about the specifics of the classes implementing these features or how to use them. Instead it concentrates on the recommended structure of an application and how that structure supports these features.

The Cocoa frameworks are `AppKit.framework` and `Foundation.framework`. You can examine them in `/System/Library/Frameworks/`.

This document contains the following articles:

- [Features of a Cocoa Application](Features%20of%20a%20Cocoa%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaydglkciffeur2iizfa) describes the features provided by the Application Kit that are shared by all Cocoa applications.
- [Document Architecture](Document%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhezdclkdifbugqkjifbq) explains how the Application Kit supports document-based applications. This common type of application enables users to create and edit documents: container objects that manage user data and present it in windows.
- [Scripting](Scripting.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhezdalktk4yq) explains the concepts you need to understand to make your application scriptable—that is, one that responds to Apple events using the AppleScript system.
- [Undo and Redo](Undo%20and%20Redo.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhezdelkdifbueq2djjdq) describes the support Cocoa provides for implementing undo and redo, and explains how those features work with the document architecture and other application mechanisms.
- [Graceful Application Termination](Graceful%20Application%20Termination.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dalktk4yq) explains how a Cocoa application can quit executing gracefully—that is, ensuring that the user's data is saved and cleaning up after itself.

[Next](Features%20of%20a%20Cocoa%20Application.md)

