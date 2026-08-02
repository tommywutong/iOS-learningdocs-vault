---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WOResponse.html
archived_at: '2026-07-18T01:28:54.392543Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WOResourceManager-2.md)
[!](WOSession-2.md)

---

# WOResponse

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
WebObjects/WOResponse.h

---

## Class Description

A WOResponse object represents an HTTP response that an application returns to a Web server to complete a cycle of the request-response loop. The composition of a response occurs during the third and final phase of this loop, a phase marked by the propagation of the __[appendToResponse:inContext:](WOApplication-2.md#apple-g43tama)__ message through the objects of the application. The [WOApplication](WOApplication-2.md) object first sends this message, passing in a newly-created WOResponse object as an argument. [WOElement](WOElement-2.md) objects, which represent the dynamic and static HTML elements on a page, respond to the message by appending their HTML representation to the content of the WOResponse object. WOApplication, [WOSession](WOSession-2.md), and [WOComponent](WOComponent-2.md) objects can also respond to the message by adding information to the WOResponse object.

A WOResponse has two major parts: HTML content and HTTP information. The content is what is displayed in a Web browser; it can include _escaped_ HTML, which is HTML code shown "as is," uninterpreted. The other information encapsulated by a WOResponse object is in the handling the response. This HTTP data includes headers, status codes, and version string. See the HTTP specification or HTTP documentation for descriptions of these items.

As you might expect, the methods of the WOResponse class can be divided into two groups, those that add to a response's HTML content and those that read and set HTTP information. The former group consists of methods that escape HTML ([__appendContentHTMLAttributeValue:__](#apple-g4ya) and [__appendContentHTMLString:__](#apple-g42a)) and those that don't. For images and other binary data, you can use the [__appendContentData:__](#apple-gy3a). You can obtain and set the entire content of the response with [__content__](#apple-haza) and [__setContent:__](#apple-gezde). The following example shows a sequence of "appendContent" messages that compose an HTTP "POST" message:

> ```
> [aResponse appendContentString:@"&ltform method=\"POST\" action=\""];
> ```

> ```
> [aResponse appendContentHTMLAttributeValue:[aContext url]];
> ```

> ```
> [aResponse appendContentCharacter:'"'];
> ```

> ```
> [aResponse.appendContentString:@"&gt"];
> ```

Most of the remaining WOResponse methods set and read the response's HTTP headers, the HTTP status code, and the HTTP version.

---

### Content Encodings

You can set the string encoding used for the response content with [__setContentEncoding:__](#apple-gezdm) and you find out what the current encoding is with [__contentEncoding__](#apple-gu3dony). An integer represents the type of encoding. The following table lists these integer values along with their OPENSTEP string-constant names.

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

# Adopted Protocols

**NSCopying**

**- copy

**- copyWithZone:****

**WOActionResults**

**[- generateResponse](#apple-ge3dgnry)**

---

## Method Types

**Creation**

**[- init](#apple-ge3dkmzs)**

**Obtaining attributes**

**[+ defaultEncoding](#apple-gqzdiny)

**[- content](#apple-haza)

**[- headerForKey:](#apple-he4a)

**[- headerKeys](#apple-geyde)

**[- headersForKey:](#apple-geydm)

**[- httpVersion](#apple-geyta)

**[- status](#apple-gmztgoa)

**[- userInfo](#apple-ge2ti)****************

**Setting attributes**

**[+ setDefaultEncoding:](#apple-gqzdkna)

**[- setContent:](#apple-gezde)

**[- setHeader:forKey:](#apple-gezti)

**[- setHeaders:forKey:](#apple-geztq)

**[- setHTTPVersion:](#apple-gezta)

**[- setStatus:](#apple-ge2de)

**[- setUserInfo:](#apple-ge2dm)**************

**Appending response content**

**[- appendContentBytes:length:](#apple-ge3dcnjr)

**[- appendContentCharacter:](#apple-gqzdqmi)

**[- appendContentData:](#apple-gy3a)

**[- appendContentString:](#apple-g44a)

**[- setContentEncoding:](#apple-gezdm)

**[- contentEncoding](#apple-gu3dony)************

**Working with HTML content**

**[- appendContentHTMLAttributeValue:](#apple-g4ya)

**[- appendContentHTMLString:](#apple-g42a)

**[+ stringByEscapingHTMLString:](#apple-gu2deoi)

**[+ stringByEscapingHTMLAttributeValue:](#apple-gu2dimi)********

**Working with cookies**

**[- addCookie:](#apple-he4tq)

**[- cookies](#apple-heya)

**[- removeCookie:](#apple-geytq)******

---

## Class Methods

---

### defaultEncoding

+ (NSStringEncoding)__defaultEncoding__

Returns the default character encoding used to construct a new WOResponse. By default, this encoding is NSISOLatin1. For more information, see ["Content Encodings"](#apple-geydgnq).

---

### setDefaultEncoding:

+ (void)__setDefaultEncoding:__ (NSStringEncoding)_aStringEncoding_

Lets you specify the character encoding used by default when construcing a new WOResponse. For more information, see ["Content Encodings"](#apple-geydgnq).

---

### stringByEscapingHTMLString:

+ (NSString \*)__stringByEscapingHTMLString:__ (NSString \*)_aString_

This method takes a string and, if escaping is required, returns a new string with certain characters escaped out. If escaping is not required, no conversion is performed and _aString_ is returned. Use this method to escape strings which will appear in the visible part of an HTML file (that is, not inside a tag). The escaped characters are:

| & | &amp; |
| " | &quot; |
| < | &lt; |
| > | &gt; |

```
```


---

### stringByEscapingHTMLAttributeValue:

+ (NSString \*)__stringByEscapingHTMLAttributeValue:__ (NSString \*)_aString_

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

### addCookie:

- (void)__addCookie:__ (WOCookie \*)_aCookie_

Adds the specified WOCookie object to the response.

__See also:__
[- __cookies__](#apple-heya), [- __removeCookie:__](#apple-geytq), [WOCookie](WOCookie-2.md) class specification

---

### appendContentBytes:length:

- (void)__appendContentBytes:__ (const void \*)_someBytes_ __length:__ (unsigned)_length_

Appends _length_ number of bytes pointed to by _someBytes_ to the HTTP response.

---

### appendContentCharacter:

- (void)__appendContentCharacter:__ (char)_aChar_

Appends a single ASCII character (_aChar_) to the HTTP response.

Example:

> ```
> // ...
> ```

> ```
> if (aFlag)
> ```

> ```
> 	[aResponse appendContentCharacter:'Y'];
> ```

> ```
> else
> ```

> ```
> 	[aResponse appendContentCharacter:'N'];
> ```

---

### appendContentData:

- (void)__appendContentData:__ (NSData \*)_dataObject_

Appends a data-encapsulating object (_dataObject_) to the HTTP response.

---

### appendContentHTMLAttributeValue:

- (void)__appendContentHTMLAttributeValue:__ (NSString \*)_aValue_

Appends an HTML attribute value to the HTTP content after transforming the string _aValue_ into an NSData object using the receiver's content encoding. Special HTML characters ("<", ">", "&", and double quote) are _escaped_ so that the browser does not interpret them. In other words, the message

> ```
> [aResponse appendContentHTMLAttributeValue:@"<B>"];
> ```

would transform the argument to "<B>".

__See also:__
__[- setContentEncoding:](#apple-gezdm)__

---

### appendContentHTMLString:

- (void)__appendContentHTMLString:__ (NSString \*)_aString_

Appends an HTML string to the HTTP response after transforming the string _aString_ into an NSData object using the receiver's content encoding. Special HTML characters ("<", ">", "&", and double quote) are _escaped_ so that the browser does not interpret them. For example, "<P>" becomes "&ltP&gt".

__See also:__
__[- setContentEncoding:](#apple-gezdm)__

---

### appendContentString:

- (void)__appendContentString:__ (NSString \*)_aString_

Appends a string to the content of the HTTP response. The string is transformed into an NSData object using the receiver's content encoding. The special HTML characters "<", ">", "&", and double-quote are not escaped so the browser can interpret them as HTML.

---

### content

- (NSData \*)__content__

Returns the HTML content of the receiver as an NSData object.

An exception is raised if you attempt to get the content when all elements of the page have not had their chance to append HTML to the response. Thus, you should invoke this method in the application object's __handleRequest:__  method, after super's __handleRequest:__  has been invoked. (For scripted applications, __handleRequest:__  is implemented in Application.wos). Note that at this point in the request-handling process, the components, pages, and session have already been put to sleep, so you won't have access to any context, session, or page information. If you need such information for your response, store it somewhere--such as in WOResponse's "user info" dictionary-at a point when you do have access to it. You may want to do this in your application's __[appendToResponse:inContext:](WOApplication-2.md#apple-g43tama)__  method, for example.

__See also:__
[- __setContent:__](#apple-gezde), __[- setContentEncoding:](#apple-gezdm)__

---

### contentEncoding

- (NSStringEncoding)__contentEncoding__

Returns an integer representing the encoding used for the response content. See ["Content Encodings"](#apple-geydgnq) in the class description for a mapped list of supported encodings and their Objective-C names. Usually, you will want the response encoding to be the same as that used by the submitting form on the client browser. In this case it is preferable to use WORequest's [__formValueEncoding__](WORequest-2.md#apple-g44q).

> ```
> NSStringEncoding theEncoding = [[aContext request] formValueEncoding];
> ```

The default string encoding is ISO Latin1.

__See also:__
[- __setContent:__](#apple-gezde), __[- setContentEncoding:](#apple-gezdm)__

---

### cookies

- (NSArray \*)__cookies__

Returns an array of WOCookie objects to be included in the response.

__See also:__
[- __addCookie:__](#apple-he4tq), [- __removeCookie:__](#apple-geytq), [WOCookie](WOCookie-2.md) class specification

---

### generateResponse

- (WOResponse \*)__generateResponse__

Returns a WOResponse object. WOResponse's implementation simply returns itself.

__See also:__
[- __generateResponse__](WOComponent-2.md#apple-he3q) (WOComponent)

---

### headerForKey:

- (NSString \*)__headerForKey:__ (NSString \*)_aKey_

Returns the HTTP header information identified by _aKey_. If there are multiple headers associated with the one key, only the first one is returned. Returns __nil__  if there are no headers for the key.

__See also:__
__[- setHeader:forKey:](#apple-gezti)__

---

### headerKeys

- (NSArray \*)__headerKeys__

Returns an array of string keys associated with the receiver's HTTP headers. Returns __nil__  if there are no headers. You could easily test to see if a header is included by doing something similar to this:

> ```
> NSArray *hKeys =  [aResponse headerKeys];
> ```

> ```
> if ([hKeys containsObject:@"expires"]) {
> ```

> ```
> 	// do something
> ```

> ```
> }
> ```

__See also:__
__[- setHeaders:forKey:](#apple-geztq)__

---

### headersForKey:

- (NSArray \*)__headersForKey:__ (NSString \*)_aKey_

Returns _all_ HTTP headers identified by _aKey_.

__See also:__
__[- setHeaders:forKey:](#apple-geztq)__

---

### httpVersion

- (NSString \*)__httpVersion__

Returns the version of HTTP used for the response (for example, "HTTP/1.0").

__See also:__
__[- setHTTPVersion:](#apple-gezta)__

---

### init

- (id)__init__

Initializes a WOResponse instance. HTTP status is set to 200 (OK), client caching is enabled, and the default string encoding is made ISO Latin 1.

---

### removeCookie:

- (void)__removeCookie:__ (WOCookie \*)_aCookie_

Removes the specified WOCookie object from the response.

__See also:__
[- __cookies__](#apple-heya), [- __removeCookie:__](#apple-geytq), [WOCookie](WOCookie-2.md) class specification

---

### setContent:

- (void)__setContent:__ (NSData \*)_someData_

Sets the HTML content of the HTTP response to _someData_.

__See also:__
__[- content](#apple-haza)__

---

### setContentEncoding:

- (void)__setContentEncoding:__ (NSStringEncoding)_anEncoding_

Sets the encoding used for the content of the HTTP response. See ["Content Encodings"](#apple-geydgnq) in the class description for a mapped list of supported encodings and their Objective-C names. The default string encoding is ISO Latin1.

__See also:__
__[- contentEncoding](#apple-gu3dony)__

---

### setHTTPVersion:

- (void)__setHTTPVersion:__ (NSString \*)_aVersion_

Sets the version of HTTP used for the response (for example, "HTTP/1.0").

__See also:__
__[- httpVersion](#apple-geyta)__

---

### setHeader:forKey:

- (void)__setHeader:__ (NSString \*)_aHeader_ __forKey:__ (NSString \*)_aKey_

Sets the HTTP header _aHeader_ in the receiver and associates, for retrieval, the HTTP key _aKey_ with the header. This method is commonly used to set the type of content in a response, for example:

> ```
> [aResponse setHeader:@"text/html" forKey:@"content-type"];
> ```

__See also:__
__[- headerForKey:](#apple-he4a)__

---

### setHeaders:forKey:

- (void)__setHeaders:__ (NSArray \*)_headerList_ __forKey:__ (NSString \*)_aKey_

Sets the list of HTTP headers _headerList_ in the receiver and associates, for retrieval, the HTTP key _aKey_ with the list of header elements.

__See also:__
[- __headerKeys__](#apple-geyde), `[-](#apple-geydm)`__headersForKey:__

---

### setStatus:

- (void)__setStatus:__ (unsigned int)_anInt_

Sets the HTTP status to _anInt_. Consult the HTTP specification or HTTP documentation for the significance of status integers.

__See also:__
__[- status](#apple-gmztgoa)__

---

### setUserInfo:

- (void)__setUserInfo:__ (NSDictionary \*)_aDictionary_

Sets a dictionary in the WOResponse object that, as a convenience, can contain any kind of information related to the current response. Objects further down the __[appendToResponse:inContext:](WOApplication-2.md#apple-g43tama)__  message "chain" can retrieve this information using [__userInfo__](#apple-ge2ti).

---

### status

- (unsigned int)__status__

Returns an integer code representing the HTTP status. Consult the HTTP specification or HTTP documentation for the significance of these status codes.

By default, the status is 200 ("OK" status).

__See also:__
__[- setStatus:](#apple-ge2de)__

---

### userInfo

- (NSDictionary \*)__userInfo__

Returns a dictionary that, as a convenience, can contain any kind of information related to the current response. An object further "upstream" in the __[appendToResponse:inContext:](WOApplication-2.md#apple-g43tama)__  message "chain" can set this dictionary in the WOResponse object as a way to pass information to other objects.

__See also:__
__[- setUserInfo:](#apple-ge2dm)__

****

---

[!](WOResourceManager-2.md)
[!](WOSession-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
