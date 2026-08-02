---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOQualifierComparison.html
archived_at: '2026-07-15T08:11:43.530144Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOQualifierComparison

> __(informal protocol)__

> __Declared in:__ : EOControl/EOQualifier.h

---

## Protocol Description

---

The EOQualifierComparison informal
protocol defines methods for comparing values. These methods are
used for evaluating qualifiers in memory.

|  |
| --- |
| __Note:__  This interface doesn't exist in the Yellow Box package, com.apple.yellow.eocontrol |

Though declared for NSObject, most of these methods work properly
only with value classes: NSString, NSDate, NSNumber, NSDecimalNumber,
and EONull.

## Method Types

---

> **Testing value objects**
> : [- doesContain:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeq3pnvygc4tjonxw4l3en5sxgq3pnz2gc2lohi)
> : [- isEqualTo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeq3pnvygc4tjonxw4l3joncxc5lbnrkg6oq)
> : [- isGreaterThan:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeq3pnvygc4tjonxw4l3jondxezlborsxevdimfxdu)
> : [- isGreaterThan:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeq3pnvygc4tjonxw4l3jondxezlborsxevdimfxdu)
> : [- isLessThan:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeq3pnvygc4tjonxw4l3jonggk43tkrugc3r2)
> : [- isLessThanOrEqualTo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeq3pnvygc4tjonxw4l3jonggk43tkrugc3spojcxc5lbnrkg6oq)
> : [- isLike:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeq3pnvygc4tjonxw4l3jonggs23fhi)
> : [- isCaseInsensitiveLike:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeq3pnvygc4tjonxw4l3jonbwc43fjfxhgzloonuxi2lwmvggs23fhi)
> : [- isNotEqualTo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeq3pnvygc4tjonxw4l3jonhg65cfof2wc3cun45a)

## Instance Methods

---

### doesContain:

`- (BOOL)doesContain:(id)anObject`

Returns `YES` if
the receiver contains _anObject_, `NO` if
it doesn't. NSObject's implementation of this method returns `YES` only
if the receiver is a kind of NSArray and contains _anObject_.
In all other cases it returns `NO`.

---

### isCaseInsensitiveLike:

`- (BOOL)isCaseInsensitiveLike:(NSString
*)anObject`

Returns `YES` if
the receiver is a case-insensitive match for _anObject_, `NO` if
it isn't. See ["Using Wildcards and the like Operator" on page 266](EOQualifier-4.md#apple-ijbesqsjijaue) for the wildcard characters allowed.

---

### isEqualTo:

`- (BOOL)isEqualTo:(id)anObject`

Returns `YES` if
the receiver is equal to _anObject_, `NO` if
it isn't. NSObject's implementation invokes __isEqual:__ and
returns the result.

---

### isGreaterThan:

`- (BOOL)isGreaterThan:(id)anObject`

Returns `YES` if
the receiver is greater than _anObject_, `NO` if
it isn't. NSObject's implementation invokes __compare:__ and
returns `YES` if the result
is NSOrderedDescending.

---

### isGreaterThanOrEqualTo:

`- (BOOL)isGreaterThanOrEqualTo:(id)anObject`

Returns `YES` if
the receiver is greater than or equal to _anObject_, `NO` if
it isn't. NSObject's implementation invokes compare: and returns `YES` if
the result is NSOrderedAscending.

---

### isLessThan:

`- (BOOL)isLessThan:(id)anObject`

Returns `YES` if
the receiver is less than _anObject_, `NO` if
it isn't. NSObject's implementation invokes compare: and returns `YES` if
the result is NSOrderedAscending.

---

### isLessThanOrEqualTo:

`- (BOOL)isLessThanOrEqualTo:(id)anObject`

Returns `YES` if
the receiver is less than or equal to _anObject_, `NO` if
it isn't. NSObject's implementation invokes compare: and returns `YES` if
the result is NSOrderedAscending or NSOrderedSame.

---

### isLike:

`- (BOOL)isLike:(NSString
*)aString`

Returns `YES` if
the receiver matches _aString_ according
to the semantics of the SQL __like__ comparison operator, `NO` if
it doesn't. See ["Using Wildcards and the like Operator" on page 266](EOQualifier-4.md#apple-ijbesqsjijaue) for the wildcard characters allowed. NSObject's
implementation returns `NO`;
NSString's performs a proper comparison.

---

### isNotEqualTo:

`- (BOOL)isNotEqualTo:(id)anObject`

Returns `YES` if
the receiver is not equal to _anObject_, `NO` if
it is. NSObject's implementation invokes __isEqual:__,
inverts the result, and returns it.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
