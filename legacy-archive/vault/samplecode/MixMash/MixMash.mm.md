---
title: MixMash
apple_id: DTS40008646
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2009-04-15'
source_url: https://developer.apple.com/library/archive/samplecode/MixMash/Listings/MixMash_mm.html
archived_at: '2026-07-18T03:15:00.477176Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MixMash](MixMash.md)


[Next](Document%20Revision%20History.md)[Previous](MixMash.h.md)

# MixMash.mm

```objc
/*  Copyright © 2007 Apple Inc. All Rights Reserved.

    Disclaimer: IMPORTANT:  This Apple software is supplied to you by 
            Apple Inc. ("Apple") in consideration of your agreement to the
            following terms, and your use, installation, modification or
            redistribution of this Apple software constitutes acceptance of these
            terms.  If you do not agree with these terms, please do not use,
            install, modify or redistribute this Apple software.

            In consideration of your agreement to abide by the following terms, and
            subject to these terms, Apple grants you a personal, non-exclusive
            license, under Apple's copyrights in this original Apple software (the
            "Apple Software"), to use, reproduce, modify and redistribute the Apple
            Software, with or without modifications, in source and/or binary forms;
            provided that if you redistribute the Apple Software in its entirety and
            without modifications, you must retain this notice and the following
            text and disclaimers in all such redistributions of the Apple Software. 
            Neither the name, trademarks, service marks or logos of Apple Inc. 
            may be used to endorse or promote products derived from the Apple
            Software without specific prior written permission from Apple.  Except
            as expressly stated in this notice, no other rights or licenses, express
            or implied, are granted by Apple herein, including but not limited to
            any patent rights that may be infringed by your derivative works or by
            other works in which the Apple Software may be incorporated.

            The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
            MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
            THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
            FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
            OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

            IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
            OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
            SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
            INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
            MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
            AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
            STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
            POSSIBILITY OF SUCH DAMAGE.
*/
#import "MixMash.h"
#include <AudioUnit/AudioUnit.h>
#include <vector>
#include "CAComponentDescription.h"
#include "CAXException.h"
#include "CAStreamBasicDescription.h"

#define kAudioPlaybackSampleRate    44100
#define kDefaultTotalTime           30
#define kDefaultMinSliceLength      0.050
#define kDefaultMaxSliceLength      0.250

OSStatus FilePlayerRenderCallback(
                        void *                          inRefCon,
                        AudioUnitRenderActionFlags *    ioActionFlags,
                        const AudioTimeStamp *          inTimeStamp,
                        UInt32                          inBusNumber,
                        UInt32                          inNumberFrames,
                        AudioBufferList *               ioData)
{
    MixMash *This = (MixMash *)inRefCon;

    if (!This->mHaveStartTime) {
        AudioTimeStamp ts;
        UInt32 propertySize = sizeof(ts);
        OSStatus err = AudioUnitGetProperty(This->mPlayerUnit, kAudioUnitProperty_ScheduleStartTimeStamp, kAudioUnitScope_Global, 0, &ts, &propertySize);
        if (!err && (ts.mFlags & kAudioTimeStampSampleTimeValid) && ts.mSampleTime >= 0.) {
            This->mStartSample = ts.mSampleTime;
            This->mHaveStartTime = YES;
        }
    }
    This->mCurrentTime = inTimeStamp->mSampleTime;
    return noErr;
}

@implementation MixMash
- (id)init
{
    self = [super init];
    if (self) {
        mTotalLength = kDefaultTotalTime;
        mMinSliceLength = kDefaultMinSliceLength;
        mMaxSliceLength = kDefaultMaxSliceLength;
        mAudioFiles = new AudioFileList;
        mRegionList = new RegionList;
        mPlayRow = -1;

        AUNode theOutputNode, thePlayerNode;
        AudioUnit theOutputUnit;
        CAStreamBasicDescription theAudioFormat;

        // create and open the graph
        XThrowIfError(
            NewAUGraph(&mGraph),
            "NewAUGraph failed");
        XThrowIfError(
            AUGraphOpen(mGraph),
            "couldn't open graph");

        // add an output unit
        CAComponentDescription outputDesc(kAudioUnitType_Output, kAudioUnitSubType_DefaultOutput, kAudioUnitManufacturer_Apple);
        XThrowIfError(
            AUGraphAddNode(mGraph, &outputDesc, &theOutputNode),
            "couldn't create node for output unit");
        XThrowIfError(
            AUGraphNodeInfo(mGraph, theOutputNode, NULL, &theOutputUnit),
            "couldn't get output unit from node");

        // add a file player
        CAComponentDescription playerDesc(kAudioUnitType_Generator, kAudioUnitSubType_AudioFilePlayer, kAudioUnitManufacturer_Apple);
        XThrowIfError(
            AUGraphAddNode(mGraph, &playerDesc, &thePlayerNode),
            "couldn't create node for file player");
        XThrowIfError(
            AUGraphNodeInfo(mGraph, thePlayerNode, NULL, &mPlayerUnit),
            "couldn't get player unit from node");

        //set the render callback
        XThrowIfError(
            AudioUnitAddRenderNotify(mPlayerUnit, FilePlayerRenderCallback, self),
            "couldn't set file player render callback");

        // Make the player's output format -- in terms of sample rate and number of channels.
        // The player will convert to deinterleaved float.
        theAudioFormat.mSampleRate = kAudioPlaybackSampleRate;  
        theAudioFormat.SetCanonical(2, false /* deinterleaved */);
        XThrowIfError(
            AudioUnitSetProperty(mPlayerUnit, kAudioUnitProperty_StreamFormat, kAudioUnitScope_Output, 0, &theAudioFormat, sizeof(CAStreamBasicDescription)),
            "couldn't set player's output stream format");

        // connect the player to the output unit (stream format will propagate)
        XThrowIfError(
            AUGraphConnectNodeInput(mGraph, thePlayerNode, 0, theOutputNode, 0),
            "couldn't connect mixer to output unit");

        // initialize the AUGraph
        XThrowIfError(
            AUGraphInitialize(mGraph),
            "couldn't initialize graph");
        XThrowIfError(AUGraphStart(mGraph), "couldn't start graph");

        // set the image to display the current file being played
        mSpeakerImage = [NSImage imageNamed: @"Speaker.tiff"];

        // set a default path for sources
        mSourcePath = @"/System/Library/Sounds";
    }
    return self;
}

- (void)awakeFromNib
{
    [mFolderName setStringValue: [mSourcePath lastPathComponent]];
}

- (void)closeFiles
{
    for (AudioFileList::iterator it = mAudioFiles->begin(); it != mAudioFiles->end(); ++it) {
        AudioFileClose((*it).fileid);
        [(*it).description release];
    }
    mAudioFiles->clear();
}

- (void)dealloc
{
    [self closeFiles];
    delete mAudioFiles;
    delete mRegionList;
    [super dealloc];
}

class CmpRgnTime {
public:
    bool operator () (Float64 t, ScheduledAudioFileRegion &a)
    {
        return a.mTimeStamp.mSampleTime > t;
    }
};

- (void)updatePlayLoc
{
    if (!mHaveStartTime)
        return;
    Float64 pos = mCurrentTime - mStartSample;
    int row;
    if (pos >= mTotalLengthSamples)
        row = -1;
    else {
        RegionList::iterator i = std::upper_bound(mRegionList->begin(), mRegionList->end(), pos, CmpRgnTime());
        row = i - mRegionList->begin() - 1;
    }

    if (row != mPlayRow) {
        mPlayRow = row;
        if (mPlayRow >= 0)
            [mPlaylistTable scrollRowToVisible: mPlayRow];
        [mPlaylistTable reloadData];
        if (row == -1)
            [self stop];
    }
}

- (void)play
{
    if (mPlaying) return;
    OSStatus err;
    AudioUnitReset(mPlayerUnit, kAudioUnitScope_Global, 0);

    // give the player the array of AudioFileIDs it will be playing
    AudioFileID *fileids = new AudioFileID[mAudioFiles->size()], *pf = fileids;
    for (AudioFileList::iterator fi = mAudioFiles->begin(); fi != mAudioFiles->end(); ++fi)
        *pf++ = (*fi).fileid;

    XThrowIfError(
        AudioUnitSetProperty(mPlayerUnit, kAudioUnitProperty_ScheduledFileIDs, kAudioUnitScope_Global, 0, fileids, mAudioFiles->size() * sizeof(AudioFileID)),
        "couldn't set the player's list of AudioFileID's");
    delete[] fileids;

    // schedule events
    for (RegionList::iterator it = mRegionList->begin(); it != mRegionList->end(); ++it) {
        err = AudioUnitSetProperty(mPlayerUnit, kAudioUnitProperty_ScheduledFileRegion, kAudioUnitScope_Global, 0, &(*it), sizeof(ScheduledAudioFileRegion));
        if (err)
            printf("schedule region: error %ld\n", (long int)err);
    }
    UInt32 primeFrames = 0; // default
    AudioUnitSetProperty(mPlayerUnit, kAudioUnitProperty_ScheduledFilePrime, kAudioUnitScope_Global, 0, &primeFrames, sizeof(primeFrames));

    AudioTimeStamp startTime;
    startTime.mFlags = kAudioTimeStampSampleTimeValid;
    startTime.mSampleTime = -1;
    AudioUnitSetProperty(mPlayerUnit, kAudioUnitProperty_ScheduleStartTimeStamp, kAudioUnitScope_Global, 0, &startTime, sizeof(startTime));
    mPlaying = YES;
    mHaveStartTime = NO;
    [mPlayButton setTitle: @"Stop"];

    mPlayTimer = [NSTimer scheduledTimerWithTimeInterval:0.040 target:self selector:@selector(updatePlayLoc)
                        userInfo:nil repeats:YES];
}

- (void)stop
{
    if (!mPlaying) return;

    AudioUnitReset(mPlayerUnit, kAudioUnitScope_Global, 0);
    mPlaying = NO;
    [mPlayButton setTitle: @"Play"];
    mPlayRow = -1;
    [mPlayTimer invalidate];
    mPlayTimer = nil;
}

static int randChoice(int n)
{
    return random() % n;
}

static double frand()
{
    return (double)random() / (double)RAND_MAX;
}

- (void)findAudioFilesInFolder: (NSString *)folder fileList: (NSMutableArray *)files
{
    NSFileManager *fm = [NSFileManager defaultManager];
    NSArray *subs = [fm directoryContentsAtPath: folder];
    NSEnumerator *e = [subs objectEnumerator];
    NSString *s;
    while ((s = [e nextObject]) != nil) {
        NSString *path = [folder stringByAppendingPathComponent: s];
        BOOL isDir;
        if ([fm fileExistsAtPath: path isDirectory: &isDir]) {
            if (isDir)
                [self findAudioFilesInFolder: path fileList: files];
            else {
                const char *ext = [[s pathExtension] cStringUsingEncoding: NSASCIIStringEncoding];
                if (!strcmp(ext, "aif") || !strcmp(ext, "wav") || !strcmp(ext, "mp3")
                 || !strcmp(ext, "aiff") || !strcmp(ext, "sd2") || !strcmp(ext, "aac")) {
                    [files addObject: path];
                }
            }
        }
    }
}

- (NSMutableArray *)audioFilesInFolder: (NSString *)folder
{
    NSMutableArray *files = [[[NSMutableArray alloc] init] autorelease];
    [self findAudioFilesInFolder: folder fileList: files];
    return files;
}

- (IBAction)generatePlaylist: (id)sender
{
    [self stop];
    [self closeFiles];
    mRegionList->clear();

    Float64 playTime = 0;
    Float64 endTime = mTotalLength * 44100;
    NSMutableArray *paths;

    paths = [self audioFilesInFolder: mSourcePath];
    if ([paths count] == 0)
        return;

    bool gotTooManyFilesOpen = false;
    mTotalLengthSamples = 0;
    while (playTime < endTime) {
        // pick a random file
        AudioFile af;
        if (!gotTooManyFilesOpen && [paths count]) {
            // from a file we haven't played from
            int i = randChoice([paths count]);
            NSString *filePath = [paths objectAtIndex: i];
            // remove it from the list so we don't pick again
            [paths removeObjectAtIndex: i];

            printf("file: %s\n", [filePath cStringUsingEncoding: NSASCIIStringEncoding]);

            // try to open the audio file
            OSStatus err;
            FSRef fsref;
            err = FSPathMakeRef((Byte *)[filePath UTF8String], &fsref, NULL);
            if (err) { printf("FSPathMakeRef: %ld\n", (long int)err); continue; }
            err = AudioFileOpen(&fsref, fsRdPerm, 0, &af.fileid);
            if (err) { 
                if (err == tmfoErr) {
                    gotTooManyFilesOpen = true;
                    continue;
                }
                printf("AudioFileOpen: %ld\n", (long int)err); continue;
            }

            // get its sample rate and duration
            UInt32 propsize = sizeof(af.filefmt);
            err = AudioFileGetProperty(af.fileid, kAudioFilePropertyDataFormat, &propsize, &af.filefmt);
            if (err || af.filefmt.mFramesPerPacket == 0 /* no VBR */) {
                printf("get data format: err=%ld framesperpacket=%ld\n", (long int)err, (long int)af.filefmt.mFramesPerPacket);
                AudioFileClose(af.fileid);
                continue;
            }

            propsize = sizeof(UInt64);
            err = AudioFileGetProperty(af.fileid, kAudioFilePropertyAudioDataPacketCount, &propsize, &af.npackets);
            if (err || af.npackets == 0) {
                printf("get data packet count: err=%ld npackets=%qd\n", (long int)err, af.npackets);
                AudioFileClose(af.fileid);
                continue;
            }

            // generate description
            char buf[64];

            if (af.filefmt.mChannelsPerFrame > 2)
                sprintf(buf, "%ld ch", (long int)af.filefmt.mChannelsPerFrame);
            else
                strcpy(buf, af.filefmt.mChannelsPerFrame == 2 ? "stereo" : "mono");
            if (af.filefmt.mFormatID == kAudioFormatLinearPCM) {
                sprintf(buf + strlen(buf), ", %ld-bit %s", (long int)af.filefmt.mBitsPerChannel, (af.filefmt.mFormatFlags & kLinearPCMFormatFlagIsFloat) ? "float" : "integer");
            }
            if (af.filefmt.mSampleRate != 0)
                sprintf(buf + strlen(buf), ", %.f Hz", af.filefmt.mSampleRate);

            af.description = [[NSString stringWithFormat: @"%@\n%s", [filePath lastPathComponent], buf] retain];
            mAudioFiles->push_back(af);
        } else if (mAudioFiles->size() == 0) {
            break;
        } else {
            // from a file we've already played from
            int i = randChoice(mAudioFiles->size());
            af = (*mAudioFiles)[i];
        }

        Float64 fileDuration = (af.npackets * af.filefmt.mFramesPerPacket) / af.filefmt.mSampleRate;
        Float64 sliceDuration = std::min(frand() * (mMaxSliceLength - mMinSliceLength) + mMinSliceLength, fileDuration);
        Float64 sliceStart = frand() * (fileDuration - sliceDuration);

        ScheduledAudioFileRegion rgn;
        rgn.mTimeStamp.mFlags = kAudioTimeStampSampleTimeValid;
        rgn.mTimeStamp.mSampleTime = playTime;
        rgn.mCompletionProc = NULL;
        rgn.mCompletionProcUserData = NULL;
        rgn.mAudioFile = af.fileid;
        rgn.mLoopCount = 0;
        rgn.mStartFrame = SInt64(sliceStart * af.filefmt.mSampleRate);
        rgn.mFramesToPlay = UInt32(sliceDuration * af.filefmt.mSampleRate);
        printf("  t: %.3f : %ld frames @ frame %qd\n", playTime / 44100., (long int)rgn.mFramesToPlay, rgn.mStartFrame);
        mRegionList->push_back(rgn);

        playTime += ceil(sliceDuration * kAudioPlaybackSampleRate);  
        [mPlaylistTable reloadData];
        [mPlaylistTable scrollRowToVisible: mRegionList->size() - 1];
        [mPlaylistTable displayIfNeeded];
    }
    mTotalLengthSamples = playTime;
    [mPlaylistTable scrollRowToVisible: 0];
}

- (IBAction)togglePlay: (id)sender
{
    if (mPlaying) {
        [self stop];
    } else {
        [self play];
    }
}

- (int)numberOfRowsInTableView:(NSTableView *)tableView
{
    return mRegionList->size();
}

NSString *formatSample(UInt64 sample, Float64 rate, bool millis)
{
    char buf[32];
    double seconds = double(sample) / rate;
    int milliseconds = int(seconds * 1000 + 0.5);
    int minutes = milliseconds / 60000;
    milliseconds %= 60000;
    int isec = milliseconds / 1000;
    milliseconds %= 1000;
    if (minutes)
        sprintf(buf, "%2d:%02d.%03d", minutes, isec, milliseconds);
    else
        sprintf(buf, "   %2d.%03d", isec, milliseconds);
    return [NSString stringWithUTF8String: buf];
}

- (AudioFile *)FileForRegion: (ScheduledAudioFileRegion *)rgn
{
    AudioFile *af = NULL;
    for (AudioFileList::iterator i = mAudioFiles->begin(); i != mAudioFiles->end(); ++i)
        if ((*i).fileid == rgn->mAudioFile) {
            af = &(*i);
            break;
        }
    return af;
}

- (id)tableView:(NSTableView *)tableView objectValueForTableColumn:(NSTableColumn *)tableColumn row:(int)row
{
    ScheduledAudioFileRegion *rgn = &(*mRegionList)[row];
    AudioFile *af = [self FileForRegion: rgn];
    if (af == NULL)
        return nil;
    if (tableColumn == mPlayLocColumn) {
        return (row == mPlayRow) ? mSpeakerImage : nil;
    } else if (tableColumn == mFileColumn) {
        return af->description;
    } else if (tableColumn == mStartColumn) {
        int seconds = int(rgn->mStartFrame / af->filefmt.mSampleRate + 0.5);
        int minutes = seconds / 60;
        seconds %= 60;
        return [NSString stringWithFormat: @"%d:%02d", minutes, seconds];
    } else if (tableColumn == mLengthColumn) {
        double s = rgn->mFramesToPlay / af->filefmt.mSampleRate;
        return [NSString stringWithFormat: @"%.3f", s];
    }
    return nil;
}

// optional
- (void)tableView:(NSTableView *)tableView setObjectValue:(id)object forTableColumn:(NSTableColumn *)tableColumn row:(int)row
{
    ScheduledAudioFileRegion *rgn = &(*mRegionList)[row];
    AudioFile *af = [self FileForRegion: rgn];
    if (af == NULL)
        return;
    if (tableColumn == mLengthColumn) {
        double s = [object doubleValue];
        rgn->mFramesToPlay = UInt32(s * af->filefmt.mSampleRate);
    }
}

- (IBAction)setFolder: (id)sender
{
    NSOpenPanel *panel = [NSOpenPanel openPanel];
    [panel setCanChooseDirectories: YES];
    [panel setCanChooseFiles: NO];
    if ([panel runModalForDirectory: mSourcePath file: nil types: nil] == NSOKButton) {
        [mSourcePath release];
        mSourcePath = [[panel filename] retain];
        [mFolderName setStringValue: [mSourcePath lastPathComponent]];
    }
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](MixMash.h.md)

