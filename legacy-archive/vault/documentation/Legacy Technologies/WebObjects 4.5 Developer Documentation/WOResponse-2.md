---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WOResponse.html
archived_at: '2026-07-15T08:11:47.740438Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOResponse

> __Inherits
> from:__  [WOMessage](WOMessage-2.md#apple-k5hvezltobxw443f) NSObject

> __Conforms to:__  [WOActionResults](WOActionResults-2.md#apple-ijaucscbijces) NSObject
> (NSObject)

> __Declared in:__  WebObjects/WOResponse.h

---

## Class Description

---

A WOResponse object represents an HTTP response that an application
returns to a Web server to complete a cycle of the request-response
loop. The composition of a response occurs during the third and
final phase of this loop, a phase marked by the propagation of the [appendToResponse:inContext:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qxa4dfnzsfi32smvzxa33oonstu2loinxw45dfpb2du) message
through the objects of the application. The [WOApplication](WOApplication-2.md#apple-k5huc4dqnruwgylunfxw4) object first sends this
message, passing in a newly-created WOResponse object as an argument. [WOElement](WOElement-2.md#apple-k5huk3dfnvsw45a) objects, which represent the
dynamic and static HTML elements on a page, respond to the message
by appending their HTML representation to the content of the WOResponse
object. WOApplication, [WOSession](WOSession-2.md#apple-k5hvgzltonuw63q), and [WOComponent](WOComponent-2.md#apple-k5hug33nobxw4zlooq) objects can also respond
to the message by adding information to the WOResponse object.

A WOResponse has two major parts: HTML content and HTTP information.
The content is what is displayed in a Web browser; it can include _escaped_ HTML,
which is HTML code shown "as is," uninterpreted. The other
information encapsulated by a WOResponse object is used when handling
the response. This HTTP data includes headers, status codes, and
version string. See the HTTP specification or HTTP documentation
for descriptions of these items.

The [WOMessage](WOMessage-2.md#apple-k5hvezltobxw443f) class-from which WOResponse
inherits-declares most of the methods you use when constructing
a response. These methods can be divided into two groups, those
that add to a response's HTML content and those that read and set
HTTP information. To the methods provided by [WOMessage](WOMessage-2.md#apple-k5hvezltobxw443f), the WOResponse class adds
two methods that escape HTML ( [appendContentHTMLAttributeValue:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzxa33oonss6ylqobsw4zcdn5xhizloorefitkmif2hi4tjmj2xizkwmfwhkzj2) and [appendContentHTMLString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzxa33oonss6ylqobsw4zcdn5xhizloorefitkmkn2he2lom45a)). For images
and other binary data, use [appendContentData:](WOMessage-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwc4dqmvxgiq3pnz2gk3tuirqxiyj2) (declared
in the [WOMessage](WOMessage-2.md#apple-k5hvezltobxw443f) class). You can obtain and
set the entire content of the response with [WOMessage](WOMessage-2.md#apple-k5hvezltobxw443f)'s [content](WOMessage-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwg33oorsw45a) and [setContent:](WOMessage-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzluinxw45dfnz2du) methods. The following
example shows a sequence of __appendContent...__ messages
that compose an HTTP "POST" message:

> ```
> [aResponse appendContentString:@"<form method=\"POST\" action=\""];
> [aResponse appendContentHTMLAttributeValue:[aContext url]];
> [aResponse appendContentCharacter:'"'];
> [aResponse.appendContentString:@">"];
> ```

The remaining WOResponse instance methods set and read the
the HTTP status code. WOResponse also provides two class methods
that allow you to escape NSString objects.

## Adopted Protocols

---

> NSCopying: - copy
> : - copyWithZone:
> WOActionResults: [- generateResponse](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzxa33oonss6z3fnzsxeylumvjgk43qn5xhgzi)

## Method Types

---

> **Creation**
> : [- init](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzxa33oonss62lonf2a)
>
> **Working with HTTP status**
> : [- setStatus:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzxa33oonss643forjxiyluovztu)
> : [- status](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzxa33oonss643umf2hk4y)
>
> **Working with HTML content**
> : [- appendContentHTMLAttributeValue:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzxa33oonss6ylqobsw4zcdn5xhizloorefitkmif2hi4tjmj2xizkwmfwhkzj2)
> : [- appendContentHTMLString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzxa33oonss6ylqobsw4zcdn5xhizloorefitkmkn2he2lom45a)
> : [- generateResponse](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzxa33oonss6z3fnzsxeylumvjgk43qn5xhgzi)
> : [+ stringByEscapingHTMLString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hvezltobxw443ff5zxi4tjnztue6kfonrwc4djnztuqvcnjrjxi4tjnzttu)
> : [+ stringByEscapingHTMLAttributeValue:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hvezltobxw443ff5zxi4tjnztue6kfonrwc4djnztuqvcnjraxi5dsnfrhk5dfkzqwy5lfhi)
>
> **Controlling Client Caching**
> : [- disableClientCaching](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzxa33oonss6zdjonqwe3dfinwgszloorbwcy3infxgo)

## Class Methods

---

### stringByEscapingHTMLAttributeValue:

`+ (NSString *)stringByEscapingHTMLAttributeValue:(NSString
*)aString`

This method takes astring and, if escaping is
required, returns a new string with certain characters escaped out.
If escaping is not required, no conversion is performed and _aString_ is
returned. Use this method to escape strings which will appear as
attribute values of a tag. The escaped characters are:

|  |  |
| --- | --- |
| __Character__ | __Escaped character__ |
| & | & |
| " | " |
| \t |  |
| \n |  |
| \r |  |
| < | < |
| > | > |

---

### stringByEscapingHTMLString:

`+ (NSString *)stringByEscapingHTMLString:(NSString
*)aString`

This method takes a string and, if escaping
is required, returns a new string with certain characters escaped
out. If escaping is not required, no conversion is performed and _aString_ is
returned. Use this method to escape strings which will appear in
the visible part of an HTML file (that is, not inside a tag). The
escaped characters are:

|  |  |
| --- | --- |
| __Character__ | __Escaped character__ |
| & | & |
| " | " |
| < | < |
| > | > |

---

## Instance Methods

---

### appendContentHTMLAttributeValue:

`- (void)appendContentHTMLAttributeValue:(NSString
*)aValue`

Appends an HTML attribute value to the HTTP
content after transforming the string _aValue_ into
an NSData object using the receiver's content encoding. Special
HTML characters ("<", ">", "&",
and double quote) are _escaped_ so
that the browser does not interpret them. In other words, the message
> ```
> [aResponse appendContentHTMLAttributeValue:@"<B>"];
> ```

would
transform the argument to "<B>".

__See
Also:__  [- setContentEncoding:](WOMessage-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzluinxw45dfnz2ek3tdn5sgs3thhi) ( [WOMessage](WOMessage-2.md#apple-k5hvezltobxw443f) class)

---

### appendContentHTMLString:

`- (void)appendContentHTMLString:(NSString
*)aString`

Appends an HTML string to the HTTP response
after transforming the string _aString_ into
an NSData object using the receiver's content encoding. Special
HTML characters ("<", ">", "&",
and double quote) are _escaped_ so
that the browser does not interpret them. For example, "<P>"
becomes "<P>".

__See Also:__  [- setContentEncoding:](WOMessage-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzluinxw45dfnz2ek3tdn5sgs3thhi) ( [WOMessage](WOMessage-2.md#apple-k5hvezltobxw443f) class)

---

### disableClientCaching

`- (void)disableClientCaching`

Attempts to disable caching in the client
browser by appending a "no-cache" Cache-Control response directive
to the HTTP response and by appending Expires and Date values that
equal (they are both set to the current date and time).

This
method shouldn't be invoked more than once for a given response.

---

### generateResponse

`- (WOResponse *)generateResponse`

Returns a WOResponse object. WOResponse's
implementation simply returns itself.

__See
Also:__  [- generateResponse](WOComponent-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5wxa33omvxhil3hmvxgk4tborsvezltobxw443f) (WOComponent)

---

### init

`- (id)init`

Initializes a WOResponse instance. HTTP status
is set to 200 (OK), client caching is enabled, and the default string
encoding is made ISO Latin 1.

---

### setStatus:

`- (void)setStatus:(unsigned
int)anInt`

Sets the HTTP status to _anInt_.
Consult the HTTP specification or HTTP documentation for the significance
of status integers.

__See Also:__  [- status](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzxa33oonss643umf2hk4y)

---

### status

`- (unsigned int)status`

Returns an integer code representing the HTTP
status. Consult the HTTP specification or HTTP documentation for
the significance of these status codes.

By default, the status
is 200 ("OK" status).

__See
Also:__  [- setStatus:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzxa33oonss643forjxiyluovztu)

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
