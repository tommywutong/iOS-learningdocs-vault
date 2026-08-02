---
title: Accessibility Programming Guide for OS X
apple_id: TP40001078
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/index.html
archived_at: '2026-07-15T03:49:19.624182Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)



## Introduction

### About This Technology

Accessible apps help users with disabilities access information and information technology. Accessible apps enable individuals and support their viewpoints and working styles.

Apple’s commitment to accessibility is rooted in the Macintosh’s legendary ease-of-use and is enhanced by the Accessibility features in OS X. Beginning in OS X version 10.2, Apple introduced the accessibility architecture, which defines how accessibility clients interact with apps running in OS X. An accessibility client is an app that modifies the way users interact with their computer. For example, the VoiceOver app reads the contents of the screen and provides audible cues as the user operates the standard mouse and keyboard. Other apps let the user operate their computer using specialized hardware, for example using a head-tracking mouse.

With OS X version 10.10, Apple introduced a new API with the following goals:

- Replace the previous, key-based API with a simpler, method-based API.
- Provide protocols that guide developers through the process of creating accessible controls.
- Update the OS X accessibility API to make it similar to the iOS accessibility API.
- Provide backward compatibility, letting developers mix and match the method-based and key-based APIs.

Use of this new, method-based API is strongly preferred over the older, key-based API.

### At a Glance

The accessibility API provides accessibility clients with information about your app. Even though standard AppKit views and controls already adopt the accessibility API, you may want to add additional information to make the controls more useful within the context of your app. Additionally, if your app uses custom controls, those controls need to adopt the appropriate accessibility protocols to ensure that they provide the required information to accessibility clients.

> [!NOTE]
> 

### Accessibility Has Become a Must-Have Feature

Over the years, the emphasis on accessibility has shifted from a bonus add-on to a must-have feature for all high-quality apps. By making your app accessible, you are enabling individuals and supporting their viewpoints and working styles. This approach both broadens the pool of possible users, while also improving your current users’ ability to interact with your app.

> [!NOTE]
> 

### Add Accessibility to your App

The accessibility API provides protocols that define how accessibility clients interact with your app. Your app must carefully consider how it presents itself to the accessibility clients. Ideally, you want to strip away the unimportant implementation details and focus the user’s attention on the tools they need to accomplish their desired tasks.

If your app uses standard AppKit controls and views, accessibility is already built in. Much of the work has been done for you. Still, you might need to customize the default information returned by the controls to provide better descriptions or additional context for the user. Custom views and controls need to adopt the proper accessibility protocols. These protocols then guide you through the process of implementing the required properties and methods. Implementing the protocol, however, is only the starting point. You can further enhance and refine these controls as needed for your app.

> [!NOTE]
> 

### Test Your App

Implementing an accessible user interface is only half the battle. You must also test the interface to make sure that users can operate it effectively. OS X and Xcode provide a number of tools and techniques for testing an accessible UI.

> [!NOTE]
> 

### How to Use This Document

This document provides an introduction to the new OS X accessibility architecture. Because all apps should be accessible, all Cocoa app developers should read this document. Additionally, if you’re developing an accessibility client—for example, a screen reader or an assistive input device—this document provides a solid background on the information and actions that you can access from an accessible app.

### See Also

Apple offers additional developer documentation on accessibility that you may find useful.

- _[NSAccessibility Protocol Reference](https://developer.apple.com/documentation/appkit/nsaccessibility)_ provides the complete list of properties and action methods used by the OS X accessibility API.
- _OS X Human Interface Guidelines_ describes a number of guidelines for creating user interfaces. Accessibility clients expect your user interface to follow these guidelines. It is considerably easier to accessibility-enable your app when you adhere to these guidelines.

[Why Make Your App Accessible?](OSXAXwhy.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzyfvbuqmrqgywviucykjcummjqge)
