---
title: NSNetService and Automatic Reference Counting (ARC)
apple_id: DTS40011324
resource_type: QA
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2011-10-28'
source_url: https://developer.apple.com/library/archive/qa/qa1546/_index.html
archived_at: '2026-07-18T02:32:15.877703Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1546

# NSNetService and Automatic Reference Counting (ARC)

## Q:  I create a pair of streams using `-[NSNetService getInputStream:outputStream:]` and, after converting my project to automatic reference counting (ARC), my streams refuse to open properly. What's causing this?

A: `-[NSNetService getInputStream:outputStream:]` has a number of outstanding bugs
(r. 6868813)
(r. 9821932)
(r. 9856751)
, some of which are exacerbated by ARC. The best way to avoid all of these problems is to drop down a level and use `CFStreamCreatePairWithSocketToNetService` to create your streams. The code in Listing 1 shows how you can create a category on NSNetService that provides a functional replacement for `-[NSNetService getInputStream:outputStream:]`.

__Listing 1__  A functional replacement for -[NSNetService getInputStream:outputStream:]

```objc
@interface NSNetService (QNetworkAdditions)

- (BOOL)qNetworkAdditions_getInputStream:(out NSInputStream **)inputStreamPtr
    outputStream:(out NSOutputStream **)outputStreamPtr;

@end

@implementation NSNetService (QNetworkAdditions)

- (BOOL)qNetworkAdditions_getInputStream:(NSInputStream **)inputStreamPtr
    outputStream:(NSOutputStream **)outputStreamPtr
{
    BOOL                result;
    CFReadStreamRef     readStream;
    CFWriteStreamRef    writeStream;

    result = NO;

    readStream = NULL;
    writeStream = NULL;

    if ( (inputStreamPtr != NULL) || (outputStreamPtr != NULL) ) {
        CFNetServiceRef     netService;

        netService = CFNetServiceCreate(
            NULL,
            (__bridge CFStringRef) [self domain],
            (__bridge CFStringRef) [self type],
            (__bridge CFStringRef) [self name],
            0
        );
        if (netService != NULL) {
            CFStreamCreatePairWithSocketToNetService(
                NULL,
                netService,
                ((inputStreamPtr  != NULL) ? &readStream : NULL),
                ((outputStreamPtr != NULL) ? &writeStream : NULL)
            );
            CFRelease(netService);
        }

        // We have failed if the client requested an input stream and didn't
        // get one, or requested an output stream and didn't get one. We also
        // fail if the client requested neither the input nor the output
        // stream, but we don't get here in that case.

        result = ! ((( inputStreamPtr != NULL) && ( readStream == NULL)) ||
                    ((outputStreamPtr != NULL) && (writeStream == NULL)));
    }
    if (inputStreamPtr != NULL) {
        *inputStreamPtr  = CFBridgingRelease(readStream);
    }
    if (outputStreamPtr != NULL) {
        *outputStreamPtr = CFBridgingRelease(writeStream);
    }

    return result;
}

@end
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-10-28 | New document that describes an issue with NSNetService that can cause connections never to complete. |

