---
title: UIElementInspector
apple_id: DTS10000728
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: ApplicationServices
published: '2010-06-03'
source_url: https://developer.apple.com/library/archive/samplecode/UIElementInspector/Introduction/Intro.html
archived_at: '2026-07-18T03:27:29.623917Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# UIElementInspector

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.4, 2010-06-03 Major refactoring of code to be a better example of MVC design pattern. Enable compilation in 64-bit by moving from a Carbon function to Cocoa. Centralized most access of AX calls to a utility wrapper class. Removed unused code and simplified the selection model of the app. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanzshawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X 10.6 and later |
| __Runtime Requirements:__ | Mac OS X version 10.6 and later. |

This sample demonstrates the use of the Accessibility API introduced in Mac OS X version 10.2.

This API provides an abstraction layer to allow accessibility applications a way to manipulate the UI of other applications, be they Carbon or Cocoa. The API is provided for use by both Carbon and Cocoa applications, although this sample demonstrates their use from a Cocoa application. In this sample, the Accessibility API is used to get information about whatever AXUIElements (widgets) are under the mouse at any given time. Information can be obtained from the AXUIElement, and actions that it has can be performed.

As the mouse moves, the inspector window displays information obtained through the new API. When you then lock the inspector window on an element, you can dig deeper into the information provided by the API for that object, as well as trigger any actions that it might provide, in the interaction window. This sample does not demonstrate how to make a custom UI element accessible so that the Accessibility API can access it. Custom Cocoa widgets will often just inherit the right behavior from their superclass. Carbon applications will typically need to provide a little more code to serve up the right information to applications that are interested. Instead, this sample shows how to use the Accessibility API itself - to get information on other applications and UI elements on the screen, which you would need to do as an accessibility application.

Version 1.1 - Update: some minor bug fixes are included in this release.

Version 1.2 - Fixed "Attributes" popup synching problem - fixed mismatch between attributes and values. Updated Xcode project for Universal Binary builds.

[Next](main.m.md)

