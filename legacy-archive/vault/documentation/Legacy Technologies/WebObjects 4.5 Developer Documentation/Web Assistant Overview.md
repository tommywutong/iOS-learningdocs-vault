---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.66.html
archived_at: '2026-07-15T08:11:18.739116Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Customizing%20Your%20Application%20With%20the%20Web%20Assistant.md) [!](Running%20the%20Web%20Assistant%20With%20appletviewer.md) [!](Restricting%20Access%20to%20Entities.md)

---

#  Web Assistant Overview

When the Web Assistant applet is launched, it appears in a window whose title indicates the current page and entity:

!

The Web Assistant has four displays, each selectable by clicking a tab:

- 

  __Properties__
  . Allows you to set which properties of an entity are shown in a page, the order in which they're displayed, and the display characteristics of properties (for example, color and alignment).
- 

  __Page__
  . Allows you to customize global page properties, such as template, overall style, color, and border thickness.
- 

  __Generation.__
  Only available in expert mode, this display allows you to generate templates and "freeze" customized pages as reusable components.
- 

  __Entities__
  . Allows you to select which entities of the model are hidden, which are shown, and which are read-only.

The Web Assistant stays synchronous with your browser. When you navigate to a new page, it displays the settings for that page.

The Web Assistant has two modes, Standard mode and Expert mode. By default the Web Assistant opens in Standard mode, which lets you customize the current page in your application. When you customize a page in Standard mode, the changes apply to all occurrences of that page, and that page only. For example, if you change the order of properties in an edit page for the Movie entity, then any time a Movie edit page is displayed, those changes are in effect (provided you have clicked Update or Save). However, the changes don't apply to a Movie query, list, or inspect page; if you want to customize those in the same way, you must do so explicitly.

Using Web Assistant's Expert mode, you can customize any page in the application, regardless of whether it is currently displayed. Thus, by specifying the "\*all\*" setting in Expert mode, you could change all pages of a given entity at once. In addition, you can generate a template or "freeze" a page as a reusable component. For more information, see [Web Assistant Expert Mode](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.6d.html#13620)
.

When you've made changes to a page, you can use the buttons at the bottom of the Web Assistant to apply them:

- 

  _Update:_
  Sends your changes to the server. On some systems this causes the page to be refreshed in your browser.
- 

  _Revert:_
  Causes all settings to revert to their last saved values.
- 

  _Use Defaults:_
  reverts all settings to the values they had when the project was created.
- 

  _Save:_
  Saves the changes to disk. You need to save your changes in order for them to persist beyond the current session.

The _Info_
button displays a brief description of the currently selected Direct to Web component.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Customizing%20Your%20Application%20With%20the%20Web%20Assistant.md) [!](Running%20the%20Web%20Assistant%20With%20appletviewer.md) [!](Restricting%20Access%20to%20Entities.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
