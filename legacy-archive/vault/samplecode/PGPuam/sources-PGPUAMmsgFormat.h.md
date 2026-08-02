---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_PGPUAMmsgFormat_h.html
archived_at: '2026-07-18T03:18:32.796681Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](sources-PPCGlue.c.md)[Previous](sources-PGPUAMmsgFormat.c.md)

# sources/PGPUAMmsgFormat.h

```


//------------------------------------------------------------------------------------
// PGPUAM Login Command
//------------------------------------------------------------------------------------
void*  FormatLoginCmd           (const void *outbuf, StringPtr serverVersion, StringPtr uamName, StringPtr userName, StringPtr challengeString );

typedef struct 
{
    StringPtr       userName;           // AFP User Name
    StringPtr       challengeString;    // Challenge String
}PUAM_LOGIN_CMD;

void*  FormatChallengeStr( const void   *outbuf, 
                            UInt8       *challengeBuffer,
                            UInt32      challengeBufferSize );

void*  ParseLoginCmd(const void *inbuf,  UInt32 *length, PUAM_LOGIN_CMD *vmsgP);


//------------------------------------------------------------------------------------
// PGPUAM Login Response
//------------------------------------------------------------------------------------
typedef struct 
{
    StringPtr   CounterChallengePString;    // Counter Challenge String
    StringPtr   FingerPrintPString;         // Fingerprint of challenged key
}PUAM_LOGIN_RESP;


void*  FormatLoginResp( const   void       *outbuf, 
                                StringPtr   counterChallengePString, 
                                StringPtr   fingerPrintPString );

void*  ParseLoginResp(const void *inbuf,  UInt32 *length, PUAM_LOGIN_RESP *vmsgP);

//------------------------------------------------------------------------------------
// PGPUAM Login Continue Command
//------------------------------------------------------------------------------------

typedef struct 
{
    StringPtr   SigPString; // Signature reply String
 }PUAM_LOGIN_CONT_CMD;


void*  FormatLoginContinueCmd( const void   *outbuf, StringPtr  counterChallengePString );

void*  ParseLoginContinueCmd(const void *inbuf,  UInt32 *length, PUAM_LOGIN_CONT_CMD *vmsgP);
```

[Next](sources-PPCGlue.c.md)[Previous](sources-PGPUAMmsgFormat.c.md)

