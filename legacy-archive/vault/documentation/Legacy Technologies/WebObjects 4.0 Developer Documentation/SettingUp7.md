---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/SettingUp7.html
archived_at: '2026-07-18T01:27:53.768466Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](SettingUp6.md)

## Web Components

A _component_ represents a page, or part of a page, in your application. An application can have one or more components.
Every application starts with a component called Main, which is shown in the Web Components suitcase in the second column of the browser as __Main.wo__. All components have the __.wo__ extension.
If you double-click a component, WebObjects Builder opens the component for editing. ["Editing With WebObjects Builder"](Editing%20With%20WebObjects%20Builder.md#apple-geydinjr) shows how to edit your component using WebObjects Builder.

On disk, a component is represented as a folder with the __.wo__ extension. Every component has several files that specify the component's look and behavior. The name of each one is the component's name followed by a specific file extension. These are the files in the Main component:

- __Main.html__ is the HTML template for the component. This file contains HTML tags, just like any web page; in addition, it typically contains tags for dynamic WebObjects elements.
- __Main.wod__ is the _declarations file_ that specifies bindings between the dynamic elements and variables or methods in your code.
- __Main.woo__ is used to store information about display groups (if your project accesses a database) and encodings for HTML templates. You should never edit this file (it does not appear in Project Builder's browser).

To create a new component:

- With Web Components selected in the first column of the browser, choose File !New in Project.
- In the New File panel, type the name of your project and click OK.

The WebObjects Component Wizard appears.

!

- If you want the Wizard to assist you in creating a component with database access, choose Component Wizard from Available Assistance; otherwise choose None. See ["Creating a WebObjects Database Application](Creating%20a%20WebObjects%20Database%20Application.md)" in _Getting Started With WebObjects_ for more information on using the Wizard with databases.
- Specify the language for your component and click Finish.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](SettingUp8.md)
