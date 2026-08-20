---
title: Sheet Programming Topics
apple_id: 10000002i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-05-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sheets/Sheets.html
archived_at: '2026-07-15T07:19:04.480999Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Sheets.md)

# Introduction to Sheets

A sheet is simply a dialog attached to a specific window, ensuring that a user never loses track of which window the dialog belongs to. Sheets can be dialogs that require information from the user (such as a Save dialog) or they can be alerts that provide messages about error conditions or warn users of potentially hazardous actions (such as a Save Before Quitting alert).

Alert sheets are document-modal whereas standard alert dialogs are application-modal. A standard alert dialog appears in its own window (technically, an NSPanel object) and allows no user action in the application until the user dismisses the alert. See _[Dialogs and Special Panels](../Dialogs%20and%20Special%20Panels/Introduction%20to%20Dialogs%20and%20Special%20Panels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3tc2i)_ for a discussion of standard alert dialogs.

The Dialogs section in _Apple Human Interface Guidelines_ discusses sheets from the point of view of how they relate to other OS X user interface objects.

Cocoa developers interested in using sheets in their application should read this document.

This programming describes sheets and how they work, and provides examples on how you can use sheets in your applications. It contains the following articles:

- [About Sheets](About%20Sheets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2dglkcifbemskcjfaq) provides basic information about sheets.
- [Types of Alerts](Types%20of%20Alerts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2dilkcifbemskcjfaq) describes the types of alerts and how they are used.
- [Using Alert Sheets](Using%20Alert%20Sheets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2dklkcifbemskcjfaq) describes how to present an alert sheet.
- [Displaying Alert Help](Displaying%20Alert%20Help.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga3tolkcifbeischjjda) describes how to display help information associated with an alert sheet.
- [Using Custom Sheets](Using%20Custom%20Sheets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4talkcifbemskcjfaq) describes how to create and present a custom sheet.
- [Presenting a Series of Sheets](Presenting%20a%20Series%20of%20Sheets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2dmlkcifbemskcjfaq) describes how to present a series of sheets.
- [Sheet Notifications](Sheet%20Notifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2dolkcifbemskcjfaq) describes the notifications sent, along with their related delegate methods, while working with a sheet.
- [Positioning Sheets](Positioning%20Sheets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4delkciffeiqkkjbda) describes how to position a sheet within its window.
- [Using Application-Modal Dialogs](Using%20Application-Modal%20Dialogs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytembxfvbecqsgjfbesqi) describes how to create and present an application-modal dialog.

[Next](About%20Sheets.md)

