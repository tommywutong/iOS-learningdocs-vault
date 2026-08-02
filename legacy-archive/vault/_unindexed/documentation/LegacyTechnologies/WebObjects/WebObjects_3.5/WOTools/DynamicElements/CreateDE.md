---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/DynamicElements/CreateDE.htm
archived_at: '2026-07-15T07:56:19.098305Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!](DynElTOC.md)[Table
of Contents](DynElTOC.md) [!](Attribut.md)[Previous
Section](Attribut.md) 

# Creating Dynamic Elements

There are several methods of adding dynamic elements
to your component.

## Using the Toolbar

You create dynamic elements in the same way that you
create other elements: by clicking buttons in the toolbar or using the
menu commands. In WebObjects Builder, there are two groups of buttons in
the switchable toolbar that allow you to create dynamic elements:

- The Forms toolbar ! allows you to create dynamic
  form elements. (You can also create standard HTML form elements using this
  toolbar.) See ["Creating Form-Based Dynamic
  Elements"](FormBase.md#apple-gy2danq) for more detailed information about working with forms. 
- The Other WebObjects toolbar ! allows you to
  create all other types of dynamic elements. See ["Creating
  Other WebObjects"](CreateWO.md#apple-guydooi) for more detailed information about each type of
  element.

## Dragging Elements into the Component Window

Some elements can be created by dragging an item from
the file system into a component window. These include:

- Components (see ["Reusable Components"](ReuseCmp.md#apple-gezdambq)) 
- Client-side Java components (see ["WOApplets"](WOApplet.md#apple-gyytomi)) 
- Image files and image maps (see ["Dynamic Images"](DynImgs.md#apple-g4ztiny))

In addition, you can also drag a model file (of type
__.eomodeld__) into a component to create a variable of type WODisplayGroup
(see ["Adding Display Groups"](AddDspGp.md#apple-heyteni)).

Certain file types (such as __.gif__, __.jpeg__,
__.tif__, __.eps__, and __.bmp__) are automatically recognized
by WebObjects Builder. The Preferences Panel (which you display by choosing
Tools !Options) shows a list of file extensions
that WebObjects Builder accepts. You can drag any item with one of those
file extensions into a component window, and the item will be added to
your project. You can add file types if you need them.

!

## Using the Add WebObject Panel

The Add WebObject panel is an advanced feature for
those who wish to work in source editing mode. It allows you to add a dynamic
element and set its bindings by hand.

1. In source editing mode, place the cursor at the point in the HTML template
   where you want to add the element. 
2. Choose Tools !Add WebObject. 

A panel appears that allows you to create a dynamic element by entering
its class and its name. The name is used by the HTML template and declarations
(__.wod__) file to uniquely identify the element. (Normally, you allow
WebObjects Builder to generate names for you, but if you add elements in
source editing mode, you must specify their names.)

3. Click Add. 

The element appears in the HTML template. A template appears in the
lower pane (the declarations file) showing the bindable attributes of the
element. Elements in brackets are optional. See ["Binding
Elements"](Binding.md#apple-gy2tioi) for more information on bindings.

__Note:__ You must type in the bindings of all the attributes you
want to bind, and delete the others. Otherwise, you will not be able to
switch back to graphical editing mode or save the file.

!
[!](DynElTOC.md)[Table
of Contents](DynElTOC.md) [!](ObjBrwsr.md)[Next
Section](ObjBrwsr.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
