---
title: DNSServiceDiscovery Mach-Based API
apple_id: TP30001129
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-04-29'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/dns_discovery_mach/reference/reference_mach2.html
archived_at: '2026-07-15T08:18:33.208112Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [DNSServiceDiscovery Mach-Based API](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](reference_mach.md)

# Constants and Data Types

This section describes the constants and data types
used by the DNSServiceDiscovery API:

- `[DNSServiceDiscovery Flags and Errors](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml3enzzv643foj3gsy3fl5sgs43dn53gk4tzl5zgkzq)`
- `[Registration and Record Update](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2ejzjvgzlsozuwgzksmvtws43uojqxi2lpnzjgk4dmpe)`
- `[Resolver](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2ejzjvgzlsozuwgzksmvzw63dwmvzfezlqnr4q)`
- `[Domain Enumeration](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2ejzjvgzlsozuwgzken5wwc2loivxhk3lfojqxi2lpnzjgk4dmpe)`
- `[Service Browser](#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2ejzjvgzlsozuwgzkcojxxo43fojjgk4dmpe)`

These flags and data types are used by most DNSServiceDiscovery
functions and callbacks.

```
/* Opaque internal data type */
typedef struct _dns_service_discovery_t * dns_service_discovery_ref;

   /* possible reply flags values */
   enum {
      kDNSServiceDiscoveryNoFlags= 0,
      kDNSServiceDiscoveryMoreRepliesImmediately= 1 << 0,
};
// If the kDNSServiceDiscoveryMoreRepliesImmediately flag is set,
// do not update your UI

/* possible error code values */
typedef enum
{
kDNSServiceDiscoveryWaiting     = 1,
kDNSServiceDiscoveryNoError     = 0,

// mDNS Error codes are in the range
// FFFE FF00 (-65792) to FFFE FFFF (-65537)
kDNSServiceDiscoveryUnknownErr        = -65537,       // 0xFFFE FFFF
kDNSServiceDiscoveryNoSuchNameErr     = -65538,
kDNSServiceDiscoveryNoMemoryErr       = -65539,
kDNSServiceDiscoveryBadParamErr       = -65540,
kDNSServiceDiscoveryBadReferenceErr   = -65541,
kDNSServiceDiscoveryBadStateErr       = -65542,
kDNSServiceDiscoveryBadFlagsErr       = -65543,
kDNSServiceDiscoveryUnsupportedErr    = -65544,
kDNSServiceDiscoveryNotInitializedErr = -65545,
kDNSServiceDiscoveryNoCache           = -65546,
kDNSServiceDiscoveryAlreadyRegistered = -65547,
kDNSServiceDiscoveryNameConflict      = -65548,
kDNSServiceDiscoveryInvalid           = -65549,
kDNSServiceDiscoveryMemFree           = -65792        // 0xFFFE FF00
} DNSServiceRegistrationReplyErrorType;
```


These types are used for DNS registration and update.

```
typedef void (*DNSServiceRegistrationReply) (
DNSServiceRegistrationReplyErrorType errorCode,
void *context
);

typedef uint32_t DNSRecordReference;
```


These types and flags are used when resolving the IP address
for a service.

```
typedef void (*DNSServiceResolverReply) (
   struct sockaddr *interface,
   // Host interface IP addr--needed if multiple LAN connections
   struct sockaddr *address,
   // Service link-local IP address, including port number
   const char *txtRecord,
   DNSServiceDiscoveryReplyFlags flags,
   void *context
);
```


These constants are used when determining the domain(s)
in which you should search for or register a service

```
typedef enum
{
   DNSServiceDomainEnumerationReplyAddDomain, // Domain found
   DNSServiceDomainEnumerationReplyAddDomainDefault,
   // Domain found (and should be selected by default)
   DNSServiceDomainEnumerationReplyRemoveDomain,
   // Domain has been removed from network
} DNSServiceDomainEnumerationReplyResultType;
typedef enum
{
   DNSServiceDiscoverReplyFlagsFinished,
   DNSServiceDiscoverReplyFlagsMoreComing,
} DNSServiceDiscoveryReplyFlags;
typedef void (*DNSServiceDomainEnumerationReply) (
   DNSServiceDomainEnumerationReplyResultType resultType,
   const char *replyDomain,
   DNSServiceDiscoveryReplyFlags flags,
   void *context
);
```


These types and constants are used when browsing for services

```
typedef enum
{
   DNSServiceBrowserReplyAddInstance,
   // Instance of service found
   DNSServiceBrowserReplyRemoveInstance
   // Instance has been removed from network
} DNSServiceBrowserReplyResultType;
typedef void (*DNSServiceBrowserReply) (
   DNSServiceBrowserReplyResultType resultType, // Add or remove
   const char *replyName,
   const char *replyType,
   const char *replyDomain,
   DNSServiceDiscoveryReplyFlags flags,
   void *context
);
```

[Next](Document%20Revision%20History.md)[Previous](reference_mach.md)

