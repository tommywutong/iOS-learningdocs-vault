---
title: DTSCPlusLibrary
apple_id: DTS10000731
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/DTSCPlusLibrary/Listings/Headers_Template_h.html
archived_at: '2026-07-18T03:05:53.598095Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DTSCPlusLibrary](DTSCPlusLibrary.md)


[Next](Headers-Timer.h.md)[Previous](Headers-SpinCursor.h.md)

# Headers/Template.h

```c
/*
    File:       Template.h

    Contains:   

    Written by: Kent Sandvik    

    Copyright:  Copyright © 1992-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/18/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
// ¥¥¥ Define the label so the file will be included only once. Note that 
// ¥¥¥ we use only one _ instead of two in order to conform to the ANSI specs. 
// ¥¥¥ Also don't forget the last #endif at the end of the file!

#ifndef _FOO_
#define _FOO_

// ¥¥¥ This is the only header file we always need to include, it contains the 
// ¥¥¥ global headers, structures and functions for all classes.
#ifndef _DTSCPLUSLIBRARY_
#include "DTSCPlusLibrary.h"
#endif

// ¥¥¥ Specify below all the needed Macintosh toolbox interfaces - don't just 
// ¥¥¥ include one file and assume that this file will include more files. 
// ¥¥¥ Each header file should be self-contained. 
//  Toolbox Include Files
#ifndef __PROCESSES__
#include <Processes.h>
#endif

#ifndef __APPLEEVENTS__
#include <AppleEvents.h>
#endif


// ¥¥¥ Specify any global structures and enums/typedefs here
// Global structures, typdefs and enums

const ProcessSerialNumber kMyProcess = {
                                        kNoProcess, kNoProcess};


// ¥¥¥ Here is the start of the class definition. Each file should only have
// ¥¥¥ one class definition, unless we are dealing with really small classes.
// ¥¥¥ Why are all member functions virtual? It's for SLM support, and developers could change this easily.
// _________________________________________________________________________________________________________ //
//  TFoo Class Interface

class TFoo
{
    // ¥¥¥ Provide information about the TFoo class here - this because using a browser we 
    // ¥¥¥ will have information needed concerning how to use the class.
public:
    // ¥¥¥ This section will contain any class specific typedefs and enums. The reason 
    // ¥¥¥ it's the first section has to do with C++, you need to specify enums and 
    // ¥¥¥ typedefs before using themÉ
    //  TYPEDEFS AND ENUMS
    enum EConstants
    {
        kFirstThing = 1, kLastThing = 999
    };

    // ¥¥¥ Here we will specify all the constructors and destructors needed 
    //  CONSTRUCTORS & DESTRUCTOR
    TFoo();                                     // default constructors
    virtual~ TFoo();                            // virtual destructor

    // ¥¥¥ This section will contain the main interfaces to the class itself.
    //  MAIN INTERFACE
    virtual Boolean KillApplication(ProcessSerialNumber*);// quit the application
    virtual short GetNumProcesses();            // get the N amount of currently running procs

    // ¥¥¥ This section will contain the get and set member functions.
    //  PUBLIC ACCESSORS AND MUTATORS   
    virtual ProcessSerialNumber GetMyProcessID() const;

    // ¥¥¥ This section will contain possible iterators, note the keywords Next, Last, First and Reset.
    // ITERATORS
    virtual void Next();                        // next PSN
    virtual Boolean Last();                     // last PSN?
    virtual void First();                       // first PSN
    virtual void Reset();                       // reset the list to the last entry

    //  ¥¥¥ This section will contain fields inside the class.
    //  FIELDS
protected:
    ProcessSerialNumber fProcessID;             // any specific PSN number
    ProcessSerialNumber fMyProcessID;           // our PSN number
    ProcessSerialNumber fFirstPSN;              // the first one we got
    Boolean fFirstTime;                         // signals order of iterators
    Boolean fLast;                              // used to signal last process in an iterator list
private:
    Boolean fState;                             // state of the object
    OSErr fError;                               // latest toolbox error
};


#endif

// _________________________________________________________________________________________________________ //


/*  Change History (most recent last):
  No        Init.   Date        Comment
  1         khs     6/10/92     New file
  2         khs     7/6/92      First decent working class
*/
```

[Next](Headers-Timer.h.md)[Previous](Headers-SpinCursor.h.md)

