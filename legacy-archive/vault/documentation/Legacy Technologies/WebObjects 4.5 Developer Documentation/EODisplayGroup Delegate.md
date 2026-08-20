---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Protocols/EODisplayGroupDelegate.html
archived_at: '2026-07-15T08:11:45.727010Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md) 

# EODisplayGroup Delegate

> __(informal protocol)__

> __Declared in:__ : EOInterface/EODisplayGroup.h

---

## Protocol Description

---

The EODisplayGroup Delegate informal
protocol defines methods that an EODisplayGroup can invoke in its
delegate. Delegates are not required to provide implementations
for all of the methods in the informal protocol. Instead, declare
and implement any subset of the methods declared in the informal
protocol that you need, and use the EODisplayGroup method [setDelegate:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluirswyzlhmf2gkoq) method to assign your
object as the delegate. A display group can determine if the delegate
doesn't implement a delegate method and only attempts to invoke
the methods the delegate actually implements.

## Method Types

---

> **Fetching objects**
> : [- displayGroupShouldFetch:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xau3in52wyzcgmv2gg2b2)
> : [- displayGroup:didFetchObjects:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotenfsemzlumnue6ytkmvrxi4z2)
> : [- displayGroup:shouldRefetchForInvalidatedAllObjectsNotification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaottnbxxk3dekjswmzlumnuem33sjfxhmylmnfsgc5dfmrawy3cpmjvgky3uonhg65djmzuwgylunfxw4oq)
>
> **Inserting, updating,
> and deleting objects**
> : [- displayGroup:shouldInsertObject:atIndex:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaottnbxxk3dejfxhgzlsorhwe2tfmn2duylujfxgizlyhi)
> : [- displayGroup:didInsertObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotenfses3ttmvzhit3cnjswg5b2)
> : [- displayGroup:createObjectFailedForDataSource:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotdojswc5dfj5rguzldordgc2lmmvsem33sirqxiyktn52xey3fhi)
> : [- displayGroup:didSetValue:forObject:key:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotenfsfgzlukzqwy5lfhjtg64spmjvgky3uhjvwk6j2)
> : [- displayGroup:shouldDeleteObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaottnbxxk3deirswyzlumvhwe2tfmn2du)
> : [- displayGroup:didDeleteObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotenfseizlmmv2gkt3cnjswg5b2)
>
> **Managing the display**
> : [- displayGroup:shouldDisplayAlertWithTitle:message:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaottnbxxk3deiruxg4dmmf4uc3dfoj2fo2lunbkgs5dmmu5g2zltonqwozj2)
> : [- displayGroup:shouldRedisplayForChangesInEditingContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaottnbxxk3dekjswi2ltobwgc6kgn5zeg2dbnztwk42jnzcwi2lunfxgoq3pnz2gk6duhi)
> : [- displayGroup:displayArrayForObjects:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaotenfzxa3dbpfaxe4tbpfdg64spmjvgky3uom5a)
>
> **Managing the selection**
> : [- displayGroup:shouldChangeSelectionToIndexes:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xaottnbxxk3deinugc3thmvjwk3dfmn2gs33okrxus3temv4gk4z2)
> : [- displayGroupDidChangeSelection:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xardjmrbwqylom5svgzlmmvrxi2lpny5a)
> : [- displayGroupDidChangeSelectedObjects:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xardjmrbwqylom5svgzlmmvrxizlej5rguzldorztu)
>
> **Changing the data source**
> : [- displayGroupDidChangeDataSource:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2enfzxa3dbpfdxe33voaqeizlmmvtwc5dff5sgs43qnrqxsr3sn52xardjmrbwqylom5suiylumfjw65lsmnstu)

## Instance Methods

---

### displayGroup:createObjectFailedForDataSource:

`- (void)displayGroup:(EODisplayGroup
*)aDisplayGroup
createObjectFailedForDataSource:(EODataSource
*)aDataSource`

Invoked from [insertObjectAtIndex:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxws3ttmvzhit3cnjswg5cborew4zdfpa5a) to inform the
delegate that _aDisplayGroup_ has failed
to create a new object for _aDataSource_.
If the delegate doesn't implement this method, the EODisplayGroup
instead runs an alert panel to inform the user of the failure.

---

### displayGroupDidChangeDataSource:

`- (void)displayGroupDidChangeDataSource:(EODisplayGroup
*)aDisplayGroup`

Informs the delegate that _aDisplayGroup_'s
EODataSource has changed.

---

### displayGroupDidChangeSelectedObjects:

`- (void)displayGroupDidChangeSelectedObjects:(EODisplayGroup
*)aDisplayGroup`

Informs the delegate that _aDisplayGroup_'s
set of selected objects has changed, regardless of whether the selection
indexes have changed.

---

### displayGroupDidChangeSelection:

`- (void)displayGroupDidChangeSelection:(EODisplayGroup
*)aDisplayGroup`

Informs the delegate that _aDisplayGroup_'s
selection has changed.

---

### displayGroup:didDeleteObject:

`- (void)displayGroup:(EODisplayGroup
*)aDisplayGroup
didDeleteObject:(id)anObject`

Informs the delegate that _aDisplayGroup_ has
deleted _anObject_.

---

### displayGroup:didFetchObjects:

`- (void)displayGroup:(EODisplayGroup
*)aDisplayGroup
didFetchObjects:(NSArray *)objects`

Informs the delegate that _aDisplayGroup_ has
fetched _objects_.

---

### displayGroup:didInsertObject:

`- (void)displayGroup:(EODisplayGroup
*)aDisplayGroup
didInsertObject:(id)anObject`

Informs the delegate that _aDisplayGroup_ has
inserted _anObject_.

---

### displayGroup:didSetValue:forObject:key:

`- (void)displayGroup:(EODisplayGroup
*)aDisplayGroup
didSetValue:(id)value
forObject:(id)anObject
key:(NSString *)key`

Informs the delegate that _aDisplayGroup_ has
altered a property value of _anObject_. _key_ identifies
the property, and _value_ is its new
value.

---

### displayGroup:displayArrayForObjects:

`- (NSArray *)displayGroup:(EODisplayGroup
*)aDisplayGroup
displayArrayForObjects:(NSArray
*)objects`

Invoked from [updateDisplayedObjects](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxk4demf2gkrdjonygyylzmvse6ytkmvrxi4y),
this method allows the delegate to filter and sort _aDisplayGroup_'s
array of objects to limit which ones get displayed. _objects_ contains
all of _aDisplayGroup_'s objects.
The delegate should filter any objects that shouldn't be shown
and sort the remainder, returning a new array containing this group
of objects. You can use the NSArray methods __filteredArrayUsingQualifier:__ and __sortedArrayUsingKeyOrderArray:__ added in
EOControl to create the new array.

If the delegate doesn't implement this method, the EODisplayGroup
uses its own qualifier and sort ordering to update its displayed
objects array.

__See Also:__
[- sortOrderings](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxg33sorhxezdfojuw4z3t), [- qualifier](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxc5lbnruwm2lfoi), [- displayedObjects](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwi2ltobwgc6lfmrhwe2tfmn2hg)

---

### displayGroup:shouldChangeSelectionToIndexes:

`- (BOOL)displayGroup:(EODisplayGroup
*)aDisplayGroup
shouldChangeSelectionToIndexes:(NSArray
*)newIndexes`

Allows the delegate to prevent a change in selection
by _aDisplayGroup_. _newIndexes_ is
the proposed new selection, an array of NSNumbers. If the delegate
returns YES, the selection changes; if the delegate returns NO,
the selection remains as it is.

---

### displayGroup:shouldDeleteObject:

`- (BOOL)displayGroup:(EODisplayGroup
*)aDisplayGroup
shouldDeleteObject:(id)anObject`

Allows the delegate to prevent _aDisplayGroup_ from
deleting _anObject_. If the delegate
returns YES, _anObject_ is deleted;
if the delegate returns NO, the deletion is abandoned.

---

### displayGroup:shouldDisplayAlertWithTitle:message:

`- (BOOL)displayGroup:(EODisplayGroup
*)aDisplayGroup
shouldDisplayAlertWithTitle:(NSString
*)title
message:(NSString *)message`

Allows the delegate to prevent _aDisplayGroup_ from
displaying an attention panel with _title_ and _message_.
The delegate can return YES to allow _aDisplayGroup_ to
display the panel, or NO to prevent it from doing so (perhaps displaying
a different attention panel).

---

### displayGroupShouldFetch:

`- (BOOL)displayGroupShouldFetch:(EODisplayGroup
*)aDisplayGroup`

Allows the delegate to prevent _aDisplayGroup_ from
fetching. If the delegate returns YES, _aDisplayGroup_ performs
the fetch; if the delegate returns NO, _aDisplayGroup_ abandons
the fetch.

---

### displayGroup:shouldInsertObject:atIndex:

`- (BOOL)displayGroup:(EODisplayGroup
*)aDisplayGroup
shouldInsertObject:(id)anObject
atIndex:(unsigned int)anIndex`

Allows the delegate to prevent _aDisplayGroup_ from
inserting _anObject_ at _anIndex_.
If the delegate returns YES, _anObject_ is
inserted; if the delegate returns NO, the insertion is abandoned.

---

### displayGroup:shouldRedisplayForChangesInEditingContext:

`- (BOOL)displayGroup:(EODisplayGroup
*)aDisplayGroup
shouldRedisplayForEditingContextChangeNotification:(NSNotification
*)aNotification`

Invoked whenever _aDisplayGroup_ receives
an `EOObjectsChangedInEditingContextNotification`,
this method allows the delegate to suppress redisplay based on the
nature of the change that has occurred. If the delegate returns YES, _aDisplayGroup_ redisplays;
if it returns NO, _aDisplayGroup_ doesn't. _aNotification_ supplies
the EOEditingContext that has changed, as well as which objects
have changed and how. See the EOEditingContext class specification
for information on `EOObjectsChangedInEditingContextNotification`.

__See Also:__
[- redisplay](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxezlenfzxa3dbpe)

---

### displayGroup:shouldRefetchForInvalidatedAllObjectsNotification:

`- (BOOL)displayGroup:(EODisplayGroup
*)aDisplayGroup
shouldRefetchForInvalidatedAllObjectsNotification:(NSNotification
*)aNotification`

Invoked whenever _aDisplayGroup_ receives
an `EOInvalidatedAllObjectsInStoreNotification`,
this method allows the delegate to suppress refetching of the invalidated
objects. If the delegate returns YES, _aDisplayGroup_ immediately
refetches its objects. If the delegate returns NO, _aDisplayGroup_ doesn't immediately
fetch, instead delaying until absolutely necessary. _aNotification_ is
an NSNotification. See the EOObjectStore and EOEditingContext class
specifications for information on this notification.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
