---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WOMessage.html
archived_at: '2026-07-15T08:15:15.677261Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WOMessage

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.appserver

---

## Class Description

---

WOMessage is the parent class for both WORequest and [WOMessage](#apple-k5hvezltobxw443f),and implements much of the behavior that is generic to both. WOMessage represents a message with an HTTP header and either HTML or XML content. HTML content is typically used when interacting with a Web browser, while XML content can be used in messages that originate from or are destined for another application (either an application that "speaks" XML or another WebObjects application).

The methods of the WOMessage class can be divided primarily into two groups, those that deal with a message's content and those that read and set header information. Most of the remaining WOMessage methods control how the content is encoded and allow you to attach arbitrary "user info" to your WOMessage objects in order to pass information about a given message to other objects within your application.

|  |
| --- |
| __Note:__ Headers are case-insensitive. WebObjects enforces the HTTP specification, but avoid mixing the case of header keys. See the HTTP specification or HTTP documentation for more information on the HTTP headers and version. |

## Content Encodings

You can set the string encoding used for the response content with [setContentEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643forbw63tumvxhirlomnxwi2lom4) and you find out what the current encoding is with [contentEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6y3pnz2gk3tuivxgg33enfxgo). An integer represents the type of encoding. The following table lists these integer values along with their WebObjects string-constant names.

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

## Messages with XML Content

The WOMessage class contains three methods that allow you to construct and interpret messages whose content is formatted as XML. [appendContentDOMDocumentFragment](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6ylqobsw4zcdn5xhizloorce6tken5rxk3lfnz2em4tbm5wwk3tu) allows you to build up an XML message piece by piece. [setContentDOMDocument](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643forbw63tumvxhircpjvcg6y3vnvsw45a), on the other hand, allows you to specify the message's content all at once. To obtain the content of a message that is formatted as XML, use [contentAsDOMDocument](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6y3pnz2gk3tuifzuit2nirxwg5lnmvxhi).

The arguments to these methods are XML documents (or, in the case of __appendContentDOMDocumentFragment__, a document fragment) as defined by the Document Object Model (DOM). Installed as a part of WebObjects is the com.ibm.xml.dom package (IBM's alphaWorks), which contains various XML parsers for Java written by IBM. The included DOM parser is used to generate document and document fragment objects from XML data (or to manipulate and/or generate XML data from a document object). For more information on the Document Object Model, see the online documentation at http://www.w3.org/DOM/.

## Constants

---

WOMessage declares these constants:

|  |  |
| --- | --- |
| __API__ | __Description__ |
| TheDefaultResponseEncoding | This protected class variable contains a String identifying the default encoding to use when constructing responses (which is defined in WOMessage to be ISOLatin1). |
| HTTP_STATUS_OK | This constant contains an integer value (200) corresponding to the HTTP 1.1 status code for "OK". |
| HTTP_STATUS_NO_CONTENT | This constant contains an integer value (204) corresponding to the HTTP 1.1 status code for "No content". |
| HTTP_STATUS_MOVED_PERMANENTLY | This constant contains an integer value (301) corresponding to the HTTP 1.1 status code for "Moved permanently". |
| HTTP_STATUS_FOUND | This constant contains an integer value (302) corresponding to the HTTP 1.1 status code for "Found". |
| HTTP_STATUS_FORBIDDEN | This constant contains an integer value (403) corresponding to the HTTP 1.1 status code for "Forbidden". |
| HTTP_STATUS_NOT_FOUND | This constant contains an integer value (404) corresponding to the HTTP 1.1 status code for "Not found". |

## Method Types

---

> **Creation**
> : [WOMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6v2pjvsxg43bm5sq)
>
> **Working with message headers**
> : [appendHeader](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6ylqobsw4zcimvqwizls): [appendHeaders](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6ylqobsw4zcimvqwizlsom): [headerForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss62dfmfsgk4sgn5zewzlz): [headerKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss62dfmfsgk4slmv4xg): [headers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss62dfmfsgk4tt): [headersForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss62dfmfsgk4ttizxxes3fpe): [httpVersion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss62duoryfmzlsonuw63q): [removeHeadersForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss64tfnvxxmzkimvqwizlsondg64slmv4q): [setHeader](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643foregkylemvza): [setHeaders](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643foregkylemvzhg): [setHTTPVersion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643forefivcqkzsxe43jn5xa)
>
> **Working with message content**
> : [addCookie](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6ylemrbw633lnfsq): [appendContentCharacter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6ylqobsw4zcdn5xhizloorbwqylsmfrxizls): [appendContentData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6ylqobsw4zcdn5xhizloorcgc5db): [appendContentHTMLString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6ylqobsw4zcdn5xhizloorefitkmkn2he2lom4): [appendContentHTMLAttributeValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6ylqobsw4zcdn5xhizloorefitkmif2hi4tjmj2xizkwmfwhkzi): [appendContentString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6ylqobsw4zcdn5xhizloorjxi4tjnztq): [appendContentDOMDocumentFragment](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6ylqobsw4zcdn5xhizloorce6tken5rxk3lfnz2em4tbm5wwk3tu): [content](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6y3pnz2gk3tu): [contentAsDOMDocument](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6y3pnz2gk3tuifzuit2nirxwg5lnmvxhi): [contentString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6y3pnz2gk3tukn2he2lom4): [cookies](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6y3pn5vwszlt): [removeCookie](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss64tfnvxxmzkdn5xww2lf): [setContent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643forbw63tumvxhi): [setContentDOMDocument](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643forbw63tumvxhircpjvcg6y3vnvsw45a): [setHeaders](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643foregkylemvzhg): [stringByEscapingHTMLAttributeValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6tlfonzwcz3ff5zxi4tjnztue6kfonrwc4djnztuqvcnjraxi5dsnfrhk5dfkzqwy5lf): [stringByEscapingHTMLString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6tlfonzwcz3ff5zxi4tjnztue6kfonrwc4djnztuqvcnjrjxi4tjnztq)
>
> **Controlling content encoding**
> : [defaultEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6tlfonzwcz3ff5sgkztbovwhirlomnxwi2lom4): [setDefaultEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6tlfonzwcz3ff5zwk5cemvtgc5lmorcw4y3pmruw4zy): [contentEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6y3pnz2gk3tuivxgg33enfxgo): [setContentEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643forbw63tumvxhirlomnxwi2lom4)
>
> **Working with user info**
> : [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643forkxgzlsjfxgm3y): [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss65ltmvzes3tgn4)

## Constructors

---

### WOMessage

`public WOMessage()`

Returns an initialized WOMessage instance. The default string encoding is set to ISO Latin 1.

---

## Static Methods

---

### defaultEncoding

`public static String defaultEncoding()`

Returns the default character encoding used to construct a new WOMessage which initially is NSISOLatin1. For more information, see ["Content Encodings"](#apple-ijeeoqskivcee).

---

### requiresHTMLEscaping

`protected static boolean requiresHTMLEscaping( String aString, char[] charactersString)`

This protected class method takes a String and an array of characters and returns `true` if any of the characters in the character array are found in the String.

---

### setDefaultEncoding

`public static void setDefaultEncoding(String aStringEncoding)`

Lets you specify the character encoding to be used by default when construcing a new WOMessage. For more information, see ["Content Encodings"](#apple-ijeeoqskivcee).

---

### stringByEscapingHTMLAttributeValue

`public static String stringByEscapingHTMLAttributeValue(String aString)`

This class method takes a string and, if escaping is required, returns a new string with certain characters escaped out. If escaping is not required, no conversion is performed and the original string is returned. Use this method to escape strings which will appear as attribute values of a tag. The escaped characters are: "<", ">", "&", "\t", "\n", "\r", and double quote.

---

### __stringByEscapingHTMLString__

`public static String stringByEscapingHTMLString(String aString)`

This class method takes a string and, if escaping is required, returns a new string with certain characters escaped out. If escaping is not required, no conversion is performed and the original string is returned. Use this method to escape strings which will appear in the visible part of an HTML file (that is, not inside a tag). The escaped characters are: "<", ">", "&", and double quote.

---

## Instance Methods

---

### addCookie

`public void addCookie(WOCookie aCookie)`

A convenience method that adds the specified WOCookie object to the message content.

__See Also:__ [cookies](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6y3pn5vwszlt), [removeCookie](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss64tfnvxxmzkdn5xww2lf), WOCookie class specification

---

### appendContentCharacter

`public void appendContentCharacter(char aChar)`

Appends a single ASCII character (_aChar_) to the message's contents.

---

### appendContentData

`public void appendContentData(NSData dataObject)`

Appends a data-encapsulating object (_dataObject_) to the message's contents.

---

### appendContentHTMLAttributeValue

`public void appendContentHTMLAttributeValue(String aString)`

Appends an HTML attribute value (passed in as a String) to the HTTP content after transforming the string argument into an NSData object using the receiver's content encoding. Special HTML characters ("<", ">", "&", "\t", "\n", "\r", and double quote) are escaped so that the browser does not interpret them.

---

### appendContentHTMLString

`public void appendContentHTMLString(String aString)`

Appends an HTML string (passed in as a parameter) to the HTTP response after transforming the string paramenter into an NSData object using the receiver's content encoding. Special HTML characters ("<", ">", "&", and double quote) are escaped so that the browser does not interpret them.

---

### appendContentString

`public void appendContentString(String aString)`

Appends a string to the content of the message's contents. The string is transformed into an NSData object using the receiver's content encoding. The special HTML characters "<", ">", "&", and double-quote are not escaped so a browser can interpret them as HTML.

---

### appendContentDOMDocumentFragment

`public void appendContentDOMDocumentFragment( org.w3c.dom.DocumentFragment aDocumentFragment)`

Converts the supplied DOM document fragment to an XML string and appends it to the message's contents.

__See Also:__ [contentAsDOMDocument](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6y3pnz2gk3tuifzuit2nirxwg5lnmvxhi), [setContentDOMDocument](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643forbw63tumvxhircpjvcg6y3vnvsw45a), [Messages with XML Content](#apple-ijdumq2eivdeq)

---

### appendHeader

`public void appendHeader( String header, String aKey)`

Appends _header_ to the list of HTTP headers in the receiver and associates, for retrieval, the HTTP key _aKey_ with the new header. If a header list doesn't already exist for the receiver, one is created before the new header is appended.

__See Also:__ [headerKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss62dfmfsgk4slmv4xg), [headersForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss62dfmfsgk4ttizxxes3fpe), [setHeaders](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643foregkylemvzhg)

---

### appendHeaders

`public void appendHeaders( NSArray headerList, String aKey)`

Appends _headerList_ to the list of HTTP headers in the receiver and associates, for retrieval, the HTTP key _aKey_ with the list of header elements. If a header list doesn't already exist for the receiver, one is created before the list of headers is appended.

__See Also:__ [headerKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss62dfmfsgk4slmv4xg), [headersForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss62dfmfsgk4ttizxxes3fpe), [setHeaders](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643foregkylemvzhg)

---

### __clone__

`public Object clone()`

Returns a new object that is a copy of the receiver.

---

### content

`public NSData content()`

Returns the HTML content of the receiver as an NSData object.

An exception is raised if you attempt to get the content when all elements of the page have not had their chance to append HTML to the response. Thus, you should invoke this method in the application object's __handleRequest:__ method, after super's __handleRequest:__ has been invoked. (For scripted applications, __handleRequest:__ is implemented in Application.wos). Note that at this point in the request-handling process, the components, pages, and session have already been put to sleep, so you won't have access to any context, session, or page information. If you need such information for your response, store it somewhere--such as in WOMessage's "user info" dictionary-at a point when you do have access to it. You may want to do this in your application's appendToResponse method, for example.

__See Also:__ [setContent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643forbw63tumvxhi), [setContentEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643forbw63tumvxhirlomnxwi2lom4)

---

### contentAsDOMDocument

`public org.w3c.dom.Document contentAsDOMDocument() throws WODOMParserException`

Returns the content of the receiver as a DOM document object. Throws a DOMParserException if the DOM parser throws an exception.

__See Also:__ [appendContentDOMDocumentFragment](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6ylqobsw4zcdn5xhizloorce6tken5rxk3lfnz2em4tbm5wwk3tu), [setContentDOMDocument](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643forbw63tumvxhircpjvcg6y3vnvsw45a)

---

### contentEncoding

`public String contentEncoding()`

Returns a String representing the encoding used for the message's content. See ["Content Encodings"](#apple-ijeeoqskivcee) in the class description for a mapped list of supported encodings and their WebObjects names. For responses, you will want the response encoding to be the same as that used by the submitting form on the client browser. In this case it is preferable to use WORequest's formValueEncoding.

The default string encoding is ISO Latin1.

__See Also:__ [setContent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643forbw63tumvxhi), [setContentEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643forbw63tumvxhirlomnxwi2lom4)

---

### __contentString__

`public String contentString()`

Returns the content of the receiver as a String object.

---

### cookies

`public NSArray cookies()`

A convenience method that returns an array of WOCookie objects to be included in the message (which is uaually a [WOMessage](#apple-k5hvezltobxw443f)).

__See Also:__ [addCookie](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6ylemrbw633lnfsq), [removeCookie](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss64tfnvxxmzkdn5xww2lf), WOCookie class specification

---

### equals

`public boolean equals(Object aMessage)`

Inherited from java.lang.Object. Returns `true` if the supplied Object is a WOMessage (or a subclass) whose headers and content equal those of the receiver.

---

### headerForKey

`public String headerForKey(Object aKey)`

Returns the HTTP header information identified by _aKey_. If there are multiple headers associated with the one key, only the first one is returned. Returns `null` if the message has no headers for the key.

__See Also:__ [setHeader](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643foregkylemvza)

---

### headerKeys

`public NSArray headerKeys()`

Returns an array of string keys associated with the receiver's HTTP headers. Returns `null` if there are no headers. You could easily test to see if a header is included by doing something similar to this:
> ```
> ImmutableVector hKeys =  aMessage.headerKeys();
>     if (hKeys.contains("expires")) {
>         // do something
>     }
> ```

__See Also:__ [setHeaders](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643foregkylemvzhg)

---

### headers

`public NSDictionary headers()`

Returns the header dictionary with which the message was initialized.

---

### headersForKey

`public NSArray headersForKey(Object aKey)`

Returns _all_ HTTP headers identified by _aKey_.

__See Also:__ [setHeaders](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643foregkylemvzhg)

---

### httpVersion

`public String httpVersion()`

Returns the version of HTTP used for the message (for example, "HTTP/1.0").

__See Also:__ [setHTTPVersion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643forefivcqkzsxe43jn5xa)

---

### removeCookie

`public void removeCookie(WOCookie aCookie)`

A convenience method that removes the specified WOCookie object from the message.

__See Also:__ [cookies](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6y3pn5vwszlt), [removeCookie](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss64tfnvxxmzkdn5xww2lf), WOCookie class specification

---

### removeHeadersForKey

`public void removeHeadersForKey(Object aKey)`

Removes those headers from the receiver that correspond to the specified key.

---

### setContent

`public void setContent(NSData someData)`

Sets the message contents to _someData_.

`public void setContent(char[] someContent)`

Sets the message contents to the contents of the supplied character array.

`public void setContent(String someContent)`

Sets the message contents to the contents of the supplied String object.

__See Also:__ [content](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6y3pnz2gk3tu)

---

### setContentDOMDocument

`public void setContentDOMDocument(org.w3c.dom.Document aDocument)`

Sets the XML content of the response to the DOM document _aDocument_.

__See Also:__ [appendContentDOMDocumentFragment](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6ylqobsw4zcdn5xhizloorce6tken5rxk3lfnz2em4tbm5wwk3tu), [contentAsDOMDocument](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6y3pnz2gk3tuifzuit2nirxwg5lnmvxhi)

---

### setContentEncoding

`public void setContentEncoding(String anEncoding)`

Sets the encoding used for the message contents. See ["Content Encodings"](#apple-ijeeoqskivcee) in the class description for a mapped list of supported encodings and their WebObjects names. The default string encoding is ISO Latin1.

__See Also:__ [contentEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6y3pnz2gk3tuivxgg33enfxgo)

---

### setHTTPVersion

`public void setHTTPVersion(String aVersion)`

Sets the version of HTTP used for the message (for example, "HTTP/1.0").

__See Also:__ [httpVersion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss62duoryfmzlsonuw63q)

---

### setHeader

`public void setHeader( String aHeader, String aKey)`

Sets the HTTP header in the receiver to _aHeader_ and associates, for retrieval, the HTTP key _aKey_ with the header. This method is commonly used to set the type of content in a response, for example:
> ```
> aResponse.setHeader("text/html", "content-type");
> ```

__See Also:__ [headerForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss62dfmfsgk4sgn5zewzlz)

---

### setHeaders

`public void setHeaders( NSArray headerList, String aKey)`

Sets the HTTP header in the receiver to _headerList_ and associates, for retrieval, the HTTP key _aKey_ with the list of header elements.

`public void setHeaders(NSDictionary headerDictionary)`

Sets the list of HTTP headers in the receiver to the contents of the supplied NSDictionary object.

__See Also:__ [appendHeaders](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss6ylqobsw4zcimvqwizlsom), [headerKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss62dfmfsgk4slmv4xg), [headersForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss62dfmfsgk4ttizxxes3fpe)

---

### setUserInfo

`public void setUserInfo(NSDictionary aDictionary)`

Sets a dictionary in the WOMessage object that, as a convenience, can contain any kind of information related to the current response. Objects further down the appendToResponse message "chain" can retrieve this information using [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss65ltmvzes3tgn4).

---

### __toString__

`public String toString()`

Returns a String representation of the receiver. This string representation is suitable for debugging-it details many of the WOMessage object's attributes-and should not be confused with the __contentString()__ method.

---

### userInfo

`public NSDictionary userInfo()`

Returns a dictionary that, as a convenience, can contain any kind of information related to the current response. An object further "upstream" in the appendToResponse message "chain" can set this dictionary in the WOMessage object as a way to pass information to other objects.

__See Also:__ [setUserInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvsxg43bm5ss643forkxgzlsjfxgm3y)

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
