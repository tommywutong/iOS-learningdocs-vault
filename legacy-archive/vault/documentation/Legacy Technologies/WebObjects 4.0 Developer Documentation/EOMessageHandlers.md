---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOMessageHandlers.html
archived_at: '2026-07-18T01:28:41.383883Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOKeyValueCodingAdditions-2.md)
[!](EOObserving-2.md)

---

# EOMessageHandlers

---

#### (informal protocol)

__Category Of:__ NSObject

__Declared in:__ EOControl/EOEditingContext.h

## Category Description

The EOMessageHandlers informal protocol declares methods used for error reporting and determining fetch limits. See the [EOEditingContext](EOEditingContext-3.md), EODatabaseContext (EOAccess), and EODisplayGroup (EOInterface) class specifications for more information.

Message handlers are primarily used to implement exception handling in the interface layer's EODisplayGroup, and wouldn't ordinarily be used in a command line tool or WebObjects application.

---

#### editingContext:presentErrorMessage:

- (void)__editingContext:__ (EOEditingContext \*)_anEditingContext___presentErrorMessage:__ (NSString \*)_message_

Invoked by _anEditingContext_, this method should present _message_ to the user in whatever way is appropriate (whether by opening an attention panel or printing the message in a terminal window, for example). This message is sent only if the method is implemented.

---

#### editingContext: shouldContinueFetchingWithCurrentObjectCount:originalLimit: objectStore:

- (BOOL)`editingContext:`(EOEditingContext \*)_anEditingContext_ `shouldContinueFetchingWithCurrentObjectCount:`(unsigned)_count_`originalLimit:`(unsigned)_limit_
`objectStore:`(EOObjectStore \*)_objectStore_

Invoked by an _objectStore_ (such as an access layer EODatabaseContext) to allow the message handler for _anEditingContext_ (often an interface layer EODisplayGroup) to prompt the user about whether or not to continue fetching the current result set. The _count_ argument is the number of objects fetched so far. _limit_ is the original limit specified an EOFetchSpecification. This message is sent only if the method is implemented.

---

[!](EOKeyValueCodingAdditions-2.md)
[!](EOObserving-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
