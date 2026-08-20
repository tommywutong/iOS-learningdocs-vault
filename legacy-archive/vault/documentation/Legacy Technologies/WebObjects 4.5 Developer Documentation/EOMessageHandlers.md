---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOMessageHandlers.html
archived_at: '2026-07-15T08:11:43.513002Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOMessageHandlers

> __(informal protocol)__

> __Declared in:__ : EOControl/EOEditingContext.h

---

## Protocol Description

---

The [EOMessageHandlers](#apple-ijdusrciinbek) informal
protocol declares methods used for error reporting and determining fetch
limits. See the [EOEditingContext](EOEditingContext-2.md#apple-ivhukzdjoruw4z2dn5xhizlyoq), EODatabaseContext
(EOAccess), and EODisplayGroup (EOInterface) class specifications
for more information.

Message handlers are primarily used to implement exception
handling in the interface layer's EODisplayGroup, and wouldn't
ordinarily be used in a command line tool or WebObjects application.

## Instance Methods

---

### editingContext:presentErrorMessage:

`- (void)editingContext:(EOEditingContext
*)anEditingContext
presentErrorMessage:(NSString
*)message`

Invoked by _anEditingContext_,
this method should present _message_ to
the user in whatever way is appropriate (whether by opening an attention
panel or printing the message in a terminal window, for example).
This message is sent only if the method is implemented.

---

### editingContext:shouldContinueFetchingWithCurrentObjectCount:originalLimit: objectStore:

`- (BOOL)editingContext:(EOEditingContext
*)anEditingContext
shouldContinueFetchingWithCurrentObjectCount:(unsigned)count
originalLimit:(unsigned)limit
objectStore:(EOObjectStore *)objectStore`

Invoked by an _objectStore_ (such
as an access layer EODatabaseContext) to allow the message handler for _anEditingContext_ (often
an interface layer EODisplayGroup) to prompt the user about whether
or not to continue fetching the current result set. The _count_ argument
is the number of objects fetched so far. _limit_ is
the original limit specified an EOFetchSpecification. This message
is sent only if the method is implemented.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
