---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EODetailDataSource.html
archived_at: '2026-07-15T08:11:39.639023Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EODetailDataSource

> **__Inherits
> from:__**
> : [EODataSource](EODataSource-3.md#apple-ivhuiylumfjw65lsmnsq)
> : NSObject

> **__Conforms to:__**
> : NSObject
> : (NSObject)

> __Declared in:__ : EOControl/EODetailDataSource.h

---

## Class Description

---

EODetailDataSource defines a data source for use in master-detail
configurations, where operations in the detail data source are applied
directly to properties of a master object. EODetailDataSource implements
the standard [fetchObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5tgk5ddnbhwe2tfmn2hg), [insertObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5uw443foj2e6ytkmvrxioq),
and [deleteObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5sgk3dforsu6ytkmvrxioq) methods
to operate on a relationship property of its master object, so it
works for any concrete subclass of EODataSource, including another
EODetailDataSource (for a chain of three master and detail data
sources).

To set up an EODetailDataSource programmatically, you typically
create it by sending a [dataSourceQualifiedByKey:](EODataSource-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcu3povzggzjpmrqxiyktn52xey3fkf2wc3djmzuwkzccpffwk6j2) message
to the master data source, then establish the master object with
a [qualifyWithRelationshipKey:ofObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5yxkylmnfthsv3jorufezlmmf2gs33oonugs4clmv4tu33gj5rguzldoq5a) message.
The latter method records the name of a relationship for a particular
object to resolve in __fetchObjects__ and to
modify in __insertObject:__, and __deleteObject:__. These
three methods then manipulate the relationship property of the master
object to perform the operations requested. See the individual method
descriptions for more information.

## Method Types

---

> **Creating instances**
> : [- initWithMasterClassDescription:detailKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5uw42luk5uxi2cnmfzxizlsinwgc43tirsxgy3snfyhi2lpny5gizlumfuwys3fpe5a)
> : [- initWithMasterDataSource:detailKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5uw42luk5uxi2cnmfzxizlsirqxiyktn52xey3fhjsgk5dbnfwewzlzhi)
>
> **Qualifying instances**
> : [- qualifyWithRelationshipKey:ofObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5yxkylmnfthsv3jorufezlmmf2gs33oonugs4clmv4tu33gj5rguzldoq5a)
>
> **Examining instances**
> : [- masterDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5wwc43umvzeiylumfjw65lsmnsq)
> : [- detailKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5sgk5dbnfwewzlz)
> : [- masterObject](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5wwc43umvze6ytkmvrxi)
>
> **Accessing the master
> class description**
> : [- masterClassDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5wwc43umvzeg3dbonzuizltmnzgs4dunfxw4)
> : [- setMasterClassDescription:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5zwk5cnmfzxizlsinwgc43tirsxgy3snfyhi2lpny5a)
>
> **Accessing the objects**
> : [- fetchObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5tgk5ddnbhwe2tfmn2hg)
>
> **Inserting and deleting
> objects**
> : [- insertObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5uw443foj2e6ytkmvrxioq)
> : [- deleteObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5sgk3dforsu6ytkmvrxioq)
>
> **Accessing the master
> editing context**
> : [- editingContext](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5swi2lunfxgoq3pnz2gk6du)

## Instance Methods

---

### deleteObject:

`- (void)deleteObject:(id)anObject`

Sends a [removeObject:fromPropertyWithKey:](EORelationshipManipulation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2smvwgc5djn5xhg2djobgwc3tjob2wyylunfxw4l3smvww65tfj5rguzldoq5gm4tpnvihe33qmvzhi6kxnf2gqs3fpe5a) message
(defined in the [EORelationshipManipulation](EORelationshipManipulation-2.md#apple-infemqsfireei) informal
protocol) to the master object with _anObject_ and
the receiver's detail key as the arguments. Raises an NSInternalInconsistencyException if
there's no master object or no detail key set.

---

### detailKey

`- (NSString *)detailKey`

Returns the name of the relationship for which
the receiver provides objects, as provided to [initWithMasterDataSource:detailKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5uw42luk5uxi2cnmfzxizlsirqxiyktn52xey3fhjsgk5dbnfwewzlzhi) or
as set in [qualifyWithRelationshipKey:ofObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5yxkylmnfthsv3jorufezlmmf2gs33oonugs4clmv4tu33gj5rguzldoq5a).
If none has been set yet, returns nil.

---

### editingContext

`- (EOEditingContext *)editingContext`

Returns the EOEditingContext of the master object,
or nil if there isn't one.

---

### fetchObjects

`- (NSArray *)fetchObjects`

Sends [valueForKey:](EOKeyValueCoding-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2lmv4vmylmovsug33enfxgol3wmfwhkzkgn5zewzlzhi) (defined in the [EOKeyValueCoding](EOKeyValueCoding-3.md#apple-ineucq2iizduu) informal
protocol) to the master object with the receiver's detail key
as the argument, constructs an array for the returned object or
objects, and returns it. Returns an empty array if there's no
master object, or returns an array containing the master object itself
if no detail key is set.

---

### initWithMasterClassDescription:detailKey:

`- initWithMasterClassDescription:(EOClassDescription
*)masterClassDescription detailKey:(NSString
*)relationshipKey`

Initializes a newly allocated EODetailDataSource
to provide objects based on a relationship of objects in the master
object associated with _masterClassDescription_.
Invokes [qualifyWithRelationshipKey:ofObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5yxkylmnfthsv3jorufezlmmf2gs33oonugs4clmv4tu33gj5rguzldoq5a) with _relationshipKey_ specified
as the relationship key and nil specified as the object. The receiver
initially has no master object selected; to select one, use __qualifyWithRelationshipKey:ofObject:__.
This is the designated initializer for the EODetailDataSource class.
Returns __self__.

__See
Also:__  [- masterClassDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5wwc43umvzeg3dbonzuizltmnzgs4dunfxw4), [- detailKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5sgk5dbnfwewzlz)

---

### initWithMasterDataSource:detailKey:

`- (id)initWithMasterDataSource:(EODataSource
*)masterDataSource
detailKey:(NSString *)relationshipKey`

Initializes a newly allocated EODetailDataSource
to provide objects based on a relationship of objects in _masterDataSource_ named
by _relationshipKey_. Invokes [initWithMasterClassDescription:detailKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5uw42luk5uxi2cnmfzxizlsinwgc43tirsxgy3snfyhi2lpny5gizlumfuwys3fpe5a) with
nil specified for the class description and _relationshipKey_ specified
as the detail key. The receiver initially has no master object selected;
to select one, use [qualifyWithRelationshipKey:ofObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5yxkylmnfthsv3jorufezlmmf2gs33oonugs4clmv4tu33gj5rguzldoq5a). Returns __self__.

__See
Also:__  [- masterDataSource](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5wwc43umvzeiylumfjw65lsmnsq), [- detailKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5sgk5dbnfwewzlz)

---

### insertObject:

`- (void)insertObject:(id)anObject`

Sends an [addObject:toBothSidesOfRelationshipWithKey:](EORelationshipManipulation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2smvwgc5djn5xhg2djobgwc3tjob2wyylunfxw4l3bmrse6ytkmvrxiotun5bg65diknuwizltj5tfezlmmf2gs33oonugs4cxnf2gqs3fpe5a) message
(defined in the [EORelationshipManipulation](EORelationshipManipulation-2.md#apple-infemqsfireei) informal
protocol) to the master object with _anObject_ and
the receiver's detail key as the arguments. Raises an NSInternalInconsistencyException if
there's no master object or no detail key set.

---

### masterClassDescription

`- (EOClassDescription *)masterClassDescription`

Returns the EOClassDescription of the receiver's
master object.

__See Also:__  [- setMasterClassDescription:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5zwk5cnmfzxizlsinwgc43tirsxgy3snfyhi2lpny5a), [- initWithMasterClassDescription:detailKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5uw42luk5uxi2cnmfzxizlsinwgc43tirsxgy3snfyhi2lpny5gizlumfuwys3fpe5a)

---

### masterDataSource

`- (EODataSource *)masterDataSource`

Returns the receiver's master data source.

__See
Also:__  [- detailKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5sgk5dbnfwewzlz), [- initWithMasterDataSource:detailKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5uw42luk5uxi2cnmfzxizlsirqxiyktn52xey3fhjsgk5dbnfwewzlzhi)

---

### masterObject

`- (id)masterObject`

Returns the object in the master data source
for which the receiver provides objects. You can change this with
a [qualifyWithRelationshipKey:ofObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5yxkylmnfthsv3jorufezlmmf2gs33oonugs4clmv4tu33gj5rguzldoq5a) message.

__See
Also:__  [- detailKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5sgk5dbnfwewzlz)

---

### __qualifyWithRelationshipKey:ofObject:__

`- (void)qualifyWithRelationshipKey:(NSString
*)relationshipKey
ofObject:(id)masterObject`

Configures the receiver to provide objects based
on the relationship of _masterObject_ named
by _relationshipKey_. _relationshipKey_ can
be different from the one used with [initWithMasterDataSource:detailKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5uw42luk5uxi2cnmfzxizlsirqxiyktn52xey3fhjsgk5dbnfwewzlzhi),
which changes the relationship the receiver operates on. If _masterObject_ is nil,
this method causes the receiver to return an empty array when sent
a [fetchObjects](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5tgk5ddnbhwe2tfmn2hg) message.

__See
Also:__  [- detailKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5sgk5dbnfwewzlz)

---

### setMasterClassDescription:

`- (void)setMasterClassDescription:(EOClassDescription
*)classDescription`

Assigns _classDescription_ as
the EOClassDescription for the receiver's master object.

__See
Also:__  [- masterClassDescription](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emv2gc2lmirqxiyktn52xey3ff5wwc43umvzeg3dbonzuizltmnzgs4dunfxw4)

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
