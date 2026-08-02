---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EODistributionRef/Java/Server/Classes/EODistributionContext.html
archived_at: '2026-07-15T08:13:49.060229Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EODistributionRef/Java/Server/Art/up.gif)](../../EODistributionTOC.md) 

# EODistributionContext

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : NSDisposable

> **__Package:__**
> : com.webobjects.eodistribution

---

## Class Description

---

An EODistributionContext object encodes data to send to the client and decodes data received from the client over the distribution channel. An EODistributionContext is also responsible for tracking the state of the server-side object graph and communicating any changes to the client, thus keeping the client and server object graphs in sync. EODistributionContext-or, if implemented, its delegate-validates remote invocations originating from client objects. The server-side EODistributionContext communicates with the EODistributedObjectStore on the client. See the EODistributionContext.Delegate interface description for more information on security and validation.

## Constants

---

EODistributionContext defines String constants for the names of the notifications it posts. For more information, see ["Notifications" (page 31)](#apple-irauoqsjjffeu).

## Interfaces Implemented

---

> : NSDisposable
>
> : `dipose`
>
> :

## Constructors

---

### EODistributionContext

`public com.webobjects.eodistribution.EODistributionContext( com.webobjects.appserver.WOSession session, com.webobjects.eocontrol.EOEditingContext editingContext)`

`public com.webobjects.eodistribution.EODistributionContext( com.webobjects.appserver.WOSession session)`

Creates a new EODistributionContext for use within _session_ and with _editingContext_, if provided, or with _session_'s default editing context otherwise.

---

## Instance Methods

---

### addRemoteMethodReceiver

`public void addRemoteMethodReceiver(Object target)`

Adds the specified object to the list of targets that can receive remote method invocations.

---

### delegate

`public Object delegate()`

Returns the receiver's delegate.

---

### editingContext

`public com.webobjects.eocontrol.EOEditingContext editingContext()`

Returns the receiver's editing context.

__See Also:__ [EODistributionContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg33oorsxq5bpivhui2ltorzgsytvoruw63sdn5xhizlyoq) constructor

---

### invocationTarget

`public Object invocationTarget()`

Returns the target object to which client requests are sent for processing.

__See Also:__ [responseToClientMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg33oorsxq5bpojsxg4dpnzzwkvdpinwgszloorgwk43tmftwk)

---

### remoteMethodReceivers

`public NSArray remoteMethodReceivers()`

Returns the list of targets that can receive remote method invocations.

---

### responseToClientMessage

`public NSData responseToClientMessage(NSData message)`

Called to generate the response to a client request. The target object specified with [setInvocationTarget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg33oorsxq5bponsxisloozxwgylunfxw4vdbojtwk5a) is invoked with the client request, and the response returned by the target object is returned from this method.

__See Also:__ [invocationTarget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg33oorsxq5bpnfxhm33dmf2gs33okrqxez3foq)

---

### session

`public com.webobjects.appserver.WOSession session()`

Returns the receiver's session.

__See Also:__ [EODistributionContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg33oorsxq5bpivhui2ltorzgsytvoruw63sdn5xhizlyoq) constructor

---

### setDelegate

`public void setDelegate(Object delegate)`

Specifies that _delegate_ should be used by the [EODistributionContext](#apple-ivhui2ltorzgsytvoruw63sdn5xhizlyoq) to validate method invocations and fetches requested by the client. For more information, see the EODistributionContext.Delegate interface specification.

__See Also:__ [delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg33oorsxq5bpmrswyzlhmf2gk)

---

### setInvocationTarget

`public void setInvocationTarget(Object invocationTarget)`

Specifies the target object to which client requests are sent for processing.

__See Also:__ [responseToClientMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg5dsnfrhk5djn5xeg33oorsxq5bpojsxg4dpnzzwkvdpinwgszloorgwk43tmftwk)

---

## Notifications

---

### LoadUserDefaultsNotification

Posted whenever a distribution context receives a request for user default values from a client application. Receivers can load default values (from a database, for example) and add them to the mutable dictionary provided in the notification's userInfo.

|  |  |
| --- | --- |
| Notification object | `this` |
| userInfo | An NSDictionary containing a single entry with the key "defaults" and an NSMutableDictionary as the value. The keys to the mutable subdictionary are the names of the user defaults and the corresponding values are the default values themselves. |

### SaveUserDefaultsNotification

Posted whenever the distribution context receives user default values from a client application. Receivers can use this notification to store the default values (in a database, for example).

|  |  |
| --- | --- |
| Notification object | `this` |
| userInfo | An NSDictionary containing a single entry with the key "defaults" and another NSDictionary as the value. The keys to the mutable subdictionary are the names of the user defaults and the corresponding values are the default values themselves. |

### RemoteMethodReceiverNeededNotification

This notification is broadcast when the client first invokes a remote method using the distribution context. The receiver of the notification should add a remote method receiver to the distribution context using the __addRemoteMethodReceiver__ method.

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/EODistributionRef/Java/Server/Art/up.gif)](../../EODistributionTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
