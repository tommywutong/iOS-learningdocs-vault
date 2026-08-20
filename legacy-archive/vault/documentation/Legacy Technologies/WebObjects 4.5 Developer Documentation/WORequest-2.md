---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WORequest.html
archived_at: '2026-07-15T08:11:47.682294Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WORequest

> __Inherits
> from:__  [WOMessage](WOMessage-2.md#apple-k5hvezltobxw443f) NSObject

> __Declared in:__  WebObjects/WORequest.h

---

## Class Description

---

A WORequest object typically represents an HTTP request and
thus constitutes an event that requires a reaction from a WebObjects
application. WORequest objects encapsulate the data transmitted
to an HTTP server in a request. Requests usually originate from
user actions in a browser, such as the submission of a URL or a
mouse click on a hyperlink, button, or active image in a page. From
the perspective of WebObjects, the URL identifies a WebObjects application
and the click on a control usually results in the display of a page
of a WebObjects application. Such actions cause the browser to send
an HTTP request to an HTTP server, which forwards the request to
a WebObjects adaptor, which converts it to a WORequest object and
sends that object to the appropriate request handler.

WORequest objects can also be created from HTTP requests sent
by client-side components (Java applets specially modified to interact
with the server side of a WebObjects application), and from HTTP requests
submitted by custom client-side programs that don't use the Java
client-side components. As well, WORequest objects can originate
from custom adaptors that handle HTTP requests _or_ non-HTTP events.
(All the adaptors shipped with WebObjects handle HTTP events only).

Since adaptors usually create WORequest objects, and since
you can usually use WebObjects' adaptors without modifications,
you probably won't have to create your own instances of WORequest
in your code (although you can if you need to). More typically,
your code will obtain information from WORequest objects as they
become available during certain points in the request-response loop.
The application supplies WORequest objects as arguments in the __takeValuesFromRequest:inContext:__ and __invokeActionForRequest:inContext:__ methods,
which are implementable by WOApplication, [WOSession](WOSession-2.md#apple-k5hvgzltonuw63q), [WOComponent](WOComponent-2.md#apple-k5hug33nobxw4zlooq), and [WOElement](WOElement-2.md#apple-k5huk3dfnvsw45a) objects. You can also obtain
the current WORequest object at any time during request handling
through WOContext's [request](WOContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xhizlyoqxxezlrovsxg5a) method.

|  |
| --- |
| Because WORequest objects usually correspond to HTTP requests, the data they encapsulate is almost the same as what you would find in an HTTP request. Thus an understanding of HTTP requests is important for understanding the data vended by WORequest objects. A recommended prerequisite therefore is to review the current HTTP specification or HTTP documentation. |

Note that WORequest inherits from [WOMessage](WOMessage-2.md#apple-k5hvezltobxw443f). Of particular interest
are those [WOMessage](WOMessage-2.md#apple-k5hvezltobxw443f) methods that allow you to
access the request headers ( [headerForKey:](WOMessage-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxertpojfwk6j2), [headerKeys](WOMessage-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxes3fpfzq), [headers](WOMessage-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxe4y), and [headersForKey:](WOMessage-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxe42gn5zewzlzhi)) and [content](WOMessage-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwg33oorsw45a), which return the contents
of the request.

## Programmatically Creating WORequest Objects

As stated above, in most WebObjects applications WORequest
objects are created for you; your application is more concerned
with interpreting and responding to WORequest objects. However,
it is possible to place two WebObjects applications in a peer-to-peer
configuration and have them communicate using WORequest and WOResponse
objects. In situations like these, your application will need to
create the WORequest objects itself and send them to the peer application
using [WOHTTPConnection](WOHTTPConnection-2.md#apple-k5hvezltobxw443f).

The methods declared directly on WORequest allow you to extract
information from a WORequest object. WORequest inherits a number
of methods from WOMessage, however, that allow you to programmatically
specify the contents of a request. In particular, the __appendContent...__ and [setContent:](WOMessage-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzluinxw45dfnz2du) methods in the WOMessage
class are designed to do this. For more information, see the [WOMessage](WOMessage-2.md#apple-k5hvezltobxw443f) class specification.

## Adopted Protocols

---

> NSCopying: - copy
> : - copyWithZone:

## Method Types

---

> **Working with cookies**
> : [- cookieValueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwg33pnnuwkvtbnr2wkrtpojfwk6j2)
> : [- cookieValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwg33pnnuwkvtbnr2wk4y)
> : [- cookieValuesForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwg33pnnuwkvtbnr2wk42gn5zewzlzhi)
>
> **Form values**
> : [- defaultFormValueEncoding](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwizlgmf2wy5cgn5zg2vtbnr2wkrlomnxwi2lom4)
> : [- formValueEncoding](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwm33snvlgc3dvmvcw4y3pmruw4zy)
> : [- formValueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwm33snvlgc3dvmvdg64slmv4tu)
> : [- formValueKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwm33snvlgc3dvmvfwk6lt)
> : [- formValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwm33snvlgc3dvmvzq)
> : [- formValuesForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwm33snvlgc3dvmvzum33sjnsxsoq)
> : [- isFormValueEncodingDetectionEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxws42gn5zg2vtbnr2wkrlomnxwi2lom5cgk5dfmn2gs33oivxgcytmmvsa)
>
> **Request handling**
> : [- requestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxxezlrovsxg5cimfxgi3dfojfwk6i)
> : [- requestHandlerPath](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxxezlrovsxg5cimfxgi3dfojigc5di)
> : [- requestHandlerPathArray](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxxezlrovsxg5cimfxgi3dfojigc5diifzheylz)
>
> **Form Values**
> : [- setDefaultFormValueEncoding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxxgzluirswmylvnr2em33snvlgc3dvmvcw4y3pmruw4zz2)
> : [- setFormValueEncodingDetectionEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxxgzluizxxe3kwmfwhkzkfnzrw6zdjnztuizlumvrxi2lpnzcw4ylcnrswioq)
>
> **Obtaining attributes**
> : [- adaptorPrefix](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwczdbob2g64sqojswm2ly)
> : [- applicationName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwc4dqnruwgylunfxw4ttbnvsq)
> : [- applicationNumber](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwc4dqnruwgylunfxw4ttvnvrgk4q)
> : [- browserLanguages](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwe4tpo5zwk4smmfxgo5lbm5sxg)
> : [- isFromClientComponent](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxws42gojxw2q3mnfsw45cdn5wxa33omvxhi)
> : [- initWithMethod:uri:httpVersion:headers:content:userInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxws3tjorlws5dijvsxi2dpmq5hk4tjhjuhi5dqkzsxe43jn5xdu2dfmfsgk4tthjrw63tumvxhiotvonsxeslomzxtu)
> : [- method](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxw2zlunbxwi)
> : [- sessionID](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxxgzltonuw63sjiq)
> : [- uri](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxxk4tj)

## Instance Methods

---

### adaptorPrefix

`- (NSString *)adaptorPrefix`

Returns the part of the request's URI that is
specific to a particular adaptor. This is typically a URL ending
in "/WebObjects", "/WebObjects.exe", "/WebObjects.dll",
or uppercase versions of these strings. WebObjects uses a request's
adaptor prefix to set the adaptor prefix in the generated response's URL.
A WORequest must always have an adaptor prefix.

__See
Also:__  [- applicationName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwc4dqnruwgylunfxw4ttbnvsq), [- applicationNumber](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwc4dqnruwgylunfxw4ttvnvrgk4q), [- uri](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxxk4tj)

---

### applicationName

`- (NSString *)applicationName`

Returns the part of the request's URI that identifies
the application the request is intended for. This name does not
include the ".woa" extension of an application directory.
A WORequest must always have an application name specified.

__See
Also:__  [- adaptorPrefix](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwczdbob2g64sqojswm2ly), [- applicationNumber](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwc4dqnruwgylunfxw4ttvnvrgk4q), [- uri](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxxk4tj)

---

### applicationNumber

`- (int)applicationNumber`

Returns the part of the request's URI that identifies
the particular application instance the request is intended for.
This attribute is -1 if the request can be handled by any instance
of the application, which is always the case for the first request
in a session.

__See Also:__  [- applicationName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwc4dqnruwgylunfxw4ttbnvsq), [- uri](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxxk4tj)

---

### browserLanguages

`- (NSArray *)browserLanguages`

Returns the language preference list from the
user's browser.

---

### cookieValueForKey:

`- (NSString *)cookieValueForKey:(NSString
*)aKey`

Returns a string value for the cookie key specified
by _aKey_.

__See
Also:__  [- cookieValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwg33pnnuwkvtbnr2wk4y), [- cookieValuesForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwg33pnnuwkvtbnr2wk42gn5zewzlzhi), [WOCookie](WOCookie-2.md#apple-k5hug33pnnuwk) class specification

---

### cookieValues

`- (NSDictionary *)cookieValues`

Returns a dictionary of cookie values and cookie
keys.

__See Also:__  [- cookieValueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwg33pnnuwkvtbnr2wkrtpojfwk6j2), [- cookieValuesForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwg33pnnuwkvtbnr2wk42gn5zewzlzhi), [WOCookie](WOCookie-2.md#apple-k5hug33pnnuwk) class specification

---

### cookieValuesForKey:

`- (NSArray *)cookieValuesForKey:(NSString
*)aKey`

Returns an array of values for the cookie key
specified by _aKey_. Use this method
to retrieve information stored in a cookie in an HTTP header. Valid
keys are specified in the cookie specification.

__See
Also:__  [- cookieValueForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwg33pnnuwkvtbnr2wkrtpojfwk6j2), [- cookieValues](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwg33pnnuwkvtbnr2wk4y), [WOCookie](WOCookie-2.md#apple-k5hug33pnnuwk) class specification

---

### defaultFormValueEncoding

`- (NSStringEncoding)defaultFormValueEncoding`

Returns the _default_ string
encoding the WORequest object uses for converting form values from
ASCII to Unicode. It uses the default encoding only when it can
detect no encoding from the ASCII form values or if encoding detection
is disabled. If no default form-value encoding is set, NSISOLatin1StringEncoding
is used.

__See Also:__  [- setDefaultFormValueEncoding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxxgzluirswmylvnr2em33snvlgc3dvmvcw4y3pmruw4zz2)

---

### formValueEncoding

`- (NSStringEncoding)formValueEncoding`

Returns the encoding last used to convert form
values from ASCII to Unicode. This encoding is either the result
of an earlier detection of form-value encoding or the default form
value encoding.

__See Also:__  [- defaultFormValueEncoding](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwizlgmf2wy5cgn5zg2vtbnr2wkrlomnxwi2lom4), [- isFormValueEncodingDetectionEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxws42gn5zg2vtbnr2wkrlomnxwi2lom5cgk5dfmn2gs33oivxgcytmmvsa)

---

### formValueForKey:

`- (id)formValueForKey:(NSString
*)aKey`

Returns a form value identified by the name _aKey_.
If there are multiple form values identified by the same name,
only one of the values is returned, and which of these values is
not defined. You should use this method for names that you know
occur only once in the name/value pairs of form data.

---

### formValueKeys

`- (NSArray *)formValueKeys`

Returns an array of NSStrings corresponding
to the names (or keys) used to access values of a form. The array
is not sorted in any particular order, and is not necessarily sorted
in the same order on successive invocations of this method.

---

### formValues

`- (NSDictionary *)formValues`

Returns an NSDictionary containing all of the
form data name/value pairs.

---

### formValuesForKey:

`- (NSArray *)formValuesForKey:(NSString
*)aKey`

Returns an array of all values (as NSStrings)
of the form identified by the name _aKey_.
This array is not sorted in any particular order, and is not necessarily
sorted in the same order on successive invocations of this method.
You should use this method when you know that a name (key) used
for accessing form data can be matched with more than one value.

---

### initWithMethod:uri:httpVersion:headers:content:userInfo:

`- (id)initWithMethod:(NSString
*)aMethod
uri:(NSString *)aURL
httpVersion:(NSString *)anHTTPVersion
headers:(NSDictionary *)someHeaders
content:(NSData *)aContent
userInfo:(NSDictionary *)userInfo`

Returns a WORequest object initialized with
the specified parameters. The first two arguments are required:

- _aMethod_ must be either "GET"
  or "POST"; anything else causes an exception to be raised.
- _aURL_ must be a valid URL; if
  the URL is invalid, an exception is raised.

If
either argument is omitted, an exception is raised.

The
remaining arguments are optional; if you specify __nil__ for
these, the designated initializer substitutes default values or
initializes them to __nil__. The _someHeaders_ argument
(if not __nil__) should be a dictionary whose
NSString keys correspond to header names and whose values are arrays
of one or more strings corresponding to the values of each header.
The _userInfo_ dictionary can contain
any information that the WORequest object wants to pass along to
other objects involved in handling the request.

For
more information on each argument, see the description of the corresponding
accessor method.

---

### isFormValueEncodingDetectionEnabled

`- (BOOL)isFormValueEncodingDetectionEnabled`

Returns whether detection of form-value encoding
is allowed to take place when form values are obtained.

__See
Also:__  [- setFormValueEncodingDetectionEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxxgzluizxxe3kwmfwhkzkfnzrw6zdjnztuizlumvrxi2lpnzcw4ylcnrswioq)

---

### isFromClientComponent

`- (BOOL)isFromClientComponent`

Returns whether the request originated from
an event in a client-side component (that is, a Java applet that
can interact with the server side of a WebObjects application).

If
you use dynamic elements and write write HTML code in the response,
you should check that the request is not from a client-side component
before writing into the response.

---

### method

`- (NSString *)method`

Returns the method the WORequest object was
initialized with. A WORequest's method defines where it will look
for form values. The only currently supported methods are "GET"
and "PUT", which have the same meaning as the HTTP request
method tokens of the same name.

__See Also:__  [- content](WOMessage-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwg33oorsw45a) ( [WOMessage](WOMessage-2.md#apple-k5hvezltobxw443f) class), [- httpVersion](WOMessage-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwq5duoblgk4ttnfxw4) ( [WOMessage](WOMessage-2.md#apple-k5hvezltobxw443f) class)

---

### requestHandlerKey

`- (NSString *)requestHandlerKey`

Returns the part of the request's URI which
identifies the request handler. This identifies the request handle
which will process the reuquest and cannot be nil

---

### requestHandlerPath

`- (NSString *)requestHandlerPath`

Returns the part of the URL which identifies,
for a given request handler, which information is requested. Different
request handlers use this part of the URL in different ways.

---

### requestHandlerPathArray

`- (NSArray *)requestHandlerPathArray`

Returns the request handler path decomposed
into elements.

---

### sessionID

`- (NSString *)sessionID`

Returns the session ID, or nil if no session
ID is found. This method first looks for the session ID in the URL,
then checks the form values, and finally checks to see if the session
ID is stored in a cookie.

---

### setDefaultFormValueEncoding:

`- (void)setDefaultFormValueEncoding:(NSStringEncoding)anEncoding`

Sets the default string encoding for the receiver
to use when converting its form values from ASCII to Unicode. The
default string encoding is called into play if the WORequest cannot
detect an encoding from the ASCII form values or if encoding detection
is disabled. If no default form value encoding is explicitly set,
the WORequest uses NSISOLatin1StringEncoding.

__See
Also:__  [- defaultFormValueEncoding](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwizlgmf2wy5cgn5zg2vtbnr2wkrlomnxwi2lom4), [- setFormValueEncodingDetectionEnabled:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxxgzluizxxe3kwmfwhkzkfnzrw6zdjnztuizlumvrxi2lpnzcw4ylcnrswioq)

---

### setFormValueEncodingDetectionEnabled:

`- (void)setFormValueEncodingDetectionEnabled:(BOOL)flag`

Enables or disables automatic detection of the
best encoding for the receiver to use when it converts form values
from ASCII to Unicode. When detection is enabled, a WORequest
object scans the ASCII form values and applies heuristics to decide
which is the best encoding to use. If no specific encoding is discernible,
or if detection is disabled, the WORequest uses the default form
value encoding for the conversion.

__See Also:__  [- isFormValueEncodingDetectionEnabled](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxws42gn5zg2vtbnr2wkrlomnxwi2lom5cgk5dfmn2gs33oivxgcytmmvsa), [- setDefaultFormValueEncoding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxxgzluirswmylvnr2em33snvlgc3dvmvcw4y3pmruw4zz2)

---

### uri

`- (NSString *)uri`

Returns the Uniform Resource Identifier (URI)
the WORequest was initialized with. For a session's first request,
the URI indicates the resource that the request is seeking (such
as a WebObjects application); for subsequent requests in the session,
the URI indicates which page of the application should handle the
request. If the request was caused (as is usually the case) by a
web browser submitting a URL to an HTTP server, the URI is that
part of the URL that follows the port number. Because the format
of WebObjects URLs and the corresponding request URI might change
between different versions of WebObjects, you should not attempt
to parse the URI returned by this method. Instead, use WORequest's
accessor methods to access particular URI/URL components.

__See
Also:__  [- adaptorPrefix](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwczdbob2g64sqojswm2ly), [- applicationName](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwc4dqnruwgylunfxw4ttbnvsq), [- applicationNumber](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwc4dqnruwgylunfxw4ttvnvrgk4q)

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
