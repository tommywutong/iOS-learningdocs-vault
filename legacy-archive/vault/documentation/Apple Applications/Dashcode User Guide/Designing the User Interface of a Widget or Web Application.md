---
title: Dashcode User Guide
apple_id: TP40004692
resource_type: Guide
platform: Safari|Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashcode_UserGuide/Contents/Resources/en.lproj/DesignTools/DesignTools.html
archived_at: '2026-07-15T05:17:37.966517Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashcode User Guide](Introduction%20to%20Dashcode%20User%20Guide.md)


[Next](Adding%20Source%20Code%20and%20Creating%20Bindings.md)[Previous](Starting%20a%20Project.md)

# Designing the User Interface of a Widget or Web Application

After you’ve started a project as discussed in [Starting a Project](Starting%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnbnknltc), use Dashcode’s design tools to design the interface of the widget or web application. This chapter describes the canvas, the interface design area in Dashcode, and how to begin laying out an interface. It also discusses how to add Dashcode parts to your project and how to use the inspector window to adjust the appearance or behavior of a part.

Read this chapter to learn how to use Dashcode’s design tools to create, modify, and preview the appearance of your widget or web application.

Dashcode includes a workspace where you lay out the elements that comprise the user interface of a web application or a widget. This workspace, called the _canvas_, is visible in the main portion of the project window when you select your widget or web application in the navigator. You can freely move and resize any element in an interface when the canvas is visible. To move an element, drag it to where you want it to be. To resize an element, drag one of its resize handles. If you hold down the Shift key while resizing an element, the original proportions are maintained.

Dashcode also provides commands you can use to arrange and align elements in a widget or web application interface. For more on how to do this, see [Arranging and Locking Elements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnjnknltg).

You can drag any item from the Finder to the canvas to add it to a your widget or web application. This means that you can design the user interface in an application such as Adobe Illustrator or Photoshop, save the images, and drag them into your Dashcode project from the Finder. Dashcode, however, offers its own design elements. Learn about them in [Adding Parts to an Interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnjnknlti).

By default, all new widgets created from a Dashcode template have two sides: a front and a back. The canvas shows you only one of these sides at a time. To switch between the sides, click front or back in the navigator. (If you don’t see front and back in the navigator, click the disclosure triangle next to the widget’s name.)

When a side is visible on the canvas, you can add and arrange elements on it. To work on the other side, click the corresponding name in the navigator.

Dashcode includes a set of controls, shapes, and views called _parts_. Choose Window > Show Library and click the Parts button to see the parts included with Dashcode.

Some parts are appropriate only for specific products. The Library displays only those parts that can be used in the product that is selected in the currently active project. For example, in Dashcode 3.0, you see a different set of parts when you switch between the Safari and mobile Safari products of your dual-product web application project. Similarly, the Library shows a different set of parts when you switch between a web application project and a widget project.

To add a part to a widget’s or web application’s interface, drag it from the Parts Library to the widget body or web application page on the canvas. Once a part is on the canvas, you can change its properties, as discussed in [Changing an Element’s Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnjnknlte). If you want to know more about laying out parts in your project’s user interface, read [Arranging and Locking Elements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnjnknltg).

A number of Dashcode parts can be manipulated programmatically. Read [Dashcode Parts](Dashcode%20Parts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjufvjvoni) to learn more about using these parts.

You can drag any photo in your iPhoto library to the canvas to include it in a widget or web application. To show your iPhoto library, choose Window > Show Library and click the Photos button. Once the photo is on the canvas, you can arrange it as described in [Arranging and Locking Elements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnjnknltg) and adjust its properties as discussed in [Changing an Element’s Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnjnknlte).

The inspector window reveals information about the selected element on the canvas. In this window, you can view and edit the element’s properties based on the inspector type you choose. Choose an inspector by clicking its button at the top of the window. The inspector window includes the following inspectors, from left to right:

- The Attributes inspector allows you to modify the selected element’s ID (used in JavaScript to reference the element), its CSS class, whether it’s shown in the widget or web application and in the default image, and any parameters that are unique to the element.
- If it’s appropriate for the selected element, the Fill & Stroke inspector allows you to adjust its style and add effects. Style adjustments you can make include:

  - Fill, such as solid, gradient, or image
  - Corner roundness, opacity, and reflection
  - Stroke color and width

  Effects you can add include:

  - Glass, including control over shine, tone, horizon, and curvature
  - Recess, including control over depth, shadow, and highlights
- The Metrics inspector allows you to modify the selected element’s size and position, as well as its behavior if the widget or webpage is resized. The Layout pop-up menu allows you to select whether the element should be positioned using absolute or document-flow positioning (learn about these positioning styles in [Absolute versus Document-Flow Positioning](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnjnknltcma)). The Autoresize settings affect how an element behaves when the widget or webpage is resized on the canvas. Note that the values in the Size section reflect the actual dimensions of the selected element, including borders.
- If the selected element displays text, you can adjust the text’s font, style, color, size, shadow, alignment, and spacing in the Text inspector. You can also set whether text wraps or not and how to handle text overflow. Setting the text overflow to Clip cuts any string in the selected element at its bounds, allowing for no overflow, whereas setting the text overflow to Ellipsis appends an ellipsis character (…) to the selected element’s text when it reaches the element’s bounds.
- The Bindings inspector allows you to set and adjust bindings between a data source and specific properties of the selected element. For each bindable property of the element, you can specify the data source to bind to, the key path of the item in the data source, a value transformer, and placeholder values. (To learn about value transformers, see [Adding a Value Transformer](Adding%20Source%20Code%20and%20Creating%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcmy).)

  You do not have to use the Bindings inspector to create bindings. Instead, you can drag connections from items in the data model view to elements on the canvas or listed in the navigator. (To learn how to show the data model view, see [Viewing a Project’s Data Sources and Bindings](Adding%20Source%20Code%20and%20Creating%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcna); to learn how to create bindings, see [Creating Bindings](Adding%20Source%20Code%20and%20Creating%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcnq).) However, you must use the Bindings inspector to specify a value transformer or supply placeholder values.
- The Behaviors inspector allows you to assign to the selected element JavaScript handlers for various events. For each event, you can assign an existing JavaScript function as its handler or create an empty function that’s automatically added to the project’s JavaScript code. After you assign a handler to an event, click the arrow next to the handler’s name to reveal the function in the source code editor.

  Working with code is discussed in [Adding Source Code and Creating Bindings](Adding%20Source%20Code%20and%20Creating%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltm).

Dashcode offers helpful options for arranging elements on the canvas. If an element is obscured by other elements, select it and choose Arrange > Bring Forward or Arrange > Bring to Front to move it in front of any elements currently obscuring it. Similarly, if you want to move an element behind another, select it and choose Arrange > Send Backward or Arrange > Send to Back.

Dashcode offers alignment and distribution options for arranging multiple elements with respect to each other. If you want to align a few items on their left edges, you select them on the canvas and choose Arrange > Align > Left. Similar options are available to align elements by center, right, top, middle, and bottom. If you want an equal amount of vertical space between multiple elements, choose Arrange > Distribute > Vertically. A similar option exists to distribute elements horizontally.

If you want to lock an element so that you can no longer move it, select the element and choose Arrange > Lock. If you change your mind and want to move it again, select it and choose Arrange > Unlock. Note that locking an element only locks its placement on the canvas—you can still adjust its attributes in the inspector.

Dashcode allows you to position elements in your widget or web application using either absolute or document-flow (that is, relative) positioning. You can change the positioning of a selected element by switching between Absolute and Document Flow in the Layout section of the Metrics inspector.

Briefly, absolute positioning means that an element’s position within its containing element is always the same, regardless of the positions of its sibling elements. In other words, an absolutely positioned element retains its position within the containing element, even if the sibling elements around it expand or shrink. Absolute positioning allows you to have precise control over complicated layouts, but does not support dynamic resizing very well.

In contrast, document-flow positioning means that an element’s position is defined in terms of the positions of its document-flow sibling elements. In document-flow positioning sibling elements are displayed in order, vertically, so the position of an individual element depends on its location in the series of elements. If one element expands downward, it pushes down all the sibling elements that come after it by the same amount, without changing their sizes or their relative positions. Although document-flow positioning provides great flexibility to support dynamic resizing, it does not give you fine-grained control over layouts.

Because widgets tend to stay the same size (or switch among a small number of predefined sizes), Dashcode widget projects use absolute positioning by default. Conversely, because web applications need more flexibility in sizing, Dashcode web application projects use document-flow positioning for most elements by default.

The default positioning style used in a project does not mean that there are no variations, however. In the Browser template web application project, for example, the elements in the list row (the row title and the row arrow) are absolutely positioned to ensure a consistent layout.

When you customize a project, you should be aware of the positioning style of the element you’re changing. This is because dragging a part into an existing container element on the canvas causes the part to adopt the prevailing positioning style of its new siblings. If you want the new part to adopt the alternate positioning style, hold down the Shift key while you drag the part onto the canvas.

Use the search field in the toolbar to find elements in your project’s interface and code. This particular type of search works when you’re designing and coding a widget or web application. When Dashcode is running a widget, the toolbar’s search field narrows results from either the run log or the Stackframe & Variables table, depending on which is visible. This is discussed further in [The Run Log and Tracing Execution](Testing%20and%20Sharing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjwfvjvomi) and [Checking Values in Memory](Testing%20and%20Sharing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjwfvjvomy).

To search for an element, type part of the element’s name in the search field. When the search results are returned, the navigator is replaced with search results. Selecting an item in the search results either highlights it on the canvas or shows the source code file that contains the implementation of the element.

By default, the canvas displays rulers along its top and left sides. Rulers, when used with guides, help you align elements relative to one another. To add a guide, position the pointer anywhere in a ruler and drag towards the canvas. As you drag away from the ruler, a guide appears—it remains wherever you stop dragging. To remove a guide, drag it back to a ruler. To hide the rulers, choose View > Hide Rulers.

Users click a widget’s close box to close it (web applications do not have a close box). By default, a widget’s close box appears over the top left of a widget’s body. If necessary, move the close box so that it overlaps the top left corner of your widget’s body. To hide the close box on the canvas, choose View > Hide Invisible Items.

Because the canvas generates HTML and CSS automatically for you, you may want to turn its code generation off if you’re tweaking elements by hand. To turn off the automatic code generator, choose View > Stop Code Generator. When you’re finished tweaking values by hand, you can turn the code generator back on by choosing View > Start Code Generator.

The default image preview shows you a widget’s default image, which is displayed while it loads in Dashboard. To see your widget’s default image, select Default Image in the navigator.

By default, all the elements on the front of a widget except the text parts (Text, Text area, and Text field) are included in a widget’s default image. Other parts that display text, such as pop-up menus, are also included. You are discouraged from leaving text in your widget’s default image because any text on your interface may change when the widget is localized. Therefore, you should remove parts that display text from your widget’s default image. To remove any element from your widget’s default image, follow these steps:

1. Select the widget item in the navigator to show the canvas.
2. Select the element on the canvas that you want removed from the default image.
3. Show the Attributes inspector (as discussed in [Changing an Element’s Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnjnknlte)).
4. Deselect Show in Default Image.

The toolbar below the default image preview offers additional configuration options for default images:

**_Start Sync / Stop Sync_**
: By default, Dashcode updates a widget’s default image whenever the widget’s interface changes. To turn this behavior off, click Stop Sync. To enable this behavior if it’s been turned off, click Start Sync.

**_Import_**
: If you already have an image that you want to use as a widget’s default image, click the Import button and select it in the dialog that appears.

**_Open in External Editor_**
: If you want to tweak your default image in an application other than Dashcode, click the Open in External Editor button. When you do, the default image as shown in Dashcode is opened in your default PNG-handling application.

You can use the widget icon editor to design a widget’s icon. The widget icon represents a widget in the Dashboard widget bar and in the widget manager. To show the widget icon editor, select Widget Icon in the navigator.

To modify the appearance of the body of the widget icon, show the Fill & Stroke inspector and change the fill style, corner roundness, opacity, and stroke style. The toolbar at the bottom of the widget icon editor offers additional configuration options for widget icons:

**_Start Sync / Stop Sync_**
: By default, Dashcode syncs the style of a widget’s front image with its widget icon. To turn this behavior off, click Stop Sync. To enable this behavior if it’s been turned off, click Start Sync.

**_Place_**
: To put an image, such as a logo, on a widget’s icon, click the Place button and select the image file. Once the image is placed, you can move and resize it.

**_Import_**
: If you already have an image that you want to use as a widget’s icon, click the Import button and select it in the dialog that appears.

**_Open in External Editor_**
: If you want to customize a widget icon in an application other than Dashcode, click the Open in External Editor button. When you do this, the icon is opened in your default PNG-handling application.

A mobile Safari web application can provide a Web Clip icon for users to place on their Home screens and use as a type of bookmark for the application. When a user taps a Web Clip icon the web application opens automatically, without requiring the user to navigate to it. Web Clip icons should be simple, attractive, and easy for users to recognize.

Providing a Web Clip icon is a good idea for most mobile Safari web applications, but for those that can run in full-screen mode, it's essential. This is because the only way users can experience a web application's full-screen mode is by tapping its Web Clip icon to open it. For more information on specifying the mode your web application can run in, see [Application Attributes for Mobile Safari Web Applications](Starting%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnbnknlts).

You can use the Web Clip Icon composer to design your application’s icon. To show the Web Clip Icon composer, select Web Clip Icon in the navigator.

To modify the appearance of the body of the icon, show the Fill & Stroke inspector and change the fill style, opacity, and stroke style. The toolbar at the bottom of the Web Clip Icon composer offers additional configuration options for these icons:

**_Place_**
: To put an image, such as a logo, on a web application’s icon, click the Place button and select the image file. Once the image is placed, you can move and resize it.

**_Import_**
: If you already have an image that you want to use as a web application’s icon, click the Import button and select it in the dialog that appears.

**_Open in External Editor_**
: If you want to customize a web application icon in an application other than Dashcode, click the Open in External Editor button. When you do this, the icon is opened in your default PNG-handling application.

A Safari web application should include a favicon (an abbreviation of the term “favorites icon”), which visually identifies the web application in the browser. Typically, a browser that supports favicons displays them in the address field and in bookmarks or history lists. A browser that supports tabbed browsing may also display a favicon next to the web application’s title in a tab.

Providing a distinctive favicon is a good idea because it helps users recognize your web application. You can specify your favicon in Dashcode’s Favicon composer. To show the Favicon composer, select Favicon in the navigator.

You can create your favicon in two sizes: 32 x 32 pixels and 16 x 16 pixels. The smaller size can be used by all browsers that support favicons. Creating a 32 x 32 pixel version of your favicon is optional, because some browsers ignore it or merely scale it down before displaying it.

The toolbar at the bottom of the Favicon composer offers the following options for designing a favicon:

**_Import_**
: If you have an image that you want to use as a favicon, click the Import button and select it in the dialog that appears.

**_Open in External Editor_**
: If you want to customize a favicon in an application other than Dashcode, click the “Open in External Editor” button. When you do this, the favicon is opened in your default ICO-handling application.

Dashcode updates the favicon in your project when you save the changes you made in an external editing application.

[Next](Adding%20Source%20Code%20and%20Creating%20Bindings.md)[Previous](Starting%20a%20Project.md)

