---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/AppSetup/ReusableComponents.html
archived_at: '2026-07-15T07:50:15.861747Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](AppSetup.book.md)
[!Previous Section](AddExistingComponent.md)

 Reusable Components

|  |  |
| --- | --- |
|  | ---  Reusable Components One of the strengths of the WebObjects architecture is its support of reusable components. Any component that you define can be reused by any WebObjects application. The most common type of component represents an entire HTML page. However, WebObjects also supports components that represent a part of a page and can be used within multiple pages of the same application or even multiple sections of the same page.  Although some pages must be crafted individually for an application, many could be identical across applications. Even pages that aren't identical across applications can share at least some portions (header, footer, navigation bars, and so on) with pages in other applications. With reusable components, you can factor out a portion of a page (or a complete page) that's used throughout one or more applications, define it once, and then use it wherever you want, simply by referring to it by name. |

!

|  |  |
| --- | --- |
|  | To reuse an existing component, you must add it to each application that wants to use it.  When you add one component to the page of another component, WebObjects Builder displays it as a [custom element](../DynElem/CustomElement.md). You use this component just like you would use any other dynamic element that you drag from the palette.  For more information on reusable components, see "[Creating Reusable Components](../../DevGuide/Reuse/Reuse.book.md)" in the _WebObjects Developer's Guide_. Also, "[Reusing Components](../DynElem/ReuseComponents.md)" and "[Creating Reusable Components](../Advanced/CreateReusableComponent.md)" in this guide describe how to use a component within another component and how to create a reusable component using WebObjects Builder.   --- |

[!Table of Contents](AppSetup.book.md)
[!Next Section](DeleteComponent.md)
