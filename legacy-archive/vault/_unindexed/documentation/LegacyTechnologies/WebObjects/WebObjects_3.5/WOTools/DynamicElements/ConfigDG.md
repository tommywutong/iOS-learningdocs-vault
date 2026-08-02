---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/DynamicElements/ConfigDG.htm
archived_at: '2026-07-15T07:56:16.600516Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](DynElTOC.md)[Table
of Contents](DynElTOC.md) [!](AddDspGp.md)[Previous
Section](AddDspGp.md) 

### Configuring the Display Group

A display group must be configured in order for it
to be created and initialized automatically when the component is initialized.
Display groups are instantiated from an archive file (with the extension
.__woo__) that's stored in the component. You shouldn't edit .__woo__
files by hand; they're maintained by WebObjects Builder.

In the object browser, !
means that the display group has been configured. A !
means that it has not been configured, and so the variable isn't automatically
created. A configured display group shows its keys and actions in the second
column of the object browser. You can bind them to elements in your program.

!

To configure a display group (or change its configuration),
double-click its name to open the Display Group Options panel.

!

In this panel, you specify the following information:

- _Entity:_ The Entity combo box has a list of entities from the models
  in your project. You can select one from the list or type the name. 
- _Has detail data source:_ Check this to create a detail display group.
  See ["Creating a Detail Display Group"](CreateDG.md#apple-geydemrs)
  for more information. 
- _Entries per batch:_ Set a non-zero value here to specify the number
  of records to be displayed at once. When the value is zero, all records
  are displayed. 
- _Qualification:_ When displaying records according to a query, this
  setting determines whether to display records that begin with, end with,
  or contain the item specified. 
- _Fetches on load_: When you check this option, the display group fetches
  all its objects as soon as the component is loaded into the application. 
- _Sorting:_ You select an attribute by which to sort your displayed
  objects from the pop-up list, and use the radio buttons to select the order
  of sorting.

[!](DynElTOC.md)[Table
of Contents](DynElTOC.md) [!](CreateDG.md)[Next
Section](CreateDG.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
