---
title: What encryption, authentication, and proxy technologies does Safari support?
apple_id: DTS40008174
resource_type: QA
platform: Safari|macOS
topic: Security
technology: null
published: '2009-01-27'
source_url: https://developer.apple.com/library/archive/qa/qa1537/_index.html
archived_at: '2026-07-18T02:32:15.404732Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1537

# What encryption, authentication, and proxy technologies does Safari support?

## Q:  What encryption, authentication, and proxy technologies does Safari support?

A: What encryption, authentication, and proxy technologies does Safari support?

Encryption technologies are used to provide a secure, encrypted channel between two systems and protect the information in the channel from eavesdroppers. Safari supports common encryption mechanisms such as SSL versions 2 and 3, as well as the next-generation security standard Transport Layer Security (TLS). Safari supports 40- and 128-bit SSL encryption, and Safari supports signed Java applications.

Safari supports standards-based authentication such as Kerberos single sign-on and X.509 personal certificates for logging into secure sites. Safari also supports the proprietary authentication protocol NTLMv2.

Firewalls use proxy services to control traffic flowing in and out of the network. Safari supports a variety of proxy protocols, including FTP Proxy, Web Proxy (HTTP), Secure Web Proxy (HTTPS), Streaming Proxy (RTSP), SOCKS Proxy, and Gopher Proxy. Safari also supports Automatic Proxy configuration, so administrators can configure browser clients on the network via a .PAC file. On Mac OS X, proxy settings can be configured in the Advanced Network panel of System Preferences. On Windows, Safari respects proxy settings in the Internet control panel.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-01-27 | New document that provides information about the security technologies that Safari supports. |

