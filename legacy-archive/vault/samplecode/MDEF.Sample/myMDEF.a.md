---
title: MDEF.Sample
apple_id: DTS10000191
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MDEF.Sample/Listings/myMDEF_a.html
archived_at: '2026-07-18T03:13:51.256203Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MDEF.Sample](MDEF.Sample.md)


[Next](Sample.r.md)[Previous](MDEF.Sample.md)

# myMDEF.a

```
        INCLUDE 'traps.a'

        STRING ASIS


MyMDEF  MAIN EXPORT             ; this will be the entry point
    IMPORT MYMENU               ; name of Pascal FUNCTION that is the WDEF
                                ; we IMPORT externally referenced routines
                                ; from Pascal (in this case, just this one)
    BRA.S   @0                  ; branch around the header to the actual code
    DC.W    0                   ; flags word
    DC.B    'MDEF'              ; type
    DC.W    128                 ; ID number
    DC.W    0                   ; version
@0  JMP MyMenu                  ; this calls the Pascal WDEF
    END
```

[Next](Sample.r.md)[Previous](MDEF.Sample.md)

