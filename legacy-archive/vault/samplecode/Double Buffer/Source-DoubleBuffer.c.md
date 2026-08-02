---
title: Double Buffer
apple_id: DTS10000344
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Double_Buffer/Listings/Source_DoubleBuffer_c.html
archived_at: '2026-07-18T03:07:08.139253Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Double Buffer](Double%20Buffer.md)


[Next](Document%20Revision%20History.md)[Previous](Resource-DoubleBufferPPC.r.md)

# Source/DoubleBuffer.c

```c
#include    <Resources.h>
#include    <Sound.h>
#include    <Memory.h>

#define TRUE            0xFF
#define FALSE           0
#define kDoubleBufferSize   0x1000

struct LocalVars {
    long    bytesTotal;
    long    bytesCopied;
    Ptr     dataPtr;
};

typedef struct LocalVars LocalVars;
typedef LocalVars *LocalVarsPtr;

pascal void MyDoubleBackProc (SndChannelPtr channel,
                                            SndDoubleBufferPtr doubleBufferPtr);

void main()
{
SndDoubleBufferHeader   doubleHeader;
SndDoubleBufferPtr      doubleBuffer;
int                     i;
OSErr                   err;
SCStatus                Stats;
SndChannelPtr           chan;
SoundHeaderPtr          Head;
Handle                  SoundData;
LocalVars               myVars;

SoundData = GetResource ('snd ', 100);
if (ResError() != noErr || SoundData == nil)
    Debugger();
HLock (SoundData);

chan = nil;
err = SndNewChannel (&chan, sampledSynth, 0, nil);
if (err != noErr)
    Debugger();

Head = (SoundHeaderPtr) NewPtrClear (sizeof(SoundHeader));
Head->samplePtr = *SoundData;
Head->length = 45838;
Head->sampleRate = 0x56EE8BA3;      //recorded at 22KHz
Head->loopStart = 0;
Head->loopEnd = 0;
Head->encode = 0;
Head->baseFrequency = 60;
Head->sampleArea[0] = 0;

myVars.bytesTotal = Head->length;
myVars.bytesCopied = 0;
myVars.dataPtr = Head->samplePtr;

doubleHeader.dbhNumChannels = 1;
doubleHeader.dbhSampleSize = 8;
doubleHeader.dbhCompressionID = 0;
doubleHeader.dbhPacketSize = 0;
doubleHeader.dbhSampleRate = Head->sampleRate;

/* create a UPP for the SndDoubleBackProc */
doubleHeader.dbhDoubleBack = NewSndDoubleBackProc (MyDoubleBackProc);

for (i = 0; i <= 1; ++i) {
    doubleBuffer = (SndDoubleBufferPtr) NewPtrClear (sizeof(SndDoubleBuffer) + kDoubleBufferSize);

    if (doubleBuffer == nil || MemError() != 0)
        Debugger();

    doubleBuffer->dbNumFrames = 0;
    doubleBuffer->dbFlags = 0;
    doubleBuffer->dbUserInfo [0] = (long) &myVars;

    MyDoubleBackProc (chan, doubleBuffer);          // initialize the buffers

    doubleHeader.dbhBufferPtr [i] = doubleBuffer;
    }

err = SndPlayDoubleBuffer (chan, &doubleHeader);
if (err != noErr)
    Debugger();

do {
    err = SndChannelStatus (chan, sizeof (Stats), &Stats);
    } while (Stats.scChannelBusy);

for (i = 0; i <= 1; ++i)
    DisposePtr ((Ptr) doubleHeader.dbhBufferPtr[i]);

err = SndDisposeChannel (chan,FALSE);
if (err != noErr)
    Debugger();

HUnlock (SoundData);
}
/**********************************/

pascal void MyDoubleBackProc (SndChannelPtr chan,SndDoubleBufferPtr doubleBuffer)
{
#pragma unused (chan)

LocalVarsPtr    myVarsPtr;
long            bytesToCopy;

myVarsPtr = (LocalVarsPtr) doubleBuffer->dbUserInfo[0];
bytesToCopy = myVarsPtr->bytesTotal - myVarsPtr->bytesCopied;

if (bytesToCopy > kDoubleBufferSize)
    bytesToCopy = kDoubleBufferSize;

BlockMove (myVarsPtr->dataPtr, &doubleBuffer->dbSoundData[0], bytesToCopy);

doubleBuffer->dbNumFrames = bytesToCopy;
doubleBuffer->dbFlags = (doubleBuffer->dbFlags) | dbBufferReady;

myVarsPtr->dataPtr = (Ptr) ((myVarsPtr->dataPtr) + bytesToCopy);
myVarsPtr->bytesCopied = myVarsPtr->bytesCopied + bytesToCopy;

if (myVarsPtr->bytesCopied == myVarsPtr->bytesTotal)
    doubleBuffer->dbFlags = (doubleBuffer->dbFlags) | dbLastBuffer;

return;
}

/**********************************/
```

[Next](Document%20Revision%20History.md)[Previous](Resource-DoubleBufferPPC.r.md)

