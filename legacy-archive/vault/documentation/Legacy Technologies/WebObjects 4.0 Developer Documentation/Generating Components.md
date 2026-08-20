---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb21.html
archived_at: '2026-07-18T01:24:54.863987Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DirectToWeb20.md)

# Generating Components

When you have worked with the WebAssistant and customized your pages to your liking, you may still want to add more features to your application. To do so, you can "freeze" a page; that is, save it as a WebObjects component. When you do this, the component becomes part of your project and is no longer created "on the fly" by Direct to Web. This has several advantages:

- You have complete control over the visual appearance of the page. You can add any static or dynamic HTML elements you like, using a tool such as WebObjects Builder.
- You can add functionality to the page by editing the component's Java code, as well as by editing the bindings of the page's dynamic elements.
- Your application's performance improves because Direct to Web doesn't have to go through the process of creating the page "on the fly."

The main disadvantage of generating components is that you lose the ability to modify settings with the WebAssistant. Therefore, you should try to get your settings as close as possible to what you want before generating the component.
To save a page as a component:

- Click the Expert Mode button at the bottom of the WebAssistant to enter Expert mode.
- Click Customize Page at the top of the WebAssistant.

!

- Select the task and entity corresponding to the page you want to generate.

You can't select "\*all\*" to generate multiple components. You must generate the components one at a time.

- In the Advanced Options group of controls, make sure the "Choose DirectToWeb page" radio button is selected.
- Click Generate.

The Freeze Component window appears. It contains a text field with a default name for your page (the page name followed by the entity name). You can edit the name if you choose.

!

- Click the Ok button.

Direct to Web generates a component and adds it to your project. (You may have to wait a few moments for this process to complete.) Your settings are automatically saved.

- Rebuild your project.

To "un-freeze" a component, select the "Choose DirectToWeb page" radio button but do not click the Generate button.
When you generate a page and click Update, the browser's current page doesn't reflect the changes. To use the new component, you must rebuild the application, relaunch it, and then navigate to a new instance of the page. For example, if the current page is a Movie query page, and you use the WebAssistant to freeze it, you must rebuild the project with the frozen component, then launch the application and navigate to a new instance of Movie query (by clicking Build Query); the new instance uses the frozen component.
The generated component is like any other WebObjects component. You can edit your component graphically using WebObjects Builder. You can also examine the HTML and bindings (__.wod__ file) of the new component in Project Builder.
Direct to Web also generates Java code for your component, which you can modify appropriate to your needs. Each component implements an interface that is appropriate to the page: QueryPageInterface, ListPageInterface, InspectPageInterface, and EditPageInterface. For example, the __QueryMovieRole.java__ file shown below implements the QueryPageInterface. For example, it contains an action method called __queryClicked__ that returns a component when the Query DB button is clicked. (Note that the component's submit button is bound to __queryClicked__ in __QueryMovieRole.wod__.)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Modifying%20Your%20Application%27s%20Code.md)
