---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/Script/DeleteVariables.html
archived_at: '2026-07-15T07:50:56.983846Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Script.book.md)
[!Previous Section](ObjectBrowser.md)

Deleting Variables

# Deleting Variables

Select the variable in the [object browser](ObjectBrowser.md).

Press the Delete button in the top part of the object browser.

The variable is removed from the script file as well as the object browser.

!

Always use the object browser to delete variables. For variables, WebObjects Builder always assumes the list in the object browser is correct and updates the script to match. It does not go the other direction: If you delete a variable from the [script window](ScriptWindow.md), WebObjects Builder tells you there are variables in the object browser that are not declared in the script and asks if it should add them.

Although you can access application and session variables from a component window's object browser, you can't delete them there. You must delete application and session variables in the application window.

[!Table of Contents](Script.book.md)
[!Next Section](CreateClasses.md)
