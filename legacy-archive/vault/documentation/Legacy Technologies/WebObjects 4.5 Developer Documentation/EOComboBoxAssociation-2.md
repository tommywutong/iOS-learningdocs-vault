---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOComboBoxAssociation.html
archived_at: '2026-07-15T08:11:45.394388Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOComboBoxAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5axg43pmnuwc5djn5xa) : EODelayedObserver (EOControl) : NSObject

> **__Conforms to:__**
> : NSCoding
> : (EOAssociation)
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EOComboBoxAssociation.h

---

## Class Description

---

An EOComboBoxAssociation object displays an attribute or to-one
relationship value in an NSComboBox (Application Kit). The items
in the combo box can be entered manually, or for a relationship,
constructed dynamically from values supplied by an EODisplayGroup. EOComboBoxAssociation
is very similar to the EOPopUpAssociation.

|  |
| --- |
| __Usable With__ |
| NSComboBox (Application Kit) |

|  |
| --- |
| __Aspects__ |
| titles | Property of the enterprise objects in an EODisplayGroup that supplies the titles for the items in the combo box list. |
| selectedTitle | String property of the enterprise object supplying the title to display in the combo box. When the value of the combo box changes either because a new value is typed in or a selection is made using the pop up menu, the new text value is assigned to this property. |
| selectedObject | Relationship property of the enterprise object containing the enterprise object to select from the titles EODisplayGroup. selectedObject is usually mutually exclusive with selectedTitle. When the value of the combo box changes, the association updates the relationship to point to the new object. |
| enabled | A boolean attribute of the selected object that determines whether the combo box is enabled. |

|  |
| --- |
| __Object Keys Taken__ |
| target | When the user chooses an item in the pop-up menu, the EOComboBoxAssociation updates the selected object's property with the item's title or object. |
| dataSource | When the NSComboBox requests values for its list, the EOComboBoxAssociation provides them by querying the appropriate EODisplayGroup or groups. |
| delegate | An EOComboBoxAssociation accepts the message comboBoxSelectionDidChange. |

## Examples

There are three basic ways to configure a combo box and it's
association. Each is described below.

## Selecting a String from a Static List

Suppose you have a Movie display group and you want to provide
a combo box for setting the rating from a static list of strings.
In this example, a Movie object's rating is a string property
rather than a relationship to a Rating object). To do this, in Interface
Builder, type the list of ratings into the combo box. Control-drag
a connection from the combo box to the Movie display group. Choose EOComboBoxAssociation
in the Connections inspector, and bind the selectedTitle aspect
to the "rating" key.

## Selecting a String from a Dynamic List

This example is similar to the previous one, except in this
example, a Movie object's rating is chosen from strings in a Rating
database table. There's a Rating EODisplayGroup that fetches the
ratings into Rating objects, and the combo box is filled from the
"ratingString" property of the rating display group's Rating
objects. To do this, in Interface Builder, control-drag a connection
from the combo box to the Ratings display group. Choose EOComboBoxAssociation
in the Connections inspector, and bind the titles aspect to the
"ratingString" key. Similarly, control-drag a connection from
the combo box to the Movie display group. Again choose EOComboBoxAssociation
in the Connections inspector, and bind the selectedTitle aspect
to the "rating" key.

## Selecting the Destination of a To-One Relationship

Suppose you have a list of employees and want to assign each
employee a department. In terms of the object model, you want to
assign a Department object as the destination of an Employee object's __department__ relationship.
To do this, in Interface Builder, control-drag a connection from
the combo box to a Department display group. Choose EOComboBoxAssociation
in the Connections inspector, and bind the titles aspect to the
"name" key. Similarly, control-drag a connection from the combo
box to the Employee display group. Again choose EOComboBoxAssociation
in the Connections inspector, and bind the selectedObject to the
"department" key.

If the selectedObject aspect is bound and the user types a
value that doesn't match any of those currently in the list, an
error panel is displayed.

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
