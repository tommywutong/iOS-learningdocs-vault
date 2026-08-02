---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb23.html
archived_at: '2026-07-18T01:24:57.147573Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Modifying%20Your%20Application%27s%20Code.md)

# Using Direct to Web in Other WebObjects Applications

Other WebObjects applications (that is, applications not using the Direct to Web option in the wizard) can use the Direct to Web framework to display query, list, edit, and other pages in the Direct to Web repetoire. Making use of Direct to Web can be a convenient shortcut for many applications when all they need is a standard database-related page. They can use Direct to Web in one of two ways:

- By embedding Direct to Web components in the pages of their application
- By linking to a dynamically-created Direct to Web page and appropriately implementing the action method invoked when the link is clicked

## Embedding Direct to Web Components

Using a Direct To Web component is not much different than using any other off-the-shelf component. The procedure is the following.

- Add the __DirectToWeb__ framework to your project. You can find this framework in _NEXT_ROOT___/System/Library/Frameworks__.
- Decide which Direct to Web component you want to use and become familiar with its API.

See ["Direct to Web Component Reference"](DirectToWeb24.md#apple-gezdgnru) for summaries of these components.

- Put a WebObjects tag for the component in the page that is to display it.

```
<webObject name=MyD2WQuery></webObject>
```


This is a step you can complete in WebObjects Builder.

- Make the appropriate bindings for the component.

```
MyD2WQuery: D2WQuery {
    entityName="Movie";
    displayKeys="( title, roles, studio.budget )";
    queryDataSource=movieDisplayGroup.dataSource;
}
```


All embedded components require an __entityName__ binding to specify the entity the page will be dealing with. Extra bindings could be required, depending on the functionality of the page. For example, List pages require a __dataSource__ binding.

You can also complete this step in WebObjects Builder.

- If necessary, implement the action method for the component.
- You can customize embedded Direct to Web components using the WebAssistant. But first you must add a file named u__ser.d2wmodel__ to the Resources category of your application project. The WebAssistant uses this file to maintain your settings. In addition, before you launch the WebAssistant, make sure rapid-turnaround is enabled for your application. You can then launch the WebAssistant using the __appletviewer__ tool; see ["Running WebAssistant With appletviewer"](Customizing%20Your%20Application%20With%20WebAssistant.md#apple-geztinrv).

When the WebAssistant acts upon a non-DirectToWeb application, it does not automatically track which page is displayed. Thus you must point it at the page you want to modify in Expert mode. For example, if you want to customize a list page for Movies, you will have to click Expert Mode and then select "list" as the Task and "Movie" as the entity. You can then customize a component in the same way you customize DirectToWeb pages. Also, when you click Update to send the new settings to the application, the browser does not automatically refresh your page. You must either click the "Reload" button in your browser or (especially in cases where you pick a new type of component) you must re-navigate to the page.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DirectToWeb24.md)
