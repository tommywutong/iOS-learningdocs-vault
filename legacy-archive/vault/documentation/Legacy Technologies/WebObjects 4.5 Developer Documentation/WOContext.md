---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Classes/WOContext.html
archived_at: '2026-07-15T08:11:46.767769Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOContext

> __Inherits
> from:__  NSObject

> __Package:__ com.apple.yellow.webobjects

---

## Class Description

---

A WOContext object lets you access objects and information
that define the _context_ of a transaction.
In a typical request-response loop (a transaction), several objects
have a hand in what is going on: the [WOApplication](WOApplication.md#apple-k5huc4dqnruwgylunfxw4) and [WOSession](WOSession.md#apple-k5hvgzltonuw63q) objects, the page involved
in the request or response (a [WOComponent](WOComponent.md#apple-k5hug33nobxw4zlooq) object), the page's subcomponents
(also WOComponents), plus the dynamic elements on the page. The
WOContext object passed as an argument in the [takeValuesFromRequest](WOComponent.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bporqwwzkwmfwhkzltizzg63ksmvyxkzltoq), [invokeActionForRequest](WOComponent.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnfxhm33lmvawg5djn5xem33skjsxc5lfon2a),
and [appendToResponse](WOComponent.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmfyhazlomrkg6utfonyg63ttmu) messages
allows access to these objects. A context is identified by the _context
ID_, which appears in the URL after the session ID
and page name. Each context ID is an integer that the session increments
each time a new context is created.

WOContext objects provide other information and services related
to the current transaction. From them you can get the entire URL
currently in effect as well as portions of that URL, such as the
element ID, the context ID, and the URL up to and including the
session ID.

A WOContext object plays a further role behind the scenes.
For the benefit of a page's dynamic elements, it keeps track of
the _current component_, that is, the
WOComponent associated with the current element in the request-handling
cycle. The current component can be the WOComponent that represents
one of the page's subcomponents or the page itself. By reference
to the current component (accessed through WOContext's [component](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6y3pnvyg63tfnz2a) method),
a dynamic element can exchange values associatively between itself
and the WOComponent that contains it.

## Method Types

---

> **Constructors**
> : [WOContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6v2pinxw45dfpb2a)
>
> **Creating new object instances**
> : [contextWithRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6q3pnz2gk6duf5rw63tumv4hiv3jorufezlrovsxg5a)
>
> **Obtaining attributes**
> : [component](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6y3pnvyg63tfnz2a)
> : [contextID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6y3pnz2gk6dujfca)
> : [elementID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6zlmmvwwk3tujfca)
> : [hasSession](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c62dbonjwk43tnfxw4)
> : [isInForm](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c62ltjfxem33snu)
> : [page](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64dbm5sq)
> : [request](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64tfof2wk43u)
> : [response](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64tfonyg63ttmu)
> : [session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c643fonzws33o)
> : [session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c643fonzws33o)
> : [setInForm](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c643forew4rtpojwq)
>
> **Manipulating element
> ID**
> : [appendElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6ylqobsw4zcfnrsw2zlooreuiq3pnvyg63tfnz2a)
> : [appendZeroElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6ylqobsw4zc2mvzg6rlmmvwwk3tujfceg33nobxw4zlooq)
> : [deleteAllElementIDComponents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6zdfnrsxizkbnrwek3dfnvsw45cjirbw63lqn5xgk3tuom)
> : [deleteLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6zdfnrsxizkmmfzxirlmmvwwk3tujfceg33nobxw4zlooq)
> : [incrementLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c62lomnzgk3lfnz2eyyltorcwyzlnmvxhiskeinxw24dpnzsw45a)
>
> **Generating URLs**
> : [directActionURLForActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6zdjojswg5cbmn2gs33okvjeyrtpojawg5djn5xe4ylnmvsa)
> : [completeURLWithRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6y3pnvygyzlumvkvetcxnf2gqutfof2wk43ujbqw4zdmmvzewzlz)
> : [componentActionURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6y3pnvyg63tfnz2ecy3unfxw4vksjq)
> : [urlWithRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c65lsnrlws5dikjsxc5lfon2eqylomrwgk4slmv4q)

## Constructors

---

### WOContext

`public WOContext()`

Returns a WOContext instance initialized with
a unique context ID.

`public WOContext(WORequest aRequest)`

Returns a WOContext instance initialized with _aRequest_.

---

## Static Methods

---

### contextWithRequest

`public static WOContext contextWithRequest(WORequest aRequest)`

Creates and returns a WOContext with _aRequest_.
This is the preferred way to create a WOContext. All other constructors
call this one, so if you subclass WOContext, you need to override
only this one.

---

## Instance Methods

---

### appendElementIDComponent

`public void appendElementIDComponent(String aString)`

Appends a string to the current element ID to
create an identifier of an HTML element. For example, if the current
element ID is "0.1.1" and you send this message with an
argument of "NameField," the element ID for that field
becomes "0.1.1.NameField".

__See Also:__  [deleteAllElementIDComponents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6zdfnrsxizkbnrwek3dfnvsw45cjirbw63lqn5xgk3tuom), [deleteLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6zdfnrsxizkmmfzxirlmmvwwk3tujfceg33nobxw4zlooq), [incrementLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c62lomnzgk3lfnz2eyyltorcwyzlnmvxhiskeinxw24dpnzsw45a)

---

### appendZeroElementIDComponent

`public void appendZeroElementIDComponent()`

Appends a ".0" to the current element
ID to create an identifier of the first "child" HTML element.
For example, if the current element ID is "0.1.1", after
you send this message the element ID becomes "0.1.1.0".

__See
Also:__  [deleteAllElementIDComponents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6zdfnrsxizkbnrwek3dfnvsw45cjirbw63lqn5xgk3tuom), [deleteLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6zdfnrsxizkmmfzxirlmmvwwk3tujfceg33nobxw4zlooq), [incrementLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c62lomnzgk3lfnz2eyyltorcwyzlnmvxhiskeinxw24dpnzsw45a)

---

### completeURLWithRequestHandlerKey

`public String completeURLWithRequestHandlerKey(
String requestHandlerKey,
String aRequestHandlerPath,
String aQueryString,
boolean isSecure,
int somePort)`

Returns the complete URL for the specified request
handler. The _requestHandlerKey_ is
one of the keys provided by WOApplication. The _requestHandlerPath_ is
any URL encoded string. The _queryString_ is added
at the end of the URL behind a "?". If _isSecure_ is true,
this method uses "https" instead of "http." If _somePort_ is
0 (zero), this method uses the default port.

__See
Also:__  [urlWithRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c65lsnrlws5dikjsxc5lfon2eqylomrwgk4slmv4q)

---

### component

`public WOComponent component()`

Returns the component that dynamic elements
are currently using to push and pull values associatively. This
component could represent the current request or response page or
a subcomponent of that page.

__See Also:__  [WOComponent](WOComponent.md#apple-k5hug33nobxw4zlooq) class, [page](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64dbm5sq), [request](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64tfof2wk43u), [response](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64tfonyg63ttmu), [session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c643fonzws33o)

---

### componentActionURL

`public String componentActionURL()`

Returns the complete URL for the component action.

---

### contextID

`public String contextID()`

Returns the context ID of the receiver.

---

### deleteAllElementIDComponents

`public void deleteAllElementIDComponents()`

Deletes all components of the current element
ID.

__See Also:__  [appendElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6ylqobsw4zcfnrsw2zlooreuiq3pnvyg63tfnz2a), [appendZeroElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6ylqobsw4zc2mvzg6rlmmvwwk3tujfceg33nobxw4zlooq), [incrementLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c62lomnzgk3lfnz2eyyltorcwyzlnmvxhiskeinxw24dpnzsw45a)

---

### deleteLastElementIDComponent

`public void deleteLastElementIDComponent()`

Deletes the last digit (or name) of the current
element ID, along with its dot separator. Thus, after sending this
message, "0.0.1.1" becomes "0.0.1".

__See
Also:__  [appendElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6ylqobsw4zcfnrsw2zlooreuiq3pnvyg63tfnz2a), [appendZeroElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6ylqobsw4zc2mvzg6rlmmvwwk3tujfceg33nobxw4zlooq), [incrementLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c62lomnzgk3lfnz2eyyltorcwyzlnmvxhiskeinxw24dpnzsw45a)

---

### directActionURLForActionNamed

`public String directActionURLForActionNamed(
String anActionName,
NSDictionary aQueryDict)`

Returns the complete URL for the specified action.
You can specify _aQueryDict_, and _anActionName_ can be "ActionClass/ActionName"
or "ActionName".

__See Also:__  [WODirectAction](WODirectAction.md#apple-k5hui2lsmvrxiqldoruw63q) class specification

---

### elementID

`public String elementID()`

Returns the element ID identifying the current [WOElement](WOElement.md#apple-k5huk3dfnvsw45a).This method helps you avoid
creating a session in direct actions.

---

### hasSession

`public boolean hasSession()`

Returns whether a session exists for the receiving
context.

__See Also:__  [session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c643fonzws33o)

---

### incrementLastElementIDComponent

`public void incrementLastElementIDComponent()`

Increments the last digit of the current element
ID. For example, after this message is sent, "0.0.1.2" becomes
"0.0.1.3".

__See Also:__  [appendElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6ylqobsw4zcfnrsw2zlooreuiq3pnvyg63tfnz2a), [appendZeroElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6ylqobsw4zc2mvzg6rlmmvwwk3tujfceg33nobxw4zlooq), [deleteAllElementIDComponents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6zdfnrsxizkbnrwek3dfnvsw45cjirbw63lqn5xgk3tuom), [deleteLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6zdfnrsxizkmmfzxirlmmvwwk3tujfceg33nobxw4zlooq)

---

### isInForm

`public boolean isInForm()`

Returns true when in the context of a WOForm.

__See
Also:__  [setInForm](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c643forew4rtpojwq)

---

### page

`public WOComponent page()`

Returns the [WOComponent](WOComponent.md#apple-k5hug33nobxw4zlooq) object that represents
the request or response page.

__See Also:__  [component](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6y3pnvyg63tfnz2a), [request](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64tfof2wk43u), [response](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64tfonyg63ttmu), [session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c643fonzws33o)

---

### request

`public WORequest request()`

Returns the transaction's [WORequest](WORequest.md#apple-k5hvezlrovsxg5a) object.

__See
Also:__  [component](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6y3pnvyg63tfnz2a), [page](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64dbm5sq), [response](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64tfonyg63ttmu), [session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c643fonzws33o)

---

### response

`public WOResponse response()`

Returns the transaction's [WOResponse](WOResponse.md#apple-k5hvezltobxw443f) object.

__See
Also:__  [component](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6y3pnvyg63tfnz2a), [page](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64dbm5sq), [response](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64tfonyg63ttmu), [session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c643fonzws33o)

---

### senderID

`public String senderID()`

Returns the part of the WORequest's URI that
identifies the dynamic element on the page (such as a form or an
active image) responsible for submitting the request. The sender
ID is the same as the element ID used to identify the dynamic element.
A request's sender ID may be null, as it always is on the first
request of a session.

__See Also:__  [request](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64tfof2wk43u) , [uri](WORequest.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c65lsne) (WORequest)

---

### session

`public WOSession session()`

Returns the object representing the receiving
context's session, if one exists. If the receiver does not have a
session, this method creates a new session object and returns it.
Note that not all contexts have a session: Direct Actions, for instance,
don't always need a session. Use [hasSession](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c62dbonjwk43tnfxw4) to determine whether a
context has a session associated with it.

__See
Also:__  [component](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6y3pnvyg63tfnz2a), [page](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64dbm5sq), [request](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64tfof2wk43u), [response](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c64tfonyg63ttmu), [WOSession](WOSession.md#apple-k5hvgzltonuw63q) class

---

### setInForm

`public void setInForm(boolean flag)`

If you write something that behaves like a WOForm,
set this to notify WODynamicElements that they are in a form.

__See
Also:__  [isInForm](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c62ltjfxem33snu)

---

### urlWithRequestHandlerKey

`public String urlWithRequestHandlerKey(
String requestHandlerKey,
String aRequestHandlerPath,
String aQueryString)`

Returns a URL relative to cgi-bin/WebObjects
for the specified request handler. The _requestHandlerKey_ is
one of the keys provided by WOApplication. The _requestHandlerPath_ is
any URL encoded string. The _queryString_ is
added at the end of the URL behind a "?".

__See
Also:__  [completeURLWithRequestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw45dfpb2c6y3pnvygyzlumvkvetcxnf2gqutfof2wk43ujbqw4zdmmvzewzlz)

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
