---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Intro/Components.html
archived_at: '2026-07-15T07:47:08.406975Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Start.book.md) [!Previous Section](Ingredients.md)

## Components

To write a WebObjects application, you create components and connect them together. A component is a page or portion of a page that has both HTML content and behavior. Each component is located in its own directory named _Component___.wo__ and generally contains these files:

- An _HTML template_ (_Component___.html__) that specifies how the page looks.
- A _script file_ (_Component___.wos__) that defines the component's attributes (variables) and implements its behavior in WebScript.
- A _declarations file_ (_Component___.wod__) that binds the dynamic elements of the template to the script's variables and actions.
- If necessary, any images or other resources the component uses.
!Figure 1. The Contents of a Component Directory

The script file is only included in scripted components. You may also write _compiled components_, which use Java or Objective-C instead of a script file. For more information, see "Creating a Compiled Application" in the book _Getting Started With WebObjects_.
The first page of a WebObjects application is usually named __Main.wo__. When users start a session with a WebObjects application, they can specify the name of the first page, but such a practice is uncommon. If no page is specified, WebObjects applications look for the __Main.wo__ component.
__Note:__  Not all components represent an entire page. You can nest small, reusable components inside a component representing a whole page. For more information, see the "[Creating Reusable Components](../Reuse/Reuse.book.md)" chapter.

[!Table of Contents](Start.book.md) [!Next Section](AppExecutables.md)
