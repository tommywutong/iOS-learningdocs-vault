---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/GuestBook/LaunchingWOBuilder.html
archived_at: '2026-07-18T01:21:08.257914Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20Simple%20WebObjects%20Application.md) [!Previous Section](Examining%20Your%20Project.md)

# Launching WebObjects Builder

Now that you've created your project, you'll edit the Main component with WebObjects Builder.

- Select Web Components in the first column of the browser.
- Double-click __Main.wo__ in the second column.

The WebObjects Builder tool launches and displays a window titled __Main.wo__. This represents your application's Main component.

!

You create your component graphically in the upper pane of the component window. The browser at the bottom of the window (known as the _object browser__)_ is used to display variables and methods your component uses. Note that there are two variables already defined, __application__ and __session__. You'll create others later.

The toolbar at the top of the window contains several buttons that allow you to create the content of your component. WebObjects Builder also has menu commands corresponding to these buttons.

__Note:__ Depending on the width of the window, the toolbar may appear in two rows or one.

- From the ! pop-up list at the left of the toolbar, choose !.

This pop-up list allows you to switch between graphical editing mode and source editing mode. When you choose source editing mode, the text of your HTML template (__Main.html__) appears. It is a skeleton at this point, since the page is empty. As you add elements graphically, their corresponding HTML tags appear in this file.

!

The bottom pane shows your declarations (__Main.wod__) file. Later, when you bind variables to your dynamic elements, this file stores the information. Normally, you do not type directly in this file. You can add elements using the toolbar in either source or graphical editing mode.

- Switch back to graphical editing mode. For the rest of the tutorial, you'll work in this mode.

[!Table of Contents](Creating%20a%20Simple%20WebObjects%20Application.md) [!Next Section](Creating%20the%20Page%27s%20Content.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
