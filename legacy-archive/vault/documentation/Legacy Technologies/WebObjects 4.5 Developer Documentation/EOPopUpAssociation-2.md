---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOPopUpAssociation.html
archived_at: '2026-07-15T08:11:45.580585Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOPopUpAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5axg43pmnuwc5djn5xa) : EODelayedObserver (EOControl) : NSObject

> **__Conforms to:__**
> : NSCoding
> : (EOAssociation)
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EOPopUpAssociation.h

---

## Class Description

---

An EOPopUpAssociation object displays an attribute or to-one
relationship value in an NSPopUpButton (Application Kit).

The items in the NSPopUpButton can be entered manually, or
for a relationship, constructed dynamically from values supplied
by the destination entity's EODisplayGroup. The value displayed by
the NSPopUpButton can be bound by one of three aspects: __selectedTitle__,
which is useful for values representable as strings; __selectedTag__,
for integer values; and __selectedObject__,
for the destination object of a relationship.

|  |
| --- |
| __Usable With__ |
| NSPopUpButton (Application Kit) |

|  |
| --- |
| __Aspects__ |
| titles | An attribute of the objects in an EODisplayGroup whose values can be represented as strings. |
| selectedTitle | An attribute of the selected object whose values can be represented as strings. |
| selectedTag | An integer attribute of the selected object. |
| selectedObject | A to-one relationship of the selected object; the value displayed is that for the attribute bound to the __titles__ aspect. |
| enabled | A boolean attribute of the selected object, which determines whether the NSPopUpButton is enabled. |

|  |
| --- |
| __Object Keys Taken__ |
| target | When the user chooses an item in the pop-up list, the EOPopUpAssociation updates the selected object's property with the item's title, tag, or object. |

## Examples

There are several basic ways to configure a combo box and
it's association. They are described below.

## Selecting a String from a Static List

Suppose you have a Movie display group and you want to provide
a pop-up list for setting the rating from a static list of strings.
In this example, a Movie object's rating is a string property
rather than a relationship to a Rating object. To do this, in Interface
Builder, type the list of ratings into the pop-up list. Control-drag
a connection from the pop-up list to the Movie display group. Choose EOPopUpAssociation
in the Connections inspector, and bind the selectedTitle aspect
to the "rating" key. With this configuration, if an object's
string attribute value isn't in the pop-up list, it's temporarily added
while the object is selected.

## Selecting a String from a Dynamic List

This example is similar to the previous one, except in this
example, a Movie object's rating is chosen from strings in a Rating
database table. There's a Rating EODisplayGroup that fetches the
ratings into Rating objects, and the pop-up list is filled from
the "ratingString" property of the rating display group's
Rating objects. To do this, in Interface Builder, control-drag a
connection from the pop-up list to the Ratings display group. Choose
EOPopUpAssociation in the Connections inspector, and bind the titles
aspect to the "ratingString" key. Similarly, control-drag a
connection from the pop-up list to the Movie display group. Again
choose EOComboBoxAssociation in the Connections inspector, and bind the
selectedTitle aspect to the "rating" key.

## Selecting an Integer Tag from a Static List

Suppose you have a Customer enterprise object whose credit
card type (Visa, MasterCard, and so on) is indicated by an integer
tag. You want a user to be able to choose a customer's card type
from a pop-up list. To do this, in Interface Builder, set the credit
card names and tags for the pop-up list. Control-drag a connection
from the pop-up list to the Customer display group. Choose EOPopUpAssociation
in the Connections inspector, and bind the selectedTag aspect to
the "cardType" key. You can also allow for a general "other"
value by defining a special tag and setting it in the EOPopUpAssociation
using [setTagValueForOther:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2qn5yfk4cbonzw6y3jmf2gs33of5zwk5cumftvmylmovsum33sj52gqzlshi).
Credit card tags from the database not matching any in the pop-up
list are then displayed as the "other" value. (It would also
make sense to disable the pop-up list in this case, to avoid writing
the meaningless tag back to the database.)

## Selecting the Destination of a To-One Relationship

Suppose you have a list of employees and want to assign each
employee a department. In terms of the object model, you want to
assign a Department object as the destination of an Employee object's __department__ relationship.
To do this, in Interface Builder, control-drag a connection from
the pop-up list to a Department display group. Choose EOComboBoxAssociation
in the Connections inspector, and bind the titles aspect to the
"name" key. Similarly, control-drag a connection from the pop-up
list to the Employee display group. Again choose EOComboBoxAssociation
in the Connections inspector, and bind the selectedObject to the
"department" key. This fills the pop-up list with the names
of departments, and causes the name of the selected Employee's
Department to be selected in the pop-up list.

## Instance Methods

---

### setTagValueForOther:

`- (void)setTagValueForOther:(int)tag`

Records _tag_ as
the "unknown" tag. When a property value doesn't match any
other tag in the pop-up list, the EOPopUpAssociation automatically
selects the item for this tag. If there's no item for this tag, the
pop-up list's selection isn't changed. This tag value is by
default -1.

---

### tagValueForOther

`- (int)tagValueForOther`

Returns the "unknown" tag.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
