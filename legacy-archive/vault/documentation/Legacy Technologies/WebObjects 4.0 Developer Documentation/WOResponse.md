---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/WOResponse.html
archived_at: '2026-07-18T01:28:52.377344Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](WOResourceManager.md)
[!](WOSession.md)

---

# WOResponse

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.webobjects

---

## Class Description

A WOResponse object represents an HTTP response that an application returns to a Web server to complete a cycle of the request-response loop. The composition of a response occurs during the third and final phase of this loop, a phase marked by the propagation of the `[appendToResponse](WOApplication.md#apple-g43tama)` message through the objects of the application. The [WOApplication](WOApplication.md) object first sends this message, passing in a newly-created WOResponse object as an argument. [WOElement](WOElement.md) objects, which represent the dynamic and static HTML elements on a page, respond to the message by appending their HTML representation to the content of the WOResponse object. WOApplication, [WOSession](WOSession.md), and [WOComponent](WOComponent.md) objects can also respond to the message by adding information to the WOResponse object.

A WOResponse has two major parts: HTML content and HTTP information. The content is what is displayed in a Web browser; it can include _escaped_ HTML, which is HTML code shown "as is," uninterpreted. The other information encapsulated by a WOResponse object is in the handling the response. This HTTP data includes headers, status codes, and version string. See the HTTP specification or HTTP documentation for descriptions of these items.

As you might expect, the methods of the WOResponse class can be divided into two groups, those that add to a response's HTML content and those that read and set HTTP information. The former group consists of methods that escape HTML ([`appendContentHTMLAttributeValue`](#apple-g4ya) and [`appendContentHTMLString`](#apple-g42a)) and those that don't. For images and other binary data, you can use the [`appendContentData`](#apple-gy3a). You can obtain and set the entire content of the response with [`content`](#apple-haza) and [`setContent`](#apple-gezde). The following example shows a sequence of "appendContent" messages that compose an HTTP "POST" message:

> ```
> aResponse.appendContentString("<form method=\"POST\" action=\"");
> ```

> ```
> aResponse.appendContentHTMLAttributeValue(aContext.url());
> ```

> ```
> aResponse.appendContentCharacter('"');
> ```

> ```
> aResponse.appendContentString(">");
> ```

Most of the remaining WOResponse methods set and read the response's HTTP headers, the HTTP status code, and the HTTP version.

---

### Content Encodings

You can set the string encoding used for the response content with [`setContentEncoding`](#apple-gezdm) and you find out what the current encoding is with [`contentEncoding`](#apple-gu3dony). An integer represents the type of encoding. The following table lists these integer values along with their OPENSTEP string-constant names.

| __int Value__ | __OPENSTEP Name__ | __Notes__ |
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

```
```


---

## Method Types

**Constructors**

**[WOResponse](#apple-ge3dqmru)**

**Obtaining attributes**

**[defaultEncoding](#apple-gqzdiny)

**[content](#apple-haza)

**[headerForKey](#apple-he4a)

**[headerKeys](#apple-geyde)

**[headersForKey](#apple-geydm)

**[httpVersion](#apple-geyta)

**[status](#apple-gmztgoa)

**[userInfo](#apple-ge2ti)****************

**Setting attributes**

**[setDefaultEncoding](#apple-gqzdkna)

**[setContent](#apple-gezde)

**[setHeader](#apple-gezti)

**[setHeaders](#apple-geztq)

**[setHTTPVersion](#apple-gezta)

**[setStatus](#apple-ge2de)

**[setUserInfo](#apple-ge2dm)**************

**Appending response content**

**[appendContentData](#apple-gy3a)

**[appendContentString](#apple-g44a)

**[setContentEncoding](#apple-gezdm)

**[contentEncoding](#apple-gu3dony)********

**Working with HTML content**

**[appendContentHTMLAttributeValue](#apple-g4ya)

**[appendContentHTMLString](#apple-g42a)

**[stringByEscapingHTMLString](#apple-gu2deoi)

**[stringByEscapingHTMLAttributeValue](#apple-gu2dimi)********

**Working with cookies**

**[addCookie](#apple-he4tq)

**[cookies](#apple-heya)

**[removeCookie](#apple-geytq)******

---

## Constructors

---

### WOResponse

public `WOResponse`()

Returns an initialized WOResponse instance. HTTP status is set to 200 (OK), client caching is enabled, and the default string encoding is made ISO Latin 1.

#

---

### defaultEncoding

public static int `defaultEncoding`()

Returns the default character encoding used to construct a new WOResponse. By default, this encoding is NSISOLatin1. For more information, see ["Content Encodings"](#apple-geydgnq).

---

### setDefaultEncoding

public static void `setDefaultEncoding`(int _aStringEncoding_)

Lets you specify the character encoding used by default when construcing a new WOResponse. For more information, see ["Content Encodings"](#apple-geydgnq).

---

### stringByEscapingHTMLString

public static java.lang.String `stringByEscapingHTMLString`(java.lang.String _aString_)

This method takes a string and, if escaping is required, returns a new string with certain characters escaped out. If escaping is not required, no conversion is performed and _aString_ is returned. Use this method to escape strings which will appear in the visible part of an HTML file (that is, not inside a tag). The escaped characters are:

| & | &amp; |
| " | &quot; |
| < | &lt; |
| > | &gt; |

```
```


---

### stringByEscapingHTMLAttributeValue

public static java.lang.String `stringByEscapingHTMLAttributeValue`(java.lang.String _aString_)

This method takes astring and, if escaping is required, returns a new string with certain characters escaped out. If escaping is not required, no conversion is performed and _aString_ is returned. Use this method to escape strings which will appear as attribute values of a tag. The escaped characters are:

| & | &amp; |
| " | &quot; |
| \t | &#9; |
| \n | &#10; |
| \r | &#13; |
| < | &lt; |
| > | &gt; |

```
```


---

## Instance Methods

---

### addCookie

public void `addCookie`(WOCookie _aCookie_)

Adds the specified WOCookie object to the response.

__See also:__
[`cookies`](#apple-heya), [`removeCookie`](#apple-geytq), [WOCookie](WOCookie.md) class specification

---

### appendContentCharacter

public void `appendContentCharacter`(byte _aChar_)

Appends a single ASCII character (_aChar_) to the HTTP response.

---

### appendContentData

public void `appendContentData`(NSData _dataObject_)

Appends a data-encapsulating object (_dataObject_) to the HTTP response.

---

### appendContentHTMLAttributeValue

public void `appendContentHTMLAttributeValue`(java.lang.String _aValue_)

Appends an HTML attribute value to the HTTP content after transforming the string _aValue_ into an NSData object using the receiver's content encoding. Special HTML characters ("<", ">", "&", and double quote) are _escaped_ so that the browser does not interpret them. In other words, the message

> ```
> aResponse.appendContentHTMLAttributeValue("<B>");
> ```

would transform the argument to "<B>".

__See also:__
`[setContentEncoding](#apple-gezdm)`

---

### appendContentHTMLString

public void `appendContentHTMLString`(java.lang.String _aString_)

Appends an HTML string to the HTTP response after transforming the string _aString_ into an NSData object using the receiver's content encoding. Special HTML characters ("<", ">", "&", and double quote) are _escaped_ so that the browser does not interpret them. For example, "<P>" becomes "&ltP&gt".

__See also:__
`[setContentEncoding](#apple-gezdm)`

---

### appendContentString

public void `appendContentString`(java.lang.String _aString_)

Appends a string to the content of the HTTP response. The string is transformed into an NSData object using the receiver's content encoding. The special HTML characters "<", ">", "&", and double-quote are not escaped so the browser can interpret them as HTML.

---

### content

public NSData `content`()

Returns the HTML content of the receiver as an NSData object.

An exception is raised if you attempt to get the content when all elements of the page have not had their chance to append HTML to the response. Thus, you should invoke this method in the application object's `handleRequest:` method, after super's `handleRequest:` has been invoked. (For scripted applications, `handleRequest:` is implemented in Application.wos). Note that at this point in the request-handling process, the components, pages, and session have already been put to sleep, so you won't have access to any context, session, or page information. If you need such information for your response, store it somewhere--such as in WOResponse's "user info" dictionary-at a point when you do have access to it. You may want to do this in your application's `[appendToResponse](WOApplication.md#apple-g43tama)` method, for example.

__See also:__
[`setContent`](#apple-gezde), `[setContentEncoding](#apple-gezdm)`

---

### contentEncoding

public int `contentEncoding`()

Returns an integer representing the encoding used for the response content. See ["Content Encodings"](#apple-geydgnq) in the class description for a mapped list of supported encodings and their Objective-C names. Usually, you will want the response encoding to be the same as that used by the submitting form on the client browser. In this case it is preferable to use WORequest's [`formValueEncoding`](WORequest.md#apple-g44q).

> ```
> NSStringEncoding theEncoding = [[aContext request] formValueEncoding];
> ```

The default string encoding is ISO Latin1.

__See also:__
[`setContent`](#apple-gezde), `[setContentEncoding](#apple-gezdm)`

---

### cookies

public NSArray `cookies`()

Returns an array of WOCookie objects to be included in the response.

__See also:__
[`addCookie`](#apple-he4tq), [`removeCookie`](#apple-geytq), [WOCookie](WOCookie.md) class specification

---

### headerForKey

public java.lang.String `headerForKey`(java.lang.String _aKey_)

Returns the HTTP header information identified by _aKey_. If there are multiple headers associated with the one key, only the first one is returned. Returns `null` if there are no headers for the key.

__See also:__
`[setHeader](#apple-gezti)`

---

### headerKeys

public NSArray `headerKeys`()

Returns an array of string keys associated with the receiver's HTTP headers. Returns `null` if there are no headers. You could easily test to see if a header is included by doing something similar to this:

> ```
> ImmutableVector hKeys =  aResponse.headerKeys();
> ```

> ```
> if (hKeys.contains("expires")) {
> ```

> ```
> // do something
> ```

> ```
> }
> ```

__See also:__
`[setHeaders](#apple-geztq)`

---

### headersForKey

public NSArray `headersForKey`(java.lang.String _aKey_)

Returns _all_ HTTP headers identified by _aKey_.

__See also:__
`[setHeaders](#apple-geztq)`

---

### httpVersion

public java.lang.String `httpVersion`()

Returns the version of HTTP used for the response (for example, "HTTP/1.0").

__See also:__
`[setHTTPVersion](#apple-gezta)`

---

### removeCookie

public void `removeCookie`(WOCookie _aCookie_)

Removes the specified WOCookie object from the response.

__See also:__
[`cookies`](#apple-heya), [`removeCookie`](#apple-geytq), [WOCookie](WOCookie.md) class specification

---

### setContent

public void `setContent`(NSData _someData_)

Sets the HTML content of the HTTP response to _someData_.

__See also:__
`[content](#apple-haza)`

---

### setContentEncoding

public void `setContentEncoding`(int _anEncoding_)

Sets the encoding used for the content of the HTTP response. See ["Content Encodings"](#apple-geydgnq) in the class description for a mapped list of supported encodings and their Objective-C names. The default string encoding is ISO Latin1.

__See also:__
`[contentEncoding](#apple-gu3dony)`

---

### setHTTPVersion

public void `setHTTPVersion`(java.lang.String _aVersion_)

Sets the version of HTTP used for the response (for example, "HTTP/1.0").

__See also:__
`[httpVersion](#apple-geyta)`

---

### setHeader

public void `setHeader`(java.lang.String _aHeader_, java.lang.String _aKey_)

Sets the HTTP header _aHeader_ in the receiver and associates, for retrieval, the HTTP key _aKey_ with the header. This method is commonly used to set the type of content in a response, for example:

> ```
> aResponse.setHeader("text/html", "content-type");
> ```

__See also:__
`[headerForKey](#apple-he4a)`

---

### setHeaders

public void `setHeaders`(NSArray _headerList_, java.lang.String _aKey_)

Sets the list of HTTP headers _headerList_ in the receiver and associates, for retrieval, the HTTP key _aKey_ with the list of header elements.

__See also:__
[`headerKeys`](#apple-geyde), ____`headersForKey`

---

### setStatus

public void `setStatus`(int _anInt_)

Sets the HTTP status to _anInt_. Consult the HTTP specification or HTTP documentation for the significance of status integers.

__See also:__
`[status](#apple-gmztgoa)`

---

### setUserInfo

public void `setUserInfo`(NSDictionary _aDictionary_)

Sets a dictionary in the WOResponse object that, as a convenience, can contain any kind of information related to the current response. Objects further down the `[appendToResponse](WOApplication.md#apple-g43tama)` message "chain" can retrieve this information using [`userInfo`](#apple-ge2ti).

---

### status

public int `status`()

Returns an integer code representing the HTTP status. Consult the HTTP specification or HTTP documentation for the significance of these status codes.

By default, the status is 200 ("OK" status).

__See also:__
`[setStatus](#apple-ge2de)`

---

### userInfo

public NSDictionary `userInfo`()

Returns a dictionary that, as a convenience, can contain any kind of information related to the current response. An object further "upstream" in the `[appendToResponse](WOApplication.md#apple-g43tama)` message "chain" can set this dictionary in the WOResponse object as a way to pass information to other objects.

__See also:__
`[setUserInfo](#apple-ge2dm)`

****

---

[!](WOResourceManager.md)
[!](WOSession.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
