---
title: How to Detect a CD
apple_id: DTS10000012
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/How_to_Detect_a_CD/Listings/Not_used_in_this_example_Determine_Devices_using_SCSI_cscsi_h.html
archived_at: '2026-07-18T03:11:57.161199Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [How to Detect a CD](How%20to%20Detect%20a%20CD.md)


[Next](Not%20used%20in%20this%20example-Determine%20Devices%20using%20SCSI-main.cp.md)[Previous](Not%20used%20in%20this%20example-Determine%20Devices%20using%20SCSI-cscsi.cp.md)

# Not used in this example/Determine Devices using SCSI/cscsi.h

```c
#ifndef CSCSI_H
#define CSCSI_H

#include        <Types.h>
#include        <SCSI.H>

typedef enum
{
        dataIn=1, dataOut=2, noData=3
} XferDir;

#define USE_CDB         0x01
#define USE_BUF         0x02
#define USE_LEN         0x04
#define USE_DIR         0x08
#define USE_ID          0x10

#define CAN_DATA        (USE_CDB|USE_BUF|USE_LEN|USE_DIR|USE_ID)
#define CAN_NO_DATA     (USE_CDB|USE_DIR|USE_ID)

#define SCSI_NEED_INFO  (-1)
#define SCSI_OK                 (0)

class   CSCSIOp
{
    short   targetID;
    Byte    cdb[12];
    Byte    cdbLen;
    Byte    *dataPtr;
    long    dataLen;
    short   status;
    short   message;
    OSErr   err;
    XferDir dir;
    long    timeout;
    short   haveInfo;
    long    moved;
public:
            CSCSIOp( void );
            ~CSCSIOp( void );
    void    keep( short what );
    void    setID( short ID );
    void    setCDB( short len, Byte * cdbPtr );
    void    set6( Byte a, Byte b, Byte c, Byte d, Byte e, Byte f );
    void    set10( Byte a, Byte b, Byte c, Byte d, Byte e, Byte f,
                                    Byte g, Byte h, Byte i, Byte j );
    void    set12( Byte a, Byte b, Byte c, Byte d, Byte e, Byte f,
                                    Byte g, Byte h, Byte i, Byte j, Byte k, Byte l );
    void    setLen( long len );
    void    setBuf( void * buf );
    void    setDir( XferDir direction );
    short   execute( void );
    short   getStatus( void );
    short   getMessage( void );
    void    setTimeout( long newTime );
    OSErr   getErr( void );
    long    getMoved( void );
};

#endif
```

[Next](Not%20used%20in%20this%20example-Determine%20Devices%20using%20SCSI-main.cp.md)[Previous](Not%20used%20in%20this%20example-Determine%20Devices%20using%20SCSI-cscsi.cp.md)

