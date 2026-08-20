---
title: TCP
apple_id: DTS10000263
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/TCP/Listings/TCPReceive_c.html
archived_at: '2026-07-18T03:25:59.170090Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCP](TCP.md)


[Next](TCPSend.c.md)[Previous](TCPPB.h.md)

# TCPReceive.c

```c
/*
** James "im" Beninghaus
*/


#include    <Errors.h>
#include    <Devices.h>
#include    <QuickDraw.h>
#include    <stdio.h>

#include    <MacTCPCommonTypes.h>>
#include    <AddressXlation.h>
#include    <GetMyIPAddr.h>
#include    <TCPPB.h>
#include    <UDPPB.h>

#define     _STORAGE_   true

#include    <TCP.h>


main (int argc, char *argv[], char *envp[]) {

    auto    OSErr           osErr           = noErr;
    auto    short           index;
    auto    char            *option;
    auto    char            *parameter;
    auto    TCPNotifyProc   asrProc         = nil;
    auto    TCPiopb         pb;
    auto    StreamPtr       stream;
    auto    char            streamBuf[4096];
    auto    long            streamBufLen    = sizeof(streamBuf);
    auto    Ptr             streamBufPtr;
    auto    char            ioBuf[256]      = "";
    auto    unsigned short  ioBufLen        = sizeof(ioBuf);
    auto    ip_addr         localIP         = cAnyIP;
    auto    ip_port         localPort       = cReceivePort;
    auto    ip_addr         remoteIP        = cAnyIP;
    auto    ip_port         remotePort      = cAnyPort;

    InitGraf((Ptr) &qd.thePort);

    if (argc > 1) { 
        if ( ('-' != argv[1][0]) && ('n' != argv[1][1]) ) {
            printf("TCPReceive [-n]");
            exit(paramErr);
        } else {
            asrProc = ASR;
        }           
    }

    osErr = _TCPInit();
    if (noErr == osErr) {
        osErr = _TCPCreate(&pb, &stream, streamBuf, streamBufLen, (TCPNotifyProc) asrProc, (Ptr) nil,  (TCPIOCompletionProc) nil, false);
        if (noErr == osErr) {
            osErr = _TCPPassiveOpen(&pb, stream, &remoteIP, &remotePort, &localIP, &localPort, (Ptr) nil, (TCPIOCompletionProc) nil, false);
            if (noErr == osErr) {
                /* receive data from the remote host */
                osErr = _TCPRcv(&pb, stream, ioBuf, &ioBufLen, (Ptr) nil, (TCPIOCompletionProc) nil, false);
                if (noErr == osErr)
                    printf("%s\n", ioBuf);
                osErr = _TCPClose(&pb, stream, nil, (TCPIOCompletionProc) nil, false);
            }
            osErr = _TCPRelease(&pb, stream, &streamBufPtr, &streamBufLen, (TCPIOCompletionProc) nil, false);
        }
    }
    exit(osErr);
}
```

[Next](TCPSend.c.md)[Previous](TCPPB.h.md)

