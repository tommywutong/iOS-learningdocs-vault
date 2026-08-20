---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/SettingUp/WebComps.htm
archived_at: '2026-07-15T07:57:50.315546Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](SetUpTOC.md) [!Previous Section](AddorDel.md)

## Web Components

A _component_ represents a page, or part of a page, in your application. An application can have one or more components.
Every application starts with a component called Main, which is shown in the second column of the browser as __Main.wo__. All components have the __.wo__ extension.
If you double-click a component, WebObjects Builder opens the component for editing. ["Editing With WebObjects Builder"](../Editing/EditTOC.md#apple-geydinjr) shows how to edit your component using WebObjects Builder.

On disk, a component is represented as a folder with the __.wo__ extension. Every component has several files that specify the component's look and behavior. The name of each one is the component's name followed by a specific file extension. These are the files in the Main component:

- __Main.html__ is the HTML template for the component. This file contains HTML tags, just like any web page; in addition, it typically contains tags for dynamic WebObjects elements.
- __Main.wod__ is the _declarations file_ that specifies bindings between the dynamic elements and variables or methods in your code.
- __Main.api__ is used for components that are reused by other components (see ["Reusable Components"](../DynamicElements/ReuseCmp.md#apple-gezdambq)).
- __Main.woo__ is used to store information about display groups (if your project accesses a database) and encodings for HTML templates. You should never edit this file (it does not appear in Project Builder's browser).

To create a new component:

- With Web Components selected in the first column of the browser, choose File !New in Project.
- In the New File panel, type the name of your project and click OK.

The WebObjects Component Wizard appears.

!- If you want the Wizard to assist you in creating a component with database access, choose Component Wizard from Available Assistance; otherwise choose None. See ["Creating a WebObjects Database Application](../../GettingStarted/Movies/MoviesTOC.md)" in _Getting Started With WebObjects_ for more information on using the Wizard with databases.
- Specify the language for your component and click Finish.

[!Table of Contents](SetUpTOC.md) [!Next Section](Classes.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
