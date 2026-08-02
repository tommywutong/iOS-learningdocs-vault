---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOComboBoxAssociation.html
archived_at: '2026-07-15T08:11:44.612558Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOComboBoxAssociation

> **__Inherits
> from:__**
> : [(com.apple.client.eointerface)
> EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) :
> EODelayedObserver (EOControl) :
> Object
> (com.apple.yellow.eointerface)
> EOAssociation :
> EODelayedObserver (EOControl) :
> NSObject

> **__Implements:__**
> : EOObserving (EODelayedObserver)
> : (com.apple.client.eointerface only) java.awt.event.ActionListener
> : (com.apple.client.eointerface only) NSDisposable (EOAssociation)

> **__Package:__**
> : com.apple.client.eointerface
> : com.apple.yellow.eointerface

---

## Class Description

---

An EOComboBoxAssociation object displays an attribute or to-one
relationship value in an NSComboBox (Application Kit), or javax.swing.JComboBox.
The items in the combo box can be entered manually, or for a relationship,
constructed dynamically from values supplied by an EODisplayGroup. EOComboBoxAssociation
is very similar to the EOPopUpAssociation (com.apple.yellow.eointerface only).

|  |
| --- |
| __Usable With__ |
| (com.apple.client.eointerface) javax.swing.JComboBox   (com.apple.yellow.eointerface) NSComboBox (Application Kit) |

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
| (com.apple.yellow.eointerface only) target | When the user chooses an item in the pop-up menu, the EOComboBoxAssociation updates the selected object's property with the item's title or object. |
| (com.apple.yellow.eointerface only) dataSource | When the NSComboBox requests values for its list, the EOComboBoxAssociation provides them by querying the appropriate EODisplayGroup or groups. |
| (com.apple.yellow.eointerface only) delegate | An EOComboBoxAssociation accepts the message comboBoxSelectionDidChange. |

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
assign a Department object as the destination of an Employee object's `department` relationship.
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

## Constructors

---

### EOComboBoxAssociation

`public EOComboBoxAssociation(Object  aDisplayObject)`

Creates a new EOComboBoxAssociation to monitor
and update the values in  _aDisplayObject,_
a combo box (using the com.apple.yellow.eointerface APIs, it's
a com.apple.yellow.application.NSComboBox; using com.apple.client.eointerface APIs,
it's a javax.swing.JComboBox).

You normally set up associations
with the Interface Builder application, in which case you don't
need to create them programmatically. However, if you do create
them up programmatically, setting them up is a multi-step process.
After creating an association, you must bind its aspects and establish
its connections.

__See Also:__  [bindAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe2lomraxg4dfmn2a) (EOAssociation), [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) (EOAssociation)

---

## Instance Methods

---

### actionPerformed

`public void actionPerformed(java.awt.event.ActionEvent  anActionEvent)`

(com.apple.client.eointerface only) Invoked
when the receiver's display object is acted upon. Sends the method
identified by the receiver's action aspect (with an argument,
if the argument aspect is bound) to the selected objects.

---

### breakConnection

`public void breakConnection()`

(com.apple.client.eointerface) Causes the association
to remove itself from the list of listeners of the JComboBox, and
then calls `super`.

(com.apple.yellow.eointerface)
See the [breakConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe4tfmfvug33onzswg5djn5xa) method description
in the superclass ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4)).

---

### endEditing

`public boolean endEditing()`

See the [endEditing](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk3teivsgs5djnztq) method description in
the superclass ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4)).

---

### establishConnection

`public void establishConnection()`

(com.apple.client.eointerface) Causes the association
to add itself as a listener of the JComboBox.

(com.apple.yellow.eointerface)
See the [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) method
description in the superclass ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4)).

---

### isUsableWithObject

`public boolean isUsableWithObject(Object  aDisplayObject)`

See the [isUsableWithObject](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxws42vonqwe3dfk5uxi2cpmjvgky3u) method description
in the superclass ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4)).

---

### primaryAspect

`public String primaryAspect()`

See the [primaryAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxa4tjnvqxe6kbonygky3u) method description
in the superclass ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4)).

---

### subjectChanged

`public void subjectChanged()`

See the [subjectChanged](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg5lcnjswg5cdnbqw4z3fmq) method description
in the superclass ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4)).

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
