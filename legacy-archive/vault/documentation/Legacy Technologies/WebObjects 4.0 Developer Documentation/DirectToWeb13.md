---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb13.html
archived_at: '2026-07-18T01:24:23.394872Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Customizing%20Your%20Application%20With%20WebAssistant.md)

## WebAssistant Overview

When the Web Assistant applet is launched, it appears in a window whose title indicates the current page and entity:

!

The WebAssistant has three displays, each selectable by clicking a tab:

- __Customize Application__. Allows you to select which entities of the model are hidden, which are shown, and which are read-only.
- __Customize Page__. Allows you to customize global page properties, such as overall style, color, and border thickness. In expert mode, allows you to "freeze" customized pages as reusable components.
- __Customize Properties__. Allows you to set which properties of an entity are shown in a page, the order in which they're displayed, and the display characteristics of properties (for example, color and alignment).

The WebAssistant stays synchronous with your browser. When you navigate to a new page, it displays the settings for that page.
The Web Assistant has two modes, Standard mode and Expert mode. By default the Web Assistant opens in Standard mode, which lets you customize the current page in your application. When you customize a page in Standard mode, the changes apply to all occurrences of that page, and that page only. For example, if you change the order of properties in an edit page for the Movie entity, then any time a Movie edit page is displayed, those changes are in effect. However, the changes don't apply to a Movie query, list, or inspect page; if you want to customize those in the same way, you must do so explicitly.
Using Web Assistant's Expert mode, you can customize any page in the application, regardless of whether it is currently displayed. Thus, by specifying the "\*all\*" setting in Expert mode, you could change all pages of a given entity at once. For more information, see ["WebAssistant Expert Mode"](DirectToWeb20.md#apple-haydkna).

When you've made changes to a page, you can use the buttons at the bottom of the WebAssistant to apply them:

- _Update:_ Sends your changes to the server and causes the page to be refreshed.
- _Revert:_ Causes all settings to revert to their last saved values.
- _Save:_ Saves the changes to disk. You need to save your changes in order for them to persist beyond the current session.
- _Use Defaults:_ reverts all settings to the values they had when the project was created.

The _Info_ button displays a brief description of the currently selected Direct to Web component.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DirectToWeb14.md)
