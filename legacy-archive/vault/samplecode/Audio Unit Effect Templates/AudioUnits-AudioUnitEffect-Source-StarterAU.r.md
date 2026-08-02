---
title: Audio Unit Effect Templates
apple_id: DTS10003458
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2005-06-06'
source_url: https://developer.apple.com/library/archive/samplecode/AudioUnitEffectTemplates/Listings/Audio_Units_Audio_Unit_Effect_Source_StarterAU_r.html
archived_at: '2026-07-18T03:01:32.072941Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Effect Templates](Audio%20Unit%20Effect%20Templates.md)


[Next](AudioUnits-AudioUnitEffect-Source-StarterAUVersion.h.md)[Previous](AudioUnits-AudioUnitEffect-Source-StarterAU.h.md)

# Audio_Units/Audio_Unit_Effect/Source/StarterAU.r

```c
/*
*   File:       ÇPROJECTNAMEÈ.r
*   
*   Version:    1.0
* 
*   Created:    ÇDATEÈ
*   
*   Copyright:  Copyright © ÇYEARÈ ÇORGANIZATIONNAMEÈ, All Rights Reserved
* 
*   Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple Computer, Inc. ("Apple") in 
*               consideration of your agreement to the following terms, and your use, installation, modification 
*               or redistribution of this Apple software constitutes acceptance of these terms.  If you do 
*               not agree with these terms, please do not use, install, modify or redistribute this Apple 
*               software.
*
*               In consideration of your agreement to abide by the following terms, and subject to these terms, 
*               Apple grants you a personal, non-exclusive license, under Apple's copyrights in this 
*               original Apple software (the "Apple Software"), to use, reproduce, modify and redistribute the 
*               Apple Software, with or without modifications, in source and/or binary forms; provided that if you 
*               redistribute the Apple Software in its entirety and without modifications, you must retain this 
*               notice and the following text and disclaimers in all such redistributions of the Apple Software. 
*               Neither the name, trademarks, service marks or logos of Apple Computer, Inc. may be used to 
*               endorse or promote products derived from the Apple Software without specific prior written 
*               permission from Apple.  Except as expressly stated in this notice, no other rights or 
*               licenses, express or implied, are granted by Apple herein, including but not limited to any 
*               patent rights that may be infringed by your derivative works or by other works in which the 
*               Apple Software may be incorporated.
*
*               The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO WARRANTIES, EXPRESS OR 
*               IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY 
*               AND FITNESS FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND OPERATION ALONE 
*               OR IN COMBINATION WITH YOUR PRODUCTS.
*
*               IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR CONSEQUENTIAL 
*               DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS 
*               OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, 
*               REPRODUCTION, MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED AND WHETHER 
*               UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE), STRICT LIABILITY OR OTHERWISE, EVEN 
*               IF APPLE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*
*/
#include <AudioUnit/AudioUnit.r>

#include "ÇPROJECTNAMEÈVersion.h"

// Note that resource IDs must be spaced 2 apart for the 'STR ' name and description
#define kAudioUnitResID_ÇPROJECTNAMEÈ               1000

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ÇPROJECTNAMEÈ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#define RES_ID          kAudioUnitResID_ÇPROJECTNAMEÈ
#define COMP_TYPE       kAudioUnitType_Effect
#define COMP_SUBTYPE    ÇPROJECTNAMEÈ_COMP_SUBTYPE
#define COMP_MANUF      ÇPROJECTNAMEÈ_COMP_MANF 

#define VERSION         kÇPROJECTNAMEÈVersion
#define NAME            "ÇORGANIZATIONNAMEÈ: ÇPROJECTNAMEÈ"
#define DESCRIPTION     "ÇPROJECTNAMEÈ AU"
#define ENTRY_POINT     "ÇPROJECTNAMEÈEntry"

#include "AUResources.r"
```

[Next](AudioUnits-AudioUnitEffect-Source-StarterAUVersion.h.md)[Previous](AudioUnits-AudioUnitEffect-Source-StarterAU.h.md)

