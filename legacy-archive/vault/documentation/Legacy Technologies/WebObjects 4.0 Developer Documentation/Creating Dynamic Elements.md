---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DynamicElements3.html
archived_at: '2026-07-18T01:25:56.768495Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Attributes.md)

# Creating Dynamic Elements

There are several ways to add dynamic elements to your component.

## Using the Toolbar

You create dynamic elements in the same way that you create other elements: by clicking buttons in the toolbar or using the menu commands. In WebObjects Builder, there are two groups of buttons in the switchable toolbar that allow you to create dynamic elements:

- The Forms toolbar ! allows you to create dynamic form elements. See ["Creating Form-Based Dynamic Elements"](Creating%20Form-Based%20Dynamic%20Elements.md#apple-gy2danq) for more detailed information about working with forms.
- The Other WebObjects toolbar ! allows you to create all other types of dynamic elements. See ["Creating Other WebObjects"](Creating%20Other%20WebObjects.md#apple-guydooi) for more details on each type of element.

## Dragging Elements into the Component Window

Some elements can be created by dragging an item from the file system into a component window. These include:

- Components (see ["Reusable Components"](Reusable%20Components.md#apple-gezdambq))
- Client-side Java components (see ["WOApplets"](DynamicElements20.md#apple-gyytomi))
- Image files and image maps (see ["Dynamic Images"](DynamicElements19.md#apple-g4ztiny))

In addition, you can also drag a model file (of type __.eomodeld__) into a component to create a variable of type WODisplayGroup (see ["Adding Display Groups"](DynamicElements6-2.md#apple-heyteni)).

Certain file types (such as __.gif__, __.jpeg__, __.tif__, __.eps__, and __.bmp__) are automatically recognized by WebObjects Builder. The Preferences Panel (which you display by choosing Tools !Options) shows a list of file extensions that WebObjects Builder accepts. You can drag any item with one of those file extensions into a component window, and the item will be added to your project. You can add file types if you need them.

!

## Using the Add WebObject Panel

The Add WebObject panel is an advanced feature for those who wish to work in source editing mode. It allows you to add a dynamic element and set its bindings by hand.

- In other source editing or graphical mode, place the cursor at the point in the HTML template where you want to add the element.
- Choose Tools !Add WebObject.

A panel appears that allows you to create a dynamic element by entering its class and its name. The name is used by the HTML template and declarations (__.wod__) file to uniquely identify the element. (Normally, you allow WebObjects Builder to generate names for you, but if you add elements in source editing mode, you must specify their names.)

- Click Add.

The element appears in the HTML template.!

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](The%20Object%20Browser.md)
