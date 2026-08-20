---
title: Resolves may return an IPv6 address in Panther
apple_id: DTS10002345
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2005-01-10'
source_url: https://developer.apple.com/library/archive/qa/qa1298/_index.html
archived_at: '2026-07-18T02:30:22.374897Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1298

# Resolves may return an IPv6 address in Panther

## Q:  Starting in Mac OS X 10.3, my Resolve callback function is sometimes returning a sockaddr with an IP address of 0.0.0.0. What's going on?

A: Starting in Mac OS X 10.3, my Resolve callback function is sometimes returning a sockaddr with an IP address of 0.0.0.0. What's going on?

Bonjour supports IPv6 address records in Mac OS X 10.3 and later, so this 0.0.0.0 address is actually the result of parsing a sockaddr as if it was IPv4, when in fact it's probably IPv6. Since your advertised service may not support IPv6, you'll most likely want to ignore all IPv6 addresses. Here's some code that demonstrates how to ignore IPv6 addresses for both CFNetServices and NSNetServices.

__Listing 1__  Example CFNetServices Resolve callback function.

```c
#include <CoreServices/CoreServices.h> #include <netinet/in.h> #include <arpa/inet.h> #include <sys/types.h> #include <sys/socket.h>   static void MyResolveCallback(CFNetServiceRef service, CFStreamError* error, void* info) {   struct sockaddr * socketAddress;   CFArrayRef addresses;   char buffer[256];   uint16_t port;   int count;    addresses = CFNetServiceGetAddressing(service);    /* Search for the IPv4 addresses in the array. */   for (count = 0; count < CFArrayGetCount(addresses); count++) {      socketAddress = (struct sockaddr *)CFDataGetBytePtr(CFArrayGetValueAtIndex(addresses, count));      /* Only continue if this is an IPv4 address. */     if (socketAddress && socketAddress->sa_family == AF_INET) {        if (inet_ntop(AF_INET, &((struct sockaddr_in *)           socketAddress)->sin_addr, buffer, sizeof(buffer))) {          port = ntohs(((struct sockaddr_in *)socketAddress)->sin_port);          printf("IP Address = %s\n", buffer);         printf("Port Number = %d\n", port);          /* Now that you know the IP address and port number, you         should attempt to connect to the service. If the connection         succeeds, then cancel the Resolve operation. If the connection         fails, keep the Resolve running just in case your Resolve         callback gets called again with another IPv4 address, and then         try connecting to the new address. */       }     }   }    return; }
```


__Listing 2__  Example NSNetServices netServiceDidResolveAddress method.

```objc
#import <Foundation/Foundation.h> #import <netinet/in.h> #import <arpa/inet.h> #import <sys/types.h> #import <sys/socket.h>   - (void)netServiceDidResolveAddress:(NSNetService *)sender {    NSArray * addresses;   struct sockaddr * socketAddress;   char buffer[256];   uint16_t port;   int count;    addresses = [sender addresses];    /* Search for the IPv4 addresses in the array. */   for (count = 0; count < [addresses count]; count++) {      socketAddress = (struct sockaddr *)[[addresses objectAtIndex:count] bytes];       /* Only continue if this is an IPv4 address. */     if (socketAddress && socketAddress->sa_family == AF_INET) {        if (inet_ntop(AF_INET, &((struct sockaddr_in *)           socketAddress)->sin_addr, buffer, sizeof(buffer))) {          port = ntohs(((struct sockaddr_in *)socketAddress)->sin_port);          printf("IP Address = %s\n", buffer);         printf("Port Number = %d\n", port);          /* Now that you know the IP address and port number, you         should attempt to connect to the service. If the connection         succeeds, then cancel the Resolve operation. If the connection         fails, keep the Resolve running just in case your Resolve         callback gets called again with another IPv4 address, and then         try connecting to the new address. */       }     }   }    return; }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-01-10 | Updated example code to be more robust against changes in callback behavior that might occur in the future. |
| 2003-10-15 | New document that explains why you get an IP address of 0.0.0.0 when resolving a Bonjour service. |

