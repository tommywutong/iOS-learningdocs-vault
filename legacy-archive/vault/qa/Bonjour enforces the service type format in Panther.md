---
title: Bonjour enforces the service type format in Panther
apple_id: DTS10002338
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2004-03-23'
source_url: https://developer.apple.com/library/archive/qa/qa1198/_index.html
archived_at: '2026-07-18T02:30:12.462349Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1198

# Bonjour enforces the service type format in Panther

## Q:  My application uses Bonjour to advertise a service. Everything works great in Mac OS X 10.2, but in Mac OS X 10.3, my service registration fails with a -65540 error. What am I doing wrong?

A: My application uses Bonjour to advertise a service. Everything works great in Mac OS X 10.2, but in Mac OS X 10.3, my service registration fails with a -65540 error. What am I doing wrong?

Starting with Mac OS X 10.3, mDNSResponder enforces the proper format for a Bonjour service type. A service type must be of the form:

_applicationprotocol._transportprotocol

Currently, "_transportprotocol" must be either "_tcp" or "_udp". The "applicationprotocol" must only contain letters, digits and hyphens, and must begin and end with a letter or digit. As an example, the service type for Hypertext Transport Protocol is "_http._tcp".

IANA restricts the "applicationprotocol" to be 14 characters or less. Apple highly recommends that your "applicationprotocol" be 14 characters or less so it can be registered with [IANA](http://www.iana.org/cgi-bin/usr-port-number.pl) or with the [DNS-SD Web Site](http://www.dns-sd.org/ServiceTypes.html). If your service type is not formatted correctly, you'll see a message in the system log (/var/log/system.log) similar to Listing 1.

__Listing 1__  system.log message

```
Sep 10 19:58:02 ice-cube mDNSResponder[257]: 9987: DNSServiceRegister("Test","._#$@._tpd.", "", 80) failed: Bad Name (-65540) Sep 10 19:58:14 ice-cube mDNSResponder[257]: ConstructServiceName: Invalid service application protocol name: Test..local.
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-03-23 | Unspecified content revisions. |
| 2003-10-23 | New document that explains why registering a Bonjour service might fail on Panther. |

