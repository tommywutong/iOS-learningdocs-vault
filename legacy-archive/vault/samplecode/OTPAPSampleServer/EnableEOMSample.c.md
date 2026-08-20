---
title: OTPAPSampleServer
apple_id: DTS10000252
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/OTPAPSampleServer/Listings/EnableEOMSample_c.html
archived_at: '2026-07-18T03:17:17.112375Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OTPAPSampleServer](OTPAPSampleServer.md)


[Next](EnableSelfSendSample.c.md)[Previous](ATalkSampleUtils.h.md)

# EnableEOMSample.c

```c
/*
    File: EnableIPReuseAddrSample.c
    By:     Rich Kubota
            Developer Technical Support

    Purpose: Demonstrate the use of the OTOptionManagement call to tell a PAP or
            ADSP endpoint to enable/disable the EOM option.

            Note that this sample does not support asynch endpoints.  To support
            an asynch endpoint, the same call to OTOptionManagement would happen
            however, the endpoint handler will be called with the
            T_OPTMGMTCOMPLETE event.  The handler would then inspect the cookie, 
            which will be the TOptMgmt "ret" value to check for the
            success or failure of the call.

*/

#include "OpenTransport.h"          // open transport files         
#include "OpenTptAppletalk.h"

extern OSStatus DoNegotiateEOMOption(EndpointRef ep, Boolean enableEOM);

/*
    Sample function to enable/disable the EOM option for 
    ADSP.  This function also demonstrates the
    use of the OTOptionManagement call.

    Unless explicitely defined by XTI, all Open Transport options
    use a kOTFourByteOptionSize buffer.

    Input
    EndpointRef ep - endpoint on which to set EOM option on
    Boolean enableEOM - true - option on, false - option off

   Return: kOTNoError indicates that the option was successfully negotiated
            OSStatus is an error if < 0, otherwise, the status field is
            returned and is > 0.

*/
OSStatus DoNegotiateEOMOption(EndpointRef ep, Boolean enableEOM)

{
    UInt8       buf[kOTFourByteOptionSize]; // define buffer for fourByte Option size
    TOption*    opt;                        // option ptr to make items easier to access
    TOptMgmt    req;
    TOptMgmt    ret;
    OSStatus    err;

    if (OTIsSynchronous(ep) == false)           // check whether ep sync or not
    {
        DebugStr("\pThis routine does not support asynch endpoints");
        return (OSStatus)-1;
    }

    opt = (TOption*)buf;                    // set option ptr to buffer
    req.opt.buf = buf;
    req.opt.len = sizeof(buf);
    req.flags   = T_NEGOTIATE;              // negotiate for EOM option

    ret.opt.buf = buf;
    ret.opt.maxlen = kOTFourByteOptionSize;

    opt->level  = ATK_PAP;                  // dealing with PAP
    opt->name   = OPT_ENABLEEOM;
    opt->len    = kOTFourByteOptionSize;
    opt->status = 0;
    *(UInt32*)opt->value = enableEOM;       // set the desired option level, true or false

    err = OTOptionManagement(ep, &req, &ret);

        // if no error then return the option status value
    if (err == kOTNoError)
    {
        if (opt->status != T_SUCCESS)
            err = opt->status;
        else
            err = kOTNoError;
    }

    return err;
}
```

[Next](EnableSelfSendSample.c.md)[Previous](ATalkSampleUtils.h.md)

