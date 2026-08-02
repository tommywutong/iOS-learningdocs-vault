---
title: TCP
apple_id: DTS10000263
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/TCP/Listings/ASR_c.html
archived_at: '2026-07-18T03:25:58.788009Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCP](TCP.md)


[Next](dnr.c.md)[Previous](AddressXlation.h.md)

# ASR.c

```c
#include    <MacTCPCommonTypes.h>>
#include    <TCPPB.h>

#define     _STORAGE_   true
#include    <TCP.h>

pascal void ASR (StreamPtr stream, unsigned short eventCode, Ptr userData, unsigned short terminReason, struct ICMPReport *icmpMsg)
{
    switch (eventCode) {
        case TCPClosing :
            DebugStr("\pTCPClosing");
            break;
        case TCPULPTimeout :
            DebugStr("\pTCPULPTimeout");
            break;
        case TCPTerminate :
            switch (terminReason) {
                case TCPULPAbort :
                    DebugStr("\pTCPULPAbort");
                    break;
                case TCPRemoteAbort :
                    DebugStr("\pTCPRemoteAbort");
                    break;
                case TCPNetworkFailure :
                    DebugStr("\pTCPNetworkFailure");
                    break;
                case TCPSecPrecMismatch :
                    DebugStr("\pTCPSecPrecMismatch");
                    break;
                case TCPULPTimeoutTerminate :
                    DebugStr("\pTCPULPTimeoutTerminate");
                    break;
                case TCPULPClose :
                    DebugStr("\pTCPULPClose");
                    break;
                case TCPServiceError :
                    DebugStr("\pTCPServiceError");
                    break;
            }
            break;
        case TCPDataArrival :
            DebugStr("\pTCPDataArrival");
            break;
        case TCPUrgent :
            DebugStr("\pTCPUrgent");
            break;
        case TCPICMPReceived :
            switch (icmpMsg->reportType) {
                case netUnreach :
                    DebugStr("\pTCPICMPReceived netUnreach");
                    break;
                case hostUnreach :
                    DebugStr("\pTCPICMPReceived hostUnreach");
                    break;
                case protocolUnreach :
                    DebugStr("\pTCPICMPReceived protocolUnreach");
                    break;
                case portUnreach :
                    DebugStr("\pTCPICMPReceived portUnreach");
                    break;
                case fragReqd :
                    DebugStr("\pTCPICMPReceived fragReqd");
                    break;
                case sourceRouteFailed :
                    DebugStr("\pTCPICMPReceived sourceRouteFailed");
                    break;
                case timeExceeded :
                    DebugStr("\pTCPICMPReceived timeExceeded");
                    break;
                case parmProblem :
                    DebugStr("\pTCPICMPReceived parmProblem");
                    break;
                case missingOption :
                    DebugStr("\pTCPICMPReceived missingOption");
                    break;
            }
            break;
    }
}
```

[Next](dnr.c.md)[Previous](AddressXlation.h.md)

