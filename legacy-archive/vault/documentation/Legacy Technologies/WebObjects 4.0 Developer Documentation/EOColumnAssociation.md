---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOColumnAssociation.html
archived_at: '2026-07-18T01:28:42.765423Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOAssociation-2.md)
[!](EOComboBoxAssociation.md)

---

# EOColumnAssociation

__Inherits From:__
EOAssociation : EODelayedObserver (EOControl) : NSObject

EOObserving (EODelayedObserver)

__Inherits From:__
com.apple.yellow.eointerface (Yellow Box)

---

## Class Description

An EOColumnAssociation object cooperates with an EOTableViewAssociation to display values in a column of an NSTableView (Application Kit). It is for use in Yellow Box applications only. For an equivalent Java Client class, see the [EOTableColumnAssociation](EOTableColumnAssociation.md) class specification.

A column association links an NSTableColumn (Application Kit) to a single attribute of all displayed objects in an EODisplayGroup. The value of each object is displayed in its corresponding row.

The EOTableViewAssociation receives target, delegate, and data source messages from the table view, and forwards them as needed to the appropriate column association. Column associations provide values for the cells of each NSTableColumn, and also accept edited values to set in their display groups.

EOColumnAssociations provide values using NSTableView's DataSource methods

---

tableViewSetObjectValueForLocation
and

---

tableViewObjectValueForLocation
. This allows values with non-string representations to be displayed. For example, if an NSImageCell (Application Kit) is used as an NSTableColumn's data cell, an EOColumnAssociation can be used to display NSImages (Application Kit) in the NSTableView.

| __Usable With__ |
| NSTableColumn (Application Kit) |

```
```

| __Aspects__ | __Aspects__ |
| value | An attribute of the objects, displayed in each row of the NSTableColumn. |
| enabled | A boolean attribute of the objects, which determines whether each object's value cell is editable. Note that because EOTableViewAssociation also uses this aspect, you can use it with different keys to limit editability to the whole row or to an individual cell (column) in that row. |

```
```

| __Object Keys Taken__ | __Object Keys Taken__ |
| identifier | An EOColumnAssociations sets itself as the identifer of its NSTableColumn. (Note: This key isn't formally reserved by the `objectKeysTaken` method, as Interface Builder doesn't treat it as an outlet.) |

```
```


---

## Example

To display the last and first names of objects in a Talent display group, in Interface Builder, Control-drag a connection from the last name column to the display group. Select EOColumnAssociation in the Connections inspector, and bind the `value` aspect to the "lastName" key (this automatically creates an EOTableViewAssociation to manage the individual columns). Repeat to set up a column association for the first name. Now when you run the application, the last and first names of each Talent object in the display group's [`displayedObjects`](EODisplayGroup.md#apple-geztmmi) array are put in the correponding row.

---

## Method Types

**Sorting rows**

**[setSortingSelector](#apple-geytg)

**[sortingSelector](#apple-gezda)****

**Table view data source methods**

**[tableViewSetObjectValueForLocation](#apple-geztq)

**[tableViewObjectValueForLocation](#apple-geztk)****

**Table view delegate methods**

**[tableViewShouldEditLocation](#apple-ge2dc)

**[tableViewWillDisplayCell](#apple-ge2di)****

**Control delegate methods**

**[controlDidFailToFormatStringErrorDescription](#apple-geydoma)

**[controlIsValidObject](#apple-gezdm)

**[controlTextShouldBeginEditing](#apple-gezte)******

---

## Constructors

public `EOColumnAssociation`(java.lang.Object _aDisplayObject_)

Creates a new EOColumnAssociation to monitor and update the row values in _aDisplayObject_, an NSTableColumn (Application Kit).

You normally set up associations with the Interface Builder application, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See also:__
[`bindAspect`](EOAssociation.md#apple-gu2tq) (EOAssociation), [`establishConnection`](EOAssociation.md#apple-gu4dq) (EOAssociation)

---

## Instance Methods

---

### setSortingSelector

public void `setSortingSelector`(com.apple.yellow.foundation.NSSelector _aSelector_)

Sets the method selector used to sort rows to _aSelector_, one of:

- EOSortOrdering.EO_COMPARE_ASCENDING
- EOSortOrdering.EO_COMPARE_DESCENDING
- EOSortOrdering.EO_COMPARE_CASE_INSENSITIVE_ASCENDING
- EOSortOrdering.EO_COMPARE_CASE_INSENSITIVE_DESCENDING
- `null` (to tell the receiver not to sort)

For more information on these selectors, see the section "Comparison Methods" in the EOSortOrdering class specification (EOControl).

If the EOTableViewAssociation for the receiver's NSTableView (Application Kit) sorts its rows, it applies this method as needed to sort them. The default sorting selector is EOSortOrdering.EO_COMPARE_ASCENDING.

---

### sortingSelector

public com.apple.yellow.foundation.NSSelector `sortingSelector`()

Returns the method selector used to sort rows, or `null` if the column isn't sorted.

# Data Source and Delegate Methods

These methods are forwarded by the corresponding NSTableView's EOTableViewAssociation to the appropriate EOColumnAssociation.

---

### controlDidFailToFormatStringErrorDescription

public boolean `controlDidFailToFormatStringErrorDescription`(
com.apple.yellow.application.NSControl _aTableView_,
java.lang.String _aString_,
java.lang.String _errorDescription_)

Invokes [`shouldEndEditing`](EOAssociation.md#apple-gyyta) (defined by EOAssociation) and returns the result.

---

### controlIsValidObject

public boolean `controlIsValidObject`(
com.apple.yellow.application.NSControl _aNSControl_,
java.lang.Object _anObject_)

Saves the value of any cell being edited using [`setValueForAspect`](EOAssociation.md#apple-gyyde), and if successful sends an [`associationDidEndEditing`](EODisplayGroup.md#apple-gezteoi) message to the receiver's EODisplayGroup. Returns true if successful (or if no changes need be saved), false if unsuccessful.

---

### controlTextShouldBeginEditing

public boolean `controlTextShouldBeginEditing`(
com.apple.yellow.application.NSControl _aNSControl_,
com.apple.yellow.application.NSText _aNSText_)

Sends an [`associationDidBeginEditing`](EODisplayGroup.md#apple-gezteni) message to the receiver's EODisplayGroup and returns true.

---

### tableViewObjectValueForLocation

public java.lang.Object `tableViewObjectValueForLocation`(
com.apple.yellow.application.NSTableView _aNSTableView_,
com.apple.yellow.application.NSTableColumn _aNSTableColumn_,
int _anInt_)

Returns the value of the property of the object at _rowIndex_ bound to the `value` aspect.

---

### tableViewSetObjectValueForLocation

public void `tableViewSetObjectValueForLocation`(
com.apple.yellow.application.NSTableView _aTableView_,
java.lang.Object _value_,
com.apple.yellow.application.NSTableColumn _aTableColumn_,
int _rowIndex_)

Sets the property of the object at _rowIndex_ bound to the `value` aspect to _value_.

---

### tableViewShouldEditLocation

public boolean `tableViewShouldEditLocation`(
com.apple.yellow.application.NSTableView _aTableView_,
com.apple.yellow.application.NSTableColumn _aTableColumn_,
int _rowIndex_)

Returns false if the `enabled` aspect is bound and its value for the object at _rowIndex_ is false. Otherwise returns true. Note that because the `enabled` aspects of EOTableViewAssociation and EOColumnAssociation can be bound to different keys, you can limit editability to the whole row or to an individual cell (column) in that row.

---

### tableViewWillDisplayCell

public void `tableViewWillDisplayCell`(
com.apple.yellow.application.NSTableView _aTableView_,
java.lang.Object _aCell_,
com.apple.yellow.application.NSTableColumn _aTableColumn_,
int _rowIndex_)

Alters the display characteristics for _aCell_ according to the values for the `enabled` aspect of the object at _rowIndex_.

---

[!](EOAssociation-2.md)
[!](EOComboBoxAssociation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
