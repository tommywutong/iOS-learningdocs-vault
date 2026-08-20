---
title: Dashcode User Guide
apple_id: TP40004692
resource_type: Guide
platform: Safari|Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashcode_UserGuide/Contents/Resources/en.lproj/CodeAndDebugging/CodeAndDebugging.html
archived_at: '2026-07-15T05:17:34.827397Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashcode User Guide](Introduction%20to%20Dashcode%20User%20Guide.md)


[Next](Testing%20and%20Sharing.md)[Previous](Designing%20the%20User%20Interface%20of%20a%20Widget%20or%20Web%20Application.md)

# Adding Source Code and Creating Bindings

After you’ve started a project and designed the user interface, you may need to customize the implementation by adding code, data sources, or bindings to your widget or web application. This chapter describes how to:

- View the files and data sources that make up your project
- Write custom code to perform tasks that aren’t automatically provided by the template
- Add data sources and bind them to elements in the user interface
- Write a value transformer that converts the value of a property to a version that’s appropriate for display

This chapter also shows you how to turn on access to resources, such as files outside of the project and the network. Finally, it covers the application preferences that affect your code editing experience in Dashcode.

Dashcode includes all the HTML, CSS, and JavaScript files that constitute a widget or web application. When you want to add functionality beyond what a template provides, you need to view and edit these implementation files. To show your project’s implementation files, choose View > Files. This reveals the Files list under the navigator. In the Files list, you can add, duplicate, and rename files and folders, as discussed in [Adding and Moving Files and Folders](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknlto).

When you select an HTML, CSS, JavaScript, or property list file in the Files list, the _source code editor_ appears below the canvas showing the selected file’s contents. In the code editor you can edit the actual HTML, CSS, and JavaScript files that implement your widget or web application. For more on coding using HTML, CSS, and JavaScript, read [Using HTML, CSS, and JavaScript Programming Interfaces](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltc).

Above the text view portion of the source code editor are two pop-up menus, a file history menu on the left and, in some cases, a function menu to the right of that. The file history menu lists the text files and data sources that you've recently edited or viewed in the source code editor. When you select a file or data source in the file history menu, it’s displayed in the source code editor. When you first open a project, the file history menu contains the files you’re most likely to open, such as `main.js`, `main.css`, and `index.html` or `main.html`. Depending on the file you’re currently viewing in the source code editor, the function menu lists the names of all the functions in a JavaScript file or all the rules in a CSS file. Note that the function menu is not available when viewing HTML files, property list files, or data sources.

One common way to add code is to add an event handler to an element in the user interface. You do this using the Behaviors inspector, as discussed in [Adding a Handler for an Event](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknlti). If you’re using Dashcode version 3.0 and later, a common reason to add code is when you need a value transformer to provide an appropriate value to display, based on other information in your project. You do this using the Bindings inspector, as discussed in [Adding a Value Transformer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcmy).

When working with resources originating outside a widget or web application—`XMLHttpRequest`, command-line tools, Java applets, and such—you need to explicitly turn on access to these items. To learn more about resource access and what elements need activation, read [Resource Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknlte).

You can also modify how the source code editor looks and behaves, as described in [Code Editing Preferences](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltg).

Dashcode supports the use of data sources and bindings to give you an easy, efficient way to get source data into the user interface and keep the display in sync with the data. A _data source_ represents data from a source that can be remote, such as an RSS feed, or a local object, such as a list. A _binding_ is a connection between a specific property or attribute in the data source and a property of an element on the canvas.

To show the data sources in your project click the data source button at the bottom of the navigator (the button looks like a circle with a square inside it). This reveals the Data Sources list in the navigator. In this list you can add, remove, and rename data sources, as described in [Adding or Changing a Data Source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcni).

Select a data source in the Data Sources list to see a graphical representation of its layout in the source code editor below the canvas. This representation is called the _data model_ and it shows you the structure of the data source, the data types of the properties in it, and, when possible, a preview of the data. You can use the data model view to create bindings and to see at a glance which user interface elements have bindings to properties in the data source. To learn how to create bindings, see [Creating Bindings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcnq). To see which elements have bindings to properties in the selected data source, move the pointer over an existing binding in the data model: Dashcode flashes the connected element on the canvas.

In the data model view, Dashcode displays the hierarchical organization of the data source, using disclosure triangles to indicate properties that contain children. Open a disclosure triangle to reveal a box containing a list of child properties. When you move the pointer over a child property, Dashcode highlights all its ancestor properties.

Each property is accompanied by an icon that indicates its data type:

- ![../Art/attribute.jpg](attachments/Art/attribute.jpg) (Attribute)
- ![../Art/bool.jpg](attachments/Art/bool.jpg) (Boolean)
- ![../Art/num.jpg](attachments/Art/num.jpg) (Number)
- ![../Art/obj.jpg](attachments/Art/obj.jpg) (Object)
- ![../Art/string.jpg](attachments/Art/string.jpg) (String)

When a data source contains an array of properties of the same type, the array is represented by an icon that looks like a stack of data type icons. For example, an array of strings is represented by this icon: ![../Art/string_array.jpg](attachments/Art/string_array.jpg)

If a data source has access to actual data (when, for example, you’ve specified a feed URL or you supply static data), data is displayed to the right of a property’s name. When the property value is an array, Dashcode displays the total number of array members and provides arrow controls you can use to step through the array. One array member at a time is displayed in a box revealed by a disclosure triangle.

When you hover over a property name, Dashcode displays a help tag that provides the key path of the property and its data type. The _key path_ represents the property’s position in the hierarchy. A key path for a property named _property_n_ is of the form _property_1_._property_2_._[...]_._property_n_, where _property_1_ is the root-level ancestor. For example, the Podcast template contains a data source that represents podcast data. The key path that locates the podcast title property in the data hierarchy is `content.channel.title`.

Dashcode displays all existing bindings to the far right of a data source property. When no binding yet exists, Dashcode displays a _binding control_ (a small circle) when you move the pointer over a property’s row. When you position the pointer over the binding control itself, it displays a plus symbol (+).

Existing bindings are displayed in a capsule to the right of a property; the capsule is visible until you remove the binding. Usually, the binding capsule contains a delete control on the left (it looks like an X), the property of the user interface element to which the item is bound, and a binding control on the right. However, if a single data source property has multiple bindings the capsule displays a disclosure triangle on the left and the word “Multiple” in place of the user interface property. Open the disclosure triangle in the capsule to reveal the set of bindings for that data source property.

A good example of a property with multiple bindings is the `queryInProgress` property of the feed data source in the RSS template for web applications. This data source property is bound to both the visible and animating properties of the activity indicator part on the canvas. This ensures that when the application runs, the activity indicator is visible only while a query is in progress and that it spins until the query is finished.

As mentioned in [Changing an Element’s Properties](Designing%20the%20User%20Interface%20of%20a%20Widget%20or%20Web%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnjnknlte), you can also view and change bindings in the Bindings inspector. Whereas the data model view gives you a bindings-centric perspective on these connections, the Bindings inspector gives you an element-centric perspective. The Bindings inspector displays the bindable properties of the currently selected element and provides controls to create and change bindings. If a binding already exists on a property, the Bindings inspector displays the data source name and the complete key path of the bound property in the data source.

After you’ve revealed a project’s source code, you can modify its HTML, CSS, and JavaScript files, as discussed in [Viewing a Project’s Source Code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltk). Any HTML, CSS, or JavaScript code that works in Safari and its WebKit engine can be used in a widget or web application. To learn more about HTML, CSS, and JavaScript, read these documents:

- _Safari FAQ_
- _[WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483)_
- _[Safari HTML Reference](../Safari%20HTML%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanbz)_
- _[Safari Web Content Guide](../Safari%20Web%20Content%20Guide/Developing%20Web%20Content%20for%20Safari.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjr)_
- _WebKit DOM Reference_

To learn more about creating a webpage or web application optimized to run in Safari on iPhone, see _[Safari Web Content Guide](../Safari%20Web%20Content%20Guide/Developing%20Web%20Content%20for%20Safari.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjr)_.

In addition to WebKit’s HTML, CSS, and JavaScript programming interfaces, Apple offers Dashboard-specific programming interfaces for use in widgets. For more on these programming interfaces, read _[Dashboard Programming Topics](../Dashboard%20Programming%20Topics/Introduction%20to%20Dashboard%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqmzx)_ and _[Dashboard Reference](../Dashboard%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmzz)_.

All Dashcode templates support data sources to represent the data provided to the widget or web application. Data sources and bindings work together to dispense data to user interface elements and allow them to stay in sync when the data changes. (See [Creating Bindings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcnq) to learn how to create bindings.)

For your convenience, all project templates include at least one data source, even if the data source does not represent any actual data. For example, the Browser template includes a data source that represents static data from a JavaScript file included in the default project. The RSS template includes a data source that can represent data from an RSS feed; you see actual data when you supply a specific feed URL.

To add a new data source, reveal the Data Sources list in the navigator (as described in [Viewing a Project’s Data Sources and Bindings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcna)) and select New Data Source in the action menu below the list. Or, select File > New > Data Source. When you do this, the new data source appears in the list. (If you have a dual-product project, the new data source is automatically available in both products.)

To specify the location of a data source, you supply a URL for a JSON or XML feed. Note that you can also supply the local path of a file of static data to serve as the data source. You do not need to specify a location for a data source that represents a list or grid part.

There are two ways to supply the location of a data source, depending on the template your project uses. For all projects, you can enter a URL in the data model view of the new data source (you reveal the data model view when you select the data source in the Data Sources list). For projects based on RSS, Podcast, Maps, Photocast, Video Podcast, or Daily Feed templates, you can also enter a URL in the Properties section of the widget attributes or application attributes pane.

If you’ve entered a valid URL, Dashcode updates the data model view to display the available properties and attributes of the data, along with some actual data when possible.

All Dashcode templates support bindings, which allow a user interface element to get specific items of data from a data source and automatically update its display when that data changes.

Dashcode offers an easy way to create bindings in the data model view. To find out how to reveal this view and for a description of its contents, see [Viewing a Project’s Data Sources and Bindings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcna).

To create a binding between a data source property and an element on the canvas:

1. Press and hold the mouse button on the circular binding control next to the data source property, and drag the pointer to the element on the canvas that you want to bind to.

   As you drag, a connection line extends from the binding control, and each element on the canvas highlights as you pass the pointer over it. (You can see an example of how this looks in [Figure 3-8](Dual-Product%20Web%20Application%20Tutorial.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjzfvjvomju).)
2. Release the mouse button when the element you want to bind to is highlighted.

   As soon as you stop dragging, Dashcode displays a contextual menu that lists the bindable properties of the selected element.
3. Choose the appropriate property to complete the binding.

   If you choose not to complete the binding after you stop dragging, simply click outside of the contextual menu and the binding is not created.

If the Bindings inspector wasn’t visible before, it opens when you complete a binding, allowing you to specify a value transformer and placeholder text or values.

You can also create bindings in the Bindings inspector, without dragging from the data model view. To do this, follow these steps:

1. Select the element you want to bind to on the canvas or in the navigator.

   When you do this, the Bindings inspector displays the bindable properties of the element.
2. In the Bindings inspector, open the disclosure triangle to the left of the element property you want to bind to.
3. Select the “Bind to” checkbox and choose a data source from the pop-up menu.
4. Open the Key Path pop-down menu to reveal the top-level properties of the selected data source.
5. Choose a data source property in the Key Path menu.

   If the data source property you’re interested in is a child of a top-level property, click the pop-down control again to see a list of the current property’s children. Continue choosing child properties until you reach the one you want.

Because bindings are tightly integrated with user interface objects, you must create bindings separately in both products of a dual-product project. This is because each product uses different parts to display data, even though they can share a single data source.

A value transformer is a function that takes a data source value and returns an appropriate display value, based on other information in the data source or contextual information in your code. For example, you might want to transform a temperature value from Fahrenheit to Celsius, or format a numerical value as a currency value.

Because a value transformer may need to interpret the data model and make decisions based on context, you must usually write it yourself. That said, Dashcode includes a few generic value transformers you can use, such as a reverse-value function. To specify a value transformer open the Bindings inspector and:

1. Select the user interface element that is bound to the data source item you want to transform.
2. Click the Value Transformer text field.

   Dashcode displays the generic value transformers, along with any value transformers you’ve already included in your project, in a pop-down list.
3. Select an existing function or type the name of the function you plan to write and press Return.

   If you select an existing value transformer, Dashcode displays an arrow control that you can click to see the function in the source code editor.

   If you supply the name of a new value transformer, Dashcode inserts the new function in your project’s JavaScript file and displays it in the source code editor. You can then add custom code that performs the transformation.

Dashcode includes several built-in value transformers in the `transformers.js` file. You can customize some of these transformers by changing the default parameters. For example, the truncation value transformer (`DC.transformer.Truncated`) automatically truncates the passed-in string to 10 characters, but you can change this by editing the transformer function. The `transformers.js` file contains the following value transformers:

- `DC.transformer.Boolean` returns the Boolean value `TRUE` if the passed-in value is equal to a value you supply as the “true value.” For example, you might designate the string “red” as the true value. Changing the Boolean value transformer to use this string, this value transformer returns `TRUE` when the passed-in value is “red.”

  You can also specify a reverse transformation for this function. If you want to do this, you also need to supply a “false value” that the function can use to test the passed-in value against. In this case, the transformer returns either the true or false value that you supplied, depending on which one the passed-in value matches.
- `DC.transformer.FirstObject` returns the first object in an array.
- `DC.transformer.Matches` returns the Boolean value `TRUE` if the passed-in value matches a regular expression you define.
- `DC.transformer.Not` returns the opposite Boolean value of the passed-in value (that is, it returns `TRUE` for a value whose Boolean value is `FALSE`).
- `DC.transformer.StringToObjects` creates a JavaScript object from a passed-in array, or, in reverse, creates a string from a passed-in object.
- `DC.transformer.Truncated` truncates the passed-in string to a number of characters that you define (or 10, by default), and adds an ellipsis.

When you add a handler using the Behaviors inspector (as discussed in [Changing an Element’s Properties](Designing%20the%20User%20Interface%20of%20a%20Widget%20or%20Web%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnjnknlte)), the new handler function is inserted in the project’s JavaScript file. When you click the arrow in the Behaviors inspector next to the handler function’s name, the source code editor appears under the canvas with the function selected. You can then add your custom code to handle the event.

For more on using the source code editor, read [Viewing a Project’s Source Code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltk). To learn about JavaScript and the Dashboard programming interfaces, read [Using HTML, CSS, and JavaScript Programming Interfaces](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltc).

You might want to allow users to run your web application even if they lose their network connection. You can do this by taking advantage of the `manifest` attribute available in the HTML 5 specification. The value of the `manifest` attribute is the URL of a file that contains the resources your web application needs to have cached in order to run offline.

To enable offline usage of your web application, select the Offline Viewing checkbox in the General section of the application attributes pane. Dashcode adds the `manifest` attribute to the `HTML` element in the `index.html` file.

Dashcode helps you support offline usage of your web application by providing some code snippets you can use to query and respond to changes in online status. You can elect to receive these events when the user goes online or offline, and you can write code to update the user interface or access different resources, as necessary.

By default, Dashcode creates two products in a web application project: a mobile Safari web application (a web application optimized to run in Safari on iPhone) and a Safari web application. As described in [Creating a Project from a Template](Starting%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnbnknltg), after you select a template to start your project, you choose whether you want to create both products, or only one.

Before you add or remove a product from your existing project, it’s important to understand how Dashcode organizes the files in your project. In a dual-product project, you see the following files and folders at the root level of the Files list (among other, optional files and folders):

- The safari folder contains all the files and parts that are unique to the Safari web application.
- The Images folder contains all the images that are common to both products.
- The `index.html` file is the main HTML file for the project.
- The mobile folder contains all the files and parts that are unique to the mobile Safari web application.
- The Parts folder contains Dashcode parts and other code files that are common to both products.

As you can imagine, a project that creates only a mobile Safari web application does not contain a safari folder, and a project that creates only a Safari web application does not contain a mobile folder.

If you have a dual-product project, you can remove a product by choosing File > Delete _Current_ Product, where _Current_ is “Safari” or “Mobile Safari,” depending on which product is currently selected.

If you want to add a product to a single-destination project, choose File > Add _Other_ Product, where _Other_ is “Safari” or “Mobile Safari,” and represents the product you want to add.

If you want to modify a web application by changing or adding a view, such as a detail view, it’s recommended that you add code to control it. Each view in a web application is controlled by a JavaScript controller object. The controller object is in charge of configuring the interface within a view so that it displays properly, and so that the view can handle all activity that occurs within it.

If you add a list or grid part, you can write a controller for it that supplies data dynamically or you can bind the list to an array property in a data source. Or, you can combine these approaches and use bindings to get the number of rows and the data for each row, and a controller to configure each row.

For more information on some of the parts you can add to your web application, see [Dashcode Parts](Dashcode%20Parts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjufvjvoni). To learn about JavaScript and the Dashboard programming interfaces, read [Using HTML, CSS, and JavaScript Programming Interfaces](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltc).

Dashcode’s source code editor includes a code completion feature that suggests possible variable and function names based on partially entered text. When Code Sense has a suggestion, it underlines the text you’re typing. To see the list of suggestions, press the Option and Escape keys. Use the Up and Down Arrow keys to select the symbol you want. To add the symbol, press the Tab key. To dismiss the suggestion list, press the Escape key.

See [Code Editing Preferences](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltg) for more information on how to set Code Sense preferences.

Dashcode includes a set of reusable _code snippets_. Each code snippet provides a bit of functionality that you can use to enhance your widget or web application. To show the code snippets, choose Window > Show Library and click the Code button. To add a code snippet to your project, drag it from the Code Library to the source code editor.

In addition to the code snippets included with Dashcode, you can save your own snippets for later use by dragging them from the source code editor to a group you create in the Code Library. To create a new group, choose New Group from the action menu under the listings in the Code Library.

You can add additional files and folders to a widget or web application in Dashcode. Although this is rarely necessary, it can be helpful when organizing numerous files or areas of functionality. To add a new file, show the files list, choose File > New and choose either JavaScript File, CSS File, or File. After you create a new file, you can view and edit its contents as described in [Viewing a Project’s Source Code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltk).

To add a folder to your project, choose File > New > Folder. To add items to the folder, drag them on to its icon.

In the Files list, you can rename, duplicate, move, and delete files and folders. To rename an item, select it in the Files list and choose Rename from the action menu (the gear icon beneath the Files list). To duplicate an item, choose Duplicate from the action menu. To remove an item, choose Move to Trash from the action menu. To move an item, drag its icon to another folder’s icon.

If you intend to use any of the following resources in your widget, you need to turn on access to them first:

- Network resources (including `XMLHttpRequest`)
- External files
- Internet plug-ins, such as QuickTime and Quartz Composer
- Java applets
- Command-line applications

Turn on access to these resources, select Widget Attributes in the navigator. Then select the option for the resource you want to use. Options include:

**_Network / Disk Access_**
: If your widget requires access to network resources or files on disk, select the appropriate item. Unless your template already needs access to network resources (such as `XMLHttpRequest`) and files on disk outside of your widget bundle, these resources are turned off.

**_Extensions_**
: If your widget uses content provided through an Internet plug-in or a Java applet, or uses a command-line utility via `widget.system`, select the appropriate option. Unless your template already needs access to plug-ins (such as QuickTime), Java, and command-line utilities, these resources are turned off.

The source code editor has a number of preferences you can set to change its behavior to better suit your tastes. To show these preferences, choose Dashcode > Preferences. The Preferences window includes the following items:

- General preferences include an option for opening source code files in Dashcode or in a helper application.
- The source code editor has various visibility and behavior preferences, including the visibility of the gutter and line number next to your source code, the source code editor’s line wrapping, and the Tab key’s indentation behavior. You can set these preferences in Editing preferences.
- Your source code can be colored based on the code’s syntax. You can adjust text font, size, and color in Formatting preferences.
- Dashcode offers a code completion feature called Code Sense (as described in [Code Completion Using Code Sense](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltq)). At the top of the source code editor, a pop-up menu shows the symbols in a file. Code Sense preferences include a setting for how these symbols are organized. This pane also includes settings for code completion.

[Next](Testing%20and%20Sharing.md)[Previous](Designing%20the%20User%20Interface%20of%20a%20Widget%20or%20Web%20Application.md)

