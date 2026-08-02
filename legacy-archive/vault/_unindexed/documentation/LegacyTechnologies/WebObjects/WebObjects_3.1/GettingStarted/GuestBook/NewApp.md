---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/GuestBook/NewApp.html
archived_at: '2026-07-15T07:48:48.010706Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBook.book.md) [!Previous Section](Launch.md)

# Create a new application directory

The first step to creating the guest book application is to create a directory for it. A WebObjects application is always contained in a single directory that has the extension __.woa__. For the application to run, this directory must be under your HTTP server's document root (specifically under the __WebObjects__ subdirectory) so that your server can access it. WebObjects Builder helps you set the application directory up correctly.

- Choose File !New Application.

The panel that appears shows you the contents of the directory _<DocumentRoot>___/WebObjects__. _<DocumentRoot>_ is your HTTP server's document root, which you specified when you installed WebObjects.

- Type __GuestBook__ as the file name, and click Save.
!

WebObjects Builder opens two windows: an application window, which represents the contents of the __GuestBook.woa__ directory, and an empty editing window labeled __Main.wo__.
You no longer need the untitled document, so you can close it at any time.

## A closer look

The application window shows you what the application directory contains. When first created, all that the application directory contains is a directory named __Main.wo__. __Main.wo__ is a _component_. Components define dynamic HTML pages and are the basic building blocks of a WebObjects application. The first component in an application is called __Main.wo__.
There are three parts to a component: an HTML template, a script, and bindings between the two. You use WebObjects Builder to create these three parts. The section "[Components](../../DevGuide/Intro/Components.md)" in the introduction to the _WebObjects Developer's Guide_ describes other things that can go into a component.

Usually applications contain several components, each representing all or part of a page. The GuestBook application, however, only has a single page, which is represented by the Main component. The rest of this tutorial describes how to edit the Main component.
To learn how to set up more complex applications, see "[Setting up Applications](../../WOBuilder/AppSetup/AppSetup.book.md)" in _Using WebObjects Builder_. For more background on WebObjects applications and what they can contain, see "[The Ingredients of a WebObjects Application](../../DevGuide/Intro/Ingredients.md)" in the introduction to the _WebObjects Developer's Guide_.

[!Table of Contents](GuestBook.book.md) [!Next Section](CreateInputFields.md)
