---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOMessageHandlers.html
archived_at: '2026-07-15T08:11:38.962222Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOEditingContext.MessageHandler

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Interface Description

---

The [EOEditingContext.MessageHandler](#apple-ijdusrciinbek) interface declares
methods used for error reporting and determining fetch limits. See
the [EOEditingContext](EOEditingContext.md#apple-ivhukzdjoruw4z2dn5xhizlyoq), EODatabaseContext
(EOAccess), and EODisplayGroup (EOInterface) class specifications
for more information.

Message handlers are primarily used to implement exception
handling in the interface layer's EODisplayGroup, and wouldn't
ordinarily be used in a command line tool or WebObjects application.

Message handlers are not required to provide implementations
for all of the methods in the interface. When you write a handler,
you don't have to use the `implements` keyword
to specify that the object implements the EOEditingContext.MessageHandler interface.
Instead, simply use the EOEditingContext method [setMessageHandler](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxitlfonzwcz3fjbqw4zdmmvza) method
to assign your object as the EOEditingContext's handler and then
declare and implement any subset of the methods declared in the EOEditingContext.MessageHandler interface.
An EOEditingContext can determine if the handler doesn't implement
a method and only attempts to invoke the methods the handler actually implements.

## Instance Methods

---

### editingContextPresentErrorMessage

`public abstract void editingContextPresentErrorMessage(
EOEditingContext anEditingContext,
String message)`

Invoked by _anEditingContext,_
this method should present _message_ to
the user in whatever way is appropriate (whether by opening an attention
panel or printing the message in a terminal window, for example).
This message is sent only if the method is implemented.

---

### editingContextShouldContinueFetching

`public abstract boolean editingContextShouldContinueFetching(
EOEditingContext anEditingContext,
int count,
int limit,
EOObjectStore objectStore)`

Invoked by an _objectStore_ (such
as an access layer EODatabaseContext) to allow the message handler for _anEditingContext_ (often
an interface layer EODisplayGroup) to prompt the user about whether
or not to continue fetching the current result set. The _count_ argument
is the number of objects fetched so far. _limit_ is
the original limit specified an EOFetchSpecification. This message
is sent only if the method is implemented.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
