---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOColumnAssociation.html
archived_at: '2026-07-15T08:11:45.377200Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOColumnAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5axg43pmnuwc5djn5xa) : EODelayedObserver (EOControl) : NSObject

> **__Conforms to:__**
> : NSCoding
> : (EOAssociation)
> : EOObserving (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOInterface/EOColumnAssociation.h

---

## Class Description

---

An EOColumnAssociation object cooperates with an EOTableViewAssociation
to display values in a column of an NSTableView (Application Kit).

A column association links an NSTableColumn (Application Kit)
to a single attribute of all displayed objects in an EODisplayGroup.
The value of each object is displayed in its corresponding row.

Column associations provide values for the cells of each NSTableColumn,
and also accept edited values to set in their display groups. The
EOTableViewAssociation receives target, delegate, and data source messages
from the table view, and forwards them as needed to the appropriate
column association.

EOColumnAssociations provide values using NSTableView's
DataSource methods __tableView:setObjectValue:forTableColumn:row:__ and __tableView:objectValueForTableColumn:__.
This allows values with non-string representations to be displayed.
For example, if an NSImageCell (Application Kit) is used as an NSTableColumn's
data cell, an EOColumnAssociation can be used to display NSImages (Application
Kit) in the NSTableView.

|  |
| --- |
| __Usable With__ |
| NSTableColumn (Application Kit) |

|  |
| --- |
| __Aspects__ |
| value | An attribute of the objects, displayed in each row of the NSTableColumn. |
| enabled | A boolean attribute of the objects, which determines whether each object's value cell is editable. Note that because EOTableViewAssociation also uses this aspect, you can use it with different keys to limit editability to the whole row or to an individual cell (column) in that row. |

|  |
| --- |
| __Object Keys Taken__ |
| identifier | An EOColumnAssociations sets itself as the identifier of its NSTableColumn. (Note: This key isn't formally reserved by the __objectKeysTaken__ method, as Interface Builder doesn't treat it as an outlet.) |

## Example

To display the last and first names of objects in a Talent
display group, in Interface Builder, Control-drag a connection from
the last name column to the display group. Select EOColumnAssociation
in the Connections inspector, and bind the __value__ aspect
to the "lastName" key (this automatically creates an EOTableViewAssociation
to manage the individual columns). Repeat to set up a column association
for the first name. Now when you run the application, the last and
first names of each Talent object in the display group's [displayedObjects](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg) array are put in
the corresponding row.

## Method Types

---

> **Sorting rows**
> : [- setSortingSelector:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5whk3loifzxg33dnfqxi2lpnyxxgzluknxxe5djnztvgzlmmvrxi33shi)
> : [- sortingSelector](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5whk3loifzxg33dnfqxi2lpnyxxg33soruw4z2tmvwgky3un5za)
>
> **Table view data source
> methods**
> : [- tableView:setObjectValue:forTableColumn:row:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5whk3loifzxg33dnfqxi2lpnyxxiylcnrsvm2lfo45hgzluj5rguzldorlgc3dvmu5gm33skrqwe3dfinxwy5lnny5he33xhi)
> : [- tableView:objectValueForTableColumn:row:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5whk3loifzxg33dnfqxi2lpnyxxiylcnrsvm2lfo45g6ytkmvrxivtbnr2wkrtpojkgcytmmvbw63dvnvxdu4tpo45a)
>
> **Table view delegate methods**
> : [- tableView:shouldEditTableColumn:row:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5whk3loifzxg33dnfqxi2lpnyxxiylcnrsvm2lfo45hg2dpovwgirlenf2fiylcnrsug33movww4otsn53tu)
> : [- tableView:willDisplayCell:forTableColumn:row:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5whk3loifzxg33dnfqxi2lpnyxxiylcnrsvm2lfo45ho2lmnrcgs43qnrqxsq3fnrwduztpojkgcytmmvbw63dvnvxdu4tpo45a)
>
> **Control delegate methods**
> : [- control:didFailToFormatString:errorDescription:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5whk3loifzxg33dnfqxi2lpnyxwg33oorzg63b2mruwirtbnfwfi32gn5zg2ylukn2he2lom45gk4tsn5zeizltmnzgs4dunfxw4oq)
> : [- control:isValidObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5whk3loifzxg33dnfqxi2lpnyxwg33oorzg63b2nfzvmylmnfse6ytkmvrxioq)
> : [- control:textShouldBeginEditing:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5whk3loifzxg33dnfqxi2lpnyxwg33oorzg63b2orsxq5ctnbxxk3deijswo2loivsgs5djnzttu)

## Instance Methods

---

### control:didFailToFormatString:errorDescription:

`- (BOOL)control:(NSControl
*)aTableView
didFailToFormatString:(NSString
*)aString
errorDescription:(NSString *)errorDescription`

Invokes [shouldEndEditingForAspect:invalidInput:errorDescription:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwq33vnrsek3teivsgs5djnztum33sifzxazldoq5gs3twmfwgszcjnzyhk5b2mvzhe33sirsxgy3snfyhi2lpny5a) (defined
by EOAssociation) and returns the result.

---

### control:isValidObject:

`- (BOOL)control:(NSControl
*)aTableView
isValidObject:(id)anObject`

Saves the value of any cell being edited using [setValue:forAspect:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwk5cwmfwhkzj2mzxxeqltobswg5b2),
and if successful sends an [associationDidEndEditing:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc43tn5rwsylunfxw4rdjmrcw4zcfmruxi2lom45a) message
to the receiver's EODisplayGroup. Returns YES if successful (or
if no changes need be saved), NO if unsuccessful.

---

### control:textShouldBeginEditing:

`- (BOOL)control:(NSControl
*)aTableView
textShouldBeginEditing:(NSText
*)fieldEditor`

Sends an [associationDidBeginEditing:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc43tn5rwsylunfxw4rdjmrbgkz3jnzcwi2lunfxgooq) message
to the receiver's EODisplayGroup and returns YES.

---

### setSortingSelector:

`- (void)setSortingSelector:(SEL)aSelector`

Sets the method selector used to sort rows to _aSelector_,
one of (defined in EOControl):

- EOCompareAscending
- EOCompareDescending
- EOCompareCaseInsensitiveAscending
- EOCompareCaseInsensitiveDescending
- nil (to tell the receiver not to sort)

For
more information on these selectors, see the section "Comparison
Methods" in the EOSortOrdering class specification (EOControl).

If
the EOTableViewAssociation for the receiver's NSTableView (Application
Kit) sorts its rows, it applies this method as needed to sort them.
The default sorting selector is EOCompareAscending.

---

### sortingSelector

`- (SEL)sortingSelector`

Returns the method selector used to sort rows,
or nil if the column isn't sorted.

---

### tableView:objectValueForTableColumn:row:

`- (id)tableView:(NSTableView
*)aTableView
objectValueForTableColumn:(NSTableColumn
*)aTableColumn
row:(int)rowIndex`

Returns the value of the property of the object
at _rowIndex_ bound to the __value__ aspect.

---

### tableView:setObjectValue:forTableColumn:row:

`- (void)tableView:(NSTableView
*)aTableView
setObjectValue:(id)value
forTableColumn:(NSTableColumn
*)aTableColumn
row:(int)rowIndex`

Sets the property of the object at _rowIndex_ bound
to the __value__ aspect to _value_.

---

### tableView:shouldEditTableColumn:row:

`- (BOOL)tableView:(NSTableView
*)aTableView
shouldEditTableColumn:(NSTableColumn
*)aTableColumn
row:(int)rowIndex`

Returns NO if the __enabled__ aspect
is bound and its value for the object at _rowIndex_ is NO.
Otherwise returns YES. Note that because the __enabled__ aspects
of EOTableViewAssociation and EOColumnAssociation can be bound to
different keys, you can limit editability to the whole row or to
an individual cell (column) in that row.

---

### tableView:willDisplayCell:forTableColumn:row:

`- (void)tableView:(NSTableView
*)aTableView
willDisplayCell:(id)aCell
forTableColumn:(NSTableColumn
*)aTableColumn
row:(int)rowIndex`

Alters the display characteristics for _aCell_ according
to the values for the __enabled__ aspect of
the object at _rowIndex_.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
