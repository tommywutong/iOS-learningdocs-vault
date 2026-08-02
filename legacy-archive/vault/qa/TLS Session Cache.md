---
title: TLS Session Cache
apple_id: DTS40010700
resource_type: QA
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2015-08-19'
source_url: https://developer.apple.com/library/archive/qa/qa1727/_index.html
archived_at: '2026-07-18T02:34:30.053732Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1727

# TLS Session Cache

## Q:  I'm using NSURLConnection to access two HTTPS URLs on the same server. I want to use a unique client identity for each connection. When I access the first URL I get an authentication challenge that allows me to supply the correct client identity, but when I then access the second URL I don't get any authentication challenges. How can I get an authentication challenge for this second connection?

A: When you access a URL via HTTPS, you're actually using HTTP over TLS (Transport Layer Security, the evolution of SSL, the Secure Sockets Layer). You don't get a second challenge because the second connection reuses the TLS session established by the first. To understand this problem, you need to understand something about TLS itself, and how it is implemented on OS X and iOS.

Opening a TLS session is computationally expensive (because it involves working with large asymmetric keys), so TLS has a mechanism to avoid doing this work for each connection. A TLS connection can either establish a new session or it can attempt to resume an existing session, where resuming an existing session is much cheaper than starting a new one. A TLS client can therefore boost performance by maintaining a cache of existing sessions and reusing them when it's appropriate.

The core TLS code on both OS X and iOS, Secure Transport, maintains such a cache. This TLS session cache is implemented independently in each process. In most circumstances the TLS session cache works transparently to speed up TLS connections, but in some cases it can cause problems. In this case, your second connection has reused the TLS session of the first connection, and thus you don't have an opportunity to supply a new client identity for the second connection.

Because caching can occur at various levels within the NSURLConnection stack, before trying to work around a TLS session cache problem it's a good idea to confirm that this is actually the root cause. You can do this by exploiting the fact that TLS session cache entries persist for about 10 minutes. Thus, if the problem still occurs when the second connection follows the first connection by 9 minutes, but goes away if the delay is 11 minutes, chances are that the TLS session cache is to blame.

Inside the NSURLConnection Framework, there's no direct way to flush the TLS session cache (other than to terminate the process itself), nor is there a way to tell NSURLConnection not to use it
(r. 8957312)
. The only reasonable workaround is to change your connection in such a way that the second connection doesn't hit (in the sense of a "cache hit") the cache entry created by the first connection. To do this you need to understand the TLS session cache key format used by NSURLConnection or, more accurately, the CFSocketStream that underlies NSURLConnection.

If you cannot switch to NSURLSession, please see below.

In the absence of a proxy, the TLS session cache key contains the destination IP address, the destination port, and the destination DNS name, for example, `{131.39.46.209:47873}devforums.apple.com`. Consequently, altering the IP address, the port, or the DNS name will cause a TLS session cache miss, and allow your second connection to receive the TLS authentication challenges. While it's unlikely that you'll be able to alter the IP address component of the TLS session cache key, the port and DNS name components are potential workaround candidates. For example:

- If your two connections represent very different operations, you might consider configuring your server to listen on two different ports. For example, if the first connection is for enrollment and the second connection is for data transfer, you can have two instances of your server, one for enrollment and one for data transfer, each listening on their own port. Most HTTP servers are easy to configure in this way.
- If you have control over the DNS namespace of the server, you could configure that namespace to ensure that each connection goes to a unique DNS address. Let's say your server is currently at `myapp.example.com`. You could configure your DNS server to map all names within that domain (`*.myapp.example.com`) to your server. Your clients could then have each connection target a unique name within that namespace, thus avoiding any chance the connection will hit the TLS session cache. For example, your client's first connection might target `s464287123.myapp.example.com`, its second connection `s338233934.myapp.example.com`, and so on, all of which are redirected by your DNS server to `myapp.example.com`.
- Both of the previous suggestions require you to reconfigure the server in some way. If you have no control over the server, your options are rather limited. One sneaky workaround is to append a dot (".") to the DNS name you're connecting to. If you're not familiar with the details of DNS, a name ending in dot is considered to be a fully qualified domain name (FQDN), whereas names not ending in dot (partially qualified domain names, PQDN) may be resolved by appending some default domain. For example, `devforums.apple.com.` (note the trailing dot) is an FQDN for DevForums but, when you're at Apple and the default DNS domain is `apple.com.`, you can refer to it via the PQDN of `devforums`.

  It turns out that the host name from the URL you give NSURLConnection passes down, unmodified, through many layers of CFNetwork until it eventually forms a component of the Secure Transport TLS session cache key. Thus, if you have a program that first connected to `devforums.apple.com.` (with a trailing dot) and then connected to `devforums.apple.com` (without a trailing dot), each connection will get TLS authentication challenges.

  The obvious drawback of this approach is that it doesn't scale; you can't just keep adding dots!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-08-19 | Added Note to redirect users to NSURLSession and updated expository content. |
| 2011-02-10 | New document that describes how the TLS session cache affects HTTPS connections that need different TLS parameters. |

