---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_PGPUAMclientProtocol_h.html
archived_at: '2026-07-18T03:18:32.432482Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](sources-PGPUAMdefines.h.md)[Previous](sources-PGPUAMclientProtocol.c.md)

# sources/PGPUAMclientProtocol.h

```


#pragma mark PGPUAM Login Command

typedef void (*LoginIdleProcPtr) ();

//------------------------------------------------------------------------------------
// PGPUAM Login Command
//------------------------------------------------------------------------------------

OSStatus    SndLoginCmd(    ClientUAMCallbackRec    *callbacks,
                                        StringPtr   serverVersion, 
                                        StringPtr   uamName, 
                                        StringPtr   userName,
                                        StringPtr   challengeString,
                                        OTAddress   *serverAddress,
                                        UInt8       *replyBuffer,
                                        UInt32      replyBufferSize,
                                        UInt32      *actReplyBufferSize,
                                        short       *sessionRefNum,
                                LoginIdleProcPtr    idleProc
                                        );



//------------------------------------------------------------------------------------
// PGPUAM Login Continue Command
//------------------------------------------------------------------------------------

OSStatus SndLoginContinueCmd(   ClientUAMCallbackRec    *callbacks,
                                    short       sessionRefNum,
                                    StringPtr   answerString, 
                                    UInt8       *replyBuffer,
                                    UInt32      replyBufferSize,
                                    UInt32      *actReplyBufferSize,
                            LoginIdleProcPtr    idleProc
                                        );
```

[Next](sources-PGPUAMdefines.h.md)[Previous](sources-PGPUAMclientProtocol.c.md)

