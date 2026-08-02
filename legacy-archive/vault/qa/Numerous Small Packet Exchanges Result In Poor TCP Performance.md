---
title: Numerous Small Packet Exchanges Result In Poor TCP Performance
apple_id: DTS10001438
resource_type: QA
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2011-09-09'
source_url: https://developer.apple.com/library/archive/qa/nw26/_index.html
archived_at: '2026-07-18T02:29:48.120912Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A NW26

# Numerous Small Packet Exchanges Result In Poor TCP Performance

## Q:  My TCP application exchanges a number of small packets of information, which may or may not generate a response from the other side. In some cases, I find that the application delays sending packets, and performance is terrible. How can I solve this problem?

A: One possible reason for this behavior is the [Nagle algorithm](http://en.wikipedia.org/wiki/Nagle's_algorithm), which is a feature of TCP that works to prevent send-side 'silly window syndrome'. If a TCP connection has unacknowledged data, the Nagle algorithm will prevent the transmission of new data, with the goal being to coalesce lots of small data packets into one large one. For example, if an application generates data one byte at a time, this algorithm prevents it from filling the network with lots of one-byte payload TCP packets.

In most cases the Nagle algorithm is a good thing, and you should leave it enabled. So, before disabling the Nagle algorithm, you should check that you are using TCP efficiently. Specifically, make sure that you present your data to TCP as whole logical units. For example, if your data consists of a header followed by a body, don't write the header and then write the body. Rather, concatenate everything into one single buffer and write it all at once (alternatively, you can use a function, such as sendmsg, that supports discontiguous writes). This will prevent the Nagle algorithm from delaying the body unnecessarily. In short, if you use TCP efficiently, you might find that this fixes your problem and you don't need to worry about the Nagle algorithm at all.

However, for some applications—particularly interactive applications, like telnet—the Nagle algorithm can cause unnecessary delays. If that's the case you can disable it on a specific connection by setting the `TCP_NODELAY` socket option, as shown in Listing 1.

__Listing 1__  Setting the TCP_NODELAY option

```
int err; static const int kOne = 1;  err = setsockopt(fd, IPPROTO_TCP, TCP_NODELAY, &kOne, sizeof(kOne)); if (err < 0) {     err = errno; }
```

If you're using a high-level TCP API, like NSStream or CFStream, you can disable the Nagle algorithm by first getting the file descriptor from the stream using `kCFStreamPropertySocketNativeHandle` and then calling `setsockopt` on that descriptor.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-09-09 | Updated to describe BSD Sockets rather than Open Transport. |
| 1998-05-25 | New document that explains why numerous small package exchanges result in poor TCP performance. |

