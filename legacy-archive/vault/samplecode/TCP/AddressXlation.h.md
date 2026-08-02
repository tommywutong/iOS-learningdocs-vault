---
title: TCP
apple_id: DTS10000263
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/TCP/Listings/AddressXlation_h.html
archived_at: '2026-07-18T03:25:58.835729Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCP](TCP.md)


[Next](ASR.c.md)[Previous](TCP.md)

# AddressXlation.h

```
/* 
    AddressXlation.h        
    MacTCP name to address translation routines.

    Copyright Apple Computer, Inc. 1988 
    All rights reserved

*/  

#define NUM_ALT_ADDRS   4

typedef struct hostInfo {
    int rtnCode;
    char cname[255];
    unsigned long addr[NUM_ALT_ADDRS];
};

typedef enum AddrClasses {
    A = 1,
    NS,
    CNAME = 5,
    lastClass = 65535
}; 

typedef struct cacheEntryRecord {
    char *cname;
    unsigned short type;
    enum AddrClasses class;
    unsigned long ttl;
    union {
        char *name;
        ip_addr addr;
    } rdata;
};

typedef pascal void (*EnumResultProcPtr)(struct cacheEntryRecord *cacheEntryRecordPtr, char *userDataPtr);

typedef pascal void (*ResultProcPtr)(struct hostInfo *hostInfoPtr, char *userDataPtr);

extern OSErr OpenResolver(char *fileName);

extern OSErr StrToAddr(char *hostName, struct hostInfo *hostInfoPtr, ResultProcPtr ResultProc, char *userDataPtr);

extern OSErr AddrToStr(unsigned long addr, char *addrStr);

extern OSErr EnumCache(EnumResultProcPtr enumResultProc, char *userDataPtr);

extern OSErr AddrToName(ip_addr addr, struct hostInfo *hostInfoPtr, ResultProcPtr ResultProc, char *userDataPtr);

extern OSErr CloseResolver();
```

[Next](ASR.c.md)[Previous](TCP.md)

