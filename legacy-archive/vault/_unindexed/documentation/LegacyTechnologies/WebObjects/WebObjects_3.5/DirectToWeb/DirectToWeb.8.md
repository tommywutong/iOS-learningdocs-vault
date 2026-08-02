---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DirectToWeb/DirectToWeb.8.html
archived_at: '2026-07-15T07:53:01.978050Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.7.md)[Previous
Section](DirectToWeb.7.md) 

#   Customizing Your Application With WebAssistant

The WebAssistant allows you to customize each page of your application. You can specify:

- 

  Which properties are displayed, and in what order.

By default, an entity's propertie s are listed in alphabetical order. Often, you'll want to change the order, as well as hiding some properties.

- 

  How number and date strings should be represented.
- 

  How relationships should be represented.

To activate the WebAssistant, click Customize in the Direct to Web header. A Java applet window appears showing the WebAssistant. This window lets you customize the current page in your application. (Using the Expert mode, you can customize any page in the application, regardless of whether it is currently displayed; see [See WebAssistant Expert Mode](DirectToWeb.a.md#apple-geztmmrq)
.

When you customize a page using the WebAssistant, the changes apply to all occurrences of that page, and that page only. For example, if you change the order of properties in an edit page for the Movie entity, then any time a Movie edit page is displayed, those changes are in effect. However, the changes don't apply to a Movie query, list, or inspect page; if you want to customize those in the same way, you must do so explicitly. Or, you can use the "\*all\*" setting in Expert mode to change all four pages at once; see [See WebAssistant Expert Mode](DirectToWeb.a.md#apple-geztmmrq)
.

###### 

!

All the entity's properties (attributes and relationships) are listed in the Show column, in the order in which they are displayed in the page. Properties in the Hide column are not displayed in the page. For each property, you can:

- 

  Move it to the Hide column it by double-clicking it or by selecting it and clicking the left arrow. Likewise, if a property is hidden, you can show it by double-clicking it or by selecting it and clicking the right arrow.
- 

  Move it up or down in the list by clicking the Rearrange up and down arrows. This changes the order of appearance of the properties in the page.
- 

  Change its name by editing the Display Name field.

_Note:_
This change only affects the way the entity is labeled in the page, and has no effect on the actual entity name.

The "Value type" field shows the data type of the selected property. You can't edit this field.

The icon in the upper right of the window shows whether the selected property is an attribute !
or a relationship !
.

The WOComponent box shows the name of the component that is being used to display the property in the page. In many cases (when the Pick button is enabled), you can choose a different component to display the property. In the above example, the _studio_
entity uses the QueryToOneField component. If you click the Pick button, a new applet window appears, allowing you to select a different component.

###### 

!

These are reusable components found in the Direct to Web Framework; see [See The Direct to Web Components](DirectToWeb.9.md#apple-ge2tgnzs)
for more information on the available components.

When you've made your changes to the page, you can use the buttons at the bottom of the WebAssistant to apply them:

- 

  _Update:_
  Sends your changes to the server and causes the page to be refreshed.
- 

  _Revert:_
  Causes the settings to revert to their last saved values.
- 

  _Save:_
  Saves the changes to disk. You need to save your changes in order for them to persist beyond the current session.
- 

  _Use Defaults:_
  reverts all settings to the values they had when the project was created.

Note that when you have activated the WebAssistant, a frame appears at the bottom of each page in your application, containing a "Show WebAssistant" button and a status field. To bring the WebAssistant to the front, click the Show WebAssistant button (rather than clicking Customize again).

###### 

!

[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.9.md)[Next
Section](DirectToWeb.9.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
