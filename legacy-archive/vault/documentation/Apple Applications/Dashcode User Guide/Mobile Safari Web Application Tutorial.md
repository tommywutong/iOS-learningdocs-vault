---
title: Dashcode User Guide
apple_id: TP40004692
resource_type: Guide
platform: Safari|Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashcode_UserGuide/Contents/Resources/en.lproj/MakingaWebApp/MakingaWebApp.html
archived_at: '2026-07-15T05:17:42.504748Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashcode User Guide](Introduction%20to%20Dashcode%20User%20Guide.md)


[Next](Dual-Product%20Web%20Application%20Tutorial.md)[Previous](Dashboard%20Widget%20Tutorial.md)

# Mobile Safari Web Application Tutorial

This tutorial walks you through using Dashcode to create project that produces a mobile Safari web application. A mobile Safari web application (also known as an iPhone web application) is web content that is optimized for Safari on iPhone and that offers users an application-like experience. As you follow the steps, you learn how to choose a template, customize your code, and share your application with others. Completing this tutorial is a quick and easy way to get started building mobile Safari web applications in Dashcode.

This is the second of three tutorials in this document. If you’re interested in learning how to start developing Dashboard widgets, be sure to read [Dashboard Widget Tutorial](Dashboard%20Widget%20Tutorial.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmznknltc). If you want to learn how to create a project that produces both a mobile Safari web application and a Safari web application, read [Dual-Product Web Application Tutorial](Dual-Product%20Web%20Application%20Tutorial.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjzfvjvomq). The remainder of the document, beginning with [Starting a Project](Starting%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnbnknltc), delves more deeply into the Dashcode development environment, describing how it supports both widget and web application development.

In this tutorial, you build a mobile Safari web application that displays information about national parks. This project is based on the browser type of web application, and supports navigation through multiple levels of content.

Before continuing, make sure that you have Dashcode version 3.0 or later installed on your Mac. If you don’t have Dashcode installed, read [Getting and Running Dashcode](Introduction%20to%20Dashcode%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjnknlte) to learn how to get and install Dashcode.

To start, double-click the Dashcode icon to open it. A new project window opens and displays a dialog that displays two types of projects—Safari and Dashboard—and an assortment of templates for each project type. _Templates_ are handy starting points for creating common types of web applications and widgets. (To find out what a template does, select it to show a short description of its capabilities.)

For this tutorial, select the Safari project type. Then, to create a browser-type web application that’s optimized to run in Safari on iPhone:

1. Select the Browser template.
2. Click the “Develop for: Safari” checkbox to deselect it. (Make sure the “Develop for: Mobile Safari” checkbox is still selected.)
3. Click Choose.

A project window opens, displaying the first page of a new mobile Safari web application based on the Browser template, as shown in Figure 2-1.

__Figure 2-1__  A new mobile Safari web application project based on the Browser template

!!

Along the left side of the project window is the _navigator_, which you use to switch between the various tools available when you’re designing a web application. The main portion of the window is the _canvas_, which you use to design your web application’s interface.

At the bottom of the navigator in Figure 2-1 you can see the _Workflow Steps list_, which guides you through the web application development process. Each step is a milestone in creating a web application, telling you what to do and where to do it. When you complete a step, mark it as done and move on to the next step.

The Browser template gives you a mobile Safari web application that displays some built-in information and supports navigating from one page to the next. You don’t need to customize the application at all to see how it works, but you should specify a title to display.

In the canvas, double-click Browser and type in a new title, such as Parks. You’ll see this title in the header of the first page.

You should also give a name to the webpage itself. When you begin a project, this name is Untitled. To specify a name, double-click Untitled at the top of the navigator and type the name you want, say, National Parks.

Now is also a good time to save your project. Choose File > Save to save the project. Give your project a name and select a location to save it in. The project encapsulates the web application and all the information Dashcode needs to create it for you.

Your new mobile Safari web application is already functional, even though it only displays placeholder data. To prove this, click the green Run button in the Dashcode toolbar (alternatively, you can choose Debug > Run).

Dashcode opens your web application in a simulator application.

Take a few moments to use the application. You should see Parks (or a different title you typed in) displayed in the header of the first page and you should see National Parks (or a different title you gave the webpage) in the title bar area, if this area is visible.

Notice that when you click a row item in the first page, a new page appears that gives details about the item. There are a few other things you should notice about the second page:

- The title of the second page is the same as the name of the row item you selected in the first page.
- A back button has appeared to the left of the title and its label is Parks, which is the title of the first page. You can click this button to return to the first page.
- The text in the middle of the second page includes the name of the row item you selected.

The two pages of your web application should look similar to those shown in Figure 2-2.

__Figure 2-2__  The default Browser-based mobile Safari web application contains a top-level page (left) and a detail page (right)

!

Although the information about national parks is just placeholder information provided by the Browser template, it helps you see some of the connections between the pages. You’ll learn a bit more about these connections in the next step, [Explore the Views in the Stack Layout](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjyfvjvomy).

Before you continue, quit the simulation by choosing Quit from the simulation application menu or pressing Command-Q. Or, in Dashcode, you can click the red Stop button.

A browser-style mobile Safari web application allows users to navigate from one page to the next. As you found out when you tested it, your web application already supports the ability to select an item in the top-level list and reveal information about it in a detail view. One of the keys to this structure is the stack layout.

If you can’t already see it in the navigator, reveal the stack layout by clicking the disclosure triangles next to National Parks and, below that, next to `browser`. When you click the disclosure triangle next to `stackLayout`, you see two items: `listLevel` and `detailLevel`. In this application, the list level view contains the list of parks, and the detail level view contains the text that describes a selected park.

You can change the way the detail page is revealed when you select a row in the top-level list. To do this, follow these steps:

1. Make sure the inspector is open. If it isn’t, click the blue Info button in Dashcode’s toolbar.
2. Select `stackLayout` in the navigator.
3. Click the Attributes toolbar item in the inspector (it’s the one on the left). This should change the inspector’s title to Attributes (stackLayout).

At the bottom of the inspector is a section titled Subview Transition. The values in this section control the transitions between pages. You can choose to have pages slide in from right to left (this is the default) or other ways, such as from top to bottom. Note that you may not be able to see the effect of changing the transition type in the simulator application, but you will see the effect when you view your application on an actual device.

As you’ve seen, the mobile Safari web application you created using the Browser template is already functional even though all its data is static. To make it more useful, you can add functionality that gets current information from the web. In this step, you use Dashcode’s design tools to add a button to the detail page that performs a Google search on the featured park (you’ll add the code to support this action in the next step).

To add a button to your web application, use a button _part_. Parts are controls and views used in a web application’s user interface. Dashcode lists the available parts in the Library.

To find the appropriate button part, choose Window > Show Library and click Parts. Scroll through the list of parts until you find the Push Button part, and drag this part into your detail page on the canvas.

Double-click the button on your detail page and give it a label (you can also do this by typing the label in the Label field of the Attributes inspector for the button). You may need to resize the button to fit the label you choose. Figure 2-3 shows the new button in the detail view, before it receives a new label.

__Figure 2-3__  Adding a part to the mobile Safari web application’s user interface

!

To make the button perform a search on the featured park, you need to add behavior to the button. In the Inspector, click Behaviors (it’s the rightmost button). This shows the Behaviors pane, in which you assign handler functions to events on an object.

On the canvas, select the button you added to the detail page. In the Behaviors inspector, double-click in the Handlers column next to the `onclick` event name. Enter the name of a new function, such as `detailButtonHandler`, and press Return. If you don’t already see it, click the arrow next to the function name you entered to reveal the _source code editor_ below the canvas. Clicking the arrow reveals the `detailButtonHandler` function Dashcode inserted in your web application’s code (specifically, in the `main.js` file).

Between the braces (`{...}`), enter the following three lines of code:

```
var dsource = dashcode.getDataSource("list");
var name = dsource.selection().valueForKey("name");
document.location = ("http://www.google.com/search?client=googlet&q=" + name);
```

These lines of code do the following:

- The first line of code creates a local variable named `dsource`, and gives it the value of the data source named `list`.

  In the Browser template, the `list` data source supplies the detail page with the static information about the selected park.
- The second line of code creates a local variable named `name`, and gives it the value of the `name` property of the currently selected park.

  In a data source, each category of data is represented by a different property. In the `list` data source, the `name` property contains the name of the selected park.
- The third line of code tells the web application to display the search results for the park specified in `name`.

After you add the code for the button’s event handler, the source code editor should look similar to Figure 2-4.

__Figure 2-4__  Adding code to handle the button’s click event

!

Test your web application again by clicking Run (or by choosing Debug > Run). In the detail page for a park, click the button you added and make sure it displays the results of a Google search on the featured park (be sure you’re connected to the Internet before you try this).

Congratulations! You’ve created your first mobile Safari web application using Dashcode.

To use your application on an iPhone or iPod touch, you need to deploy the application and make it available on a web server. To learn how to do this, see [Deploying a Web Application](Testing%20and%20Sharing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjwfvjvony).

[Next](Dual-Product%20Web%20Application%20Tutorial.md)[Previous](Dashboard%20Widget%20Tutorial.md)

