---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb20.html
archived_at: '2026-07-18T01:24:53.124277Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DirectToWeb19.md)

## WebAssistant Expert Mode

Expert mode is similar to standard mode, except that it allows you to make changes to any page in your application whether it is currently displayed in your browser or not. If you click the Expert mode button at the bottom of the WebAssistant, the window expands to show two additional lists:

- Tasks shows the types of pages available in Direct to Web.
- Entities shows all the entities in the model.

!

To customize any page in your application, simply select the type of page and the entity. The figure above shows an example of choosing the inspect page for the Talent entity, making the WebAssistant focus on this page rather than the page currently showing in the browser.
If you select "\*all\*" under Tasks, any changes you make affect all customizable pages for the selected entity. If you select "\*all\*" under Entities, you'll see a list of data types that exist in the application, as shown in the following figure.

!

Any changes you make affect all occurrences of that type. For example, the figure shows NSCalendarDate selected. You can specify a formatter, and pick a component to use anywhere in the application that an NSCalendarDate object is displayed.
If you click Show Browser Page, the task and entity for the current browser page are selected in the WebAssistant.
You can also select the Customize Page display of the WebAssistant while in Expert mode and change the underlying component, color, and border thickness of whatever page for whatever entity you select in the Tasks and Entities browsers.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Generating%20Components.md)
