---
title: Get Tool Config
apple_id: DTS10000002
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Get_Tool_Config/Listings/GetToolConfig_c.html
archived_at: '2026-07-18T03:10:50.167352Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Get Tool Config](Get%20Tool%20Config.md)


[Next](Document%20Revision%20History.md)[Previous](Get%20Tool%20Config.md)

# GetToolConfig.c

```c
/*
    File:           GetToolConfig.c

    Description:    This q&d allows one to accumulate into a TEXT file the config strings 
                of Connection Tools that have been configured with CMChoose.

    Author:     GDG

    Copyright:  Copyright: © 1999 by Apple Computer, Inc.
                all rights reserved.

    Disclaimer: You may incorporate this sample code into your applications without
                restriction, though the sample code has been provided "AS IS" and the
                responsibility for its operation is 100% yours.  However, what you are
                not permitted to do is to redistribute the source as "DSC Sample Code"
                after having made changes. If you're going to re-distribute the source,
                we require that you make it clear in the source that the code was
                descended from Apple Sample Code, but that you've made changes.

    Change History (most recent first):
            6/22/99 Updated for Metrowerks Codewarrior Pro 2.1(KG)
            2/97        recompiled PPC and 68K projects in CodeWarrior 11(MW)
            8/30/91     fixed it up to be useful(GDG)
            8/10/91 created this bugger from some existing source lying about(GDG)


*/
#include <Traps.h>
#include <stdio.h>
#include <CommResources.h>
#include <Connections.h>
#include <Memory.h>
#include <TextUtils.h>
#include <CTBUtilities.h>

// function prototypes
void main(void);

void main() {
    short           procID;
    ConnHandle      connection;
    CMBufferSizes   bufSizes;
    OSErr           err;
    Str255          toolName;
    Point           where;
    short           result;
    Ptr             configStream;
    FILE*           fp;

    // putting something into TTY window initializes QD globals, etc.
    printf("¥¥Êrunning Get Tool Config program ¥¥\n\n");

    // initialize CTB and managers
    if (NGetTrapAddress(_CommToolboxDispatch, OSTrap) ==
        NGetTrapAddress(_Unimplemented, OSTrap)) {
        printf("¥¥ CTB Not available ¥¥\n");
        return;
    }
    if (noErr != InitCRM()) {
        printf("¥¥ CTB Available but InitCRM failed. ¥¥\n");
        return;
    }
    if (noErr != InitCTBUtilities()) {
        printf("¥¥ CTB Available: InitCTBUtilities Fail. ¥¥\n");
        return;
    }
    if (cmNoTools == InitCM()) {
        printf("¥¥ CTB Available: No connection tools found. ¥¥\n");
        return;
    }

    // get a Connection Tool name
    err = CRMGetIndToolName('cbnd',1,toolName);
    if (err != noErr) {
        printf("¥¥ CRMGetIndToolName failed... no Conn Tool available ?!?!? ¥¥\n");
        return;
    }
    // get a resource ID for it
    procID = CMGetProcID(toolName);
    if (-1 == procID) {
        printf("¥¥ CMGetProcID: No 'Apple (ISDN) Serial Tool'. ¥¥\n");
        return;
    }

    // init the CMBufferSizes variable so that Tool will init with defaults
    bufSizes[cmDataIn] = 0;
    bufSizes[cmDataOut] = 0;
    bufSizes[cmCntlIn] = 0;
    bufSizes[cmCntlOut] = 0;
    bufSizes[cmAttnIn] = 0;
    bufSizes[cmAttnOut] = 0;

    // now get a conn record set up 
    connection = CMNew(procID, cmData|cmNoMenus|cmQuiet, bufSizes, 0, 0);
    if (connection == nil) {
        printf("¥¥ CMNew: Can't create a CTB connection record. ¥¥\n");
        return;
    }

    // CMChoose Dialog has to hang off this point (global coordinates)
    SetPt(&where,20,40);
    // now do CMChoose et al:
    result = CMChoose(&connection,where,NULL);
    if ((result == chooseOKMajor) || (result == chooseOKMinor)) {
        configStream = CMGetConfig(connection);
        if (configStream == NULL) {
            printf("CMGetConfig failed\n\n");
        } else {
            CMGetToolName((**connection).procID,toolName);
            p2cstr(toolName);
            printf("¥ Configuration string for %s:\n'%s'\n\n",toolName, configStream);
            fp = fopen("Tool Configs","a");
            if (fp != NULL) {
                fprintf(fp,"¥ Configuration string for %s:\n'%s'\n\n",toolName, configStream);
                fclose(fp);
                printf("¥¥ Configuration string info appended to file 'Tool Configs'. ¥¥\n\n");
            } else {
                printf("¥¥ Output file could not be opened. ¥¥\n");
            }
            DisposePtr(configStream);
        }
    } else {
        printf("¥¥ CMChoose failed. ¥¥\n");
    }
    CMDispose(connection);
    printf("¥¥Êclosing Get Tool Config program ¥¥\n\n");
}
```

[Next](Document%20Revision%20History.md)[Previous](Get%20Tool%20Config.md)

