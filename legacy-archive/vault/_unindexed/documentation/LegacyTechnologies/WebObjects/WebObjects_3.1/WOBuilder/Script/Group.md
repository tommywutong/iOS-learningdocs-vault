---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/Script/Group.html
archived_at: '2026-07-15T07:50:59.969971Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Script.book.md)
[!Previous Section](Classes.md)

Creating Classes by Grouping

# Creating Classes by Grouping

Select variables in the object browser.

Choose Tools->Script->Group Variables.

Enter the Class's name in the panel that opens.

!

The Group Variables command takes the selected variables and creates a new dictionary class out of them. The variables become the dictionary's attributes. The class's scope is the same as the variables used to create the class. That is, if you group variables in a component window, the class is visible only in that component. If you group variables in an application window, the class is visible in all components.

The Ungroup Variables command reverses the effects of a Group Variables command. You can use it on any dictionary class, regardless of if it was created using the Group Variables command.

[!Table of Contents](Script.book.md)
[!Next Section](DeleteClasses.md)
