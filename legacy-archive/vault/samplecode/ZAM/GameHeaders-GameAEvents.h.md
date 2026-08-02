---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/GameHeaders_GameAEvents_h.html
archived_at: '2026-07-18T03:28:32.496804Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](GameHeaders-GameDef.h.md)[Previous](GameHeaders-FixGraf.h.md)

# GameHeaders/GameAEvents.h

```
#pragma once

#define kZAMEventClass          'ZAME'


/* request game apple event & parameters */
#define kRequestGameID      'ZREQ'
    #define keyName             'NAME'
        #define typePStr        'PSTR'

/* accept game apple event & parameters  -- sent as a reply event */
#define kAcceptID           'AK'
#define kTimeID             'TS'

    #define keyAnswer       'ZANS'
//          typeBoolean
//       keyName    
//          typePStr    

// AppleEvents.h
/* send me your map */
#define kSetupMapID         'ZSET'


/* aim  tank in this direction */
#define kRotateTankID               'RTNK'
    #define keyRotateDir            'DREK'
//              typeShortInteger

/* set the speed of my tank to this */
#define kSetTankSpeedID         'SPED'
    #define keySpeed            'kSPD'
//          typeShortInteger


#define kFireMissileID          'FIRE'
    #define keyMissileNum       'MNUM'
//              typeShortInteger
        #define keyDir          'CPAS'  
//              typeShortInteger
    #define keyLocation         'LOCA'
        #define typefixPt       'FXPT'

#define kTankSynchID            'TSYN'
#define keySynchTime            'TTIM'
#define keyTankStatus           'TSTA'
    #define typeTankStatus      'tSTA'
#define keyTankPosition         'TLOC'
//          typefixPt
#define keyTankDirection        'TDIR'
//          typeShortInteger
#define keyTankSpeed            'TSPD'
//          typeShortInteger
#define keyMissilePos           'MPZN'
    #define typefixPtList       'FPLT'


#define kMoveRemoteTankID           'TMOV'
#define kMoveRemoteMissileID        'MMOV'
//          keyMissileNum
//              typeShortInteger
//          keyLocation
//              typefixPt   

#define kGoodByeID              'GBYE'

extern Boolean  gByeNeeded;


//#define NO_NET  1
```

[Next](GameHeaders-GameDef.h.md)[Previous](GameHeaders-FixGraf.h.md)

