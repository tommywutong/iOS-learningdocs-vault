---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/EOTableViewAssociation.html
archived_at: '2026-07-15T08:11:45.622589Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EOTableViewAssociation

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

An EOTableViewAssociation object manages the individual EOColumnAssociations
between an NSTableView (Application Kit) and an EODisplayGroup.

An EOTableViewAssociation can sort the objects in the display
group by the left-to-right order of the table columns. The first
EOColumnAssociation to be bound to a table view automatically creates
the EOTableViewAssociation; you should rarely need to do so yourself.

An EOTableViewAssociation receives data source and delegate
messages from the table view, some of which it handles itself, and
some of which it forwards to the appropriate EOColumnAssociations.
For more information, see the EOColumnAssociation class specification.

|  |
| --- |
| __Usable With__ |
| NSTableView |

|  |
| --- |
| __Aspects__ |
| source | Bound to the EODisplayGroup providing objects. This aspect doesn't use a key. |
| enabled | A boolean attribute of the objects, which determines whether each object's row is editable. Note that because EOColumnAssociation also uses this aspect, you can use it with different keys to limit editability to the whole row or to an individual cell (column) in that row. |
| textColor | An NSColor attribute of the objects, which determines the color of text for each object's row in the NSTableView. |
| bold | A boolean attribute of the objects, which determines whether each objects row is displayed in bold or regular weight text. |
| italic | A boolean attribute of the objects, which determines whether each objects row is displayed in italic or normal angle text. |

|  |
| --- |
| __Object Keys Taken__ |
| dataSource | An EOTableViewAssociation responds to some data source messages and forwards others to the appropriate EOColumnAssociation. |
| delegate | An EOTableViewAssociation forwards delegate messages to the appropriate EOColumnAssociations. |
| target | Reserved, but not used. |

## Example

For an example of using an EOTableViewAssociation, see the
EOColumnAssociation class specification.

## Method Types

---

> **Setting up a table view
> association**
> : [+ bindToTableView:displayGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhviylcnrsvm2lfo5axg43pmnuwc5djn5xc6ytjnzsfi32umfrgyzkwnfsxootenfzxa3dbpfdxe33voa5a)
>
> **Sorting**
> : [- setSortsByColumnOrder:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2umfrgyzkwnfsxoqltonxwg2lboruw63rponsxiu3poj2hgqtzinxwy5lnnzhxezdfoi5a)
> : [- sortsByColumnOrder](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2umfrgyzkwnfsxoqltonxwg2lboruw63rponxxe5dtij4ug33movww4t3smrsxe)
>
> **Accessing the active
> EOColumnAssociation**
> : [- editingAssociation](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2umfrgyzkwnfsxoqltonxwg2lboruw63rpmvsgs5djnztuc43tn5rwsylunfxw4)
>
> **Table view data source
> methods**
> : [- numberOfRowsInTableView:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2umfrgyzkwnfsxoqltonxwg2lboruw63rpnz2w2ytfojhwmutpo5zus3sumfrgyzkwnfsxooq)
> : [- tableView:setObjectValue:forTableColumn:row:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2umfrgyzkwnfsxoqltonxwg2lboruw63rporqwe3dfkzuwk5z2onsxit3cnjswg5cwmfwhkzj2mzxxevdbmjwgkq3pnr2w23r2ojxxooq)
> : [- tableView:objectValueForTableColumn:row:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2umfrgyzkwnfsxoqltonxwg2lboruw63rporqwe3dfkzuwk5z2n5rguzldorlgc3dvmvdg64sumfrgyzkdn5whk3lohjzg65z2)
>
> **Table view delegate methods**
> : [- tableView:shouldEditTableColumn:row:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2umfrgyzkwnfsxoqltonxwg2lboruw63rporqwe3dfkzuwk5z2onug65lmmrcwi2lukrqwe3dfinxwy5lnny5he33xhi)
> : [- tableView:willDisplayCell:forTableColumn:row:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2umfrgyzkwnfsxoqltonxwg2lboruw63rporqwe3dfkzuwk5z2o5uwy3cenfzxa3dbpfbwk3dmhjtg64sumfrgyzkdn5whk3lohjzg65z2)
>
> **Table view notification
> methods**
> : [- tableViewSelectionDidChange:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2umfrgyzkwnfsxoqltonxwg2lboruw63rporqwe3dfkzuwk52tmvwgky3unfxw4rdjmrbwqylom5stu)
>
> **Control delegate methods**
> : [- control:didFailToFormatString:errorDescription:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2umfrgyzkwnfsxoqltonxwg2lboruw63rpmnxw45dsn5wduzdjmrdgc2lmkrxum33snvqxiu3uojuw4zz2mvzhe33sirsxgy3snfyhi2lpny5a)
> : [- control:isValidObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2umfrgyzkwnfsxoqltonxwg2lboruw63rpmnxw45dsn5wdu2ltkzqwy2lej5rguzldoq5a)
> : [- control:textShouldBeginEditing:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2umfrgyzkwnfsxoqltonxwg2lboruw63rpmnxw45dsn5wdu5dfpb2fg2dpovwgiqtfm5uw4rlenf2gs3thhi)

## Class Methods

---

### bindToTableView:displayGroup:

`+ (void)bindToTableView:(NSTableView
*)aTableView
displayGroup:(EODisplayGroup *)aDisplayGroup`

Creates an EOTableViewAssociation, binding _aTableView_ to _aDisplayGroup_,
if there isn't already a table view association for _aTableView_.
EOColumnAssociation's __establishConnection__ invokes
this method to guarantee the presence of a coordinating EOTableViewAssociation.

---

## Instance Methods

---

### control:didFailToFormatString:errorDescription:

`- (BOOL)control:(NSControl
*)aTableView
didFailToFormatString:(NSString
*)aString
errorDescription:(NSString *)errorDescription`

Forwards the message to the receiver's editing
association.

__See Also:__  [- editingAssociation](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2umfrgyzkwnfsxoqltonxwg2lboruw63rpmvsgs5djnztuc43tn5rwsylunfxw4)

---

### control:isValidObject:

`- (BOOL)control:(NSControl
*)aTableView
isValidObject:(id)anObject`

Forwards the message to the receiver's editing
association.

__See Also:__  [- editingAssociation](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2umfrgyzkwnfsxoqltonxwg2lboruw63rpmvsgs5djnztuc43tn5rwsylunfxw4)

---

### control:textShouldBeginEditing:

`- (BOOL)control:(NSControl
*)aTableView
textShouldBeginEditing:(NSText
*)fieldEditor`

Forwards the message to the receiver's editing
association.

__See Also:__  [- editingAssociation](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2umfrgyzkwnfsxoqltonxwg2lboruw63rpmvsgs5djnztuc43tn5rwsylunfxw4)

---

### editingAssociation

`- (EOColumnAssociation *)editingAssociation`

Returns the EOColumnAssociation for the NSTableView
cell being edited, or nil if no cell is being edited.

---

### numberOfRowsInTableView:

`- (int)numberOfRowsInTableView:(NSTableView
*)aTableView`

Returns the number of displayed objects in the
receiver's EODisplayGroup.

__See Also:__  [- displayedObjects](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg) (EODisplayGroup)

---

### setSortsByColumnOrder:

`- (void)setSortsByColumnOrder:(BOOL)flag`

Controls whether the receiver applies a sort
ordering to its EODisplayGroup. If _flag_ is YES,
it builds EOSortOrderings (EOControl) for each of the EOColumnAssociations,
collects them into an NSArray based on the left-to-right order of
the columns, and assigns them to the display group with [setSortOrderings:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknxxe5cpojsgk4tjnztxgoq). If _flag_ is NO,
it doesn't alter the sort ordering of the display group.

An
EOTableViewAssociation assigns sort orderings based on the left
to right order of the table columns, and reassigns them whenever
the user moves a column.

__See Also:__  [- sortingSelector](EOColumnAssociation.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dn5whk3loifzxg33dnfqxi2lpnyxxg33soruw4z2tmvwgky3un5za) (EOColumnAssociation)

---

### sortsByColumnOrder

`- (BOOL)sortsByColumnOrder`

Returns YES if the receiver assigns EOSortOrderings
(EOControl) to its EODisplayGroup based on the sorting selectors
of its EOColumnAssociations, NO if it doesn't alter the display
group's sort ordering.

---

### tableView:objectValueForTableColumn:row:

`- (id)tableView:(NSTableView
*)aTableView
objectValueForTableColumn:(NSTableColumn
*)aTableColumn
row:(int)rowIndex`

Forwards the message to _aTableColumn_'s
identifier-assumed to be the EOColumnAssociation bound to that
column-so that it can provide the value.

---

### tableViewSelectionDidChange:

`- (void)tableViewSelectionDidChange:(NSNotification
*)aNotification`

Updates the receiver's EODisplayGroup based
on the new selection in the table view.

__See
Also:__  [- setSelectionIndexes:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldoruw63sjnzsgk6dfom5a) (EODisplayGroup)

---

### tableView:setObjectValue:forTableColumn:row:

`- (void)tableView:(NSTableView
*)aTableView
setObjectValue:(id)value
forTableColumn:(NSTableColumn
*)aTableColumn
row:(int)rowIndex`

Forwards the message to _aTableColumn_'s
identifier-assumed to be the EOColumnAssociation bound to that
column-so that it can set the value.

---

### tableView:shouldEditTableColumn:row:

`- (BOOL)tableView:(NSTableView
*)aTableView
shouldEditTableColumn:(NSTableColumn
*)aTableColumn
row:(int)rowIndex`

Returns NO if the `enabled` aspect
is bound and its value for the object at _rowIndex_ is NO.
Otherwise forwards the message to _aTableColumn_'s
identifier-assumed to be the EOColumnAssociation bound to that
column-and returns its response. Note that because the two associations' `enabled` aspects
can be bound to different keys, you can limit editability to the
whole row or to an individual cell (column) in that row.

---

### tableView:willDisplayCell:forTableColumn:row:

`- (void)tableView:(NSTableView
*)aTableView
willDisplayCell:(id)aCell
forTableColumn:(NSTableColumn
*)aTableColumn
row:(int)rowIndex`

Alters the display characteristics for _aCell_ according
to the values for the __enabled__, __textColor__, __bold__,
and __italic__ aspects of the object at _rowIndex_.
Then forwards the message to _aTableColumn_'s
identifier-assumed to be the EOColumnAssociation bound to that
column-allowing it to adjust _aCell_ based
on its own __enabled__ aspect.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
