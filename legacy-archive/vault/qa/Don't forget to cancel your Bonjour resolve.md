---
title: Don't forget to cancel your Bonjour resolve
apple_id: DTS10002343
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2007-08-30'
source_url: https://developer.apple.com/library/archive/qa/qa1297/_index.html
archived_at: '2026-07-18T02:30:22.329741Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1297

# Don't forget to cancel your Bonjour resolve

## Q:  After I Resolve a Bonjour service in order to get its IP addresses, do I need to cancel the Resolve operation?

A: After I Resolve a Bonjour service in order to get its IP addresses, do I need to cancel the Resolve operation?

Yes. Leaving the Resolve operation running places an unnecessary burden on the network because you end up sending query packets every couple of minutes in order to keep the DNS resource records up-to-date in the local machine's Bonjour cache. You should only Resolve the service at the moment you need to connect to it, and you should cancel the Resolve immediately after successfully connecting to the service. Manually stopping the Resolve also holds for any resolution involving a timeout scheme. Starting in Mac OS X 10.3, failure to cancel the Resolve will cause the following message to appear in the system log (`/var/log/system.log`).

__Listing 1__  system.log message

```
Oct 11 12:57:54 admin mDNSResponder[266]: 37755: DNSServiceResolver(Ice Cube._http._tcp.local.) has remained active for over two minutes. This places considerable burden on the network.
```

The process by which you cancel the Resolve operation(s) depends on the method you are using.

- If you are using `DNSServiceResolve`, you need to call `DNSServiceRefDeallocate`.
- If you are using `CFNetServiceResolve` or `CFNetServiceResolveWithTimeout`, you need to make the following calls:

  __Listing 2__  CFNetServiceResolve Cancellation

```
CFNetServiceSetClient(netService, NULL, NULL); CFNetServiceUnscheduleFromRunLoop(netService, runLoop, runLoopMode); CFNetServiceCancel(netService); CFRelease(netService);
```
- If you are using `NSNetService`, you need to make the following calls:

  __Listing 3__  NSNetService Cancellation

```
[NSNetService stop]; [NSNetService release];
```

  Or you can use [NSNetService resolveWithTimeout:] and specify a timeout interval. An example of the calls needed would look similar to the following:

  __Listing 4__  NSNetService Timeout Example

```
if ([someNetServiceInstance respondsToSelector:@selector(resolveWithTimeout:)]) {      // Mac OS X 10.4 "Tiger" or later      [someNetServiceInstance resolveWithTimeout:20]; } else {      // Mac OS X 10.3 "Panther" or earlier      [someNetServiceInstance resolve];      NSTimer * stopTimer = [NSTimer timerWithTimeInterval:20                                      target:someNetServiceInstance                                      selector:@selector(stop)                                      userInfo:nil                                      repeats:NO];      [[NSRunLoop currentRunLoop] addTimer:stopTimer forMode:NSDefaultRunLoopMode]; }
```

There are some rare applications that need to keep a Resolve running in order to monitor for TXT record changes. iChat, for example, continuously monitors for changes to a buddy's status message, which is stored in the Bonjour TXT record. If your application requires this type of functionality, starting in Mac OS X 10.4 you can now monitor for TXT records using `CFNetServiceMonitor` and/or `[NSNetService startMonitoring]`. If you want your application to support Mac OS X 10.3 use the DNSServiceDiscovery APIs, located at `/usr/include/dns_sd.h`.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-08-30 | Disambiguated language conveying timeout cancellation. |
| 2007-08-07 | Added language to emphasize the importance of stopping a resolve once connected to a service. |
| 2006-10-06 | Added the descriptions by which you can cancel the resolve operation. |
| 2003-10-15 | New document that explains why it's important to cancel a Bonjour resolve operation. |

