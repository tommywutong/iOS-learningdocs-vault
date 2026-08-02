---
title: Advertising a Bonjour service on a specific set of networking interfaces.
apple_id: DTS10004223
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2007-02-12'
source_url: https://developer.apple.com/library/archive/qa/qa1513/_index.html
archived_at: '2026-07-18T02:31:55.272603Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1513

# Advertising a Bonjour service on a specific set of networking interfaces.

## Q:  I want to use Bonjour to advertise my services but I only want to do so on a specific set of networking interfaces. Is this possible?

A: I want to use Bonjour to advertise my services but I only want to do so on a specific set of networking interfaces. Is this possible?

Yes. However, you will __NOT__ be able to use the [NSNetServices](https://developer.apple.com/documentation/Networking/Conceptual/NSNetServiceProgGuide/index.html) and [CFNetServices](https://developer.apple.com/documentation/Networking/Conceptual/NSNetServiceProgGuide/index.html) APIs to do this. You will need to use the [DNSServiceDiscovery](https://developer.apple.com/documentation/Networking/Reference/DNSServiceDiscovery_CRef/dns_sd/index.html) socket-based API.

You can register your service by issuing a call to `DNSServiceRegister()`, paying close attention to the third parameter specifying an interface index. Determining which interface index maps to a specific interface name can be done by calling `if_nametoindex()`. See below for an example:

__Listing 1__  Example function that registers a service on a single interface.

```
static int doBonjourRegisterOnSingleInterface(     char * interface_name,          // e.g., "en0", "en1", etc.     DNSServiceRef * ssr,     DNSServiceRegisterReply callBack ) {     int err = 0;      DNSServiceFlags flags   = kDNSServiceFlagsDefault;     uint32_t int_index      = 0;     const char *name        = "Clarus";     const char *regtype     = "_http._tcp";     const char *domain      = NULL; // default domain     const char *host        = NULL; // default host     uint16_t port           = 9999;     uint16_t txtLen         = 5;     const char txtRecord[] = "\x04Moof";      // Resolve the index of the specified interface.     int_index = if_nametoindex(interface_name);      if(int_index != 0) {            err = DNSServiceRegister(                             ssr,                             flags,                             int_index,                             name,       /* may be NULL */                             regType,                             domain,     /* may be NULL */                             host,       /* may be NULL */                             htons(port),                             txtLen,                             txtRecord,                             callback,   /* may be NULL */                             NULL        /* may be NULL */           );       } else {           // Desired interface name could not be resolved.           err = -1;      }      return err; }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-02-12 | New document that explains how to register a Bonjour service only on a specific set of networking interfaces. |

