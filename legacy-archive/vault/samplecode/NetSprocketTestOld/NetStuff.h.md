---
title: NetSprocketTestOld
apple_id: DTS10000058
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/NetSprocketTestOld/Listings/NetStuff_h.html
archived_at: '2026-07-18T03:16:57.818344Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NetSprocketTestOld](NetSprocketTestOld.md)


[Next](Proto.h.md)[Previous](NetStuff.cp.md)

# NetStuff.h

```c
#ifndef __NETSTUFF__
#define __NETSTUFF__

#include <NetSprocket.h>


extern Boolean gHost;
extern NSpGameReference gNetGame;

enum {
    kUserCancelled = -100
    };

#ifdef __cplusplus
extern "C" {
#endif

OSStatus    InitNetworking(NSpGameID inGameID);
void        ShutdownNetworking(void);
OSStatus    DoHost(void);
OSStatus    DoJoin(void);
void        HandleNetwork(void);
void        RefreshWindow(WindowPtr inWindow);
void        HandleNetMenuChoice(short menu, short item);
void        AdjustNetMenus();
void        DoCloseNetWindow(WindowPtr inWindow);

#ifdef __cplusplus
}
#endif

enum {
    kPlayerInputMessage = 1,
    kGameStateMessage,
    kLeaveMessage
    };

#define iJunk       1
#define iNormal     2
#define iRegistered 3
//-------------------
#define iBlocking   5
//-------------------
#define i1X         7
#define i10X        8
#define i30X        9
#define iNoLimit    10
//-------------------
#define iLess500    12
#define i1K         13
#define i10K        14
#define i100K       15
//-------------------
#define iEnumerate  17

typedef struct PlayerInputMessage
{
    NSpMessageHeader    h;
    UInt8               data[100];
} PlayerInputMessage;

typedef struct GameStateMessage
{
    NSpMessageHeader    h;
    UInt8               data[500];
} GameStateMessage;


typedef struct AddPlayerMessage
{
    NSpMessageHeader    h;
    NSpPlayerID         id;
} AddPlayerMessage;

typedef struct WindowStuff
{
    NSpPlayerID     id;
    Str255          text;
    UInt32          lastMessage;
    Boolean         changed;
} WindowStuff;

#endif
```

[Next](Proto.h.md)[Previous](NetStuff.cp.md)

