---
title: Registering a Bonjour service multiple times
apple_id: DTS10002335
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: CoreServices
published: '2003-10-23'
source_url: https://developer.apple.com/library/archive/qa/qa1311/_index.html
archived_at: '2026-07-18T02:30:22.565781Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1311

# Registering a Bonjour service multiple times

## Q:  When registering the same Bonjour service multiple times while running on the same machine, none of the registrations receive a name conflict error. Why is this?

A: When registering the same Bonjour service multiple times while running on the same machine, none of the registrations receive a name conflict error. Why is this?

If you try to register the same name/type/domain/port multiple times on the same machine, you won't get an error because the DNS resource records being registered have identical rdata so the registrations are in agreement. Only when the rdata differs is it considered a name conflict.

The reason for this is to allow Bonjour proxies of various kinds. Suppose you have a networked printer which does LPR printing, but doesn't advertise that using Bonjour. You could create a Bonjour proxy to advertise on the printer's behalf. For fault-tolerance, you might run two proxies on the network, and you would not want the two proxies to conflict with each other. Because Bonjour only considers it to be a conflict when the two sets of rdata are different, the two proxies can coexist peacefully side-by-side. As long as both give identical answers to the same question, neither sees the other's answer as being in conflict with its own.

An example of when the rdata would be different is if you registered two identical name/type/domain/ports from different machines by using CFNetServices or NSNetServices. In that case, the rdata will be different because the Target Host in the SRV record will contain a different address record (because the two machines have different IP addresses), and this will generate a name conflict error. Alternatively, registering two identical name/type/domains from the same machine, but using two different port numbers would be considered a name conflict.

Even though registering the same Bonjour service multiple times on the same machine is perfectly legal, it most often happens because of an application bug. Therefore, in order to alert the application developer of this situation, an error message is printed to the system log (/var/log/system.log) which is similar to the following.

__Listing 1__  system.log message

```
Oct  4 18:16:21 localhost mDNSResponder[177]: 13423: Client application registered 2 identical instances of service Cube._http._tcp.local. port 80.
```

For more information about the protocols used by Bonjour, please see the technical specifications referenced by the [Bonjour Developer Web Site](https://developer.apple.com/bonjour/).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2003-10-23 | New document that explains why registering the same Bonjour service twice on the same machine doesn't cause a name conflict. |

