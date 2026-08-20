---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/DynElem/ReuseComponents.html
archived_at: '2026-07-15T07:50:29.830075Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElem.book.md)
[!Previous Section](CustomElement.md)

Reusing Components

# Reusing Components

Place the cursor where you want the component to appear.

Drag the component from an application window.

!

Dragging a component into the component window adds it to the page as an abstract element. The component looks like a [custom element](CustomElement.md). If you inspect this element, you'll see it has the component's name. You treat the component just like you would any other dynamic element: you must bind to it to be able to interact with it in the script file.

You can drag a component from any application window. If you drag across applications, the component is added to the destination component's application (because WebObjects requires that all components used by an application be in that application's directory.)

To create components that can be reused in this manner, see "[Creating Reusable Components](../Advanced/CreateReusableComponent.md)."

__Tip:__ If you use a component frequently, store it on a [custom palette](../Advanced/CreatePalette.md).

[!Table of Contents](DynElem.book.md)
[!Next Section](BindElements.md)
