---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOComboBoxAssociation.html
archived_at: '2026-07-18T01:28:42.859624Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOColumnAssociation.md)
[!](EOControlAssociation.md)

---

# EOComboBoxAssociation

__Inherits From:__
EOAssociation : .EODelayedObserver (EOControl) : Object (Java Client)
EOAssociation : .EODelayedObserver (EOControl) : NSObject (Yellow Box)

EOObserving (EODelayedObserver)
java.awt.event.ActionListener (Java Client)

__Inherits From:__
com.apple.client.eointerface (Java Client)
com.apple.yellow.eointerface (Yellow Box)

---

## Class Description

An EOComboBoxAssociation object displays an attribute or to-one relationship value in an NSComboBox (Application Kit), or JComboBox (Swing). The items in the ComboBox can be entered manually, or for a relationship, constructed dynamically from values supplied by an EODisplayGroup. EOComboBoxAssociation is very similar to the EOPopUpAssociation (Yellow Box only).

| __Usable With__ |
| NSComboBox (Application Kit), JComboBox (Swing) |

```
```

| __Aspects__(defined in EOAssociation for Java Client applications) | __Aspects__(defined in EOAssociation for Java Client applications) |
| titles (Yellow Box)   TitlesAspect (Java Client) | Property of the enterprise objects in an EODisplayGroup that supplies the titles for the items in the combo box list. |
| selectedTitle (Yellow Box) SelectedTitlesAspect (Java Client) | String property of the enterprise object supplying the title to display in the c ombo box. When the value of the combo box changes either because a new value is typed in or a selection is made using the pop up menu, the new text value is assigned to this property. |
| selectedObject (Yellow Box) SelectedObjectAspect (Java Client) | Relationship property of the enterprise object containing the enterprise object to select from the __titles__  EODisplayGroup. __selectedObject__  is usually mutually exclusive with __selectedTitle__ . When the value of the combo box changes, the association updates the relationship to point to the new object. |
| enabled (Yellow Box) EnabledAspect (Java Client) | A boolean attribute of the selected object that determines whether the combo box is enabled. |

```
```

| __Object Keys Taken__(none forJava Client) | __Object Keys Taken__(none forJava Client) |
| target | When the user chooses an item in the pop-up menu, the EOComboBoxAssociation updates the selected object's property with the item's title or object. |
| dataSource | When the NSComboBox requests values for its list, the EOComboBoxAssociation provides them by querying the appropriate EODisplayGroup or groups. |
| delegate | An EOComboBoxAssociation accepts the message   ---  comboBoxSelectionDidChange . |

```
```


---

## Examples

There are three basic ways to configure a combo box and it's association. Each is described below.

---

### Selecting a String from a Static List

Suppose you have a Movie display group and you want to provide a combo box for setting the rating from a static list of strings. In this example, a Movie object's rating is a string property rather than a relationship to a Rating object). To do this, in Interface Builder, type the list of ratings into the combo box. Control-drag a connection from the combo box to the Movie display group. Choose EOComboBoxAssociation in the Connections inspector, and bind the __selectedTitle__  aspect to the "rating" key.

---

### Selecting a String from a Dynamic List

This example is similar to the previous one, except in this example, a Movie object's rating is chosen from strings in a Rating database table. There's a Rating EODisplayGroup that fetches the ratings into Rating objects, and the combo box is filled from the "ratingString" property of the rating display group's Rating objects. To do this, in Interface Builder, control-drag a connection from the combo box to the Ratings display group. Choose EOComboBoxAssociation in the Connections inspector, and bind the __titles__  aspect to the "ratingString" key. Similarly, control-drag a connection from the combo box to the Movie display group. Again choose EOComboBoxAssociation in the Connections inspector, and bind the __selectedTitle__  aspect to the "rating" key.

---

### Selecting the Destination of a To-One Relationship

Suppose you have a list of employees and want to assign each employee a department. In terms of the object model, you want to assign a Department object as the destination of an Employee object's `department` relationship. To do this, in Interface Builder, control-drag a connection from the combo box to a Department display group. Choose EOComboBoxAssociation in the Connections inspector, and bind the __titles__  aspect to the "name" key. Similarly, control-drag a connection from the combo box to the Employee display group. Again choose EOComboBoxAssociation in the Connections inspector, and bind the __selectedObject__  to the "department" key.

If the __selectedObject__  aspect is bound and the user types a value that doesn't match any of those currently in the list, an error panel is displayed.

---

## Constructors

public `EOComboBoxAssociation`(java.lang.Object _aDisplayObject_)

Creates a new EOComboBoxAssociation to monitor and update the values in _aDisplayObject_, an NSComboBox (Application Kit) or a JComboBox (Java Client).

You normally set up associations with the Interface Builder application, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See also:__
[`bindAspect`](EOAssociation.md#apple-gu2tq) (EOAssociation), [`establishConnection`](EOAssociation.md#apple-gu4dq) (EOAssociation)

---

## Instance Methods

---

### breakConnection

public void `breakConnection`()

Causes the association to remove itself from the list of listeners of the JComboBox, and then calls super.

This method is available for Java Client applications only; there is no Yellow Box equivalent.

---

### establishConnection

public void `establishConnection`()

Causes the association to add itself as a listener of the JComboBox.

This method is available for Java Client applications only; there is no Yellow Box equivalent.

---

### subjectChanged

public void `subjectChanged`()

Called when the EODisplayGroup notifies the association that the values represented in the UI widget need to change to reflect a change in the underlying object graph.

This method is available for Java Client applications only; there is no Yellow Box equivalent.

---

[!](EOColumnAssociation.md)
[!](EOControlAssociation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
