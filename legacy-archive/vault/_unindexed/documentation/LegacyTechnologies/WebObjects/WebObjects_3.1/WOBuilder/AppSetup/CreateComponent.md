---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/AppSetup/CreateComponent.html
archived_at: '2026-07-15T07:50:13.746806Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](AppSetup.book.md)
[!Previous Section](AppWindow.md)

Creating Components

# Creating Components

Click the plus sign in the Component display of the application window. A new component is created with the name `Untitled`.

Type a name for the component.

Press Enter.

!

If you have a large number of components, you might want to enter a comment in the Description field to help you identify the component.

When you create a component, you're creating a subdirectory named _Component___.wo__ under the application directory. There are three parts to a component: an HTML template, a script, and bindings between the two. You use WebObjects Builder's [component window](ComponentWindow.md) to create these three parts. "[Components](../../DevGuide/Intro/Components.md)" in the introduction to the _WebObjects Developer's Guide_ describes other things that can go into a component.

In many cases, you'll want to use components that already exist. [Reusing components](ReusableComponents.md) is one of the powerful features of WebObjects. If the component already exists, you can [add it to the application](AddExistingComponent.md).

__Note:__ The menu command File->New creates a new component that is not added to your application.

[!Table of Contents](AppSetup.book.md)
[!Next Section](ComponentWindow.md)
