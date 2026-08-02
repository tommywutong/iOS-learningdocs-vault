---
title: Use the Computer Name when registering your Bonjour service
apple_id: DTS10001751
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: CoreServices
published: '2004-03-05'
source_url: https://developer.apple.com/library/archive/qa/qa1228/_index.html
archived_at: '2026-07-18T02:30:12.682529Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1228

# Use the Computer Name when registering your Bonjour service

## Q:  When I advertise my service with Bonjour, I use `SCDynamicStoreCopyLocalHostName` which retrieves the "Local Hostname" from the Sharing preference panel, and then I pass in that name when registering. Is that the correct thing to do?

A: When I advertise my service with Bonjour, I use `SCDynamicStoreCopyLocalHostName` which retrieves the "Local Hostname" from the Sharing preference panel, and then I pass in that name when registering. Is that the correct thing to do?

No. A Bonjour service name may contain any characters without restriction, including spaces, punctuation, accented characters, non-Roman text, and anything else that may be represented using UTF-8. Therefore, it probably doesn't make sense to advertise a service using the "Local Hostname", with its restricted character set. In most situations, you should advertise your service using the "Computer Name" from the Sharing preference panel, although you're free to advertise a service using whatever name you choose.

It's easy to register a service with the "Computer Name" when using CFNetServices, NSNetServices, or DNSServiceDiscovery. Simply pass in an empty string ("") for the name, and the system will automatically advertise your service using the "Computer Name", and will automatically handle name conflicts by appending a digit to the end of the name.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-03-05 | New document that explains why you should use the Computer Name when advertising a Bonjour service. |

