---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOTableViewAssociation.html
archived_at: '2026-07-18T01:28:44.267001Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOTableColumnAssociation.md)
[!](EOTextAssociation.md)

---

# EOTableViewAssociation

__Inherits From:__
EOAssociation : EODelayedObserver (EOControl) : NSObject

EOObserving (EODelayedObserver)

__Inherits From:__
com.apple.yellow.eointerface (Yellow Box)

---

## Class Description

An EOTableViewAssociation object manages the individual EOColumnAssociations between an NSTableView (Application Kit) and an EODisplayGroup. It is for use in Yellow Box applications only; for an equivalent Java Client class, see the [EOTableAssociation](EOTableAssociation.md) class specification.

An EOTableViewAssociation can sort the objects in the display group by the left-to-right order of the table columns. The first EOColumnAssociation to be bound to a table view automatically creates the EOTableViewAssociation; you should rarely need to do so yourself.

An EOTableViewAssociation receives data source and delegate messages from the table view, some of which it handles itself, and some of which it forwards to the appropriate EOColumnAssociations. For more information, see the EOColumnAssociation class specification.

| __Usable With__ |
| NSTableView |

```
```

| __Aspects__ | __Aspects__ |
| source | Bound to the EODisplayGroup providing objects. This aspect doesn't use a key. |
| enabled | A boolean attribute of the objects, which determines whether each object's row is editable. Note that because EOColumnAssociation also uses this aspect, you can use it with different keys to limit editability to the whole row or to an individual cell (column) in that row. |
| textColor | An NSColor attribute of the objects, which determines the color of text for each object's row in the NSTableView. |
| bold | A boolean attribute of the objects, which determines whether each objects row is displayed in bold or regular weight text. |
| italic | A boolean attribute of the objects, which determines whether each objects row is displayed in italic or normal angle text. |

```
```

| __Object Keys Taken__ | __Object Keys Taken__ |
| dataSource | An EOTableViewAssociation responds to some data source messages and forwards others to the appropriate EOColumnAssociation. |
| delegate | An EOTableViewAssociation forwards delegate messages to the appropriate EOColumnAssociations. |
| target | Reserved, but not used. |

```
```


---

## Example

For an example of using an EOTableViewAssociation, see the EOColumnAssociation class specification.

---

## Method Types

**Setting up a table view association**

**[bindToTableView](#apple-gezte)**

**Sorting**

**[setSortsByColumnOrder](#apple-gezts)

**[sortsByColumnOrder](#apple-ge2di)****

**Accessing the active EOColumnAssociation**

**[editingAssociation](#apple-geztm)**

**Table view data source methods**

**[numberOfRowsInTableView](#apple-ge3de)

**[tableViewSetObjectValueForLocation](#apple-ge3ds)

**[tableViewObjectValueForLocation](#apple-ge3dm)******

**Table view delegate methods**

**[tableViewShouldEditLocation](#apple-ge3te)

**[tableViewWillDisplayCell](#apple-ge3tk)****

**Table view notification methods**

**[tableViewSelectionDidChange](#apple-geytsoa)**

**Control delegate methods**

**[controlDidFailToFormatStringErrorDescription](#apple-ge2ti)

**[controlIsValidObject](#apple-geytenq)

**[controlTextShouldBeginEditing](#apple-ge2tq)******

---

## Constructors

public `EOTableViewAssociation`(java.lang.Object _aDisplayObject_)

Creates a new EOTableViewAssociation to manage EOColumnAssociations associated with _aDisplayObject_, an NSTableView (Application Kit).

You normally set up associations with the Interface Builder application, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See also:__
[`bindAspect`](EOAssociation.md#apple-gu2tq) (EOAssociation), [`establishConnection`](EOAssociation.md#apple-gu4dq) (EOAssociation)

---

### bindToTableView

public static void `bindToTableView`(
com.apple.yellow.application.NSTableView _aTableView_,
EODisplayGroup _aDisplayGroup_)

Creates an EOTableViewAssociation, binding _aTableView_ to _aDisplayGroup_, if there isn't already a table view association for _aTableView_.

---

## Instance Methods

---

### editingAssociation

public EOColumnAssociation `editingAssociation`()

Returns the EOColumnAssociation for the NSTableView cell being edited, or `null` if no cell is being edited.

---

### setSortsByColumnOrder

public void `setSortsByColumnOrder`(boolean _flag_)

Controls whether the receiver applies a sort ordering to its EODisplayGroup. If _flag_ is `true`, it builds EOSortOrderings (EOControl) for each of the EOColumnAssociations, collects them into an NSArray based on the left-to-right order of the columns, and assigns them to the display group with [`setSortOrderings`](EODisplayGroup.md#apple-ge2teoa). If _flag_ is `false`, it doesn't alter the sort ordering of the display group.

An EOTableViewAssociation assigns sort orderings based on the left to right order of the table columns, and reassigns them whenever the user moves a column.

__See also:__
[`sortingSelector`](EOColumnAssociation.md#apple-gezda) (EOColumnAssociation)

---

### sortsByColumnOrder

public boolean `sortsByColumnOrder`()

Returns `true` if the receiver assigns EOSortOrderings (EOControl) to its EODisplayGroup based on the sorting selectors of its EOColumnAssociations, `false` if it doesn't alter the display group's sort ordering.

# Data Source, Delegate, and Notification Methods

---

### controlDidFailToFormatStringErrorDescription

public boolean `controlDidFailToFormatStringErrorDescription`(
com.apple.yellow.application.NSControl _aTableView_,
java.lang.String _aString_,
java.lang.String _errorDescription_)

Forwards the message to the receiver's editing association.

__See also:__
[`editingAssociation`](#apple-geztm)

---

### controlIsValidObject

public boolean `controlIsValidObject`(
com.apple.yellow.application.NSControl _aTableView_,
java.lang.Object _anObject_)

Forwards the message to the receiver's editing association.

__See also:__
[`editingAssociation`](#apple-geztm)

---

### controlTextShouldBeginEditing

public boolean `controlTextShouldBeginEditing`(
com.apple.yellow.application.NSControl _aTableView_,
com.apple.yellow.application.NSText _fieldEditor_)

Forwards the message to the receiver's editing association.

__See also:__
[`editingAssociation`](#apple-geztm)

---

### numberOfRowsInTableView

public int `numberOfRowsInTableView`(com.apple.yellow.application.NSTableView _aTableView_)

Returns the number of displayed objects in the receiver's EODisplayGroup.

__See also:__
[`displayedObjects`](EODisplayGroup.md#apple-geztmmi) (EODisplayGroup)

---

### tableViewObjectValueForLocation

public java.lang.Object `tableViewObjectValueForLocation`(
com.apple.yellow.application.NSTableView _aTableView_,
com.apple.yellow.application.NSTableColumn _aTableColumn_,
int _rowIndex_)

Forwards the message to _aTableColumn_'s identifier-assumed to be the EOColumnAssociation bound to that column-so that it can provide the value.

---

### tableViewSelectionDidChange

public void `tableViewSelectionDidChange`(com.apple.yellow.foundation.NSNotification _aNotification_)

Updates the receiver's EODisplayGroup based on the new selection in the table view.

__See also:__
[`setSelectionIndexes`](EODisplayGroup.md#apple-ge2tcoa) (EODisplayGroup)

---

### tableViewSetObjectValueForLocation

public void `tableViewSetObjectValueForLocation`(
com.apple.yellow.application.NSTableView _aTableView_,
java.lang.Object _value_,
com.apple.yellow.application.NSTableColumn _aTableColumn_,
int _rowIndex_)

Forwards the message to _aTableColumn_'s identifier-assumed to be the EOColumnAssociation bound to that column-so that it can set the value.

---

### tableViewShouldEditLocation

public boolean `tableViewShouldEditLocation`(
com.apple.yellow.application.NSTableView _aTableView_,
com.apple.yellow.application.NSTableColumn _aTableColumn_,
int _rowIndex_)

Returns `false` if the "enabled" aspect is bound and its value for the object at _rowIndex_ is 0. Otherwise forwards the message to _aTableColumn_'s identifier-assumed to be the EOColumnAssociation bound to that column-and returns its response. Note that because the two associations' `enabled` aspects can be bound to different keys, you can limit editability to the whole row or to an individual cell (column) in that row.

---

### tableViewWillDisplayCell

public void `tableViewWillDisplayCell`(
com.apple.yellow.application.NSTableView _aTableView_,
java.lang.Object _aCell_,
com.apple.yellow.application.NSTableColumn _aTableColumn_,
int _rowIndex_)

Alters the display characteristics for _aCell_ according to the values for the `enabled`, `textColor`, `bold`, and `italic` aspects of the object at _rowIndex_. Then forwards the message to _aTableColumn_'s identifier-assumed to be the EOColumnAssociation bound to that column-allowing it to adjust _aCell_ based on its own `enabled` aspect.

---

[!](EOTableColumnAssociation.md)
[!](EOTextAssociation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
