---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Classes/WOComponent.html
archived_at: '2026-07-15T08:11:46.735515Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOComponent

> __Inherits
> from:__  [WOElement](WOElement.md#apple-k5huk3dfnvsw45a) NSObject

> __Implements:__  [WOActionResults](WOActionResults.md#apple-ijaucscbijces),
> EOKeyValueCoding (com.apple.yellow.eocontrol),
> EOKeyValueCodingAdditions (com.apple.yellow.eocontrol)

> __Package:__ com.apple.yellow.webobjects

---

## Class Description

---

WOComponent objects dynamically render web pages (or sections
of pages) at run time. They provide custom navigation and other
logic for the page, provide a framework for organizing constituent
objects (static and dynamic HTML elements and subcomponents), and
enable the attribute bindings of dynamic elements.

The WOComponent class has many methods that have the same
names as methods of the [WOApplication](WOApplication.md#apple-k5huc4dqnruwgylunfxw4) class. However, the
scope of the WOComponent methods is limited to a component rather
than being application-wide. For example, you can control component-definition
caching on a per-component basis using [setCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponsxiq3bmnugs3thivxgcytmmvsa),
which has a WOApplication counterpart. When this kind of caching
is enabled for a component, the application parses the contents
of the component directory the first time the component is requested,
creates the component definition, stores this object in memory,
and restores it for subsequent requests.

WOComponent objects also respond to [awake](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmf3wc23f), [sleep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponwgkzlq), and the three request-handling
messages: [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bporqwwzkwmfwhkzltizzg63ksmvyxkzltoq), [invokeActionForRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnfxhm33lmvawg5djn5xem33skjsxc5lfon2a),and [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmfyhazlomrkg6utfonyg63ttmu). You can override
these methods in your compiled subclasses, and thereby integrate
your custom behavior into the request-response loop. (You can also
override these methods in component scripts using WebScript.)

## Subcomponents

A WOComponent object can represent a dynamic fragment of a
Web page as well as an entire page. Such _subcomponents_,
or _reusable components_, are nested
within a parent component representing the page _or_ another
subcomponent. Each component keeps track of its parent and subcomponents-when a
component receives a request-handling message, such as [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bporqwwzkwmfwhkzltizzg63ksmvyxkzltoq), it forwards
that message to its subcomponents

The WOComponent class also provides a child-parent callback
mechanism to allow a child component to communicate with its parent.
In the parent's declaration file, bind an arbitrary attribute
of the child to an action method of the parent. Then, as the last
step in the child's action method, invoke [performParentAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpobsxeztpojwvaylsmvxhiqldoruw63q) with
the argument being the arbitrary attribute, returning the object
received back as the response page. See the method description for [performParentAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpobsxeztpojwvaylsmvxhiqldoruw63q) for
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
variables by implementing the [reset](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpojsxgzlu) method. In
your implementation of __reset__ , release
and set to null each instance variable. Note that a stateless component's
instance variables will remain valid for the duration of the phase (takeValuesFromRequest,
invokeAction and appendToResponse); this lets you use instance variables in
your stateless components to hold things analgous to items in a
WORepetition.

Stateless components primarily save memory, but they can significantly
speed up your application as well depending on how many stateless
components you use in your application. To make a component stateless,
override the component's [isStateless](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnfzvg5dborswyzltom) method
so that it returns true.

If a stateless component is needed simultaneously in separate
threads, additional instances of the component are created (and
later discarded) as necessary to prevent conflicts. Thus, the number
of threads in which a component could be used determines the maximum
number of instances of a stateless component that may be allocated
at any given time.

## Interfaces Implemented

---

> [WOActionResults](WOActionResults.md#apple-ijaucscbijces): [generateResponse](WOActionResults.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6v2pifrxi2lpnzjgk43vnr2hgl3hmvxgk4tborsvezltobxw443f)
> EOKeyValueCoding: __handleQueryWithUnboundKey__
> : __handleTakeValueForUnboundKey__
> : __storedValueForKey__
> : __takeStoredValueForKey__
> : __takeValueForKey__
> : __unableToSetNullForKey__
> : __valueForKey__
> EOKeyValueCoding: __takeValueForKeyPath__
> : __takeValuesFromDictionary__
> : __valueForKeyPath__
> : __valuesForKeys__

## Method Types

---

> **Creation**
> : [WOComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpk5hug33nobxw4zlooq)
>
> **Obtaining attributes**
> : [application](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmfyha3djmnqxi2lpny)
> : [baseURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmjqxgzkvkjga)
> : [context](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmnxw45dfpb2a)
> : [frameworkName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmzzgc3lfo5xxe22omfwwk)
> : [hasSession](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnbqxgu3fonzws33o)
> : [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnzqw2zi)
> : [pageWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpobqwozkxnf2gqttbnvsq)
> : [path](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpobqxi2a)
> : [session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponsxg43jn5xa)
>
> **Caching**
> : [isCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnfzugyldnbuw4z2fnzqwe3dfmq)
> : [setCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponsxiq3bmnugs3thivxgcytmmvsa)
>
> **Handling requests**
> : [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmfyhazlomrkg6utfonyg63ttmu)
> : [awake](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmf3wc23f)
> : [ensureAwakeInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmvxhg5lsmvaxoyllmvew4q3pnz2gk6du)
> : [invokeActionForRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnfxhm33lmvawg5djn5xem33skjsxc5lfon2a)
> : [sleep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponwgkzlq)
> : [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bporqwwzkwmfwhkzltizzg63ksmvyxkzltoq)
>
> **Logging**
> : [debugString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6q3pnvyg63tfnz2c6zdfmj2wou3uojuw4zy)
> : [isEventLoggingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnfzuk5tfnz2ey33hm5uw4z2fnzqwe3dfmq)
> : [logString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6q3pnvyg63tfnz2c63dpm5jxi4tjnztq)
>
> **Template parsing**
> : [templateWithHTMLString:declarationString:languages:](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6q3pnvyg63tfnz2c65dfnvygyylumvlws5dijbke2tctorzgs3thhjsgky3mmfzgc5djn5xfg5dsnfxgootmmfxgo5lbm5sxgoq)
>
> **Component statistics**
> : [descriptionForResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmrsxgy3snfyhi2lpnzdg64ssmvzxa33oonsq)
>
> **Invoking actions**
> : [parent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpobqxezlooq)
> : [performParentAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpobsxeztpojwvaylsmvxhiqldoruw63q)
>
> **Synchronizing components**
> : [canGetValueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmnqw4r3forlgc3dvmvdg64scnfxgi2lom4)
> : [canSetValueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmnqw4u3forlgc3dvmvdg64scnfxgi2lom4)
> : [hasBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnbqxgqtjnzsgs3th)
> : [setValueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponsxivtbnr2wkrtpojbgs3tenfxgo)
> : [synchronizesVariablesWithBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpon4w4y3iojxw42l2mvzvmylsnfqwe3dfonlws5diijuw4zdjnztxg)
> : [valueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpozqwy5lfizxxeqtjnzsgs3th)
>
> **Other**
> : [isStateless](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnfzvg5dborswyzltom)
> : [reset](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpojsxgzlu)
> : [templateWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bporsw24dmmf2gkv3jorue4ylnmu)
> : [validateTakeValueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpozqwy2lemf2gkvdbnnsvmylmovsum33sjnsxsudborua)

## Constructors

---

### WOComponent

`public WOComponent()`

WebObjects Builder archive file exists in the
component directory, it initializes component variables from this
archive. This constructor throws exceptions if it cannot determine
the name of the component or if it cannot initialize the object
for any other reason. Override __WOComponent__()
in compiled subclasses to perform custom initializations; as always,
invoke __super__'s default constructor as the
first thing.

---

## Static Methods

---

### debugString

`public static void debugString(String aString)`

Like [logString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6q3pnvyg63tfnz2c63dpm5jxi4tjnztq),
prints a message to the standard error device (stderr), but only
prints the message if the WODebuggingEnabled user default option
is __true__. If WODebuggingEnabled is __false__,
the [debugString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6q3pnvyg63tfnz2c6zdfmj2wou3uojuw4zy) messages
aren't printed. See [logString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6q3pnvyg63tfnz2c63dpm5jxi4tjnztq) for
information on the format of _aString_.

---

### logString

`public static void logString(String aString)`

Prints a message to the standard error device
(stderr). The message can include formatted variable data using
String's concatenation feature, for example:
> ```
> int i = 500;
>
> float f = 2.045;
>
> WOComponent.logString("Amount = " + i + ", Rate = " + f ", Total = " + i*f);
> ```

---

### templateWithHTMLString:declarationString:languages:

`public static WOElement templateWithHTMLString(
String anHTMLString,
String aDeclarationString,
NSArray languages)`

Programmatically creates the component's template
using _anHTMLString_ as the HTML template contents
and _aDeclarationString_ as the declarations
file contents. Returns (as a WOElement object) the graph of static
and dynamic elements build by parsing the HTML and declaration strings.
You can then use the returned WOElement as the component's template.

__See
Also:__  [templateWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bporsw24dmmf2gkv3jorue4ylnmu)

---

## Instance Methods

---

### appendToResponse

`public void appendToResponse(
WOResponse aResponse,
WOContext aContext)`

Component objects associated with a response
receive this message during the last phase of the request-response
loop. In the append-to-response phase, the application objects (particularly
the response page instance itself) generate the HTML content of
the page. WOComponent's default implementation of this method
forwards the message to the root [WOElement](WOElement.md#apple-k5huk3dfnvsw45a) object of the component template.
Compiled or scripted subclasses of WOComponent can override this
method to replace or supplement the default behavior with custom
logic.

__See Also:__  [invokeActionForRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnfxhm33lmvawg5djn5xem33skjsxc5lfon2a), [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bporqwwzkwmfwhkzltizzg63ksmvyxkzltoq)

---

### application

`public WOApplication application()`

Returns the WOApplication object for the current
application.

__See Also:__  [WOApplication](WOApplication.md#apple-k5huc4dqnruwgylunfxw4) class, [context](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmnxw45dfpb2a), [session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponsxg43jn5xa)

---

### awake

`public void awake()`

Invoked at the beginning of a WOComponent's
involvement in a cycle of the request-response loop, giving the
WOComponent an opportunity to initialize its instance variables
or perform setup operations. The default implementation does nothing.

__See
Also:__  [ensureAwakeInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmvxhg5lsmvaxoyllmvew4q3pnz2gk6du), [sleep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponwgkzlq)

---

### baseURL

`public String baseURL()`

Returns the component URL relative to the server's
document root, for example: "/WebObjects/MyApp.woa/Resources/Main.wo"

__See
Also:__  [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnzqw2zi), [path](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpobqxi2a)

---

### canGetValueForBinding

`public boolean canGetValueForBinding(String aBindingName)`

Verifies that the binding exists and that [valueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpozqwy5lfizxxeqtjnzsgs3th) will
return a value.

__See Also:__  [canSetValueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmnqw4u3forlgc3dvmvdg64scnfxgi2lom4), [hasBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnbqxgqtjnzsgs3th), [valueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpozqwy5lfizxxeqtjnzsgs3th)

---

### canSetValueForBinding

`public boolean canSetValueForBinding(String aBindingName)`

Verifies that the binding exists and that [setValueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponsxivtbnr2wkrtpojbgs3tenfxgo) will succeed.

__See
Also:__  [canGetValueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmnqw4r3forlgc3dvmvdg64scnfxgi2lom4), [hasBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnbqxgqtjnzsgs3th), [setValueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponsxivtbnr2wkrtpojbgs3tenfxgo)

---

### context

`public WOContext context()`

Returns the WOContext object for the current
transaction.

__See Also:__  [WOContext](WOContext.md#apple-k5hug33oorsxq5a) class, [application](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmfyha3djmnqxi2lpny), [session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponsxg43jn5xa)

---

### descriptionForResponse

`public String descriptionForResponse(
WOResponse aResponse,
WOContext aContext)`

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
Also:__  [WOStatisticsStore](WOStatisticsStore.md#apple-k5hvg5dboruxg5djmnzvg5dpojsq) class

---

### ensureAwakeInContext

`public void ensureAwakeInContext(WOContext aContext)`

Ensures that the receiver is awake in
the specified context. Invoke this method before using a component
which was stored in a variable. You don't need to invoke [ensureAwakeInContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmvxhg5lsmvaxoyllmvew4q3pnz2gk6du) if the component
was just created with [pageWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpobqwozkxnf2gqttbnvsq),
if it was restored from the WebObjects page cache, or if the page
will simply be returned as the result of an action. That is, you
only need to invoke this method if you're going to send messages
to a component that is otherwise not awakened. If the receiving
component is already awake, this method has no effect.

__See
Also:__  [awake](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmf3wc23f)

---

### frameworkName

`public String frameworkName()`

If the component is stored in a framework, this
method returns the name of that framework. For example, if the component
is in the framework _NeXT_ROOT___/System/Library/Frameworks/WOExtensions.framework__,
then this method returns the string "WOExtensions".

If
the component is not stored in a framework, this method returns null.

__See
Also:__  [WOResourceManager](WOResourceManager.md#apple-k5hvezltn52xey3fjvqw4ylhmvza) class

---

### generateResponse

`public abstract WOResponse generateResponse()`

Returns a newly-created WOResponse object. WOComponent's
implementation of this method translates the receiving component
into a WOResponse object by sending iteself an [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmfyhazlomrkg6utfonyg63ttmu) message.

__See
Also:__  [generateResponse](WOResponse.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg4dpnzzwkl3hmvxgk4tborsvezltobxw443f) (WOResponse)

---

### hasBinding

`public boolean hasBinding(String aBindingName)`

Returns whether the component has a binding
named _aBindingName_. This method traverses
the chain of associations to the top-level parent, if necessary.

__See
Also:__  [canGetValueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmnqw4r3forlgc3dvmvdg64scnfxgi2lom4), [canSetValueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmnqw4u3forlgc3dvmvdg64scnfxgi2lom4)

---

### hasSession

`public boolean hasSession()`

Returns whether the component is already in
a session. For example, in direct actions, sessions are lazily created
and you can avoid creating another one unnecessarily by calling [hasSession](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnbqxgu3fonzws33o) before [session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponsxg43jn5xa).

__See
Also:__  [session](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponsxg43jn5xa)

---

### invokeActionForRequest

`public WOElement invokeAction(
WORequest aRequest,
WOContext aContext)`

WOComponent objects associated with a request
page receive this message during the middle phase of request handling.
In this middle phase, the [invokeActionForRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnfxhm33lmvawg5djn5xem33skjsxc5lfon2a) message is
propagated through the [WOElement](WOElement.md#apple-k5huk3dfnvsw45a) objects of the page; the
dynamic element on which the user has acted (by, for example, clicking
a button) responds by triggering the method in the request component
that is bound to the action. WOComponent's default implementation
of this method forwards the message to the root WOElement object
of the component template.Compiled or scripted subclasses of WOComponent
can override this method to replace or supplement the default behavior
with custom logic. (Scripted subclasses must use the Objective-C
form of this method: invokeActionForRequest:inContext:).

__See
Also:__  [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmfyhazlomrkg6utfonyg63ttmu), [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bporqwwzkwmfwhkzltizzg63ksmvyxkzltoq)

---

### isCachingEnabled

`public boolean isCachingEnabled()`

Returns whether component-definition caching
is enabled for this component. false is the default.

__See
Also:__  [setCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponsxiq3bmnugs3thivxgcytmmvsa)

---

### isEventLoggingEnabled

`public boolean isEventLoggingEnabled()`

Called to determine if a component wants
event logging. This is not desirable, for example, for components
which are associated with event display as they would interfere
with the actual event logging. The default implementation of this
method returns true.

__See Also:__  [WOEvent](WOEvent.md#apple-k5hug33pnnuwk) class

---

### isStateless

`public boolean isStateless()`

By default, this method returns false,
indicating that state will be maintained for instances of the receiver.
Overriding this method to return true will make the component stateless.
A single instance of each stateless component is shared between
multiple sessions, reducing your application's memory footprint.

__See
Also:__  [reset](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpojsxgzlu)

---

### name

`public String name()`

Returns the name of the component, which includes
a path of all directories under DOCUMENTROOT/WebObjects and is minus
the ".wo" extension; for example "Main" is a typical component
name.

__See Also:__  [baseURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmjqxgzkvkjga), [path](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpobqxi2a)

---

### pageWithName

`public WOComponent pageWithName(String aName)`

Returns a new page instance (a WOComponent object)
identified by _aName_. If _aName_ is null,
the "Main" component is assumed. If the method cannot create
a valid page instance, it throws an exception.

__See
Also:__  [restorePageForContextID](WOSession.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc64tfon2g64tfkbqwozkgn5zeg33oorsxq5cjiq) (WOSession), [savePage](WOSession.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643bozsvaylhmu) (WOSession)

---

### parent

`public WOComponent parent()`

Returns the parent component of the receiver.

---

### path

`public String path()`

Returns the file-system path of the component,
which is an absolute path and includes the ".wo" extension;
for example "C:\Apple\Library\WOApps\MyApp.woa\Resources\Main.wo"
is a typical path.

__See Also:__  [baseURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmjqxgzkvkjga), [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnzqw2zi)

---

### performParentAction

`public Object performParentAction(String anActionName)`

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
declaration to the parent component's "displaySelection" method.The __performParentAction__ method
is used to activate this binding. Let's assume the child component
has an action method called "click"; the implementation would
look like this:

> ```
> public WOComponent click() {             /* this is the child's action */
>     selection = /* some value */;
>     /* now invoke the parent's action */
>     return performParentAction(callBack);
> }
> ```

---

### reset

`public void reset()`

This method-which is only invoked if
the component is stateless-allows a component instance to reset
or delete temporary references to objects that are specific to a
given context. To ensure that when the shared instance of a component
is reused by another session there are no side effects, implement this
method so that it releases and sets to null each of the component's
instance variables.

__See Also:__  [isStateless](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnfzvg5dborswyzltom)

---

### session

`public WOSession session()`

Returns the current WOSession object. This method
creates a new one if there isn't one.

__See
Also:__  [WOSession](WOSession.md#apple-k5hvgzltonuw63q) class, [application](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmfyha3djmnqxi2lpny), [context](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmnxw45dfpb2a), [hasSession](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnbqxgu3fonzws33o)

---

### setCachingEnabled

`public void setCachingEnabled(boolean flag)`

Enables or disables the caching of component
definitions for the receiving component. WOComponent definitions
contain templates and other common information related to components,
and are used to generate instances of those components.When this
attribute is set to true, the application parses the HTML template
and the declaration (".wod") file of a component once and then
stores the resulting component definition for future requests. By
default, this kind of caching is disabled so that you can edit a _scripted_ component
without having to relaunch the application every time to check the results.(Note
that this does not apply to Java subclasses of WOComponent; in this
case, you still have to kill and relaunch the application.)

With [WOApplication](WOApplication.md#apple-k5huc4dqnruwgylunfxw4)'s method of the same
name, you can turn component-definition caching off globally. You
can then control caching of individual component definitions using
WOComponent's version of this method. Selective caching is an
especially valuable technique for very large applications where
only the most frequently requested components should be cached.

__See
Also:__  [isCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnfzugyldnbuw4z2fnzqwe3dfmq)

---

### setValueForBinding

`public void setValueForBinding(
Object aValue,
String aBindingName)`

Sets the value of the binding specified by _aBindingName_ in
the parent component to _aValue_.
If the binding isn't settable, this method throws an exceptionn.

__See
Also:__  [isValueSettableInComponent](WOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifzxg33dnfqxi2lpnyxws42wmfwhkzktmv2hiylcnrsus3sdn5wxa33omvxhi) ( [WOAssociation](WOAssociation.md#apple-k5huc43tn5rwsylunfxw4) class)

---

### sleep

`public void sleep()`

Invoked at the conclusion of a request-handling
cycle to give component the opportunity for deallocating objects
created and initialized in its [awake](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmf3wc23f) method. The default implementation
does nothing.

---

### synchronizesVariablesWithBindings

`public boolean synchronizesVariablesWithBindings()`

Returns whether a nested component pulls all
values down from its parent and pushes all values to its parent
before and after each phase of the request-response loop. By default,
this method returns true. Override this method to create a non-synchronizing
component.

__See Also:__  [setValueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponsxivtbnr2wkrtpojbgs3tenfxgo), [valueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpozqwy5lfizxxeqtjnzsgs3th)

---

### takeValuesFromRequest

`public void takeValuesFromRequest(
WORequest aRequest,
WOContext aContext)`

WOComponent objects associated with a request
receive this message during the first phase of the request-response
loop. The default WOComponent behavior is to send the message to
the root object of the component's template.In this phase, each
dynamic element in the template extracts any entered data or changed
state (such as a check in a check box) associated with an attribute
and assigns the value to the component variable bound to the attribute.Compiled
or scripted subclasses of Component can override this method to
replace or supplement the default behavior with custom logic. (Scripted subclasses
must use the Objective-C form of this method: takeValuesFromRequest:inContext:).

__See
Also:__  [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmfyhazlomrkg6utfonyg63ttmu), [invokeActionForRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpnfxhm33lmvawg5djn5xem33skjsxc5lfon2a)

---

### templateWithName

`public WOElement templateWithName(String aName)`

Returns the root object of the graph of static
and dynamic HTML elements and subcomponents that is used to graphically
render the component identified by _aName_.
This template is constructed from the ".html" and ".wod"
file found in the component directory. You identify the template
by specifying the component name: for example, "HelloWorld."
If the template is not cached, the application will parse the HTML
and declaration files of the specified component to create the template.

__See
Also:__  [setCachingEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponsxiq3bmnugs3thivxgcytmmvsa)

---

### validationFailedWithException

`public void validationFailedWithException(
Throwable exception,
Object value,
String keyPath)`

Called when an Enterprise Object or formatter
failed validation during an assignment. The default implementation
ignores the error. Subclassers can override to record the error
and possibly return a different page for the current action.

---

### validateTakeValueForKeyPath

`public Object validateTakeValueForKeyPath(Object value,
String keyPath)
throws com.apple.yellow.eocontrol.EOValidation.Exception`

Validates (and coerces) the given value,
assigning it if it is different than the current value. Throws a validation
exception if __validateValueForKey__ returns
an exception. Returns the coerced (assigned) value.

---

### valueForBinding

`public Object valueForBinding(String aBindingName)`

Gets the value for the specified binding from
the parent component. If the parent doesn't provide _aBindingName_ in
its delcarations file, this method attempts to get the value from
the current component using __valueForKey__.If
the current component doesn't define this key, this method returns null.
This cascading lookup makes it easy to provide default values for
optional bindings.

__See Also:__  [canGetValueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmnqw4r3forlgc3dvmvdg64scnfxgi2lom4), [setValueForBinding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bponsxivtbnr2wkrtpojbgs3tenfxgo), [synchronizesVariablesWithBindings](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpon4w4y3iojxw42l2mvzvmylsnfqwe3dfonlws5diijuw4zdjnztxg)

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
