---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/XML/Classes/WOXMLException.html
archived_at: '2026-07-15T08:14:47.301939Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/XML/Art/up.gif)](../XMLTOC.md) 

# WOXMLException

> __Inherits from:__ com.webobjects.foundation.NSForwardException

> __Package:__ com.webobjects.appserver.xml

---

## Class Description

---

This class serves solely to wrap a number of exceptions that can arise during the parsing process, reducing the number of exceptions your code has to catch. In particular, exceptions that are thrown by the SAX parser are encapsulated in WOXMLException objects by [WOXMLException](#apple-k5hug33oorsxq5a) and then re-thrown.

The WOXMLException class encapsulates both an exception and an optional text string that can be retrieved with [getMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyrlymnsxa5djn5xc6z3forgwk43tmftwk) (this message is also prepended to the text that is returned from [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyrlymnsxa5djn5xc65dpkn2he2lom4)).

## Constructors

---

### WOXMLException

`public WOXMLException(String optionalMessage)`

`public WOXMLException(Throwable anException)`

`public WOXMLException(Throwable anException, String optionalMessage)`

Creates and returns a new WOXMLException object. If _optionalMessage_ is included, the message text can later be retrieved with [getMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyrlymnsxa5djn5xc6z3forgwk43tmftwk) and is prepended to the string returned from [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2plbguyrlymnsxa5djn5xc65dpkn2he2lom4). If _anException_ is supplied, the string returned by __toString__ lists (among other things) _anException_'s class.

---

## Instance Methods

---

### getMessage

`public String getMessage()`

Returns the optional message supplied when the WOXMLException was created, followed by any optional message from the encapsulated exception.

---

### toString

`public String toString()`

Returns a string representation of the WOXMLException object, including the _optionalMessage_ (if one was supplied when the WOXMLException was created) and the name of the encapsulated exception.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/Reference/XML/Art/up.gif)](../XMLTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
