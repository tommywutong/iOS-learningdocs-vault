---
title: Use empty string for Bonjour domains
apple_id: DTS10003186
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2004-02-06'
source_url: https://developer.apple.com/library/archive/qa/qa1331/_index.html
archived_at: '2026-07-18T02:30:25.152173Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1331

# Use empty string for Bonjour domains

## Q:  When using Bonjour API's like CFNetServices, NSNetServices and DNSServiceDiscovery, what should I pass in for the domain parameter?

A: When using Bonjour API's like CFNetServices, NSNetServices and DNSServiceDiscovery, what should I pass in for the domain parameter?

Normally, when Registering and Browsing for services, you should pass in an empty string ("") for the domain, and the system will automatically do the correct thing. In Mac OS X 10.2 through 10.3.x, using an empty string will cause the system to Register and Browse for services in the Multicast DNS "local." domain. In addition, by passing in an empty string for the domain, your application will automatically take advantage of future enhancements to Bonjour.

When Resolving a service, make sure to pass in the same domain which was returned in the Browse callback when you originally discovered the service. Don't assume that all services are in the "local." domain. If you hard code "local." as the domain for Resolving, your application may not be compatible with future versions of Mac OS X.

In some cases, you may want to prevent your application from operating outside the local network. For example, iTunes must only share music with other computers on the local link. In cases like this, you can restrict Bonjour service discovery to the local network by explicitly passing in "local." for the domain parameter when Registering and Browsing.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-02-06 | New document that explains what to specify for the domain parameter when using Bonjour API's. |

