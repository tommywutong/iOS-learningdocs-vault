---
title: SonogramViewDemo
apple_id: DTS40008647
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-01-24'
source_url: https://developer.apple.com/library/archive/samplecode/SonogramViewDemo/Listings/Source_CocoaUI_CASonogramView_mm.html
archived_at: '2026-07-18T03:25:01.964789Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SonogramViewDemo](SonogramViewDemo.md)


[Next](Source-CocoaUI-CASonogramViewSharedData.h.md)[Previous](Source-CocoaUI-CASonogramView.h.md)

# Source/CocoaUI/CASonogramView.mm

```objc
/*
    File: CASonogramView.mm
Abstract: n/a
 Version: 1.0.1

Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
Inc. ("Apple") in consideration of your agreement to the following
terms, and your use, installation, modification or redistribution of
this Apple software constitutes acceptance of these terms.  If you do
not agree with these terms, please do not use, install, modify or
redistribute this Apple software.

In consideration of your agreement to abide by the following terms, and
subject to these terms, Apple grants you a personal, non-exclusive
license, under Apple's copyrights in this original Apple software (the
"Apple Software"), to use, reproduce, modify and redistribute the Apple
Software, with or without modifications, in source and/or binary forms;
provided that if you redistribute the Apple Software in its entirety and
without modifications, you must retain this notice and the following
text and disclaimers in all such redistributions of the Apple Software.
Neither the name, trademarks, service marks or logos of Apple Inc. may
be used to endorse or promote products derived from the Apple Software
without specific prior written permission from Apple.  Except as
expressly stated in this notice, no other rights or licenses, express or
implied, are granted by Apple herein, including but not limited to any
patent rights that may be infringed by your derivative works or by other
works in which the Apple Software may be incorporated.

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

Copyright (C) 2012 Apple Inc. All Rights Reserved.

*/

#import "CASonogramView.h"

#define NSRectToCGRect(r) CGRectMake(r.origin.x, r.origin.y, r.size.width, r.size.height)

typedef struct{
    float red;
    float green;
    float blue;
} ColorTriplet;

@implementation CASonogramView

#pragma mark ___Coloing___
- (void) createColormap: (UInt32) mapsize
{
    colormapSize = mapsize;
    if (colormap) free(colormap);
    colormap = (Float32*)calloc(3*mapsize, sizeof(Float32));    

    Float32 bRed = [backgroundColor redComponent];
    Float32 bGreen = [backgroundColor greenComponent];
    Float32 bBlue = [backgroundColor blueComponent];

    Float32 fRed = [lineColor redComponent];
    Float32 fGreen = [lineColor greenComponent];
    Float32 fBlue = [lineColor blueComponent];

    Float32 incrRed = (fRed - bRed)/mapsize;
    Float32 incrGreen = (fGreen - bGreen)/mapsize;
    Float32 incrBlue = (fBlue - bBlue)/mapsize;

    UInt32 index;
    for (UInt32 i = 0; i < mapsize; i++) {
        index = i*3;
        colormap[index] = bRed;
        colormap[index+1] = bGreen;
        colormap[index+2] = bBlue;

        bRed += incrRed;
        bGreen += incrGreen;
        bBlue += incrBlue;      

    }   
}

- (UInt32) skewColor: (Float32) x
{
    UInt32 pos = (UInt32)(x * (colormapSize-1));
    return(pos);
}

- (UInt32)  getIndex: (Float32) value 
            withMin: (Float32) minD 
            andMax: (Float32) maxD 
            andScale: (Float32) scale
{   
    if (maxD < .001) return 0;

    value /= scale;

    Float32 maxDB = 20.0 * log10(1.0 + maxD);   
    Float32 minDB = 20.0 * log10(1.0 + minD);   
    Float32 inDB = 20.0 * log10(1.0 + value);

    Float32 db;
    db = (inDB <= minDB) ? minDB : inDB;
    db = (inDB >= maxDB) ? maxDB : inDB;

    Float32 ratio = (db/maxDB); 
    UInt32 j = [self skewColor: ratio];

    return j;
}

- (ColorTriplet) getColorWithIndex: (UInt32) j 
{   
    ColorTriplet c;
    UInt32 index = j*3;
    c.red =  colormap[index];
    c.green = colormap[index+1];
    c.blue = colormap[index+2];
    return c;
}



#pragma mark ___Initialize___


- (void) setStaticView: (BOOL) isStatic
{
    isStaticView = isStatic;
}

- (void) InitializeBuffers
{   
    [self createColormap: mNumBins];    

    UInt32 numBytesPerFrame = mNumBins*4*sizeof(unsigned char); // rgba

    if (mRingBuffer) delete(mRingBuffer);
    mRingBuffer = new CARingBuffer();
    mRingBuffer->Allocate(1, numBytesPerFrame, mNumSlicesTotal);

    mRingBufferCounter = 0; 
    mRenderCounter = 0;

    UInt32 numTotalBytes = numBytesPerFrame*mNumSlicesTotal;

    CAStreamBasicDescription    bufClientDesc;      
    bufClientDesc.SetCanonical(1, false);
    if(mFetchingBufferList) {
        mFetchingBufferList->DeallocateBuffers();
        delete(mFetchingBufferList);
    }
    mFetchingBufferList = CABufferList::New("fetch buffer", bufClientDesc );
    mFetchingBufferList->AllocateBuffers(numTotalBytes);

    if(mStoringBufferList) {
        mStoringBufferList->DeallocateBuffers();
        delete(mStoringBufferList);
    }
    mStoringBufferList = CABufferList::New("store buffer", bufClientDesc );
    mStoringBufferList->AllocateBuffers(numTotalBytes);


    storing = false;    
}



- (void) Initialize
{
    backgroundColor = [[NSColor colorWithCalibratedRed: 0 green: 0 blue: 0 alpha:1]retain];
    lineColor = [[NSColor colorWithCalibratedRed: 1 green: 1 blue: 1 alpha:1]retain];

    [myBackgroundWell setColor:backgroundColor];        
    [myLineWell setColor: lineColor];

    mNumSlicesTotal = (UInt32) ([self frame].size.width);       
    mNumBinsTotal = (UInt32) ([self frame].size.height);        

    mRingBufferCounter = 0; 
    mRenderCounter = 0;

    [self InitializeBuffers];

    isStaticView = false;

}

- (id)initWithFrame:(NSRect)frame 
{
    self = [super initWithFrame:frame];
    if (self) {
        [self Initialize];
   }
    return self;
}


- (void) dealloc
{
    if (backgroundColor) [backgroundColor release];
    if (lineColor) [lineColor release]; 

    if (colormap) free(colormap);;

    if (mRingBuffer) delete(mRingBuffer);
    if (mFetchingBufferList) delete(mFetchingBufferList);
    if (mStoringBufferList) delete(mStoringBufferList);

    [super dealloc];
}


#pragma mark ___IBActions___

- (void) setLineColor:(NSColor*) color
{
    if ( color != lineColor ) {
        [color retain];
        [lineColor release];
        lineColor = color;
    }
}

- (void) setBackgroundColor:(NSColor*) color
{
    if ( color != backgroundColor ) {
        [color retain];
        [backgroundColor release];
        backgroundColor =  color;
    }
}

- (IBAction) changeBackgroundColor: (id) sender
{
    [self setBackgroundColor : [sender color]];
    [self createColormap: mNumBins];    
    [self setNeedsDisplay: YES];
}

- (IBAction) changeLineColor: (id) sender
{
    [self  setLineColor: [sender color]];
    [self createColormap: mNumBins];    
    [self setNeedsDisplay: YES];
}

- (IBAction) changeDistortion: (id) sender
{
    [self setNeedsDisplay: YES];
}

#pragma mark ___Reading___

- (bool) storing
{ 
    return storing;
}


#pragma mark ___Drawing___
- (void) storeSlices: (SonogramOverview*) data
{   
    if([myHoldButton state] == NSOnState) return;

    storing = true;

    if (mNumBins != data->mNumBins){
        mNumBins =  data->mNumBins;
        [self InitializeBuffers];
    }

    mNumSlices = data->mNumSlices;

    Float32 linmin = data->mMinAmp;
    Float32 linmax = data->mMaxAmp;

    UInt32 numBytesPerRow = mNumBins*4*sizeof(unsigned char);   //rgba

    AudioBufferList* mStoringList = &mStoringBufferList->GetModifiableBufferList(); 
    unsigned char* bitmapImageSliceBits = (unsigned char*) mStoringList->mBuffers[data->mChannel].mData;


    Float32 linmag; 
    UInt32  index, index1, index2;
    ColorTriplet c;

    for (UInt32 j = 0; j < mNumSlices; j++) {   // for each frame   
        for (UInt32 i = 0; i < mNumBins; i++) {     // for each frequency

            index1 = i + j*mNumBins;
            linmag  = data->mOverview[index1];  

            if  (isnan(linmag)) linmag = 0.0;

            index = [self getIndex: linmag withMin: linmin andMax: linmax andScale: 1.0];
            c = [self getColorWithIndex: index];


            index2 = i*4 + j*numBytesPerRow;


            bitmapImageSliceBits[index2  ] = 255;
            bitmapImageSliceBits[index2+1] = (unsigned char) (255*c.red);
            bitmapImageSliceBits[index2+2] = (unsigned char) (255*c.green);
            bitmapImageSliceBits[index2+3] = (unsigned char) (255*c.blue);      

        }
    }    

    //store
    mRingBuffer->Store(mStoringList, mNumSlices, mRingBufferCounter);
    if (!isStaticView)
        mRingBufferCounter += mNumSlices;

    [self setNeedsDisplay: YES];

    storing = false;

}


- (void)drawRect:(NSRect)rect
{   
    [super drawRect: rect];

    if (!mRingBuffer) return;
    AudioBufferList* fetchBufferList = &mFetchingBufferList->GetModifiableBufferList(); 

    // fetch    
    SInt64 newNum = mRingBufferCounter-mRenderCounter;
#if __MAC_OS_X_VERSION_MIN_REQUIRED < 1070
    mRingBuffer->Fetch(fetchBufferList, mNumSlicesTotal, mRingBufferCounter, true);
#else
    mRingBuffer->Fetch(fetchBufferList, mNumSlicesTotal, mRingBufferCounter);
#endif
    if (!isStaticView)
        mRenderCounter += newNum;

    unsigned char* bitmapImageBits = (unsigned char*) fetchBufferList->mBuffers[0].mData;

    UInt32 numBytesPerRow = mNumBins*4*sizeof(unsigned char); 
    UInt32 numTotalBytes = mNumSlicesTotal*numBytesPerRow;

    NSData* bitmapData = [[NSData alloc] initWithBytesNoCopy:bitmapImageBits length:numTotalBytes freeWhenDone:NO];

    CGColorSpaceRef colorSpace = CGColorSpaceCreateDeviceRGB();
    CIImage* mSpectrumImage = [[CIImage alloc] initWithBitmapData : bitmapData
                                                      bytesPerRow : numBytesPerRow 
                                                             size :  CGSizeMake( (Float32) mNumSlicesTotal, (Float32) mNumBins)
                                                           format : kCIFormatARGB8
                                                       colorSpace : colorSpace];
    CGColorSpaceRelease(colorSpace);

    NSRect drawRect = rect;

    // affine transform
    NSRect sonogramImageRect = NSMakeRect(0, 0, mNumSlicesTotal, mNumBins); 

    NSAffineTransform* yFlip = [NSAffineTransform transform];
    [yFlip rotateByDegrees: 90];
    [yFlip translateXBy: 0.0 yBy: -sonogramImageRect.size.height];

    CIFilter* flipYTransform = [CIFilter filterWithName: @"CIAffineTransform"]; 
    [flipYTransform setValue: yFlip forKey: @"inputTransform"]; 
    [flipYTransform setValue: mSpectrumImage forKey: @"inputImage"];    
    CIImage* affineOutputImage = [flipYTransform valueForKey: @"outputImage"];

    if ([myDistortionButton selectedRow] == 1){     
        CIFilter* bumpDistortion = [CIFilter filterWithName: @"CIBumpDistortion"];
        [bumpDistortion setValue: affineOutputImage forKey: @"inputImage"];
        [bumpDistortion setValue: [CIVector vectorWithX:512 Y:0] forKey: @"inputCenter"];
        [bumpDistortion setValue: [NSNumber numberWithFloat: 512] forKey: @"inputRadius"];
        [bumpDistortion setValue: [NSNumber numberWithFloat: 0.60] forKey: @"inputScale"];
        CIImage* bumpOutputImage = [bumpDistortion valueForKey: @"outputImage"];

        [bumpOutputImage drawInRect: drawRect 
                            fromRect:  sonogramImageRect
                            operation: NSCompositeCopy
                            fraction: 1.0];
    }
    else if ([myDistortionButton selectedRow] == 2){ // only on Leopard 
        CIFilter* bumpDistortion = [CIFilter filterWithName: @"CIBumpDistortionLinear"];
        [bumpDistortion setValue: affineOutputImage forKey: @"inputImage"];
        [bumpDistortion setValue: [CIVector vectorWithX:512 Y:0] forKey: @"inputCenter"];
        [bumpDistortion setValue: [NSNumber numberWithFloat: 1024] forKey: @"inputRadius"];
        [bumpDistortion setValue: [NSNumber numberWithFloat: 0.30] forKey: @"inputScale"];
        [bumpDistortion setValue: [NSNumber numberWithFloat: M_PI * 0.5] forKey: @"inputAngle"];
        CIImage* bumpOutputImage = [bumpDistortion valueForKey: @"outputImage"];

        [bumpOutputImage drawInRect: drawRect 
                            fromRect:  sonogramImageRect
                            operation: NSCompositeCopy
                            fraction: 1.0]; 
    }
    else {
        [affineOutputImage drawInRect: drawRect 
                            fromRect:  sonogramImageRect
                            operation: NSCompositeCopy 
                            fraction: 1.0];
    }

    [bitmapData release];
    [mSpectrumImage release];

}



@end
```

[Next](Source-CocoaUI-CASonogramViewSharedData.h.md)[Previous](Source-CocoaUI-CASonogramView.h.md)

