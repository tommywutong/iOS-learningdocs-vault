---
title: Miscellaneous User Space API Reference
apple_id: TP40002878
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/DNSServiceDiscovery/CompositePage.html
archived_at: '2026-07-15T07:23:22.781962Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md)


|  |
| --- |
| [ADC Home](https://developer.apple.com/) __>__ [Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) __>__ Reference __>__ [Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422) __>__ [Miscellaneous User Space API Reference](Miscellaneous%20User%20Space%20API%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df5theylnmv3w64tlf5wws43dl5ugkylemvzhg) |

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DNSServiceDiscovery.h | DNSServiceDiscovery.h | DNSServiceDiscovery.h | DNSServiceDiscovery.h | DNSServiceDiscovery.h |

|  |  |
| --- | --- |
| __Includes:__ | <mach/mach_types.h>  [<sys/types.h>](https://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/types/index.html#//apple_ref/doc/header/types.h)  <sys/socket.h>  <sys/cdefs.h>  <netinet/in.h>  <AvailabilityMacros.h> |

## Introduction

---

## Functions

**[DNSServiceBrowserCreate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzkcojxxo43fojbxezlborsq)**
:

**[DNSServiceDiscovery_handleReply](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzkenfzwg33wmvzhsx3imfxgi3dfkjsxa3dz)**
:

**[DNSServiceDiscoveryDeallocate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzkenfzwg33wmvzhsrdfmfwgy33dmf2gk)**
:

**[DNSServiceDiscoveryMachPort](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzkenfzwg33wmvzhstlbmnufa33soq)**
:

**[DNSServiceDomainEnumerationCreate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzken5wwc2loivxhk3lfojqxi2lpnzbxezlborsq)**
:

**[DNSServiceRegistrationAddRecord](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzksmvtws43uojqxi2lpnzawizcsmvrw64te)**
:

**[DNSServiceRegistrationCreate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzksmvtws43uojqxi2lpnzbxezlborsq)**
:

**[DNSServiceRegistrationRemoveRecord](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzksmvtws43uojqxi2lpnzjgk3lpozsvezldn5zgi)**
:

**[DNSServiceRegistrationUpdateRecord](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzksmvtws43uojqxi2lpnzkxazdborsvezldn5zgi)**
:

**[DNSServiceResolver_handleReply](#apple-f4xwc4dqnrsv64tfmyxwi33df52gs5dmmu5gm5lommxuitstknsxe5tjmnsvezltn5whmzlsl5ugc3tenrsvezlqnr4q)**
:

**[DNSServiceResolverResolve](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ejzjvgzlsozuwgzksmvzw63dwmvzfezltn5whmzi)**
:

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DNSServiceBrowserCreate | DNSServiceBrowserCreate | DNSServiceBrowserCreate | DNSServiceBrowserCreate | DNSServiceBrowserCreate |

---

```
dns_service_discovery_ref DNSServiceBrowserCreate (
    const char *regtype,
    const char *domain,
    DNSServiceBrowserReply callBack,
    void *context );
```

##### Parameters

**`regtype`**
: The type of service

**`domain`**
: The domain in which to find the service

**`callBack`**
: The function to be called when service instances are found or removed

**`context`**
: A user specified context which will be passed to the callout function.

##### Return Value

A dns_registration_t

##### Discussion

@description Asynchronously create a DNS Service browser

**_Availability_**
: Introduced in OS X v10.2, and deprecated in OS X v10.2.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DNSServiceDiscovery_handleReply | DNSServiceDiscovery_handleReply | DNSServiceDiscovery_handleReply | DNSServiceDiscovery_handleReply | DNSServiceDiscovery_handleReply |

---

```
void DNSServiceDiscovery_handleReply(
    void *replyMsg);
```

##### Parameters

**`replyMsg`**
: The Mach message.

##### Discussion

@description This function should be called with the Mach message sent
to the port returned by the call to DNSServiceResolverResolve.
The reply message will be interpreted and will result in a
call to the specified callout function.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DNSServiceDiscoveryDeallocate | DNSServiceDiscoveryDeallocate | DNSServiceDiscoveryDeallocate | DNSServiceDiscoveryDeallocate | DNSServiceDiscoveryDeallocate |

---

```
void DNSServiceDiscoveryDeallocate(
    dns_service_discovery_ref dnsServiceDiscovery);
```

##### Parameters

**`dnsServiceDiscovery`**
: A dns_service_discovery_ref as returned from a creation or enumeration call

##### Return Value

void

##### Discussion

@description Deallocates the DNS Service Discovery type / closes the connection to the server

**_Availability_**
: Introduced in OS X v10.2, and deprecated in OS X v10.2.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DNSServiceDiscoveryMachPort | DNSServiceDiscoveryMachPort | DNSServiceDiscoveryMachPort | DNSServiceDiscoveryMachPort | DNSServiceDiscoveryMachPort |

---

```
mach_port_t DNSServiceDiscoveryMachPort(
    dns_service_discovery_ref dnsServiceDiscovery);
```

##### Parameters

**`registration`**
: A dns_service_discovery_ref as returned from DNSServiceRegistrationCreate

##### Return Value

A mach reply port which will be sent messages as appropriate.
These messages should be passed to the DNSServiceDiscovery_handleReply
function. A NULL value indicates that no address was
specified or some other error occurred which prevented the
resolution from being started.

##### Discussion

@description Returns the mach port for a dns_service_discovery_ref

**_Availability_**
: Introduced in OS X v10.2, and deprecated in OS X v10.2.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DNSServiceDomainEnumerationCreate | DNSServiceDomainEnumerationCreate | DNSServiceDomainEnumerationCreate | DNSServiceDomainEnumerationCreate | DNSServiceDomainEnumerationCreate |

---

```
dns_service_discovery_ref DNSServiceDomainEnumerationCreate (
    int registrationDomains,
    DNSServiceDomainEnumerationReply callBack,
    void *context );
```

##### Parameters

**`registrationDomains`**
: A boolean indicating whether you are looking
for recommended registration domains
(e.g. equivalent to the AppleTalk zone list in the AppleTalk Control Panel)
or recommended browsing domains
(e.g. equivalent to the AppleTalk zone list in the Chooser).

**`callBack`**
: The function to be called when domains are found or removed

**`context`**
: A user specified context which will be passed to the callout function.

##### Return Value

A dns_registration_t

##### Discussion

@description Asynchronously create a DNS Domain Enumerator

**_Availability_**
: Introduced in OS X v10.2, and deprecated in OS X v10.2.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DNSServiceRegistrationAddRecord | DNSServiceRegistrationAddRecord | DNSServiceRegistrationAddRecord | DNSServiceRegistrationAddRecord | DNSServiceRegistrationAddRecord |

---

```
DNSRecordReference DNSServiceRegistrationAddRecord(
    dns_service_discovery_ref dnsServiceDiscovery,
    uint16_t rrtype,
    uint16_t rdlen,
    const char *rdata,
    uint32_t ttl) ;
```

##### Parameters

**`dnsServiceDiscovery`**
: A dns_service_discovery_ref as returned from a DNSServiceRegistrationCreate call

**`rrtype`**
: A standard DNS Resource Record Type, from http://www.iana.org/assignments/dns-parameters

**`rdlen`**
: Length of the data

**`rdata`**
: Opaque binary Resource Record data, up to 64 kB.

**`ttl`**
: time to live for the added record.

##### Return Value

DNSRecordReference An opaque reference that can be passed to the update and remove record calls. If an error occurs, this value will be zero or negative

##### Discussion

@description Request that the mDNS Responder add the DNS Record of a specific type

**_Availability_**
: Introduced in OS X v10.2, and deprecated in OS X v10.2.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DNSServiceRegistrationCreate | DNSServiceRegistrationCreate | DNSServiceRegistrationCreate | DNSServiceRegistrationCreate | DNSServiceRegistrationCreate |

---

```
dns_service_discovery_ref DNSServiceRegistrationCreate (
    const char *name,
    const char *regtype,
    const char *domain,
    uint16_t port,
    const char *txtRecord,
    DNSServiceRegistrationReply callBack,
    void *context );
```

##### Parameters

**`name`**
: The name of this service instance (e.g. "Steve's Printer")

**`regtype`**
: The service type (e.g. "_printer._tcp." -- see
RFC 2782 (DNS SRV) and )

**`domain`**
: The domain in which to register the service (e.g. "apple.com.")

**`port`**
: The local port on which this service is being offered (in network byte order)

**`txtRecord`**
: Optional protocol-specific additional information

**`callBack`**
: The DNSServiceRegistrationReply function to be called

**`context`**
: A user specified context which will be passed to the callout function.

##### Return Value

A dns_registration_t

##### Discussion

@description Register a named service with DNS Service Discovery

**_Availability_**
: Introduced in OS X v10.2, and deprecated in OS X v10.2.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DNSServiceRegistrationRemoveRecord | DNSServiceRegistrationRemoveRecord | DNSServiceRegistrationRemoveRecord | DNSServiceRegistrationRemoveRecord | DNSServiceRegistrationRemoveRecord |

---

```
DNSServiceRegistrationReplyErrorType DNSServiceRegistrationRemoveRecord(
    dns_service_discovery_ref ref,
    DNSRecordReference reference) ;
```

##### Parameters

**`dnsServiceDiscovery`**
: A dns_service_discovery_ref as returned from a DNSServiceRegistrationCreate call

**`dnsRecordReference`**
: A dnsRecordReference as returned from a DNSServiceRegistrationAddRecord call

##### Return Value

DNSServiceRegistrationReplyErrorType If an error occurs, this value will be non zero

##### Discussion

@description Request that the mDNS Responder remove the DNS Record(s) of a specific type

**_Availability_**
: Introduced in OS X v10.2, and deprecated in OS X v10.2.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DNSServiceRegistrationUpdateRecord | DNSServiceRegistrationUpdateRecord | DNSServiceRegistrationUpdateRecord | DNSServiceRegistrationUpdateRecord | DNSServiceRegistrationUpdateRecord |

---

```
DNSServiceRegistrationReplyErrorType DNSServiceRegistrationUpdateRecord(
    dns_service_discovery_ref ref,
    DNSRecordReference reference,
    uint16_t rdlen,
    const char *rdata,
    uint32_t ttl) ;
```

##### Parameters

**`dnsServiceDiscovery`**
: A dns_service_discovery_ref as returned from a DNSServiceRegistrationCreate call

**`dnsRecordReference`**
: A dnsRecordReference as returned from a DNSServiceRegistrationAddRecord call

**`rdlen`**
: Length of the data

**`rdata`**
: Opaque binary Resource Record data, up to 64 kB.

**`ttl`**
: time to live for the updated record.

##### Return Value

DNSServiceRegistrationReplyErrorType If an error occurs, this value will be non zero

##### Discussion

@description Request that the mDNS Responder add the DNS Record of a specific type

**_Availability_**
: Introduced in OS X v10.2, and deprecated in OS X v10.2.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DNSServiceResolver_handleReply | DNSServiceResolver_handleReply | DNSServiceResolver_handleReply | DNSServiceResolver_handleReply | DNSServiceResolver_handleReply |

---

```
void DNSServiceDiscovery_handleReply(
    void *replyMsg);
```

##### Parameters

**`replyMsg`**
: The Mach message.

##### Discussion

@description This function should be called with the Mach message sent
to the port returned by the call to DNSServiceResolverResolve.
The reply message will be interpreted and will result in a
call to the specified callout function.

---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DNSServiceResolverResolve | DNSServiceResolverResolve | DNSServiceResolverResolve | DNSServiceResolverResolve | DNSServiceResolverResolve |

---

```
dns_service_discovery_ref DNSServiceResolverResolve (
    const char *name,
    const char *regtype,
    const char *domain,
    DNSServiceResolverReply callBack,
    void *context );
```

##### Parameters

**`name`**
: The name of the service instance

**`regtype`**
: The type of service

**`domain`**
: The domain in which to find the service

**`callBack`**
: The DNSServiceResolverReply function to be called when the specified
address has been resolved.

**`context`**
: A user specified context which will be passed to the callout function.

##### Return Value

A dns_registration_t

##### Discussion

@description Resolved a named instance of a service to its address, port, and
(optionally) other demultiplexing information contained in the TXT record.

**_Availability_**
: Introduced in OS X v10.2, and deprecated in OS X v10.2.

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Last Updated: 2006-06-20
