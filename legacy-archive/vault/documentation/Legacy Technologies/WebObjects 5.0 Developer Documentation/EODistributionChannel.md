---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EODistributionRef/Java/Client/Classes/EODistributionChannel.html
archived_at: '2026-07-15T08:13:48.588930Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EODistributionRef/Java/Client/Art/up.gif)](../../EODistributionTOC.md) 

# EODistributionChannel

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.eodistribution.client

---

## Class Description

---

EODistributionChannel is an abstract class that defines the interface for objects implementing channels for communicating data between the client and the server in a distributed Enterprise Objects application. The com.apple.client.eodistribution package includes EOHTTPChannel, a concrete subclass of EODistributionChannel that handles communication via the HTTP protocol (the most common protocol in distributed Internet applications). You can create you own subclass of EODistributionChannel if you need client-server communication based on a different protocol such as CORBA/IIOP.

An EODistributionChannel object has a __connection dictionary__ that contains the values required to establish a connection on the channel, for example port, host, and URL components. You can change the connection dictionary with the [setConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg2dbnzxgk3bponsxiq3pnzxgky3unfxw4rdjmn2gs33omfzhs) method.

: ## Method Types

---

> **Getting an EODistributionChannel**
>
> : [channelWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rdjon2he2lcov2gs33oinugc3tomvwc6y3imfxg4zlmk5uxi2comfwwk)
>
> **Sending data on the channel**
>
> : [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg2dbnzxgk3bpmvzxiylcnruxg2cdn5xg4zldoruw63q): [responseToMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg2dbnzxgk3bpojsxg4dpnzzwkvdpjvsxg43bm5sq)
>
> **Setting and getting the connection dictionary**
>
> : [connectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg2dbnzxgk3bpmnxw43tfmn2gs33oiruwg5djn5xgc4tz): [connectionKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg2dbnzxgk3bpmnxw43tfmn2gs33ojnsxs4y): [setConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg2dbnzxgk3bponsxiq3pnzxgky3unfxw4rdjmn2gs33omfzhs)
>
> :
>
> **Accessing the delegate**
>
> : [delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg2dbnzxgk3bpmrswyzlhmf2gk): [setDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg2dbnzxgk3bponsxirdfnrswoylumu)

## Static Methods

---

### channelWithName

`public static EODistributionChannel channelWithName(String className)`

Returns an EODistributionChannel object instantiated from the class whose name is _className_. Returns __null__ if there is no class with that name, or if there is an instantiation, illegal-access, or security exception.

---

## Instance Methods

---

### connectionDictionary

`public NSDictionary connectionDictionary()`

Returns the connection dictionary used by the receiver.

---

### connectionKeys

`public abstract NSArray connectionKeys()`

Overridden by subclasses to return the set of keys used to access the values in the connection dictionary that the channel needs to connect with the server.

---

### delegate

`public Object delegate()`

Returns the receiver's delegate.

---

### establishConnection

`public abstract void establishConnection()`

Overridden by subclasses to establish a connection with the server using a specific protocol.

__See Also:__ [responseToMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg2dbnzxgk3bpojsxg4dpnzzwkvdpjvsxg43bm5sq)

---

### responseToMessage

`public abstract Object responseToMessage( Object aMessage, NSCoder aCoder)`

Overridden by subclasses to send the message _aMessage_ to the server and synchronously receive a response. Before it is sent the message should be encoded using _aCoder_.

__See Also:__ [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg2dbnzxgk3bpmvzxiylcnruxg2cdn5xg4zldoruw63q)

---

### setConnectionDictionary

`public void setConnectionDictionary(NSDictionary aDictionary)`

Sets the connection dictionary used by the receiver to _aDictionary_.

---

### setDelegate

`public void setDelegate(Object delegate)`

Sets the receiver's delegate.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/EODistributionRef/Java/Client/Art/up.gif)](../../EODistributionTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
