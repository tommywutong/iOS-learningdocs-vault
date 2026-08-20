---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WOComponent.html
archived_at: '2026-07-15T08:11:47.420205Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOComponent

> __Inherits
> from:__  [WOElement](WOElement-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2xj5cwyzlnmvxhi) : NSObject

> __Conforms to:__  [WOActionResults](WOActionResults-2.md#apple-ijaucscbijces) NSObject
> (NSObject)

> __Declared in:__  WebObjects/WOComponent.h

---

## Class Description

---

WOComponent objects dynamically render web pages (or sections
of pages) at run time. They provide custom navigation and other
logic for the page, provide a framework for organizing constituent
objects (static and dynamic HTML elements and subcomponents), and
enable the attribute bindings of dynamic elements.

The WOComponent class has many methods that have the same
names as methods of the [WOApplication](WOApplication-2.md#apple-k5huc4dqnruwgylunfxw4) class. However, the
scope of the WOComponent methods is limited to a component rather
than being application-wide. For example, you can control component-definition
caching on a per-component basis using [setCachingEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tmv2egyldnbuw4z2fnzqwe3dfmq5a),
which has a WOApplication counterpart. When this kind of caching
is enabled for a component, the application parses the contents
of the component directory the first time the component is requested,
creates the component definition, stores this object in memory,
and restores it for subsequent requests.

WOComponent objects also respond to [awake](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3bo5qwwzi), [sleep](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tnrswk4a), and the three request-handling
messages: [takeValuesFromRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3umfvwkvtbnr2wk42gojxw2utfof2wk43uhjuw4q3pnz2gk6duhi), [invokeActionForRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3jnz3g623fifrxi2lpnzdg64ssmvyxkzltoq5gs3sdn5xhizlyoq5a),and [appendToResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3bobygk3tekrxvezltobxw443fhjuw4q3pnz2gk6duhi). You
can override these methods in your compiled subclasses, and thereby
integrate your custom behavior into the request-response loop. (You
can also override these methods in component scripts using WebScript.)

## Subcomponents

A WOComponent object can represent a dynamic fragment of a
Web page as well as an entire page. Such _subcomponents_,
or _reusable components_, are nested
within a parent component representing the page _or_ another
subcomponent. Each component keeps track of its parent and subcomponents-when a
component receives a request-handling message, such as [takeValuesFromRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3umfvwkvtbnr2wk42gojxw2utfof2wk43uhjuw4q3pnz2gk6duhi),
it forwards that message to its subcomponents

The WOComponent class also provides a child-parent callback
mechanism to allow a child component to communicate with its parent.
In the parent's declaration file, bind an arbitrary attribute
of the child to an action method of the parent. Then, as the last
step in the child's action method, invoke [performParentAction:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3qmvzgm33snvigc4tfnz2ecy3unfxw4oq) with
the argument being the arbitrary attribute, returning the object
received back as the response page. See the method description for [performParentAction:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3qmvzgm33snvigc4tfnz2ecy3unfxw4oq) for
details.

## Stateless Components

For extra efficiency, you can create __stateless__ components:
components that can be shared between sessions. Stateless components
aren't replicated each time they're needed; rather, a single
shared instance is referenced each time the component is used.

Stateless components cannot have state. They can have instance
variables, but the variable's content must be transient. To ensure
that when the shared instance of a component is reused by another
session there are no side effects, reset your component's instance
variables by implementing the [reset](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3smvzwk5a) method. In
your implementation of __reset__ , release
and set to nil each instance variable. Note that a stateless component's
instance variables will remain valid for the duration of the phase (takeValuesFromRequest,
invokeAction and appendToResponse); this lets you use instance variables in
your stateless components to hold things analgous to items in a
WORepetition.

Stateless components primarily save memory, but they can significantly
speed up your application as well depending on how many stateless
components you use in your application. To make a component stateless,
override the component's [isStateless](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3jonjxiylumvwgk43t) method
so that it returns YES.

If a stateless component is needed simultaneously in separate
threads, additional instances of the component are created (and
later discarded) as necessary to prevent conflicts. Thus, the number
of threads in which a component could be used determines the maximum
number of instances of a stateless component that may be allocated
at any given time.

## Adopted Protocols

---

> [WOActionResults](WOActionResults-2.md#apple-ijaucscbijces): [generateResponse](WOActionResults-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxvot2bmn2gs33okjsxg5lmorzs6z3fnzsxeylumvjgk43qn5xhgzi)
> NSCoding: - encodeWithCoder:
> : - initWithCoder:
> NSCopying: - copy
> : - copyWithZone:

## Method Types

---

> **Creation**
> : [- init](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3jnzuxi)
>
> **Obtaining attributes**
> : [- application](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3bobygy2ldmf2gs33o)
> : [- baseURL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3cmfzwkvksjq)
> : [- context](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3dn5xhizlyoq)
> : [- frameworkName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3gojqw2zlxn5zgwttbnvsq)
> : [- hasSession](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3imfzvgzltonuw63q)
> : [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3omfwwk)
> : [- pageWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3qmftwkv3jorue4ylnmu5a)
> : [- path](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3qmf2gq)
> : [- session](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tmvzxg2lpny)
>
> **Caching**
> : [- isCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3jonbwcy3infxgorlomfrgyzle)
> : [- setCachingEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tmv2egyldnbuw4z2fnzqwe3dfmq5a)
>
> **Handling requests**
> : [- appendToResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3bobygk3tekrxvezltobxw443fhjuw4q3pnz2gk6duhi)
> : [- awake](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3bo5qwwzi)
> : [- ensureAwakeInContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3fnzzxk4tfif3wc23fjfxeg33oorsxq5b2)
> : [- invokeActionForRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3jnz3g623fifrxi2lpnzdg64ssmvyxkzltoq5gs3sdn5xhizlyoq5a)
> : [- sleep](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tnrswk4a)
> : [- takeValuesFromRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3umfvwkvtbnr2wk42gojxw2utfof2wk43uhjuw4q3pnz2gk6duhi)
>
> **Logging**
> : [- debugWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3emvrhkz2xnf2gqrtpojwwc5b2)
> : [- isEventLoggingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3joncxmzloorgg6z3hnfxgorlomfrgyzle)
> : [- logWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3mn5tvo2lunbdg64tnmf2du)
> : [- logWithFormat:arguments:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3mn5tvo2lunbdg64tnmf2duylsm52w2zloorztu)
>
> **Template parsing**
> : [+ templateWithHTMLString:declarationString:languages:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33nobxw4zlooqxxizlnobwgc5dfk5uxi2cikrguyu3uojuw4zz2mrswg3dbojqxi2lpnzjxi4tjnzttu3dbnztxkylhmvztu)
>
> **Component statistics**
> : [- descriptionForResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3emvzwg4tjob2gs33oizxxeutfonyg63ttmu5gs3sdn5xhizlyoq5a)
>
> **Invoking actions**
> : [- parent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3qmfzgk3tu)
> : [- performParentAction:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3qmvzgm33snvigc4tfnz2ecy3unfxw4oq)
>
> **Synchronizing components**
> : [- canGetValueForBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3dmfxeozlukzqwy5lfizxxeqtjnzsgs3thhi)
> : [- canSetValueForBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3dmfxfgzlukzqwy5lfizxxeqtjnzsgs3thhi)
> : [- hasBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3imfzue2lomruw4zz2)
> : [- setValue:forBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tmv2fmylmovstuztpojbgs3tenfxgooq)
> : [- synchronizesVariablesWithBindings](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tpfxgg2dsn5xgs6tfonlgc4tjmfrgyzltk5uxi2ccnfxgi2lom5zq)
> : [- valueForBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3wmfwhkzkgn5zee2lomruw4zz2)
>
> **Other**
> : [- isStateless](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3jonjxiylumvwgk43t)
> : [- reset](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3smvzwk5a)
> : [- templateWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3umvwxa3dborsvo2lunbhgc3lfhi)

## Class Methods

---

### templateWithHTMLString:declarationString:languages:

`+ (WOElement *)templateWithHTMLString:(NSString
*)anHTMLString
declarationString:(NSString *)aDeclarationString
languages:(NSArray*)languages`

Programmatically creates the component's template
using _anHTMLString_ as the HTML template contents
and _aDeclarationString_ as the declarations
file contents. Returns (as a WOElement object) the graph of static
and dynamic elements build by parsing the HTML and declaration strings.
You can then use the returned WOElement as the component's template.

__See
Also:__  [- templateWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3umvwxa3dborsvo2lunbhgc3lfhi)

---

## Instance Methods

---

### appendToResponse:inContext:

`- (void)appendToResponse:(WOResponse
*)aResponse
inContext:(WOContext *)aContext`

Component objects associated with a response
receive this message during the last phase of the request-response
loop. In the append-to-response phase, the application objects (particularly
the response page instance itself) generate the HTML content of
the page. WOComponent's default implementation of this method
forwards the message to the root [WOElement](WOElement-2.md#apple-k5huk3dfnvsw45a) object of the component template.
Compiled or scripted subclasses of WOComponent can override this
method to replace or supplement the default behavior with custom
logic.

__See Also:__  [- invokeActionForRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3jnz3g623fifrxi2lpnzdg64ssmvyxkzltoq5gs3sdn5xhizlyoq5a), [- takeValuesFromRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3umfvwkvtbnr2wk42gojxw2utfof2wk43uhjuw4q3pnz2gk6duhi)

---

### application

`- (WOApplication *)application`

Returns the WOApplication object for the current
application.

__See Also:__  [WOApplication](WOApplication-2.md#apple-k5huc4dqnruwgylunfxw4) class, [- context](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3dn5xhizlyoq), [- session](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tmvzxg2lpny)

---

### awake

`- (void)awake`

Invoked at the beginning of a WOComponent's
involvement in a cycle of the request-response loop, giving the
WOComponent an opportunity to initialize its instance variables
or perform setup operations. The default implementation does nothing.

__See
Also:__  [- ensureAwakeInContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3fnzzxk4tfif3wc23fjfxeg33oorsxq5b2), [- init](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3jnzuxi), [- sleep](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tnrswk4a)

---

### baseURL

`- (NSString *)baseURL`

Returns the component URL relative to the server's
document root, for example: "/WebObjects/MyApp.woa/Resources/Main.wo"

__See
Also:__  [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3omfwwk), [- path](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3qmf2gq)

---

### canGetValueForBinding:

`- (BOOL)canGetValueForBinding:(NSString
*)aBindingName`

Verifies that the binding exists and that [valueForBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3wmfwhkzkgn5zee2lomruw4zz2) will
return a value.

__See Also:__  [- canSetValueForBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3dmfxfgzlukzqwy5lfizxxeqtjnzsgs3thhi), [- hasBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3imfzue2lomruw4zz2), [- valueForBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3wmfwhkzkgn5zee2lomruw4zz2)

---

### canSetValueForBinding:

`- (BOOL)canSetValueForBinding:(NSString
*)aBindingName`

Verifies that the binding exists and that [setValue:forBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tmv2fmylmovstuztpojbgs3tenfxgooq) will succeed.

__See
Also:__  [- canGetValueForBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3dmfxeozlukzqwy5lfizxxeqtjnzsgs3thhi), [- hasBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3imfzue2lomruw4zz2), [- setValue:forBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tmv2fmylmovstuztpojbgs3tenfxgooq)

---

### context

`- (WOContext *)context`

Returns the WOContext object for the current
transaction.

__See Also:__  [WOContext](WOContext-2.md#apple-k5hug33oorsxq5a) class, [- application](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3bobygy2ldmf2gs33o), [- session](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tmvzxg2lpny)

---

### debugWithFormat:

`- (void)debugWithFormat:(NSString
*)aFormatString,...`

Like [logWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3mn5tvo2lunbdg64tnmf2du), prints a message
to the standard error device (stderr), but only prints the message if
the WODebuggingEnabled user default option is YES. If WODebuggingEnabled
is NO, the [debugWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3emvrhkz2xnf2gqrtpojwwc5b2) messages
aren't printed. See [logWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3mn5tvo2lunbdg64tnmf2du) for information on
the format of _aFormatString_.

__See
Also:__  [- logWithFormat:arguments:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3mn5tvo2lunbdg64tnmf2duylsm52w2zloorztu)

---

### descriptionForResponse:inContext:

`- (NSString *)descriptionForResponse:(WOResponse
*)aResponse
inContext:(WOContext *)aContext`

Records information about the component if it
is the response component in the current request-response loop transaction.
The default implementation records the component's name. You might
override this method if you want to record more information about
the component. For example, you might want to record the values
of some instance variables as well as the component name.

This
message is sent only to the top-level response component, that is,
the one representing the entire page. Components nested inside of
that top-level component do not receive this message.

If
a CLFF log file is kept for this application, the string returned
by this method is recorded in that log file. Thus, you must ensure
that the string you return can be analyzed by a CLFF-analysis tool.

__See
Also:__  [WOStatisticsStore](WOStatisticsStore-2.md#apple-k5hvg5dboruxg5djmnzvg5dpojsq) class

---

### ensureAwakeInContext:

`- (void)ensureAwakeInContext:(WOContext
*)aContext`

Ensures that the receiver is awake in
the specified context. Invoke this method before using a component
which was stored in a variable. You don't need to invoke [ensureAwakeInContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3fnzzxk4tfif3wc23fjfxeg33oorsxq5b2) if the component
was just created with [pageWithName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3qmftwkv3jorue4ylnmu5a),
if it was restored from the WebObjects page cache, or if the page
will simply be returned as the result of an action. That is, you
only need to invoke this method if you're going to send messages
to a component that is otherwise not awakened. If the receiving
component is already awake, this method has no effect.

__See
Also:__  [- awake](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3bo5qwwzi)

---

### frameworkName

`- (NSString *)frameworkName`

If the component is stored in a framework, this
method returns the name of that framework. For example, if the component
is in the framework _NeXT_ROOT___/System/Library/Frameworks/WOExtensions.framework__,
then this method returns the string "WOExtensions".

If
the component is not stored in a framework, this method returns nil.

__See
Also:__  [WOResourceManager](WOResourceManager-2.md#apple-k5hvezltn52xey3fjvqw4ylhmvza) class

---

### generateResponse

`- (WOResponse *)generateResponse`

Returns a newly-created WOResponse object. WOComponent's
implementation of this method translates the receiving component
into a WOResponse object by sending iteself an [appendToResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3bobygk3tekrxvezltobxw443fhjuw4q3pnz2gk6duhi) message.

__See
Also:__  [- generateResponse](WOResponse-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzxa33oonss6z3fnzsxeylumvjgk43qn5xhgzi) (WOResponse)

---

### hasBinding:

`- (BOOL)hasBinding:(NSString
*)aBindingName`

Returns whether the component has a binding
named _aBindingName_. This method traverses
the chain of associations to the top-level parent, if necessary.

__See
Also:__  [- canGetValueForBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3dmfxeozlukzqwy5lfizxxeqtjnzsgs3thhi), [- canSetValueForBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3dmfxfgzlukzqwy5lfizxxeqtjnzsgs3thhi)

---

### hasSession

`- (BOOL)hasSession`

Returns whether the component is already in
a session. For example, in direct actions, sessions are lazily created
and you can avoid creating another one unnecessarily by calling [hasSession](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3imfzvgzltonuw63q) before [session](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tmvzxg2lpny).

__See
Also:__  [- session](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tmvzxg2lpny)

---

### init

`- (id)init`

Initializes a WOComponent object. If a WebObjects
Builder archive file exists in the component directory, it initializes
component variables from this archive. An exception is thrown if
the method cannot determine the name of the component or if it cannot
initialize the object for any other reason. Override [init](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3jnzuxi) in compiled subclasses to perform
custom initializations; as always, invoke __super__'s __init__ method
as the first thing.

__See Also:__  [- awake](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3bo5qwwzi)

---

### invokeActionForRequest:inContext:

`- (WOElement *)invokeActionForRequest:(WORequest
*)aRequest
inContext:(WOContext *)aContext`

WOComponent objects associated with a request
page receive this message during the middle phase of request handling.
In this middle phase, the [invokeActionForRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3jnz3g623fifrxi2lpnzdg64ssmvyxkzltoq5gs3sdn5xhizlyoq5a) message
is propagated through the [WOElement](WOElement-2.md#apple-k5huk3dfnvsw45a) objects of the page; the
dynamic element on which the user has acted (by, for example, clicking
a button) responds by triggering the method in the request component that
is bound to the action. WOComponent's default implementation of
this method forwards the message to the root WOElement object of
the component template.Compiled or scripted subclasses of WOComponent
can override this method to replace or supplement the default behavior
with custom logic.

__See Also:__  [- appendToResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3bobygk3tekrxvezltobxw443fhjuw4q3pnz2gk6duhi), [- takeValuesFromRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3umfvwkvtbnr2wk42gojxw2utfof2wk43uhjuw4q3pnz2gk6duhi)

---

### isCachingEnabled

`- (BOOL)isCachingEnabled`

Returns whether component-definition caching
is enabled for this component. NO is the default.

__See
Also:__  [- setCachingEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tmv2egyldnbuw4z2fnzqwe3dfmq5a)

---

### isEventLoggingEnabled

`- (BOOL)isEventLoggingEnabled`

Called to determine if a component wants
event logging. This is not desirable, for example, for components
which are associated with event display as they would interfere
with the actual event logging. The default implementation of this
method returns YES.

__See Also:__  [WOEvent](WOEvent-2.md#apple-k5hug33pnnuwk) class

---

### isStateless

`- (BOOL)isStateless`

By default, this method returns NO, indicating
that state will be maintained for instances of the receiver. Overriding
this method to return YES will make the component stateless. A single
instance of each stateless component is shared between multiple
sessions, reducing your application's memory footprint.

__See
Also:__  [- reset](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3smvzwk5a)

---

### logWithFormat:

`- (void)logWithFormat:(NSString
*)aFormat,...`

Prints a message to the standard error device
(stderr). The message can include formatted variable data using __printf__-style
conversion specifiers, for example:
> ```
> id i = 500;
> id f = 2.045;
> [self logWithFormat:@"Amount = %@, Rate = %@, Total = %@",
> i, f, i*f];
> ```

Note
that in WebScript, all variables are objects, so the only conversion
specifier allowed is %@ as shown above. In compiled Objective-C
code, all __printf__ conversion specifiers
are allowed. The equivalent method in Java is __logString__.

---

### logWithFormat:arguments:

`- (void)logWithFormat:(NSString
*)aFormat
arguments:(va_list)someArguments`

Prints a message to the standard error device
(stderr). This method is used by [logWithFormat:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3mn5tvo2lunbdg64tnmf2du).

---

### name

`- (NSString *)name`

Returns the name of the component minus the
".wo" extension; for example "Main" is a typical component
name.

__See Also:__  [- baseURL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3cmfzwkvksjq), [- path](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3qmf2gq)

---

### pageWithName:

`- (WOComponent *)pageWithName:(NSString
*)aName`

Returns a new page instance (a WOComponent object)
identified by _aName_. If _aName_ is nil,
the "Main" component is assumed. If the method cannot create
a valid page instance, it raises an exception.

__See
Also:__  [- restorePageForContextID:](WOSession-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnyxxezltorxxezkqmftwkrtpojbw63tumv4hiskehi) (WOSession), [- savePage:](WOSession-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2tmvzxg2lpnyxxgylwmvigcz3fhi) (WOSession)

---

### parent

`- (WOComponent *)parent`

Returns the parent component of the receiver.

---

### path

`- (NSString *)path`

Returns the file-system path of the component,
which is an absolute path and includes the ".wo" extension;
for example "C:\Apple\Library\WOApps\MyApp.woa\Resources\Main.wo"
is a typical path.

__See Also:__  [- baseURL](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3cmfzwkvksjq), [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3omfwwk)

---

### performParentAction:

`- (id)performParentAction:(NSString
*)anActionName`

Allows a subcomponent to invoke an action method
of its parent component bound to the child component (_attribute_).
Parent and child components are "synchronized" when this method
returns: the variables that are bound by a declaration of the child
component in the parent component's declaration file have the
same value.

An example best illustrates this mechanism. Let's
say you have a Palette subcomponent, and this WOComponent is nested
in a parent component with a "displaySelection" action method.
When the user selects an item in the palette (perhaps a color),
you want to invoke "displaySelection" to show the result of
the new selection (perhaps a car in the new color). The declaration
in the parent's ".wod" file would look like this:

> ```
> PALETTE: Palette {
>    selection = number;
>    callBack = "displaySelection";
> };
> ```

The "callBack"
item is an arbitrary attribute of the child component bound in this
declaration to the parent component's "displaySelection" method.The __performParentAction:__ method
is used to activate this binding. Let's assume the child component
has an action method called "click"; the implementation would
look like this:

> ```
> - click {             /* this is the child's action */
>     selection = /* some value */;
>     /* now invoke the parent's action */
>     return [self performParentAction:callBack];
> }
> ```

---

### reset

`- (void)reset`

This method-which is only invoked if
the component is stateless-allows a component instance to reset
or delete temporary references to objects that are specific to a
given context. To ensure that when the shared instance of a component
is reused by another session there are no side effects, implement this
method so that it releases and sets to nil each of the component's
instance variables.

__See Also:__  [- isStateless](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3jonjxiylumvwgk43t)

---

### session

`- (WOSession *)session`

Returns the current WOSession object. This method
creates a new one if there isn't one.

__See
Also:__  [WOSession](WOSession-2.md#apple-k5hvgzltonuw63q) class, [- application](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3bobygy2ldmf2gs33o), [- context](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3dn5xhizlyoq), [- hasSession](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3imfzvgzltonuw63q)

---

### setCachingEnabled:

`- (void)setCachingEnabled:(BOOL)flag`

Enables or disables the caching of component
definitions for the receiving component. WOComponent definitions
contain templates and other common information related to components,
and are used to generate instances of those components.When this
attribute is set to YES, the application parses the HTML template
and the declaration (".wod") file of a component once and then
stores the resulting component definition for future requests. By
default, this kind of caching is disabled so that you can edit a _scripted_ component
without having to relaunch the application every time to check the results.(Note
that this does not apply to Java subclasses of WOComponent; in this
case, you still have to kill and relaunch the application.)

With [WOApplication](WOApplication-2.md#apple-k5huc4dqnruwgylunfxw4)'s method of the same
name, you can turn component-definition caching off globally. You
can then control caching of individual component definitions using
WOComponent's version of this method. Selective caching is an
especially valuable technique for very large applications where
only the most frequently requested components should be cached.

__See
Also:__  [- isCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3jonbwcy3infxgorlomfrgyzle)

---

### setValue:forBinding:

`- (void)setValue:(id)aValue
forBinding:(NSString *)aBindingName`

Sets the value of the binding specified by _aBindingName_ in
the parent component to _aValue_.
If the binding isn't settable, this method raises an NSGenericException.

__See
Also:__  [- isValueSettableInComponent:](WOAssociation-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bonzw6y3jmf2gs33of5uxgvtbnr2wku3for2gcytmmvew4q3pnvyg63tfnz2du) ( [WOAssociation](WOAssociation-2.md#apple-k5huc43tn5rwsylunfxw4) class)

---

### sleep

`- (void)sleep`

Invoked at the conclusion of a request-handling
cycle to give component the opportunity for deallocating objects
created and initialized in its [awake](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3bo5qwwzi) method. The default implementation
does nothing.

---

### synchronizesVariablesWithBindings

`- (BOOL)synchronizesVariablesWithBindings`

Returns whether a nested component pulls all
values down from its parent and pushes all values to its parent
before and after each phase of the request-response loop. By default,
this method returns YES. Override this method to create a non-synchronizing
component.

__See Also:__  [- setValue:forBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tmv2fmylmovstuztpojbgs3tenfxgooq), [- valueForBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3wmfwhkzkgn5zee2lomruw4zz2)

---

### takeValuesFromRequest:inContext:

`- (void)takeValuesFromRequest:(WORequest
*)aRequest
inContext:(WOContext *)aContext`

WOComponent objects associated with a request
receive this message during the first phase of the request-response
loop. The default WOComponent behavior is to send the message to
the root object of the component's template.In this phase, each
dynamic element in the template extracts any entered data or changed
state (such as a check in a check box) associated with an attribute
and assigns the value to the component variable bound to the attribute.Compiled
or scripted subclasses of Component can override this method to
replace or supplement the default behavior with custom logic.

__See
Also:__  [- appendToResponse:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3bobygk3tekrxvezltobxw443fhjuw4q3pnz2gk6duhi), [- invokeActionForRequest:inContext:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3jnz3g623fifrxi2lpnzdg64ssmvyxkzltoq5gs3sdn5xhizlyoq5a)

---

### templateWithName:

`- (WOElement *)templateWithName:(NSString
*)aName`

Returns the root object of the graph of static
and dynamic HTML elements and subcomponents that is used to graphically
render the component identified by _aName_.
This template is constructed from the ".html" and ".wod"
file found in the component directory. You identify the template
by specifying the component name: for example, "HelloWorld."
If the template is not cached, the application will parse the HTML
and declaration files of the specified component to create the template.

__See
Also:__  [- setCachingEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tmv2egyldnbuw4z2fnzqwe3dfmq5a)

---

### validationFailedWithException:value:keyPath:

`- (void)validationFailedWithException:(NSException
*)exception
value:(id)value
keyPath:(NSString *)keyPath`

Called when an Enterprise Object or formatter
failed validation during an assignment. The default implementation
ignores the error. Subclassers can override to record the error
and possibly return a different page for the current action.

---

### valueForBinding:

`- (id)valueForBinding:(NSString
*)aBindingName`

Gets the value for the specified binding from
the parent component. If the parent doesn't provide _aBindingName_ in
its delcarations file, this method attempts to get the value from
the current component using __valueForKey:__.If
the current component doesn't define this key, this method returns nil.
This cascading lookup makes it easy to provide default values for
optional bindings.

__See Also:__  [- canGetValueForBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3dmfxeozlukzqwy5lfizxxeqtjnzsgs3thhi), [- setValue:forBinding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tmv2fmylmovstuztpojbgs3tenfxgooq), [- synchronizesVariablesWithBindings](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3tpfxgg2dsn5xgs6tfonlgc4tjmfrgyzltk5uxi2ccnfxgi2lom5zq)

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
