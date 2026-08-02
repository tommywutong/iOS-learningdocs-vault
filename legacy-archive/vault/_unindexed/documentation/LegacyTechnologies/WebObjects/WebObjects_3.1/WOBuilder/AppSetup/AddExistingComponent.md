---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/AppSetup/AddExistingComponent.html
archived_at: '2026-07-15T07:50:06.851389Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](AppSetup.book.md)
[!Previous Section](ComponentWindow.md)

 Adding Existing Components

# Adding Existing Components

Open the application containing the component you want to reuse.

Drag the component from that application to the current application's window.

!

You can [reuse components](ReusableComponents.md) that you created for other applications by dragging them into a page in the current application.

When you drag a component from one application window to another, the component is copied into the destination application's directory. Applications can only use components that are copied into the application directory.

If the existing component is intended to be used within a page, you can drag the component directly into a page in the destination application. If you do this, it adds the component to the page as a "[custom element](../DynElem/CustomElement.md)" (in addition to listing it in the application window). If you inspect this custom element, you'll see it has the component's name.

[!Table of Contents](AppSetup.book.md)
[!Next Section](ReusableComponents.md)
