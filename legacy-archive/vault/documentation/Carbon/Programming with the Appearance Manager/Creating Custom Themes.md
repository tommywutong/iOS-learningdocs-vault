---
title: Programming with the Appearance Manager
apple_id: TP40001038
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2001-11-20'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgAppearance_Manager/Concepts/Appearance.1d.html
archived_at: '2026-07-15T05:23:56.587623Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming with the Appearance Manager](toc.md)



__PATH__Documentation > [Carbon](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000420) > User Experience

[![Up](attachments/Concepts/images/up.gif)](Appearance.f.md)
[![Previous](attachments/Concepts/images/previous.gif)](Appearance.1c.md)
[![Next](attachments/Concepts/images/next.gif)](Appearance.ba.md)

---

#    Creating  Custom Themes

There are two common cases where you may wish to create a custom theme. The first is to set up a custom theme environment for your program, to be used only when your program is active. This is useful for some programs, such as games, that need to control the entire user environment while they are active. The second is to create a theme environment that you want to be user-selectable and to have systemwide effect.

In the first case, if you set up a custom theme environment for your application, you don't need the theme you create to show up in the Appearance control panel (that is, to be user-selectable). The steps to create a custom theme that is not user-selectable are as follows:

1. 

   Create a collection, using the Collection Manager function
   NewCollection
   .
2. 

   Using theme collection tags and Collection Manager functions, add collection items describing attributes of the theme to the collection. Note that you do not need to add collection items for every tag defined by the Appearance Manager; you need to include collection items only for those attributes that you want to change. See
   Theme Collection Tags
   for descriptions of available tag values.
3. 

   Call the function
   GetTheme
   to get a collection containing a copy of the data for the theme that is currently running.
4. 

   Call
   SetTheme
   to set your collection as the current theme.
5. 

   After you have finished using the custom theme environment for your program, restore the previous theme by calling
   SetTheme
   . Pass
   SetTheme
   a reference to the collection for the previous theme, which you obtained with your call to
   GetTheme
   in Step 3.
6. 

   Dispose of the collection and its contents when you are done.

In the second case, if you want the theme to be user-selectable and to have systemwide effect, you need the theme to show up in the Appearance control panel and must therefore follow these steps:

1. 

   Create a collection, using the Collection Manager function
   NewCollection
   .
2. 

   Using theme collection tags and Collection Manager functions, add collection items describing attributes of the theme to the collection. Note that you do not need to add collection items for every tag defined by the Appearance Manager; you need to include collection items only for those attributes that you want to change. See
   Theme Collection Tags
   for descriptions of available tag values.
3. 

   Flatten the collection to a handle, using the Collection Manager function
   FlattenCollectionToHdl
   .
4. 

   Use the Resource Manager to save the flattened collection as a resource of type
   'scen'
   . Save the
   'scen'
   resource into a custom theme file (that is, in a file of type
   'scen'
   ) in the Theme Files folder; see
   Appearance Manager File Type Constants
   for a description of the
   'scen'
   file type. See _More Macintosh Toolbox_
   for a discussion of the Resource Manager and how resources are added to files and released.
5. 

   Dispose of the collection and its contents when you are done.

---

© 1999, 2000 Apple Computer, Inc. – (Last Updated 27 Nov 00)

[![Up](attachments/Concepts/images/up.gif)](Appearance.f.md) [![Previous](attachments/Concepts/images/previous.gif)](Appearance.1c.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
