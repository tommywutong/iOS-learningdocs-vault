---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOMessageHandlers.html
archived_at: '2026-07-18T01:28:33.022303Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOKeyValueCodingAdditions.md)
[!](EOObserving.md)

---

# EOEditingContext.MessageHandler

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Interface Description

The EOEditingContext.MessageHandler interface declares methods used for error reporting and determining fetch limits. See the [EOEditingContext](EOEditingContext.md), EODatabaseContext (EOAccess), and EODisplayGroup (EOInterface) class specifications for more information.

Message handlers are primarily used to implement exception handling in the interface layer's EODisplayGroup, and wouldn't ordinarily be used in a command line tool or WebObjects application.

Message handlers are not required to provide implementations for all of the methods in the interface. When you write a handler, you don't have to use the __implements__ keyword to specify that the object implements the MessageHandler interface. Instead, simply use the EOEditingContext method [__setMessageHandler__](EOEditingContext.md)method to assign your object as the EOEditingContext's handler and then declare and implement any subset of the methods declared in the MessageHandler interface. An EOEditingContext can determine if the handler doesn't implement a method and only attempts to invoke the methods the handler actually implements

## Instance Methods

---

#### editingContextPresentException

public abstract void __editingContextPresentException__ (
EOEditingContext _anEditingContext_,
java.lang.Exception _anException_)

This method is available for Java Client applications only; the Yellow Box equivalent is __editingContextPresentErrorMessage__ .

Invoked by _anEditingContext_, this method should present an error message to the user in whatever way is appropriate (whether by opening an attention panel or printing the message in a terminal window, for example). The error message can be derived from _anException_, an exception that was thrown as the result of some error.

---

#### editingContextPresentErrorMessage

public abstract void __editingContextPresentErrorMessage__ (
EOEditingContext _anEditingContext_,
java.lang.String _message_)

This method is available for Yellow Box applications only; the Java Client equivalent is __editingContextPresentException__ .

Invoked by _anEditingContext_, this method should present _message_ to the user in whatever way is appropriate (whether by opening an attention panel or printing the message in a terminal window, for example). This message is sent only if the method is implemented.

---

#### editingContextShouldContinueFetching

public abstract boolean __editingContextShouldContinueFetching__ (
EOEditingContext _anEditingContext_,
int _count_,
int _limit_,
EOObjectStore _objectStore_)

Invoked by an _objectStore_ (such as an access layer EODatabaseContext) to allow the message handler for _anEditingContext_ (often an interface layer EODisplayGroup) to prompt the user about whether or not to continue fetching the current result set. The _count_ argument is the number of objects fetched so far. _limit_ is the original limit specified an EOFetchSpecification. This message is sent only if the method is implemented.

---

[!](EOKeyValueCodingAdditions.md)
[!](EOObserving.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
