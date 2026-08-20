---
title: Using NSStreams For A TCP Connection Without NSHost
apple_id: DTS40008977
resource_type: QA
platform: iOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2012-03-27'
source_url: https://developer.apple.com/library/archive/qa/qa1652/_index.html
archived_at: '2026-07-18T02:33:17.345805Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1652

# Using NSStreams For A TCP Connection Without NSHost

## Q:  Given that `+getStreamsToHost:port:inputStream:outputStream:` is not supported on iOS, how can I create NSStreams for a TCP connection to a named host?

A: You can do this by exploiting the toll-free bridge between NSStream and CFStream. Use `CFStreamCreatePairWithSocketToHost` to create CFStreams to the host, and then cast the resulting CFStreams to NSStreams.

Listing 1 shows an example of this. It adds a category to NSStream that implements a replacement for `+getStreamsToHost:port:inputStream:outputStream:`.

__Listing 1__  A category to create TCP streams to a named host

```objc
@interface NSStream (QNetworkAdditions)

+ (void)qNetworkAdditions_getStreamsToHostNamed:(NSString *)hostName
    port:(NSInteger)port
    inputStream:(out NSInputStream **)inputStreamPtr
    outputStream:(out NSOutputStream **)outputStreamPtr;

@end

@implementation NSStream (QNetworkAdditions)

+ (void)qNetworkAdditions_getStreamsToHostNamed:(NSString *)hostName
    port:(NSInteger)port
    inputStream:(out NSInputStream **)inputStreamPtr
    outputStream:(out NSOutputStream **)outputStreamPtr
{
    CFReadStreamRef     readStream;
    CFWriteStreamRef    writeStream;

    assert(hostName != nil);
    assert( (port > 0) && (port < 65536) );
    assert( (inputStreamPtr != NULL) || (outputStreamPtr != NULL) );

    readStream = NULL;
    writeStream = NULL;

    CFStreamCreatePairWithSocketToHost(
        NULL,
        (__bridge CFStringRef) hostName,
        port,
        ((inputStreamPtr  != NULL) ? &readStream : NULL),
        ((outputStreamPtr != NULL) ? &writeStream : NULL)
    );

    if (inputStreamPtr != NULL) {
        *inputStreamPtr  = CFBridgingRelease(readStream);
    }
    if (outputStreamPtr != NULL) {
        *outputStreamPtr = CFBridgingRelease(writeStream);
    }
}

@end
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-03-27 | Fixed a typo (r. 11064426). |
| 2011-10-19 | Updated the code to support automatic reference counting (ARC). |
| 2009-06-23 | New document that describes how to create TCP NSStreams without NSHost (which is not supported on iOS). |

