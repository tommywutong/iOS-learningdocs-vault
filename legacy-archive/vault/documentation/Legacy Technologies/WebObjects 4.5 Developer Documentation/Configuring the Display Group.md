---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.46.html
archived_at: '2026-07-15T08:10:41.069202Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Adding%20Display%20Groups.md) [!](Adding%20Display%20Groups.md) [!](Creating%20a%20Detail%20Display%20Group-2.md)

---

#   Configuring the Display Group

A display group must be configured in order for it to be created and initialized automatically when the component is initialized at run time. Display groups are instantiated from an archive file (with the extension .__woo__
) that's stored in the component. You shouldn't edit .__woo__
files by hand; they're maintained by WebObjects Builder.

In the object browser, !
means that the display group has been configured. A !
means that it has not been configured, and so the variable isn't automatically created at run time. A configured display group shows its keys and actions in the second column of the object browser. You can bind them to elements in your program.

!

To configure a display group (or change its configuration), double-click its name to open the Display Group Options panel.

!

In this panel, you specify the following information:

- 

  _Entity:_
  The Entity combo box contains entities from the models in your project. You can select one from the list or type the name.
- 

  _Has detail data source:_
  Check this to create a detail display group. See [Creating a Detail Display Group](Creating%20a%20Detail%20Display%20Group-2.md#apple-giztmnbs)
  for more information.
- 

  _Entries per batch:_
  Set a non-zero value here to specify the number of records to be displayed at once. When the value is zero, all records are displayed.
- 

  _Qualification:_
  When displaying records according to a query, this setting determines whether to display records that begin with, end with, or contain the item specified.
- 

  _Fetches on load_
  : When you check this option, the display group fetches all its objects as soon as the component is loaded into the application.
- 

  _Sorting:_
  You select an attribute by which to sort your displayed objects from the pop-up list, and use the radio buttons to select the order of sorting.
- 

  Fetch Spec: The Fetch Spec pop-up list contains all the fetch specification defined in the corresponding model file. A fetch spec is simply a predefined query.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Adding%20Display%20Groups.md) [!](Adding%20Display%20Groups.md) [!](Creating%20a%20Detail%20Display%20Group-2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
