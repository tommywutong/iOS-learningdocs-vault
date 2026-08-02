---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WOMessage.html
archived_at: '2026-07-15T08:11:47.654700Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOMessage

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  WebObjects/WOMessage.h

---

## Class Description

---

WOMessage is the parent class for both [WORequest](WORequest-2.md#apple-k5hvezlrovsxg5a) and [WOResponse](WOResponse-2.md#apple-k5hvezltobxw443f),and implements much of
the behavior that is generic to both. WOMessage represents a message
with an HTTP header and either HTML or XML content. HTML content
is typically used when interacting with a Web browser, while XML
content can be used in messages that originate from or are destined
for another application (either an application that "speaks"
XML or another WebObjects application).

The methods of the WOMessage class can be divided primarily
into two groups, those that deal with a message's content and
those that read and set header information. Most of the remaining
WOMessage methods control how the content is encoded and allow you
to attach arbitrary "user info" to your WOMessage objects in
order to pass information about a given message to other objects
within your application.

|  |
| --- |
| Headers are case-insensitive. WebObjects enforces the HTTP specification, but avoid mixing the case of header keys. See the HTTP specification or HTTP documentation for more information on the HTTP headers and version. |

## Content Encodings

You can set the string encoding used for the response content
with [setContentEncoding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzluinxw45dfnz2ek3tdn5sgs3thhi) and
you find out what the current encoding is with [contentEncoding](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwg33oorsw45cfnzrw6zdjnztq).
An integer represents the type of encoding. The following table
lists these integer values along with their WebObjects string-constant
names.

|  |  |  |
| --- | --- | --- |
| __int Value__ | __WebObjects Name__ | __Notes__ |
| 1 | NSASCIIStringEncoding | 0 through 127 |
| 2 | NSNEXTSTEPStringEncoding |  |
| 3 | NSJapaneseEUCStringEncoding |  |
| 4 | NSUTF8StringEncoding |  |
| 5 | NSISOLatin1StringEncoding | default |
| 6 | NSSymbolStringEncoding |  |
| 7 | NSNonLossyASCIIStringEncoding | 7-bit verbose ASCII to represent all unichars |
| 8 | NSShiftJISStringEncoding |  |
| 9 | NSISOLatin2StringEncoding |  |
| 10 | NSUnicodeStringEncoding |  |
| 11 | NSWindowsCP1251StringEncoding | Cyrillic; same as AdobeStandardCyrillic |
| 12 | NSWindowsCP1252StringEncoding | Windows Latin1 |
| 13 | NSWindowsCP1253StringEncoding | Windows Greek |
| 14 | NSWindowsCP1254StringEncoding | Windows Turkish |
| 15 | NSWindowsCP1250StringEncoding | Windows Latin2 |
| 21 | NSISO2022JPStringEncoding | ISO 2022 Japanese encoding for electronic mail |

.

## Adopted Protocols

---

> NSCopying: - copy
> : - copyWithZone:

## Method Types

---

> **Creation**
> : [- init](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxws3tjoq)
>
> **Working with message headers**
> : [- appendHeader:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwc4dqmvxgisdfmfsgk4r2mzxxes3fpe5a)
> : [- appendHeaders:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwc4dqmvxgisdfmfsgk4tthjtg64slmv4tu)
> : [- headerForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxertpojfwk6j2)
> : [- headerKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxes3fpfzq)
> : [- headers](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxe4y)
> : [- headersForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxe42gn5zewzlzhi)
> : [- httpVersion](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwq5duoblgk4ttnfxw4)
> : [- removeHeadersForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxezlnn53gksdfmfsgk4ttizxxes3fpe5a)
> : [- setHeader:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzlujbswczdfoi5gm33sjnsxsoq)
> : [- setHeaders:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzlujbswczdfojztu)
> : [- setHeaders:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzlujbswczdfojztuztpojfwk6j2)
> : [- setHTTPVersion:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzlujbkfiucwmvzhg2lpny5a)
>
> **Working with message content**
> : [- addCookie:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwczdeinxw623jmu5a)
> : [- appendContentBytes:length:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwc4dqmvxgiq3pnz2gk3tuij4xizlthjwgk3thorudu)
> : [- appendContentCharacter:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwc4dqmvxgiq3pnz2gk3tuinugc4tbmn2gk4r2)
> : [- appendContentData:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwc4dqmvxgiq3pnz2gk3tuirqxiyj2)
> : [- appendContentString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwc4dqmvxgiq3pnz2gk3tukn2he2lom45a)
> : [- content](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwg33oorsw45a)
> : [- cookies](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwg33pnnuwk4y)
> : [- removeCookie:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxezlnn53gkq3pn5vwszj2)
> : [- setContent:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzluinxw45dfnz2du)
>
> **Controlling content encoding**
> : [+ defaultEncoding](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hu2zltonqwozjpmrswmylvnr2ek3tdn5sgs3th)
> : [+ setDefaultEncoding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hu2zltonqwozjponsxirdfmzqxk3duivxgg33enfxgooq)
> : [- contentEncoding](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwg33oorsw45cfnzrw6zdjnztq)
> : [- setContentEncoding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzluinxw45dfnz2ek3tdn5sgs3thhi)
>
> **Working with user info**
> : [- setUserInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzlukvzwk4sjnztg6oq)
> : [- userInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxk43fojew4ztp)

## Class Methods

---

### defaultEncoding

`+ (NSStringEncoding)defaultEncoding`

Returns the default character encoding used
to construct a new WOMessage which initially is NSISOLatin1. For
more information, see ["Content Encodings"](#apple-ijeeoqskivcee).

---

### setDefaultEncoding:

`+ (void)setDefaultEncoding:(NSStringEncoding)aStringEncoding`

Lets you specify the character encoding to be
used by default when construcing a new WOMessage. For more information,
see ["Content Encodings"](#apple-ijeeoqskivcee).

---

## Instance Methods

---

### addCookie:

`- (void)addCookie:(WOCookie
*)aCookie`

A convenience method that adds the specified
WOCookie object to the message content.

__See
Also:__  [- cookies](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwg33pnnuwk4y), [- removeCookie:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxezlnn53gkq3pn5vwszj2), [WOCookie](WOCookie-2.md#apple-k5hug33pnnuwk) class specification

---

### appendContentBytes:length:

`- (void)appendContentBytes:(const
void *)someBytes
length:(unsigned)length`

Appends _length_ number
of bytes pointed to by _someBytes_ to
the HTTP response.

---

### appendContentCharacter:

`- (void)appendContentCharacter:(char)aChar`

Appends a single ASCII character (_aChar_)
to the message's contents.

Example:

> ```
> // ...
> if (aFlag)
>     [aResponse appendContentCharacter:'Y'];
> else
>     [aResponse appendContentCharacter:'N'];
> ```

---

### appendContentData:

`- (void)appendContentData:(NSData
*)dataObject`

Appends a data-encapsulating object (_dataObject_)
to the message's contents.

---

### appendContentString:

`- (void)appendContentString:(NSString
*)aString`

Appends a string to the content of the message's
contents. The string is transformed into an NSData object using
the receiver's content encoding. The special HTML characters "<",
">", "&", and double-quote are not escaped
so a browser can interpret them as HTML.

---

### appendHeader:forKey:

`- (void)appendHeader:(NSString
*)aHeader
forKey:(NSString *)aKey`

Appends the HTTP header _aHeader_ to
the receiver and associates, for retrieval, the HTTP key _aKey_ with
the header. This method is commonly used to set the type of content
in a response, for example:
> ```
> [aResponse appendHeader:@"text/html" forKey:@"content-type"];
> ```

__See
Also:__
[- headerForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxertpojfwk6j2),
[- setHeader:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzlujbswczdfoi5gm33sjnsxsoq)

---

### appendHeaders:forKey:

`- (void)appendHeaders:(NSArray
*)headerList
forKey:(NSString *)aKey`

Appends _headerList_ to the list of HTTP headers in
the receiver and associates, for retrieval, the HTTP key _aKey_ with
the list of header elements. If a header doesn't already exist
for the receiver, one is created before the list of headers is appended.

__See
Also:__
[- headerKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxes3fpfzq),
[- headersForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxe42gn5zewzlzhi),
[- setHeaders:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzlujbswczdfojztuztpojfwk6j2)

---

### content

`- (NSData *)content`

Returns the HTML content of the receiver as
an NSData object.

An exception is raised if you attempt to
get the content when all elements of the page have not had their chance
to append HTML to the response. Thus, you should invoke this method
in the application object's __handleRequest:__ method,
after super's __handleRequest:__ has been
invoked. (For scripted applications, __handleRequest:__ is
implemented in Application.wos). Note that at this point in the request-handling
process, the components, pages, and session have already been put
to sleep, so you won't have access to any context, session, or
page information. If you need such information for your response,
store it somewhere--such as in WOMessage's "user info" dictionary-at
a point when you do have access to it. You may want to do this in
your application's [appendToResponse:inContext:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qxa4dfnzsfi32smvzxa33oonstu2loinxw45dfpb2du) method, for
example.

__See Also:__  [- setContent:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzluinxw45dfnz2du), [- setContentEncoding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzluinxw45dfnz2ek3tdn5sgs3thhi)

---

### contentEncoding

`- (NSStringEncoding)contentEncoding`

Returns an integer representing the encoding
used for the message's content. See ["Content Encodings"](#apple-ijeeoqskivcee) in the class
description for a mapped list of supported encodings and their WebObjects
names. For responses, you will want the response encoding to be
the same as that used by the submitting form on the client browser.
In this case it is preferable to use WORequest's [formValueEncoding](WORequest-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwm33snvlgc3dvmvcw4y3pmruw4zy).
> ```
> NSStringEncoding theEncoding = [[aContext request] formValueEncoding];
> ```

The
default string encoding is ISO Latin1.

__See
Also:__  [- setContent:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzluinxw45dfnz2du), [- setContentEncoding:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzluinxw45dfnz2ek3tdn5sgs3thhi)

---

### cookies

`- (NSArray *)cookies`

A convenience method that returns an array of
WOCookie objects to be included in the message (which is uaually
a [WOResponse](WOResponse-2.md#apple-k5hvezltobxw443f)).

__See
Also:__  [- addCookie:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwczdeinxw623jmu5a), [- removeCookie:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxezlnn53gkq3pn5vwszj2), [WOCookie](WOCookie-2.md#apple-k5hug33pnnuwk) class specification

---

### headerForKey:

`- (NSString *)headerForKey:(NSString
*)aKey`

Returns the HTTP header information identified
by _aKey_. If there are multiple headers
associated with the one key, only the first one is returned. Returns nil if
the message has no headers for the key.

__See
Also:__  [- setHeader:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzlujbswczdfoi5gm33sjnsxsoq)

---

### headerKeys

`- (NSArray *)headerKeys`

Returns an array of string keys associated with
the receiver's HTTP headers. Returns nil if there are no headers.
You could easily test to see if a header is included by doing something
similar to this:
> ```
> NSArray *hKeys =  [aMessage headerKeys];
> if ([hKeys containsObject:@"expires"]) {
>     // do something
> }
> ```

__See
Also:__  [- setHeaders:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzlujbswczdfojztuztpojfwk6j2)

---

### headers

`- (NSDictionary *)headers`

Returns the header dictionary with which the
message was initialized.

---

### headersForKey:

`- (NSArray *)headersForKey:(NSString
*)aKey`

Returns _all_ HTTP
headers identified by _aKey_.

__See
Also:__  [- setHeaders:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzlujbswczdfojztuztpojfwk6j2)

---

### httpVersion

`- (NSString *)httpVersion`

Returns the version of HTTP used for the message
(for example, "HTTP/1.0").

__See Also:__  [- setHTTPVersion:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzlujbkfiucwmvzhg2lpny5a)

---

### init

`- (id)init`

Initializes a WOMessage instance. The default
string encoding is made ISO Latin 1.

---

### removeCookie:

`- (void)removeCookie:(WOCookie
*)aCookie`

A convenience method that removes the specified
WOCookie object from the message.

__See Also:__  [- cookies](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwg33pnnuwk4y), [- removeCookie:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxezlnn53gkq3pn5vwszj2), [WOCookie](WOCookie-2.md#apple-k5hug33pnnuwk) class specification

---

### removeHeadersForKey:

`- (void)removeHeadersForKey:(NSString
*)aKey`

Removes the specified headers from the message.

__See
Also:__  [- headerKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxes3fpfzq), [- headersForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxe42gn5zewzlzhi), [- setHeaders:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzlujbswczdfojztuztpojfwk6j2)

---

### setContent:

`- (void)setContent:(NSData
*)someData`

Sets the message contents to _someData_.

__See
Also:__  [- content](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwg33oorsw45a)

---

### setContentEncoding:

`- (void)setContentEncoding:(NSStringEncoding)anEncoding`

Sets the encoding used for the message contents.
See ["Content Encodings"](#apple-ijeeoqskivcee) in the class description for a mapped list
of supported encodings and their WebObjects names. The default string
encoding is ISO Latin1.

__See Also:__  [- contentEncoding](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwg33oorsw45cfnzrw6zdjnztq)

---

### setHTTPVersion:

`- (void)setHTTPVersion:(NSString
*)aVersion`

Sets the version of HTTP used for the message
(for example, "HTTP/1.0").

__See Also:__  [- httpVersion](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwq5duoblgk4ttnfxw4)

---

### setHeader:forKey:

`- (void)setHeader:(NSString
*)aHeader
forKey:(NSString *)aKey`

Sets the HTTP header _aHeader_ in the receiver and associates, for retrieval, the HTTP key _aKey_ with
the header. This method is commonly used to set the type of content
in a response, for example:
> ```
> [aResponse setHeader:@"text/html" forKey:@"content-type"];
> ```

__See
Also:__
[- appendHeader:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwc4dqmvxgisdfmfsgk4r2mzxxes3fpe5a),
[- headerForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxertpojfwk6j2)

---

### setHeaders:

`- (void)setHeaders:(NSDictionary
*)headerDictionary`

For each key in _headerDictionary_,
appends the corresponding value to the list of HTTP headers in the receiver
and associates, for retrieval, the dictionary key with the header
value. If a header doesn't already exist for the receiver, one
is created before the list of headers is appended.

__See
Also:__  [- headers](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxe4y), [- removeHeadersForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxezlnn53gksdfmfsgk4ttizxxes3fpe5a)

---

### setHeaders:forKey:

`- (void)setHeaders:(NSArray *)headerList
forKey:(NSString *)aKey`

Sets the list of HTTP headers in the receiver to _headerList_ and associates, for retrieval, the HTTP key _aKey_ with
the list of header elements. If a header list doesn't already exist
for the receiver, one is created before the list of headers is set.

__See
Also:__
[- appendHeaders:forKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwc4dqmvxgisdfmfsgk4tthjtg64slmv4tu),
[- headerKeys](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxes3fpfzq),
[- headersForKey:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwqzlbmrsxe42gn5zewzlzhi)

---

### setUserInfo:

`- (void)setUserInfo:(NSDictionary
*)aDictionary`

Sets a dictionary in the WOMessage object that,
as a convenience, can contain any kind of information related to
the current response. Objects further down the [appendToResponse:inContext:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qxa4dfnzsfi32smvzxa33oonstu2loinxw45dfpb2du) message
"chain" can retrieve this information using [userInfo](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxk43fojew4ztp).

---

### userInfo

`- (NSDictionary *)userInfo`

Returns a dictionary that, as a convenience,
can contain any kind of information related to the current response.
An object further "upstream" in the [appendToResponse:inContext:](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5qxa4dfnzsfi32smvzxa33oonstu2loinxw45dfpb2du) message
"chain" can set this dictionary in the WOMessage object
as a way to pass information to other objects.

__See
Also:__  [- setUserInfo:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxgzlukvzwk4sjnztg6oq)

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
