---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WOContext.html
archived_at: '2026-07-15T08:11:47.449208Z'
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

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  WebObjects/WOContext.h

---

## Class Description

---

A WOContext object lets you access objects and information
that define the _context_ of a transaction.
In a typical request-response loop (a transaction), several objects
have a hand in what is going on: the [WOApplication](WOApplication-2.md#apple-k5huc4dqnruwgylunfxw4) and [WOSession](WOSession-2.md#apple-k5hvgzltonuw63q) objects, the page involved
in the request or response (a [WOComponent](WOComponent-2.md#apple-k5hug33nobxw4zlooq) object), the page's subcomponents
(also WOComponents), plus the dynamic elements on the page. The
WOContext object passed as an argument in the [takeValuesFromRequest:inContext:](WOComponent-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3umfvwkvtbnr2wk42gojxw2utfof2wk43uhjuw4q3pnz2gk6duhi), [invokeActionForRequest:inContext:](WOComponent-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3jnz3g623fifrxi2lpnzdg64ssmvyxkzltoq5gs3sdn5xhizlyoq5a),
and [appendToResponse:inContext:](WOComponent-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3bobygk3tekrxvezltobxw443fhjuw4q3pnz2gk6duhi) messages
allows access to these objects. A context is identified by the _context
ID_, which appears in the URL after the session ID and
page name. Each context ID is an integer that the session increments
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
to the current component (accessed through WOContext's [component](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwg33nobxw4zlooq) method),
a dynamic element can exchange values associatively between itself
and the WOComponent that contains it.

## Adopted Protocols

---

> NSCopying: - copy
> : - copyWithZone:

## Method Types

---

> **Creating new object instances**
> : [+ contextWithRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33oorsxq5bpmnxw45dfpb2fo2lunbjgk4lvmvzxioq)
> : [- init](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxws3tjoq)
> : [- initWithRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxws3tjorlws5dikjsxc5lfon2du)
>
> **Obtaining attributes**
> : [- component](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwg33nobxw4zlooq)
> : [- contextID](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwg33oorsxq5cjiq)
> : [- elementID](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwk3dfnvsw45cjiq)
> : [- hasSession](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwqyltknsxg43jn5xa)
> : [- isInForm](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxws42jnzdg64tn)
> : [- page](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxaylhmu)
> : [- request](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxezlrovsxg5a)
> : [- response](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxezltobxw443f)
> : [- session](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxgzltonuw63q)
> : [- session](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxgzltonuw63q)
> : [- setInForm:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxgzlujfxem33snu5a)
>
> **Manipulating element
> ID**
> : [- appendElementIDComponent:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwc4dqmvxgirlmmvwwk3tujfceg33nobxw4zlooq5a)
> : [- appendZeroElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwc4dqmvxgiwtfojxuk3dfnvsw45cjirbw63lqn5xgk3tu)
> : [- deleteAllElementIDComponents](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwizlmmv2gkqlmnrcwyzlnmvxhiskeinxw24dpnzsw45dt)
> : [- deleteLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwizlmmv2gktdbon2ek3dfnvsw45cjirbw63lqn5xgk3tu)
> : [- incrementLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxws3tdojsw2zloorggc43uivwgk3lfnz2esrcdn5wxa33omvxhi)
>
> **Generating URLs**
> : [- directActionURLForActionNamed:queryDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwi2lsmvrxiqldoruw63svkjgem33sifrxi2lpnzhgc3lfmq5hc5lfoj4ui2ldoruw63tboj4tu)
> : [- completeURLWithRequestHandlerKey:path:queryString:isSecure:port:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwg33nobwgk5dfkvjeyv3jorufezlrovsxg5cimfxgi3dfojfwk6j2obqxi2b2of2wk4tzkn2he2lom45gs42tmvrxk4tfhjyg64tuhi)
> : [- componentActionURL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwg33nobxw4zloorawg5djn5xfkusm)
> : [- urlWithRequestHandlerKey:path:queryString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxk4tmk5uxi2csmvyxkzltoregc3tenrsxes3fpe5hayluna5hc5lfoj4vg5dsnfxgooq)

## Class Methods

---

### contextWithRequest:

`+ (WOContext *)contextWithRequest:(WORequest
*)aRequest`

Creates and returns a WOContext with _aRequest_.
This is the preferred way to create a WOContext. All other constructors
call this one, so if you subclass WOContext, you need to override
only this one.

---

## Instance Methods

---

### appendElementIDComponent:

`- (void)appendElementIDComponent:(NSString
*)aString`

Appends a string to the current element ID to
create an identifier of an HTML element. For example, if the current
element ID is "0.1.1" and you send this message with an
argument of "NameField," the element ID for that field
becomes "0.1.1.NameField".

__See Also:__  [- deleteAllElementIDComponents](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwizlmmv2gkqlmnrcwyzlnmvxhiskeinxw24dpnzsw45dt), [- deleteLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwizlmmv2gktdbon2ek3dfnvsw45cjirbw63lqn5xgk3tu), [- incrementLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxws3tdojsw2zloorggc43uivwgk3lfnz2esrcdn5wxa33omvxhi)

---

### appendZeroElementIDComponent

`- (void)appendZeroElementIDComponent`

Appends a ".0" to the current element
ID to create an identifier of the first "child" HTML element.
For example, if the current element ID is "0.1.1", after
you send this message the element ID becomes "0.1.1.0".

__See
Also:__  [- deleteAllElementIDComponents](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwizlmmv2gkqlmnrcwyzlnmvxhiskeinxw24dpnzsw45dt), [- deleteLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwizlmmv2gktdbon2ek3dfnvsw45cjirbw63lqn5xgk3tu), [- incrementLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxws3tdojsw2zloorggc43uivwgk3lfnz2esrcdn5wxa33omvxhi)

---

### completeURLWithRequestHandlerKey:path:queryString:isSecure:port:

`- (NSString *)completeURLWithRequestHandlerKey:(NSString
*)requestHandlerKey
path:(NSString *)aRequestHandlerPath
queryString:(NSString *)aQueryString
isSecure:(BOOL)isSecure
port:(int)somePort`

Returns the complete URL for the specified request
handler. The _requestHandlerKey_ is
one of the keys provided by WOApplication. The _requestHandlerPath_ is
any URL encoded string. The _queryString_ is added
at the end of the URL behind a "?". If _isSecure_ is YES,
this method uses "https" instead of "http." If _somePort_ is
0 (zero), this method uses the default port.

__See
Also:__  [- urlWithRequestHandlerKey:path:queryString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxk4tmk5uxi2csmvyxkzltoregc3tenrsxes3fpe5hayluna5hc5lfoj4vg5dsnfxgooq)

---

### component

`- (WOComponent *)component`

Returns the component that dynamic elements
are currently using to push and pull values associatively. This
component could represent the current request or response page or
a subcomponent of that page.

__See Also:__  [WOComponent](WOComponent-2.md#apple-k5hug33nobxw4zlooq) class, [- page](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxaylhmu), [- request](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxezlrovsxg5a), [- response](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxezltobxw443f), [- session](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxgzltonuw63q)

---

### componentActionURL

`- (NSString *)componentActionURL`

Returns the complete URL for the component action.

---

### contextID

`- (NSString *)contextID`

Returns the context ID of the receiver.

---

### deleteAllElementIDComponents

`- (void)deleteAllElementIDComponents`

Deletes all components of the current element
ID.

__See Also:__  [- appendElementIDComponent:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwc4dqmvxgirlmmvwwk3tujfceg33nobxw4zlooq5a), [- appendZeroElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwc4dqmvxgiwtfojxuk3dfnvsw45cjirbw63lqn5xgk3tu), [- incrementLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxws3tdojsw2zloorggc43uivwgk3lfnz2esrcdn5wxa33omvxhi)

---

### deleteLastElementIDComponent

`- (void)deleteLastElementIDComponent`

Deletes the last digit (or name) of the current
element ID, along with its dot separator. Thus, after sending this
message, "0.0.1.1" becomes "0.0.1".

__See
Also:__  [- appendElementIDComponent:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwc4dqmvxgirlmmvwwk3tujfceg33nobxw4zlooq5a), [- appendZeroElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwc4dqmvxgiwtfojxuk3dfnvsw45cjirbw63lqn5xgk3tu), [- incrementLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxws3tdojsw2zloorggc43uivwgk3lfnz2esrcdn5wxa33omvxhi)

---

### directActionURLForActionNamed:queryDictionary:

`- (NSString *)directActionURLForActionNamed:(NSString
*)anActionName
queryDictionary:(NSDictionary
*)aQueryDict`

Returns the complete URL for the specified action.
You can specify _aQueryDict_, and _anActionName_ can be @"ActionClass/ActionName"
or @"ActionName".

__See Also:__  [WODirectAction](WODirectAction-2.md#apple-k5hui2lsmvrxiqldoruw63q) class specification

---

### elementID

`- (NSString *)elementID`

Returns the element ID identifying the current [WOElement](WOElement-2.md#apple-k5huk3dfnvsw45a).This method helps you avoid
creating a session in direct actions.

---

### hasSession

`- (BOOL)hasSession`

Returns whether a session exists for the receiving
context.

__See Also:__  [- session](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxgzltonuw63q)

---

### incrementLastElementIDComponent

`- (void)incrementLastElementIDComponent`

Increments the last digit of the current element
ID. For example, after this message is sent, "0.0.1.2" becomes
"0.0.1.3".

__See Also:__  [- appendElementIDComponent:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwc4dqmvxgirlmmvwwk3tujfceg33nobxw4zlooq5a), [- appendZeroElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwc4dqmvxgiwtfojxuk3dfnvsw45cjirbw63lqn5xgk3tu), [- deleteAllElementIDComponents](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwizlmmv2gkqlmnrcwyzlnmvxhiskeinxw24dpnzsw45dt), [- deleteLastElementIDComponent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwizlmmv2gktdbon2ek3dfnvsw45cjirbw63lqn5xgk3tu)

---

### init

`- (id)init`

Returns a WOContext instance initialized with
a unique context ID. Generally, you should call [initWithRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxws3tjorlws5dikjsxc5lfon2du) instead
to ensure that the WOContext instance is properly initialized.

---

### initWithRequest:

`- (id)initWithRequest:(WORequest
*)aRequest`

Returns a WOContext with _aRequest_.

---

### isInForm

`- (BOOL)isInForm`

Returns YES when in the context of a WOForm.

__See
Also:__  [setInForm:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxgzlujfxem33snu5a)

---

### page

`- (WOComponent *)page`

Returns the [WOComponent](WOComponent-2.md#apple-k5hug33nobxw4zlooq) object that represents
the request or response page.

__See Also:__  [- component](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwg33nobxw4zlooq), [- request](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxezlrovsxg5a), [- response](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxezltobxw443f), [- session](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxgzltonuw63q)

---

### request

`- (WORequest *)request`

Returns the transaction's [WORequest](WORequest-2.md#apple-k5hvezlrovsxg5a) object.

__See
Also:__  [- component](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwg33nobxw4zlooq), [- page](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxaylhmu), [- response](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxezltobxw443f), [- session](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxgzltonuw63q)

---

### response

`- (WOResponse *)response`

Returns the transaction's [WOResponse](WOResponse-2.md#apple-k5hvezltobxw443f) object.

__See
Also:__  [- component](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwg33nobxw4zlooq), [- page](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxaylhmu), [- response](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxezltobxw443f), [- session](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxgzltonuw63q)

---

### senderID

`- (NSString *)senderID`

Returns the part of the WORequest's URI that
identifies the dynamic element on the page (such as a form or an
active image) responsible for submitting the request. The sender
ID is the same as the element ID used to identify the dynamic element.
A request's sender ID may be nil, as it always is on the first request
of a session.

__See Also:__  [- initWithRequest:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxws3tjorlws5dikjsxc5lfon2du), [- request](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxezlrovsxg5a) , [- uri](WORequest-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxxk4tj) (WORequest)

---

### session

`- (WOSession *)session`

Returns the object representing the receiving
context's session, if one exists. If the receiver does not have a
session, this method creates a new session object and returns it.
Note that not all contexts have a session: Direct Actions, for instance,
don't always need a session. Use [hasSession](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwqyltknsxg43jn5xa) to determine whether a
context has a session associated with it.

__See
Also:__  [- component](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwg33nobxw4zlooq), [- page](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxaylhmu), [- request](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxezlrovsxg5a), [- response](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxezltobxw443f), [WOSession](WOSession-2.md#apple-k5hvgzltonuw63q) class

---

### setInForm:

`- (void)setInForm:(BOOL)flag`

If you write something that behaves like a WOForm,
set this to notify WODynamicElements that they are in a form.

__See
Also:__  [isInForm](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxws42jnzdg64tn)

---

### urlWithRequestHandlerKey:path:queryString:

`- (NSString *)urlWithRequestHandlerKey:(NSString
*)requestHandlerKey
path:(NSString *)aRequestHandlerPath
queryString:(NSString *)aQueryString`

Returns a URL relative to cgi-bin/WebObjects
for the specified request handler. The _requestHandlerKey_ is
one of the keys provided by WOApplication. The _requestHandlerPath_ is
any URL encoded string. The _queryString_ is
added at the end of the URL behind a "?".

__See
Also:__  [- completeURLWithRequestHandlerKey:path:queryString:isSecure:port:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxwg33nobwgk5dfkvjeyv3jorufezlrovsxg5cimfxgi3dfojfwk6j2obqxi2b2of2wk4tzkn2he2lom45gs42tmvrxk4tfhjyg64tuhi)

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
