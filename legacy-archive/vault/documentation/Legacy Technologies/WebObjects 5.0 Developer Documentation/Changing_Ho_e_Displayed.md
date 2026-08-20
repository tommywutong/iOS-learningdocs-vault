---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/WalkThrough/Changing_Ho_e_Displayed.html
archived_at: '2026-07-15T08:12:23.760483Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Setting_Whi_e_Displayed.md)[![Next](attachments/DirectToWeb/Images/next.gif)](WebAssistant_Expert_Mode.md)

## Changing How Properties Are Displayed

You can use the Properties display of the WebAssistant to
specify various display characteristics of properties, such as formatting,
color, alignment, and the representation of relationships. The fields
and controls for setting these characteristics are on the right
half of the display. Here is an example:

![[image: ../Art/wadatereleased.gif]](../Art/wadatereleased.gif)

Let's go over the various elements of this part of the user
interface:

- At the top
  is the Display field, which holds the title of the property for
  the current page and entity. As discussed in ["Setting Which Properties are Displayed"](Setting_Whi_e_Displayed.md#apple-ijbusq2iineeq),
  you can edit this string.
- Next to the Display field, in parentheses, is its data type.
  The data type determines the set of display components available
  for use. You cannot edit this information directly (however, you
  can edit the model file, which specifies the data type, using EOModeler).
- The pop-up list shows the name of the component that is used
  to display the selected property in the current page. From this
  menu you can choose a different component to display the property.
  When you choose a display component, the set of controls and fields
  in the right side of the Properties display can change.

The items in the pop-up list identify reusable components
in the Direct to Web framework called property-level components,
which are used to render the properties on the pages you see in
your application. Each property in a page of any type is initially
shown in a default way for that type using a default property-level
component.

### Textual Attributes and Formatting

The display components available for the currently selected
property offer characteristics suitable to the data type and function
of the attribute. A few examples might help to clarify this statement:

- If the data
  type of the attribute is an String but it is a URL, then the DisplayHyperlink or
  DisplayMailTo components could be what you want.
- If the attribute is a date (NSTimestamp), then you might choose
  the DisplayString component and provide format specifiers to have
  the date formatted in a certain way.
- Similarly, if the attribute is a currency value (BigDecimal),
  you might want to use the DisplayNumber component and format the
  display of the attribute with two decimal positions and a leading
  dollar sign.
- If you want to highlight a certain column of values in a table
  by giving them a different color, then you could choose the DisplayStyledString
  component which lets you apply a color to a property.

You can click the Info button in the WebAssistant to get a
short description of the currently selected display component.

The three most common display characteristics for properties
are alignment, formatting, and color. Each of these has their own
controls or fields in the right side of the Property display:

- __Alignment__ Choose
  Right, Center, or Left from the pop-up list to specify the alignment of
  text within a cell of a table.
- __Formatter__ You can have your application
  display some types of data, such as dates and numbers, as formatted
  strings. For example, the date "Sat 4 Jul 98" can be also represented
  as "July 4, 1998." The number one thousand can be represented
  either as "1,000" or "1.000", depending on the locale. There
  are different format specifiers for dates and numbers; check the
  reference documentation for the NSTimestampFormatter and NSNumberFormatter
  classes for details.
- __Color__ To change the color of text,
  either move the sliders to the right of the sample color or enter
  hexadecimal numbers in the field above the sliders. The color specification
  is RGB-based (that is, a specific mixture of red, green, and blue).
  The top slider manipulates red saturation, the middle slider is
  for green, and the bottom slider is for blue. The three pairs of
  hexadecimal digits after the number sign in the field represent
  (left to right) saturation levels of red, green, and blue.

### Representation of Relationships

Properties that are relationships (instead of attributes)
have their own set of display components that you can use. Take
the following list page as an example:

![[image: ../Art/listpage.gif]](../Art/listpage.gif)

There are four relationships on this page. Two are to-one
relationships (Studio and Plot Summary) and two are to-many relationships
(Directors and Roles). By default, all to-many relationships are
displayed using DisplayToManyFault, and to-one relationships are
displayed using DisplayToOneFault. "Fault" indicates that the
records in the relationship aren't displayed until they are asked
for; that is, until the user clicks Inspect. When you click Inspect,
a list page appears, showing all the records in the relationship (such
as all roles in the movie).

You can change the display component for the relationship
to get a different presentation. Consider the Roles relationship
in the Movie-List page example above. Using your browser, navigate
to the list page for the Movie entity. Move the roles property to
the Show list using the WebAssistant and choose D2WDisplayToManyBrowser
from the component pop-up list. The right side of the WebAssistant
should look similar to the following example:

![[image: ../Art/wadisplaytomanybrowser.gif]](../Art/wadisplaytomanybrowser.gif)

In addition to the Alignment pop-up list, the WOComponent
group includes two controls specific to the display of relationships.
The items in the Target Keys browser are selected attributes of
the destination entity; these "target keys" refer to a string
identifying a to-many relationship. In this case the Movie Roles
entity has one target key, `roleName`.
In addition, Direct to Web provides a default key called `userPresentableDescription`,
which is usually a combination of the relationship's keys, if
there are multiple keys.

The Allow Collapsing checkbox, when checked, causes the relationship
initially to be presented as a disclosure triangle followed by a
number and the plural form of the display name for the destination
entity (for example, "6 Movie Roles"). When the user clicks
the triangle, the table cell expands to display the items in the
form appropriate to the display component; in this case, a browser:

![[image: ../Art/displaytomanybrowser.gif]](../Art/displaytomanybrowser.gif)

To get a better sense of the control you have over the presentation
of relationships, set the display component for the Movie Roles
relationship to DisplayToMany and uncheck the Allow Collapsing checkbox.
When you update your browser, a cell in the Roles table should look
similar to this

![[image: ../Art/displaytomany.gif]](../Art/displaytomany.gif)

To-one relationships by their nature offer fewer possibilities
for presentation.The DisplayToOneFault component presents an Inspect
button which, when clicked, displays the relationship record in
an inspect page. The other choice of component, DisplayToOne, displays
the target key for the single destination record as a hyperlink
which, when clicked, brings you to the same inspect page.

A note of caution: The type of display component appropriate
to a relationship depends on the likely number of records in that
relationship. For example, the Studio entity has a Movies to-many
relationship; if some studios have produced hundreds of movies,
it might make more sense to use DisplayToManyFault (that is, the
Inspect button) rather than display the titles of all those movies
in a cell in the table.

To find out more about a display component for a relationship,
click the Info button in the WebAssistant after selecting the component.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Setting_Whi_e_Displayed.md)[![Next](attachments/DirectToWeb/Images/next.gif)](WebAssistant_Expert_Mode.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
