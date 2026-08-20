---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.9.html
archived_at: '2026-07-15T08:08:33.767769Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Creating%20a%20Simple%20WebObjects%20Application.md) [!](Examining%20Your%20Project.md) [!](Creating%20the%20Page%27s%20Content.md)

---

#  Launching WebObjects Builder

Now that you've created your project, you'll edit the Main component with WebObjects Builder.

1. 

   Select Web Components in the first column of the browser.
2. 

   Double-click __Main.wo__ in the second column.

The WebObjects Builder tool launches and displays a window titled __Main.wo__. This represents your application's Main component.!

You create your component graphically in the upper pane of the component window. The browser at the bottom of the window (known as the _object browser_) is used to display variables and methods your component uses. Note that there are two variables already defined, __application__ and __session__. You'll create others later.

The _path view_ lies between the upper pane and the object browser and shows the _element path_ to the selected element. Any element can be contained in a hierarchy of several levels of elements and can in turn contain other elements. Here, the path view shows the HTML BODY tag representing the page element, which is the top level of the hierarchy. By clicking the tags in the path view, you can easily choose different elements in the hierarchy.

The toolbar at the top of the window contains several buttons that allow you to create the content of your component. WebObjects Builder also has menu commands corresponding to these buttons.

3. 

   From the ! pop-up list at the left of the toolbar, choose !
   .

   This pop-up list allows you to switch between editing views, which determine the way WebObjects Builder displays your page and the way you edit it. WebObjects Builder provides three editing views: the layout view for general editing, the preview view for displaying (approximately) what your page looks like in a browser, and the source view for editing raw HTML. When you choose the source view, the text of your HTML template (__Main.html__) appears. It is a skeleton at this point, since the page is empty. As you add elements graphically, their corresponding HTML tags appear in this file.

   !

   The bottom pane shows your declarations (__Main.wod__) file. Later, when you bind variables to your dynamic elements, this file stores the information. Normally, you do not type directly in this file. You can add elements using the toolbar in all of the views.
4. 

   Switch back to the layout view. For the rest of the tutorial, you'll work in this view.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Creating%20a%20Simple%20WebObjects%20Application.md) [!](Examining%20Your%20Project.md) [!](Creating%20the%20Page%27s%20Content.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
