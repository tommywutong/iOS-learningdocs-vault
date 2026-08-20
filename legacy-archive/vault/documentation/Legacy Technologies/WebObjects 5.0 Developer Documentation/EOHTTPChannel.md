---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EODistributionRef/Java/Client/Classes/EOHTTPChannel.html
archived_at: '2026-07-15T08:13:48.609420Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EODistributionRef/Java/Client/Art/up.gif)](../../EODistributionTOC.md) 

# EOHTTPChannel

> **__Inherits from:__**
> : [EODistributionChannel](EODistributionChannel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhui2ltorzgsytvoruw63sdnbqw43tfnq): Object

> **__Package:__**
> : com.webobjects.eodistribution.client

---

## Class Description

---

An EOHTTPChannel is an object that handles communication between the client and server in distributed enterprise-objects applications using the HTTP protocol. It is commonly used in WebObjects applications that employ an Enterprise Object Java client. EOHTTPChannel is concrete subclass of EODistributionChannel.

An EODistributedObjectStore manages the flow of data over the EOHTTPChannel. It sends data from the client to the server by invoking EOHTTPChannel's [responseToMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjbkfiucdnbqw43tfnqxxezltobxw443fkrxu2zltonqwozi) message, which uses an HTTP "POST" command. Communication from the server is handled through notifications "piggybacked" onto the response.

## Constants

---

EOHTTPChannel defines the following String constants as connection keys (for more information, see [connectionKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjbkfiucdnbqw43tfnqxwg33onzswg5djn5xewzlzom)):

- ApplicationURLKey
- ComponentURLKey
- SessionIDKey
- PageKey

## Instance Methods

---

### connectionKeys

`public NSArray connectionKeys()`

Returns the keys to the connection dictionary used by the receiver. The default keys for EOHTTPChannel are the following constants:

|  |  |
| --- | --- |
| __Key__ | __Value__ |
| ApplicationURLKey | The application's base URL, specifying where your application's resources are located under the web server's document root. |
| ComponentURLKey | The URL identifying a particular Java client side component. |
| SessionIDKey | The session ID for the current session. |
| PageKey | The name of the page component involved in the current transaction. |

---

### establishConnection

`public void establishConnection()`

Establishes a connection with the server and begins communication using the HTTP protocol. Prior to establishing the connection, the method sets the requisite host, port, and URL information using the information in the connection dictionary. Throws an NSForwardException if a native IOException or a MalformedURLException occurs; also throws an IllegalArgumentException if required information is missing from the connection dictionary.

---

### responseToMessage

`public Object responseToMessage( Object aMessage, NSCoder aCoder)`

Sends the message _aMessage_ from the client to the server using the HTTP "POST" command; the message is encoded before it is sent using _aCoder_. Synchronously receives, decodes, and returns the response to the message.

Throws a RuntimeException if the method is re-entered or an NSForwardException if any native exception related to socket-creation or I/O occurs.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/EODistributionRef/Java/Client/Art/up.gif)](../../EODistributionTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
