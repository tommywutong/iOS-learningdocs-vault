---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DirectToWeb/DirectToWeb.a.html
archived_at: '2026-07-15T07:53:07.011661Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.9.md)[Previous
Section](DirectToWeb.9.md) 

##   WebAssistant Expert Mode

Expert mode is similar to standard mode, except that it allows you to make changes to any page in your application regardless of whether it is currently displayed in your browser. If you click the Expert mode button at the bottom of the WebAssistant, the window expands to show two additional lists:

- 

  Tasks shows the four types of pages available in Direct to Web.
- 

  Entities shows all the entities in the model.

##### 

!

To customize any page in your application, simply select the type of page and the entity. The figure above shows an example of customizing the inspect page for the Movie entity, regardless of what page is showing in the browser.

If you select "\*all\*" under Tasks, any changes you make will affect all four pages for the selected entity. If you select "\*all\*" under Entities, you'll see a list of data types that exist in the application, as shown in the following figure. Any changes you make affect all occurrences of that type. For example, the figure shows NSCalendarDate selected. You can specify a formatter, and pick a component to use anywhere in the application that an NSCalendarDate object is displayed.

##### 

!

If you click Show Browser Page, the task and entity for the current browser page are selected in the WebAssistant.

[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.b.md)[Next
Section](DirectToWeb.b.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
