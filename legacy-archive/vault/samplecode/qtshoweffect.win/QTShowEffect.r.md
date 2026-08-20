---
title: qtshoweffect.win
apple_id: DTS10000839
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/qtshoweffect.win/Listings/QTShowEffect_r.html
archived_at: '2026-07-26T19:52:43.688071Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtshoweffect.win](qtshoweffect.win.md)


[Next](Document%20Revision%20History.md)[Previous](QTShowEffect.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTShowEffect.r

```
/* QTShowEffect.r */

data 'MENU' (133, preload) {
    $"0085 0000 0000 0000 0000 FFFF FFFF 0100"            /* .........ÿÿÿÿ.. */
    $"00"                                                 /* . */
};

data 'MENU' (134) {
    $"0086 0000 0000 0000 0000 FFFF FFFF 0100"            /* .........ÿÿÿÿ.. */
    $"00"                                                 /* . */
};

data 'DITL' (133, "Select Effect dialog box") {
    $"0001 0000 0000 002F 00E3 0043 011F 0402"            /* ......./.ã.C.... */
    $"4F4B 0000 0000 0009 000A 001D 0113 0702"            /* OK.....Æ........ */
    $"0085"                                               /* . */
};

data 'DITL' (132, "Custom dialog box") {
    $"0003 0000 0000 0004 0007 0018 011A 0702"            /* ................ */
    $"0086 0000 0000 0151 0007 017C 0140 885C"            /* ......Q...|.@\ */
    $"5468 6973 2073 686F 7773 2068 6F77 2074"            /* This shows how t */
    $"6865 2065 6666 6563 7473 2063 6F6E 7472"            /* he effects contr */
    $"6F6C 7320 6361 6E20 6265 2070 7574 2069"            /* ols can be put i */
    $"6E74 6F20 6120 6469 616C 6F67 2062 6F78"            /* nto a dialog box */
    $"2070 726F 7669 6465 6420 6279 2061 6E20"            /*  provided by an  */
    $"6170 706C 6963 6174 696F 6E2E 0000 0000"            /* application..... */
    $"0152 0154 0166 018E 0402 4F4B 0000 0000"            /* .R.T.f...OK.... */
    $"001B 0007 0147 0197 8000"                           /* .....G.. */
};

data 'DLOG' (133, "Select Effect dialog box") {
    $"004A 0022 009A 014E 0005 0000 0000 0000"            /* .J."..N........ */
    $"0000 0085 0D53 656C 6563 7420 4566 6665"            /* ...ÂSelect Effe */
    $"6374 300A"                                          /* ct0. */
};

data 'DLOG' (132, "Extra dialog box") {
    $"0034 001C 01C2 01BA 0005 0000 0000 0000"            /* .4...Â.º........ */
    $"0000 0084 1043 7573 746F 6D69 7A65 2045"            /* ....Customize E */
    $"6666 6563 7400 300A"                                /* ffect.0. */
};

data 'PICT' (128, "About box PICT") {
    $"5B0A 0000 0000 00E0 00AB 0011 02FF 0C00"            /* [......à.«...ÿ.. */
    $"FFFE 0000 005A 0000 005A 0000 0000 0000"            /* ÿþ...Z...Z...... */
    $"0118 00D6 0000 0000 00A1 01F2 0016 3842"            /* ...Ö.....¡.ò..8B */
    $"494D 0000 0000 0000 00E0 00AB 4772 8970"            /* IM.......à.«Grp */
    $"68AF 626A 0001 000A 0000 0000 0118 00D6"            /* h¯bj...........Ö */
    $"8201 0000 0DB8 0000 0001 0000 0000 0000"            /* ...Â¸.......... */
    $"0000 0000 0000 0000 0001 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 4000 0000 0000 0D85"            /* ........@.....Â */
    $"0000 0000 0118 00D6 0000 0056 726C 6520"            /* .......Ö...Vrle  */
    $"0000 0000 0000 0000 0001 0001 6170 706C"            /* ............appl */
    $"0000 0000 0000 0400 00D6 0118 005A 0000"            /* .........Ö...Z.. */
    $"005A 0000 0000 0D2F 0001 0941 6E69 6D61"            /* .Z....Â/..ÆAnima */
    $"7469 6F6E 0000 0000 0000 0000 0000 0000"            /* tion............ */
    $"0000 0000 0000 0000 0000 0028 0028 4000"            /* ...........(.(@. */
    $"0D2F 0008 0000 0000 0118 0000 01CB FFFF"            /* Â/...........Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 01CB FFFF"            /* .Ëÿÿÿÿ.ÿÿ..ÿ.Ëÿÿ */
    $"FFFF 01FF FF00 00FF 01CB FFFF FFFF 01FF"            /* ÿÿ.ÿÿ..ÿ.Ëÿÿÿÿ.ÿ */
    $"FF00 00FF 01CB FFFF FFFF 01FF FF00 00FF"            /* ÿ..ÿ.Ëÿÿÿÿ.ÿÿ..ÿ */
    $"01CB FFFF FFFF 01FF FF00 00FF 0000 009A"            /* .Ëÿÿÿÿ.ÿÿ..ÿ... */
    $"0000 00FF 8358 0000 0000 0118 00D6 0000"            /* ...ÿX.......Ö.. */
    $"0004 0000 0000 005A 0000 005A 0000 0010"            /* .......Z...Z.... */
    $"0020 0003 0008 0000 0000 0000 0000 0000"            /* . .............. */
    $"0000 0000 0000 0118 00D6 0000 0000 0118"            /* .........Ö...... */
    $"00D6 0040 000C 81FF 81FF 81FF 81FF 81FF"            /* .Ö.@..ÿÿÿÿÿ */
    $"FFFF 000C 81FF 81FF 81FF 81FF 81FF FFFF"            /* ÿÿ..ÿÿÿÿÿÿÿ */
    $"000C 81FF 81FF 81FF 81FF 81FF FFFF 000C"            /* ..ÿÿÿÿÿÿÿ.. */
    $"81FF 81FF 81FF 81FF 81FF FFFF 000C 81FF"            /* ÿÿÿÿÿÿÿ..ÿ */
    $"81FF 81FF 81FF 81FF FFFF 000C 81FF 81FF"            /* ÿÿÿÿÿÿ..ÿÿ */
    $"81FF 81FF 81FF FFFF 0033 97FF 03FC F8F6"            /* ÿÿÿÿÿ.3ÿ.üøö */
    $"F3FC F102 F3F6 FAF7 FF81 FFC1 FF03 FCF8"            /* óüñ.óöú÷ÿÿÁÿ.üø */
    $"F6F3 FCF1 02F3 F6FA CDFF 81FF EBFF 03FC"            /* öóüñ.óöúÍÿÿëÿ.ü */
    $"F8F6 F3FC F102 F3F6 FAA3 FFFF FF00 5D9E"            /* øöóüñ.óöú£ÿÿÿ.] */
    $"FF0B FDF8 DAA2 8370 5C4B 3C33 2924 FE25"            /* ÿ.ýøÚ¢p\K<3)$þ% */
    $"0824 2935 4355 6982 B2EC FCFF 81FF C8FF"            /* .$)5CUi²ìüÿÿÈÿ */
    $"0BFD F8DA A283 705C 4B3C 3329 24FE 2508"            /* .ýøÚ¢p\K<3)$þ%. */
    $"2429 3543 5569 82B2 ECD2 FF81 FFF2 FF0B"            /* $)5CUi²ìÒÿÿòÿ. */
    $"FDF8 DAA2 8370 5C4B 3C33 2924 FE25 0824"            /* ýøÚ¢p\K<3)$þ%.$ */
    $"2935 4355 6982 B2EC A8FF FFFF 006E A1FF"            /* )5CUi²ì¨ÿÿÿ.n¡ÿ */
    $"0EE0 976F 4F33 1D0C 060A 0D0F 1113 1415"            /* .àoO3....Â..... */
    $"FD16 0C15 1413 100D 0912 2B53 85D5 FEFF"            /* ý......ÂÆ.+SÕþÿ */
    $"81FF CBFF 0EE0 976F 4F33 1D0C 060A 0D0F"            /* ÿËÿ.àoO3....Â. */
    $"1113 1415 FD16 0B15 1413 100D 0912 2B53"            /* ....ý......ÂÆ.+S */
    $"85D5 FED6 FF81 FFF5 FF0E E097 6F4F 331D"            /* ÕþÖÿÿõÿ.àoO3. */
    $"0C06 0A0D 0F11 1314 15FD 160B 1514 1310"            /* ...Â.....ý...... */
    $"0D09 122B 5385 D5FE ACFF FFFF 0077 A5FF"            /* ÂÆ.+SÕþ¬ÿÿÿ.w¥ÿ */
    $"12F9 BA73 491F 0808 0E12 1519 1A1B 1B1C"            /* .ùºsI........... */
    $"1D1D 1E1E FA1F FF1E 071D 1B18 100C 1F4D"            /* ....ú.ÿ........M */
    $"9A00 F982 FFCF FF12 F9BA 7349 1F08 080E"            /* .ùÿÏÿ.ùºsI.... */
    $"1215 191A 1B1B 1C1D 1D1E 1EFA 1FFF 1E08"            /* ...........ú.ÿ.. */
    $"1D1B 1810 0C1F 4D9A F9D8 FF81 FFF9 FF12"            /* ......MùØÿÿùÿ. */
    $"F9BA 7349 1F08 080E 1215 191A 1B1B 1C1D"            /* ùºsI............ */
    $"1D1E 1EFA 1FFF 1E08 1D1B 1810 0C1F 4D9A"            /* ...ú.ÿ........M */
    $"F9AE FFFF FF00 89A8 FF17 EBAD 6E36 1006"            /* ù®ÿÿÿ.¨ÿ.ë­n6.. */
    $"0D13 1819 1A1B 1C1D 1E1F 1F21 2223 2324"            /* Â..........!"##$ */
    $"2525 FB27 0826 2524 2321 1F1B 110E 0240"            /* %%û'.&%$#!.....@ */
    $"8CE0 84FF D2FF 17EB AD6E 3610 060D 1318"            /* àÿÒÿ.ë­n6..Â.. */
    $"191A 1B1C 1D1E 1F1F 2122 2323 2425 25FB"            /* ........!"##$%%û */
    $"270B 2625 2423 211F 1B11 0E40 8CE0 DAFF"            /* '.&%$#!....@àÚÿ */
    $"81FF FCFF 17EB AD6E 3610 060D 1318 191A"            /* ÿüÿ.ë­n6..Â.... */
    $"1B1C 1D1E 1F1F 2122 2323 2425 25FB 270B"            /* ......!"##$%%û'. */
    $"2625 2423 211F 1B11 0E40 8CE0 B0FF FFFF"            /* &%$#!....@à°ÿÿÿ */
    $"009E AAFF 1CDF 8C2A 0A05 0E14 1819 1A1A"            /* .ªÿ.ß*........ */
    $"1C1D 1E1F 2122 2425 2728 292A 2B2D 2E2F"            /* ....!"$%'()*+-./ */
    $"3030 FE31 0830 2F2E 2C2A 2825 231F 0414"            /* 00þ1.0/.,*(%#... */
    $"0C25 9AF6 86FF D4FF 1CDF 8C2A 0A05 0E14"            /* .%öÿÔÿ.ß*.... */
    $"1819 1A1A 1C1D 1E1F 2122 2425 2728 292A"            /* ........!"$%'()* */
    $"2B2D 2E2F 3030 FE31 0D30 2F2E 2C2A 2825"            /* +-./00þ1Â0/.,*(% */
    $"231F 140C 259A F6DC FF81 FFFE FF1C DF8C"            /* #...%öÜÿÿþÿ.ß */
    $"2A0A 050E 1418 191A 1A1C 1D1E 1F21 2224"            /* *............!"$ */
    $"2527 2829 2A2B 2D2E 2F30 30FE 310D 302F"            /* %'()*+-./00þ1Â0/ */
    $"2E2C 2A28 2523 1F14 0C25 9AF6 B2FF FFFF"            /* .,*(%#...%ö²ÿÿÿ */
    $"00A6 ACFF 2AE3 871B 060C 1416 1819 1A1B"            /* .¦¬ÿ*ã......... */
    $"1C1D 1F20 2122 2426 282A 2B2D 2E30 3233"            /* ... !"$&(*+-.023 */
    $"3436 3738 383A 3A39 3838 3633 312E 2B27"            /* 46788::988631.+' */
    $"0522 1F17 0C51 DC87 FFD6 FF30 E387 1B06"            /* ."...QÜÿÖÿ0ã.. */
    $"0C14 1618 191A 1B1C 1D1F 2021 2224 2628"            /* .......... !"$&( */
    $"2A2B 2D2E 3032 3334 3637 3838 3A3A 3938"            /* *+-.02346788::98 */
    $"3836 3331 2E2B 2722 1F17 0C51 DCDD FF81"            /* 8631.+'"...QÜÝÿ */
    $"FF31 FFE3 871B 060C 1416 1819 1A1B 1C1D"            /* ÿ1ÿã........... */
    $"1F20 2122 2426 282A 2B2D 2E30 3233 3436"            /* . !"$&(*+-.02346 */
    $"3738 383A 3A39 3838 3633 312E 2B27 221F"            /* 788::988631.+'". */
    $"170C 51DC B3FF FFFF 00AF AEFF 2CFE B128"            /* ..QÜ³ÿÿÿ.¯®ÿ,þ±( */
    $"030E 1415 1617 191A 1B1C 1D1F 2122 2326"            /* ............!"#& */
    $"2829 2B2D 2F31 3335 3739 3A3C 3E3F 4141"            /* ()+-/13579:<>?AA */
    $"4242 4141 3E3D 3A36 332F 062A 2622 1D0C"            /* BBAA>=:63/.*&".. */
    $"37CB 88FF D8FF 33FE B128 030E 1415 1617"            /* 7ËÿØÿ3þ±(...... */
    $"191A 1B1C 1D1F 2122 2326 2829 2B2D 2F31"            /* ......!"#&()+-/1 */
    $"3335 3739 3A3C 3E3F 4141 4242 4141 3E3D"            /* 3579:<>?AABBAA>= */
    $"3A36 332F 2A26 221D 0C37 CBDE FF82 FF00"            /* :63/*&"..7ËÞÿÿ. */
    $"FE32 B128 030E 1415 1617 191A 1B1C 1D1F"            /* þ2±(............ */
    $"2122 2326 2829 2B2D 2F31 3335 3739 3A3C"            /* !"#&()+-/13579:< */
    $"3E3F 4141 4242 4141 3E3D 3A36 332F 2A26"            /* >?AABBAA>=:63/*& */
    $"221D 0C37 CBB4 FFFF FF00 B5AF FF2D E86C"            /* "..7Ë´ÿÿÿ.µ¯ÿ-èl */
    $"090A 1214 1515 1718 1A1B 1C1D 1F21 2323"            /* Æ............!## */
    $"2427 2A2B 2E30 3234 3739 3B3D 4042 4345"            /* $'*+.02479;=@BCE */
    $"4748 494A 4A49 4845 4340 3C37 0732 2D29"            /* GHIJJIHEC@<7.2-) */
    $"2420 1222 B289 FFD9 FF35 E86C 090A 1214"            /* $ ."²ÿÙÿ5èlÆ... */
    $"1515 1718 1A1B 1C1D 1F21 2323 2427 2A2B"            /* .........!##$'*+ */
    $"2E30 3234 3739 3B3D 4042 4345 4748 494A"            /* .02479;=@BCEGHIJ */
    $"4A49 4845 4340 3C37 322D 2924 2012 22B2"            /* JIHEC@<72-)$ ."² */
    $"DFFF 83FF 01E8 6C33 090A 1214 1515 1718"            /* ßÿÿ.èl3Æ....... */
    $"1A1B 1C1D 1F21 2323 2427 2A2B 2E30 3234"            /* .....!##$'*+.024 */
    $"3739 3B3D 4042 4345 4748 494A 4A49 4845"            /* 79;=@BCEGHIJJIHE */
    $"4340 3C37 322D 2924 2012 22B2 B5FF FFFF"            /* C@<72-)$ ."²µÿÿÿ */
    $"00BB B0FF 25C3 2D01 0F12 1314 1516 1719"            /* .»°ÿ%Ã-......... */
    $"1A1B 1C1E 2021 2324 2629 2B2D 3033 3437"            /* .... !#$&)+-0347 */
    $"393C 3F41 4346 494B 4D4F 50FE 5105 4F4E"            /* 9<?ACFIKMOPþQ.ON */
    $"4C48 4440 083A 3530 2A25 2014 16AC 8AFF"            /* LHD@.:50*% ..¬ÿ */
    $"DAFF 25C3 2D01 0F12 1314 1516 1719 1A1B"            /* Úÿ%Ã-........... */
    $"1C1E 2021 2324 2629 2B2D 3033 3437 393C"            /* .. !#$&)+-03479< */
    $"3F41 4346 494B 4D4F 50FE 510E 4F4E 4C48"            /* ?ACFIKMOPþQ.ONLH */
    $"4440 3A35 302A 2520 1416 ACE0 FF84 FF02"            /* D@:50*% ..¬àÿÿ. */
    $"C32D 0122 0F12 1314 1516 1719 1A1B 1C1E"            /* Ã-."............ */
    $"2021 2324 2629 2B2D 3033 3437 393C 3F41"            /*  !#$&)+-03479<?A */
    $"4346 494B 4D4F 50FE 510E 4F4E 4C48 4440"            /* CFIKMOPþQ.ONLHD@ */
    $"3A35 302A 2520 1416 ACB6 FFFF FF00 C4B2"            /* :50*% ..¬¶ÿÿÿ.Ä² */
    $"FF30 FE7F 0B06 0F11 1213 1416 1718 191A"            /* ÿ0þ............. */
    $"1B1C 1F21 2223 2527 2A2D 2E31 3436 383C"            /* ...!"#%'*-.1468< */
    $"3F42 4447 4A4D 5052 5455 5657 5756 5554"            /* ?BDGJMPRTUVWWVUT */
    $"504C 4809 433D 3831 2B25 2016 128C 8BFF"            /* PLHÆC=81+% ..ÿ */
    $"DCFF 3AFE 7F0B 060F 1112 1314 1617 1819"            /* Üÿ:þ............ */
    $"1A1B 1C1F 2122 2325 272A 2D2E 3134 3638"            /* ....!"#%'*-.1468 */
    $"3C3F 4244 474A 4D50 5254 5556 5757 5655"            /* <?BDGJMPRTUVWWVU */
    $"5450 4C48 433D 3831 2B25 2016 128C E1FF"            /* TPLHC=81+% ..áÿ */
    $"86FF 04FE 7F0B 060F 3511 1213 1416 1718"            /* ÿ.þ....5....... */
    $"191A 1B1C 1F21 2223 2527 2A2D 2E31 3436"            /* .....!"#%'*-.146 */
    $"383C 3F42 4447 4A4D 5052 5455 5657 5756"            /* 8<?BDGJMPRTUVWWV */
    $"5554 504C 4843 3D38 312B 2520 1612 8CB7"            /* UTPLHC=81+% ..· */
    $"FFFF FF00 C7B2 FF28 8800 0A10 1112 1314"            /* ÿÿÿ.Ç²ÿ(....... */
    $"1415 1717 191B 1C1C 1E21 2224 2628 2B2E"            /* .........!"$&(+. */
    $"3033 3537 3B3E 4144 4649 4C4F 5254 5759"            /* 0357;>ADFILORTWY */
    $"5AFE 5B04 5A59 5754 4F0A 4A44 3E39 312A"            /* Zþ[.ZYWTO.JD>91* */
    $"2420 1610 9D8C FFDC FF28 8800 0A10 1112"            /* $ ..ÿÜÿ(..... */
    $"1314 1415 1717 191B 1C1C 1E21 2224 2628"            /* ...........!"$&( */
    $"2B2E 3033 3537 3B3E 4144 4649 4C4F 5254"            /* +.0357;>ADFILORT */
    $"5759 5AFE 5B0F 5A59 5754 4F4A 443E 3931"            /* WYZþ[.ZYWTOJD>91 */
    $"2A24 2016 109D E2FF 86FF 0488 000A 1011"            /* *$ ..âÿÿ..... */
    $"2312 1314 1415 1717 191B 1C1C 1E21 2224"            /* #............!"$ */
    $"2628 2B2E 3033 3537 3B3E 4144 4649 4C4F"            /* &(+.0357;>ADFILO */
    $"5254 5759 5AFE 5B0F 5A59 5754 4F4A 443E"            /* RTWYZþ[.ZYWTOJD> */
    $"3931 2A24 2016 109D B8FF FFFF 00CD B3FF"            /* 91*$ ..¸ÿÿÿ.Í³ÿ */
    $"2A9B 090A 0F10 1112 1314 1415 1717 191B"            /* *Æ............. */
    $"1C1C 1E21 2224 2628 2B2E 3134 3638 3B3E"            /* ...!"$&(+.1468;> */
    $"4244 474A 4D50 5356 585B 5D5E FE5F 035E"            /* BDGJMPSVX[]^þ_.^ */
    $"5B59 540B 4F4B 453E 372F 2823 1E13 1FD6"            /* [YT.OKE>7/(#...Ö */
    $"8DFF DDFF 2A9B 090A 0F10 1112 1314 1415"            /* ÿÝÿ*Æ......... */
    $"1717 191B 1C1C 1E21 2224 2628 2B2E 3134"            /* .......!"$&(+.14 */
    $"3638 3B3E 4244 474A 4D50 5356 585B 5D5E"            /* 68;>BDGJMPSVX[]^ */
    $"FE5F 0F5E 5B59 544F 4B45 3E37 2F28 231E"            /* þ_.^[YTOKE>7/(#. */
    $"131F D6E3 FF87 FF05 9B09 0A0F 1011 2412"            /* ..Öãÿÿ.Æ....$. */
    $"1314 1415 1717 191B 1C1C 1E21 2224 2628"            /* ...........!"$&( */
    $"2B2E 3134 3638 3B3E 4244 474A 4D50 5356"            /* +.1468;>BDGJMPSV */
    $"585B 5D5E FE5F 0F5E 5B59 544F 4B45 3E37"            /* X[]^þ_.^[YTOKE>7 */
    $"2F28 231E 131F D6B9 FFFF FF00 D0B4 FF2B"            /* /(#...Ö¹ÿÿÿ.Ð´ÿ+ */
    $"B10C 070E 0F10 1112 1314 1415 1717 191B"            /* ±............... */
    $"1C1D 1F21 2224 2628 2B2E 3134 363A 3C3F"            /* ...!"$&(+.146:<? */
    $"4145 494C 4F52 5457 5A5D 5F61 FD62 025F"            /* AEILORTWZ]_aýb._ */
    $"5D59 0C54 4F49 433D 352D 2722 1E0F 4AF2"            /* ]Y.TOIC=5-'"..Jò */
    $"8EFF DEFF 2BB1 0C07 0E0F 1011 1213 1414"            /* ÿÞÿ+±.......... */
    $"1517 1719 1B1C 1D1F 2122 2426 282B 2E31"            /* ........!"$&(+.1 */
    $"3436 3A3C 3F41 4549 4C4F 5254 575A 5D5F"            /* 46:<?AEILORTWZ]_ */
    $"61FD 620F 5F5D 5954 4F49 433D 352D 2722"            /* aýb._]YTOIC=5-'" */
    $"1E0F 4AF2 E4FF 88FF 06B1 0C07 0E0F 1011"            /* ..Jòäÿÿ.±...... */
    $"2412 1314 1415 1717 191B 1C1D 1F21 2224"            /* $............!"$ */
    $"2628 2B2E 3134 363A 3C3F 4145 494C 4F52"            /* &(+.146:<?AEILOR */
    $"5457 5A5D 5F61 FD62 0F5F 5D59 544F 4943"            /* TWZ]_aýb._]YTOIC */
    $"3D35 2D27 221E 0F4A F2BA FFFF FF00 D6B5"            /* =5-'"..Jòºÿÿÿ.Öµ */
    $"FF33 DC22 020D 0E10 1111 1213 1414 1617"            /* ÿ3Ü".Â.......... */
    $"1819 1B1C 1E1F 2223 2426 292C 2F31 3437"            /* ......"#$&),/147 */
    $"3B3D 3F42 464A 4D50 5255 585C 5E60 6263"            /* ;=?BFJMPRUX\^`bc */
    $"6564 6362 605D 0C58 544E 4842 3A32 2B24"            /* edcb`].XTNHB:2+$ */
    $"201B 0881 8EFF DFFF 40DC 2202 0D0E 1011"            /*  ..ÿßÿ@Ü".Â... */
    $"1112 1314 1416 1718 191B 1C1E 1F22 2324"            /* ............."#$ */
    $"2629 2C2F 3134 373B 3D3F 4246 4A4D 5052"            /* &),/147;=?BFJMPR */
    $"5558 5C5E 6062 6365 6463 6260 5D58 544E"            /* UX\^`bcedcb`]XTN */
    $"4842 3A32 2B24 201B 0881 E4FF 89FF 07DC"            /* HB:2+$ ..äÿÿ.Ü */
    $"2202 0D0E 1011 1138 1213 1414 1617 1819"            /* ".Â....8........ */
    $"1B1C 1E1F 2223 2426 292C 2F31 3437 3B3D"            /* ...."#$&),/147;= */
    $"3F42 464A 4D50 5255 585C 5E60 6263 6564"            /* ?BFJMPRUX\^`bced */
    $"6362 605D 5854 4E48 423A 322B 2420 1B08"            /* cb`]XTNHB:2+$ .. */
    $"81BA FFFF FF00 DCB6 FF34 F444 000C 0E0F"            /* ºÿÿÿ.Ü¶ÿ4ôD.... */
    $"0F11 1112 1314 1415 1717 191B 1C1D 1F22"            /* ..............." */
    $"2325 2628 2C2F 3234 373B 3D3F 4346 4A4E"            /* #%&(,/247;=?CFJN */
    $"5152 5559 5D5F 6163 6466 6665 6462 600D"            /* QRUY]_acdffedb`Â */
    $"5C58 524B 463E 362F 2923 1E17 11B4 8FFF"            /* \XRKF>6/)#...´ÿ */
    $"E0FF 42F4 4400 0C0E 0F0F 1111 1213 1414"            /* àÿBôD........... */
    $"1517 1719 1B1C 1D1F 2223 2526 282C 2F32"            /* ........"#%&(,/2 */
    $"3437 3B3D 3F43 464A 4E51 5255 595D 5F61"            /* 47;=?CFJNQRUY]_a */
    $"6364 6666 6564 6260 5C58 524B 463E 362F"            /* cdffedb`\XRKF>6/ */
    $"2923 1E17 11B4 E5FF 8AFF 08F4 4400 0C0E"            /* )#...´åÿÿ.ôD... */
    $"0F0F 1111 3912 1314 1415 1717 191B 1C1D"            /* ....9........... */
    $"1F22 2325 2628 2C2F 3234 373B 3D3F 4346"            /* ."#%&(,/247;=?CF */
    $"4A4E 5152 5559 5D5F 6163 6466 6665 6462"            /* JNQRUY]_acdffedb */
    $"605C 5852 4B46 3E36 2F29 231E 1711 B4BB"            /* `\XRKF>6/)#...´» */
    $"FFFF FF00 DCB6 FF2E 7300 0B0C 0E0F 0F11"            /* ÿÿÿ.Ü¶ÿ.s....... */
    $"1112 1314 1415 1717 191B 1C1D 1F22 2325"            /* ............."#% */
    $"272A 2C2F 3234 373B 3D3F 4346 4A4E 5154"            /* '*,/247;=?CFJNQT */
    $"5659 5D5F 6264 65FD 6601 6562 0E5F 5B55"            /* VY]_bdeýf.eb._[U */
    $"504A 423A 332D 2621 1C10 2EE6 90FF E0FF"            /* PJB:3-&!...æÿàÿ */
    $"2E73 000B 0C0E 0F0F 1111 1213 1414 1517"            /* .s.............. */
    $"1719 1B1C 1D1F 2223 2527 2A2C 2F32 3437"            /* ......"#%'*,/247 */
    $"3B3D 3F43 464A 4E51 5456 595D 5F62 6465"            /* ;=?CFJNQTVY]_bde */
    $"FD66 1065 625F 5B55 504A 423A 332D 2621"            /* ýf.eb_[UPJB:3-&! */
    $"1C10 2EE6 E6FF 8AFF 0873 000B 0C0E 0F0F"            /* ...ææÿÿ.s...... */
    $"1111 2512 1314 1415 1717 191B 1C1D 1F22"            /* ..%............" */
    $"2325 272A 2C2F 3234 373B 3D3F 4346 4A4E"            /* #%'*,/247;=?CFJN */
    $"5154 5659 5D5F 6264 65FD 6610 6562 5F5B"            /* QTVY]_bdeýf.eb_[ */
    $"5550 4A42 3A33 2D26 211C 102E E6BC FFFF"            /* UPJB:3-&!...æ¼ÿÿ */
    $"FF00 E2B7 FF35 CC10 060C 0D0E 0F0F 1111"            /* ÿ.â·ÿ5Ì...Â..... */
    $"1213 1414 1617 1819 1B1C 1E1F 2224 2527"            /* ............"$%' */
    $"292C 2F32 3437 3B3E 4143 464A 4E51 5456"            /* ),/247;>ACFJNQTV */
    $"595D 5F62 6465 6768 6867 6664 0E60 5C58"            /* Y]_bdeghhgfd.`\X */
    $"534D 463E 3630 2923 1E1A 097D 90FF E1FF"            /* SMF>60)#..Æ}ÿáÿ */
    $"44CC 1006 0C0D 0E0F 0F11 1112 1314 1416"            /* DÌ...Â.......... */
    $"1718 191B 1C1E 1F22 2425 2729 2C2F 3234"            /* ......."$%'),/24 */
    $"373B 3E41 4346 4A4E 5154 5659 5D5F 6264"            /* 7;>ACFJNQTVY]_bd */
    $"6567 6868 6766 6460 5C58 534D 463E 3630"            /* eghhgfd`\XSMF>60 */
    $"2923 1E1A 097D E6FF 8BFF 09CC 1006 0C0D"            /* )#..Æ}æÿÿÆÌ...Â */
    $"0E0F 0F11 113A 1213 1414 1617 1819 1B1C"            /* .....:.......... */
    $"1E1F 2224 2527 292C 2F32 3437 3B3E 4143"            /* .."$%'),/247;>AC */
    $"464A 4E51 5456 595D 5F62 6465 6768 6867"            /* FJNQTVY]_bdeghhg */
    $"6664 605C 5853 4D46 3E36 3029 231E 1A09"            /* fd`\XSMF>60)#..Æ */
    $"7DBC FFFF FF00 E5B7 FF30 4D00 0B0C 0D0E"            /* }¼ÿÿÿ.å·ÿ0M...Â. */
    $"0F0F 1111 1213 1315 1517 1819 1B1C 1D1F"            /* ................ */
    $"2223 2527 292C 2F31 3437 3B3E 4143 454A"            /* "#%'),/147;>ACEJ */
    $"4D50 5356 585C 5E61 6465 67FE 6801 6765"            /* MPSVX\^adegþh.ge */
    $"0F62 5E5A 5550 4941 3933 2C26 201C 1519"            /* .b^ZUPIA93,& ... */
    $"D091 FFE1 FF30 4D00 0B0C 0D0E 0F0F 1111"            /* Ðÿáÿ0M...Â..... */
    $"1213 1315 1517 1819 1B1C 1D1F 2223 2527"            /* ............"#%' */
    $"292C 2F31 3437 3B3E 4143 454A 4D50 5356"            /* ),/147;>ACEJMPSV */
    $"585C 5E61 6465 67FE 6811 6765 625E 5A55"            /* X\^adegþh.geb^ZU */
    $"5049 4139 332C 2620 1C15 19D0 E7FF 8BFF"            /* PIA93,& ...Ðçÿÿ */
    $"094D 000B 0C0D 0E0F 0F11 1126 1213 1315"            /* ÆM...Â.....&.... */
    $"1517 1819 1B1C 1D1F 2223 2527 292C 2F31"            /* ........"#%'),/1 */
    $"3437 3B3E 4143 454A 4D50 5356 585C 5E61"            /* 47;>ACEJMPSVX\^a */
    $"6465 67FE 6811 6765 625E 5A55 5049 4139"            /* degþh.geb^ZUPIA9 */
    $"332C 2620 1C15 19D0 BDFF FFFF 00E8 B8FF"            /* 3,& ...Ð½ÿÿÿ.è¸ÿ */
    $"36D5 0E07 0B0C 0D0E 0F0F 1111 1213 1415"            /* 6Õ....Â......... */
    $"1617 181A 1B1C 1D20 2223 2527 292C 2F31"            /* ....... "#%'),/1 */
    $"3437 3B3E 4143 464A 4C4D 4C50 5659 5C5D"            /* 47;>ACFJLMLPVY\] */
    $"5C5E 6467 6969 6866 0F63 605C 5852 4B43"            /* \^dgiihf.c`\XRKC */
    $"3D35 2F28 221D 1A0B 6791 FFE2 FF46 D50E"            /* =5/("...gÿâÿFÕ. */
    $"070B 0C0D 0E0F 0F11 1112 1314 1516 1718"            /* ...Â............ */
    $"1A1B 1C1D 2022 2325 2729 2C2F 3134 373B"            /* .... "#%'),/147; */
    $"3E41 4346 4A4C 4D4C 5056 595C 5D5C 5E64"            /* >ACFJLMLPVY\]\^d */
    $"6769 6968 6663 605C 5852 4B43 3D35 2F28"            /* giihfc`\XRKC=5/( */
    $"221D 1A0B 67E7 FF8C FF0A D50E 070B 0C0D"            /* "...gçÿÿ.Õ....Â */
    $"0E0F 0F11 113B 1213 1415 1617 181A 1B1C"            /* .....;.......... */
    $"1D20 2223 2527 292C 2F31 3437 3B3E 4143"            /* . "#%'),/147;>AC */
    $"464A 4C4D 4C50 5659 5C5D 5C5E 6467 6969"            /* FJLMLPVY\]\^dgii */
    $"6866 6360 5C58 524B 433D 352F 2822 1D1A"            /* hfc`\XRKC=5/(".. */
    $"0B67 BDFF FFFF 00EB B8FF 0E66 000A 0C0D"            /* .g½ÿÿÿ.ë¸ÿ.f...Â */
    $"0D0E 0F0F 1111 1213 1315 FE16 2417 191C"            /* Â.........þ.$... */
    $"1E20 2223 2527 292C 2F31 3437 3B3E 4243"            /* . "#%'),/147;>BC */
    $"4244 4E60 859D ACB1 B4B3 AC9A 7566 6266"            /* BDN`¬±´³¬ufbf */
    $"6867 1064 615D 5954 4D46 3F38 312B 241F"            /* hg.da]YTMF?81+$. */
    $"1B16 0FB7 92FF E2FF 0E66 000A 0C0D 0D0E"            /* ...·ÿâÿ.f...ÂÂ. */
    $"0F0F 1111 1213 1315 FE16 3517 191C 1E20"            /* ........þ.5....  */
    $"2223 2527 292C 2F31 3437 3B3E 4243 4244"            /* "#%'),/147;>BCBD */
    $"4E60 859D ACB1 B4B3 AC9A 7566 6266 6867"            /* N`¬±´³¬ufbfhg */
    $"6461 5D59 544D 463F 3831 2B24 1F1B 160F"            /* da]YTMF?81+$.... */
    $"B7E8 FF8C FF0A 6600 0A0C 0D0D 0E0F 0F11"            /* ·èÿÿ.f...ÂÂ.... */
    $"1103 1213 1315 FE16 3517 191C 1E20 2223"            /* ......þ.5.... "# */
    $"2527 292C 2F31 3437 3B3E 4243 4244 4E60"            /* %'),/147;>BCBDN` */
    $"859D ACB1 B4B3 AC9A 7566 6266 6867 6461"            /* ¬±´³¬ufbfhgda */
    $"5D59 544D 463F 3831 2B24 1F1B 160F B7BE"            /* ]YTMF?81+$....·¾ */
    $"FFFF FF00 EEB9 FF37 CC0A 070B 0C0D 0D0E"            /* ÿÿÿ.î¹ÿ7Ì....ÂÂ. */
    $"0F0F 1111 1211 100A 0B11 1619 1816 1317"            /* ................ */
    $"1F23 2527 2A2D 2F31 3437 3B3D 3D3E 5288"            /* .#%'*-/147;==>R */
    $"AFCA DBE5 EAF0 F3F6 FAF7 E8CE A772 6264"            /* ¯ÊÛåêðóöú÷èÎ§rbd */
    $"1065 625F 5955 4F48 4039 342E 2822 1D1A"            /* .eb_YUOH@94.(".. */
    $"0870 92FF E3FF 48CC 0A07 0B0C 0D0D 0E0F"            /* .pÿãÿHÌ....ÂÂ.. */
    $"0F11 1112 1110 0A0B 1116 1918 1613 171F"            /* ................ */
    $"2325 272A 2D2F 3134 373B 3D3D 3E52 88AF"            /* #%'*-/147;==>R¯ */
    $"CADB E5EA F0F3 F6FA F7E8 CEA7 7262 6465"            /* ÊÛåêðóöú÷èÎ§rbde */
    $"625F 5955 4F48 4039 342E 2822 1D1A 0870"            /* b_YUOH@94.("...p */
    $"E8FF 8DFF 0BCC 0A07 0B0C 0D0D 0E0F 0F11"            /* èÿÿ.Ì....ÂÂ.... */
    $"113C 1211 100A 0B11 1619 1816 1317 1F23"            /* .<.............# */
    $"2527 2A2D 2F31 3437 3B3D 3D3E 5288 AFCA"            /* %'*-/147;==>R¯Ê */
    $"DBE5 EAF0 F3F6 FAF7 E8CE A772 6264 6562"            /* Ûåêðóöú÷èÎ§rbdeb */
    $"5F59 554F 4840 3934 2E28 221D 1A08 70BE"            /* _YUOH@94.("...p¾ */
    $"FFFF FF00 F1B9 FF31 7D00 0A0B 0C0D 0D0E"            /* ÿÿÿ.ñ¹ÿ1}....ÂÂ. */
    $"0F10 100E 0A11 2659 7F92 A2AB A59B 8857"            /* ......&Y.¢«¥W */
    $"291C 1C26 2A2D 3032 3437 3938 4D84 B2CD"            /* )..&*-024798M²Í */
    $"D5DB E2E8 EEF3 F7F9 FBFC FEFF 02E8 B56F"            /* ÕÛâèîó÷ùûüþÿ.èµo */
    $"115F 625F 5B56 504A 433C 3731 2A23 1E1B"            /* ._b_[VPJC<71*#.. */
    $"122B E793 FFE3 FF31 7D00 0A0B 0C0D 0D0E"            /* .+çÿãÿ1}....ÂÂ. */
    $"0F10 100E 0A11 2659 7F92 A2AB A59B 8857"            /* ......&Y.¢«¥W */
    $"291C 1C26 2A2D 3032 3437 3938 4D84 B2CD"            /* )..&*-024798M²Í */
    $"D5DB E2E8 EEF3 F7F9 FBFC FEFF 14E8 B56F"            /* ÕÛâèîó÷ùûüþÿ.èµo */
    $"5F62 5F5B 5650 4A43 3C37 312A 231E 1B12"            /* _b_[VPJC<71*#... */
    $"2BE7 E9FF 8DFF 0B7D 000A 0B0C 0D0D 0E0F"            /* +çéÿÿ.}....ÂÂ.. */
    $"1010 0E25 0A11 2659 7F92 A2AB A59B 8857"            /* ...%..&Y.¢«¥W */
    $"291C 1C26 2A2D 3032 3437 3938 4D84 B2CD"            /* )..&*-024798M²Í */
    $"D5DB E2E8 EEF3 F7F9 FBFC FEFF 14E8 B56F"            /* ÕÛâèîó÷ùûüþÿ.èµo */
    $"5F62 5F5B 5650 4A43 3C37 312A 231E 1B12"            /* _b_[VPJC<71*#... */
    $"2BE7 BFFF FFFF 00EB BAFF 31E2 1903 0A0B"            /* +ç¿ÿÿÿ.ëºÿ1â.... */
    $"0C0D 0D0E 0F0E 0916 5497 C0DB E8ED F1F5"            /* .ÂÂ...Æ.TÀÛèíñõ */
    $"F9FC FFF4 D3A5 5924 222C 3033 3535 396B"            /* ùüÿôÓ¥Y$",03559k */
    $"A5BF C6CF DAE2 EAF2 F8FC FDFD FEFB FF00"            /* ¥¿ÆÏÚâêòøüýýþûÿ. */
    $"E311 885A 5E5D 5852 4B45 3F3B 332C 2520"            /* ã.Z^]XRKE?;3,%  */
    $"1C19 0888 93FF E4FF 31E2 1903 0A0B 0C0D"            /* ...ÿäÿ1â.....Â */
    $"0D0E 0F0E 0916 5497 C0DB E8ED F1F5 F9FC"            /* Â...Æ.TÀÛèíñõùü */
    $"FFF4 D3A5 5924 222C 3033 3535 396B A5BF"            /* ÿôÓ¥Y$",03559k¥¿ */
    $"C6CF DAE2 EAF2 F8FC FDFD FEFB FF12 E388"            /* ÆÏÚâêòøüýýþûÿ.ã */
    $"5A5E 5D58 524B 453F 3B33 2C25 201C 1908"            /* Z^]XRKE?;3,% ... */
    $"88E9 FF8E FF0C E219 030A 0B0C 0D0D 0E0F"            /* éÿÿ.â.....ÂÂ.. */
    $"0E09 1624 5497 C0DB E8ED F1F5 F9FC FFF4"            /* .Æ.$TÀÛèíñõùüÿô */
    $"D3A5 5924 222C 3033 3535 396B A5BF C6CF"            /* Ó¥Y$",03559k¥¿ÆÏ */
    $"DAE2 EAF2 F8FC FDFD FEFB FF12 E388 5A5E"            /* Úâêòøüýýþûÿ.ãZ^ */
    $"5D58 524B 453F 3B33 2C25 201C 1908 88BF"            /* ]XRKE?;3,% ...¿ */
    $"FFFF FF00 DEBA FF05 A000 090A 0B0D FE0E"            /* ÿÿÿ.Þºÿ. .Æ..Âþ. */
    $"2407 1154 9EC8 D6DB E0E7 EEF3 F6F9 FBFC"            /* $..TÈÖÛàçîóöùûü */
    $"FEFF FFF5 C25E 232B 3331 3A7B ABB7 C0CA"            /* þÿÿõÂ^#+31:{«·ÀÊ */
    $"D4DF E9F3 FAFE F6FF 12F5 AA5C 5959 534D"            /* Ôßéóúþöÿ.õª\YYSM */
    $"4741 3C35 2D26 211D 1A0E 3CFA 94FF E4FF"            /* GA<5-&!...<úÿäÿ */
    $"05A0 0009 0A0B 0DFE 0E24 0711 549E C8D6"            /* . .Æ..Âþ.$..TÈÖ */
    $"DBE0 E7EE F3F6 F9FB FCFE FFFF F5C2 5E23"            /* ÛàçîóöùûüþÿÿõÂ^# */
    $"2B33 313A 7BAB B7C0 CAD4 DFE9 F3FA FEF6"            /* +31:{«·ÀÊÔßéóúþö */
    $"FF12 F5AA 5C59 5953 4D47 413C 352D 2621"            /* ÿ.õª\YYSMGA<5-&! */
    $"1D1A 0E3C FAEA FF8E FF05 A000 090A 0B0D"            /* ...<úêÿÿ. .Æ..Â */
    $"FE0E 0307 1154 9E20 C8D6 DBE0 E7EE F3F6"            /* þ....T ÈÖÛàçîóö */
    $"F9FB FCFE FFFF F5C2 5E23 2B33 313A 7BAB"            /* ùûüþÿÿõÂ^#+31:{« */
    $"B7C0 CAD4 DFE9 F3FA FEF6 FF12 F5AA 5C59"            /* ·ÀÊÔßéóúþöÿ.õª\Y */
    $"5953 4D47 413C 352D 2621 1D1A 0E3C FAC0"            /* YSMGA<5-&!...<úÀ */
    $"FFFF FF00 CDBB FF15 FB40 000A 0B0C 0D0E"            /* ÿÿÿ.Í»ÿ.û@....Â. */
    $"0C0C 3D88 BCC8 CDD7 E1EA F2F8 FCFD F9FF"            /* ..=¼ÈÍ×áêòøüýùÿ */
    $"0FF7 A23C 2941 79A5 B0BA C5CE D8E4 EDF7"            /* .÷¢<)Ay¥°ºÅÎØäí÷ */
    $"FEF5 FF12 FFFE BD65 5555 4F48 423C 352E"            /* þõÿ.ÿþ½eUUOHB<5. */
    $"2822 1E1A 160D A894 FFE5 FF15 FB40 000A"            /* ("...Â¨ÿåÿ.û@.. */
    $"0B0C 0D0E 0C0C 3D88 BCC8 CDD7 E1EA F2F8"            /* ..Â...=¼ÈÍ×áêòø */
    $"FCFD F9FF 0FF7 A23C 2941 79A5 B0BA C5CE"            /* üýùÿ.÷¢<)Ay¥°ºÅÎ */
    $"D8E4 EDF7 FEF4 FF11 FEBD 6555 554F 4842"            /* Øäí÷þôÿ.þ½eUUOHB */
    $"3C35 2E28 221E 1A16 0DA8 EAFF 8FFF 0DFB"            /* <5.("...Â¨êÿÿÂû */
    $"4000 0A0B 0C0D 0E0C 0C3D 88BC C807 CDD7"            /* @....Â...=¼È.Í× */
    $"E1EA F2F8 FCFD F9FF 0FF7 A23C 2941 79A5"            /* áêòøüýùÿ.÷¢<)Ay¥ */
    $"B0BA C5CE D8E4 EDF7 FEF4 FF11 FEBD 6555"            /* °ºÅÎØäí÷þôÿ.þ½eU */
    $"554F 4842 3C35 2E28 221E 1A16 0DA8 C0FF"            /* UOHB<5.("...Â¨Àÿ */
    $"FFFF 00B9 BBFF 12C3 0707 0A0B 0C0D 0C09"            /* ÿÿ.¹»ÿ.Ã.....Â.Æ */
    $"51A9 B9BF C8D3 DDE8 F2FA F4FF 0DC9 5076"            /* Q©¹¿ÈÓÝèòúôÿÂÉPv */
    $"9BA7 B2BD C6CF D9E4 EDF5 FCF5 FFFE FF0F"            /* §²½ÆÏÙäíõüõÿþÿ. */
    $"C35D 5250 4A44 3D36 2F29 2420 1C18 0A51"            /* Ã]RPJD=6/)$ ...Q */
    $"94FF E5FF 12C3 0707 0A0B 0C0D 0C09 51A9"            /* ÿåÿ.Ã.....Â.ÆQ© */
    $"B9BF C8D3 DDE8 F2FA F4FF 0DC9 5076 9BA7"            /* ¹¿ÈÓÝèòúôÿÂÉPv§ */
    $"B2BD C6CF D9E4 EDF5 FCF2 FF0F C35D 5250"            /* ²½ÆÏÙäíõüòÿ.Ã]RP */
    $"4A44 3D36 2F29 2420 1C18 0A51 EAFF 8FFF"            /* JD=6/)$ ...Qêÿÿ */
    $"0DC3 0707 0A0B 0C0D 0C09 51A9 B9BF C804"            /* ÂÃ.....Â.ÆQ©¹¿È. */
    $"D3DD E8F2 FAF4 FF0D C950 769B A7B2 BDC6"            /* ÓÝèòúôÿÂÉPv§²½Æ */
    $"CFD9 E4ED F5FC F2FF 0FC3 5D52 504A 443D"            /* ÏÙäíõüòÿ.Ã]RPJD= */
    $"362F 2924 201C 180A 51C0 FFFF FF00 C2BB"            /* 6/)$ ...QÀÿÿÿ.Â» */
    $"FF12 8300 080A 0B0C 0B09 509F AEB7 C2CC"            /* ÿ.......ÆP®·ÂÌ */
    $"D6E0 EBF5 FDF4 FF0E F593 889B A9B4 BDC6"            /* Öàëõýôÿ.õ©´½Æ */
    $"CFD8 E1E9 F1F7 FCF6 FFFF FF11 FDFC AD53"            /* ÏØáéñ÷üöÿÿÿ.ýü­S */
    $"504B 453F 3830 2A25 211D 1912 21DC 95FF"            /* PKE?80*%!...!Üÿ */
    $"E5FF 1283 0008 0A0B 0C0B 0950 9FAE B7C2"            /* åÿ.......ÆP®·Â */
    $"CCD6 E0EB F5FD F4FF 0EF5 9288 9BA9 B4BD"            /* ÌÖàëõýôÿ.õ©´½ */
    $"C6CF D8E1 E9F1 F7FC F4FF 11FD FCAD 5350"            /* ÆÏØáéñ÷üôÿ.ýü­SP */
    $"4B45 3F38 302A 2521 1D19 1221 DCEB FF8F"            /* KE?80*%!...!Üëÿ */
    $"FF0D 8300 080A 0B0C 0B09 509F AEB7 C2CC"            /* ÿÂ......ÆP®·ÂÌ */
    $"04D6 E0EB F5FD F4FF 0EF5 9388 9BA9 B4BD"            /* .Öàëõýôÿ.õ©´½ */
    $"C6CF D8E1 E9F1 F7FC F4FF 11FD FCAD 5350"            /* ÆÏØáéñ÷üôÿ.ýü­SP */
    $"4B45 3F38 302A 2521 1D19 1221 DCC1 FFFF"            /* KE?80*%!...!ÜÁÿÿ */
    $"FF00 C8BC FF03 F128 020A FE0B 0C08 4894"            /* ÿ.È¼ÿ.ñ(..þ...H */
    $"A3AF BAC4 CDD6 E1EA F3FB F4FF 0FC5 778F"            /* £¯ºÄÍÖáêóûôÿ.Åw */
    $"9CA9 B4BD C5CD D6DE E5EB F0F7 FEF7 FFFF"            /* ©´½ÅÍÖÞåëð÷þ÷ÿÿ */
    $"FF11 FEFA F283 4A4D 463F 3932 2C26 221E"            /* ÿ.þúòJMF?92,&". */
    $"1916 0684 95FF E6FF 03F1 2802 0AFE 0B0C"            /* ...ÿæÿ.ñ(..þ.. */
    $"0848 94A3 AFBA C4CD D6E1 EAF3 FBF4 FF0F"            /* .H£¯ºÄÍÖáêóûôÿ. */
    $"C577 8F9C A9B4 BDC5 CDD6 DEE5 EBF0 F7FE"            /* Åw©´½ÅÍÖÞåëð÷þ */
    $"F5FF 11FE FAF2 834A 4D46 3F39 322C 2622"            /* õÿ.þúòJMF?92,&" */
    $"1E19 1606 84EB FF90 FF03 F128 020A FE0B"            /* ....ëÿÿ.ñ(..þ. */
    $"0708 4894 A3AF BAC4 CD04 D6E1 EAF3 FBF4"            /* ..H£¯ºÄÍ.Öáêóûô */
    $"FF0F C577 8F9C A9B4 BDC5 CDD6 DEE5 EBF0"            /* ÿ.Åw©´½ÅÍÖÞåëð */
    $"F7FE F5FF 11FE FAF2 834A 4D46 3F39 322C"            /* ÷þõÿ.þúòJMF?92, */
    $"2622 1E19 1606 84C1 FFFF FF00 D3BC FF14"            /* &"....Áÿÿÿ.Ó¼ÿ. */
    $"BE05 0709 0B0C 0733 8597 A4B1 BBC4 CDD5"            /* ¾..Æ...3¤±»ÄÍÕ */
    $"DFE8 EFF6 FBF6 FF10 FE9D 7B90 9CA9 B2BB"            /* ßèïöûöÿ.þ{©²» */
    $"C4CB D3DB E0E6 EBF3 FDF7 FF14 FFFE FDFA"            /* ÄËÓÛàæëóý÷ÿ.ÿþýú */
    $"F8C4 504B 4841 3A34 2D28 231E 1A18 0B4B"            /* øÄPKHA:4-(#....K */
    $"FE96 FFE6 FF14 BE05 0709 0B0C 0733 8597"            /* þÿæÿ.¾..Æ...3 */
    $"A4B1 BBC4 CDD5 DFE8 EFF6 FBF6 FF10 FD9D"            /* ¤±»ÄÍÕßèïöûöÿ.ý */
    $"7B90 9CA9 B2BB C4CB D3DB E0E6 EBF3 FDF6"            /* {©²»ÄËÓÛàæëóýö */
    $"FF13 FEFD FAF8 C450 4B48 413A 342D 2823"            /* ÿ.þýúøÄPKHA:4-(# */
    $"1E1A 180B 4BFE ECFF 90FF 0EBE 0507 090B"            /* ....Kþìÿÿ.¾..Æ. */
    $"0C07 3385 97A4 B1BB C4CD 05D5 DFE8 EFF6"            /* ..3¤±»ÄÍ.Õßèïö */
    $"FBF6 FF10 FD9C 7B90 9CA9 B2BB C4CB D3DB"            /* ûöÿ.ý{©²»ÄËÓÛ */
    $"E0E6 EBF3 FDF6 FF13 FEFD FAF8 C450 4B48"            /* àæëóýöÿ.þýúøÄPKH */
    $"413A 342D 2823 1E1A 180B 4BFE C2FF FFFF"            /* A:4-(#....KþÂÿÿÿ */
    $"00D4 BCFF 1581 0009 0A0C 091B 6E8C 98A5"            /* .Ô¼ÿ..Æ..Æ.n¥ */
    $"B1BB C3CC D4DD E3EA EFF6 FCF7 FF10 EF84"            /* ±»ÃÌÔÝãêïöü÷ÿ.ï */
    $"7F8F 9BA8 B1BA C1C8 D0D7 DCE1 E8F0 FBF7"            /* .¨±ºÁÈÐ×Üáèðû÷ */
    $"FFFF FF12 FDFA F4EB 8748 4842 3C35 2E29"            /* ÿÿÿ.ýúôëHHB<5.) */
    $"241F 1C19 131A D996 FFE6 FF15 8100 090A"            /* $.....Ùÿæÿ..Æ. */
    $"0C09 1B6E 8C98 A5B1 BBC3 CCD4 DDE3 EAEF"            /* .Æ.n¥±»ÃÌÔÝãêï */
    $"F6FC F7FF 10EF 847F 8F9B A8B1 BAC1 C8D0"            /* öü÷ÿ.ï.¨±ºÁÈÐ */
    $"D7DC E1E8 F0FB F5FF 12FD FAF4 EB87 4848"            /* ×Üáèðûõÿ.ýúôëHH */
    $"423C 352E 2924 1F1C 1913 1AD9 ECFF 90FF"            /* B<5.)$.....Ùìÿÿ */
    $"0E81 0009 0A0C 091B 6E8C 98A5 B1BB C3CC"            /* ..Æ..Æ.n¥±»ÃÌ */
    $"06D4 DDE3 EAEF F6FC F7FF 10EF 847F 8F9B"            /* .ÔÝãêïöü÷ÿ.ï. */
    $"A8B1 BAC1 C8D0 D7DC E1E8 F0FB F5FF 12FD"            /* ¨±ºÁÈÐ×Üáèðûõÿ.ý */
    $"FAF4 EB87 4848 423C 352E 2924 1F1C 1913"            /* úôëHHB<5.)$.... */
    $"1AD9 C2FF FFFF 00D7 BDFF 16EF 2401 090A"            /* .ÙÂÿÿÿ.×½ÿ.ï$.Æ. */
    $"0B0B 527F 8C98 A5B0 B9C2 C9D1 D8DF E5EA"            /* ..R.¥°¹ÂÉÑØßåê */
    $"F0F9 F7FF 10DF 797F 8E99 A5AE B6BE C4CC"            /* ðù÷ÿ.ßy.¥®¶¾ÄÌ */
    $"D3D9 E2F0 F4FC F7FF FFFF 12FB F8F3 EEC6"            /* ÓÙâðôü÷ÿÿÿ.ûøóîÆ */
    $"5148 433D 362F 2A25 201D 1916 067B 96FF"            /* QHC=6/*% ....{ÿ */
    $"E7FF 16EF 2401 090A 0B0B 527F 8C98 A5B0"            /* çÿ.ï$.Æ...R.¥° */
    $"B9C2 C9D1 D8DF E5EA F0F9 F7FF 10DF 797F"            /* ¹ÂÉÑØßåêðù÷ÿ.ßy. */
    $"8E99 A5AE B6BE C4CC D3D9 E2F0 F4FC F5FF"            /* ¥®¶¾ÄÌÓÙâðôüõÿ */
    $"12FB F8F3 EEC6 5148 433D 362F 2A25 201D"            /* .ûøóîÆQHC=6/*% . */
    $"1916 067B ECFF 91FF 0FEF 2401 090A 0B0B"            /* ...{ìÿÿ.ï$.Æ... */
    $"527F 8C98 A5B0 B9C2 C906 D1D8 DFE5 EAF0"            /* R.¥°¹ÂÉ.ÑØßåêð */
    $"F9F7 FF10 DF79 7F8E 99A5 AEB6 BEC4 CCD3"            /* ù÷ÿ.ßy.¥®¶¾ÄÌÓ */
    $"D9E2 F0F4 FCF5 FF12 FBF8 F3EE C651 4843"            /* Ùâðôüõÿ.ûøóîÆQHC */
    $"3D36 2F2A 2520 1D19 1606 7BC2 FFFF FF00"            /* =6/*% ....{Âÿÿÿ. */
    $"E5BD FF16 BE06 0609 0A08 2A6C 7D8C 98A4"            /* å½ÿ.¾..Æ..*l}¤ */
    $"AFB7 BFC7 CED5 DAE1 E7EE F9F7 FF13 D572"            /* ¯·¿ÇÎÕÚáçîù÷ÿ.Õr */
    $"7E8B 96A2 AAB2 BAC1 C8D2 DEC6 8359 576B"            /* ~¢ª²ºÁÈÒÞÆYWk */
    $"ACF4 FAFF 15FF FDF9 F5F1 EADF 7C43 453E"            /* ¬ôúÿ.ÿýùõñêß|CE> */
    $"3730 2B26 211E 1A17 0C48 FD97 FFE7 FF16"            /* 70+&!....Hýÿçÿ. */
    $"BE06 0609 0A08 2A6C 7D8C 98A4 AFB7 BFC7"            /* ¾..Æ..*l}¤¯·¿Ç */
    $"CED5 DAE1 E7EE F9F7 FF13 D572 7E8B 96A2"            /* ÎÕÚáçîù÷ÿ.Õr~¢ */
    $"AAB2 BAC1 C8D2 DEC6 8359 576B ACF4 F9FF"            /* ª²ºÁÈÒÞÆYWk¬ôùÿ */
    $"14FD F9F5 F1EA DF7C 4345 3E37 302B 2621"            /* .ýùõñêß|CE>70+&! */
    $"1E1A 170C 48FD EDFF 91FF 0FBE 0606 090A"            /* ....Hýíÿÿ.¾..Æ. */
    $"082A 6C7D 8C98 A4AF B7BF C706 CED5 DAE1"            /* .*l}¤¯·¿Ç.ÎÕÚá */
    $"E7EE F9F7 FF13 D572 7E8B 96A2 AAB2 BAC1"            /* çîù÷ÿ.Õr~¢ª²ºÁ */
    $"C8D2 DEC6 8359 576B ACF4 F9FF 14FD F9F5"            /* ÈÒÞÆYWk¬ôùÿ.ýùõ */
    $"F1EA DF7C 4345 3E37 302B 2621 1E1A 170C"            /* ñêß|CE>70+&!.... */
    $"48FD C3FF FFFF 00E7 BDFF 168B 0009 0A0A"            /* HýÃÿÿÿ.ç½ÿ..Æ.. */
    $"0C4A 6E7D 8A96 A2AC B4BC C3CA D1D8 E4ED"            /* .Jn}¢¬´¼ÃÊÑØäí */
    $"EBF4 F7FF 0DCB 6D7B 8893 9EA6 AEB6 BCC9"            /* ëô÷ÿÂËm{¦®¶¼É */
    $"C463 14FD 0002 1548 ABFB FF15 FEFA F5F2"            /* Äc.ý...H«ûÿ.þúõò */
    $"EEE7 E2A4 4745 3F38 312C 2722 1E1B 1912"            /* îçâ¤GE?81,'".... */
    $"1FE0 97FF E7FF 168B 0009 0A0A 0C4A 6E7D"            /* .àÿçÿ..Æ...Jn} */
    $"8A96 A2AC B4BC C3CA D1D8 E4ED EBF4 F7FF"            /* ¢¬´¼ÃÊÑØäíëô÷ÿ */
    $"0DCB 6D7B 8893 9EA6 AEB6 BCC9 C463 14FD"            /* ÂËm{¦®¶¼ÉÄc.ý */
    $"0002 1548 ABFB FF15 FEFA F5F2 EEE7 E2A4"            /* ...H«ûÿ.þúõòîçâ¤ */
    $"4745 3F38 312C 2722 1E1B 1912 1FE0 EDFF"            /* GE?81,'".....àíÿ */
    $"91FF 0F8B 0009 0A0A 0C4A 6E7D 8A96 A2AC"            /* ÿ..Æ...Jn}¢¬ */
    $"B4BC C306 CAD1 D8E4 EDEB F4F7 FF0D CB6D"            /* ´¼Ã.ÊÑØäíëô÷ÿÂËm */
    $"7B88 939E A6AE B6BC C9C4 6314 FD00 0215"            /* {¦®¶¼ÉÄc.ý... */
    $"48AB FBFF 15FE FAF5 F2EE E7E2 A447 453F"            /* H«ûÿ.þúõòîçâ¤GE? */
    $"3831 2C27 221E 1B19 121F E0C3 FFFF FF00"            /* 81,'".....àÃÿÿÿ. */
    $"F7BD FF19 5A00 0A0B 0918 596C 7B88 939F"            /* ÷½ÿ.Z...Æ.Yl{ */
    $"A9B1 B9BF C6D4 DBB0 6646 4359 8DE6 FAFF"            /* ©±¹¿ÆÔÛ°fFCYæúÿ */
    $"0BC7 6978 848F 9AA2 AAB1 BDB4 35FD 0005"            /* .Çix¢ª±½´5ý.. */
    $"091B 3E65 4E9A FDFF 00FE 15FA F4F1 EEEB"            /* Æ.>eNýÿ.þ.úôñîë */
    $"E5DD B94F 4440 3932 2D28 231F 1B18 1507"            /* åÝ¹OD@92-(#..... */
    $"9597 FFE7 FF19 5A00 0A0B 0918 596C 7B88"            /* ÿçÿ.Z...Æ.Yl{ */
    $"939F A9B1 B9BF C6D4 DBB0 6646 4359 8DE6"            /* ©±¹¿ÆÔÛ°fFCYæ */
    $"FAFF 0BC6 6978 848F 9AA2 AAB1 BDB4 35FD"            /* úÿ.Æix¢ª±½´5ý */
    $"0005 091B 3E65 4E9A FDFF 16FE FAF4 F1EE"            /* ..Æ.>eNýÿ.þúôñî */
    $"EBE5 DDB9 4F44 4039 322D 2823 1F1B 1815"            /* ëåÝ¹OD@92-(#.... */
    $"0795 EDFF 91FF 0F5A 000A 0B09 1859 6C7B"            /* .íÿÿ.Z...Æ.Yl{ */
    $"8893 9FA9 B1B9 BF09 C6D4 DBB0 6646 4359"            /* ©±¹¿ÆÆÔÛ°fFCY */
    $"8DE6 FAFF 0BC6 6978 848F 9AA2 AAB1 BDB4"            /* æúÿ.Æix¢ª±½´ */
    $"35FD 0005 091B 3E65 4E9A FDFF 16FE FAF4"            /* 5ý..Æ.>eNýÿ.þúô */
    $"F1EE EBE5 DDB9 4F44 4039 322D 2823 1F1B"            /* ñîëåÝ¹OD@92-(#.. */
    $"1815 0795 C3FF FFFF 0100 BEFF 14EE 2404"            /* ...Ãÿÿÿ..¾ÿ.î$. */
    $"0A0B 072A 6069 7885 8F9A A5AD B4BB C9A8"            /* ...*`ix¥­´»É¨ */
    $"4B08 FE00 0404 1545 97EE FCFF 0ABE 6373"            /* K.þ....Eîüÿ.¾cs */
    $"808A 949D A5AD BA49 FC00 0A0C 2264 BF8C"            /* ¥­ºIü..."d¿ */
    $"319B FFFD FBF7 15F2 EFEC E9E5 E0D8 C661"            /* 1ÿýû÷.òïìéåàØÆa */
    $"4441 3B34 2E28 2420 1B18 1708 5E97 FFE8"            /* DA;4.($ ....^ÿè */
    $"FF14 EE24 040A 0B07 2A60 6978 858F 9AA5"            /* ÿ.î$....*`ix¥ */
    $"ADB4 BBC9 A84B 08FE 0004 0415 4597 EEFC"            /* ­´»É¨K.þ....Eîü */
    $"FF0A BE63 7380 8A94 9DA5 ADBA 49FC 0020"            /* ÿ.¾cs¥­ºIü.  */
    $"0C22 64BF 8C31 9BFF FDFB F7F2 EFEC E9E5"            /* ."d¿1ÿýû÷òïìéå */
    $"E0D8 C661 4441 3B34 2E28 2420 1B18 1708"            /* àØÆaDA;4.($ .... */
    $"5EED FF92 FF10 EE24 040A 0B07 2A60 6978"            /* ^íÿÿ.î$....*`ix */
    $"858F 9AA5 ADB4 BB03 C9A8 4B08 FE00 0404"            /* ¥­´».É¨K.þ... */
    $"1545 97EE FCFF 0ABE 6373 808A 949D A5AD"            /* .Eîüÿ.¾cs¥­ */
    $"BA49 FC00 200C 2264 BF8C 319B FFFD FBF7"            /* ºIü. ."d¿1ÿýû÷ */
    $"F2EF ECE9 E5E0 D8C6 6144 413B 342E 2824"            /* òïìéåàØÆaDA;4.($ */
    $"201B 1817 085E C3FF FFFF 0103 BEFF 12A1"            /*  ....^Ãÿÿÿ..¾ÿ.¡ */
    $"0009 0A0A 0B43 6266 7480 8B96 A0A8 AFBD"            /* .Æ...Cbft ¨¯½ */
    $"A918 FD00 060A 1F51 885A 65F4 FDFF 0ABA"            /* ©.ý....QZeôýÿ.º */
    $"616E 7A85 8F97 9FAD 7D02 FC00 0A0B 1E4C"            /* anz­}.ü....L */
    $"7E62 2220 D4F6 EFEC 16EA E8E7 E4E1 DBD3"            /* ~b" Ôöïì.êèçäáÛÓ */
    $"CA79 4242 3C35 2F2A 2420 1D19 170F 32F6"            /* ÊyBB<5/*$ ....2ö */
    $"98FF E8FF 12A1 0009 0A0A 0B43 6266 7480"            /* ÿèÿ.¡.Æ...Cbft */
    $"8B96 A0A8 AFBD A918 FD00 060A 1F51 885A"            /*  ¨¯½©.ý....QZ */
    $"65F4 FDFF 0ABA 616E 7A85 8F97 9FAD 7D02"            /* eôýÿ.ºanz­}. */
    $"FC00 210B 1E4C 7E62 2220 D4F6 EFEC EAE8"            /* ü.!..L~b" Ôöïìêè */
    $"E7E4 E1DB D3CA 7942 423C 352F 2A24 201D"            /* çäáÛÓÊyBB<5/*$ . */
    $"1917 0F32 F6EE FF92 FF10 A100 090A 0A0B"            /* ...2öîÿÿ.¡.Æ... */
    $"4362 6674 808B 96A0 A8AF BD01 A918 FD00"            /* Cbft ¨¯½.©.ý. */
    $"060A 1F51 885A 65F4 FDFF 0ABA 626E 7A85"            /* ...QZeôýÿ.ºbnz */
    $"8F97 9FAD 7D02 FC00 210B 1E4C 7E62 2220"            /* ­}.ü.!..L~b"  */
    $"D4F6 EFEC EAE8 E7E4 E1DB D3CA 7942 423C"            /* ÔöïìêèçäáÛÓÊyBB< */
    $"352F 2A24 201D 1917 0F32 F6C4 FFFF FF01"            /* 5/*$ ....2öÄÿÿÿ. */
    $"00BE FF11 5F00 0A0A 0912 5461 6570 7C86"            /* .¾ÿ._...Æ.Taep| */
    $"919B A3AC B33F FC00 140C 246D C588 288F"            /* £¬³?ü...$mÅ( */
    $"FFFC F9FC B462 6B75 7F8A 929B A538 FB00"            /* ÿüùü´bku.¥8û. */
    $"0A07 1323 2D28 1700 6FF3 E6E5 16E4 E3E2"            /* ...#-(..oóæå.äãâ */
    $"E0DD D7CF C984 4343 3D36 302A 2621 1D1B"            /* àÝ×ÏÉCC=60*&!.. */
    $"1712 1AD9 98FF E8FF 115F 000A 0A09 1254"            /* ...Ùÿèÿ._...Æ.T */
    $"6165 707C 8691 9BA3 ACB3 3FFC 0014 0C24"            /* aep|£¬³?ü...$ */
    $"6DC5 8828 8FFF FCF9 FCB4 626A 757F 8A92"            /* mÅ(ÿüùü´bju. */
    $"9BA5 38FB 0021 0713 232D 2817 006F F3E6"            /* ¥8û.!..#-(..oóæ */
    $"E5E4 E3E2 E0DD D7CF C984 4343 3D36 302A"            /* åäãâàÝ×ÏÉCC=60* */
    $"2621 1D1B 1712 1AD9 EEFF 92FF 105F 000A"            /* &!.....Ùîÿÿ._.. */
    $"0A09 1254 6165 707C 8691 9BA3 ACB3 003F"            /* .Æ.Taep|£¬³.? */
    $"FC00 140C 246D C588 288F FFFC F9FC B562"            /* ü...$mÅ(ÿüùüµb */
    $"6A75 7F8A 929B A538 FB00 2107 1323 2D28"            /* ju.¥8û.!..#-( */
    $"1700 6FF3 E6E5 E4E3 E2E0 DDD7 CFC9 8443"            /* ..oóæåäãâàÝ×ÏÉC */
    $"433D 3630 2A26 211D 1B17 121A D9C4 FFFF"            /* C=60*&!.....ÙÄÿÿ */
    $"FF00 FFBF FF11 F72E 0109 0B09 1957 6265"            /* ÿ.ÿ¿ÿ.÷..Æ.Æ.Wbe */
    $"6B77 828C 969D AD7C FB00 140A 1E48 6E52"            /* kw­|û....HnR */
    $"2118 CEF5 EEF2 B363 696F 7984 8C96 961C"            /* !.Îõîò³cioy. */
    $"FB00 0A02 090F 1210 0900 47E3 E1E0 16DF"            /* û...Æ...Æ.Gãáà.ß */
    $"DEDD DAD7 D2CA C385 4543 3D37 312B 2721"            /* ÞÝÚ×ÒÊÃEC=71+'! */
    $"1D1C 1813 0FB2 98FF E9FF 11F7 2E01 090B"            /* .....²ÿéÿ.÷..Æ. */
    $"0919 5762 656B 7782 8C96 9DAD 7CFB 0014"            /* Æ.Wbekw­|û.. */
    $"0A1E 486E 5221 18CE F5EE F2B3 6369 6F79"            /* ..HnR!.Îõîò³cioy */
    $"848C 9696 1CFB 0021 0209 0F12 1009 0047"            /* .û.!.Æ...Æ.G */
    $"E3E1 E0DF DEDD DAD7 D2CA C385 4543 3D37"            /* ãáàßÞÝÚ×ÒÊÃEC=7 */
    $"312B 2721 1D1C 1813 0FB2 EEFF 93FF 11F7"            /* 1+'!.....²îÿÿ.÷ */
    $"2E01 090B 0919 5762 656B 7782 8C96 9DAD"            /* ..Æ.Æ.Wbekw­ */
    $"7CFB 0014 0A1E 486E 5221 18CE F5EE F2B3"            /* |û....HnR!.Îõîò³ */
    $"6369 6F79 848C 9696 1CFB 0021 0209 0F12"            /* cioy.û.!.Æ.. */
    $"1009 0047 E3E1 E0DF DEDD DAD7 D2CA C385"            /* .Æ.GãáàßÞÝÚ×ÒÊÃ */
    $"4543 3D37 312B 2721 1D1C 1813 0FB2 C4FF"            /* EC=71+'!.....²Äÿ */
    $"FFFF 00F9 BFFF 11C2 0806 0A0B 081F 5A62"            /* ÿÿ.ù¿ÿ.Â......Zb */
    $"6569 707C 8790 99A5 3FFB 0014 0612 2027"            /* eip|¥?û.... ' */
    $"2213 008A F1E5 EAB5 6468 6B72 7D86 908D"            /* "..ñåêµdhkr} */
    $"0DF9 0008 0304 0300 0033 D6DC DA16 DAD8"            /* Âù.......3ÖÜÚ.ÚØ */
    $"D7D6 D2CD C5BD 8246 443E 3832 2D27 221E"            /* ×ÖÒÍÅ½FD>82-'". */
    $"1B19 1605 8998 FFE9 FF11 C208 060A 0B08"            /* ....ÿéÿ.Â..... */
    $"1F5A 6265 6970 7C87 9099 A53F FB00 1406"            /* .Zbeip|¥?û... */
    $"1220 2722 1300 8AF1 E5EA B664 686B 727D"            /* . '"..ñåê¶dhkr} */
    $"8690 8D0D F900 1F03 0403 0000 33D6 DCDA"            /* Âù.......3ÖÜÚ */
    $"DAD8 D7D6 D2CD C5BD 8246 443E 3832 2D27"            /* ÚØ×ÖÒÍÅ½FD>82-' */
    $"221E 1B19 1605 89EE FF93 FF11 C208 060A"            /* ".....îÿÿ.Â... */
    $"0B08 1F5A 6265 6970 7C87 9099 A53F FB00"            /* ...Zbeip|¥?û. */
    $"1406 1220 2722 1300 8AF1 E5EA B664 686B"            /* ... '"..ñåê¶dhk */
    $"727D 8690 8D0D F900 1F03 0403 0000 33D6"            /* r}Âù.......3Ö */
    $"DCDA DAD8 D7D6 D2CD C5BD 8246 443E 3832"            /* ÜÚÚØ×ÖÒÍÅ½FD>82 */
    $"2D27 221E 1B19 1605 89C4 FFFF FF00 EDBF"            /* -'".....Äÿÿÿ.í¿ */
    $"FF11 7100 080A 0B08 205A 6166 686C 7580"            /* ÿ.q..... Zafhlu */
    $"8994 9011 FB00 1401 070D 0F0D 0700 5AE6"            /* .û....Â.Â..Zæ */
    $"DFE4 B464 686B 6E76 7F8A 870B F400 0333"            /* ßä´dhknv..ô..3 */
    $"D1D6 D3FF D315 D1D0 CCC7 BEB7 7C47 453F"            /* ÑÖÓÿÓ.ÑÐÌÇ¾·|GE? */
    $"3833 2D27 231F 1B19 170B 45FC 99FF E9FF"            /* 83-'#.....Eüÿéÿ */
    $"1171 0008 0A0B 0820 5961 6668 6C75 8089"            /* .q..... Yafhlu */
    $"9490 11FB 0014 0107 0D0F 0D07 005A E6DF"            /* .û....Â.Â..Zæß */
    $"E3B3 6468 6B6E 767F 8A87 0BF4 0002 33D1"            /* ã³dhknv..ô..3Ñ */
    $"D6FE D315 D1D0 CCC7 BEB7 7C47 453F 3833"            /* ÖþÓ.ÑÐÌÇ¾·|GE?83 */
    $"2D27 231F 1B19 170B 45FC EFFF 93FF 1171"            /* -'#.....Eüïÿÿ.q */
    $"0008 0A0B 0820 5A61 6668 6C75 8089 9490"            /* ..... Zafhlu */
    $"11FB 0014 0107 0D0F 0D07 005A E6DF E4B4"            /* .û....Â.Â..Zæßä´ */
    $"6468 6B6E 767F 8A87 0BF4 0002 33D1 D6FE"            /* dhknv..ô..3ÑÖþ */
    $"D315 D1D0 CCC7 BEB7 7C47 453F 3833 2D27"            /* Ó.ÑÐÌÇ¾·|GE?83-' */
    $"231F 1B19 170B 45FC C5FF FFFF 00E7 C0FF"            /* #.....EüÅÿÿÿ.çÀÿ */
    $"12FB 3A00 0809 0907 2058 6165 686A 6E78"            /* .û:..ÆÆ. Xaehjnx */
    $"838F 8107 F900 FE01 FF00 0D3E D9DA DDB6"            /* .ù.þ.ÿ.Â>ÙÚÝ¶ */
    $"6667 6B6D 7178 8285 1CF4 0003 4AD2 CECD"            /* fgkmqx.ô..JÒÎÍ */
    $"17CD CCCB C8C5 BFB6 AB6D 4846 4039 342E"            /* .ÍÌËÈÅ¿¶«mHF@94. */
    $"2924 201D 1916 1218 D999 FFEA FF12 FB3A"            /* )$ .....Ùÿêÿ.û: */
    $"0008 0909 0720 5961 6568 6A6E 7883 8F81"            /* ..ÆÆ. Yaehjnx */
    $"07F9 00FE 01FF 000D 3ED9 DADD B666 676B"            /* .ù.þ.ÿ.Â>ÙÚÝ¶fgk */
    $"6D71 7882 851C F400 1B4A D2CE CDCD CCCB"            /* mqx.ô..JÒÎÍÍÌË */
    $"C8C5 BFB6 AB6D 4846 4039 342E 2924 201D"            /* ÈÅ¿¶«mHF@94.)$ . */
    $"1916 1218 D9EF FF94 FF12 FB3A 0008 0909"            /* ....Ùïÿÿ.û:..ÆÆ */
    $"0720 5961 6568 6A6E 7883 8F81 07F9 00FE"            /* . Yaehjnx.ù.þ */
    $"01FF 000D 3ED9 DADD B766 676B 6D71 7882"            /* .ÿ.Â>ÙÚÝ·fgkmqx */
    $"851C F400 1B4A D2CE CDCD CCCB C8C5 BFB6"            /* .ô..JÒÎÍÍÌËÈÅ¿¶ */
    $"AB6D 4846 4039 342E 2924 201D 1916 1218"            /* «mHF@94.)$ ..... */
    $"D9C5 FFFF FF00 DBC0 FF02 D40F 06FE 090C"            /* ÙÅÿÿÿ.ÛÀÿ.Ô..þÆ. */
    $"071E 5760 6468 6A6C 727C 8782 0AF4 000D"            /* ..W`dhjlr|.ô.Â */
    $"48D7 D3D6 B869 676B 6E70 727A 8737 F400"            /* H×ÓÖ¸igknprz7ô. */
    $"0388 CDC6 C617 C6C5 C4C1 BEB8 AF9D 594B"            /* .ÍÆÆ.ÆÅÄÁ¾¸¯YK */
    $"4841 3A35 2F2A 2420 1E1A 1814 10B6 99FF"            /* HA:5/*$ .....¶ÿ */
    $"EAFF 02D4 0F06 FE09 0C07 1F58 6064 686A"            /* êÿ.Ô..þÆ...X`dhj */
    $"6C72 7C87 820A F400 0D48 D7D3 D6B8 6A67"            /* lr|.ô.ÂH×ÓÖ¸jg */
    $"6B6E 7072 7A87 37F4 0001 88CD FEC6 16C5"            /* knprz7ô..ÍþÆ.Å */
    $"C4C1 BEB8 AF9D 594B 4841 3A35 2F2A 2420"            /* ÄÁ¾¸¯YKHA:5/*$  */
    $"1E1A 1814 10B6 EFFF 94FF 02D4 0F06 FE09"            /* .....¶ïÿÿ.Ô..þÆ */
    $"0C07 1F57 6064 686A 6C72 7C87 820A F400"            /* ...W`dhjlr|.ô. */
    $"0D48 D7D3 D6B8 6A67 6B6E 7072 7A87 37F4"            /* ÂH×ÓÖ¸jgknprz7ô */
    $"0001 88CD FEC6 16C5 C4C1 BEB8 AF9D 594B"            /* ..ÍþÆ.ÅÄÁ¾¸¯YK */
    $"4841 3A35 2F2A 2420 1E1A 1814 10B6 C5FF"            /* HA:5/*$ .....¶Åÿ */
    $"FFFF 00DE C0FF 1282 0009 090A 0A08 1953"            /* ÿÿ.ÞÀÿ..ÆÆ....S */
    $"6064 686A 6C70 757F 882B F400 0E70 D6CB"            /* `dhjlpu.+ô..pÖË */
    $"CEBA 6E67 6B6D 7072 747E 6E0B F600 012E"            /* Îºngkmprt~n.ö... */
    $"BEFE BF17 BFBE BDBA B6AF A889 524E 4942"            /* ¾þ¿.¿¾½º¶¯¨RNIB */
    $"3B36 302B 2621 1E1B 1815 0693 99FF EAFF"            /* ;60+&!.....ÿêÿ */
    $"1282 0009 090A 0A08 1954 6064 686A 6C70"            /* ..ÆÆ....T`dhjlp */
    $"757F 882B F400 0E70 D6CB CEBA 6E67 6B6D"            /* u.+ô..pÖËÎºngkm */
    $"7072 747E 6E0B F600 012E BEFD BF16 BEBD"            /* prt~n.ö...¾ý¿.¾½ */
    $"BAB6 AFA8 8952 4E49 423B 3630 2B26 211E"            /* º¶¯¨RNIB;60+&!. */
    $"1B18 1506 93EF FF94 FF12 8200 0909 0A0A"            /* ....ïÿÿ..ÆÆ.. */
    $"0819 5360 6468 6A6C 7075 7F88 2BF4 000E"            /* ..S`dhjlpu.+ô.. */
    $"70D6 CBCE BA6E 676B 6D70 7274 7E6E 0BF6"            /* pÖËÎºngkmprt~n.ö */
    $"0001 2EBE FDBF 16BE BDBA B6AF A889 524E"            /* ...¾ý¿.¾½º¶¯¨RN */
    $"4942 3B36 302B 2621 1E1B 1815 0693 C5FF"            /* IB;60+&!.....Åÿ */
    $"FFFF 00E7 C0FF 1250 0009 090A 0A08 124D"            /* ÿÿ.çÀÿ.P.ÆÆ....M */
    $"6164 686B 6D6F 7177 8753 F500 0F03 9CCB"            /* adhkmoqwSõ...Ë */
    $"C4C7 BD71 666B 6D70 7273 7581 3FF7 0005"            /* ÄÇ½qfkmprsu?÷.. */
    $"0C8E BCB7 B7B8 17B7 B6B5 B2AD A69C 6F51"            /* .¼··¸.·¶µ²­¦oQ */
    $"4E49 433C 3631 2B26 221E 1B18 1608 5699"            /* NIC<61+&".....V */
    $"FFEA FF12 5000 0909 0A0A 0812 4D61 6468"            /* ÿêÿ.P.ÆÆ....Madh */
    $"6B6D 6F71 7787 53F5 000F 039C CBC4 C7BD"            /* kmoqwSõ...ËÄÇ½ */
    $"7266 6B6D 7072 7375 813F F700 1D0C 8EBC"            /* rfkmprsu?÷...¼ */
    $"B7B7 B8B7 B6B5 B2AD A69C 6F51 4E49 433C"            /* ··¸·¶µ²­¦oQNIC< */
    $"3631 2B26 221E 1B18 1608 56EF FF94 FF12"            /* 61+&".....Vïÿÿ. */
    $"5000 0909 0A0A 0811 4D61 6468 6B6D 6F71"            /* P.ÆÆ....Madhkmoq */
    $"7787 53F5 000F 039C CBC4 C7BE 7366 6B6D"            /* wSõ...ËÄÇ¾sfkm */
    $"7072 7375 813F F700 1D0C 8EBC B7B7 B8B7"            /* prsu?÷...¼··¸· */
    $"B6B5 B2AD A69C 6F51 4E49 433C 3631 2B26"            /* ¶µ²­¦oQNIC<61+& */
    $"221E 1B18 1608 56C5 FFFF FF00 F7C1 FF14"            /* ".....VÅÿÿÿ.÷Áÿ. */
    $"F424 0209 090A 0A09 0C40 6164 686B 6D70"            /* ô$.ÆÆ..Æ.@adhkmp */
    $"7173 7A76 17F6 0001 4BC1 FEBD 0BB2 6F5E"            /* qszv.ö..KÁþ½.²o^ */
    $"656B 6F72 7374 7777 32F9 0006 0470 B7AE"            /* ekorstww2ù...p·® */
    $"AEB0 B018 B0AE ACA8 A39D 8659 534F 4943"            /* ®°°.°®¬¨£YSOIC */
    $"3D38 312C 2722 1F1C 1916 1022 EA9A FFEB"            /* =81,'"....."êÿë */
    $"FF14 F424 0209 090A 0A09 0B3E 6164 686B"            /* ÿ.ô$.ÆÆ..Æ.>adhk */
    $"6D70 7173 7A76 17F6 0010 4BC1 BEBF C0B0"            /* mpqszv.ö..KÁ¾¿À° */
    $"6C60 696C 7072 7374 7777 32F9 0004 0470"            /* l`ilprstww2ù...p */
    $"B7AE AEFE B017 AEAC A8A3 9D86 5953 4F49"            /* ·®®þ°.®¬¨£YSOI */
    $"433D 3831 2C27 221F 1C19 1610 22EA F0FF"            /* C=81,'"....."êðÿ */
    $"95FF 13F4 2402 0909 0A0A 090C 3F61 6468"            /* ÿ.ô$.ÆÆ..Æ.?adh */
    $"6B6D 7071 737A 7600 17F6 0010 4BC1 BFC2"            /* kmpqszv..ö..KÁ¿Â */
    $"C5AD 6563 6D6F 7072 7374 7777 32F9 0004"            /* Å­ecmoprstww2ù.. */
    $"0470 B7AE AEFE B017 AEAC A8A3 9D86 5953"            /* .p·®®þ°.®¬¨£YS */
    $"4F49 433D 3831 2C27 221F 1C19 1610 22EA"            /* OIC=81,'"....."ê */
    $"C6FF FFFF 010C C1FF 04AB 0108 0909 FE0A"            /* Æÿÿÿ..Áÿ.«..ÆÆþ. */
    $"0D07 2A5E 6267 6B6D 6F71 7274 7D63 0AF8"            /* Â.*^bgkmoqrt}c.ø */
    $"0020 20A4 B9B3 B6BF BFAB 9784 736A 7072"            /* .  ¤¹³¶¿¿«sjpr */
    $"7474 787B 5328 0C01 0006 1940 7FA8 A4A5"            /* ttx{S(.....@.¨¤¥ */
    $"A6A7 A718 A6A4 A19C 998B 6658 5550 4B45"            /* ¦§§.¦¤¡fXUPKE */
    $"3E38 332E 2823 201C 1A17 1214 C99A FFEB"            /* >83.(# .....Éÿë */
    $"FF04 AB01 0809 09FE 0A0D 072A 5E63 676B"            /* ÿ.«..ÆÆþ.Â.*^cgk */
    $"6D6F 7172 747D 630A F800 3920 A4BA B4AD"            /* moqrt}c.ø.9 ¤º´­ */
    $"A799 8379 726B 6B71 7274 7478 7B53 280C"            /* §yrkkqrttx{S(. */
    $"0100 0619 407F A8A4 A5A6 A7A7 A6A4 A19C"            /* ....@.¨¤¥¦§§¦¤¡ */
    $"998B 6658 5550 4B45 3E38 332E 2823 201C"            /* fXUPKE>83.(# . */
    $"1A17 1214 C9F0 FF95 FF04 AB01 0809 09FE"            /* ....Éðÿÿ.«..ÆÆþ */
    $"0A0B 072A 5E62 676B 6D6F 7172 747D 0163"            /* ...*^bgkmoqrt}.c */
    $"0AF8 0039 20A4 BEB5 9B76 4932 3E4E 5C6E"            /* .ø.9 ¤¾µvI2>N\n */
    $"7272 7474 787B 5328 0C01 0006 1940 7FA8"            /* rrttx{S(.....@.¨ */
    $"A4A5 A6A7 A7A6 A4A1 9C99 8B66 5855 504B"            /* ¤¥¦§§¦¤¡fXUPK */
    $"453E 3833 2E28 2320 1C1A 1712 14C9 C6FF"            /* E>83.(# .....ÉÆÿ */
    $"FFFF 0112 C1FF 0162 00FE 09FE 0A0E 0817"            /* ÿÿ..Áÿ.b.þÆþ.... */
    $"5762 6669 6C6F 7172 7475 7E5D 15FB 0022"            /* Wbfiloqrtu~].û." */
    $"0132 96AF A7AF C1D2 DEE9 EEEA D799 6C6F"            /* .2¯§¯ÁÒÞéîê×lo */
    $"7374 7577 7E7E 7764 6076 8B9B 9C98 9A9B"            /* stuw~~wd`v */
    $"9C9D 9D18 9B99 9692 8A6D 5C5A 5651 4B45"            /* .m\ZVQKE */
    $"3F38 332F 2925 201C 1A17 140B A49A FFEB"            /* ?83/)% .....¤ÿë */
    $"FF01 6200 FE09 FE0A 0E08 1757 6266 696C"            /* ÿ.b.þÆþ....Wbfil */
    $"6F71 7274 757E 5D15 FB00 3B01 3296 B19E"            /* oqrtu~].û.;.2± */
    $"9292 9CA6 AFB1 AEA2 7F6B 7173 7475 777E"            /* ¦¯±®¢.kqstuw~ */
    $"7E77 6460 768B 9B9C 989A 9B9C 9D9D 9B99"            /* ~wd`v */
    $"9692 8A6D 5C5A 5651 4B45 3F38 332F 2925"            /* m\ZVQKE?83/)% */
    $"201C 1A17 140B A4F0 FF95 FF01 6200 FE09"            /*  .....¤ðÿÿ.b.þÆ */
    $"FE0A 0B08 1756 6266 696C 6F71 7274 7502"            /* þ....Vbfiloqrtu. */
    $"7E5D 15FB 003B 0132 97B3 8B5A 372F 343A"            /* ~].û.;.2³Z7/4: */
    $"3939 3B4A 6974 7374 7577 7E7E 7764 6076"            /* 99;Jitstuw~~wd`v */
    $"8B9B 9C98 9A9B 9C9D 9D9B 9996 928A 6D5C"            /* m\ */
    $"5A56 514B 453F 3833 2F29 2520 1C1A 1714"            /* ZVQKE?83/)% .... */
    $"0BA4 C6FF FFFF 011E C2FF 04F9 3600 0909"            /* .¤Æÿÿÿ..Âÿ.ù6.ÆÆ */
    $"FD0A 3709 0C46 6264 696B 6E70 7274 7475"            /* ý.7Æ.Fbdiknprttu */
    $"7D75 4520 100F 182E 64A0 A39D A8BD D0DB"            /* }uE ....d £¨½ÐÛ */
    $"E3EC F2F7 FDF5 B173 6F73 7475 7577 7A80"            /* ãìò÷ýõ±sostuuwz */
    $"8688 898A 8D8F 9193 9394 9318 908E 8B84"            /* . */
    $"6F61 5F5B 5652 4C46 413A 3431 2B25 211D"            /* oa_[VRLFA:41+%!. */
    $"1917 1504 849A FFEC FF04 F936 0009 09FD"            /* ....ÿìÿ.ù6.ÆÆý */
    $"0A50 090C 4562 6469 6B6E 7072 7474 757D"            /* .PÆ.Ebdiknprttu} */
    $"7545 2010 0F18 2E64 A0A5 907F 8C9C A5AB"            /* uE ....d ¥.¥« */
    $"B2B7 BABE B78C 6E70 7374 7575 777A 8086"            /* ²·º¾·npstuuwz */
    $"8889 8A8D 8F91 9393 9493 908E 8B84 6F61"            /* oa */
    $"5F5B 5652 4C46 413A 3431 2B25 211D 1917"            /* _[VRLFA:41+%!... */
    $"1504 84F0 FF96 FF04 F936 0009 09FD 0A0B"            /* ..ðÿÿ.ù6.ÆÆý.. */
    $"090B 4562 6469 6B6E 7072 7474 4475 7D75"            /* Æ.EbdiknprttDu}u */
    $"4520 100F 182E 64A0 A775 302A 3338 3A3C"            /* E ....d §u0*38:< */
    $"3E3F 3F3B 4362 7473 7475 7577 7A80 8688"            /* >??;Cbtstuuwz */
    $"898A 8D8F 9193 9394 9390 8E8B 846F 615F"            /* oa_ */
    $"5B56 524C 4641 3A34 312B 2521 1D19 1715"            /* [VRLFA:41+%!.... */
    $"0484 C6FF FFFF 0117 C2FF 04D7 1005 0909"            /* .Æÿÿÿ..Âÿ.×..ÆÆ */
    $"FC0A 3108 275C 6467 6A6C 6F71 7274 7576"            /* ü.1.'\dgjloqrtuv */
    $"797F 7D7C 8087 9299 958E 9EB8 CCDA E2EB"            /* y.}|¸ÌÚâë */
    $"F2F7 FAFB FDFC C476 6E73 7474 7675 7577"            /* ò÷úûýüÄvnsttvuuw */
    $"797D 8083 86FC 8819 8682 7A6C 6563 605C"            /* y}ü.zlec`\ */
    $"5853 4D47 413B 3531 2B26 221E 1B18 150A"            /* XSMGA;51+&"..... */
    $"47FC 9BFF ECFF 04D7 1005 0909 FC0A 3108"            /* Güÿìÿ.×..ÆÆü.1. */
    $"275C 6467 6A6C 6F71 7274 7576 797F 7D7C"            /* '\dgjloqrtuvy.}| */
    $"8087 9299 9786 7889 9AA4 AAB1 B6BA BCBC"            /* x¤ª±¶º¼¼ */
    $"BEBD 976E 7073 7474 7675 7577 797D 8083"            /* ¾½npsttvuuwy} */
    $"86FC 8819 8682 7A6C 6563 605C 5853 4D47"            /* ü.zlec`\XSMG */
    $"413B 3531 2B26 221E 1B18 150A 47FC F1FF"            /* A;51+&".....Güñÿ */
    $"96FF 04D7 1005 0909 FC0A 0A08 275C 6467"            /* ÿ.×..ÆÆü...'\dg */
    $"6A6C 6F71 7274 2675 7679 7F7D 7C80 8792"            /* jloqrt&uvy.}| */
    $"999A 752B 2B34 383A 3C3D 3F3F 4040 3D3C"            /* u++48:<=??@@=< */
    $"5E75 7374 7476 7575 7779 7D80 8386 FC88"            /* ^usttvuuwy}ü */
    $"1986 827A 6C65 6360 5C58 534D 4741 3B35"            /* .zlec`\XSMGA;5 */
    $"312B 2622 1E1B 1815 0A47 FCC7 FFFF FF01"            /* 1+&".....GüÇÿÿÿ. */
    $"15C2 FF04 8700 0809 09FB 0A25 0D41 6365"            /* .Âÿ...ÆÆû.%ÂAce */
    $"686B 6E70 7273 7475 7576 787B 7F83 8688"            /* hknprstuuvx{. */
    $"868D B0C7 D8E2 EAF2 F8FB FCFC FBFA FBBC"            /* °ÇØâêòøûüüûúû¼ */
    $"7172 FD75 FF76 FF75 0777 797B 7D7E 7D7D"            /* qrýuÿvÿu.wy{}~}} */
    $"7B19 7770 6A68 6764 615D 5854 4F48 413C"            /* {.wpjhgda]XTOHA< */
    $"3733 2C27 221E 1B19 1610 1CE6 9BFF ECFF"            /* 73,'"......æÿìÿ */
    $"0487 0008 0909 FB0A 250D 4163 6568 6B6E"            /* ...ÆÆû.%ÂAcehkn */
    $"7072 7374 7575 7678 7B7F 8386 8982 6F83"            /* prstuuvx{.o */
    $"95A3 AAB1 B6BA BDBE BDBC BDBC 906B 73FD"            /* £ª±¶º½¾½¼½¼ksý */
    $"75FF 76FF 7521 7778 7B7D 7E7D 7D7B 7770"            /* uÿvÿu!wx{}~}}{wp */
    $"6A68 6764 615D 5854 4F48 413C 3733 2C27"            /* jhgda]XTOHA<73,' */
    $"221E 1B19 1610 1CE6 F1FF 96FF 0487 0008"            /* "......æñÿÿ... */
    $"0909 FB0A 090D 4163 6568 6B6E 7072 7311"            /* ÆÆû.ÆÂAcehknprs. */
    $"7475 7576 787B 7F83 858B 7C33 2932 373A"            /* tuuvx{.|3)27: */
    $"3C3D FB40 033D 3B60 76FD 75FF 76FF 7521"            /* <=û@.=;`výuÿvÿu! */
    $"7779 7B7D 7E7D 7D7B 7770 6A68 6764 615D"            /* wy{}~}}{wpjhgda] */
    $"5854 4F48 413C 3733 2C27 221E 1B19 1610"            /* XTOHA<73,'"..... */
    $"1CE6 C7FF FFFF 0115 C2FF 014D 00FE 09FD"            /* .æÇÿÿÿ..Âÿ.M.þÆý */
    $"0AFF 0B0B 0913 4665 676A 6D6E 7072 7374"            /* .ÿ..Æ.Fegjmnprst */
    $"FC75 1777 7B7A 7EA2 C0D5 E2EB F2FA FDFE"            /* üu.w{z~¢ÀÕâëòúýþ */
    $"FDFC FAF7 F4F2 AE5B 6871 74FE 76FF 7507"            /* ýüú÷ôò®[hqtþvÿu. */
    $"7472 716E 6C6D 6F6E 196C 6B6B 6967 6462"            /* trqnlmon.lkkigdb */
    $"5E59 5550 4A43 3E38 332D 2823 1F1C 1916"            /* ^YUPJC>83-(#.... */
    $"1213 C29B FFEC FF01 4D00 FE09 FD0A FF0B"            /* ..Âÿìÿ.M.þÆý.ÿ. */
    $"0B09 1246 6567 6A6D 6E70 7273 74FC 750A"            /* .Æ.Fegjmnprstüu. */
    $"777C 7A68 7990 A1AA B0B6 BCFD BE2F BBB9"            /* w|zhy¡ª°¶¼ý¾/»¹ */
    $"B8B6 8758 6A71 7375 7676 7574 7373 716E"            /* ¸¶Xjqsuvvutssqn */
    $"6D6E 6F6E 6C6B 6B69 6764 625E 5955 504A"            /* mnonlkkigdb^YUPJ */
    $"433E 3833 2D28 231F 1C19 1612 13C2 F1FF"            /* C>83-(#......Âñÿ */
    $"96FF 014D 00FE 09FD 0AFF 0B09 0912 4665"            /* ÿ.M.þÆý.ÿ.ÆÆ.Fe */
    $"676A 6D6E 7072 0173 74FC 7509 777D 7939"            /* gjmnpr.stüuÆw}y9 */
    $"2530 363A 3C3E FC40 2F3F 3E3E 3B37 516B"            /* %06:<>ü@/?>>;7Qk */
    $"7173 7576 7675 7473 7370 6F6C 6D6F 6E6C"            /* qsuvvutsspolmonl */
    $"6B6B 6967 6462 5E59 5550 4A43 3E38 332D"            /* kkigdb^YUPJC>83- */
    $"2823 1F1C 1916 1213 C2C7 FFFF FF01 1EC3"            /* (#......ÂÇÿÿÿ..Ã */
    $"FF02 F322 03FE 09FD 0AFE 0B34 0912 3F62"            /* ÿ.ó".þÆý.þ.4Æ.?b */
    $"6A6B 6C6F 7172 7374 7475 7677 7566 5F8E"            /* jkloqrsttuvwuf_ */
    $"B2CD DFEA F3FA FEFF FEFD FBF7 F4F0 EEEB"            /* ²Íßêóúþÿþýû÷ôðîë */
    $"5E18 3341 4B52 5759 5B5E 6061 6364 696C"            /* ^.3AKRWY[^`acdil */
    $"6C19 6D6B 6B6A 6865 625E 5A56 514B 453F"            /* l.mkkjheb^ZVQKE? */
    $"3933 2D28 241F 1D19 1615 099E 9BFF EDFF"            /* 93-($.....Æÿíÿ */
    $"02F3 2203 FE09 FD0A FE0B 1909 123F 616A"            /* .ó".þÆý.þ..Æ.?aj */
    $"6B6C 6F71 7273 7474 7576 7775 6654 6A86"            /* kloqrsttuvwufTj */
    $"9BA8 B0B7 BCFE BF31 BEBD BAB8 B5B3 B04A"            /* ¨°·¼þ¿1¾½º¸µ³°J */
    $"1B33 414B 5257 595B 5D60 6263 6468 6C6C"            /* .3AKRWY[]`bcdhll */
    $"6D6B 6B6A 6865 625E 5A56 514B 453F 3933"            /* mkkjheb^ZVQKE?93 */
    $"2D28 241F 1D19 1615 099E F1FF 97FF 02F3"            /* -($.....Æñÿÿ.ó */
    $"2203 FE09 FD0A FE0B 0809 133E 626A 6B6C"            /* ".þÆý.þ..Æ.>bjkl */
    $"6F71 1072 7374 7475 7678 7569 3D21 2C35"            /* oq.rsttuvxui=!,5 */
    $"393C 3F40 FE41 3140 3F3F 3D3D 3C39 2221"            /* 9<?@þA1@??==<9"! */
    $"3341 4B52 5759 5C5E 6061 6464 696C 6C6D"            /* 3AKRWY\^`addillm */
    $"6B6B 6A68 6562 5E5A 5651 4B45 3F39 332D"            /* kkjheb^ZVQKE?93- */
    $"2824 1F1D 1916 1509 9EC7 FFFF FF01 18C3"            /* ($.....ÆÇÿÿÿ..Ã */
    $"FF02 D00C 06FE 09FD 0AFD 0B17 0A0E 264B"            /* ÿ.Ð..þÆý.ý....&K */
    $"656D 7072 7374 7575 736A 5239 2C64 A1BD"            /* emprstuusjR9,d¡½ */
    $"D9E8 F3FA FEFF 18FE FDF9 F4F0 EDE9 EF9E"            /* Ùèóúþÿ.þýùôðíéï */
    $"373D 3F42 464C 5056 5B5F 6467 696A 6C6C"            /* 7=?BFLPV[_dgijll */
    $"FF6C 176B 6A68 6563 5F5B 5752 4C46 3F3A"            /* ÿl.kjhec_[WRLF?: */
    $"342F 2824 201C 1A17 1505 789B FFED FF02"            /* 4/($ .....xÿíÿ. */
    $"D00C 06FE 09FD 0AFD 0B31 0A0D 264C 656D"            /* Ð..þÆý.ý.1.Â&Lem */
    $"7072 7374 7575 736A 523A 284B 788E A4AF"            /* prstuusjR:(Kx¤¯ */
    $"B6BD C1C2 C1C0 BEBC B8B5 B2AF B27C 3A3E"            /* ¶½ÁÂÁÀ¾¼¸µ²¯²|:> */
    $"3F42 464C 4F55 5B5F 6467 696A FD6C 176B"            /* ?BFLOU[_dgijýl.k */
    $"6A68 6563 5F5B 5752 4C46 3F3A 342F 2824"            /* jhec_[WRLF?:4/($ */
    $"201C 1A17 1505 78F1 FF97 FF02 D00C 06FE"            /*  .....xñÿÿ.Ð..þ */
    $"09FD 0AFD 0B07 0A0D 264B 656D 7071 0F72"            /* Æý.ý...Â&Kempq.r */
    $"7475 7573 6A53 3B23 1828 3037 3B3F 40FD"            /* tuusjS;#.(07;?@ý */
    $"4115 403F 3D3C 3C3B 3A38 3E3E 4041 454C"            /* A.@?=<<;:8>>@AEL */
    $"4F56 5B5F 6467 696A FD6C 176B 6A68 6563"            /* OV[_dgijýl.kjhec */
    $"5F5B 5752 4C46 3F3A 342F 2824 201C 1A17"            /* _[WRLF?:4/($ ... */
    $"1505 78C7 FFFF FF01 1CC3 FF04 A501 0709"            /* ..xÇÿÿÿ..Ãÿ.¥..Æ */
    $"09FC 0AFD 0B16 0C0B 0911 2335 4450 5655"            /* Æü.ý....Æ.#5DPVU */
    $"4D40 3326 1D16 377F A9C8 E4F2 FCFE FF19"            /* M@3&..7.©Èäòüþÿ. */
    $"FEFD FAF6 F1ED E9E5 E5B7 4F4F 5356 585B"            /* þýúöñíéåå·OOSVX[ */
    $"5E60 6264 6668 696B 6C6C FF6C 186B 6A68"            /* ^`bdfhikllÿl.kjh */
    $"6563 605C 5852 4D48 413A 352F 2A25 211D"            /* ec`\XRMHA:5/*%!. */
    $"1B18 160C 40FA 9CFF EDFF 04A5 0107 0909"            /* ....@úÿíÿ.¥..ÆÆ */
    $"FC0A FD0B 310C 0B09 1023 3544 5056 554D"            /* ü.ý.1..Æ.#5DPVUM */
    $"4033 261D 162C 6080 96AD B6BE C2C4 C3C1"            /* @3&..,`­¶¾ÂÄÃÁ */
    $"BFBD BAB6 B3B0 ACAB 8E4F 5053 5659 5B5E"            /* ¿½º¶³°¬«OPSVY[^ */
    $"6062 6466 6869 6BFD 6C18 6B6A 6865 6360"            /* `bdfhikýl.kjhec` */
    $"5C58 524D 4841 3A35 2F2A 2521 1D1B 1816"            /* \XRMHA:5/*%!.... */
    $"0C40 FAF2 FF97 FF04 A501 0709 09FC 0AFD"            /* .@úòÿÿ.¥..ÆÆü.ý */
    $"0B07 0C0B 0910 2335 4450 0F57 554D 4133"            /* ....Æ.#5DP.WUMA3 */
    $"261E 1912 1F2B 323A 3F40 41FE 4216 4140"            /* &....+2:?@AþB.A@ */
    $"3F3D 3C3C 3B39 3B4E 5153 5658 5B5E 6062"            /* ?=<<;9;NQSVX[^`b */
    $"6466 6869 6BFD 6C18 6B6A 6865 6360 5C58"            /* dfhikýl.kjhec`\X */
    $"524D 4841 3A35 2F2A 2521 1D1B 1816 0C40"            /* RMHA:5/*%!.....@ */
    $"FAC8 FFFF FF01 1AC3 FF04 7200 0809 09FC"            /* úÈÿÿÿ..Ãÿ.r..ÆÆü */
    $"0AFD 0BFE 0C12 0B0A 090C 1012 1210 1215"            /* .ý.þ....Æ....... */
    $"1A1A 1D55 85B0 D4F5 FEFD FF19 FEFB F7F3"            /* ...U°Ôõþýÿ.þû÷ó */
    $"EEEA E5DF DABA 504D 5154 575A 5C5F 6163"            /* îêåßÚºPMQTWZ\_ac */
    $"6567 696A 6B6C FF6C 186B 6A69 6664 615C"            /* egijklÿl.kjifda\ */
    $"5854 4E48 433D 3730 2B26 211E 1B18 1511"            /* XTNHC=70+&!..... */
    $"1CE4 9CFF EDFF 0472 0008 0909 FC0A FD0B"            /* .äÿíÿ.r..ÆÆü.ý. */
    $"FE0C 2F0B 0A09 0B10 1211 1011 1519 1B1A"            /* þ./..Æ.......... */
    $"4064 849F B9BE C1C6 C5C2 C0BC BAB7 B3B0"            /* @d¹¾ÁÆÅÂÀ¼º·³° */
    $"ACA9 A48F 4E4E 5154 575A 5C5F 6163 6567"            /* ¬©¤NNQTWZ\_aceg */
    $"696A 6BFE 6C18 6B6A 6966 6461 5C58 544E"            /* ijkþl.kjifda\XTN */
    $"4843 3D37 302B 2621 1E1B 1815 111C E4F2"            /* HC=70+&!......äò */
    $"FF97 FF04 7200 0809 09FC 0AFD 0BFE 0C04"            /* ÿÿ.r..ÆÆü.ý.þ.. */
    $"0B0A 090C 10FF 12FF 1126 151A 1C14 1621"            /* ..Æ..ÿ.ÿ.&.....! */
    $"2C37 423F 4043 4341 4040 3F3D 3C3C 3B39"            /* ,7B?@CCA@@?=<<;9 */
    $"3637 4B4F 5154 575A 5C5F 6163 6567 696A"            /* 67KOQTWZ\_acegij */
    $"6BFE 6C18 6B6A 6966 6461 5C58 544E 4843"            /* kþl.kjifda\XTNHC */
    $"3D37 302B 2621 1E1B 1815 111C E4C8 FFFF"            /* =70+&!......äÈÿÿ */
    $"FF01 0CC4 FF02 EE21 03FE 09FC 0AFD 0BFD"            /* ÿ..Äÿ.î!.þÆü.ý.ý */
    $"0CFD 0D0C 0F12 1619 1B1C 1533 5D81 AFDB"            /* .ýÂ........3]¯Û */
    $"FDFC FF19 FBF7 F2EF EAE4 DED5 CDB0 504D"            /* ýüÿ.û÷òïêäÞÕÍ°PM */
    $"5153 565A 5C5E 6062 6567 6869 6B6C FE6C"            /* QSVZ\^`beghiklþl */
    $"176B 6966 6461 5E59 544F 4944 3E38 312B"            /* .kifda^YTOID>81+ */
    $"2723 1F1D 1916 1312 C19C FFEE FF02 EE21"            /* '#......Áÿîÿ.î! */
    $"03FE 09FC 0AFD 0BFD 0CFD 0D2A 0F12 1619"            /* .þÆü.ý.ý.ýÂ*.... */
    $"1B1D 1628 4561 84A5 C6DE DACA C5C1 BDBA"            /* ...(Ea¥ÆÞÚÊÅÁ½º */
    $"B7B4 B0AC A7A0 9A87 4E4E 5153 565A 5C5E"            /* ·´°¬§ NNQSVZ\^ */
    $"6062 6567 6869 6BFD 6C17 6B69 6664 615E"            /* `beghikýl.kifda^ */
    $"5954 4F49 443E 3831 2B27 231F 1D19 1613"            /* YTOID>81+'#..... */
    $"12C1 F2FF 98FF 02EE 2103 FE09 FC0A FD0B"            /* .Áòÿÿ.î!.þÆü.ý. */
    $"FD0C FD0D 2A0F 1216 191B 1D18 1217 202C"            /* ý.ýÂ*......... , */
    $"394C 6459 4642 4140 3F3E 3D3C 3B39 3733"            /* 9LdYFBA@?>=<;973 */
    $"334A 4F51 5356 5A5C 5E60 6265 6768 696B"            /* 3JOQSVZ\^`beghik */
    $"FD6C 176B 6966 6461 5E59 544F 4944 3E38"            /* ýl.kifda^YTOID>8 */
    $"312B 2723 1F1D 1916 1312 C1C8 FFFF FF01"            /* 1+'#......ÁÈÿÿÿ. */
    $"17C4 FF02 C407 07FE 09FD 0AFC 0BFD 0CFF"            /* .Äÿ.Ä..þÆý.ü.ý.ÿ */
    $"0D2D 1013 1618 1819 1B1A 1950 5B74 9CBD"            /* Â-.........P[t½ */
    $"DFF6 FEFF FFFC F6F2 EEE9 E3DC D1C7 BF92"            /* ßöþÿÿüöòîéãÜÑÇ¿ */
    $"4B4E 5153 565A 5C5E 6062 6567 6869 6B6B"            /* KNQSVZ\^`beghikk */
    $"FE6C 176B 6966 6563 5F5A 5650 4B45 3E39"            /* þl.kifec_ZVPKE>9 */
    $"332D 2824 1F1D 1917 1509 9F9C FFEE FF02"            /* 3-($.....Æÿîÿ. */
    $"C407 07FE 09FD 0AFC 0BFD 0CFF 0D2D 1012"            /* Ä..þÆý.ü.ý.ÿÂ-.. */
    $"1618 1819 1B1A 173C 4557 768E AEDE F1CF"            /* .......<EWv®ÞñÏ */
    $"C1BD B9B7 B4B0 ABA5 9E96 8F73 4B4F 5153"            /* Á½¹·´°«¥sKOQS */
    $"565A 5C5E 6062 6567 6869 6B6B FE6C 176B"            /* VZ\^`beghikkþl.k */
    $"6966 6563 5F5A 5650 4B45 3E39 332D 2824"            /* ifec_ZVPKE>93-($ */
    $"1F1D 1917 1509 9FF2 FF98 FF02 C407 07FE"            /* .....Æòÿÿ.Ä..þ */
    $"09FD 0AFC 0BFD 0CFF 0D01 1013 2B16 1818"            /* Æý.ü.ý.ÿÂ...+... */
    $"191B 1B12 1417 1D28 3245 797D 4E42 403F"            /* .......(2Ey}NB@? */
    $"3D3C 3C3A 3836 332F 334C 4F51 5356 5A5C"            /* =<<:863/3LOQSVZ\ */
    $"5E60 6265 6768 696B 6BFE 6C17 6B69 6665"            /* ^`beghikkþl.kife */
    $"635F 5A56 504B 453E 3933 2D28 241F 1D19"            /* c_ZVPKE>93-($... */
    $"1715 099F C8FF FFFF 011A C4FF 029A 0008"            /* ..ÆÈÿÿÿ..Äÿ... */
    $"FE09 FD0A FC0B FE0C 300D 1012 1416 1618"            /* þÆý.ü.þ.0Â...... */
    $"181A 1C13 2357 5D6B 839A B5CA E3F8 F9F5"            /* ....#W]kµÊãøùõ */
    $"F2EE E9E3 D9CF C4B8 AC73 474F 5153 5659"            /* òîéãÙÏÄ¸¬sGOQSVY */
    $"5B5E 6062 6567 6869 6B6B FE6C 176B 6A68"            /* [^`beghikkþl.kjh */
    $"6563 5F5B 5752 4C46 413B 342F 2925 211D"            /* ec_[WRLFA;4/)%!. */
    $"1917 1604 7D9C FFEE FF02 9A00 08FE 09FD"            /* ....}ÿîÿ...þÆý */
    $"0AFC 0BFE 0C30 0D0F 1215 1616 1818 1A1C"            /* .ü.þ.0Â......... */
    $"141D 4146 5163 758D 9BB1 BEBC B9B6 B3AF"            /* ..AFQcu±¾¼¹¶³¯ */
    $"ABA3 9C94 8A80 5F49 4F51 5356 595B 5E60"            /* «£_IOQSVY[^` */
    $"6265 6768 696B 6BFE 6C17 6B6A 6865 635F"            /* beghikkþl.kjhec_ */
    $"5B57 524C 4641 3B34 2F29 2521 1D19 1716"            /* [WRLFA;4/)%!.... */
    $"047D F2FF 98FF 029A 0008 FE09 FD0A FC0B"            /* .}òÿÿ...þÆý.ü. */
    $"FE0C 040D 0F12 1516 2B16 1818 1A1C 1611"            /* þ..Â....+....... */
    $"1618 1B23 2D3D 3F44 4641 3E3E 3D3B 3A38"            /* ...#-=?DFA>>=;:8 */
    $"3532 2F28 364E 4F51 5356 595B 5E60 6265"            /* 52/(6NOQSVY[^`be */
    $"6768 696B 6BFE 6C17 6B6A 6865 635F 5B57"            /* ghikkþl.kjhec_[W */
    $"524C 4641 3B34 2F29 2521 1D19 1716 047D"            /* RLFA;4/)%!.....} */
    $"C8FF FFFF 011A C4FF 015D 00FE 09FC 0AFD"            /* Èÿÿÿ..Äÿ.].þÆü.ý */
    $"0BFE 0C01 0F11 FE14 2C15 1717 1413 150B"            /* .þ....þ.,....... */
    $"305C 626F 7C8C A1AC BED9 ECEF ECE7 E0D7"            /* 0\bo|¡¬¾Ùìïìçà× */
    $"CBC0 B3A0 8A5A 494F 5153 5659 5B5E 6062"            /* ËÀ³ ZIOQSVY[^`b */
    $"6567 6869 6B6B FE6C 176B 6A68 6664 605C"            /* eghikkþl.kjhfd`\ */
    $"5853 4D48 423C 362F 2A26 221E 1A17 1609"            /* XSMHB<6/*&"....Æ */
    $"5D9C FFEE FF01 5D00 FE09 FC0A FD0B FE0C"            /* ]ÿîÿ.].þÆü.ý.þ. */
    $"010E 12FE 142C 1517 1714 1315 0C26 454A"            /* ...þ.,.......&EJ */
    $"545E 6B7C 8592 A3B2 B4B2 AEA9 A299 9187"            /* T^k|£²´²®©¢ */
    $"7866 4F4B 4F51 5356 595B 5E60 6265 6768"            /* xfOKOQSVY[^`begh */
    $"696B 6BFE 6C17 6B6A 6866 6460 5C58 534D"            /* ikkþl.kjhfd`\XSM */
    $"4842 3C36 2F2A 2622 1E1A 1716 095D F2FF"            /* HB<6/*&"....Æ]òÿ */
    $"98FF 015D 00FE 09FC 0AFD 0BFE 0C01 0F12"            /* ÿ.].þÆü.ý.þ.... */
    $"FE14 0015 FF17 2914 1315 0F14 1719 1C20"            /* þ...ÿ.)........  */
    $"2732 3637 393D 3E3C 3B3A 3834 312E 281D"            /* '2679=><;:841.(. */
    $"394E 4F51 5356 595B 5E60 6265 6768 696B"            /* 9NOQSVY[^`beghik */
    $"6BFE 6C17 6B6A 6866 6460 5C58 534D 4842"            /* kþl.kjhfd`\XSMHB */
    $"3C36 2F2A 2622 1E1A 1716 095D C8FF FFFF"            /* <6/*&"....Æ]Èÿÿÿ */
    $"0123 C5FF 02EB 1A03 FE09 FC0A FD0B 040C"            /* .#Åÿ.ë..þÆü.ý... */
    $"0E10 1213 FE14 2C12 0F16 304C 4551 5A5A"            /* ....þ.,...0LEQZZ */
    $"6875 7C83 929C A7BC D8E5 E2DB D2C8 BAAB"            /* hu|§¼ØåâÛÒÈº« */
    $"9781 6D44 484F 5153 5659 5B5E 6062 6466"            /* mDHOQSVY[^`bdf */
    $"6869 6B6B FE6C 186B 6A68 6664 615D 5954"            /* hikkþl.kjhfda]YT */
    $"4F4A 443E 3731 2C27 221F 1B18 160E 39F8"            /* OJD>71,'".....9ø */
    $"9DFF EFFF 02EB 1A03 FE09 FC0A FD0B 040C"            /* ÿïÿ.ë..þÆü.ý... */
    $"0D10 1213 FE14 2C12 0F16 2F4C 4652 5042"            /* Â...þ.,.../LFRPB */
    $"4E58 5D64 7077 808F A3AC AAA5 9E97 8C81"            /* NX]dpw£¬ª¥ */
    $"7161 5B42 484F 5153 5659 5B5E 6062 6466"            /* qa[BHOQSVY[^`bdf */
    $"6869 6B6B FE6C 186B 6A68 6664 615D 5954"            /* hikkþl.kjhfda]YT */
    $"4F4A 443E 3731 2C27 221F 1B18 160E 39F8"            /* OJD>71,'".....9ø */
    $"F3FF 99FF 02EB 1A03 FE09 FC0A FD0B 040C"            /* óÿÿ.ë..þÆü.ý... */
    $"0E10 1213 FE14 0012 2B10 1630 4C46 553B"            /* ....þ...+..0LFU; */
    $"121B 1E1F 2229 2E32 3438 3B3A 3936 3430"            /* ....").248;:9640 */
    $"2C25 2035 4049 4F51 5356 595B 5E60 6264"            /* ,% 5@IOQSVY[^`bd */
    $"6668 696B 6BFE 6C18 6B6A 6866 6461 5D59"            /* fhikkþl.kjhfda]Y */
    $"544F 4A44 3E37 312C 2722 1F1B 1816 0E39"            /* TOJD>71,'".....9 */
    $"F8C9 FFFF FF01 26C5 FF02 C509 06FE 09FC"            /* øÉÿÿÿ.&Åÿ.ÅÆ.þÆü */
    $"0AFE 0B35 0D0F 1112 1213 130E 1329 4F86"            /* .þ.5Â........)O */
    $"B8AC 7D7F 695B 6E78 7B7D 8690 99A5 BED3"            /* ¸¬}.i[nx{}¥¾Ó */
    $"D3CB BFB2 9E88 6E8D DD99 5146 4E54 5658"            /* ÓË¿²nÝQFNTVX */
    $"5B5E 6062 6466 6768 6A6B FE6C FF6B 1669"            /* [^`bdfghjkþlÿk.i */
    $"6765 625E 5954 504B 4640 3932 2D28 2420"            /* geb^YTPKF@92-($  */
    $"1B18 1611 1FE5 9DFF EFFF 02C5 0906 FE09"            /* .....åÿïÿ.ÅÆ.þÆ */
    $"FC0A FE0B 350D 0F11 1212 1313 0E12 294E"            /* ü.þ.5Â........)N */
    $"86B9 AC7E 815E 4253 5A5D 5F65 6D74 7E90"            /* ¹¬~^BSZ]_emt~ */
    $"9F9F 9990 8677 6652 7DDD 9A51 464E 5456"            /* wfR}ÝQFNTV */
    $"585B 5E60 6264 6667 686A 6BFE 6CFF 6B16"            /* X[^`bdfghjkþlÿk. */
    $"6967 6562 5E59 5450 4B46 4039 322D 2824"            /* igeb^YTPKF@92-($ */
    $"201B 1816 111F E5F3 FF99 FF02 C509 06FE"            /*  .....åóÿÿ.ÅÆ.þ */
    $"09FC 0AFE 0B09 0D0F 1112 1213 130E 1229"            /* Æü.þ.ÆÂ........) */
    $"2B4F 86B9 AC7E 8449 101D 1F1F 2123 272C"            /* +O¹¬~I....!#', */
    $"2E32 3636 3432 2E28 221A 5FDB 9B51 464E"            /* .26642.("._ÛQFN */
    $"5456 585B 5E60 6264 6667 686A 6BFE 6CFF"            /* TVX[^`bdfghjkþlÿ */
    $"6B16 6967 6562 5E59 5450 4B46 4039 322D"            /* k.igeb^YTPKF@92- */
    $"2824 201B 1816 111F E5C9 FFFF FF01 26C5"            /* ($ .....åÉÿÿÿ.&Å */
    $"FF02 9800 08FE 09FC 0AFF 0B36 0E10 1011"            /* ÿ...þÆü.ÿ.6.... */
    $"1212 0F10 4288 AFC2 CCB7 8276 7B68 5E73"            /* ....B¯ÂÌ·v{h^s */
    $"7879 797A 7E86 8F9F B4B7 AA9A 866E 5A7F"            /* xyyz~´·ªnZ. */
    $"ECFF FFE6 A55A 4B55 595B 5D5F 6264 6667"            /* ìÿÿæ¥ZKUY[]_bdfg */
    $"686A 6BFD 6C17 6B69 6765 625F 5B56 514C"            /* hjkýl.kigeb_[VQL */
    $"4741 3A33 2E29 2521 1D19 1715 089B 9DFF"            /* GA:3.)%!.....ÿ */
    $"EFFF 0298 0008 FE09 FC0A FF0B 130E 1010"            /* ïÿ...þÆü.ÿ..... */
    $"1112 120F 1042 88B0 C2CC B782 767C 5F45"            /* .....B°ÂÌ·v|_E */
    $"56FE 5A1F 5C5F 656C 7987 8980 7465 5143"            /* VþZ.\_elyteQC */
    $"73EC FFFF E7A5 5A4B 5559 5B5D 5F62 6466"            /* sìÿÿç¥ZKUY[]_bdf */
    $"6768 6A6B FD6C 176B 6967 6562 5F5B 5651"            /* ghjkýl.kigeb_[VQ */
    $"4C47 413A 332E 2925 211D 1917 1508 9BF3"            /* LGA:3.)%!.....ó */
    $"FF99 FF02 9800 08FE 09FC 0AFF 0B0A 0E10"            /* ÿÿ...þÆü.ÿ.... */
    $"1011 1212 0F10 4388 B009 C2CC B782 767F"            /* ......C°ÆÂÌ·v. */
    $"4D12 1D1E FE1F 1E20 2327 2A2E 2F2C 2722"            /* M...þ.. #'*./,'" */
    $"1916 5EEB FFFF E6A5 5A4B 5559 5B5D 5F62"            /* ..^ëÿÿæ¥ZKUY[]_b */
    $"6466 6768 6A6B FD6C 176B 6967 6562 5F5B"            /* dfghjkýl.kigeb_[ */
    $"5651 4C47 413A 332E 2925 211D 1917 1508"            /* VQLGA:3.)%!..... */
    $"9BC9 FFFF FF01 1BC5 FF01 5B00 FD09 FD0A"            /* Éÿÿÿ..Åÿ.[.ýÆý. */
    $"040B 0D0E 1010 FE11 1E0A 2C82 B6C2 BFC2"            /* ..Â...þ...,¶Â¿Â */
    $"BF8E 7578 7A74 6170 7676 7776 7779 7D83"            /* ¿uxztapvvwvwy} */
    $"8986 7969 5C59 75DE FCFF 0DE4 824D 575A"            /* yi\YuÞüÿÂäMWZ */
    $"5D5F 6163 6568 686A 6BFC 6C16 6967 6562"            /* ]_acehhjkül.igeb */
    $"5F5C 5752 4D48 423C 362F 2A26 211D 1A18"            /* _\WRMHB<6/*&!... */
    $"1605 6C9D FFEF FF01 5B00 FD09 FD0A 040B"            /* ..lÿïÿ.[.ýÆý... */
    $"0D0E 1010 FE11 0E0A 2C82 B6C2 BFC2 BF8E"            /* Â...þ...,¶Â¿Â¿ */
    $"7578 7A72 4C53 FE59 0C58 595B 5E63 6865"            /* uxzrLSþY.XY[^che */
    $"5B4F 4549 6EDD FCFF 0DE4 824D 575A 5D5F"            /* [OEInÝüÿÂäMWZ]_ */
    $"6163 6568 686A 6BFC 6C16 6967 6562 5F5C"            /* acehhjkül.igeb_\ */
    $"5752 4D48 423C 362F 2A26 211D 1A18 1605"            /* WRMHB<6/*&!..... */
    $"6CF3 FF99 FF01 5B00 FD09 FD0A 040B 0D0E"            /* lóÿÿ.[.ýÆý...Â. */
    $"1010 FE11 050A 2C82 B6C2 BF08 C2BF 8E75"            /* ..þ...,¶Â¿.Â¿u */
    $"787B 6E20 18FC 1E0A 1F20 2124 221E 1715"            /* x{n .ü... !$"... */
    $"2861 DDFC FF0D E482 4D57 5A5D 5F61 6365"            /* (aÝüÿÂäMWZ]_ace */
    $"6868 6A6B FC6C 1669 6765 625F 5C57 524D"            /* hhjkül.igeb_\WRM */
    $"4842 3C36 2F2A 2621 1D1A 1816 056C C9FF"            /* HB<6/*&!.....lÉÿ */
    $"FFFF 011B C6FF 04E9 1903 0909 FB0A 000D"            /* ÿÿ..Æÿ.é..ÆÆû..Â */
    $"FE0F 1310 1110 0C49 A3BE B9BA BDC2 A378"            /* þ......I£¾¹º½Â£x */
    $"7678 797B 6E66 70FD 7409 7372 6E66 5E5A"            /* vxy{nfpýtÆsrnf^Z */
    $"5F6C 79CB FAFF 0CF8 9B52 585B 5D60 6365"            /* _lyËúÿ.øRX[]`ce */
    $"6768 696B FD6C 186B 6968 6664 605C 5853"            /* ghikýl.kihfd`\XS */
    $"4E49 443D 3631 2B27 231E 1A19 160B 4CFD"            /* NID=61+'#.....Lý */
    $"9EFF F0FF 04E9 1903 0909 FB0A 000D FE0F"            /* ÿðÿ.é..ÆÆû..Âþ. */
    $"1310 1110 0C49 A3BE B9BA BDC2 A378 7678"            /* .....I£¾¹º½Â£xvx */
    $"797C 674D 53FC 5708 5552 4B45 4550 6578"            /* y|gMSüW.URKEEPex */
    $"CBFA FF0C F89B 5258 5B5D 6063 6567 6869"            /* Ëúÿ.øRX[]`ceghi */
    $"6BFD 6C18 6B69 6866 6460 5C58 534E 4944"            /* kýl.kihfd`\XSNID */
    $"3D36 312B 2723 1E1A 1916 0B4C FDF4 FF9A"            /* =61+'#.....Lýôÿ */
    $"FF04 E919 0309 09FB 0A00 0DFE 0F09 1011"            /* ÿ.é..ÆÆû..Âþ.Æ.. */
    $"100C 49A3 BEB9 BABD 0AC2 A378 7678 797E"            /* ..I£¾¹º½.Â£xvxy~ */
    $"571B 181B FC1C 071B 1713 1930 5475 CDFA"            /* W...ü......0TuÍú */
    $"FF0C F89B 5258 5B5D 6063 6567 6869 6BFD"            /* ÿ.øRX[]`ceghiký */
    $"6C18 6B69 6866 6460 5C58 534E 4944 3D36"            /* l.kihfd`\XSNID=6 */
    $"312B 2723 1E1A 1916 0B4C FDCA FFFF FF01"            /* 1+'#.....LýÊÿÿÿ. */
    $"24C6 FF04 C208 0609 09FC 0A26 0C0E 0F0F"            /* $Æÿ.Â..ÆÆü.&.... */
    $"1010 0E0D 5FB1 B8B5 B8BB C1BA 8475 7778"            /* ...Â_±¸µ¸»Áºuwx */
    $"797A 7B75 6C65 6566 6664 625F 616B 757C"            /* yz{uleeffdb_aku| */
    $"7BB5 FCF9 FF0B FB81 4E5B 5D5F 6365 6667"            /* {µüùÿ.ûN[]_cefg */
    $"696A 006B FE6C 186B 6968 6663 615D 5854"            /* ij.kþl.kihfca]XT */
    $"504A 443E 3832 2D28 241F 1B18 1610 27EE"            /* PJD>82-($.....'î */
    $"9EFF F0FF 04C2 0806 0909 FC0A 190C 0E0F"            /* ÿðÿ.Â..ÆÆü..... */
    $"0F10 100E 0D5F B1B8 B5B8 BBC0 BA84 7577"            /* ....Â_±¸µ¸»Àºuw */
    $"7879 7A7C 725E 4EFE 4D09 4C4B 494F 6171"            /* xyz|r^NþMÆLKIOaq */
    $"7B7C B6FD F9FF 0CFB 814E 5B5D 5F63 6566"            /* {|¶ýùÿ.ûN[]_cef */
    $"6769 6A6B FE6C 186B 6968 6663 615D 5854"            /* gijkþl.kihfca]XT */
    $"504A 443E 3832 2D28 241F 1B18 1610 27EE"            /* PJD>82-($.....'î */
    $"F4FF 9AFF 04C2 0806 0909 FC0A 0E0C 0E0F"            /* ôÿÿ.Â..ÆÆü..... */
    $"0F10 100E 0D5F B1B8 B5B8 BBC1 17B9 8375"            /* ....Â_±¸µ¸»Á.¹u */
    $"7778 797A 7D6B 4221 1C1B 1B1C 1C1D 2C4C"            /* wxyz}kB!......,L */
    $"687A 7FB6 FCF9 FF0C FB81 4E5B 5D5F 6365"            /* hz.¶üùÿ.ûN[]_ce */
    $"6667 696A 6BFE 6C18 6B69 6866 6361 5D58"            /* fgijkþl.kihfca]X */
    $"5450 4A44 3E38 322D 2824 1F1B 1816 1027"            /* TPJD>82-($.....' */
    $"EECA FFFF FF01 24C6 FF04 9800 0809 09FE"            /* îÊÿÿÿ.$Æÿ...ÆÆþ */
    $"0AFF 0C1A 0D0E 0F0F 110C 156F B2B4 B4B7"            /* .ÿ..Â......o²´´· */
    $"BABE C09A 7676 7778 7979 7A7B 7B78 75FE"            /* º¾Àvvwxyyz{{xuþ */
    $"7407 7579 7C7F 7F7C 9FF4 F7FF 0AE6 6A54"            /* t.uy|..|ô÷ÿ.æjT */
    $"5D5F 6264 6667 696A 006B FE6C 186B 6968"            /* ]_bdfgij.kþl.kih */
    $"6665 625E 5955 514C 463F 3934 2E29 2421"            /* feb^YUQLF?94.)$! */
    $"1D1A 1814 0CAB 9EFF F0FF 0498 0008 0909"            /* .....«ÿðÿ...ÆÆ */
    $"FE0A FF0C 1A0D 0E0F 0F11 0C15 6FB2 B4B4"            /* þ.ÿ..Â......o²´´ */
    $"B7BA BEC0 9A76 7677 7879 797A 7C7D 7773"            /* ·º¾Àvvwxyyz|}ws */
    $"FE70 0772 787C 817F 7CA0 F4F7 FF0B E66A"            /* þp.rx|.| ô÷ÿ.æj */
    $"545D 5F62 6466 6769 6A6B FE6C 186B 6968"            /* T]_bdfgijkþl.kih */
    $"6665 625E 5955 514C 463F 3934 2E29 2421"            /* feb^YUQLF?94.)$! */
    $"1D1A 1814 0CAB F4FF 9AFF 0498 0008 0909"            /* .....«ôÿÿ...ÆÆ */
    $"FE0A FF0C 0E0D 0E0F 0F11 0C15 6FB2 B4B4"            /* þ.ÿ..Â......o²´´ */
    $"B7BA BEC0 0B9A 7676 7778 7979 7A7E 7E75"            /* ·º¾À.vvwxyyz~~u */
    $"6CFE 6707 6B74 7B83 817D A0F4 F7FF 0BE6"            /* lþg.kt{} ô÷ÿ.æ */
    $"6A54 5D5F 6264 6667 696A 6BFE 6C18 6B69"            /* jT]_bdfgijkþl.ki */
    $"6866 6562 5E59 5551 4C46 3F39 342E 2924"            /* hfeb^YUQLF?94.)$ */
    $"211D 1A18 140C ABCA FFFF FF01 17C6 FF01"            /* !.....«Êÿÿÿ..Æÿ. */
    $"5100 FD09 010A 0BFE 0DFF 0F12 100D 137C"            /* Q.ýÆ...þÂÿ...Â.| */
    $"B7B0 B2B6 B9BC C1AA 7B75 7677 7878 79FE"            /* ·°²¶¹¼Áª{uvwxxyþ */
    $"7A04 7B7C 7C7D 7DFE 7E03 7C7F A1E8 F5FF"            /* z.{||}}þ~.|.¡èõÿ */
    $"09C9 5A5B 5E61 6365 6668 6A00 6AFD 6B17"            /* ÆÉZ[^acefhj.jýk. */
    $"6968 6665 625F 5A55 524D 4841 3A35 302B"            /* ihfeb_ZURMHA:50+ */
    $"2621 1D1B 1916 056C 9EFF F0FF 0151 00FD"            /* &!.....lÿðÿ.Q.ý */
    $"0901 0A0B FE0D FF0F 1210 0D13 7CB7 B0B2"            /* Æ...þÂÿ...Â.|·°² */
    $"B6B9 BCC1 AB7B 7576 7778 7879 FE7A 0B7C"            /* ¶¹¼Á«{uvwxxyþz.| */
    $"7D7D 7E7E 7F7F 7E7D 7EA0 E8F5 FF0A C95A"            /* }}~~..~}~ èõÿ.ÉZ */
    $"5B5E 6163 6566 686A 6AFD 6B17 6968 6665"            /* [^acefhjjýk.ihfe */
    $"625F 5A55 524D 4841 3A35 302B 2621 1D1B"            /* b_ZURMHA:50+&!.. */
    $"1916 056C F4FF 9AFF 0151 00FD 0901 0A0B"            /* ...lôÿÿ.Q.ýÆ... */
    $"FE0D FF0F 0B10 0D13 7CB7 B0B2 B6B9 BCC1"            /* þÂÿ...Â.|·°²¶¹¼Á */
    $"AB06 7B75 7677 7878 79FE 7A02 7D7E 7FFD"            /* «.{uvwxxyþz.}~.ý */
    $"8004 7E7C 7EA1 E8F5 FF0A C95A 5B5E 6163"            /* .~|~¡èõÿ.ÉZ[^ac */
    $"6566 686A 6AFD 6B17 6968 6665 625F 5A55"            /* efhjjýk.ihfeb_ZU */
    $"524D 4841 3A35 302B 2621 1D1B 1916 056C"            /* RMHA:50+&!.....l */
    $"CAFF FFFF 0111 C7FF 02E3 1105 FE09 040A"            /* Êÿÿÿ..Çÿ.ã..þÆ.. */
    $"0B0C 0D0D FE0F 0F0E 0C6F B4AE B0B3 B7BA"            /* ..ÂÂþ....o´®°³·º */
    $"BFB9 8974 7676 77FE 78FE 7AFE 7BFC 7C02"            /* ¿¹tvvwþxþzþ{ü|. */
    $"80A2 E1F3 FF08 9952 5D60 6365 6668 6901"            /* ¢áóÿ.R]`cefhi. */
    $"696A FE6B 1869 6866 6562 5F5B 5652 4E49"            /* ijþk.ihfeb_[VRNI */
    $"423B 3531 2C27 221E 1A19 170B 4AFD 9FFF"            /* B;51,'".....Jýÿ */
    $"F1FF 02E3 1105 FE09 040A 0B0C 0D0D FE0F"            /* ñÿ.ã..þÆ....ÂÂþ. */
    $"0F0E 0C6F B4AE B0B3 B7BA BFB9 8874 7676"            /* ...o´®°³·º¿¹tvv */
    $"77FE 78FE 7AFE 7BFC 7C02 80A3 E1F3 FF0A"            /* wþxþzþ{ü|.£áóÿ. */
    $"9952 5D60 6365 6668 6969 6AFE 6B18 6968"            /* R]`cefhiijþk.ih */
    $"6665 625F 5B56 524E 4942 3B35 312C 2722"            /* feb_[VRNIB;51,'" */
    $"1E1A 1917 0B4A FDF5 FF9B FF02 E311 05FE"            /* .....Jýõÿÿ.ã..þ */
    $"0904 0A0B 0C0D 0DFE 0F0B 0E0C 6FB4 AEB0"            /* Æ....ÂÂþ....o´®° */
    $"B3B7 BABF B988 0374 7676 77FE 78FE 7AFE"            /* ³·º¿¹.tvvwþxþzþ */
    $"7BFE 7C04 7D7C 80A2 E1F3 FF0A 9952 5D60"            /* {þ|.}|¢áóÿ.R]` */
    $"6365 6668 6969 6AFE 6B18 6968 6665 625F"            /* cefhiijþk.ihfeb_ */
    $"5B56 524E 4942 3B35 312C 2722 1E1A 1917"            /* [VRNIB;51,'".... */
    $"0B4A FDCB FFFF FF01 15C7 FF02 BB07 06FE"            /* .JýËÿÿÿ..Çÿ.»..þ */
    $"0901 0B0C FE0D FF0F 1010 083F ADAE AFB2"            /* Æ...þÂÿ....?­®¯² */
    $"B5B8 BCBF 9D75 7576 7677 FE78 FD7A FE7B"            /* µ¸¼¿uuvvwþxýzþ{ */
    $"FF7C 047B 80A0 D8FC F3FF 08E9 6959 6062"            /* ÿ|.{ Øüóÿ.éiY`b */
    $"6466 6768 0169 6AFE 6B18 6968 6665 6260"            /* dfgh.ijþk.ihfeb` */
    $"5B57 534E 4A43 3D38 322D 2823 1F1B 1917"            /* [WSNJC=82-(#.... */
    $"1028 EF9F FFF1 FF02 BB07 06FE 0901 0B0C"            /* .(ïÿñÿ.»..þÆ... */
    $"FE0D FF0F 1010 083F ADAE AFB2 B5B8 BCBF"            /* þÂÿ....?­®¯²µ¸¼¿ */
    $"9D75 7576 7677 FE78 FD7A FE7B FF7C 047B"            /* uuvvwþxýzþ{ÿ|.{ */
    $"80A0 D8FC F3FF 0AE9 6959 6062 6466 6768"            /*  Øüóÿ.éiY`bdfgh */
    $"696A FE6B 1869 6866 6562 605B 5753 4E4A"            /* ijþk.ihfeb`[WSNJ */
    $"433D 3832 2D28 231F 1B19 1710 28EF F5FF"            /* C=82-(#.....(ïõÿ */
    $"9BFF 02BB 0706 FE09 010B 0CFE 0DFF 0F0C"            /* ÿ.»..þÆ...þÂÿ.. */
    $"1008 3FAD AEAF B2B5 B8BC BF9C 7503 7576"            /* ..?­®¯²µ¸¼¿u.uv */
    $"7677 FE78 FD7A FE7B FF7C 047B 809F D8FB"            /* vwþxýzþ{ÿ|.{Øû */
    $"F3FF 0AE9 6959 6062 6466 6768 696A FE6B"            /* óÿ.éiY`bdfghijþk */
    $"1869 6866 6562 605B 5753 4E4A 433D 3832"            /* .ihfeb`[WSNJC=82 */
    $"2D28 231F 1B19 1710 28EF CBFF FFFF 0111"            /* -(#.....(ïËÿÿÿ.. */
    $"C7FF 0890 0008 0909 0A0C 0C0D FE0E 0D0F"            /* Çÿ...ÆÆ...Âþ.Â. */
    $"0B20 96AF ADB1 B4B6 BAC0 AF7F 75FE 7602"            /* . ¯­±´¶ºÀ¯.uþv. */
    $"7778 78FE 79FF 7AFE 7B05 7C7D 7E9A CFF5"            /* wxxþyÿzþ{.|}~Ïõ */
    $"F1FF 07A5 545F 6163 6566 6800 69FD 6AFF"            /* ñÿ.¥T_acefh.iýjÿ */
    $"6816 6765 6260 5B58 544F 4A44 3D38 332E"            /* h.geb`[XTOJD=83. */
    $"2924 201D 1917 140B AB9F FFF1 FF08 9000"            /* )$ .....«ÿñÿ.. */
    $"0809 090A 0C0C 0DFE 0E0D 0F0B 2096 AFAD"            /* .ÆÆ...Âþ.Â.. ¯­ */
    $"B1B4 B6BA C0AF 7F75 FE76 0277 7878 FE79"            /* ±´¶ºÀ¯.uþv.wxxþy */
    $"FF7A FE7B 057C 7D7E 99CF F5F1 FF08 A554"            /* ÿzþ{.|}~Ïõñÿ.¥T */
    $"5F61 6365 6668 69FD 6AFF 6816 6765 6260"            /* _acefhiýjÿh.geb` */
    $"5B58 544F 4A44 3D38 332E 2924 201D 1917"            /* [XTOJD=83.)$ ... */
    $"140B ABF5 FF9B FF08 9000 0809 090A 0C0C"            /* ..«õÿÿ...ÆÆ... */
    $"0DFE 0E0D 0F0B 2096 AFAD B1B4 B6BA C0AF"            /* Âþ.Â.. ¯­±´¶ºÀ¯ */
    $"7E75 FE76 0277 7878 FE79 FF7A FE7B 057C"            /* ~uþv.wxxþyÿzþ{.| */
    $"7D7E 9ACF F5F1 FF08 A554 5F61 6365 6668"            /* }~Ïõñÿ.¥T_acefh */
    $"69FD 6AFF 6816 6765 6260 5B58 544F 4A44"            /* iýjÿh.geb`[XTOJD */
    $"3D38 332E 2924 201D 1917 140B ABCB FFFF"            /* =83.)$ .....«Ëÿÿ */
    $"FF01 12C8 FF19 FE42 0009 090A 0B0C 0C0D"            /* ÿ..Èÿ.þB.ÆÆ....Â */
    $"0E0E 0F0D 0E72 B1AD B0B3 B6B8 BCBA 9075"            /* ...Â.r±­°³¶¸¼ºu */
    $"FE76 FE77 0078 FE79 FE7A 077B 7C7C 8196"            /* þvþw.xþyþz.{|| */
    $"C5EF FEF1 FF07 EB69 5B61 6264 6668 0068"            /* Åïþñÿ.ëi[abdfh.h */
    $"FD69 1868 6766 6462 605C 5854 504C 453F"            /* ýi.hgfdb`\XTPLE? */
    $"3A34 2F2A 2521 1D1A 1816 066C 9FFF F2FF"            /* :4/*%!.....lÿòÿ */
    $"19FE 4200 0909 0A0B 0C0C 0D0E 0E0F 0D0E"            /* .þB.ÆÆ....Â...Â. */
    $"72B1 ADB0 B3B6 B8BC BA8F 74FE 76FE 7700"            /* r±­°³¶¸¼ºtþvþw. */
    $"78FE 79FE 7A07 7B7C 7C80 96C4 F0FE F1FF"            /* xþyþz.{||Äðþñÿ */
    $"08EB 695B 6162 6466 6868 FD69 1868 6766"            /* .ëi[abdfhhýi.hgf */
    $"6462 605C 5854 504C 453F 3A34 2F2A 2521"            /* db`\XTPLE?:4/*%! */
    $"1D1A 1816 066C F5FF 9CFF 1AFE 4200 0909"            /* .....lõÿÿ.þB.ÆÆ */
    $"0A0B 0C0C 0D0E 0E0F 0D0E 72B1 ADB0 B3B6"            /* ....Â...Â.r±­°³¶ */
    $"B8BC BA8F 7476 FF76 FE77 0078 FE79 FE7A"            /* ¸¼ºtvÿvþw.xþyþz */
    $"077B 7C7D 8095 C5EF FEF1 FF08 EB69 5B61"            /* .{|}Åïþñÿ.ëi[a */
    $"6264 6668 68FD 6918 6867 6664 6260 5C58"            /* bdfhhýi.hgfdb`\X */
    $"5450 4C45 3F3A 342F 2A25 211D 1A18 1606"            /* TPLE?:4/*%!..... */
    $"6CCB FFFF FF01 0FC8 FF05 D10B 0609 090B"            /* lËÿÿÿ..Èÿ.Ñ..ÆÆ. */
    $"FE0C 100D 0E0E 1008 50AF ACAE B1B3 B7BA"            /* þ..Â....P¯¬®±³·º */
    $"BD9E 7775 FE76 FE77 0078 FD79 FF7B 067D"            /* ½wuþvþw.xýyÿ{.} */
    $"7E83 9DCA ECFC EFFF 06A3 5760 6164 6566"            /* ~Êìüïÿ.£W`adef */
    $"0068 FD69 1968 6766 6463 605C 5955 514C"            /* .hýi.hgfdc`\YUQL */
    $"4740 3B36 312B 2622 1F1B 1916 0D3F F9A0"            /* G@;61+&"....Â?ù  */
    $"FFF2 FF05 D10B 0609 090B FE0C 100D 0E0E"            /* ÿòÿ.Ñ..ÆÆ.þ..Â.. */
    $"1008 50AF ACAE B1B3 B7BA BD9E 7875 FE76"            /* ..P¯¬®±³·º½xuþv */
    $"FE77 0078 FD79 FF7B 067D 7E83 9DCA EDFC"            /* þw.xýyÿ{.}~Êíü */
    $"EFFF 07A3 5760 6164 6566 68FD 6919 6867"            /* ïÿ.£W`adefhýi.hg */
    $"6664 6360 5C59 5551 4C47 403B 3631 2B26"            /* fdc`\YUQLG@;61+& */
    $"221F 1B19 160D 3FF9 F6FF 9CFF 05D1 0B06"            /* "....Â?ùöÿÿ.Ñ.. */
    $"0909 0BFE 0C11 0D0E 0E10 0850 AFAC AEB1"            /* ÆÆ.þ..Â....P¯¬®± */
    $"B3B7 BABD 9E77 7576 FF76 FE77 0078 FD79"            /* ³·º½wuvÿvþw.xýy */
    $"FF7B 067D 7E83 9DCA ECFC EFFF 07A3 5760"            /* ÿ{.}~Êìüïÿ.£W` */
    $"6164 6566 68FD 6919 6867 6664 6360 5C59"            /* adefhýi.hgfdc`\Y */
    $"5551 4C47 403B 3631 2B26 221F 1B19 160D"            /* UQLG@;61+&"....Â */
    $"3FF9 CCFF FFFF 0115 C8FF 1CA2 0007 090A"            /* ?ùÌÿÿÿ..Èÿ.¢..Æ. */
    $"0B0C 0D0D 0E0E 0F0A 249C ACAC B0B3 B5B8"            /* ..ÂÂ....$¬¬°³µ¸ */
    $"BCAE 8175 7676 7576 FE77 0078 FD79 087B"            /* ¼®uvvuvþw.xýy.{ */
    $"7E80 859C C8EB FAFE EFFF 06DC 615E 6163"            /* ~Èëúþïÿ.Üa^ac */
    $"6466 1E66 6768 6969 6767 6564 6260 5C59"            /* df.fghiiggedb`\Y */
    $"5651 4D48 413C 3732 2C27 231F 1C1A 1711"            /* VQMHA<72,'#..... */
    $"1CDC A0FF F2FF 1CA2 0007 090A 0B0C 0D0D"            /* .Ü ÿòÿ.¢..Æ...ÂÂ */
    $"0E0E 0F0A 249C ACAC B0B3 B5B8 BCAF 8175"            /* ....$¬¬°³µ¸¼¯u */
    $"7676 7576 FE77 0078 FD79 087B 7E80 859C"            /* vvuvþw.xýy.{~ */
    $"C8EA FAFE EFFF 25DC 615E 6163 6466 6667"            /* Èêúþïÿ%Üa^acdffg */
    $"6869 6967 6765 6462 605C 5956 514D 4841"            /* hiiggedb`\YVQMHA */
    $"3C37 322C 2723 1F1C 1A17 111C DCF6 FF9C"            /* <72,'#......Üöÿ */
    $"FF1A A200 0709 0A0B 0C0D 0D0E 0E0F 0A24"            /* ÿ.¢..Æ...ÂÂ....$ */
    $"9CAC ACB0 B3B5 B8BC AF81 7576 7601 7576"            /* ¬¬°³µ¸¼¯uvv.uv */
    $"FE77 0078 FD79 087B 7E80 859C C7EB F9FE"            /* þw.xýy.{~Çëùþ */
    $"EFFF 25DC 615E 6163 6466 6667 6869 6967"            /* ïÿ%Üa^acdffghiig */
    $"6765 6462 605C 5956 514D 4841 3C37 322C"            /* gedb`\YVQMHA<72, */
    $"2723 1F1C 1A17 111C DCCC FFFF FF01 0EC8"            /* '#......ÜÌÿÿÿ..È */
    $"FF16 7400 0809 0A0B 0C0D 0D0E 0F0E 0B6B"            /* ÿ.t..Æ...ÂÂ....k */
    $"ADA9 AEB1 B4B6 B9B9 97FD 7601 7576 FE77"            /* ­©®±´¶¹¹ýv.uvþw */
    $"FF78 FF7A 087B 7E82 899C C3E5 F6FC EEFF"            /* ÿxÿz.{~Ãåöüîÿ */
    $"06FD 8259 6162 6465 0166 67FD 6818 6765"            /* .ýYabde.fgýh.ge */
    $"6461 5F5D 5956 524E 4942 3D38 332E 2824"            /* da_]YVRNIB=83.($ */
    $"201C 1A18 1507 90A0 FFF2 FF16 7400 0809"            /*  ..... ÿòÿ.t..Æ */
    $"0A0B 0C0D 0D0E 0F0E 0B6B ADA9 AEB1 B4B6"            /* ...ÂÂ....k­©®±´¶ */
    $"B9B9 96FD 7601 7576 FE77 FF78 FF7A 087B"            /* ¹¹ýv.uvþwÿxÿz.{ */
    $"7E82 889C C2E5 F6FC EEFF 08FD 8259 6162"            /* ~Âåöüîÿ.ýYab */
    $"6465 6667 FD68 1867 6564 615F 5D59 5652"            /* defgýh.geda_]YVR */
    $"4E49 423D 3833 2E28 2420 1C1A 1815 0790"            /* NIB=83.($ ..... */
    $"F6FF 9CFF 1674 0008 090A 0B0C 0D0D 0E0F"            /* öÿÿ.t..Æ...ÂÂ.. */
    $"0E0B 6BAD A9AE B1B4 B6B9 B997 FD76 0175"            /* ..k­©®±´¶¹¹ýv.u */
    $"76FE 77FF 78FF 7A08 7B7E 8288 9CC2 E4F5"            /* vþwÿxÿz.{~Âäõ */
    $"FCEE FF08 FD82 5961 6264 6566 67FD 6818"            /* üîÿ.ýYabdefgýh. */
    $"6765 6461 5F5D 5956 524E 4942 3D38 332E"            /* geda_]YVRNIB=83. */
    $"2824 201C 1A18 1507 90CC FFFF FF01 12C9"            /* ($ .....Ìÿÿÿ..É */
    $"FF1D FE46 0009 090B 0B0C 0D0D 0E0F 0833"            /* ÿ.þF.ÆÆ...ÂÂ...3 */
    $"A5A9 ABAF B3B5 B7B6 A684 7777 7675 7576"            /* ¥©«¯³µ·¶¦wwvuuv */
    $"FE77 0C78 797A 7B7E 828A 9CBC DEF2 F9FD"            /* þw.xyz{~¼Þòùý */
    $"EDFF 059F 5561 6264 6501 6566 FD67 1866"            /* íÿ.Uabde.efýg.f */
    $"6563 615F 5D5A 5652 4E4A 433E 3934 2F29"            /* eca_]ZVRNJC>94/) */
    $"2522 1E1A 1816 085F A0FF F3FF 1DFE 4600"            /* %"....._ ÿóÿ.þF. */
    $"0909 0B0B 0C0D 0D0E 0F08 33A5 A9AB AFB3"            /* ÆÆ...ÂÂ...3¥©«¯³ */
    $"B5B7 B6A6 8477 7776 7575 76FE 770C 7879"            /* µ·¶¦wwvuuvþw.xy */
    $"7A7B 7E82 899C BCDD F1F9 FDED FF07 9F55"            /* z{~¼Ýñùýíÿ.U */
    $"6162 6465 6566 FD67 1866 6563 615F 5D5A"            /* abdeefýg.feca_]Z */
    $"5652 4E4A 433E 3934 2F29 2522 1E1A 1816"            /* VRNJC>94/)%".... */
    $"085F F6FF 9DFF 1BFE 4600 0909 0B0B 0C0D"            /* ._öÿÿ.þF.ÆÆ...Â */
    $"0D0E 0F08 33A5 A9AB AFB3 B5B7 B6A6 8477"            /* Â...3¥©«¯³µ·¶¦w */
    $"7776 7501 7576 FE77 0C78 797A 7C7E 8289"            /* wvu.uvþw.xyz|~ */
    $"9CBC DEF2 F9FD EDFF 079F 5561 6264 6565"            /* ¼Þòùýíÿ.Uabdee */
    $"66FD 6718 6665 6361 5F5D 5A56 524E 4A43"            /* fýg.feca_]ZVRNJC */
    $"3E39 342F 2925 221E 1A18 1608 5FCC FFFF"            /* >94/)%"....._Ìÿÿ */
    $"FF01 13C9 FF06 E417 0509 0B0B 0CFE 0D0E"            /* ÿ..Éÿ.ä..Æ...þÂ. */
    $"0E0C 0F7B ABA9 ACB0 B3B5 B5AB 907C 78FC"            /* ...{«©¬°³µµ«|xü */
    $"760F 7778 7879 7A7C 7F84 8B99 B6D5 EBF6"            /* v.wxxyz|.¶Õëö */
    $"FBFD EDFF 05B7 555F 6163 6401 6566 FE67"            /* ûýíÿ.·U_acd.efþg */
    $"FF66 1865 6361 5F5D 5A56 534F 4A43 3F3A"            /* ÿf.eca_]ZVSOJC?: */
    $"3530 2A26 221F 1B18 170E 34F6 A1FF F3FF"            /* 50*&".....4ö¡ÿóÿ */
    $"06E4 1705 090B 0B0C FE0D 0E0E 0C0F 7BAB"            /* .ä..Æ...þÂ....{« */
    $"A9AC B0B3 B5B5 AB90 7C78 FC76 0F77 7878"            /* ©¬°³µµ«|xüv.wxx */
    $"797A 7C7F 848B 98B6 D6EB F6FB FDED FF07"            /* yz|.¶Öëöûýíÿ. */
    $"B755 5F61 6364 6566 FE67 FF66 1865 6361"            /* ·U_acdefþgÿf.eca */
    $"5F5D 5A56 534F 4A43 3F3A 3530 2A26 221F"            /* _]ZVSOJC?:50*&". */
    $"1B18 170E 34F6 F7FF 9DFF 06E4 1705 090B"            /* ....4ö÷ÿÿ.ä..Æ. */
    $"0B0C FE0D 0E0E 0C0F 7BAB A9AC B0B3 B5B5"            /* ..þÂ....{«©¬°³µµ */
    $"AC90 7C78 FE76 FF76 0F77 7878 797A 7C7F"            /* ¬|xþvÿv.wxxyz|. */
    $"838B 98B6 D5EB F6FB FDED FF07 B755 5F61"            /* ¶Õëöûýíÿ.·U_a */
    $"6364 6566 FE67 FF66 1865 6361 5F5D 5A56"            /* cdefþgÿf.eca_]ZV */
    $"534F 4A43 3F3A 3530 2A26 221F 1B18 170E"            /* SOJC?:50*&"..... */
    $"34F6 CDFF FFFF 0115 C9FF 078A 0008 090B"            /* 4öÍÿÿÿ..Éÿ...Æ. */
    $"0B0C 0DFE 0E0D 0739 A7A7 AAAD B1B3 B4AE"            /* ..Âþ.Â.9§§ª­±³´® */
    $"9A84 7B78 FD76 1077 7878 797B 7E81 878F"            /* {xýv.wxxy{~ */
    $"9BB0 CFE5 F2F9 FCFE EDFF 05D5 5C5D 6062"            /* °Ïåòùüþíÿ.Õ\]`b */
    $"631F 6466 6566 6766 6664 6361 5F5D 5A57"            /* c.dfefgffdca_]ZW */
    $"534F 4A44 403B 3631 2B27 2420 1D19 1713"            /* SOJD@;61+'$ .... */
    $"11BA A1FF F3FF 078A 0008 090B 0B0C 0DFE"            /* .º¡ÿóÿ...Æ...Âþ */
    $"0E0D 0739 A7A7 AAAD B1B3 B4AE 9A85 7B78"            /* .Â.9§§ª­±³´®{x */
    $"FD76 1077 7878 797B 7E81 878F 9CB0 CFE5"            /* ýv.wxxy{~°Ïå */
    $"F2F9 FCFE EDFF 25D5 5C5D 6062 6364 6665"            /* òùüþíÿ%Õ\]`bcdfe */
    $"6667 6666 6463 615F 5D5A 5753 4F4A 4440"            /* fgffdca_]ZWSOJD@ */
    $"3B36 312B 2724 201D 1917 1311 BAF7 FF9D"            /* ;61+'$ .....º÷ÿ */
    $"FF07 8A00 0809 0B0B 0C0D FE0E 0D07 39A7"            /* ÿ...Æ...Âþ.Â.9§ */
    $"A7AA ADB1 B3B4 AE9A 847B 78FE 7611 7677"            /* §ª­±³´®{xþv.vw */
    $"7878 797B 7E81 878F 9CB0 CEE5 F2F9 FCFE"            /* xxy{~°Îåòùüþ */
    $"EDFF 25D5 5C5D 6062 6364 6665 6667 6666"            /* íÿ%Õ\]`bcdfefgff */
    $"6463 615F 5D5A 5753 4F4A 4440 3B36 312B"            /* dca_]ZWSOJD@;61+ */
    $"2724 201D 1917 1311 BACD FFFF FF01 15C9"            /* '$ .....ºÍÿÿÿ..É */
    $"FF07 4800 0909 0B0C 0D0D FE0E 2105 5DAD"            /* ÿ.H.ÆÆ..ÂÂþ.!.]­ */
    $"A7AA AEB1 B2AF A18C 807B 7877 7676 7778"            /* §ª®±²¯¡{xwvvwx */
    $"797A 7C7E 8389 939F B1C7 DFED F6FB FDEC"            /* yz|~±Çßíöûýì */
    $"FF05 F16A 5B60 6162 0064 FE65 FF66 1965"            /* ÿ.ñj[`ab.dþeÿf.e */
    $"6463 615F 5D5A 5753 504B 4540 3C37 322D"            /* dca_]ZWSPKE@<72- */
    $"2925 211D 1917 1504 6FA1 FFF3 FF07 4800"            /* )%!.....o¡ÿóÿ.H. */
    $"0909 0B0C 0D0D FE0E 2105 5DAD A7AA AEB1"            /* ÆÆ..ÂÂþ.!.]­§ª®± */
    $"B2B0 A18C 7F7B 7877 7676 7778 797A 7C7E"            /* ²°¡.{xwvvwxyz|~ */
    $"8389 93A0 B1C8 E0ED F6FB FDEC FF06 F16A"            /*  ±Èàíöûýìÿ.ñj */
    $"5B60 6162 64FE 65FF 6619 6564 6361 5F5D"            /* [`abdþeÿf.edca_] */
    $"5A57 5350 4B45 403C 3732 2D29 2521 1D19"            /* ZWSPKE@<72-)%!.. */
    $"1715 046F F7FF 9DFF 0748 0009 090B 0C0D"            /* ...o÷ÿÿ.H.ÆÆ..Â */
    $"0DFE 0E10 055D ADA7 AAAD B1B2 AFA0 8C80"            /* Âþ...]­§ª­±²¯  */
    $"7B78 7776 7610 7778 797A 7C7E 8389 93A0"            /* {xwvv.wxyz|~  */
    $"B1C7 DFED F6FB FDEC FF06 F16A 5B60 6162"            /* ±Çßíöûýìÿ.ñj[`ab */
    $"64FE 65FF 6619 6564 6361 5F5D 5A57 5350"            /* dþeÿf.edca_]ZWSP */
    $"4B45 403C 3732 2D29 2521 1D19 1715 046F"            /* KE@<72-)%!.....o */
    $"CDFF FFFF 0115 CAFF 07E3 1804 0A0A 0C0C"            /* Íÿÿÿ..Êÿ.ã...... */
    $"0DFE 0E22 0D11 82A9 A8AC AFB0 B0A6 9585"            /* Âþ."Â.©¨¬¯°°¦ */
    $"7E7B 7877 7778 797A 7C7D 8084 8B95 A1B1"            /* ~{xwwxyz|}¡± */
    $"C4D7 E8F1 F8FC FEEB FF04 9956 5E60 6201"            /* Ä×èñøüþëÿ.V^`b. */
    $"6364 FD65 1A64 6362 615F 5D5A 5754 504B"            /* cdýe.dcba_]ZWTPK */
    $"4642 3D38 342F 2B27 221E 1B19 160B 44FB"            /* FB=84/+'".....Dû */
    $"A2FF F4FF 07E3 1804 0A0A 0C0C 0DFE 0E22"            /* ¢ÿôÿ.ã......Âþ." */
    $"0D11 82A9 A8AC AFB0 B0A6 9485 7E7B 7877"            /* Â.©¨¬¯°°¦~{xw */
    $"7778 797A 7C7D 8084 8B95 A1B1 C4D8 E8F2"            /* wxyz|}¡±ÄØèò */
    $"F8FC FEEB FF06 9956 5E60 6263 64FD 651A"            /* øüþëÿ.V^`bcdýe. */
    $"6463 6261 5F5D 5A57 5450 4B46 423D 3834"            /* dcba_]ZWTPKFB=84 */
    $"2F2B 2722 1E1B 1916 0B44 FBF8 FF9E FF07"            /* /+'".....Dûøÿÿ. */
    $"E318 040A 0A0C 0C0D FE0E 110D 1182 A9A8"            /* ã......Âþ..Â.©¨ */
    $"ACAF B0AF A694 857E 7B78 7777 7810 797A"            /* ¬¯°¯¦~{xwwx.yz */
    $"7C7D 8084 8C95 A1B1 C4D7 E8F2 F8FC FEEB"            /* |}¡±Ä×èòøüþë */
    $"FF06 9956 5E60 6263 64FD 651A 6463 6261"            /* ÿ.V^`bcdýe.dcba */
    $"5F5D 5A57 5450 4B46 423D 3834 2F2B 2722"            /* _]ZWTPKFB=84/+'" */
    $"1E1B 1916 0B44 FBCE FFFF FF01 12CA FF07"            /* .....DûÎÿÿÿ..Êÿ. */
    $"9100 080A 0A0C 0C0D FE0E 2209 40A4 A5A9"            /* ......Âþ."Æ@¤¥© */
    $"ACAE AFAA 9D8D 837E 7B78 7879 7A7C 7D7F"            /* ¬®¯ª~{xxyz|}. */
    $"8287 8C96 A3B2 C2D3 E2ED F5FA FDFE EBFF"            /* £²ÂÓâíõúýþëÿ */
    $"04B9 555D 6062 0162 63FC 6419 6362 605F"            /* .¹U]`b.bcüd.cb`_ */
    $"5D5A 5754 504C 4742 3D38 3531 2C28 231F"            /* ]ZWTPLGB=851,(#. */
    $"1B19 1711 21E8 A2FF F4FF 0791 0008 0A0A"            /* ....!è¢ÿôÿ..... */
    $"0C0C 0DFE 0E22 0940 A4A5 A9AC AEAF AA9C"            /* ..Âþ."Æ@¤¥©¬®¯ª */
    $"8C83 7E7B 7878 797A 7C7D 7F82 878C 96A3"            /* ~{xxyz|}.£ */
    $"B2C2 D3E2 EEF5 FAFD FEEB FF06 B955 5D60"            /* ²ÂÓâîõúýþëÿ.¹U]` */
    $"6262 63FC 6419 6362 605F 5D5A 5754 504C"            /* bbcüd.cb`_]ZWTPL */
    $"4742 3D38 3531 2C28 231F 1B19 1711 21E8"            /* GB=851,(#.....!è */
    $"F8FF 9EFF 0791 0008 0A0A 0C0C 0DFE 0E11"            /* øÿÿ.......Âþ.. */
    $"0940 A4A5 A9AC AEAF AA9D 8C83 7E7B 7878"            /* Æ@¤¥©¬®¯ª~{xx */
    $"797A 107C 7D7F 8287 8C96 A3B2 C3D4 E2EE"            /* yz.|}.£²ÃÔâî */
    $"F5FA FDFE EBFF 06B9 555D 6062 6263 FC64"            /* õúýþëÿ.¹U]`bbcüd */
    $"1963 6260 5F5D 5A57 5450 4C47 423D 3835"            /* .cb`_]ZWTPLGB=85 */
    $"312C 2823 1F1B 1917 1121 E8CE FFFF FF01"            /* 1,(#.....!èÎÿÿÿ. */
    $"15CA FF2D 4E00 090A 0A0C 0C0D 0E0E 0F0E"            /* .Êÿ-N.Æ....Â.... */
    $"74A8 A5A9 ACAD ACA2 9488 817D 7B7A 7B7B"            /* t¨¥©¬­¬¢}{z{{ */
    $"7D7F 8185 8990 98A3 B2C1 D1DE E8F1 F6FA"            /* }.£²ÁÑÞèñöú */
    $"FDFE EBFF 04CA 5A5C 5F61 FF62 0063 FD64"            /* ýþëÿ.ÊZ\_aÿb.cýd */
    $"1963 6260 5F5D 5A57 5450 4C47 433E 3A36"            /* .cb`_]ZWTPLGC>:6 */
    $"322C 2824 201C 1A17 1412 BCA2 FFF4 FF2D"            /* 2,($ .....¼¢ÿôÿ- */
    $"4E00 090A 0A0C 0C0D 0E0E 0F0E 74A8 A5A9"            /* N.Æ....Â....t¨¥© */
    $"ACAD ACA3 9488 827E 7B7A 7B7B 7D7F 8185"            /* ¬­¬£~{z{{}. */
    $"8990 98A3 B2C1 D1DE E8F1 F6FA FDFE EBFF"            /* £²ÁÑÞèñöúýþëÿ */
    $"07CA 5A5C 5F61 6262 63FD 6419 6362 605F"            /* .ÊZ\_abbcýd.cb`_ */
    $"5D5A 5754 504C 4743 3E3A 3632 2C28 2420"            /* ]ZWTPLGC>:62,($  */
    $"1C1A 1714 12BC F8FF 9EFF 1C4E 0009 0A0A"            /* .....¼øÿÿ.N.Æ.. */
    $"0C0C 0D0E 0E0F 0E74 A8A5 A9AC ADAC A294"            /* ..Â....t¨¥©¬­¬¢ */
    $"8882 7E7B 7A7B 7B7D 107F 8185 8A90 98A3"            /* ~{z{{}..£ */
    $"B3C1 D1DE E8F2 F7FA FDFE EBFF 07CA 5A5C"            /* ³ÁÑÞèò÷úýþëÿ.ÊZ\ */
    $"5F61 6262 63FD 6419 6362 605F 5D5A 5754"            /* _abbcýd.cb`_]ZWT */
    $"504C 4743 3E3A 3632 2C28 2420 1C1A 1714"            /* PLGC>:62,($ .... */
    $"12BC CEFF FFFF 0118 CBFF 2DDD 1504 090A"            /* .¼Îÿÿÿ..Ëÿ-Ý..Æ. */
    $"0B0D 0D0E 0E0F 0C30 9AA3 A6AA ACAC A79A"            /* .ÂÂ....0£¦ª¬¬§ */
    $"8E86 827E 7E7D 7D7F 8184 898D 939C A5B2"            /* ~~}}.¥² */
    $"C2D0 DCE6 EDF4 F8FB FEEA FF04 D65E 5C5E"            /* ÂÐÜæíôøûþêÿ.Ö^\^ */
    $"6020 6062 6363 6464 6362 6160 5F5D 5A58"            /* ` `bccddcba`_]ZX */
    $"5552 4D49 4540 3C38 322D 2925 211D 1A18"            /* URMIE@<82-)%!... */
    $"1607 83A2 FFF5 FF2D DD15 0409 0A0B 0D0D"            /* ..¢ÿõÿ-Ý..Æ..ÂÂ */
    $"0E0E 0F0C 309A A3A6 AAAC ACA7 9A8E 8682"            /* ....0£¦ª¬¬§ */
    $"7E7E 7D7E 8081 8489 8D93 9CA5 B2C1 D0DC"            /* ~~}~¥²ÁÐÜ */
    $"E6ED F4F8 FBFE EAFF 25D6 5E5C 5E60 6062"            /* æíôøûþêÿ%Ö^\^``b */
    $"6363 6464 6362 6160 5F5D 5A58 5552 4D49"            /* ccddcba`_]ZXURMI */
    $"4540 3C38 322D 2925 211D 1A18 1607 83F8"            /* E@<82-)%!.....ø */
    $"FF9F FF1D DD15 0409 0A0B 0D0D 0E0E 0F0C"            /* ÿÿ.Ý..Æ..ÂÂ.... */
    $"309A A3A6 AAAC ACA7 9A8E 8682 7E7E 7D7E"            /* 0£¦ª¬¬§~~}~ */
    $"8081 0F84 898D 939C A5B3 C2D0 DCE6 EEF4"            /* .¥³ÂÐÜæîô */
    $"F8FB FEEA FF25 D65E 5C5E 6060 6263 6364"            /* øûþêÿ%Ö^\^``bccd */
    $"6463 6261 605F 5D5A 5855 524D 4945 403C"            /* dcba`_]ZXURMIE@< */
    $"3832 2D29 2521 1D1A 1816 0783 CEFF FFFF"            /* 82-)%!.....Îÿÿÿ */
    $"0115 CBFF 2D82 0009 0A0B 0B0D 0D0E 0F0E"            /* ..Ëÿ-.Æ...ÂÂ... */
    $"0C68 A6A2 A7AA ABA9 A194 8C87 8381 8081"            /* .h¦¢§ª«©¡ */
    $"8284 878C 9197 9FA7 B1BF CCD8 E2EA F0F5"            /* §±¿ÌØâêðõ */
    $"F9FC FEEA FF04 E664 5A5E 5F01 6062 FC63"            /* ùüþêÿ.ædZ^_.`büc */
    $"1A62 6160 5F5D 5A58 5552 4E49 4540 3C37"            /* .ba`_]ZXURNIE@<7 */
    $"322E 2925 221E 1B19 170E 32F6 A3FF F5FF"            /* 2.)%".....2ö£ÿõÿ */
    $"1782 0009 0A0B 0B0D 0D0E 0F0E 0C68 A6A2"            /* ..Æ...ÂÂ....h¦¢ */
    $"A7AA ABA9 A195 8C87 83FE 8112 8384 878C"            /* §ª«©¡þ. */
    $"9197 9FA7 B1BE CCD8 E2EA F0F5 F9FC FEEA"            /* §±¾ÌØâêðõùüþê */
    $"FF06 E664 5A5E 5F60 62FC 631A 6261 605F"            /* ÿ.ædZ^_`büc.ba`_ */
    $"5D5A 5855 524E 4945 403C 3732 2E29 2522"            /* ]ZXURNIE@<72.)%" */
    $"1E1B 1917 0E32 F6F9 FF9F FF17 8200 090A"            /* .....2öùÿÿ..Æ. */
    $"0B0B 0D0D 0E0F 0E0C 68A6 A2A7 AAAB A9A2"            /* ..ÂÂ....h¦¢§ª«©¢ */
    $"958C 8783 FE81 0283 8487 0F8C 9197 9FA8"            /* þ..¨ */
    $"B2BF CDD9 E2EA F0F5 F9FC FEEA FF06 E664"            /* ²¿ÍÙâêðõùüþêÿ.æd */
    $"5A5E 5F60 62FC 631A 6261 605F 5D5A 5855"            /* Z^_`büc.ba`_]ZXU */
    $"524E 4945 403C 3732 2E29 2522 1E1B 1917"            /* RNIE@<72.)%".... */
    $"0E32 F6CF FFFF FF01 1ECC FF2E FD40 0009"            /* .2öÏÿÿÿ..Ìÿ.ý@.Æ */
    $"0A0B 0C0D 0D0E 0F0E 1687 A2A3 A7AA A9A6"            /* ...ÂÂ....¢£§ª©¦ */
    $"9D93 8D88 8785 8586 888B 8F94 9AA1 AAB3"            /* ¡ª³ */
    $"BDC9 D5DE E6EC F2F6 FAFC FEEA FF04 EE68"            /* ½ÉÕÞæìòöúüþêÿ.îh */
    $"595D 5F02 6061 62FE 63FF 6219 6160 5E5C"            /* Y]_.`abþcÿb.a`^\ */
    $"5A58 5552 4E4A 4641 3D38 332E 2A26 221E"            /* ZXURNJFA=83.*&". */
    $"1B19 1713 13CA A3FF F6FF 2EFD 4000 090A"            /* .....Ê£ÿöÿ.ý@.Æ. */
    $"0B0C 0D0D 0E0F 0E16 87A2 A3A7 AAA9 A69C"            /* ..ÂÂ....¢£§ª©¦ */
    $"938D 8887 8585 8688 8C90 949A A1AA B3BD"            /* ¡ª³½ */
    $"C9D5 DEE6 ECF2 F6FA FCFE EAFF 07EE 6859"            /* ÉÕÞæìòöúüþêÿ.îhY */
    $"5D5F 6061 62FE 63FF 6219 6160 5E5C 5A58"            /* ]_`abþcÿb.a`^\ZX */
    $"5552 4E4A 4641 3D38 332E 2A26 221E 1B19"            /* URNJFA=83.*&"... */
    $"1713 13CA F9FF A0FF 1EFD 4000 090A 0B0C"            /* ...Êùÿ ÿ.ý@.Æ... */
    $"0D0D 0E0F 0E16 87A2 A3A7 AAA9 A69D 938D"            /* ÂÂ....¢£§ª©¦ */
    $"8887 8585 8688 8C8F 0F95 9BA1 AAB3 BDC9"            /* .¡ª³½É */
    $"D5DE E6EC F2F6 FAFC FEEA FF07 EE68 595D"            /* ÕÞæìòöúüþêÿ.îhY] */
    $"5F60 6162 FE63 FF62 1961 605E 5C5A 5855"            /* _`abþcÿb.a`^\ZXU */
    $"524E 4A46 413D 3833 2E2A 2622 1E1B 1917"            /* RNJFA=83.*&".... */
    $"1313 CACF FFFF FF01 1ECC FF05 D411 0509"            /* ..ÊÏÿÿÿ..Ìÿ.Ô..Æ */
    $"0A0B FE0D FF0E 230B 3E9E A1A5 A9AA A9A3"            /* ..þÂÿ.#.>¡¥©ª©£ */
    $"9A93 8F8C 8A8A 8B8D 9094 989D A4AC B5BE"            /* ¤¬µ¾ */
    $"C7D2 DBE3 EAEE F3F7 FAFC FEEA FF04 F775"            /* ÇÒÛãêîó÷úüþêÿ.÷u */
    $"585D 5F21 6061 6262 6363 6262 615F 5E5D"            /* X]_!`abbccbba_^] */
    $"5A58 5552 4F4B 4742 3E39 342F 2B27 231F"            /* ZXUROKGB>94/+'#. */
    $"1C1A 1715 099E A3FF F6FF 05D4 1105 090A"            /* ....Æ£ÿöÿ.Ô..Æ. */
    $"0BFE 0DFF 0E23 0B3E 9EA1 A5A9 AAA8 A39A"            /* .þÂÿ.#.>¡¥©ª¨£ */
    $"938F 8C8A 8A8B 8D90 9498 9EA4 ACB5 BEC7"            /* ¤¬µ¾Ç */
    $"D2DB E3EA EEF3 F7FA FCFE EAFF 26F7 7558"            /* ÒÛãêîó÷úüþêÿ&÷uX */
    $"5D5F 6061 6262 6363 6262 615F 5E5D 5A58"            /* ]_`abbccbba_^]ZX */
    $"5552 4F4B 4742 3E39 342F 2B27 231F 1C1A"            /* UROKGB>94/+'#... */
    $"1715 099E F9FF A0FF 05D4 1105 090A 0BFE"            /* ..Æùÿ ÿ.Ô..Æ..þ */
    $"0DFF 0E13 0B3E 9EA1 A5A9 AAA9 A39A 938F"            /* Âÿ...>¡¥©ª©£ */
    $"8C8A 8A8B 8D90 9498 0F9E A4AC B5BE C7D2"            /* .¤¬µ¾ÇÒ */
    $"DBE3 EAEE F3F7 FAFC FEEA FF26 F775 585D"            /* Ûãêîó÷úüþêÿ&÷uX] */
    $"5F60 6162 6263 6362 6261 5F5E 5D5A 5855"            /* _`abbccbba_^]ZXU */
    $"524F 4B47 423E 3934 2F2B 2723 1F1C 1A17"            /* ROKGB>94/+'#.... */
    $"1509 9ECF FFFF FF01 18CC FF06 7A00 080A"            /* .ÆÏÿÿÿ..Ìÿ.z... */
    $"0B0C 0CFE 0E24 0F0C 65A5 A1A6 A9AA A7A1"            /* ...þ.$..e¥¡¦©ª§¡ */
    $"9B95 9290 9091 9396 999D A1A8 AEB6 BEC7"            /* ¡¨®¶¾Ç */
    $"CFD9 E0E6 EBF0 F4F8 FBFD FEEA FF04 FE83"            /* ÏÙàæëðôøûýþêÿ.þ */
    $"555D 5E01 5F61 FC62 1A61 605F 5E5C 5A58"            /* U]^._aüb.a`_^\ZX */
    $"5653 4F4B 4742 3E39 3430 2C28 2320 1E1B"            /* VSOKGB>940,(# .. */
    $"1817 0959 A3FF F6FF 067A 0008 0A0B 0C0C"            /* ..ÆY£ÿöÿ.z...... */
    $"FE0E 240F 0C65 A5A1 A6A9 AAA8 A19A 9592"            /* þ.$..e¥¡¦©ª¨¡ */
    $"9090 9193 9699 9DA1 A8AE B6BE C7CF D9E0"            /* ¡¨®¶¾ÇÏÙà */
    $"E6EB F0F4 F8FB FDFE EAFF 06FE 8355 5D5E"            /* æëðôøûýþêÿ.þU]^ */
    $"5F61 FC62 1A61 605F 5E5C 5A58 5653 4F4B"            /* _aüb.a`_^\ZXVSOK */
    $"4742 3E39 3430 2C28 2320 1E1B 1817 0959"            /* GB>940,(# ....ÆY */
    $"F9FF A0FF 067A 0008 0A0B 0C0C FE0E 140F"            /* ùÿ ÿ.z......þ... */
    $"0C65 A5A1 A6A9 AAA7 A19A 9592 9090 9193"            /* .e¥¡¦©ª§¡ */
    $"9699 9DA1 0FA8 AEB6 BEC6 CFD9 E0E7 EBF0"            /* ¡.¨®¶¾ÆÏÙàçëð */
    $"F4F8 FBFD FEEA FF06 FE83 555D 5E5F 61FC"            /* ôøûýþêÿ.þU]^_aü */
    $"621A 6160 5F5E 5C5A 5856 534F 4B47 423E"            /* b.a`_^\ZXVSOKGB> */
    $"3934 302C 2823 201E 1B18 1709 59CF FFFF"            /* 940,(# ....ÆYÏÿÿ */
    $"FF01 21CD FF2E FA36 000A 0A0B 0C0C 0E0E"            /* ÿ.!Íÿ.ú6........ */
    $"0F0D 1C86 A3A3 A7AA AAA7 A29E 9A98 9798"            /* .Â.££§ªª§¢ */
    $"999D A0A3 A7AD B3B9 C1C8 CED6 DEE4 E9ED"            /*  £§­³¹ÁÈÎÖÞäéí */
    $"F1F4 F8FC FEE9 FF04 FA75 555D 5E03 5F60"            /* ñôøüþéÿ.úuU]^._` */
    $"6161 FE62 1B61 605F 5E5C 5A58 5653 504C"            /* aaþb.a`_^\ZXVSPL */
    $"4844 3F3B 3631 2D29 2420 1D1B 1817 1119"            /* HD?;61-)$ ...... */
    $"DAA4 FFF7 FF2E FA36 000A 0A0B 0C0C 0E0E"            /* Ú¤ÿ÷ÿ.ú6........ */
    $"0F0D 1C86 A3A3 A7AA AAA8 A29E 9A98 9798"            /* .Â.££§ªª¨¢ */
    $"999D A0A3 A7AD B3B9 C1C8 CED6 DEE5 E9ED"            /*  £§­³¹ÁÈÎÖÞåéí */
    $"F1F4 F8FC FEE9 FF08 FA75 555D 5E5F 6061"            /* ñôøüþéÿ.úuU]^_`a */
    $"61FE 621B 6160 5F5E 5C5A 5856 5350 4C48"            /* aþb.a`_^\ZXVSPLH */
    $"443F 3B36 312D 2924 201D 1B18 1711 19DA"            /* D?;61-)$ ......Ú */
    $"FAFF A1FF 1FFA 3600 0A0A 0B0C 0C0E 0E0F"            /* úÿ¡ÿ.ú6......... */
    $"0D1C 86A3 A3A7 AAAA A7A2 9E9A 9897 9899"            /* Â.££§ªª§¢ */
    $"9DA0 A3A7 AD0E B3B9 C1C8 CED6 DEE4 E9ED"            /*  £§­.³¹ÁÈÎÖÞäéí */
    $"F1F5 F9FC FEE9 FF08 FA75 555D 5E5F 6061"            /* ñõùüþéÿ.úuU]^_`a */
    $"61FE 621B 6160 5F5E 5C5A 5856 5350 4C48"            /* aþb.a`_^\ZXVSPLH */
    $"443F 3B36 312D 2924 201D 1B18 1711 19DA"            /* D?;61-)$ ......Ú */
    $"D0FF FFFF 0121 CDFF 06D3 0C06 090B 0C0D"            /* Ðÿÿÿ.!Íÿ.Ó..Æ..Â */
    $"FE0E 0B0F 0A4C A3A1 A4A9 ACAB A9A5 A1FE"            /* þ....L£¡¤©¬«©¥¡þ */
    $"A015 A1A3 A7AA AEB2 B7BC C2C9 D0D6 DCE2"            /*  .¡£§ª®²·¼ÂÉÐÖÜâ */
    $"E8EC EFF2 F6FA FCFE E9FF 04F3 6658 5D5E"            /* èìïòöúüþéÿ.ófX]^ */
    $"035F 6061 61FE 621B 6160 5F5E 5D5A 5856"            /* ._`aaþb.a`_^]ZXV */
    $"5350 4D49 4440 3B37 312E 2A26 221F 1C19"            /* SPMID@;71.*&"... */
    $"1814 0BA7 A4FF F7FF 06D3 0C06 090B 0C0D"            /* ...§¤ÿ÷ÿ.Ó..Æ..Â */
    $"FE0E 0B0F 0A4C A3A1 A4A9 ACAC A9A5 A1FE"            /* þ....L£¡¤©¬¬©¥¡þ */
    $"A015 A1A3 A7AA AEB2 B7BD C3C9 D0D6 DCE2"            /*  .¡£§ª®²·½ÃÉÐÖÜâ */
    $"E8EC EFF2 F6FA FCFE E9FF 08F3 6658 5D5E"            /* èìïòöúüþéÿ.ófX]^ */
    $"5F60 6161 FE62 1B61 605F 5E5D 5A58 5653"            /* _`aaþb.a`_^]ZXVS */
    $"504D 4944 403B 3731 2E2A 2622 1F1C 1918"            /* PMID@;71.*&".... */
    $"140B A7FA FFA1 FF06 D30C 0609 0B0C 0DFE"            /* ..§úÿ¡ÿ.Ó..Æ..Âþ */
    $"0E0B 0F0A 4CA3 A1A4 A9AC ABA9 A4A1 FEA0"            /* ....L£¡¤©¬«©¤¡þ  */
    $"06A1 A3A7 AAAE B2B7 0EBD C3C9 D0D6 DCE2"            /* .¡£§ª®²·.½ÃÉÐÖÜâ */
    $"E8EC EFF2 F6FA FCFE E9FF 08F3 6658 5D5E"            /* èìïòöúüþéÿ.ófX]^ */
    $"5F60 6161 FE62 1B61 605F 5E5D 5A58 5653"            /* _`aaþb.a`_^]ZXVS */
    $"504D 4944 403B 3731 2E2A 2622 1F1C 1918"            /* PMID@;71.*&".... */
    $"140B A7D0 FFFF FF01 1BCD FF06 9600 080A"            /* ..§Ðÿÿÿ..Íÿ.... */
    $"0B0C 0DFC 0E08 75A5 A2A6 ABAD ADAC A9FE"            /* ..Âü..u¥¢¦«­­¬©þ */
    $"A716 A8A9 ABAF B3B6 BBC0 C4CA D0D5 DBE0"            /* §.¨©«¯³¶»ÀÄÊÐÕÛà */
    $"E5EA EDF0 F3F6 F9FC FEE9 FF04 F063 585D"            /* åêíðóöùüþéÿ.ðcX] */
    $"5E01 5E60 FE61 1D62 6161 605F 5E5C 5B58"            /* ^.^`þa.baa`_^\[X */
    $"5653 504D 4945 403C 3733 2E2A 2622 201C"            /* VSPMIE@<73.*&" . */
    $"1A18 1707 6CA4 FFF7 FF06 9600 080A 0B0C"            /* ....l¤ÿ÷ÿ...... */
    $"0DFC 0E08 75A5 A2A6 ABAD ADAC A9FE A716"            /* Âü..u¥¢¦«­­¬©þ§. */
    $"A8A9 ABAF B3B6 BBC0 C4CA D0D5 DBE0 E5EA"            /* ¨©«¯³¶»ÀÄÊÐÕÛàåê */
    $"EDF0 F3F6 F9FC FEE9 FF06 F063 585D 5E5E"            /* íðóöùüþéÿ.ðcX]^^ */
    $"60FE 611D 6261 6160 5F5E 5C5B 5856 5350"            /* `þa.baa`_^\[XVSP */
    $"4D49 4540 3C37 332E 2A26 2220 1C1A 1817"            /* MIE@<73.*&" .... */
    $"076C FAFF A1FF 0696 0008 0A0B 0C0D FC0E"            /* .lúÿ¡ÿ......Âü. */
    $"1375 A5A2 A6AB ADAD ACA9 A7A6 A7A8 A9AB"            /* .u¥¢¦«­­¬©§¦§¨©« */
    $"AFB3 B6BB C00E C4CA D0D5 DBE0 E5EA EDF0"            /* ¯³¶»À.ÄÊÐÕÛàåêíð */
    $"F3F6 F9FC FEE9 FF06 F063 585D 5E5E 60FE"            /* óöùüþéÿ.ðcX]^^`þ */
    $"611D 6261 6160 5F5E 5C5B 5856 5350 4D49"            /* a.baa`_^\[XVSPMI */
    $"4540 3C37 332E 2A26 2220 1C1A 1817 076C"            /* E@<73.*&" .....l */
    $"D0FF FFFF 011A CEFF 14F9 3A00 0A0B 0B0C"            /* Ðÿÿÿ..Îÿ.ù:..... */
    $"0D0D 0F0F 0B24 96A3 A3A8 ACAF B0B0 FDAE"            /* ÂÂ...$££¨¬¯°°ý® */
    $"15AF B1B3 B7BA BEC2 C7CB D0D5 DBDF E4E8"            /* .¯±³·º¾ÂÇËÐÕÛßäè */
    $"EBEE F1F3 F6FA FDE8 FF04 EE62 585C 5D01"            /* ëîñóöúýèÿ.îbX\]. */
    $"5E60 FB61 1B60 5F5E 5C5B 5957 5451 4E4A"            /* ^`ûa.`_^\[YWTQNJ */
    $"4642 3E39 3430 2C28 2320 1D1B 1816 1122"            /* FB>940,(# ....." */
    $"E8A5 FFF8 FF2E F93A 000A 0B0B 0C0D 0D0F"            /* è¥ÿøÿ.ù:.....ÂÂ. */
    $"0F0B 2496 A3A3 A8AC AFB0 B0AE ADAD AEAF"            /* ..$££¨¬¯°°®­­®¯ */
    $"B1B3 B7BA BEC2 C7CB D0D6 DBDF E4E8 EBEE"            /* ±³·º¾ÂÇËÐÖÛßäèëî */
    $"F1F3 F6FA FDE8 FF06 EE62 585C 5D5E 60FB"            /* ñóöúýèÿ.îbX\]^`û */
    $"611B 605F 5E5C 5B59 5754 514E 4A46 423E"            /* a.`_^\[YWTQNJFB> */
    $"3934 302C 2823 201D 1B18 1611 22E8 FBFF"            /* 940,(# ....."èûÿ */
    $"A2FF 15F9 3A00 0A0B 0B0C 0D0D 0F0F 0B24"            /* ¢ÿ.ù:.....ÂÂ...$ */
    $"96A3 A3A8 ACAF B0B0 AEFE AD07 B0B1 B3B7"            /* ££¨¬¯°°®þ­.°±³· */
    $"BABE C2C7 0DCB D0D6 DBDF E4E8 EBEE F1F3"            /* º¾ÂÇÂËÐÖÛßäèëîñó */
    $"F6FA FDE8 FF06 EE62 585C 5D5E 60FB 611B"            /* öúýèÿ.îbX\]^`ûa. */
    $"605F 5E5C 5B59 5754 514E 4A46 423E 3934"            /* `_^\[YWTQNJFB>94 */
    $"302C 2823 201D 1B18 1611 22E8 D1FF FFFF"            /* 0,(# ....."èÑÿÿÿ */
    $"011C CEFF 13C3 0707 0A0B 0B0C 0D0D 0F0F"            /* ..Îÿ.Ã......ÂÂ.. */
    $"085A A8A3 A6AA AEB1 B2FD B316 B5B6 B8BA"            /* .Z¨£¦ª®±²ý³.µ¶¸º */
    $"BEC2 C5C9 CDD1 D6DA DFE3 E6EA EDEF F1F3"            /* ¾ÂÅÉÍÑÖÚßãæêíïñó */
    $"F7FB FDE8 FF04 E65F 585C 5D00 5EFE 60FD"            /* ÷ûýèÿ.æ_X\].^þ`ý */
    $"611B 605F 5E5C 5B59 5754 524E 4B48 4440"            /* a.`_^\[YWTRNKHD@ */
    $"3C37 332F 2B26 2320 1C19 1714 10BB A5FF"            /* <73/+&# .....»¥ÿ */
    $"F8FF 13C3 0707 0A0B 0B0C 0D0D 0F0F 085A"            /* øÿ.Ã......ÂÂ...Z */
    $"A8A3 A6AA AEB1 B2FD B316 B5B6 B8BA BEC2"            /* ¨£¦ª®±²ý³.µ¶¸º¾Â */
    $"C5C9 CDD1 D6DA DFE3 E6EA EDEF F1F3 F7FB"            /* ÅÉÍÑÖÚßãæêíïñó÷û */
    $"FDE8 FF05 E65F 585C 5D5E FE60 FD61 1B60"            /* ýèÿ.æ_X\]^þ`ýa.` */
    $"5F5E 5C5B 5957 5452 4E4B 4844 403B 3733"            /* _^\[YWTRNKHD@;73 */
    $"2F2B 2623 201C 1917 1410 BBFB FFA2 FF20"            /* /+&# .....»ûÿ¢ÿ  */
    $"C307 070A 0B0B 0C0D 0D0F 0F08 5AA8 A3A6"            /* Ã......ÂÂ...Z¨£¦ */
    $"AAAE B1B2 B3B2 B3B4 B5B6 B8BA BEC2 C5C9"            /* ª®±²³²³´µ¶¸º¾ÂÅÉ */
    $"CD0D D1D6 DADF E3E6 EAED EFF1 F3F7 FBFD"            /* ÍÂÑÖÚßãæêíïñó÷ûý */
    $"E8FF 05E6 5F58 5C5D 5EFE 60FD 611B 605F"            /* èÿ.æ_X\]^þ`ýa.`_ */
    $"5E5C 5B59 5754 524E 4C48 4441 3C37 332F"            /* ^\[YWTRNLHDA<73/ */
    $"2B26 2320 1C19 1714 10BB D1FF FFFF 011E"            /* +&# .....»Ñÿÿÿ.. */
    $"CEFF 067C 0009 0B0C 0C0D FD0E 2310 7BA8"            /* Îÿ.|.Æ...Âý.#.{¨ */
    $"A5A8 ACB1 B3B5 B6B6 B8B9 BABC BFC1 C4C7"            /* ¥¨¬±³µ¶¶¸¹º¼¿ÁÄÇ */
    $"CBCE D2D5 D9DE E2E5 E8EB EDEF F2F5 F8FB"            /* ËÎÒÕÙÞâåèëíïòõøû */
    $"FDE8 FF04 E25D 585D 5D03 5E5F 6060 FD61"            /* ýèÿ.â]X]].^_``ýa */
    $"1B60 5F5E 5D5B 5957 5452 4E4C 4845 413D"            /* .`_^][YWTRNLHEA= */
    $"3935 312D 2925 231F 1C19 1708 87A5 FFF8"            /* 951-)%#.....¥ÿø */
    $"FF06 7C00 090B 0C0C 0DFD 0E23 107B A8A5"            /* ÿ.|.Æ...Âý.#.{¨¥ */
    $"A8AC B1B3 B5B6 B6B8 B9BA BCBF C2C4 C7CB"            /* ¨¬±³µ¶¶¸¹º¼¿ÂÄÇË */
    $"CED2 D6D9 DEE2 E5E8 EBED EFF2 F5F8 FBFD"            /* ÎÒÖÙÞâåèëíïòõøûý */
    $"E8FF 08E2 5D58 5D5D 5E5F 6060 FD61 1B60"            /* èÿ.â]X]]^_``ýa.` */
    $"5F5E 5D5B 5957 5452 4E4C 4845 413D 3935"            /* _^][YWTRNLHEA=95 */
    $"312D 2925 231F 1C19 1708 87FB FFA2 FF06"            /* 1-)%#.....ûÿ¢ÿ. */
    $"7C00 090B 0C0C 0DFD 0E15 107B A8A5 A8AC"            /* |.Æ...Âý...{¨¥¨¬ */
    $"B1B3 B5B6 B6B8 B9BA BCBF C1C4 C7CB CED2"            /* ±³µ¶¶¸¹º¼¿ÁÄÇËÎÒ */
    $"0DD6 D9DE E2E5 E8EB EDEF F2F5 F8FB FDE8"            /* ÂÖÙÞâåèëíïòõøûýè */
    $"FF08 E25D 585D 5D5E 5F60 60FD 611B 605F"            /* ÿ.â]X]]^_``ýa.`_ */
    $"5E5D 5B59 5754 524E 4C48 4541 3D39 3531"            /* ^][YWTRNLHEA=951 */
    $"2D29 2523 1F1C 1917 0887 D1FF FFFF 0127"            /* -)%#.....Ñÿÿÿ.' */
    $"CFFF 04E2 1903 090B FE0C 270D 0E0E 0C1D"            /* Ïÿ.â..Æ.þ.'Â.... */
    $"97A7 A8AB AEB2 B6B7 B9BB BDBE C0C1 C4C6"            /* §¨«®²¶·¹»½¾ÀÁÄÆ */
    $"CACD D0D3 D6D9 DDE1 E4E7 E9EC EEEF F2F5"            /* ÊÍÐÓÖÙÝáäçéìîïòõ */
    $"F8FB FDE8 FF04 DE5C 585C 5D03 5E5F 6060"            /* øûýèÿ.Þ\X\].^_`` */
    $"FD61 1C60 5F5E 5C5A 5856 5451 4E4B 4845"            /* ýa.`_^\ZXVTQNKHE */
    $"413D 3935 322E 2A27 2422 1F1B 1910 31F3"            /* A=952.*'$"....1ó */
    $"A6FF F9FF 04E2 1903 090B FE0C 270D 0E0E"            /* ¦ÿùÿ.â..Æ.þ.'Â.. */
    $"0C1D 97A7 A8AB AEB2 B6B7 B9BB BDBE C0C1"            /* ..§¨«®²¶·¹»½¾ÀÁ */
    $"C4C6 CACD D0D3 D6DA DEE1 E4E7 E9EC EEEF"            /* ÄÆÊÍÐÓÖÚÞáäçéìîï */
    $"F2F5 F8FB FDE8 FF08 DE5C 585C 5D5E 5F60"            /* òõøûýèÿ.Þ\X\]^_` */
    $"60FD 611C 605F 5E5C 5A58 5654 514E 4B48"            /* `ýa.`_^\ZXVTQNKH */
    $"4541 3D39 3532 2E2A 2724 221F 1B18 1031"            /* EA=952.*'$"....1 */
    $"F3FC FFA3 FF04 E219 0309 0BFE 0C19 0D0E"            /* óüÿ£ÿ.â..Æ.þ..Â. */
    $"0E0C 1D97 A7A8 ABAE B2B6 B7B9 BBBD BEBF"            /* ...§¨«®²¶·¹»½¾¿ */
    $"C1C4 C6CA CDD0 D3D6 0DDA DEE1 E4E7 E9EC"            /* ÁÄÆÊÍÐÓÖÂÚÞáäçéì */
    $"EEEF F2F5 F8FB FDE8 FF08 DE5C 585C 5D5E"            /* îïòõøûýèÿ.Þ\X\]^ */
    $"5F60 60FD 611C 605F 5E5C 5A58 5654 514E"            /* _``ýa.`_^\ZXVTQN */
    $"4B48 4541 3D39 3532 2E2A 2724 221F 1B18"            /* KHEA=952.*'$"... */
    $"1031 F3D2 FFFF FF01 2ACF FF2F A400 080B"            /* .1óÒÿÿÿ.*Ïÿ/¤... */
    $"0B0C 0D0D 0B0F 0F09 34A3 A8A9 ADB1 B4B7"            /* ..ÂÂ...Æ4£¨©­±´· */
    $"B9BB BDBF C2C3 C6C8 CACD D0D3 D5D9 DCDF"            /* ¹»½¿ÂÃÆÈÊÍÐÓÕÙÜß */
    $"E1E5 E8EA EDEF F0F2 F5F8 FCFE E8FF 04DB"            /* áåèêíïðòõøüþèÿ.Û */
    $"5C59 5C5D 035E 5F60 60FE 611D 605F 5E5C"            /* \Y\].^_``þa.`_^\ */
    $"5A58 5653 524F 4C4A 4744 403C 3935 322F"            /* ZXVSROLJGD@<952/ */
    $"2B28 2624 221D 1A16 13C4 A6FF F9FF 2FA4"            /* +(&$"....Ä¦ÿùÿ/¤ */
    $"0008 0B0B 0C0D 0D0B 0F0F 0934 A3A8 A9AD"            /* .....ÂÂ...Æ4£¨©­ */
    $"B1B4 B7B9 BBBD BFC2 C3C6 C8CA CDD0 D3D5"            /* ±´·¹»½¿ÂÃÆÈÊÍÐÓÕ */
    $"D9DC DFE1 E5E8 EAED EFF0 F2F5 F8FC FEE8"            /* ÙÜßáåèêíïðòõøüþè */
    $"FF08 DB5C 595C 5D5E 5F60 60FE 611D 605F"            /* ÿ.Û\Y\]^_``þa.`_ */
    $"5E5D 5A58 5653 514F 4C4A 4744 403C 3935"            /* ^]ZXVSQOLJGD@<95 */
    $"322F 2B28 2624 211D 1A16 13C4 FCFF A3FF"            /* 2/+(&$!....Äüÿ£ÿ */
    $"21A4 0008 0B0B 0C0D 0D0B 0F0F 0934 A3A8"            /* !¤.....ÂÂ...Æ4£¨ */
    $"A9AD B1B4 B7B9 BBBD BFC2 C3C6 C8CA CDD0"            /* ©­±´·¹»½¿ÂÃÆÈÊÍÐ */
    $"D3D5 D90D DCDF E1E5 E8EA EDEF F0F2 F5F8"            /* ÓÕÙÂÜßáåèêíïðòõø */
    $"FCFE E8FF 08DB 5C59 5C5D 5E5F 6060 FE61"            /* üþèÿ.Û\Y\]^_``þa */
    $"1D60 5F5E 5D5A 5856 5352 4F4C 4A47 4440"            /* .`_^]ZXVSROLJGD@ */
    $"3C39 3532 2E2B 2826 2421 1D1A 1613 C4D2"            /* <952.+(&$!....ÄÒ */
    $"FFFF FF01 2ACF FF2F 4B00 0B0D 0D0E 0F10"            /* ÿÿÿ.*Ïÿ/K..ÂÂ... */
    $"0E0F 1007 4FAC A9AB AEB2 B6B8 BBBC BFC2"            /* ....O¬©«®²¶¸»¼¿Â */
    $"C4C6 C8CB CDD0 D2D5 D8DA DDE0 E3E6 E8EB"            /* ÄÆÈËÍÐÒÕØÚÝàãæèë */
    $"EDEE F0F3 F6F9 FCFD E8FF 04D9 5B59 5B5D"            /* íîðóöùüýèÿ.Ù[Y[] */
    $"035E 5F60 60FE 611D 605E 5C5B 5956 5451"            /* .^_``þa.`^\[YVTQ */
    $"504D 4B49 4644 403C 3936 332F 2B28 2624"            /* PMKIFD@<963/+(&$ */
    $"221F 1C18 0895 A6FF F9FF 2F4B 000B 0D0D"            /* "....¦ÿùÿ/K..ÂÂ */
    $"0E0F 100E 0F10 074F ACA9 ABAE B2B6 B8BB"            /* .......O¬©«®²¶¸» */
    $"BCBF C2C4 C6C8 CBCD D0D2 D5D8 DADD E0E3"            /* ¼¿ÂÄÆÈËÍÐÒÕØÚÝàã */
    $"E6E8 EBED EEF0 F3F6 F9FC FDE8 FF08 D95B"            /* æèëíîðóöùüýèÿ.Ù[ */
    $"595B 5D5E 5F60 60FE 611D 605E 5C5B 5856"            /* Y[]^_``þa.`^\[XV */
    $"5352 504D 4B49 4644 403C 3936 332F 2B28"            /* SRPMKIFD@<963/+( */
    $"2624 221F 1C18 0895 FCFF A3FF 214B 000B"            /* &$"....üÿ£ÿ!K.. */
    $"0D0D 0E0F 100F 0F10 074F ACA9 ABAE B2B6"            /* ÂÂ.......O¬©«®²¶ */
    $"B8BB BCBF C2C4 C6C8 CBCD D0D2 D5D8 DA0D"            /* ¸»¼¿ÂÄÆÈËÍÐÒÕØÚÂ */
    $"DDE0 E3E6 E8EB EDEE F0F3 F6F9 FCFD E8FF"            /* Ýàãæèëíîðóöùüýèÿ */
    $"08D9 5B59 5B5D 5E5F 6060 FE61 1D60 5E5C"            /* .Ù[Y[]^_``þa.`^\ */
    $"5B59 5654 5150 4D4B 4946 4440 3C39 3633"            /* [YVTQPMKIFD@<963 */
    $"2F2B 2826 2422 1F1C 1808 95D2 FFFF FF01"            /* /+(&$"....Òÿÿÿ. */
    $"2DD0 FF03 CD0A 080C FE0E FF10 FE0E 240F"            /* -Ðÿ.Í...þ.ÿ.þ.$. */
    $"7CAD A9AD B1B3 B7B9 BCBF C1C3 C5C8 CACC"            /* |­©­±³·¹¼¿ÁÃÅÈÊÌ */
    $"CFD1 D3D6 D9DB DEE2 E4E7 E9EB EEF0 F1F3"            /* ÏÑÓÖÙÛÞâäçéëîðñó */
    $"F6FA FDFE E8FF 04D7 5B59 5B5D 035E 5F60"            /* öúýþèÿ.×[Y[].^_` */
    $"60FE 611E 5F5D 5A58 5654 5250 4E4C 4947"            /* `þa._]ZXVTRPNLIG */
    $"4542 403C 3936 3330 2C28 2624 211F 1C19"            /* EB@<9630,(&$!... */
    $"0C4C FEA7 FFFA FF03 CD0A 080C FE0E FF10"            /* .Lþ§ÿúÿ.Í...þ.ÿ. */
    $"FE0E 240F 7CAD A9AD B1B3 B7B9 BCBF C1C3"            /* þ.$.|­©­±³·¹¼¿ÁÃ */
    $"C5C8 CACC CFD1 D3D6 D9DB DEE2 E4E7 E9EB"            /* ÅÈÊÌÏÑÓÖÙÛÞâäçéë */
    $"EEF0 F1F3 F6FA FDFE E8FF 08D7 5B59 5B5D"            /* îðñóöúýþèÿ.×[Y[] */
    $"5E5F 6060 FE61 1E5F 5D5A 5856 5452 504E"            /* ^_``þa._]ZXVTRPN */
    $"4C49 4745 4240 3C39 3633 302C 2825 2321"            /* LIGEB@<9630,(%#! */
    $"1F1C 190C 4CFE FDFF A4FF 03CD 0A08 0CFE"            /* ....Lþýÿ¤ÿ.Í...þ */
    $"0EFF 10FE 0E16 0F7C ADA9 ADB1 B3B7 B9BC"            /* .ÿ.þ...|­©­±³·¹¼ */
    $"BFC1 C3C5 C8CA CCCF D1D3 D6D9 DB0D DEE2"            /* ¿ÁÃÅÈÊÌÏÑÓÖÙÛÂÞâ */
    $"E4E7 E9EB EEF0 F1F3 F6FA FDFE E8FF 08D7"            /* äçéëîðñóöúýþèÿ.× */
    $"5B59 5B5D 5E5F 6060 FE61 1E5F 5D5A 5957"            /* [Y[]^_``þa._]ZYW */
    $"5452 504E 4C4A 4745 4240 3C39 3633 302C"            /* TRPNLJGEB@<9630, */
    $"2826 2421 1F1C 190C 4CFE D3FF FFFF 0130"            /* (&$!....LþÓÿÿÿ.0 */
    $"D0FF 306C 020C 0D0E 0E0F 1211 0E0F 0B27"            /* Ðÿ0l..Â........' */
    $"A1AB ADAF B2B5 B8BB BEC1 C3C5 C8CA CBCD"            /* ¡«­¯²µ¸»¾ÁÃÅÈÊËÍ */
    $"D0D3 D5D7 DADC DFE3 E5E8 E9EC EEEF F1F4"            /* ÐÓÕ×ÚÜßãåèéìîïñô */
    $"F7FA FDFE E8FF 04D4 5A59 5B5D 035E 5F60"            /* ÷úýþèÿ.ÔZY[].^_` */
    $"60FE 611E 5F5B 5856 5351 4F4D 4B4A 4846"            /* `þa._[XVSQOMKJHF */
    $"4442 3F3C 3936 3431 2D29 2623 201E 1B1A"            /* DB?<9641-)&# ... */
    $"1619 D1A7 FFFA FF30 6C02 0C0D 0E0E 0F12"            /* ..Ñ§ÿúÿ0l..Â.... */
    $"110E 0F0B 27A1 ABAD AFB2 B5B8 BBBE C1C3"            /* ....'¡«­¯²µ¸»¾ÁÃ */
    $"C5C8 CACB CDD0 D3D5 D7DA DCDF E3E5 E8E9"            /* ÅÈÊËÍÐÓÕ×ÚÜßãåèé */
    $"ECEE EFF1 F4F7 FAFD FEE8 FF08 D45A 595B"            /* ìîïñô÷úýþèÿ.ÔZY[ */
    $"5D5E 5F60 60FE 611E 5F5B 5856 5351 4F4D"            /* ]^_``þa._[XVSQOM */
    $"4C4A 4846 4442 3F3C 3936 3431 2D29 2523"            /* LJHFDB?<9641-)%# */
    $"201E 1B1A 1619 D1FD FFA4 FF22 6C02 0C0D"            /*  .....Ñýÿ¤ÿ"l..Â */
    $"0E0E 0F12 110E 0F0B 27A1 ABAD AFB2 B5B8"            /* ........'¡«­¯²µ¸ */
    $"BBBE C1C3 C5C8 CACB CDD0 D3D5 D7DA DC0D"            /* »¾ÁÃÅÈÊËÍÐÓÕ×ÚÜÂ */
    $"DFE3 E5E8 E9EC EEEF F1F4 F7FA FDFE E8FF"            /* ßãåèéìîïñô÷úýþèÿ */
    $"08D4 5A59 5B5D 5E5F 6060 FE61 1E5F 5B58"            /* .ÔZY[]^_``þa._[X */
    $"5653 514F 4D4C 4A49 4644 423F 3C39 3634"            /* VSQOMLJIFDB?<964 */
    $"312D 2926 2320 1E1B 1A16 18D1 D3FF FFFF"            /* 1-)&# .....ÑÓÿÿÿ */
    $"0133 D1FF 31A6 030A 0D0D 0E0F 1217 100F"            /* .3Ñÿ1¦..ÂÂ...... */
    $"0F07 45AC ACAE B1B3 B5B9 BCBF C2C4 C6C9"            /* ..E¬¬®±³µ¹¼¿ÂÄÆÉ */
    $"CBCD D0D1 D4D7 D9DB DEE0 E3E5 E8EA ECED"            /* ËÍÐÑÔ×ÙÛÞàãåèêìí */
    $"EFF1 F4F7 FAFD FEE8 FF04 D65A 595B 5D03"            /* ïñô÷úýþèÿ.ÖZY[]. */
    $"5E5F 6060 FE61 1E60 5954 5350 4E4C 4A49"            /* ^_``þa.`YTSPNLJI */
    $"4746 4644 423F 3C3A 3734 312D 2B27 2421"            /* GFFDB?<:741-+'$! */
    $"1E1B 1B19 0A7B A7FF FBFF 31A6 030A 0D0D"            /* .....{§ÿûÿ1¦..ÂÂ */
    $"0E0F 1217 100F 0F07 45AC ACAE B1B3 B5B9"            /* ........E¬¬®±³µ¹ */
    $"BCBF C2C4 C6C9 CBCD D0D1 D4D7 D9DB DEE0"            /* ¼¿ÂÄÆÉËÍÐÑÔ×ÙÛÞà */
    $"E3E5 E8EA ECED EFF1 F4F7 FAFD FEE8 FF08"            /* ãåèêìíïñô÷úýþèÿ. */
    $"D65A 595B 5D5E 5F60 60FE 611E 6059 5454"            /* ÖZY[]^_``þa.`YTT */
    $"504E 4C4A 4947 4646 4442 3F3C 3A37 3431"            /* PNLJIGFFDB?<:741 */
    $"2D2B 2824 211E 1B1B 190A 7BFD FFA5 FF23"            /* -+($!.....{ýÿ¥ÿ# */
    $"A603 0A0D 0D0E 0F12 1711 0F0F 0745 ACAC"            /* ¦..ÂÂ........E¬¬ */
    $"AEB1 B3B5 B9BC BFC2 C4C6 C9CB CDD0 D1D4"            /* ®±³µ¹¼¿ÂÄÆÉËÍÐÑÔ */
    $"D7D9 DBDE 0DE0 E3E5 E8EA ECED EFF1 F4F7"            /* ×ÙÛÞÂàãåèêìíïñô÷ */
    $"FAFD FEE8 FF08 D65A 595B 5D5E 5F60 60FE"            /* úýþèÿ.ÖZY[]^_``þ */
    $"611E 6059 5454 504E 4C4A 4947 4646 4442"            /* a.`YTTPNLJIGFFDB */
    $"3F3C 3A37 3431 2D2B 2724 211E 1B1B 190A"            /* ?<:741-+'$!..... */
    $"7BD3 FFFF FF01 33D2 FF31 D918 060D 0E0E"            /* {Óÿÿÿ.3Òÿ1Ù..Â.. */
    $"0F10 1917 0D0F 0F0A 6BB0 ACAF B2B4 B7BA"            /* ....Â...k°¬¯²´·º */
    $"BDBF C2C4 C6C9 CCCE D0D2 D5D8 D9DC DEE1"            /* ½¿ÂÄÆÉÌÎÐÒÕØÙÜÞá */
    $"E4E6 E9EB EDED F0F2 F4F7 FAFE E7FF 04DD"            /* äæéëííðòô÷úþçÿ.Ý */
    $"5C58 5C5D 035E 5F60 60FD 611E 594A 5050"            /* \X\].^_``ýa.YJPP */
    $"4D4B 4A48 4746 4545 4340 3D3B 3835 322E"            /* MKJHGFEEC@=;852. */
    $"2C29 2624 201E 1C1A 1422 D0A8 FFFC FF31"            /* ,)&$ ...."Ð¨ÿüÿ1 */
    $"D918 060D 0E0E 0F10 1917 0E0F 0F0A 6AB0"            /* Ù..Â..........j° */
    $"ACAF B2B4 B7BA BDBF C2C4 C6C9 CCCE D0D2"            /* ¬¯²´·º½¿ÂÄÆÉÌÎÐÒ */
    $"D5D8 D9DC DEE1 E4E6 E9EB EDED F0F2 F4F7"            /* ÕØÙÜÞáäæéëííðòô÷ */
    $"FAFE E7FF 08DD 5C58 5C5D 5E5F 6060 FD61"            /* úþçÿ.Ý\X\]^_``ýa */
    $"1E58 4A51 504D 4B4A 4847 4645 4543 403D"            /* .XJQPMKJHGFEEC@= */
    $"3B38 3532 2E2C 2926 2420 1E1C 1A14 22D0"            /* ;852.,)&$ ...."Ð */
    $"FEFF A6FF 24D9 1806 0D0E 0E0F 1019 170E"            /* þÿ¦ÿ$Ù..Â....... */
    $"0F0F 0A6B B0AC AFB2 B4B7 BABD BFC2 C4C6"            /* ...k°¬¯²´·º½¿ÂÄÆ */
    $"C9CC CED0 D2D5 D8D9 DCDE 0CE1 E4E6 E9EB"            /* ÉÌÎÐÒÕØÙÜÞ.áäæéë */
    $"EDED F0F2 F4F7 FAFE E7FF 08DD 5C58 5C5D"            /* ííðòô÷úþçÿ.Ý\X\] */
    $"5E5F 6060 FD61 1E58 4A51 504D 4B4A 4847"            /* ^_``ýa.XJQPMKJHG */
    $"4645 4543 403D 3B38 3532 2E2C 2926 2420"            /* FEEC@=;852.,)&$  */
    $"1E1C 1A14 22D0 D4FF FFFF 0133 D2FF 3167"            /* ...."ÐÔÿÿÿ.3Òÿ1g */
    $"000D 0E0E 0F0F 1721 110E 0F0D 1B97 ADAD"            /* .Â.....!...Â.­­ */
    $"B0B3 B5B8 BBBD BFC2 C4C6 C9CC CED0 D2D5"            /* °³µ¸»½¿ÂÄÆÉÌÎÐÒÕ */
    $"D8D9 DCDE E1E4 E6E9 EBED EDF0 F2F5 F8FB"            /* ØÙÜÞáäæéëííðòõøû */
    $"FEE7 FF04 E25E 585C 5D03 5E5F 6060 FD61"            /* þçÿ.â^X\].^_``ýa */
    $"1E60 4441 544F 4C4A 4847 4645 4544 423F"            /* .`DATOLJHGFEEDB? */
    $"3C39 3633 312D 2A28 2521 201D 1B1A 0A52"            /* <9631-*(%! ....R */
    $"A8FF FCFF 3167 000D 0E0E 0F0F 1722 110E"            /* ¨ÿüÿ1g.Â.....".. */
    $"0F0D 1B97 ADAD B0B3 B5B8 BBBD BFC2 C4C6"            /* .Â.­­°³µ¸»½¿ÂÄÆ */
    $"C9CC CED0 D2D5 D8D9 DCDE E1E4 E6E9 EBED"            /* ÉÌÎÐÒÕØÙÜÞáäæéëí */
    $"EDF0 F2F5 F8FB FEE7 FF08 E25E 585C 5D5E"            /* íðòõøûþçÿ.â^X\]^ */
    $"5F60 60FD 611E 5F43 4153 4F4C 4A48 4746"            /* _``ýa._CASOLJHGF */
    $"4545 4442 3F3C 3936 3331 2D2A 2825 2120"            /* EEDB?<9631-*(%!  */
    $"1D1B 1A0A 52FE FFA6 FF24 6700 0D0E 0E0F"            /* ....Rþÿ¦ÿ$g.Â... */
    $"0F17 2211 0E0F 0D1B 97AD ADB0 B3B5 B8BB"            /* .."...Â.­­°³µ¸» */
    $"BDBF C2C4 C6C9 CCCE D0D2 D5D8 D9DC DE0C"            /* ½¿ÂÄÆÉÌÎÐÒÕØÙÜÞ. */
    $"E1E4 E6E9 EBED EDF0 F2F5 F8FB FEE7 FF08"            /* áäæéëííðòõøûþçÿ. */
    $"E25E 585C 5D5E 5F60 60FD 611E 5F43 4053"            /* â^X\]^_``ýa._C@S */
    $"4F4C 4A48 4746 4545 4442 3F3C 3936 3331"            /* OLJHGFEEDB?<9631 */
    $"2D2A 2825 2120 1D1B 1A0A 52D4 FFFF FF01"            /* -*(%! ....RÔÿÿÿ. */
    $"39D3 FF03 B30C 090D FE0E 2B14 2619 0D0F"            /* 9Óÿ.³.ÆÂþ.+.&.Â. */
    $"0F09 39A9 ABAF B2B4 B7BA BCBF C1C3 C4C8"            /* .Æ9©«¯²´·º¼¿ÁÃÄÈ */
    $"CACC CED0 D3D6 D8D9 DCDE E2E5 E7EA ECEE"            /* ÊÌÎÐÓÖØÙÜÞâåçêìî */
    $"EEF1 F3F6 F9FB FEE7 FF04 EC63 585B 5D03"            /* îñóöùûþçÿ.ìcX[]. */
    $"5E5F 6060 FD61 1F63 552B 4A53 4E4B 4947"            /* ^_``ýa.cU+JSNKIG */
    $"4646 4544 4340 3E3B 3836 3230 2D2A 2624"            /* FFEDC@>;8620-*&$ */
    $"211F 1C1A 180D 97A9 FFFD FF03 B30C 090D"            /* !....Â©ÿýÿ.³.ÆÂ */
    $"FE0E 2B13 2618 0D0F 0F09 39A9 ABAF B2B4"            /* þ.+.&.Â..Æ9©«¯²´ */
    $"B7BA BCBF C1C3 C4C8 CACC CED0 D3D6 D8D9"            /* ·º¼¿ÁÃÄÈÊÌÎÐÓÖØÙ */
    $"DCDE E2E5 E7EA ECEE EEF1 F3F6 F9FB FEE7"            /* ÜÞâåçêìîîñóöùûþç */
    $"FF08 EC63 585B 5D5E 5F60 60FD 6121 6356"            /* ÿ.ìcX[]^_``ýa!cV */
    $"2B4B 534E 4B49 4746 4645 4443 403E 3B38"            /* +KSNKIGFFEDC@>;8 */
    $"3632 302D 2A26 2421 1F1C 1A18 0D97 FFFF"            /* 620-*&$!....Âÿÿ */
    $"A7FF 03B3 0C09 0DFE 0E1E 1426 190D 0F0F"            /* §ÿ.³.ÆÂþ...&.Â.. */
    $"0939 A9AB AFB2 B4B7 BABC BFC1 C3C4 C8CA"            /* Æ9©«¯²´·º¼¿ÁÃÄÈÊ */
    $"CCCE D0D3 D6D8 D9DC DE0C E2E5 E7EA ECEE"            /* ÌÎÐÓÖØÙÜÞ.âåçêìî */
    $"EEF1 F3F6 F9FB FEE7 FF08 EC63 585B 5D5E"            /* îñóöùûþçÿ.ìcX[]^ */
    $"5F60 60FD 611F 6356 2B4C 534E 4B49 4746"            /* _``ýa.cV+LSNKIGF */
    $"4645 4443 403E 3B38 3632 302D 2A26 2421"            /* FEDC@>;8620-*&$! */
    $"1F1C 1A18 0D97 D5FF FFFF 013B D4FF 33E5"            /* ....ÂÕÿÿÿ.;Ôÿ3å */
    $"2902 0C0D 0E0F 1123 1E0D 0E0F 0F07 5BAF"            /* )..Â...#.Â....[¯ */
    $"ABAF B1B5 B7B9 BCBF C2C3 C6C8 CBCD CFD2"            /* «¯±µ·¹¼¿ÂÃÆÈËÍÏÒ */
    $"D3D6 D9DB DDDF E2E5 E7EA ECEE EEF1 F3F6"            /* ÓÖÙÛÝßâåçêìîîñóö */
    $"F9FB FEE7 FF04 F469 575B 5D03 5E5F 6060"            /* ùûþçÿ.ôiW[].^_`` */
    $"FC61 1F65 3F2C 5252 4D4B 4947 4645 4444"            /* üa.e?,RRMKIGFEDD */
    $"423F 3C3B 3834 322F 2B29 2623 201E 1C1A"            /* B?<;842/+)&# ... */
    $"1129 DEAA FFFE FF33 E529 020C 0D0E 0F11"            /* .)Þªÿþÿ3å)..Â... */
    $"241E 0E0E 0F0F 075B AFAB AFB1 B5B7 B9BC"            /* $......[¯«¯±µ·¹¼ */
    $"BFC2 C3C6 C8CB CDCF D2D3 D6D9 DBDD DFE2"            /* ¿ÂÃÆÈËÍÏÒÓÖÙÛÝßâ */
    $"E5E7 EAEC EEEE F1F3 F6F9 FBFE E7FF 08F4"            /* åçêìîîñóöùûþçÿ.ô */
    $"6957 5B5D 5E5F 6060 FC61 2064 3F2C 5252"            /* iW[]^_``üa d?,RR */
    $"4D4B 4947 4645 4444 423F 3C3B 3834 322F"            /* MKIGFEDDB?<;842/ */
    $"2B29 2623 201E 1C1A 1129 DEFF A8FF 26E5"            /* +)&# ....)Þÿ¨ÿ&å */
    $"2902 0C0D 0E0F 1124 1E0D 0E0F 0F07 5BAF"            /* )..Â...$.Â....[¯ */
    $"ABAF B1B5 B7B9 BCBF C2C3 C6C8 CBCD CFD2"            /* «¯±µ·¹¼¿ÂÃÆÈËÍÏÒ */
    $"D3D6 D9DB DDDF 0CE2 E5E7 EAEC EEEE F1F3"            /* ÓÖÙÛÝß.âåçêìîîñó */
    $"F6F9 FBFE E7FF 08F4 6957 5B5D 5E5F 6060"            /* öùûþçÿ.ôiW[]^_`` */
    $"FC61 1F64 3E2C 5352 4D4B 4947 4645 4444"            /* üa.d>,SRMKIGFEDD */
    $"423F 3C3B 3834 322F 2B29 2623 201E 1C1A"            /* B?<;842/+)&# ... */
    $"1129 DED6 FFFF FF01 43D5 FF34 FB47 000D"            /* .)ÞÖÿÿÿ.CÕÿ4ûG.Â */
    $"0D0E 0E10 1E1F 0E0D 0E0F 0D1A 94AD ADB0"            /* Â......Â..Â.­­° */
    $"B3B5 B8BA BDC0 C2C5 C6C9 CCCE D0D2 D4D6"            /* ³µ¸º½ÀÂÅÆÉÌÎÐÒÔÖ */
    $"D9DC DEE0 E2E5 E7EA ECEE EEF1 F3F6 F9FC"            /* ÙÜÞàâåçêìîîñóöùü */
    $"FEE6 FF03 9452 5D5D 295E 5F60 6061 6262"            /* þæÿ.R]])^_``abb */
    $"6161 625D 1B32 5552 4C49 4847 4544 4443"            /* aab].2URLIHGEDDC */
    $"403F 3C39 3634 302E 2B27 2422 201D 1B19"            /* @?<9640.+'$" ... */
    $"0B50 FEAB FFFF FF34 FB47 000D 0D0E 0E10"            /* .Pþ«ÿÿÿ4ûG.ÂÂ... */
    $"1E1F 0E0D 0E0F 0D1A 94AD ADB0 B3B5 B8BA"            /* ...Â..Â.­­°³µ¸º */
    $"BDC0 C2C5 C6C9 CCCE D0D2 D4D6 D9DC DEE0"            /* ½ÀÂÅÆÉÌÎÐÒÔÖÙÜÞà */
    $"E2E5 E7EA ECEE EEF1 F3F6 F9FC FEE6 FF2D"            /* âåçêìîîñóöùüþæÿ- */
    $"9452 5D5D 5E5F 6060 6162 6261 6162 5C1C"            /* R]]^_``abbaab\. */
    $"3155 524C 4948 4745 4444 4340 3F3C 3936"            /* 1URLIHGEDDC@?<96 */
    $"3430 2E2B 2724 2220 1D1B 190B 50FE A9FF"            /* 40.+'$" ....Pþ©ÿ */
    $"27FB 4700 0D0D 0E0E 101E 1F0E 0D0E 0F0D"            /* 'ûG.ÂÂ......Â..Â */
    $"1A94 ADAD B0B3 B5B8 BABD C0C2 C5C6 C9CC"            /* .­­°³µ¸º½ÀÂÅÆÉÌ */
    $"CED0 D2D4 D6D9 DCDE E00C E2E5 E7EA ECEE"            /* ÎÐÒÔÖÙÜÞà.âåçêìî */
    $"EEF1 F3F6 F9FC FEE6 FF2D 9452 5D5D 5E5F"            /* îñóöùüþæÿ-R]]^_ */
    $"6060 6162 6261 6162 5C1C 3255 524C 4948"            /* ``abbaab\.2URLIH */
    $"4745 4444 4340 3F3C 3936 3430 2E2B 2724"            /* GEDDC@?<9640.+'$ */
    $"2220 1D1B 190B 50FE D7FF FFFF 0140 D5FF"            /* " ....Pþ×ÿÿÿ.@Õÿ */
    $"027C 000C FE0E 2E0F 1B25 0F0D 0E0E 0F09"            /* .|..þ....%.Â...Æ */
    $"39A9 ACAE B0B4 B6B9 BBBD C0C3 C6C7 C9CC"            /* 9©¬®°´¶¹»½ÀÃÆÇÉÌ */
    $"CED0 D2D4 D7DA DBDE E0E3 E6E8 EBED EFEF"            /* ÎÐÒÔ×ÚÛÞàãæèëíïï */
    $"F2F4 F7FA FCFE E6FF 03BA 535C 5D01 5E60"            /* òô÷úüþæÿ.ºS\].^` */
    $"FE61 FE62 FF61 1F64 3D0F 3F55 504B 4847"            /* þaþbÿa.d=.?UPKHG */
    $"4645 4444 4340 3E3B 3836 3330 2D29 2623"            /* FEDDC@>;8630-)&# */
    $"211F 1C1A 170C 94AB FFFF FF02 7C00 0CFE"            /* !.....«ÿÿÿ.|..þ */
    $"0E2E 0F1B 250F 0D0E 0E0F 0939 A9AC AEB0"            /* ....%.Â...Æ9©¬®° */
    $"B4B6 B9BB BDC0 C3C6 C7C9 CCCE D0D2 D4D7"            /* ´¶¹»½ÀÃÆÇÉÌÎÐÒÔ× */
    $"DADB DEE0 E3E6 E8EB EDEF EFF2 F4F7 FAFC"            /* ÚÛÞàãæèëíïïòô÷úü */
    $"FEE6 FF05 BA53 5C5D 5E60 FE61 FE62 FF61"            /* þæÿ.ºS\]^`þaþbÿa */
    $"1F64 3D0F 3F56 504B 4847 4645 4444 4340"            /* .d=.?VPKHGFEDDC@ */
    $"3E3B 3836 3330 2D29 2623 211F 1C1A 170C"            /* >;8630-)&#!..... */
    $"94A9 FF02 7C00 0CFE 0E21 0F1B 250F 0D0E"            /* ©ÿ.|..þ.!..%.Â. */
    $"0E0F 0939 A9AC AEB0 B4B6 B9BB BDC0 C3C6"            /* ..Æ9©¬®°´¶¹»½ÀÃÆ */
    $"C7C9 CCCE D0D2 D4D7 DADB DEE0 0CE3 E6E8"            /* ÇÉÌÎÐÒÔ×ÚÛÞà.ãæè */
    $"EBED EFEF F2F4 F7FA FCFE E6FF 05BA 535C"            /* ëíïïòô÷úüþæÿ.ºS\ */
    $"5D5E 60FE 61FE 62FF 611F 643D 0F3F 5650"            /* ]^`þaþbÿa.d=.?VP */
    $"4B48 4746 4544 4443 403E 3B38 3633 302D"            /* KHGFEDDC@>;8630- */
    $"2926 2321 1F1C 1A17 0C94 D7FF FFFF 0146"            /* )&#!.....×ÿÿÿ.F */
    $"D6FF 03B5 0C08 0DFE 0E04 1726 130C 0EFE"            /* Öÿ.µ..Âþ...&...þ */
    $"0F26 0966 AFAC AFB2 B4B7 BABC BEC0 C3C6"            /* .&Æf¯¬¯²´·º¼¾ÀÃÆ */
    $"C7C9 CCCE D0D3 D6D8 DBDC DFE1 E4E7 E8EA"            /* ÇÉÌÎÐÓÖØÛÜßáäçèê */
    $"EDEF EFF2 F4F7 FAFD FEE6 FF03 CE59 5B5E"            /* íïïòô÷úýþæÿ.ÎY[^ */
    $"015F 60FE 61FE 6222 6160 615F 1B15 4A55"            /* ._`þaþb"a`a_..JU */
    $"4E49 4847 4544 4443 423F 3D3A 3633 312E"            /* NIHGEDDCB?=:631. */
    $"2B28 2523 201E 1C1A 1225 DBAC FF04 FFB5"            /* +(%# ....%Û¬ÿ.ÿµ */
    $"0C08 0DFE 0E04 1826 130C 0EFE 0F26 0966"            /* ..Âþ...&...þ.&Æf */
    $"AFAC AFB2 B4B7 BABC BEC0 C3C6 C7C9 CCCE"            /* ¯¬¯²´·º¼¾ÀÃÆÇÉÌÎ */
    $"D0D3 D6D8 DBDC DFE1 E4E7 E8EA EDEF EFF2"            /* ÐÓÖØÛÜßáäçèêíïïò */
    $"F4F7 FAFD FEE6 FF05 CE59 5B5E 5F60 FE61"            /* ô÷úýþæÿ.ÎY[^_`þa */
    $"FE62 2161 6061 5E1B 1449 554E 4948 4745"            /* þb!a`a^..IUNIHGE */
    $"4444 4342 3F3D 3A36 3331 2E2B 2825 2320"            /* DDCB?=:631.+(%#  */
    $"1E1C 1A12 2500 DBAB FF03 B50C 080D FE0E"            /* ....%.Û«ÿ.µ..Âþ. */
    $"0417 2513 0C0E FE0F 1909 66AF ACAF B2B4"            /* ..%...þ..Æf¯¬¯²´ */
    $"B7BA BCBE C0C3 C6C7 C9CC CED0 D3D6 D8DB"            /* ·º¼¾ÀÃÆÇÉÌÎÐÓÖØÛ */
    $"DCDF E10C E4E7 E8EA EDEF EFF2 F4F7 FAFD"            /* Üßá.äçèêíïïòô÷úý */
    $"FEE6 FF05 CE59 5B5E 5F60 FE61 FE62 2261"            /* þæÿ.ÎY[^_`þaþb"a */
    $"6061 5F1C 154A 554E 4948 4745 4444 4342"            /* `a_..JUNIHGEDDCB */
    $"3F3D 3A36 3331 2E2B 2825 2320 1E1C 1A12"            /* ?=:631.+(%# .... */
    $"25DB D8FF FFFF 0148 D7FF 36EE 2D01 0C0C"            /* %ÛØÿÿÿ.H×ÿ6î-... */
    $"0D0E 1524 160C 0D0E 0F0F 0C1E 99AB ACAF"            /* Â..$..Â.....«¬¯ */
    $"B2B4 B7BA BCBF C1C3 C6C8 CACD CFD1 D4D5"            /* ²´·º¼¿ÁÃÆÈÊÍÏÑÔÕ */
    $"D8DB DCDF E1E4 E7E8 EBED EFF0 F2F4 F7FA"            /* ØÛÜßáäçèëíïðòô÷ú */
    $"FDFE E6FF 03EB 625A 5E01 5F60 FE61 FE62"            /* ýþæÿ.ëbZ^._`þaþb */
    $"FF61 2060 6345 0921 4F53 4C49 4845 4444"            /* ÿa `cEÆ!OSLIHEDD */
    $"4342 403E 3B39 3633 312D 2A27 2421 1F1D"            /* CB@>;9631-*'$!.. */
    $"1A19 0A59 ACFF 36EE 2D01 0C0C 0D0E 1524"            /* ...Y¬ÿ6î-...Â..$ */
    $"160C 0D0E 0F0F 0C1E 99AB ACAF B2B4 B7BA"            /* ..Â.....«¬¯²´·º */
    $"BCBF C1C3 C6C8 CACD CFD1 D4D5 D8DB DCDF"            /* ¼¿ÁÃÆÈÊÍÏÑÔÕØÛÜß */
    $"E1E4 E7E8 EBED EFF0 F2F4 F7FA FDFE E6FF"            /* áäçèëíïðòô÷úýþæÿ */
    $"05EB 625A 5E5F 60FE 61FE 62FF 611F 6063"            /* .ëbZ^_`þaþbÿa.`c */
    $"4409 2150 534C 4948 4544 4443 4240 3E3B"            /* DÆ!PSLIHEDDCB@>; */
    $"3936 3331 2D2A 2724 211F 1D1A 190A 0059"            /* 9631-*'$!......Y */
    $"ACFF 29EE 2D01 0C0C 0D0E 1524 160C 0D0E"            /* ¬ÿ)î-...Â..$..Â. */
    $"0F0F 0C1E 99AB ACAF B2B4 B7BA BCBF C1C3"            /* ....«¬¯²´·º¼¿ÁÃ */
    $"C6C8 CACD CFD1 D4D5 D8DB DCDF E10C E4E7"            /* ÆÈÊÍÏÑÔÕØÛÜßá.äç */
    $"E8EB EDEF F0F2 F4F7 FAFD FEE6 FF05 EB62"            /* èëíïðòô÷úýþæÿ.ëb */
    $"5A5E 5F60 FE61 FE62 FF61 2060 6345 0A21"            /* Z^_`þaþbÿa `cE.! */
    $"4F53 4C49 4845 4444 4342 403E 3B39 3633"            /* OSLIHEDDCB@>;963 */
    $"312D 2A27 2421 1F1D 1A19 0A59 D8FF FFFF"            /* 1-*'$!.....YØÿÿÿ */
    $"0146 D7FF 365F 000C 0D0D 0E13 2218 0B0D"            /* .F×ÿ6_..ÂÂ.."..Â */
    $"0D0E 0F0F 0741 ABAA ADB0 B3B5 B8BB BDBF"            /* Â....A«ª­°³µ¸»½¿ */
    $"C2C4 C7C8 CBCE D0D2 D3D5 D8DB DCDF E1E5"            /* ÂÄÇÈËÎÐÒÓÕØÛÜßáå */
    $"E7E9 ECEE F0F0 F3F5 F8FB FDFE E5FF 028E"            /* çéìîððóõøûýþåÿ. */
    $"545E 035F 6061 61FD 62FF 61FE 601E 2307"            /* T^._`aaýbÿaþ`.#. */
    $"2D54 504B 4846 4545 4343 423F 3C3A 3735"            /* -TPKHFEECCB?<:75 */
    $"322F 2C29 2623 201D 1C1A 1615 C4AD FF36"            /* 2/,)&# .....Ä­ÿ6 */
    $"5F00 0C0D 0D0E 1322 180B 0D0D 0E0F 0F07"            /* _..ÂÂ.."..ÂÂ.... */
    $"41AB AAAD B0B3 B5B8 BBBD BFC2 C4C7 C8CB"            /* A«ª­°³µ¸»½¿ÂÄÇÈË */
    $"CED0 D2D3 D5D8 DBDC DFE1 E5E7 E9EC EEF0"            /* ÎÐÒÓÕØÛÜßáåçéìîð */
    $"F0F3 F5F8 FBFD FEE5 FF06 8E54 5E5F 6061"            /* ðóõøûýþåÿ.T^_`a */
    $"61FD 62FF 61FF 601D 5F22 072D 5450 4B48"            /* aýbÿaÿ`._".-TPKH */
    $"4645 4543 4342 3F3C 3A37 3532 2F2C 2926"            /* FEECCB?<:752/,)& */
    $"2320 1D1C 1A16 0115 C4AD FF29 5F00 0C0D"            /* # ......Ä­ÿ)_..Â */
    $"0D0E 1223 190B 0D0D 0E0F 0F07 41AB AAAD"            /* Â..#..ÂÂ....A«ª­ */
    $"B0B3 B5B8 BBBD BFC2 C4C7 C8CB CED0 D2D3"            /* °³µ¸»½¿ÂÄÇÈËÎÐÒÓ */
    $"D5D8 DBDC DFE1 0CE5 E7E9 ECEE F0F0 F3F5"            /* ÕØÛÜßá.åçéìîððóõ */
    $"F8FB FDFE E5FF 068E 545E 5F60 6161 FD62"            /* øûýþåÿ.T^_`aaýb */
    $"FF61 FE60 1E23 072D 5450 4B48 4645 4543"            /* ÿaþ`.#.-TPKHFEEC */
    $"4342 3F3C 3A37 3532 2F2C 2926 2320 1D1C"            /* CB?<:752/,)&# .. */
    $"1A16 15C4 D9FF FFFF 0149 D8FF 0BAC 080A"            /* ...ÄÙÿÿÿ.IØÿ.¬.. */
    $"0D0E 0E12 211A 0C0C 0DFE 0E28 0D13 81AD"            /* Â...!...Âþ.(Â.­ */
    $"AAAE B1B4 B6B9 BBBE C0C3 C5C7 C8CB CED0"            /* ª®±´¶¹»¾ÀÃÅÇÈËÎÐ */
    $"D2D4 D6D9 DCDD E0E3 E6E8 E9EB EEF0 F0F3"            /* ÒÔÖÙÜÝàãæèéëîððó */
    $"F6F9 FAFD FEE5 FF02 BF55 5D03 5F60 6161"            /* öùúýþåÿ.¿U]._`aa */
    $"FB62 0C61 5F61 4B11 0B38 5750 4B47 4645"            /* ûb.a_aK..8WPKGFE */
    $"FE43 1241 3D3B 3937 3531 2E2B 2825 231F"            /* þC.A=;9751.+(%#. */
    $"1D1C 1A0F 41EB AFFF 00AC 0A08 0A0D 0E0E"            /* ....Aë¯ÿ.¬...Â.. */
    $"1220 1A0B 0C0D FE0E 280D 1381 ADAA AEB1"            /* . ...Âþ.(Â.­ª®± */
    $"B4B6 B9BB BEC0 C3C5 C7C8 CBCE D0D2 D4D6"            /* ´¶¹»¾ÀÃÅÇÈËÎÐÒÔÖ */
    $"D9DC DDE0 E3E6 E8E9 EBEE F0F0 F3F6 F9FA"            /* ÙÜÝàãæèéëîððóöùú */
    $"FDFE E5FF 06BF 555D 5F60 6161 FB62 0C61"            /* ýþåÿ.¿U]_`aaûb.a */
    $"5F61 4B11 0B38 5750 4B47 4645 FE43 0F41"            /* _aK..8WPKGFEþC.A */
    $"3D3B 3937 3531 2E2B 2825 231F 1D1C 1A02"            /* =;9751.+(%#..... */
    $"0F41 EBAF FF0B AC08 0A0D 0E0E 1220 1A0B"            /* .Aë¯ÿ.¬..Â... .. */
    $"0C0D FE0E 1B0D 1381 ADAA AEB1 B4B6 B9BB"            /* .Âþ..Â.­ª®±´¶¹» */
    $"BEC0 C3C5 C7C8 CBCE D0D2 D4D6 D9DC DDE0"            /* ¾ÀÃÅÇÈËÎÐÒÔÖÙÜÝà */
    $"E30C E6E8 E9EB EEF0 F0F3 F6F9 FAFD FEE5"            /* ã.æèéëîððóöùúýþå */
    $"FF06 BF55 5D5F 6061 61FB 620C 615F 614B"            /* ÿ.¿U]_`aaûb.a_aK */
    $"100B 3757 504B 4746 45FE 4312 413D 3B39"            /* ..7WPKGFEþC.A=;9 */
    $"3735 312E 2B28 2523 1F1D 1C1A 0F41 EBDA"            /* 751.+(%#.....AëÚ */
    $"FFFF FF01 49D9 FF37 D516 050C 0D0E 0E1E"            /* ÿÿÿ.IÙÿ7Õ...Â... */
    $"1D0A 0B0D 0D0E 0F0F 083B A9A8 ABAE B1B4"            /* ...ÂÂ....;©¨«®±´ */
    $"B7B9 BBBD C0C3 C5C7 C9CC CFD1 D3D4 D6D9"            /* ·¹»½ÀÃÅÇÉÌÏÑÓÔÖÙ */
    $"DCDD E0E3 E6E8 EAED EFF1 F1F4 F6F9 FCFE"            /* ÜÝàãæèêíïññôöùüþ */
    $"E4FF 02E9 685B 035F 6061 61FB 620B 6160"            /* äÿ.éh[._`aaûb.a` */
    $"5F5F 2F07 1344 564E 4947 FE44 1343 423F"            /* __/..DVNIGþD.CB? */
    $"3D3B 3936 322F 2C29 2724 211E 1C1B 1908"            /* =;962/,)'$!..... */
    $"76B0 FF01 D516 3505 0C0D 0E0E 1D1D 0A0B"            /* v°ÿ.Õ.5..Â...... */
    $"0D0D 0E0F 0F08 3BA9 A8AB AEB1 B4B7 B9BB"            /* ÂÂ....;©¨«®±´·¹» */
    $"BDC0 C3C5 C7C9 CCCF D1D3 D4D6 D9DC DDE0"            /* ½ÀÃÅÇÉÌÏÑÓÔÖÙÜÝà */
    $"E3E6 E8EA EDEF F1F1 F4F6 F9FC FEE4 FF06"            /* ãæèêíïññôöùüþäÿ. */
    $"E968 5B5F 6061 61FB 620B 6160 5F5F 2F07"            /* éh[_`aaûb.a`__/. */
    $"1344 564E 4947 FE44 1043 423F 3D3B 3936"            /* .DVNIGþD.CB?=;96 */
    $"322F 2C29 2724 211E 1C1B 0219 0876 B0FF"            /* 2/,)'$!......v°ÿ */
    $"2BD5 1605 0C0D 0E0F 1D1C 0A0B 0D0D 0E0F"            /* +Õ...Â......ÂÂ.. */
    $"0F08 3BA9 A8AB AEB1 B4B7 B9BB BDC0 C3C5"            /* ..;©¨«®±´·¹»½ÀÃÅ */
    $"C7C9 CCCF D1D3 D4D6 D9DC DDE0 E30B E6E8"            /* ÇÉÌÏÑÓÔÖÙÜÝàã.æè */
    $"EAED EFF1 F1F4 F6F9 FCFE E4FF 06E9 685B"            /* êíïññôöùüþäÿ.éh[ */
    $"5F60 6161 FB62 0B61 605F 5F2F 0713 4456"            /* _`aaûb.a`__/..DV */
    $"4E49 47FE 4413 4342 3F3D 3B39 3632 2F2C"            /* NIGþD.CB?=;962/, */
    $"2927 2421 1E1C 1B19 0876 DAFF FFFF 0152"            /* )'$!.....vÚÿÿÿ.R */
    $"DAFF 38F7 4B00 0C0C 0D0E 191E 0B0A 0C0D"            /* Úÿ8÷K...Â......Â */
    $"0D0E 0F0F 0662 AFA9 ADB0 B3B5 B7BA BDBF"            /* Â....b¯©­°³µ·º½¿ */
    $"C0C3 C5C9 CACC CFD1 D3D4 D7DA DDDE E1E4"            /* ÀÃÅÉÊÌÏÑÓÔ×ÚÝÞáä */
    $"E6E8 EAED EFF1 F1F4 F7FA FBFE E3FF 0192"            /* æèêíïññô÷úûþãÿ. */
    $"5601 5F61 FE62 FE63 FF62 2361 605F 5F4E"            /* V._aþbþcÿb#a`__N */
    $"1608 1B4C 544D 4847 4544 4343 413E 3C3A"            /* ...LTMHGEDCCA><: */
    $"3735 322F 2C29 2623 201E 1B1A 1512 C0B2"            /* 752/,)&# .....À² */
    $"FF02 F74B 00FF 0C33 0D0E 191E 0B0A 0C0D"            /* ÿ.÷K.ÿ.3Â......Â */
    $"0D0E 0F0F 0662 AFA9 ADB0 B3B5 B7BA BDBF"            /* Â....b¯©­°³µ·º½¿ */
    $"C0C3 C5C9 CACC CFD1 D3D4 D7DA DDDE E1E4"            /* ÀÃÅÉÊÌÏÑÓÔ×ÚÝÞáä */
    $"E6E8 EAED EFF1 F1F4 F7FA FBFE E3FF 0392"            /* æèêíïññô÷úûþãÿ. */
    $"565F 61FE 62FE 63FF 621F 6160 5F5F 4E16"            /* V_aþbþcÿb.a`__N. */
    $"081C 4B55 4D48 4745 4443 4341 3E3C 3A37"            /* ..KUMHGEDCCA><:7 */
    $"3532 2F2C 2926 2320 1E1B 031A 1512 C0B2"            /* 52/,)&# ......À² */
    $"FF2C F74B 000C 0C0D 0E19 1D0B 0A0C 0D0D"            /* ÿ,÷K...Â......ÂÂ */
    $"0E0F 0F06 62AF A9AD B0B3 B5B7 BABD BFC0"            /* ....b¯©­°³µ·º½¿À */
    $"C3C5 C9CA CCCF D1D3 D4D7 DADD DEE1 E40B"            /* ÃÅÉÊÌÏÑÓÔ×ÚÝÞáä. */
    $"E6E8 EAED EFF1 F1F4 F7FA FBFE E3FF 0392"            /* æèêíïññô÷úûþãÿ. */
    $"565F 61FE 62FE 63FF 6223 6160 5F5F 4E16"            /* V_aþbþcÿb#a`__N. */
    $"081C 4C54 4D48 4745 4443 4341 3E3C 3A37"            /* ..LTMHGEDCCA><:7 */
    $"3532 2F2C 2926 2320 1E1B 1A15 12C0 DBFF"            /* 52/,)&# .....ÀÛÿ */
    $"FFFF 0154 DAFF 0A83 000B 0D0D 0E15 220F"            /* ÿÿ.TÚÿ...ÂÂ..". */
    $"0A0C FE0D 2A0E 0F0D 1289 ABAA ADB0 B3B5"            /* ..þÂ*..Â.«ª­°³µ */
    $"B7BA BDBF C2C4 C7C9 CACC CFD1 D3D6 D7DA"            /* ·º½¿ÂÄÇÉÊÌÏÑÓÖ×Ú */
    $"DDDE E1E4 E6E8 EBED EFF1 F2F4 F7FA FBFE"            /* ÝÞáäæèëíïñòô÷úûþ */
    $"E3FF 01BA 5701 5F61 FE62 FE63 FF62 0E61"            /* ãÿ.ºW._aþbþcÿb.a */
    $"605F 5E5D 320B 0A26 5353 4C48 4644 FE43"            /* `_^]2..&SSLHFDþC */
    $"1240 3E3C 3937 3431 2E2B 2825 231F 1D1B"            /* .@><9741.+(%#... */
    $"190F 3EEF B3FF 0283 000B FE0D 0416 220F"            /* ..>ï³ÿ...þÂ..". */
    $"0A0C FE0D 2A0E 0F0D 1289 ABAA ADB0 B3B5"            /* ..þÂ*..Â.«ª­°³µ */
    $"B7BA BDBF C2C4 C7C9 CACC CFD1 D3D6 D7DA"            /* ·º½¿ÂÄÇÉÊÌÏÑÓÖ×Ú */
    $"DDDE E1E4 E6E8 EBED EFF1 F2F4 F7FA FBFE"            /* ÝÞáäæèëíïñòô÷úûþ */
    $"E3FF 03BA 575F 61FE 62FE 63FF 620E 6160"            /* ãÿ.ºW_aþbþcÿb.a` */
    $"5F5E 5C32 0B0A 2653 534C 4846 44FE 430D"            /* _^\2..&SSLHFDþCÂ */
    $"403E 3C39 3734 312E 2B28 2523 1F1D 041B"            /* @><9741.+(%#.... */
    $"190F 3EEF B3FF 0A83 000B 0D0D 0E16 210F"            /* ..>ï³ÿ...ÂÂ..!. */
    $"0A0C FE0D 1E0E 0F0D 1289 ABAA ADB0 B3B5"            /* ..þÂ...Â.«ª­°³µ */
    $"B7BA BDBF C2C4 C7C9 CACC CFD1 D3D6 D7DA"            /* ·º½¿ÂÄÇÉÊÌÏÑÓÖ×Ú */
    $"DDDE E1E4 0BE6 E8EB EDEF F1F2 F4F7 FAFB"            /* ÝÞáä.æèëíïñòô÷úû */
    $"FEE3 FF03 BA57 5F61 FE62 FE63 FF62 0E61"            /* þãÿ.ºW_aþbþcÿb.a */
    $"605F 5E5D 320B 0926 5253 4C48 4644 FE43"            /* `_^]2.Æ&RSLHFDþC */
    $"1240 3E3C 3937 3431 2E2B 2825 231F 1D1B"            /* .@><9741.+(%#... */
    $"190F 3EEF DCFF FFFF 0155 DBFF 0CB8 0809"            /* ..>ïÜÿÿÿ.UÛÿ.¸.Æ */
    $"0D0E 0E13 2112 090B 0C0C FE0E 290F 074C"            /* Â...!.Æ...þ.)..L */
    $"A9A8 ABAE B0B3 B6B8 BBBE C0C2 C5C7 C8CA"            /* ©¨«®°³¶¸»¾ÀÂÅÇÈÊ */
    $"CDD0 D2D4 D6D8 DADD DEE1 E4E7 E9EB EEF0"            /* ÍÐÒÔÖØÚÝÞáäçéëîð */
    $"F2F2 F5F7 FAFB FEE3 FF01 E065 035D 6162"            /* òòõ÷úûþãÿ.àe.]ab */
    $"62FD 63FE 6223 615F 5F5E 4F1A 090C 2F55"            /* býcþb#a__^O.Æ./U */
    $"514B 4746 4444 4242 403E 3B38 3633 302D"            /* QKGFDDBB@>;8630- */
    $"2A26 2421 1F1C 1A18 0A86 B4FF 03B8 0809"            /* *&$!.....´ÿ.¸.Æ */
    $"0DFF 0E06 1421 120A 0B0C 0CFE 0E29 0F07"            /* Âÿ...!.....þ.).. */
    $"4CA9 A8AB AEB0 B3B6 B8BB BEC0 C2C5 C7C8"            /* L©¨«®°³¶¸»¾ÀÂÅÇÈ */
    $"CACD D0D2 D4D6 D8DA DDDE E1E4 E7E9 EBEE"            /* ÊÍÐÒÔÖØÚÝÞáäçéëî */
    $"F0F2 F2F5 F7FA FBFE E3FF 05E0 655D 6162"            /* ðòòõ÷úûþãÿ.àe]ab */
    $"62FD 63FE 621E 615F 5F5E 4F1A 090C 3055"            /* býcþb.a__^O.Æ.0U */
    $"514B 4746 4444 4242 403E 3B38 3633 302D"            /* QKGFDDBB@>;8630- */
    $"2A26 2421 1F04 1C1A 180A 86B4 FF0C B808"            /* *&$!......´ÿ.¸. */
    $"090D 0E0E 1321 1109 0B0C 0CFE 0E1D 0F07"            /* ÆÂ...!.Æ...þ.... */
    $"4CA9 A8AB AEB0 B3B6 B8BB BEC0 C2C5 C7C8"            /* L©¨«®°³¶¸»¾ÀÂÅÇÈ */
    $"CACD D0D2 D4D6 D8DA DDDE E1E4 0BE7 E9EB"            /* ÊÍÐÒÔÖØÚÝÞáä.çéë */
    $"EEF0 F2F2 F5F7 FAFB FEE3 FF05 E065 5D61"            /* îðòòõ÷úûþãÿ.àe]a */
    $"6262 FD63 FE62 2361 5F5F 5E4F 1A09 0C2F"            /* bbýcþb#a__^O.Æ./ */
    $"5551 4B47 4644 4442 4240 3E3B 3836 3330"            /* UQKGFDDBB@>;8630 */
    $"2D2A 2624 211F 1C1A 180A 86DC FFFF FF01"            /* -*&$!.....Üÿÿÿ. */
    $"55DC FF3A D31A 050D 0D0E 1421 1209 0B0B"            /* UÜÿ:Ó..ÂÂ..!.Æ.. */
    $"0C0C 0E0E 0F0B 2194 A9A8 ACAF B1B4 B7B9"            /* ......!©¨¬¯±´·¹ */
    $"BCBE C0C2 C5C7 CACB CED0 D2D4 D6D8 DBDE"            /* ¼¾ÀÂÅÇÊËÎÐÒÔÖØÛÞ */
    $"DFE2 E5E7 E9EB EEF0 F2F2 F5F8 FBFC FEE2"            /* ßâåçéëîðòòõøûüþâ */
    $"FF00 A103 5761 6262 FB63 2562 6160 5E5D"            /* ÿ.¡.Wabbûc%ba`^] */
    $"5D35 0C0A 0C34 564F 4A47 4644 4343 413E"            /* ]5...4VOJGFDCCA> */
    $"3D3A 3835 322F 2C28 2623 201E 1B1A 1512"            /* =:852/,(&# ..... */
    $"BCB6 FF04 D31A 050D 0D35 0E14 2111 090B"            /* ¼¶ÿ.Ó..ÂÂ5..!.Æ. */
    $"0B0C 0C0E 0E0F 0B21 94A9 A8AC AFB1 B4B7"            /* .......!©¨¬¯±´· */
    $"B9BC BEC0 C2C5 C7CA CBCE D0D2 D4D6 D8DB"            /* ¹¼¾ÀÂÅÇÊËÎÐÒÔÖØÛ */
    $"DEDF E2E5 E7E9 EBEE F0F2 F2F5 F8FB FCFE"            /* Þßâåçéëîðòòõøûüþ */
    $"E2FF 04A1 5761 6262 FB63 1F62 6160 5E5D"            /* âÿ.¡Wabbûc.ba`^] */
    $"5C35 0D0A 0C34 564F 4A47 4644 4343 413E"            /* \5Â..4VOJGFDCCA> */
    $"3D3A 3835 322F 2C28 2623 2005 1E1B 1A15"            /* =:852/,(&# ..... */
    $"12BC B6FF 2ED3 1A05 0D0D 0E13 2012 090B"            /* .¼¶ÿ.Ó..ÂÂ.. .Æ. */
    $"0B0C 0C0E 0E0F 0B21 94A9 A8AC AFB1 B4B7"            /* .......!©¨¬¯±´· */
    $"B9BC BEC0 C2C5 C7CA CBCE D0D2 D4D6 D8DB"            /* ¹¼¾ÀÂÅÇÊËÎÐÒÔÖØÛ */
    $"DEDF E2E5 0BE7 E9EB EEF0 F2F2 F5F8 FBFC"            /* Þßâå.çéëîðòòõøûü */
    $"FEE2 FF04 A157 6162 62FB 6325 6261 605E"            /* þâÿ.¡Wabbûc%ba`^ */
    $"5D5C 350D 0A0C 3456 4F4A 4746 4443 4341"            /* ]\5Â..4VOJGFDCCA */
    $"3E3D 3A38 3532 2F2C 2826 2320 1E1B 1A15"            /* >=:852/,(&# .... */
    $"12BC DDFF FFFF 0164 DDFF 0CF5 4400 0C0D"            /* .¼Ýÿÿÿ.dÝÿ.õD..Â */
    $"0D12 2014 080A 0C0C FE0D FF0E 2908 66AA"            /* Â. .....þÂÿ.).fª */
    $"A5A9 ADB0 B2B5 B8BA BDBF C1C3 C6C8 C9CB"            /* ¥©­°²µ¸º½¿ÁÃÆÈÉË */
    $"CED0 D3D5 D6D8 DBDE E0E3 E5E7 EAEC EFF0"            /* ÎÐÓÕÖØÛÞàãåçêìïð */
    $"F2F2 F5F8 FBFC FEE2 FF00 CF04 5E60 6262"            /* òòõøûüþâÿ.Ï.^`bb */
    $"63FE 64FF 6326 6261 605E 5C5D 4C1B 0B0A"            /* cþdÿc&ba`^\]L... */
    $"103E 564D 4946 4544 4342 403E 3B3A 3734"            /* .>VMIFEDCB@>;:74 */
    $"312E 2B28 2421 1F1D 1B19 0E3A EDB8 FF05"            /* 1.+($!.....:í¸ÿ. */
    $"F544 000C 0D0D 0611 1F14 080A 0C0C FE0D"            /* õD..ÂÂ........þÂ */
    $"FF0E 2908 66AA A5A9 ADB0 B2B5 B8BA BDBF"            /* ÿ.).fª¥©­°²µ¸º½¿ */
    $"C1C3 C6C8 C9CB CED0 D3D5 D6D8 DBDE E0E3"            /* ÁÃÆÈÉËÎÐÓÕÖØÛÞàã */
    $"E5E7 EAEC EFF0 F2F2 F5F8 FBFC FEE2 FF05"            /* åçêìïðòòõøûüþâÿ. */
    $"CF5E 6062 6263 FE64 FF63 1F62 6160 5E5C"            /* Ï^`bbcþdÿc.ba`^\ */
    $"5D4C 1B0B 0A10 3D56 4D49 4645 4443 4240"            /* ]L....=VMIFEDCB@ */
    $"3E3B 3A37 3431 2E2B 2824 2106 1F1D 1B19"            /* >;:741.+($!..... */
    $"0E3A EDB8 FF0C F544 000C 0D0D 111F 1408"            /* .:í¸ÿ.õD..ÂÂ.... */
    $"0A0C 0CFE 0DFF 0E1D 0866 AAA5 A9AD B0B2"            /* ...þÂÿ...fª¥©­°² */
    $"B5B8 BABD BFC1 C3C6 C8C9 CBCE D0D3 D5D6"            /* µ¸º½¿ÁÃÆÈÉËÎÐÓÕÖ */
    $"D8DB DEE0 E3E5 0BE7 EAEC EFF0 F2F2 F5F8"            /* ØÛÞàãå.çêìïðòòõø */
    $"FBFC FEE2 FF05 CF5E 6062 6263 FE64 FF63"            /* ûüþâÿ.Ï^`bbcþdÿc */
    $"2662 6160 5E5C 5D4C 1B0B 0A10 3E56 4D49"            /* &ba`^\]L....>VMI */
    $"4645 4443 4240 3E3B 3A37 3431 2E2B 2824"            /* FEDCB@>;:741.+($ */
    $"211F 1D1B 190E 3AED DEFF FFFF 0164 DDFF"            /* !.....:íÞÿÿÿ.dÝÿ */
    $"0C8D 000B 0C0D 0F1E 1708 0A0A 0C0C FE0D"            /* ....Â........þÂ */
    $"2B0E 0A28 98A5 A6AA ADB0 B2B5 B8BA BDBF"            /* +..(¥¦ª­°²µ¸º½¿ */
    $"C1C3 C6C8 C9CC CED1 D3D5 D6D9 DBDD E0E3"            /* ÁÃÆÈÉÌÎÑÓÕÖÙÛÝàã */
    $"E6E8 EAEC EFF0 F1F2 F5F8 FBFC FEE2 FF00"            /* æèêìïðñòõøûüþâÿ. */
    $"F304 715D 6263 63FE 64FF 6326 6261 605F"            /* ó.q]bccþdÿc&ba`_ */
    $"5D5C 5833 0E0B 0917 4C55 4C48 4644 4342"            /* ]\X3..Æ.LULHFDCB */
    $"4240 3D3A 3936 3330 2E2B 2825 211E 1C1A"            /* B@=:9630.+(%!... */
    $"1807 8FB8 FF05 8D00 0B0C 0D0F 061D 1708"            /* ..¸ÿ....Â..... */
    $"090A 0C0C FE0D 2B0E 0A28 98A5 A6AA ADB0"            /* Æ...þÂ+..(¥¦ª­° */
    $"B2B5 B8BA BDBF C1C3 C6C8 C9CC CED1 D3D5"            /* ²µ¸º½¿ÁÃÆÈÉÌÎÑÓÕ */
    $"D6D9 DBDD E0E3 E6E8 EAEC EFF0 F1F2 F5F8"            /* ÖÙÛÝàãæèêìïðñòõø */
    $"FBFC FEE2 FF05 F371 5D62 6363 FE64 FF63"            /* ûüþâÿ.óq]bccþdÿc */
    $"1F62 6160 5F5D 5C57 330E 0B09 174C 544C"            /* .ba`_]\W3..Æ.LTL */
    $"4846 4443 4242 403D 3A39 3633 302E 2B28"            /* HFDCBB@=:9630.+( */
    $"2506 211E 1C1A 1807 8FB8 FF0C 8D00 0B0C"            /* %.!.....¸ÿ.... */
    $"0D0F 1D17 080A 0A0C 0CFE 0D1F 0E0A 2898"            /* Â........þÂ...( */
    $"A5A6 AAAD B0B2 B5B8 BABD BFC1 C3C6 C8C9"            /* ¥¦ª­°²µ¸º½¿ÁÃÆÈÉ */
    $"CCCE D1D3 D5D6 D9DB DDE0 E3E6 0BE8 EAEC"            /* ÌÎÑÓÕÖÙÛÝàãæ.èêì */
    $"EFF0 F1F2 F5F8 FBFC FEE2 FF05 F371 5D62"            /* ïðñòõøûüþâÿ.óq]b */
    $"6363 FE64 FF63 2662 6160 5F5D 5C58 330E"            /* ccþdÿc&ba`_]\X3. */
    $"0B09 164D 554C 4846 4443 4242 403D 3A39"            /* .Æ.MULHFDCBB@=:9 */
    $"3633 302E 2B28 2521 1E1C 1A18 078F DEFF"            /* 630.+(%!.....Þÿ */
    $"FFFF 015D DEFF 0ED4 1E06 0D0D 0E18 1A09"            /* ÿÿ.]Þÿ.Ô..ÂÂ...Æ */
    $"090A 0A0C 0C0D FE0E 2908 69A9 A3A7 ABAE"            /* Æ....Âþ.).i©£§«® */
    $"B0B3 B6B8 BABD BFC1 C3C6 C8CB CCCF D1D3"            /* °³¶¸º½¿ÁÃÆÈËÌÏÑÓ */
    $"D5D7 D9DC DFE1 E4E6 E8EA ECEF F0F1 F3F6"            /* Õ×ÙÜßáäæèêìïðñóö */
    $"F8FB FEE0 FF01 9659 FE63 FE64 FE63 2662"            /* øûþàÿ.Yþcþdþc&b */
    $"6060 5E5C 5A4A 1C0B 0B0A 2553 524B 4845"            /* ``^\ZJ....%SRKHE */
    $"4443 4242 3F3D 3A37 3532 2E2C 2925 2320"            /* DCBB?=:752.,)%#  */
    $"1D1B 1A11 30E7 BAFF 06D4 1E06 0D0D 0E18"            /* ....0çºÿ.Ô..ÂÂ.. */
    $"0719 0909 0A0A 0C0C 0DFE 0E29 0869 A9A3"            /* ..ÆÆ....Âþ.).i©£ */
    $"A7AB AEB0 B3B6 B8BA BDBF C1C3 C6C8 CBCC"            /* §«®°³¶¸º½¿ÁÃÆÈËÌ */
    $"CFD1 D3D5 D7D9 DCDF E1E4 E6E8 EAEC EFF0"            /* ÏÑÓÕ×ÙÜßáäæèêìïð */
    $"F1F3 F6F8 FBFE E0FF 0196 59FE 63FE 64FE"            /* ñóöøûþàÿ.Yþcþdþ */
    $"631E 6260 605E 5C5A 491D 0B0A 0925 5353"            /* c.b``^\ZI...Æ%SS */
    $"4B48 4544 4342 423F 3D3A 3735 322E 2C29"            /* KHEDCBB?=:752.,) */
    $"2507 2320 1D1B 1A11 30E7 BAFF 0ED4 1E06"            /* %.# ....0çºÿ.Ô.. */
    $"0D0D 0E18 1A09 090A 0A0C 0C0D FE0E 1E08"            /* ÂÂ...ÆÆ....Âþ... */
    $"69A9 A3A7 ABAE B0B3 B6B8 BABD BFC1 C3C6"            /* i©£§«®°³¶¸º½¿ÁÃÆ */
    $"C8CB CCCF D1D3 D5D7 D9DC DFE1 E4E6 0AE8"            /* ÈËÌÏÑÓÕ×ÙÜßáäæ.è */
    $"EAEC EFF0 F1F3 F6F8 FBFE E0FF 0196 59FE"            /* êìïðñóöøûþàÿ.Yþ */
    $"63FE 64FE 6326 6260 605E 5C5A 491D 0B0B"            /* cþdþc&b``^\ZI... */
    $"0926 5353 4B48 4544 4342 423F 3D3A 3735"            /* Æ&SSKHEDCBB?=:75 */
    $"322E 2C29 2523 201D 1B1A 1130 E7DF FFFF"            /* 2.,)%# ....0çßÿÿ */
    $"FF01 5DDF FF0A FC44 000D 0E0D 151E 0B07"            /* ÿ.]ßÿ.üD.Â.Â.... */
    $"09FE 0B2E 0C0D 0E0E 0928 97A3 A4A8 ACAF"            /* Æþ...Â..Æ(£¤¨¬¯ */
    $"B1B4 B7B9 BBBE C0C2 C4C7 C9CA CCCF D2D4"            /* ±´·¹»¾ÀÂÄÇÉÊÌÏÒÔ */
    $"D6D7 D9DC DFE1 E4E6 E9EB EDEF F0F1 F4F7"            /* Ö×ÙÜßáäæéëíïðñô÷ */
    $"F9FC FDE0 FF03 CE5F 6263 FB64 2763 6261"            /* ùüýàÿ.Î_bcûd'cba */
    $"5F5D 5C5B 5634 0F0A 0A0B 3257 514A 4645"            /* _]\[V4....2WQJFE */
    $"4443 4341 3E3B 3937 3430 2E2B 2725 221F"            /* DCCA>;9740.+'%". */
    $"1C1A 190A 68BB FF07 FC44 000D 0E0D 151D"            /* ....h»ÿ.üD.Â.Â.. */
    $"020B 0709 FE0B 2E0C 0D0E 0E09 2897 A3A4"            /* ...Æþ...Â..Æ(£¤ */
    $"A8AC AFB1 B4B7 B9BB BEC0 C2C4 C7C9 CACC"            /* ¨¬¯±´·¹»¾ÀÂÄÇÉÊÌ */
    $"CFD2 D4D6 D7D9 DCDF E1E4 E6E9 EBED EFF0"            /* ÏÒÔÖ×ÙÜßáäæéëíïð */
    $"F1F4 F7F9 FCFD E0FF 03CE 5F62 63FB 641F"            /* ñô÷ùüýàÿ.Î_bcûd. */
    $"6362 615F 5D5C 5B56 350F 0A0A 0B31 5750"            /* cba_]\[V5....1WP */
    $"4A46 4544 4343 413E 3B39 3734 302E 2B27"            /* JFEDCCA>;9740.+' */
    $"0725 221F 1C1A 190A 68BB FF0A FC44 000D"            /* .%".....h»ÿ.üD.Â */
    $"0E0D 151D 0B07 09FE 0B23 0C0D 0E0E 0928"            /* .Â....Æþ.#.Â..Æ( */
    $"97A3 A4A8 ACAF B1B4 B7B9 BBBE C0C2 C4C7"            /* £¤¨¬¯±´·¹»¾ÀÂÄÇ */
    $"C9CA CCCF D2D4 D6D7 D9DC DFE1 E4E6 0AE9"            /* ÉÊÌÏÒÔÖ×ÙÜßáäæ.é */
    $"EBED EFF0 F1F4 F7F9 FCFD E0FF 03CE 5F62"            /* ëíïðñô÷ùüýàÿ.Î_b */
    $"63FB 6409 6362 615F 5D5C 5B56 3410 FE0A"            /* cûdÆcba_]\[V4.þ. */
    $"1A31 5750 4A46 4544 4343 413E 3B39 3734"            /* .1WPJFEDCCA>;974 */
    $"302E 2B27 2522 1F1C 1A19 0A68 DFFF FFFF"            /* 0.+'%".....hßÿÿÿ */
    $"0164 DFFF 0C72 000B 0C0D 141B 0E07 090A"            /* .dßÿ.r...Â....Æ. */
    $"0B0B FD0D 2B0E 0B70 A6A1 A5A9 ACAF B1B4"            /* ..ýÂ+..p¦¡¥©¬¯±´ */
    $"B7BA BCBF C1C3 C4C7 C9CB CDD0 D2D4 D6D8"            /* ·º¼¿ÁÃÄÇÉËÍÐÒÔÖØ */
    $"DBDD DFE1 E4E6 E9EB EDEF F1F2 F4F7 F9FC"            /* ÛÝßáäæéëíïñòô÷ùü */
    $"FDE0 FF04 FF8C 5C63 64FE 65FF 6428 6362"            /* ýàÿ.ÿ\cdþeÿd(cb */
    $"6160 5E5C 5B59 4A21 0B0B 0A0E 3857 504A"            /* a`^\[YJ!....8WPJ */
    $"4644 4443 413F 3D3A 3835 3330 2D2A 2723"            /* FDDCA?=:8530-*'# */
    $"201E 1B1A 1614 A9BC FF07 7200 0B0C 0D14"            /*  .....©¼ÿ.r...Â. */
    $"1C0E 0407 090A 0B0B FD0D 2B0E 0B70 A6A1"            /* ....Æ...ýÂ+..p¦¡ */
    $"A5A9 ACAF B1B4 B7BA BCBF C1C3 C4C7 C9CB"            /* ¥©¬¯±´·º¼¿ÁÃÄÇÉË */
    $"CDD0 D2D4 D6D8 DBDD DFE1 E4E6 E9EB EDEF"            /* ÍÐÒÔÖØÛÝßáäæéëíï */
    $"F1F2 F4F7 F9FC FDDF FF03 8C5C 6364 FE65"            /* ñòô÷ùüýßÿ.\cdþe */
    $"FF64 1F63 6261 605E 5C5B 5A4A 200B 0B0A"            /* ÿd.cba`^\[ZJ ... */
    $"0E38 5750 4A46 4444 4341 3F3D 3A38 3533"            /* .8WPJFDDCA?=:853 */
    $"302D 2A08 2723 201E 1B1A 1614 A9BC FF0C"            /* 0-*.'# .....©¼ÿ. */
    $"7200 0B0C 0D14 1B0D 0709 0A0B 0BFD 0D20"            /* r...Â..Â.Æ...ýÂ  */
    $"0E0B 70A6 A1A5 A9AC AFB1 B4B7 BABC BFC1"            /* ..p¦¡¥©¬¯±´·º¼¿Á */
    $"C3C4 C7C9 CBCD D0D2 D4D6 D8DB DDDF E1E4"            /* ÃÄÇÉËÍÐÒÔÖØÛÝßáä */
    $"E60A E9EB EDEF F1F2 F4F7 F9FC FDDF FF03"            /* æ.éëíïñòô÷ùüýßÿ. */
    $"8C5C 6364 FE65 FF64 2863 6261 605E 5C5B"            /* \cdþeÿd(cba`^\[ */
    $"594A 210B 0B0A 0E37 5650 4A46 4444 4341"            /* YJ!....7VPJFDDCA */
    $"3F3D 3A38 3533 302D 2A27 2320 1E1B 1A16"            /* ?=:8530-*'# .... */
    $"14A9 E0FF FFFF 0167 E0FF 0D9F 0309 0C0C"            /* .©àÿÿÿ.gàÿÂ.Æ.. */
    $"121D 0E07 0909 0A0B 0BFE 0D2B 0E09 279A"            /* ....ÆÆ...þÂ+.Æ' */
    $"A1A3 A6AB ADAF B3B5 B7B9 BCBF C1C3 C5C8"            /* ¡£¦«­¯³µ·¹¼¿ÁÃÅÈ */
    $"CACB CDD0 D3D4 D6D8 DADD E0E2 E5E7 E9EB"            /* ÊËÍÐÓÔÖØÚÝàâåçéë */
    $"EDF0 F1F2 F4F7 FAFD DFFF 04FF D362 6364"            /* íðñòô÷úýßÿ.ÿÓbcd */
    $"FE65 FE64 2863 6260 5E5D 5B59 5639 120A"            /* þeþd(cb`^][YV9.. */
    $"0B09 103F 564D 4946 4443 4241 3F3C 3A37"            /* .Æ.?VMIFDCBA?<:7 */
    $"3532 2F2D 2A26 2320 1D1C 190E 2CE5 BEFF"            /* 52/-*&# ....,å¾ÿ */
    $"089F 0309 0C0C 131D 0F07 FF09 020A 0B0B"            /* ..Æ......ÿÆ.... */
    $"FE0D 2B0E 0927 9AA1 A3A6 ABAD AFB3 B5B7"            /* þÂ+.Æ'¡£¦«­¯³µ· */
    $"B9BC BFC1 C3C5 C8CA CBCD D0D3 D4D6 D8DA"            /* ¹¼¿ÁÃÅÈÊËÍÐÓÔÖØÚ */
    $"DDE0 E2E5 E7E9 EBED F0F1 F2F4 F7FA FDDE"            /* Ýàâåçéëíðñòô÷úýÞ */
    $"FF03 D362 6364 FE65 FE64 1E63 6260 5E5D"            /* ÿ.Óbcdþeþd.cb`^] */
    $"5B59 5539 130A 0B09 0F3F 574D 4946 4443"            /* [YU9...Æ.?WMIFDC */
    $"4241 3F3C 3A37 3532 2F2D 092A 2623 201D"            /* BA?<:752/-Æ*&# . */
    $"1C19 0E2C E5BE FF0D 9F03 090C 0C12 1D0E"            /* ...,å¾ÿÂ.Æ..... */
    $"0709 090A 0B0B FE0D 210E 0927 9AA1 A3A6"            /* .ÆÆ...þÂ!.Æ'¡£¦ */
    $"ABAD AFB3 B5B7 B9BC BFC1 C3C5 C8CA CBCD"            /* «­¯³µ·¹¼¿ÁÃÅÈÊËÍ */
    $"D0D3 D4D6 D8DA DDE0 E2E5 E709 E9EB EDF0"            /* ÐÓÔÖØÚÝàâåçÆéëíð */
    $"F1F2 F4F7 FAFD DEFF 03D3 6263 64FE 65FE"            /* ñòô÷úýÞÿ.Óbcdþeþ */
    $"6428 6362 605E 5D5B 5955 3913 0A0B 090F"            /* d(cb`^][YU9...Æ. */
    $"3E57 4D49 4644 4342 413F 3C3A 3735 322F"            /* >WMIFDCBA?<:752/ */
    $"2D2A 2623 201D 1C19 0E2C E5E1 FFFF FF01"            /* -*&# ....,åáÿÿÿ. */
    $"67E1 FF07 D41B 040C 0D11 1B10 FE08 0309"            /* gáÿ.Ô...Â...þ..Æ */
    $"0A0B 0BFD 0D2A 0961 A3A1 A3A7 ABAE B0B3"            /* ...ýÂ*Æa£¡£§«®°³ */
    $"B5B8 BABD BFC1 C3C5 C8CA CBCE D0D3 D4D6"            /* µ¸º½¿ÁÃÅÈÊËÎÐÓÔÖ */
    $"D9DB DDE0 E3E5 E7E9 EBEE F0F1 F2F4 F7FA"            /* ÙÛÝàãåçéëîðñòô÷ú */
    $"FDDF FF04 FFF9 7960 64FD 65FF 6428 6362"            /* ýßÿ.ÿùy`dýeÿd(cb */
    $"605E 5D5C 5958 4A24 0B0B 0A09 1648 554C"            /* `^]\YXJ$...Æ.HUL */
    $"4846 4443 4242 3E3B 3937 3431 2F2C 2825"            /* HFDCBB>;9741/,(% */
    $"2220 1D1A 1908 68BF FF09 D41B 040C 0D11"            /* " ....h¿ÿÆÔ...Â. */
    $"1B11 0808 0408 090A 0B0B FD0D 2A09 61A3"            /* ......Æ...ýÂ*Æa£ */
    $"A1A3 A7AB AEB0 B3B5 B8BA BDBF C1C3 C5C8"            /* ¡£§«®°³µ¸º½¿ÁÃÅÈ */
    $"CACB CED0 D3D4 D6D9 DBDD E0E3 E5E7 E9EB"            /* ÊËÎÐÓÔÖÙÛÝàãåçéë */
    $"EEF0 F1F2 F4F7 FAFD DEFF 03F9 7960 64FD"            /* îðñòô÷úýÞÿ.ùy`dý */
    $"65FF 641E 6362 605E 5D5C 5957 4A24 0C0B"            /* eÿd.cb`^]\YWJ$.. */
    $"0A08 1548 554C 4846 4443 4242 3E3B 3937"            /* ...HULHFDCBB>;97 */
    $"3431 2F09 2C28 2522 201D 1A19 0868 BFFF"            /* 41/Æ,(%" ....h¿ÿ */
    $"0ED4 1B04 0C0D 111C 1007 0808 090A 0B0B"            /* .Ô...Â......Æ... */
    $"FD0D 2009 61A3 A1A3 A7AB AEB0 B3B5 B8BA"            /* ýÂ Æa£¡£§«®°³µ¸º */
    $"BDBF C1C3 C5C8 CACB CED0 D3D4 D6D9 DBDD"            /* ½¿ÁÃÅÈÊËÎÐÓÔÖÙÛÝ */
    $"E0E3 E5E7 09E9 EBEE F0F1 F2F4 F7FA FDDE"            /* àãåçÆéëîðñòô÷úýÞ */
    $"FF03 F979 6064 FD65 FF64 2863 6260 5E5D"            /* ÿ.ùy`dýeÿd(cb`^] */
    $"5C59 574A 240C 0B0A 0816 4955 4C48 4644"            /* \YWJ$.....IULHFD */
    $"4342 423E 3B39 3734 312F 2C28 2522 201D"            /* CBB>;9741/,(%" . */
    $"1A19 0868 E1FF FFFF 0168 E2FF 3EF8 4400"            /* ...háÿÿÿ.hâÿ>øD. */
    $"0C0D 0F1A 1308 0908 0809 0A0B 0B0D 0D0E"            /* .Â....Æ..Æ...ÂÂ. */
    $"0829 989F A1A5 A7AB AEB1 B3B5 B8BB BDC0"            /* .)¡¥§«®±³µ¸»½À */
    $"C2C4 C5C8 CACD CED0 D3D5 D7D9 DCDD E0E3"            /* ÂÄÅÈÊÍÎÐÓÕ×ÙÜÝàã */
    $"E5E7 EAEC EEF1 F2F2 F5F8 FAFD DFFF FFFF"            /* åçêìîñòòõøúýßÿÿÿ */
    $"019B 5BFB 650B 6463 6261 5F5E 5C5A 5853"            /* .[ûe.dcba_^\ZXS */
    $"3814 FE0A 1B08 2453 524B 4745 4443 4241"            /* 8.þ...$SRKGEDCBA */
    $"3D3A 3836 3330 2C29 2623 211E 1B1A 1515"            /* =:8630,)&#!..... */
    $"BAC1 FF0A F844 000C 0D0F 1A13 0809 0833"            /* ºÁÿ.øD..Â....Æ.3 */
    $"0809 0A0B 0B0D 0D0E 0829 989F A1A5 A7AB"            /* .Æ...ÂÂ..)¡¥§« */
    $"AEB1 B3B5 B8BB BDC0 C2C4 C5C8 CACD CED0"            /* ®±³µ¸»½ÀÂÄÅÈÊÍÎÐ */
    $"D3D5 D7D9 DCDD E0E3 E5E7 EAEC EEF1 F2F2"            /* ÓÕ×ÙÜÝàãåçêìîñòò */
    $"F5F8 FAFD DDFF 019B 5BFB 650B 6463 6261"            /* õøúýÝÿ.[ûe.dcba */
    $"5F5E 5C5A 5852 3714 FE0A 1008 2353 524B"            /* _^\ZXR7.þ...#SRK */
    $"4745 4443 4241 3D3A 3836 3330 0A2C 2926"            /* GEDCBA=:8630.,)& */
    $"2321 1E1B 1A15 15BA C1FF 34F8 4400 0C0D"            /* #!.....ºÁÿ4øD..Â */
    $"101B 1308 0908 0809 0A0B 0B0D 0D0E 0829"            /* ....Æ..Æ...ÂÂ..) */
    $"989F A1A5 A7AB AEB1 B3B5 B8BB BDC0 C2C4"            /* ¡¥§«®±³µ¸»½ÀÂÄ */
    $"C5C8 CACD CED0 D3D5 D7D9 DCDD E0E3 E5E7"            /* ÅÈÊÍÎÐÓÕ×ÙÜÝàãåç */
    $"09EA ECEE F1F2 F2F5 F8FA FDDD FF01 9B5B"            /* ÆêìîñòòõøúýÝÿ.[ */
    $"FB65 0B64 6362 615F 5E5C 5A58 5338 14FE"            /* ûe.dcba_^\ZXS8.þ */
    $"0A1B 0824 5352 4B47 4544 4342 413D 3A38"            /* ...$SRKGEDCBA=:8 */
    $"3633 302C 2926 2321 1E1B 1A15 15BA E2FF"            /* 630,)&#!.....ºâÿ */
    $"FFFF 0174 E2FF 0D7A 000B 0C0D 1816 0909"            /* ÿÿ.tâÿÂz...Â..ÆÆ */
    $"0808 090A 0BFE 0CFF 0D2B 0A65 A19E A2A6"            /* ..Æ..þ.ÿÂ+.e¡¢¦ */
    $"A9AB AFB2 B4B6 B8BB BDC0 C2C4 C6C8 CACD"            /* ©«¯²´¶¸»½ÀÂÄÆÈÊÍ */
    $"CED1 D4D5 D7D9 DCDD E1E3 E5E7 EAEC EEF1"            /* ÎÑÔÕ×ÙÜÝáãåçêìîñ */
    $"F2F3 F5F8 FAFD DFFF FFFF 02D8 6763 FE66"            /* òóõøúýßÿÿÿ.Øgcþf */
    $"FF65 2B64 6362 615F 5E5C 5A58 5547 240C"            /* ÿe+dcba_^\ZXUG$. */
    $"0B0B 090B 3156 514A 4744 4343 423E 3C3A"            /* ..Æ.1VQJGDCCB><: */
    $"3735 312F 2B28 2522 1F1C 1A19 0D41 F6C2"            /* 751/+(%"....ÂAöÂ */
    $"FF0A 7A00 0B0C 0D18 1708 0908 0802 090A"            /* ÿ.z...Â...Æ...Æ. */
    $"0BFE 0CFF 0D2B 0A65 A19E A2A6 A9AB AFB2"            /* .þ.ÿÂ+.e¡¢¦©«¯² */
    $"B4B6 B8BB BDC0 C2C4 C6C8 CACD CED1 D4D5"            /* ´¶¸»½ÀÂÄÆÈÊÍÎÑÔÕ */
    $"D7D9 DCDD E1E3 E5E7 EAEC EEF1 F2F3 F5F8"            /* ×ÙÜÝáãåçêìîñòóõø */
    $"FAFD DDFF 02D8 6763 FE66 FF65 1F64 6362"            /* úýÝÿ.Øgcþfÿe.dcb */
    $"615F 5E5C 5A58 5547 240D 0B0B 090B 3156"            /* a_^\ZXUG$Â..Æ.1V */
    $"514A 4744 4343 423E 3C3A 3735 310B 2F2B"            /* QJGDCCB><:751./+ */
    $"2825 221F 1C1A 190D 41F6 C2FF 0D7A 000B"            /* (%"....ÂAöÂÿÂz.. */
    $"0C0D 1816 0909 0808 090A 0BFE 0CFF 0D21"            /* .Â..ÆÆ..Æ..þ.ÿÂ! */
    $"0A65 A19E A2A6 A9AB AFB2 B4B6 B8BB BDC0"            /* .e¡¢¦©«¯²´¶¸»½À */
    $"C2C4 C6C8 CACD CED1 D4D5 D7D9 DCDD E1E3"            /* ÂÄÆÈÊÍÎÑÔÕ×ÙÜÝáã */
    $"E5E7 09EA ECEE F1F2 F3F5 F8FA FDDD FF02"            /* åçÆêìîñòóõøúýÝÿ. */
    $"D867 63FE 66FF 652B 6463 6261 5F5E 5C5A"            /* Øgcþfÿe+dcba_^\Z */
    $"5855 4823 0C0B 0B09 0C31 5651 4A47 4443"            /* XUH#...Æ.1VQJGDC */
    $"4342 3E3C 3A37 3531 2F2B 2825 221F 1C1A"            /* CB><:751/+(%"... */
    $"190D 41F6 E3FF FFFF 016A E3FF 06D5 1107"            /* .ÂAöãÿÿÿ.jãÿ.Õ.. */
    $"0C0D 1418 FE09 FF08 FF0A 010B 0CFE 0D2B"            /* .Â..þÆÿ.ÿ....þÂ+ */
    $"082C 989D A0A3 A5A9 ADB0 B1B4 B7BA BCBE"            /* ., £¥©­°±´·º¼¾ */
    $"C1C3 C5C6 C9CB CDCE D1D4 D6D8 D9DB DEE1"            /* ÁÃÅÆÉËÍÎÑÔÖØÙÛÞá */
    $"E4E5 E7EB EDEF F2F3 F5F7 FAFD DEFF FEFF"            /* äåçëíïòóõ÷úýÞÿþÿ */
    $"019A 5EFC 662B 6564 6361 605E 5D5B 5856"            /* .^üf+edca`^][XV */
    $"4F36 130B 0B0A 0910 3C57 4F49 4645 4442"            /* O6....Æ.<WOIFEDB */
    $"403E 3B3A 3734 322E 2B28 2521 1F1C 1A18"            /* @>;:742.+(%!.... */
    $"0A84 C3FF 06D5 1107 0C0D 1518 FE09 FF08"            /* .Ãÿ.Õ...Â..þÆÿ. */
    $"FF0A 010B 0CFE 0D2B 082C 989D A0A3 A5A9"            /* ÿ....þÂ+., £¥© */
    $"ADB0 B1B4 B7BA BCBE C1C3 C5C6 C9CB CDCE"            /* ­°±´·º¼¾ÁÃÅÆÉËÍÎ */
    $"D1D4 D6D8 D9DB DEE1 E4E5 E7EB EDEF F2F3"            /* ÑÔÖØÙÛÞáäåçëíïòó */
    $"F5F7 FAFD DBFF 019A 5EFC 661F 6564 6361"            /* õ÷úýÛÿ.^üf.edca */
    $"605E 5D5B 5856 4F36 130B 0B0A 090F 3B57"            /* `^][XVO6....Æ.;W */
    $"4F49 4645 4442 403E 3B3A 3734 0B32 2E2B"            /* OIFEDB@>;:74.2.+ */
    $"2825 211F 1C1A 180A 84C3 FF06 D511 070C"            /* (%!.....Ãÿ.Õ... */
    $"0D15 18FE 09FF 08FF 0A01 0B0C FE0D 2208"            /* Â..þÆÿ.ÿ....þÂ". */
    $"2C98 9DA0 A3A5 A9AD B0B1 B4B7 BABC BEC1"            /* , £¥©­°±´·º¼¾Á */
    $"C3C5 C6C9 CBCD CED1 D4D6 D8D9 DBDE E1E4"            /* ÃÅÆÉËÍÎÑÔÖØÙÛÞáä */
    $"E5E7 08EB EDEF F2F3 F5F7 FBFD DBFF 019A"            /* åç.ëíïòóõ÷ûýÛÿ. */
    $"5EFC 662B 6564 6361 605E 5D5B 5856 4F35"            /* ^üf+edca`^][XVO5 */
    $"130B 0B0A 090F 3B56 4F49 4645 4442 403E"            /* ....Æ.;VOIFEDB@> */
    $"3B3A 3734 322E 2B28 2521 1F1C 1A18 0A84"            /* ;:742.+(%!..... */
    $"E3FF FFFF 01A3 E4FF 38ED 3902 0C0C 131A"            /* ãÿÿÿ.£äÿ8í9..... */
    $"0B09 0B0A 0808 0A0A 0B0C 0D0D 0B0F 759E"            /* .Æ........ÂÂ..u */
    $"9CA0 A2A6 AAAD B0B1 B4B7 BABC BEC1 C3C5"            /*  ¢¦ª­°±´·º¼¾ÁÃÅ */
    $"C6C9 CBCE D0D3 D6D9 DBDD E1E6 EBED F2F6"            /* ÆÉËÎÐÓÖÙÛÝáæëíòö */
    $"F4F5 FEF4 07F0 F1EF F1F2 F3F1 EEFB EDFF"            /* ôõþô.ðñïñòóñîûíÿ */
    $"ECFF ED07 F2F4 F5F6 F8FC FCFE F4FF FEFF"            /* ìÿí.òôõöøüüþôÿþÿ */
    $"02F0 7C61 FD66 2C65 6463 6260 5F5D 5B58"            /* .ð|aýf,edcb`_][X */
    $"5653 4521 0D0B 0A0A 0912 4058 4E48 4644"            /* VSE!Â...Æ.@XNHFD */
    $"4342 403D 3A39 3634 302D 2A27 2321 1E1B"            /* CB@=:9640-*'#!.. */
    $"1912 21DB C5FF 0CED 3902 0C0C 131A 0B09"            /* ..!ÛÅÿ.í9......Æ */
    $"0B0A 0808 FF0A 340B 0C0D 0D0B 0F75 9E9C"            /* ....ÿ.4..ÂÂ..u */
    $"A0A2 A6AA ADB0 B1B4 B7BA BCBE C1C3 C5C6"            /*  ¢¦ª­°±´·º¼¾ÁÃÅÆ */
    $"C9CB CED0 D3D6 D9DB DDE2 E7EB EDF3 F7F5"            /* ÉËÎÐÓÖÙÛÝâçëíó÷õ */
    $"F6F4 F4F5 F2F2 F1F3 F5F5 F4F0 F7EF 07F4"            /* öôôõòòñóõõôð÷ï.ô */
    $"F6F7 F7FA FDFD FEF1 FF02 F07C 61FD 661F"            /* ö÷÷úýýþñÿ.ð|aýf. */
    $"6564 6362 605F 5D5B 5856 5345 210E 0B0A"            /* edcb`_][XVSE!... */
    $"0A09 1241 584E 4846 4443 4240 3D3A 3936"            /* .Æ.AXNHFDCB@=:96 */
    $"0C34 302D 2A27 2321 1E1B 1912 21DB C5FF"            /* .40-*'#!....!ÛÅÿ */
    $"36ED 3902 0C0C 131A 0B09 0B0A 0808 0A0A"            /* 6í9......Æ...... */
    $"0B0C 0D0D 0B0F 759E 9CA0 A2A6 AAAD B0B1"            /* ..ÂÂ..u ¢¦ª­°± */
    $"B4B7 BABC BEC1 C3C5 C6C9 CBCE D0D3 D6D9"            /* ´·º¼¾ÁÃÅÆÉËÎÐÓÖÙ */
    $"DBDD E2E7 EBEE F3F7 08F6 F7F5 F6F6 F3F4"            /* ÛÝâçëîó÷.ö÷õööóô */
    $"F2F5 FEF7 00F3 F7F2 05F7 F8F8 F9FC FEEF"            /* òõþ÷.ó÷ò.÷øøùüþï */
    $"FF02 F07C 61FD 662C 6564 6362 605F 5D5B"            /* ÿ.ð|aýf,edcb`_][ */
    $"5856 5345 210D 0B0A 0A08 1240 584E 4846"            /* XVSE!Â.....@XNHF */
    $"4443 4240 3D3A 3936 3430 2D2A 2723 211E"            /* DCB@=:9640-*'#!. */
    $"1B19 1221 DBE4 FFFF FF01 B6E4 FF48 7300"            /* ...!Ûäÿÿÿ.¶äÿHs. */
    $"0B0D 111A 0D08 0A0B 0A08 080A 0A0B 0C0D"            /* .Â..Â..........Â */
    $"0D06 439C 9B9D A1A3 A7AA ADB0 B3B5 B7BA"            /* Â.C¡£§ª­°³µ·º */
    $"BDC0 C3C5 C8CD D3D6 D4D2 CFCB C7C5 C3B1"            /* ½ÀÃÅÈÍÓÖÔÒÏËÇÅÃ± */
    $"A195 9985 8077 776F 7076 6B77 6E6E 7B85"            /* ¡wwopvkwnn{ */
    $"8F83 8284 8586 87FE 890A 8C8D 8E88 7E80"            /* þ.~ */
    $"8986 8171 C0F5 FFFD FF01 B860 FD66 0E65"            /* qÀõÿýÿ.¸`ýf.e */
    $"6463 6261 605D 5A58 5654 4C30 140B FE0A"            /* dcba`]ZXVTL0..þ. */
    $"1A08 184A 574C 4745 4443 423F 3C3A 3835"            /* ...JWLGEDCB?<:85 */
    $"322F 2C29 2623 1F1D 1A18 0B6B C5FF 0C73"            /* 2/,)&#.....kÅÿ.s */
    $"000B 0D11 1A0D 080A 0B0A 0808 FF0A 470B"            /* ..Â..Â......ÿ.G. */
    $"0C0D 0D06 439C 9B9D A1A3 A7AA ADB0 B3B5"            /* .ÂÂ.C¡£§ª­°³µ */
    $"B7BA BDC0 C3C5 C8CD D3D6 D4D3 D1CD CBC9"            /* ·º½ÀÃÅÈÍÓÖÔÓÑÍËÉ */
    $"C7B4 A396 9A85 7D75 756C 6C70 646C 6262"            /* Ç´£}uullpdlbb */
    $"6B74 7C70 6E70 7172 7375 7475 777A 7D79"            /* kt|pnpqrsutuwz}y */
    $"7274 7D7D 7A6C BFF1 FF01 B860 FD66 0E65"            /* rt}}zl¿ñÿ.¸`ýf.e */
    $"6463 6261 605D 5A58 5654 4D30 140B FE0A"            /* dcba`]ZXVTM0..þ. */
    $"0D07 174A 574C 4745 4443 423F 3C3A 380C"            /* Â..JWLGEDCB?<:8. */
    $"3532 2F2C 2926 231F 1D1A 180B 6BC5 FF36"            /* 52/,)&#.....kÅÿ6 */
    $"7300 0B0D 111A 0E08 0A0B 0A08 080A 0A0B"            /* s..Â............ */
    $"0C0D 0D06 439C 9B9D A1A3 A7AA ADB0 B3B5"            /* .ÂÂ.C¡£§ª­°³µ */
    $"B7BA BDC0 C3C5 C8CE D3D7 D5D3 D1CE CCCA"            /* ·º½ÀÃÅÈÎÓ×ÕÓÑÎÌÊ */
    $"C8B5 A395 9984 7D11 7372 6A68 685C 6257"            /* Èµ£}.srjhh\bW */
    $"565D 6367 5B59 5A5C 5D5E FE5F 0A61 636B"            /* V]cg[YZ\]^þ_.ack */
    $"6A66 6871 7472 68BE F1FF 01B8 60FD 660E"            /* jfhqtrh¾ñÿ.¸`ýf. */
    $"6564 6362 6160 5D5A 5856 544D 3015 0BFE"            /* edcba`]ZXVTM0..þ */
    $"0A1A 0818 4B56 4C47 4544 4342 3F3C 3A38"            /* ....KVLGEDCB?<:8 */
    $"3532 2F2C 2926 231F 1D1A 180B 6BE4 FFFF"            /* 52/,)&#.....käÿÿ */
    $"FF01 BCE5 FF57 B303 080C 0F1A 1008 0A0A"            /* ÿ.¼åÿW³......... */
    $"0908 0809 0A0B 0C0C 0D09 1E89 9A9A 9EA2"            /* Æ..Æ....ÂÆ.¢ */
    $"A4A8 ABAE B1B5 BAC0 C5C1 BCB8 B6AE 947D"            /* ¤¨«®±µºÀÅÁ¼¸¶®} */
    $"695F 5D5D 646A 6E78 7E83 838B 8B58 90A9"            /* i_]]djnx~X© */
    $"ADB0 BABE C9D0 D2D7 DCE2 E4E7 E9EC EDF0"            /* ­°º¾ÉÐÒ×Üâäçéìíð */
    $"F2F3 F4F7 F9F5 F5F2 F2EB E5EE 8B82 F5FF"            /* òóô÷ùõõòòëåîõÿ */
    $"FDFF 03F8 8661 67FE 660D 6564 6260 5F5E"            /* ýÿ.øagþfÂedb`_^ */
    $"5C59 5754 503C 1F0D FD0A 1A08 1F54 524A"            /* \YWTP<.Âý....TRJ */
    $"4745 4443 413D 3C39 3734 312E 2B28 2521"            /* GEDCA=<9741.+(%! */
    $"1E1C 1A15 10BD C7FF 0DB3 0308 0C0F 1A0F"            /* .....½ÇÿÂ³...... */
    $"080A 0A09 0808 091E 0A0B 0C0C 0D09 1E89"            /* ...Æ..Æ.....ÂÆ. */
    $"9A9A 9EA2 A4A8 ABAE B1B5 BAC1 C5C2 BEBB"            /* ¢¤¨«®±µºÁÅÂ¾» */
    $"B9B1 967E 685D 57FE 5227 5053 5556 5459"            /* ¹±~h]WþR'PSUVTY */
    $"563B 7082 8689 9094 9CA2 A4A8 ADB1 B4B6"            /* V;p¢¤¨­±´¶ */
    $"B8BA BCBE BFC0 C2C5 C6C3 C4C3 C4C0 BCC6"            /* ¸º¼¾¿ÀÂÅÆÃÄÃÄÀ¼Æ */
    $"7281 F1FF 03F8 8661 67FE 660D 6564 6260"            /* rñÿ.øagþfÂedb` */
    $"5F5E 5C59 5754 503D 1F0E FD0A 0C08 2054"            /* _^\YWTP=..ý... T */
    $"524A 4745 4443 413D 3C39 0D37 3431 2E2B"            /* RJGEDCA=<9Â741.+ */
    $"2825 211E 1C1A 1510 BDC7 FF2F B303 080C"            /* (%!.....½Çÿ/³... */
    $"0F1A 0F08 0A0A 0908 0809 0A0B 0C0C 0D09"            /* ......Æ..Æ....ÂÆ */
    $"1E89 9A9A 9EA2 A4A8 ABAE B1B5 BAC1 C6C2"            /* .¢¤¨«®±µºÁÆÂ */
    $"BFBB B9B2 977D 685C 554E 4B48 FE46 0444"            /* ¿»¹²}h\UNKHþF.D */
    $"4348 4328 1641 4D51 5256 5B60 6465 676C"            /* CHC(.AMQRV[`degl */
    $"6F72 7376 7576 797B 7B7D 7D80 FD7F 047E"            /* orsvuvy{{}}ý..~ */
    $"7B83 4D81 F1FF 03F8 8661 67FE 660E 6564"            /* {Mñÿ.øagþf.ed */
    $"6260 5F5E 5C59 5754 503C 1F0D 09FE 0A1A"            /* b`_^\YWTP<.ÂÆþ.. */
    $"071F 5452 4A47 4544 4341 3D3C 3937 3431"            /* ..TRJGEDCA=<9741 */
    $"2E2B 2825 211E 1C1A 1510 BDE5 FFFF FF01"            /* .+(%!.....½åÿÿÿ. */
    $"B9E6 FF3B E328 020C 0D19 1308 080B 0C09"            /* ¹æÿ;ã(..Â......Æ */
    $"0809 090B 0B0C 0D0D 0756 9B98 9B9F A1A5"            /* .ÆÆ...ÂÂ.V¡¥ */
    $"A9AB B3AF A598 7A61 5655 5C66 6C72 7981"            /* ©«³¯¥zaVU\flry */
    $"8E9B A8B5 BCC3 CAD1 D6DC E1D2 7BDF E4E6"            /* ¨µ¼ÃÊÑÖÜáÒ{ßäæ */
    $"FEE8 11E6 E5E3 E3E4 E7E9 EBEC EEF0 F3F6"            /* þè.æåããäçéëìîðóö */
    $"F7F7 F9FC FEFB FF01 B278 F5FF FCFF 01BA"            /* ÷÷ùüþûÿ.²xõÿüÿ.º */
    $"5EFE 670E 6665 6462 6160 5E5C 5957 5552"            /* ^þg.fedba`^\YWUR */
    $"462B 13FC 0A1A 082C 5A50 4946 4443 4341"            /* F+.ü...,ZPIFDCCA */
    $"3D3A 3835 3330 2D2A 2622 1F1D 1B19 0E41"            /* =:8530-*&".....A */
    $"F4C9 FF0E E328 020C 0D19 1307 090B 0C09"            /* ôÉÿ.ã(..Â...Æ..Æ */
    $"0809 09FF 0B16 0C0D 0D07 569B 989B 9FA1"            /* .ÆÆÿ...ÂÂ.V¡ */
    $"A5A9 ABB3 B1A9 9B7B 6052 4A4A 4BFE 4A2D"            /* ¥©«³±©{`RJJKþJ- */
    $"4E57 6069 7377 7C82 878A 8F92 875C B0B3"            /* NW`isw|\°³ */
    $"B4B7 B7B8 B6B5 B4B5 B6B7 BABB BDBE C1C3"            /* ´··¸¶µ´µ¶·º»½¾ÁÃ */
    $"C5C7 C7C8 CACC D0D1 D2D6 D9E2 9576 F0FF"            /* ÅÇÇÈÊÌÐÑÒÖÙâvðÿ */
    $"01BA 5EFE 670E 6665 6462 6160 5E5C 5957"            /* .º^þg.fedba`^\YW */
    $"5552 462B 12FD 0A0C 0908 2D5A 5049 4644"            /* URF+.ý..Æ.-ZPIFD */
    $"4343 413D 3A0E 3835 3330 2D2A 2622 1F1D"            /* CCA=:.8530-*&".. */
    $"1B19 0E41 F4C9 FF38 E328 020C 0D19 1207"            /* ...AôÉÿ8ã(..Â... */
    $"090B 0C09 0809 090B 0B0C 0D0D 0756 9B98"            /* Æ..Æ.ÆÆ...ÂÂ.V */
    $"9B9F A1A5 A9AB B3B2 AA9C 7A5F 5147 4342"            /* ¡¥©«³²ªz_QGCB */
    $"3E3C 3B3C 434B 5259 5F63 686C 6E72 756E"            /* ><;<CKRY_chlnrun */
    $"4101 6E70 FE72 1174 7274 7270 7378 7A7D"            /* A.npþr.trtrpsxz} */
    $"7E7A 7A7E 8484 8281 85FD 8904 8D91 9666"            /* ~zz~ý.f */
    $"76F0 FF01 BA5E FE67 0E66 6564 6261 605E"            /* vðÿ.º^þg.fedba`^ */
    $"5C59 5755 5145 2A12 FC0A 1A08 2D5A 5049"            /* \YWUQE*.ü...-ZPI */
    $"4644 4343 413D 3A38 3533 302D 2A26 221F"            /* FDCCA=:8530-*&". */
    $"1D1B 190E 41F4 E6FF FFFF 01C2 E7FF 52F8"            /* ....Aôæÿÿÿ.ÂçÿRø */
    $"5600 0C0D 1614 0908 090B 0C0A 0809 090B"            /* V..Â..Æ.Æ....ÆÆ. */
    $"0B0C 0D08 2E90 9799 9CA0 A4A7 A9B1 8262"            /* ..Â.. ¤§©±b */
    $"6466 6A74 8797 A5AE B5B9 BBBB BDBE BEBF"            /* dfjt¥®µ¹»»½¾¾¿ */
    $"C5CB C9B7 9B86 7B64 366A 6670 8395 9BAF"            /* ÅËÉ·{d6jfp¯ */
    $"C4E2 EEEA E7E8 EAEC EDEF F2F5 F7F7 F8FB"            /* Äâîêçèêìíïòõ÷÷øû */
    $"FDFE FCFF 02C6 6AFE F6FF FCFF 14F1 8463"            /* ýþüÿ.Æjþöÿüÿ.ñc */
    $"6767 6665 6463 6161 5E5C 5A58 5553 4C38"            /* ggfedcaa^\ZXUSL8 */
    $"1D0C FD0A 1A09 0C40 5B4E 4946 4543 433F"            /* ..ý..Æ.@[NIFECC? */
    $"3C3A 3835 3330 2D28 2523 1F1D 1A17 098C"            /* <:8530-(%#....Æ */
    $"CAFF 0FF8 5600 0C0E 1614 0808 090B 0C0A"            /* Êÿ.øV.......Æ... */
    $"0809 09FF 0B48 0C0D 082E 9097 999C A0A4"            /* .ÆÆÿ.H.Â.. ¤ */
    $"A7A9 B181 5148 4442 4653 5E67 6E73 777A"            /* §©±QHDBFS^gnswz */
    $"7A7B 7C7C 7D80 8382 7765 5851 412B 5352"            /* z{||}weXQA+SR */
    $"5969 777C 8B9B B3BD BAB7 B8BB BCBE C0C2"            /* Yiw|³½º·¸»¼¾ÀÂ */
    $"C5C6 C6C7 CACC CDD0 D1D3 D5DD A466 FEF1"            /* ÅÆÆÇÊÌÍÐÑÓÕÝ¤fþñ */
    $"FF14 F184 6367 6766 6564 6361 615E 5C5A"            /* ÿ.ñcggfedcaa^\Z */
    $"5855 524C 371C 0CFD 0A0B 090C 3F5A 4E49"            /* XURL7..ý..Æ.?ZNI */
    $"4645 4343 3F3C 0E3A 3835 3330 2D28 2523"            /* FECC?<.:8530-(%# */
    $"1F1D 1A17 098C CAFF 39F8 5600 0C0E 1614"            /* ....ÆÊÿ9øV..... */
    $"0808 090B 0C0A 0809 090B 0B0C 0D08 2E90"            /* ..Æ....ÆÆ...Â.. */
    $"9799 9CA0 A4A7 A9B2 814B 3E38 3435 3F49"            /*  ¤§©²K>845?I */
    $"5157 5A5D 5E5F 6262 6163 6569 6960 5147"            /* QWZ]^_bbaceii`QG */
    $"4237 211F 3736 3B44 4E51 5964 7277 7475"            /* B7!.76;DNQYdrwtu */
    $"797B 7979 7A7D 8185 8280 8486 8687 888B"            /* y{yyz} */
    $"8E94 6F65 F0FF 14F1 8463 6767 6665 6463"            /* oeðÿ.ñcggfedc */
    $"6161 5E5C 5A58 5552 4C37 1C0C FD0A 1A09"            /* aa^\ZXURL7..ý..Æ */
    $"0C3F 5A4E 4946 4543 433F 3C3A 3835 3330"            /* .?ZNIFECC?<:8530 */
    $"2D28 2523 1F1D 1A17 098C E6FF FFFF 01C0"            /* -(%#....Ææÿÿÿ.À */
    $"E7FF 2388 000A 0C13 1508 0809 0A0B 0A09"            /* çÿ#.......Æ...Æ */
    $"0809 090B 0B0C 0C08 689A 9699 9CA0 A4A7"            /* .ÆÆ.....h ¤§ */
    $"ABAC 598B A3A8 AAFE AC2B ADAE B0B1 B3B6"            /* «¬Y£¨ªþ¬+­®°±³¶ */
    $"B7BB C3C4 AD84 5122 0C05 0102 0600 0102"            /* ·»ÃÄ­Q"........ */
    $"060A 0B12 2252 8BC0 E8F1 EBEC EEF0 F2F5"            /* ...."RÀèñëìîðòõ */
    $"F7F7 F8FB FDFE FCFF 02D9 5CF8 F6FF FBFF"            /* ÷÷øûýþüÿ.Ù\øöÿûÿ */
    $"13D3 6766 6766 6565 6361 605E 5C5A 5855"            /* .Ógfgfeeca`^\ZXU */
    $"534F 4228 11FC 0A1A 0810 4B5A 4D49 4643"            /* SOB(.ü....KZMIFC */
    $"4242 3E3B 3937 3532 2F2B 2725 221E 1C1A"            /* BB>;9752/+'%"... */
    $"1318 CECB FF0F 8800 090C 1415 0807 090A"            /* ..ÎËÿ..Æ.....Æ. */
    $"0B0A 0908 0909 FF0B FF0C 1108 689A 9699"            /* ..Æ.ÆÆÿ.ÿ...h */
    $"9CA0 A4A7 ABAE 4A52 666A 6D6E 6FFE 7131"            /*  ¤§«®JRfjmnoþq1 */
    $"7274 7676 7778 7F7F 6F57 3618 0B06 0405"            /* rtvvwx..oW6..... */
    $"0702 0405 070B 0C11 1D41 6F98 B7BF BBBC"            /* .........Ao·¿»¼ */
    $"BEC0 C2C5 C6C6 C8CA CCCD D0D1 D3D5 DCB4"            /* ¾ÀÂÅÆÆÈÊÌÍÐÑÓÕÜ´ */
    $"58F9 F0FF 13D3 6766 6766 6565 6361 605E"            /* Xùðÿ.Ógfgfeeca`^ */
    $"5C5A 5855 534F 4228 11FC 0A0A 0810 4B5A"            /* \ZXUSOB(.ü....KZ */
    $"4D49 4643 4242 3E0F 3B39 3735 322F 2B27"            /* MIFCBB>.;9752/+' */
    $"2522 1E1C 1A13 18CE CBFF 3988 000A 0C12"            /* %".....ÎËÿ9.... */
    $"1508 0809 0A0B 0A09 0809 090B 0B0C 0C08"            /* ...Æ...Æ.ÆÆ..... */
    $"689A 9699 9CA0 A4A7 ABAE 443C 5054 5758"            /* h ¤§«®D<PTWX */
    $"5559 5A59 5B5B 5A5D 5F5F 6565 5845 2C14"            /* UYZY[[Z]__eeXE,. */
    $"0A07 0505 0920 0708 080B 0D0E 1119 2F4B"            /* ....Æ ....Â.../K */
    $"6377 7B78 777A 7B7D 8083 8280 8284 8587"            /* cw{xwz{} */
    $"888A 8E93 7955 F9F0 FF13 D367 6667 6665"            /* yUùðÿ.Ógfgfe */
    $"6563 6160 5E5C 5A58 5553 4F42 2811 FC0A"            /* eca`^\ZXUSOB(.ü. */
    $"1A07 104B 5A4D 4946 4342 423E 3B39 3735"            /* ...KZMIFCBB>;975 */
    $"322F 2B27 2522 1E1C 1A13 18CE E7FF FFFF"            /* 2/+'%".....Îçÿÿÿ */
    $"01BC E8FF 0BC7 0C07 0B10 180B 0708 0A0B"            /* .¼èÿ.Ç.......... */
    $"0AFE 08FF 09FF 0B29 0C07 318F 9496 9A9D"            /* .þ.ÿÆÿ.)..1 */
    $"A1A5 A7AF 935A A3A0 A2A3 A6A8 AAAC AEB0"            /* ¡¥§¯Z£ ¢£¦¨ª¬®° */
    $"B2B4 B7C0 BC96 5418 0200 0307 0909 0B0B"            /* ²´·À¼T.....ÆÆ.. */
    $"0C0D FE0E FE0D 1008 091A 5CBC F1F4 EEF0"            /* .Âþ.þÂ..Æ.\¼ñôîð */
    $"F2F5 F7F7 F9FB FDFE FCFF 02E8 58F2 F6FF"            /* òõ÷÷ùûýþüÿ.èXòöÿ */
    $"FAFF 139B 6168 6766 6564 6261 5F5D 5A58"            /* úÿ.ahgfedba_]ZX */
    $"5653 5049 351B 0CFD 0A1A 0906 1A56 574C"            /* VSPI5..ý..Æ..VWL */
    $"4845 4443 413C 3B38 3633 312D 2926 221F"            /* HEDCA<;8631-)&". */
    $"1D1A 190A 62CC FF0B C70C 070B 1017 0A08"            /* ....bÌÿ.Ç....... */
    $"080A 0B0A FE08 FF09 FF0B 240C 0731 8F94"            /* ....þ.ÿÆÿ.$..1 */
    $"969A 9DA1 A5A7 AF96 3D66 6667 696B 6C6E"            /* ¡¥§¯=ffgikln */
    $"6D6F 7273 7477 7B79 6137 1004 0205 0809"            /* morstw{ya7.....Æ */
    $"FE0B 010C 0DFB 0EFF 0B16 1848 95C0 C3BD"            /* þ...Âû.ÿ...HÀÃ½ */
    $"BFC2 C3C4 C7C8 CACC CDD0 D1D3 D6DB C152"            /* ¿ÂÃÄÇÈÊÌÍÐÑÓÖÛÁR */
    $"F2EF FF13 9B61 6867 6665 6462 615F 5D5A"            /* òïÿ.ahgfedba_]Z */
    $"5856 5350 4835 1B0D FD0A 0A09 061A 5557"            /* XVSPH5.Âý..Æ..UW */
    $"4C48 4544 4341 0F3C 3B38 3633 312D 2926"            /* LHEDCA.<;8631-)& */
    $"221F 1D1A 190A 62CC FF0B C70C 070B 1017"            /* ".....bÌÿ.Ç..... */
    $"0B07 080A 0B0A FE08 FF09 FF0B 130C 0731"            /* ......þ.ÿÆÿ....1 */
    $"8F94 969A 9DA1 A5A7 AF97 3351 5152 5455"            /* ¡¥§¯3QQRTU */
    $"55FE 580D 5B5C 5D5F 6360 4E2D 0E05 0306"            /* UþXÂ[\]_c`N-.... */
    $"0809 FE0B 010C 0DFD 0EFF 0F18 0D0E 1734"            /* .Æþ...Âý.ÿ..Â..4 */
    $"627A 7C7A 7C7E 8283 8180 8284 8687 888B"            /* bz|z|~ */
    $"8E92 834B F3EF FF13 9B61 6867 6665 6462"            /* Kóïÿ.ahgfedb */
    $"615F 5D5A 5856 5350 4835 1B0C FD0A 1A09"            /* a_]ZXVSPH5..ý..Æ */
    $"061A 5657 4C48 4544 4341 3C3B 3836 3331"            /* ..VWLHEDCA<;8631 */
    $"2D29 2622 1F1D 1A19 0A62 E7FF FFFF 01C4"            /* -)&".....bçÿÿÿ.Ä */
    $"E8FF 3755 000C 0E17 0F08 0809 0A0B 0A08"            /* èÿ7U.......Æ.... */
    $"0809 0A0A 0C0C 0A0E 7296 9397 9B9D A1A5"            /* .Æ......r¡¥ */
    $"A8B3 5B67 A4A0 A2A3 A6A8 ABAD AEB0 B2BB"            /* ¨³[g¤ ¢£¦¨«­®°²» */
    $"B98D 4409 0003 0607 0809 0AFE 0B18 0C0D"            /* ¹DÆ.....Æ.þ...Â */
    $"0E0E 0F10 1011 1212 100D 196A CBF9 F4F3"            /* .........Â.jËùôó */
    $"F5F7 F7F9 FBFD FEFC FF02 F464 E2F6 FFFA"            /* õ÷÷ùûýþüÿ.ôdâöÿú */
    $"FF14 E06F 6567 6665 6462 615F 5D5B 5956"            /* ÿ.àoegfedba_][YV */
    $"5350 4C40 2811 09FD 0A1A 0906 295C 524A"            /* SPL@(.Æý..Æ.)\RJ */
    $"4644 4343 403C 3A37 3532 2F2B 2824 211E"            /* FDCC@<:752/+($!. */
    $"1B19 160D B4CD FF10 5500 0C0E 180F 0808"            /* ...Â´Íÿ.U....... */
    $"090A 0B0A 0808 090A 0AFF 0C24 0A0E 7296"            /* Æ.....Æ..ÿ.$..r */
    $"9397 9B9D A1A5 A8B4 5A3E 6865 6869 6C6C"            /* ¡¥¨´Z>hehill */
    $"6D6E 7071 7479 785B 2D07 0104 0607 0809"            /* mnpqtyx[-......Æ */
    $"0AFE 0B20 0C0D 0E0E 0F10 1011 1212 110E"            /* .þ. .Â.......... */
    $"1757 A2C4 C1C1 C4C6 C6C8 CACC CED0 D1D4"            /* .W¢ÄÁÁÄÆÆÈÊÌÎÐÑÔ */
    $"D6DA CC58 E3EF FF14 E06F 6567 6665 6462"            /* ÖÚÌXãïÿ.àoegfedb */
    $"615F 5D5B 5956 5350 4C3F 2711 09FD 0A09"            /* a_][YVSPL?'.Æý.Æ */
    $"0906 285C 524A 4644 4343 1040 3C3A 3735"            /* Æ.(\RJFDCC.@<:75 */
    $"322F 2B28 2421 1E1B 1916 0DB4 CDFF 2155"            /* 2/+($!....Â´Íÿ!U */
    $"000C 0E18 0F07 0809 0A0B 0A08 0809 0A0A"            /* .......Æ.....Æ.. */
    $"0C0C 0A0E 7296 9397 9B9D A1A5 A8B4 5930"            /* ....r¡¥¨´Y0 */
    $"54FE 5312 5456 5658 595A 595F 5F48 2407"            /* TþS.TVVXYZY__H$. */
    $"0205 0607 0809 0AFE 0B0E 0C0D 0E0E 0F10"            /* .....Æ.þ...Â.... */
    $"1011 1213 1311 173E 6BFE 7F0E 8182 8081"            /* .......>kþ.. */
    $"8285 8A8A 8B8F 8D91 8A4A E5EF FF13 E06F"            /* Jåïÿ.ào */
    $"6567 6665 6462 615F 5D5B 5956 5350 4C40"            /* egfedba_][YVSPL@ */
    $"2711 FC0A 1A09 0629 5C52 4A46 4443 4340"            /* '.ü..Æ.)\RJFDCC@ */
    $"3C3A 3735 322F 2B28 2421 1E1B 1916 0DB4"            /* <:752/+($!....Â´ */
    $"E8FF FFFF 01C1 E9FF 08A0 0409 0D16 1108"            /* èÿÿÿ.Áéÿ. .ÆÂ... */
    $"0809 FD0B FF08 2409 0A0A 0C0C 0541 9190"            /* .Æý.ÿ.$Æ.....A */
    $"9498 9B9F A1A6 ABAA 4189 A0A0 A2A4 A7A9"            /* ¡¦«ªA  ¢¤§© */
    $"ABAC AEB3 BA97 4406 0004 0607 FE08 0209"            /* «¬®³ºD.....þ..Æ */
    $"0A0A FE0C 170D 0E0E 0F10 1012 1213 1415"            /* ..þ..Â.......... */
    $"130B 2791 EEFA F4F6 F7F9 FCFD FEFB FF01"            /* ..'îúôö÷ùüýþûÿ. */
    $"75C0 F6FF F9FF 13B2 6068 6766 6463 6160"            /* uÀöÿùÿ.²`hgfdca` */
    $"5E5B 5957 5451 4E47 3419 0BFC 0A1A 0807"            /* ^[YWTQNG4..ü.... */
    $"395D 4F49 4644 4342 3D3B 3A37 3432 2D29"            /* 9]OIFDCB=;:742-) */
    $"2723 201D 1A18 0E41 F1CF FF08 A004 090D"            /* '# ....AñÏÿ. .ÆÂ */
    $"1611 0808 0AFD 0BFF 0802 090A 0AFF 0C1F"            /* .....ý.ÿ..Æ..ÿ.. */
    $"0541 9190 9498 9B9F A1A6 AAAC 3855 6766"            /* .A¡¦ª¬8Ugf */
    $"6869 6B6B 6C6F 6F72 7760 2D05 0005 0607"            /* hikkloorw`-..... */
    $"FE08 0209 0A0A FE0C 1F0D 0E0E 0F10 1012"            /* þ..Æ..þ..Â...... */
    $"1213 1415 140E 2274 BEC8 C4C6 C6C8 CBCC"            /* ......"t¾ÈÄÆÆÈËÌ */
    $"CED0 D2D4 D5D8 D661 C1EE FF13 B260 6867"            /* ÎÐÒÔÕØÖaÁîÿ.²`hg */
    $"6664 6361 605E 5B59 5754 514E 4633 190B"            /* fdca`^[YWTQNF3.. */
    $"FC0A 0808 0739 5D4F 4946 4443 1142 3D3B"            /* ü....9]OIFDC.B=; */
    $"3A37 3432 2D29 2723 201D 1A18 0E41 F1CF"            /* :742-)'# ....AñÏ */
    $"FF08 A004 090C 1612 0808 09FD 0BFF 0824"            /* ÿ. .Æ.....Æý.ÿ.$ */
    $"090A 0A0C 0C05 4191 9094 989B 9FA1 A6AA"            /* Æ.....A¡¦ª */
    $"AC35 4051 5152 5354 5757 5658 5B5E 4C25"            /* ¬5@QQRSTWWVX[^L% */
    $"0602 0506 07FE 0804 090A 0A0C 0C19 0C0D"            /* .....þ..Æ......Â */
    $"0E0E 0F10 1012 1213 1415 1512 1F52 7D84"            /* .............R} */
    $"8281 8384 8284 888C FD8D 0290 4EC2 EEFF"            /* ý.NÂîÿ */
    $"13B2 6068 6766 6463 6160 5E5B 5957 5451"            /* .²`hgfdca`^[YWTQ */
    $"4E46 3319 0BFC 0A1A 0807 395E 4F49 4644"            /* NF3..ü....9^OIFD */
    $"4342 3D3B 3A37 3432 2D29 2723 201D 1A18"            /* CB=;:742-)'# ... */
    $"0E41 F1E9 FFFF FF01 C8EA FF05 DD21 030C"            /* .Añéÿÿÿ.Èêÿ.Ý!.. */
    $"1514 FE08 000A FE0B 230A 0808 090A 0A0C"            /* ..þ...þ.#...Æ... */
    $"0917 7991 9195 989B 9FA2 A7AE 8A55 A19E"            /* Æ.y¢§®U¡ */
    $"A0A2 A4A7 A9AA ACB4 B36C 0E00 03FE 0600"            /*  ¢¤§©ª¬´³l...þ.. */
    $"07FE 0802 090A 0AFE 0C17 0D0E 0F0F 1010"            /* .þ..Æ..þ..Â..... */
    $"1212 1313 1516 1713 0F62 E0FF F7F8 F9FB"            /* .........bàÿ÷øùû */
    $"FDFE FBFF 0183 A2F6 FFF9 FF13 F181 6367"            /* ýþûÿ.¢öÿùÿ.ñcg */
    $"6665 6362 605E 5B59 5754 514E 4A3C 230F"            /* fecb`^[YWTQNJ<#. */
    $"FC0A 1A09 070C 485B 4C48 4643 4240 3C3B"            /* ü..Æ..H[LHFCB@<; */
    $"3937 3430 2D29 2523 1F1C 1917 0A9E D0FF"            /* 9740-)%#.....Ðÿ */
    $"05DD 2103 0C14 14FE 0800 0AFE 0B05 0A08"            /* .Ý!....þ...þ.... */
    $"0809 0A0A 1D0C 0917 7991 9195 989B 9FA2"            /* .Æ....Æ.y¢ */
    $"A7AE 8D38 6665 6767 696A 6B6C 6E73 7345"            /* §®8feggijklnssE */
    $"0900 04FE 0600 07FE 0802 090A 0AFE 0C1F"            /* Æ..þ...þ..Æ..þ.. */
    $"0D0E 0F0F 1010 1212 1313 1516 1714 1151"            /* Â..............Q */
    $"B3CC C5C6 C7CA CCCE D0D2 D4D5 D8DF 6AA1"            /* ³ÌÅÆÇÊÌÎÐÒÔÕØßj¡ */
    $"EEFF 13F1 8163 6766 6563 6260 5E5B 5957"            /* îÿ.ñcgfecb`^[YW */
    $"5451 4E4B 3D23 0FFC 0A08 0907 0C48 5B4C"            /* TQNK=#.ü..Æ..H[L */
    $"4846 4311 4240 3C3B 3937 3430 2D29 2523"            /* HFC.B@<;9740-)%# */
    $"1F1C 1917 0A9E D0FF 05DD 2103 0C14 14FE"            /* .....Ðÿ.Ý!....þ */
    $"0800 0AFE 0B23 0A08 0809 0A0A 0C09 1779"            /* ...þ.#...Æ...Æ.y */
    $"9191 9598 9B9F A2A7 AE8D 2D4F 4F50 5254"            /* ¢§®-OOPRT */
    $"5456 5858 5B5A 3809 0104 FE06 0007 FE08"            /* TVXX[Z8Æ..þ...þ. */
    $"0409 0A0A 0C0C 200C 0D0E 0F0F 1010 1212"            /* .Æ.... .Â....... */
    $"1313 1516 1715 153C 7784 8185 8583 8589"            /* .......<w */
    $"8E8E 8B8C 8E95 4FA2 EEFF 13F1 8163 6766"            /* O¢îÿ.ñcgf */
    $"6563 6260 5E5B 5957 5451 4E4A 3D23 0FFC"            /* ecb`^[YWTQNJ=#.ü */
    $"0A1A 0907 0C49 5A4C 4846 4342 403C 3B39"            /* ..Æ..IZLHFCB@<;9 */
    $"3734 302D 2925 231F 1C19 170A 9EE9 FFFF"            /* 740-)%#.....éÿÿ */
    $"FF01 CDEB FF0D FD46 000B 1316 0908 0809"            /* ÿ.ÍëÿÂýF....Æ..Æ */
    $"0A0B 0B0A FE08 2009 0A0A 0B09 5B91 8E92"            /* ....þ. Æ...Æ[ */
    $"9699 9DA0 A3A7 B04C 6EA2 9EA0 A2A4 A7A9"            /*  £§°Ln¢ ¢¤§© */
    $"ABB6 972E 0001 0505 FE06 0007 FE08 0609"            /* «¶.....þ...þ..Æ */
    $"0A0A 0C0C 0D0E FE0F FF10 FF12 FF13 0C15"            /* ....Â.þ.ÿ.ÿ.ÿ... */
    $"1617 1818 1040 D2FF F9FA FDFE FAFF 0195"            /* .....@Òÿùúýþúÿ. */
    $"8BF6 FFF8 FF13 CE63 6666 6564 6360 5D5B"            /* öÿøÿ.Îcffedc`][ */
    $"5957 5451 4E4B 442F 160B FD0A FF09 1907"            /* YWTQNKD/..ý.ÿÆ.. */
    $"1150 584B 4845 4343 3F3C 3B38 3532 2F2C"            /* .PXKHECC?<;852/, */
    $"2824 201D 1B19 0E3B F6D2 FF0D FD46 000B"            /* ($ ....;öÒÿÂýF.. */
    $"1316 0908 0809 0A0B 0B0A FE08 0209 0A0A"            /* ..Æ..Æ....þ..Æ.. */
    $"0E0B 095B 918E 9296 999D A0A3 A7B0 4B41"            /* ..Æ[ £§°KA */
    $"FE66 0B67 696B 6E70 7661 1E01 0205 05FE"            /* þf.giknpva.....þ */
    $"0600 07FE 0806 090A 0A0C 0C0D 0EFE 0FFF"            /* ...þ..Æ....Â.þ.ÿ */
    $"10FF 12FF 1315 1516 1718 1912 36A5 CEC8"            /* .ÿ.ÿ........6¥ÎÈ */
    $"C8CC CDCE D1D3 D4D5 D7E0 7B89 EDFF 13CE"            /* ÈÌÍÎÑÓÔÕ×à{íÿ.Î */
    $"6366 6665 6463 605D 5B59 5754 514E 4B44"            /* cffedc`][YWTQNKD */
    $"2F17 0CFD 0AFF 0906 0711 5058 4B48 45FF"            /* /..ý.ÿÆ...PXKHEÿ */
    $"4310 3F3C 3B38 3532 2F2C 2824 201D 1B19"            /* C.?<;852/,($ ... */
    $"0E3B F6D2 FF0D FD46 000B 1316 0908 0809"            /* .;öÒÿÂýF....Æ..Æ */
    $"0A0B 0B0A FE08 1309 0A0A 0B09 5B91 8E92"            /* ....þ..Æ...Æ[ */
    $"9699 9DA0 A3A7 B049 3251 4EFE 52FF 5407"            /*  £§°I2QNþRÿT. */
    $"585D 4C18 0103 0505 FE06 0007 FE08 0409"            /* X]L.....þ...þ..Æ */
    $"0A0A 0C0C 010D 0EFE 0FFF 10FF 12FF 1315"            /* .....Â.þ.ÿ.ÿ.ÿ.. */
    $"1516 1718 1915 2C71 8684 8585 868C 8E8C"            /* ......,q */
    $"8C8F 8F96 5689 EDFF 13CE 6366 6665 6463"            /* Víÿ.Îcffedc */
    $"605D 5B59 5754 514E 4B44 2F16 0BFD 0AFF"            /* `][YWTQNKD/..ý.ÿ */
    $"0919 0711 5058 4B48 4543 433F 3C3B 3835"            /* Æ...PXKHECC?<;85 */
    $"322F 2C28 2420 1D1B 190E 3BF6 EAFF FFFF"            /* 2/,($ ....;öêÿÿÿ */
    $"01B3 EBFF 0987 000A 1017 0A08 0809 0AFE"            /* .³ëÿÆ.......Æ.þ */
    $"0B02 0A08 08FD 0A1A 0634 898C 8E92 979A"            /* .....ý...4 */
    $"9DA0 A4AA A440 8F9E 9EA0 A3A4 A6AB B477"            /*  ¤ª¤@ £¤¦«´w */
    $"1300 03FD 05FE 07FB 081A 0908 090B 0D0E"            /* ...ý.þ.û..Æ.Æ.Â. */
    $"0F10 1012 1213 1515 1217 191A 1A11 33CB"            /* ..............3Ë */
    $"FFFD FFFE FEFB FF01 A77D F6FF F7FF 129B"            /* ÿýÿþþûÿ.§}öÿ÷ÿ. */
    $"5F66 6563 6261 5F5C 5A58 5552 4F4C 4838"            /* _fecba_\ZXUROLH8 */
    $"1F0E FD0A FE09 1805 2760 524A 4745 4342"            /* ..ý.þÆ..'`RJGECB */
    $"3E3B 3A37 3432 2E2B 2722 1F1C 1A17 0A89"            /* >;:742.+'"..... */
    $"D2FF 0987 0009 1018 0A08 0809 0AFE 0B02"            /* ÒÿÆ.Æ.....Æ.þ.. */
    $"0A08 08FD 0A1A 0634 898C 8E92 979A 9DA0"            /* ...ý...4  */
    $"A4A9 A634 5866 6767 696A 6B6D 744D 0D00"            /* ¤©¦4XfggijkmtMÂ. */
    $"03FD 05FE 07FC 08FE 0920 0B0C 0D0E 0F10"            /* .ý.þ.ü.þÆ ..Â... */
    $"1012 1213 1515 1217 191A 1A14 2CA3 D0CE"            /* ............,£ÐÎ */
    $"D2D0 CED1 D2D4 D6D8 E18C 7BEC FF12 9B5F"            /* ÒÐÎÑÒÔÖØá{ìÿ._ */
    $"6665 6362 615F 5C5A 5855 524F 4C48 381F"            /* fecba_\ZXUROLH8. */
    $"0FFD 0AFE 0905 0526 5F52 4A47 1245 4342"            /* .ý.þÆ..&_RJG.ECB */
    $"3E3B 3A37 3432 2E2B 2722 1F1C 1A17 0A89"            /* >;:742.+'"..... */
    $"D2FF 0987 000A 1017 0A08 0809 0AFE 0B02"            /* ÒÿÆ.......Æ.þ.. */
    $"0A08 08FD 0A1A 0634 898C 8E92 979A 9DA0"            /* ...ý...4  */
    $"A4AA A630 454F 4E50 5354 5256 5B3C 0B00"            /* ¤ª¦0EONPSTRV[<.. */
    $"03FD 05FE 07FD 08FF 09FF 0A20 0B0D 0E0F"            /* .ý.þ.ý.ÿÆÿ. .Â.. */
    $"0F10 1012 1213 1514 1217 1919 1B17 276F"            /* ..............'o */
    $"8988 8A89 8B8B 898D 9291 9862 7BEC FF12"            /* b{ìÿ. */
    $"9B5F 6665 6362 615F 5C5A 5855 524F 4C48"            /* _fecba_\ZXUROLH */
    $"381F 0EFD 0AFE 0918 0526 6052 4A47 4543"            /* 8..ý.þÆ..&`RJGEC */
    $"423E 3B3A 3734 322E 2B27 221F 1C1A 170A"            /* B>;:742.+'"..... */
    $"89EA FFFF FF01 C1EC FF0A D316 050D 160D"            /* êÿÿÿ.Áìÿ.Ó..Â.Â */
    $"0708 0809 0AFE 0B20 0A08 080A 0A0B 0A0E"            /* ...Æ.þ. ........ */
    $"6D8D 8C8F 9397 9A9E A1A4 AE7D 55A0 9C9F"            /* m¡¤®}U  */
    $"A0A3 A5A9 AD5F 0800 04FC 05FD 07FF 0119"            /*  £¥©­_...ü.ý.ÿ.. */
    $"0913 1818 1D1A 1511 0905 0B10 1213 1413"            /* Æ.......Æ....... */
    $"1428 1317 1A1B 1C14 34CD F7FF 01B8 70F6"            /* .(......4Í÷ÿ.¸pö */
    $"FFF7 FF13 DC69 6565 6462 615F 5C5A 5855"            /* ÿ÷ÿ.Üieedba_\ZXU */
    $"524F 4C49 3F29 140B FE0A FE09 FF08 173C"            /* ROLI?)..þ.þÆÿ..< */
    $"5F4F 4946 4443 403D 3B39 3633 302D 2925"            /* _OIFDC@=;9630-)% */
    $"211E 1B19 112B E7D4 FF0A D316 050C 150D"            /* !....+çÔÿ.Ó....Â */
    $"0708 0809 0AFE 0B06 0A08 080A 0A0B 0A19"            /* ...Æ.þ.......... */
    $"0E6D 8D8C 8F93 979A 9EA1 A4AE 7E36 6664"            /* .m¡¤®~6fd */
    $"6667 6969 6D6F 3C05 0104 FC05 FD07 2704"            /* fgiimo<...ü.ý.'. */
    $"0309 1014 1518 1613 100B 080C 1012 1314"            /* .Æ.............. */
    $"1314 2813 171A 1B1C 162E A4D9 D3D4 D1D0"            /* ..(.......¤ÙÓÔÑÐ */
    $"D2D4 D6D7 E19A 6DEC FF13 DC69 6565 6462"            /* ÒÔÖ×ámìÿ.Üieedb */
    $"615F 5C5A 5855 524F 4C4A 3F29 150B FE0A"            /* a_\ZXUROLJ?)..þ. */
    $"FE09 0508 093C 5F4F 4913 4644 4340 3D3B"            /* þÆ..Æ<_OI.FDC@=; */
    $"3936 3330 2D29 2521 1E1B 1911 2BE7 D4FF"            /* 9630-)%!....+çÔÿ */
    $"0AD3 1605 0D15 0D07 0808 090A FE0B 140A"            /* .Ó..Â.Â...Æ.þ... */
    $"0808 0A0A 0B0A 0E6D 8D8C 8F93 979A 9EA1"            /* .......m¡ */
    $"A4AE 7F2A FE4F 0850 5253 5657 3004 0104"            /* ¤®.*þO.PRSVW0... */
    $"FC05 FD07 FF05 0409 0E12 1213 2013 1110"            /* ü.ý.ÿ..Æ.... ... */
    $"0C0A 0E11 1213 1413 1328 1317 1A1B 1C19"            /* .........(...... */
    $"2970 8E8B 8E8A 888A 8C8F 939A 6A6D ECFF"            /* )pjmìÿ */
    $"13DC 6965 6564 6261 5F5C 5A58 5552 4F4C"            /* .Üieedba_\ZXUROL */
    $"4A3F 2914 0BFE 0AFE 09FF 0817 3B5F 4F49"            /* J?)..þ.þÆÿ..;_OI */
    $"4644 4340 3D3B 3936 3330 2D29 2521 1E1B"            /* FDC@=;9630-)%!.. */
    $"1911 2BE7 EBFF FFFF 01C5 ECFF 0549 000B"            /* ..+çëÿÿÿ.Åìÿ.I.. */
    $"1512 07FE 08FF 0AFE 0BFE 08FF 0A1B 0B06"            /* ...þ.ÿ.þ.þ.ÿ.... */
    $"3F89 898C 9094 979A 9EA1 A5AE 4A6D 9F9C"            /* ?¡¥®Jm */
    $"9EA1 A3A7 AB46 0001 0404 FD05 2106 0705"            /* ¡£§«F....ý.!... */
    $"0005 3C77 94B0 7F90 C4BF B5A8 9163 230B"            /* ..<w°.Ä¿µ¨c#. */
    $"0E13 1208 6DE5 6B10 181B 1C1D 1344 E8F8"            /* ....måk......Dèø */
    $"FF02 C765 FCF7 FFF7 FF13 FE8A 6066 6463"            /* ÿ.Çeü÷ÿ÷ÿ.þ`fdc */
    $"615F 5D5A 5855 524F 4C49 4333 1C0D FE0A"            /* a_]ZXUROLIC3.Âþ. */
    $"FD09 1807 0F4D 5B4C 4845 4442 3E3C 3A37"            /* ýÆ...M[LHEDB><:7 */
    $"3533 2E2B 2723 201D 1A17 0976 D4FF 0549"            /* 53.+'# ...ÆvÔÿ.I */
    $"000B 1512 07FE 08FF 0AFE 0BFE 08FF 0A01"            /* .....þ.ÿ.þ.þ.ÿ.. */
    $"0B06 193F 8989 8C90 9497 9A9E A1A5 AF48"            /* ...?¡¥¯H */
    $"4164 6264 6668 6A6C 2D00 0204 04FD 052D"            /* Adbdfhjl-....ý.- */
    $"0607 0602 0528 5063 7356 749A 968F 8473"            /* .....(PcsVts */
    $"4F1D 0B0E 1312 086D E56B 1018 1B1C 1D16"            /* O......måk...... */
    $"39BC D9D5 D5D2 D2D4 D6D8 E0A8 62FC EDFF"            /* 9¼ÙÕÕÒÒÔÖØà¨büíÿ */
    $"13FE 8A60 6664 6361 5F5D 5A58 5552 4F4C"            /* .þ`fdca_]ZXUROL */
    $"4943 331C 0DFE 0AFD 0904 070F 4D5C 4D13"            /* IC3.Âþ.ýÆ...M\M. */
    $"4845 4442 3E3C 3A37 3533 2E2B 2723 201D"            /* HEDB><:753.+'# . */
    $"1A17 0976 D4FF 0549 000B 1612 07FE 08FF"            /* ..ÆvÔÿ.I.....þ.ÿ */
    $"0AFE 0BFE 08FF 0A1B 0B06 3F89 898C 9094"            /* .þ.þ.ÿ....? */
    $"979A 9EA1 A5AF 4831 504F 5152 5354 5624"            /* ¡¥¯H1POQRSTV$ */
    $"0002 0404 FD05 0B06 0708 0405 223F 4F5D"            /* ....ý......."?O] */
    $"4549 6021 625C 544C 3518 0E10 1312 096C"            /* EI`!b\TL5.....Æl */
    $"E46B 1018 1B1C 1D1A 307F 8E8F 918B 8A8D"            /* äk......0. */
    $"9091 9673 5FFC EDFF 13FE 8A60 6664 6361"            /* s_üíÿ.þ`fdca */
    $"5F5D 5A58 5552 4F4C 4943 311B 0DFE 0AFD"            /* _]ZXUROLIC1.Âþ.ý */
    $"0918 070F 4D5C 4C48 4544 423E 3C3A 3735"            /* Æ...M\LHEDB><:75 */
    $"332E 2B27 2320 1D1A 1709 76EB FFFF FF01"            /* 3.+'# ...Ævëÿÿÿ. */
    $"CFED FF05 9400 0911 160A FE08 0509 0A0A"            /* Ïíÿ..Æ...þ..Æ.. */
    $"0B0B 09FE 08FF 0A1B 090F 7189 898D 9094"            /* ..Æþ.ÿ..Æ.q */
    $"989B 9EA1 A7A3 408D 9C9C 9FA1 A5AD 5B00"            /* ¡§£@¡¥­[. */
    $"0103 0404 FE05 2306 0500 0547 91C1 D3D2"            /* ....þ.#....GÁÓÒ */
    $"DA89 BBD7 D7DB DFE4 E1C1 761D 0A0F 78F7"            /* Ú»××ÛßäáÁv...x÷ */
    $"FFF9 7A13 191C 1D1E 155C F6F9 FF02 D659"            /* ÿùz......\öùÿ.ÖY */
    $"F7F7 FFF6 FF12 CF66 6565 6461 5F5D 5B59"            /* ÷÷ÿöÿ.Ïfeeda_][Y */
    $"5653 504D 4946 3A24 12FE 0AFC 0918 061B"            /* VSPMIF:$.þ.üÆ... */
    $"5B57 4B46 4443 413E 3B39 3734 312D 2924"            /* [WKFDCA>;9741-)$ */
    $"211E 1B19 1223 DAD6 FF05 9400 0910 160A"            /* !....#ÚÖÿ..Æ... */
    $"FE08 0509 0A0A 0B0B 09FE 08FF 0A01 090F"            /* þ..Æ....Æþ.ÿ..Æ. */
    $"1971 8989 8D90 9498 9B9E A1A7 A535 5863"            /* .q¡§¥5Xc */
    $"6566 676A 6E38 0002 0304 04FE 052E 0605"            /* efgjn8.....þ.... */
    $"0106 305D 7E8A 898D 5D95 AAAA ACAF B4B2"            /* ..0]~]ªª¬¯´² */
    $"995F 1A0C 0F78 F7FF F879 1319 1C1D 1E18"            /* _...x÷ÿøy...... */
    $"4ED1 DBD7 D6D3 D5D7 D8DF B455 F7EC FF12"            /* NÑÛ×ÖÓÕ×Øß´U÷ìÿ. */
    $"CF66 6565 6461 5F5D 5B59 5653 504D 4945"            /* Ïfeeda_][YVSPMIE */
    $"3A24 12FE 0AFC 0903 061C 5C57 144B 4644"            /* :$.þ.üÆ...\W.KFD */
    $"4341 3E3B 3937 3431 2D29 2421 1E1B 1912"            /* CA>;9741-)$!.... */
    $"23DA D6FF 0594 0009 1016 0AFE 0805 090A"            /* #ÚÖÿ..Æ...þ..Æ. */
    $"0A0B 0B09 FE08 FF0A 1B09 0F71 8989 8D90"            /* ...Æþ.ÿ..Æ.q */
    $"9498 9B9E A1A7 A530 4450 4F51 5153 572D"            /* ¡§¥0DPOQQSW- */
    $"0002 0304 04FE 050C 0605 0207 284A 656E"            /* .....þ......(Jen */
    $"6D73 495B 6A21 6B6D 7072 7162 4118 0E0E"            /* msI[j!kmprqbA... */
    $"77F7 FFF8 7913 191C 1D1E 1C3D 8A91 8F8F"            /* w÷ÿøy......= */
    $"8B8D 9190 937B 53F8 ECFF 12CF 6665 6564"            /* {Søìÿ.Ïfeed */
    $"615F 5D5B 5956 5350 4D49 4539 2411 FE0A"            /* a_][YVSPMIE9$.þ. */
    $"FC09 1806 1C5C 574B 4644 4341 3E3B 3937"            /* üÆ...\WKFDCA>;97 */
    $"3431 2D29 2421 1E1B 1912 23DA ECFF FFFF"            /* 41-)$!....#Úìÿÿÿ */
    $"01C7 EEFF 05E3 1F02 0F16 0CFE 0802 090A"            /* .Çîÿ.ã.....þ..Æ. */
    $"0AFE 0B01 0908 FE09 1C0A 0535 8586 8A8E"            /* .þ..Æ.þÆ...5 */
    $"9195 989C 9FA3 AC77 559F 9A9D 9FA3 A658"            /* £¬wU£¦X */
    $"0201 0303 0404 FE05 1602 043B 8EC3 CDC7"            /* ......þ....;ÃÍÇ */
    $"C7CA CE7D BED3 D3D5 D7D8 DBE1 E3BF 568C"            /* ÇÊÎ}¾ÓÓÕ×ØÛáã¿V */
    $"FCFF 0872 141C 1E1E 1F19 79F7 FAFF 02E8"            /* üÿ.r......y÷úÿ.è */
    $"54F0 F7FF F5FF 1393 5E65 6362 605D 5B59"            /* Tð÷ÿõÿ.^ecb`][Y */
    $"5653 504D 4A46 3F2F 190C 0AFA 0917 062B"            /* VSPMJF?/...úÆ..+ */
    $"5E53 4946 4342 403D 3A38 3633 2F2B 2723"            /* ^SIFCB@=:863/+'# */
    $"201D 1A18 0961 D7FF 05E3 1F02 0F16 0CFE"            /*  ...Æa×ÿ.ã.....þ */
    $"0802 090A 0AFE 0B01 0908 FE09 020A 0535"            /* ..Æ..þ..Æ.þÆ...5 */
    $"1985 868A 8E91 9598 9C9F A3AC 7835 6462"            /* .£¬x5db */
    $"6365 686A 3701 0203 0304 04FE 05FF 0314"            /* cehj7......þ.ÿ.. */
    $"285D 7E85 8381 8386 5897 A7A6 A8AA ABAE"            /* (]~X§¦¨ª«® */
    $"B3B4 9647 8DFC FF12 7214 1C1E 1E1F 1B67"            /* ³´Güÿ.r......g */
    $"D2DA D8D7 D5D6 D8DE C44E F0EB FF13 935E"            /* ÒÚØ×ÕÖØÞÄNðëÿ.^ */
    $"6563 6260 5D5B 5956 5350 4D4A 4640 2E19"            /* ecb`][YVSPMJF@.. */
    $"0D0A FA09 0206 2B5E 1453 4946 4342 403D"            /* Â.úÆ..+^.SIFCB@= */
    $"3A38 3633 2F2B 2723 201D 1A18 0961 D7FF"            /* :863/+'# ...Æa×ÿ */
    $"05E3 1F02 0E16 0CFE 0802 090A 0AFE 0B01"            /* .ã.....þ..Æ..þ.. */
    $"0908 FE09 1C0A 0535 8586 8A8E 9195 989C"            /* Æ.þÆ...5 */
    $"9FA3 AC78 2A4E 4E50 5052 542C 0202 0303"            /* £¬x*NNPPRT,.... */
    $"0404 FE05 FF04 0A20 4A66 6B69 686A 6D43"            /* ..þ.ÿ.. JfkihjmC */
    $"5D69 096A 6B6A 6B6D 6F72 6232 8EFC FF08"            /* ]iÆjkjkmorb2üÿ. */
    $"7114 1C1E 1E20 1E4D 8CFE 90FF 8D04 8F93"            /* q.... .Mþÿ. */
    $"8548 F1EB FF13 935E 6563 6260 5D5B 5956"            /* Hñëÿ.^ecb`][YV */
    $"5350 4D4A 463F 2E19 0D0A FA09 1706 2B5E"            /* SPMJF?..Â.úÆ..+^ */
    $"5349 4643 4240 3D3A 3836 332F 2B27 2320"            /* SIFCB@=:863/+'#  */
    $"1D1A 1809 61EC FFFF FF01 D3EE FF05 6F00"            /* ...Æaìÿÿÿ.Óîÿ.o. */
    $"0C17 0E07 FE08 0209 0A0A FE0B 1C09 0809"            /* ....þ..Æ..þ..Æ.Æ */
    $"0A0A 0714 7085 878B 8F92 9699 9C9F A4AB"            /* ....p¤« */
    $"456E 9D9A 9DA0 A95D 0001 FE03 FF04 FF05"            /* En ©]..þ.ÿ.ÿ. */
    $"1800 106E C0C7 C2C3 C5C7 CBC0 69C8 D2D3"            /* ...nÀÇÂÃÅÇËÀiÈÒÓ */
    $"D4D6 D9DA DBE7 C237 66F3 FEFF 09F2 6414"            /* ÔÖÙÚÛçÂ7fóþÿÆòd. */
    $"1C1E 1E20 2016 8DFA FF02 F465 DEF7 FFF5"            /* ...  .úÿ.ôeÞ÷ÿõ */
    $"FF12 D568 6364 6260 5D5B 5956 5350 4D4A"            /* ÿ.Õhcdb`][YVSPMJ */
    $"4742 3622 11FE 0AFC 0918 0807 3A60 4E48"            /* GB6".þ.üÆ...:`NH */
    $"4542 423F 3C39 3735 322D 2926 221E 1B18"            /* EBB?<9752-)&"... */
    $"1412 C1D8 FF05 6F00 0C18 0F07 FE08 0209"            /* ..ÁØÿ.o.....þ..Æ */
    $"0A0A FE0B 0709 0809 0A0A 0714 7014 8587"            /* ..þ..Æ.Æ....p. */
    $"8B8F 9296 999C 9FA4 AC43 4264 6364 666C"            /* ¤¬CBdcdfl */
    $"3B00 02FE 03FF 04FF 0518 010B 467D 827E"            /* ;..þ.ÿ.ÿ....F}~ */
    $"7F81 8284 7D4E 9FA6 A7A8 A9AB ADAD B599"            /* .}N¦§¨©«­­µ */
    $"2F67 F3FE FF13 F264 141C 1E1E 2020 1879"            /* /góþÿ.òd....  .y */
    $"DCD8 DAD7 D6D8 DCCF 58DF EBFF 12D5 6863"            /* ÜØÚ×ÖØÜÏXßëÿ.Õhc */
    $"6462 605D 5B59 5653 504D 4A47 4236 2211"            /* db`][YVSPMJGB6". */
    $"FE0A FC09 0208 073A 1560 4E48 4542 423F"            /* þ.üÆ...:.`NHEBB? */
    $"3C39 3735 322D 2926 221E 1B18 1412 C1D8"            /* <9752-)&".....ÁØ */
    $"FF05 6F00 0C17 0F07 FE08 0209 0A0A FE0B"            /* ÿ.o.....þ..Æ..þ. */
    $"1C09 0809 0A0A 0714 7085 878B 8F92 9699"            /* .Æ.Æ....p */
    $"9C9F A4AC 4333 4F4D 4F50 5530 0002 FE03"            /* ¤¬C3OMOPU0..þ. */
    $"FF04 FF05 0D02 0A38 6366 6365 6769 6B66"            /* ÿ.ÿ.Â..8cfcegikf */
    $"3962 680A 6C6D 696D 6F6F 7462 2269 F3FE"            /* 9bh.lmimootb"ióþ */
    $"FF13 F264 141C 1E1E 2021 1C57 9190 9390"            /* ÿ.òd.... !.W */
    $"8D8F 958F 4CE0 EBFF 12D5 6863 6462 605D"            /* Làëÿ.Õhcdb`] */
    $"5B59 5653 504D 4A47 4236 2211 FE0A FC09"            /* [YVSPMJGB6".þ.üÆ */
    $"1808 073B 604E 4845 4242 3F3C 3937 3532"            /* ...;`NHEBB?<9752 */
    $"2D29 2622 1E1B 1814 12C1 EDFF FFFF 01CC"            /* -)&".....Áíÿÿÿ.Ì */
    $"EFFF 09BE 0507 1411 0808 0909 08FE 0AFF"            /* ïÿÆ¾......ÆÆ.þ.ÿ */
    $"0B1C 0908 0809 090A 043B 8484 878B 8F92"            /* ..Æ..ÆÆ..; */
    $"969A 9DA0 A59D 3F8D 9A9A 9DA7 7906 00FD"            /*  ¥?§y..ý */
    $"03FE 0427 001F 90C6 BFBE C0C3 C5C7 CDB3"            /* .þ.'..Æ¿¾ÀÃÅÇÍ³ */
    $"5BD0 D1D2 D4D6 D8DB E6B0 2B0A 0750 EDFF"            /* [ÐÑÒÔÖØÛæ°+..Píÿ */
    $"E95A 111B 1D1E 1F21 221F 26C8 FAFF 017B"            /* éZ.....!".&Èúÿ.{ */
    $"CBF7 FFF4 FF14 925E 6562 605E 5C5A 5754"            /* Ë÷ÿôÿ.^eb`^\ZWT */
    $"514E 4A47 433B 2A16 0B0A 0AFB 0917 070F"            /* QNJGC;*....ûÆ... */
    $"4D59 4B47 4443 403D 3B39 3734 302C 2824"            /* MYKGDC@=;9740,($ */
    $"201D 1917 0A55 D9FF 09BE 0507 1411 0808"            /*  ....UÙÿÆ¾...... */
    $"0909 08FE 0AFF 0B08 0908 0809 090A 043B"            /* ÆÆ.þ.ÿ..Æ..ÆÆ..; */
    $"8413 8487 8B8F 9296 9A9D A0A5 9F32 5762"            /* . ¥2Wb */
    $"6264 6B4B 0400 FD03 FE04 3000 145E 7F7C"            /* bdkK..ý.þ.0..^.| */
    $"7B7D 7E80 8286 7447 A4A5 A6A8 AAAB AEB6"            /* {}~tG¤¥¦¨ª«®¶ */
    $"8B26 0D07 50ED FFE9 5A11 1B1D 1E1F 2122"            /* &Â.PíÿéZ.....!" */
    $"2025 AADF D8D8 D6D8 DBD9 69CC EAFF 1492"            /*  %ªßØØÖØÛÙiÌêÿ. */
    $"5E65 6260 5E5C 5A57 5451 4E4A 4743 3C2B"            /* ^eb`^\ZWTQNJGC<+ */
    $"170C 0A0A FB09 0107 1015 4E59 4B47 4443"            /* ....ûÆ....NYKGDC */
    $"403D 3B39 3734 302C 2824 201D 1917 0A55"            /* @=;9740,($ ....U */
    $"D9FF 09BE 0507 1411 0808 0909 08FE 0AFF"            /* ÙÿÆ¾......ÆÆ.þ.ÿ */
    $"0B1C 0908 0809 090A 043B 8484 878B 8F92"            /* ..Æ..ÆÆ..; */
    $"969A 9DA0 A5A0 2D44 4D4D 4E54 3C03 00FD"            /*  ¥ -DMMNT<..ý */
    $"03FE 040E 0112 4B66 6262 6465 6767 6C60"            /* .þ....Kfbbdeggl` */
    $"3166 66FE 691E 6E70 735B 1F0F 0750 EDFF"            /* 1ffþi.nps[...Píÿ */
    $"E95A 111B 1D1E 1F21 2221 2475 9690 908D"            /* éZ.....!"!$u */
    $"8F92 9354 CFEA FF14 925E 6562 605E 5C5A"            /* TÏêÿ.^eb`^\Z */
    $"5754 514E 4A47 433C 2B17 0C0A 0AFB 0917"            /* WTQNJGC<+....ûÆ. */
    $"0710 4E59 4B47 4443 403D 3B39 3734 302C"            /* ..NYKGDC@=;9740, */
    $"2824 201D 1917 0A55 EDFF FFFF 01CE F0FF"            /* ($ ....Uíÿÿÿ.Îðÿ */
    $"07F3 3C00 1214 0908 08FE 09FE 0AFF 0BFE"            /* .ó<...Æ..þÆþ.ÿ.þ */
    $"08FF 0917 0812 6C82 8488 8C8F 9296 9A9D"            /* .ÿÆ...l */
    $"A0A7 8855 9B99 9AA2 9018 0002 FD03 FF04"            /*  §U¢...ý.ÿ. */
    $"2900 28A0 C2BB BCBF C0C3 C5C7 CEA3 64D5"            /* ).( Â»¼¿ÀÃÅÇÎ£dÕ */
    $"D1D2 D4D6 DAE1 A226 0A14 1409 60E2 510E"            /* ÑÒÔÖÚá¢&...Æ`âQ. */
    $"1A1C 1D1E 1F21 2223 1A51 EFFB FF01 8EBD"            /* .....!"#.Qïûÿ.½ */
    $"F7FF F4FF 00CB FE63 1060 5E5C 5A57 5451"            /* ÷ÿôÿ.Ëþc.`^\ZWTQ */
    $"4E4B 4744 3F32 1C0E 0A0A FA09 1706 1F5D"            /* NKGD?2....úÆ...] */
    $"5349 4543 413F 3C3B 3836 322E 2A26 221F"            /* SIECA?<;862.*&". */
    $"1B19 1415 C1DB FF07 F33C 0011 140A 0808"            /* ....ÁÛÿ.ó<...... */
    $"FE09 FE0A FF0B FE08 FF09 0308 126C 8213"            /* þÆþ.ÿ.þ.ÿÆ...l. */
    $"8488 8C8F 9296 9A9D A0A7 8A38 6260 6268"            /*  §8b`bh */
    $"5B0E 0002 FD03 FF04 3100 1A67 7D78 797B"            /* [...ý.ÿ.1..g}xy{ */
    $"7D7E 7F80 876B 4FA8 A5A6 A8A9 ADB3 8122"            /* }~.kO¨¥¦¨©­³" */
    $"0C14 1409 61E3 510E 1A1C 1D1E 1F21 2223"            /* ...ÆaãQ......!"# */
    $"1C49 CBDA D6D7 D7D9 E077 BEEA FF00 CBFE"            /* .IËÚÖ××Ùàw¾êÿ.Ëþ */
    $"6310 605E 5C5A 5754 514E 4B47 443F 331E"            /* c.`^\ZWTQNKGD?3. */
    $"0E0A 0AFA 0900 0616 1F5D 5349 4543 413F"            /* ...úÆ....]SIECA? */
    $"3C3B 3836 322E 2A26 221F 1B19 1415 C1DB"            /* <;862.*&".....ÁÛ */
    $"FF07 F33C 0011 1309 0808 FE09 FE0A FF0B"            /* ÿ.ó<...Æ..þÆþ.ÿ. */
    $"FE08 FF09 1708 126C 8284 888C 8F92 969A"            /* þ.ÿÆ...l */
    $"9DA0 A88B 2D4D 4C4E 5247 0B00 02FD 03FF"            /*  ¨-MLNRG...ý.ÿ */
    $"040F 0017 5362 6062 6265 6766 696D 5934"            /* ....Sb`bbegfimY4 */
    $"6965 2166 686C 6F70 531C 0F14 1409 62E5"            /* ie!fhlopS....Æbå */
    $"510E 1A1C 1D1E 1F21 2223 1F3B 8A92 9091"            /* Q......!"#.; */
    $"9393 985A C0EA FF00 CBFE 6310 605E 5C5A"            /* ZÀêÿ.Ëþc.`^\Z */
    $"5754 514E 4B47 433F 331E 0E0A 0AFA 0917"            /* WTQNKGC?3....úÆ. */
    $"061F 5C53 4945 4341 3F3C 3B38 3632 2E2A"            /* ..\SIECA?<;862.* */
    $"2622 1F1B 1914 15C1 EEFF FFFF 01CE F0FF"            /* &".....Áîÿÿÿ.Îðÿ */
    $"0991 000C 170C 0909 0A09 08FD 0AFF 0BFE"            /* Æ....ÆÆ.Æ.ý.ÿ.þ */
    $"08FF 0917 0637 7B7F 8589 8C90 9397 9A9D"            /* .ÿÆ..7{. */
    $"A0AC 706C 9B98 9C9E 3B00 0302 FD03 2B04"            /*  ¬pl;...ý.+. */
    $"0024 AABE B8BA BDBE C1C3 C5C7 D092 6EDA"            /* .$ª¾¸º½¾ÁÃÅÇÐnÚ */
    $"D0D2 D4DA D683 140C 1314 140B 346A 0D19"            /* ÐÒÔÚÖ......4jÂ. */
    $"1B1C 1D1E 2020 2223 2318 88FB FF01 A8A3"            /* ....  "##.ûÿ.¨£ */
    $"F7FF F4FF 14FB 855E 6361 5E5C 5A57 5451"            /* ÷ÿôÿ.û^ca^\ZWTQ */
    $"4E4B 4743 4038 2512 0A0A FA09 1708 073E"            /* NKGC@8%...úÆ...> */
    $"5F4E 4844 4340 3E3B 3A37 3430 2C28 2420"            /* _NHDC@>;:740,($  */
    $"1C1A 180A 55DB FF09 9100 0B16 0C08 090A"            /* ....UÛÿÆ.....Æ. */
    $"0908 FD0A FF0B FE08 FF09 0306 387B 7F13"            /* Æ.ý.ÿ.þ.ÿÆ..8{.. */
    $"8589 8C90 9397 9A9D A0AC 6F43 625F 6465"            /*  ¬oCb_de */
    $"2600 0202 FD03 3304 0018 6D7A 7577 787B"            /* &...ý.3...mzuwx{ */
    $"7E7E 8081 875F 58AC A5A7 A8AC A969 130D"            /* ~~_X¬¥§¨¬©i.Â */
    $"1314 140D 2F5D 0E19 1B1C 1D1E 2020 2223"            /* ...Â/]......  "# */
    $"231A 75DD D8D7 D6D9 E18D A1EA FF14 FB85"            /* #.uÝØ×ÖÙá¡êÿ.û */
    $"5E63 615E 5C5A 5754 514E 4B47 4340 3825"            /* ^ca^\ZWTQNKGC@8% */
    $"130B 0AFA 0900 0816 083F 5E4E 4844 4340"            /* ...úÆ....?^NHDC@ */
    $"3E3B 3A37 3430 2C28 2420 1C1A 180A 55DB"            /* >;:740,($ ....UÛ */
    $"FF09 9100 0B16 0C09 090A 0908 FD0A FF0B"            /* ÿÆ....ÆÆ.Æ.ý.ÿ. */
    $"FE08 FF09 1706 387B 7F85 898C 9093 979A"            /* þ.ÿÆ..8{. */
    $"9DA0 AD6E 334E 4C4F 501E 0002 02FD 0311"            /*  ­n3NLOP....ý.. */
    $"0400 1457 625F 6162 6365 6668 686D 4F39"            /* ...Wb_abcefhhmO9 */
    $"6A66 2166 696E 6A44 120F 1314 1410 274F"            /* jf!finjD......'O */
    $"1019 1B1C 1D1E 2020 2223 231F 5695 9291"            /* ......  "##.V */
    $"9294 9A63 A2EA FF14 FB85 5E63 615E 5C5A"            /* c¢êÿ.û^ca^\Z */
    $"5754 514E 4B47 4340 3826 130A 0AFA 0917"            /* WTQNKGC@8&...úÆ. */
    $"0807 3F5F 4E48 4443 403E 3B3A 3734 302C"            /* ..?_NHDC@>;:740, */
    $"2824 201C 1A18 0A55 EEFF FFFF 01CB F1FF"            /* ($ ....Uîÿÿÿ.Ëñÿ */
    $"0ACD 1106 140E 0809 090A 0A09 FD0A FF0B"            /* .Í.....ÆÆ..Æý.ÿ. */
    $"FF08 FF09 1606 1A69 7B80 8589 8D90 9497"            /* ÿ.ÿÆ...i{ */
    $"9A9D A2A6 4C82 9998 A363 0001 FB03 2C00"            /* ¢¦L£c..û.,. */
    $"1496 BDB7 B8BB BCBF C2C3 C5C6 D08A 83D7"            /* .½·¸»¼¿ÂÃÅÆÐ× */
    $"D0D2 DAC6 4808 0D12 1313 0B3D C8D0 3413"            /* ÐÒÚÆH.Â....=ÈÐ4. */
    $"1B1C 1D1E 1F21 2223 2421 2AD4 FCFF 01C0"            /* .....!"#$!*Ôüÿ.À */
    $"87F7 FFF3 FF13 D264 6161 5E5C 5A57 5452"            /* ÷ÿóÿ.Òdaa^\ZWTR */
    $"4F4B 4844 413C 2F1A 0C0A F909 1707 0E4D"            /* OKHDA</...ùÆ...M */
    $"5C4C 4744 413F 3C3B 3836 332F 2B26 221E"            /* \LGDA?<;863/+&". */
    $"1C18 1317 CBDD FF0A CD11 0514 0F08 0909"            /* ....ËÝÿ.Í.....ÆÆ */
    $"0A0A 09FD 0AFF 0BFF 08FF 0904 061A 6A7B"            /* ..Æý.ÿ.ÿ.ÿÆ...j{ */
    $"8011 8589 8D90 9497 9A9D A2A7 4550 6362"            /* .¢§EPcb */
    $"6A3E 0001 FB03 3301 0D5F 7876 777A 7B7C"            /* j>..û.3.Â_xvwz{| */
    $"7F81 8383 8A5B 69AA A4A6 AC9D 3C0A 0E12"            /* .[iª¤¦¬<... */
    $"1313 0C33 9FA4 2C15 1A1C 1D1E 1F21 2223"            /* ...3¤,......!"# */
    $"2422 29B5 DDD6 D7D8 E3A1 83E9 FF13 D264"            /* $")µÝÖ×Øã¡éÿ.Òd */
    $"6161 5E5C 5A57 5452 4F4B 4844 413B 2E1A"            /* aa^\ZWTROKHDA;.. */
    $"0D0A F909 1707 0D4C 5C4C 4744 413F 3C3B"            /* Â.ùÆ..ÂL\LGDA?<; */
    $"3836 332F 2B26 221E 1C18 1317 CBDD FF0A"            /* 863/+&".....ËÝÿ. */
    $"CD11 0614 0E08 0909 0A0A 09FD 0AFF 0BFF"            /* Í.....ÆÆ..Æý.ÿ.ÿ */
    $"08FF 0916 061A 6A7B 8085 898D 9094 979A"            /* .ÿÆ...j{ */
    $"9DA2 A742 3E4F 4F54 3100 02FB 0311 020C"            /* ¢§B>OOT1..û.... */
    $"4E61 5E5F 6162 6364 6566 686F 4B43 6C69"            /* Na^_abcdefhoKCli */
    $"2168 6C62 290D 1012 1313 1028 6869 2618"            /* !hlb)Â.....(hi&. */
    $"1A1C 1D1E 1F21 2223 2423 287E 9592 9193"            /* .....!"#$#(~ */
    $"9870 82E9 FF13 D264 6161 5E5C 5A57 5452"            /* péÿ.Òdaa^\ZWTR */
    $"4F4B 4844 413C 2F1A 0C0A F909 1707 0E4D"            /* OKHDA</...ùÆ...M */
    $"5C4C 4744 413F 3C3B 3836 332F 2B26 221E"            /* \LGDA?<;863/+&". */
    $"1C18 1317 CBEF FFFF FF01 CFF1 FF0A 5600"            /* ....Ëïÿÿÿ.Ïñÿ.V. */
    $"1015 0A09 090A 0C0B 09FD 0AFF 0BFF 08FF"            /* ...ÆÆ...Æý.ÿ.ÿ.ÿ */
    $"0916 033A 7B7C 8186 8A8D 9193 979B 9DA5"            /* Æ..:{|¥ */
    $"8E34 9197 9A99 2600 02FD 032E 0402 067D"            /* 4&..ý.....} */
    $"BBB5 B6B9 BBBC BFC1 C3C4 C6D1 83A1 D3D0"            /* »µ¶¹»¼¿ÁÃÄÆÑ¡ÓÐ */
    $"D9BE 3B05 0F11 1212 0944 CFF0 F485 101B"            /* Ù¾;.....ÆDÏðô.. */
    $"1C1E 1F1F 2122 2325 251A 8FFC FF01 C381"            /* ....!"#%%.üÿ.Ã */
    $"F7FF F3FF 13FC 825D 615E 5C5A 5855 524F"            /* ÷ÿóÿ.ü]a^\ZXURO */
    $"4C48 4441 3D35 2310 0AF8 0916 041D 5B56"            /* LHDA=5#..øÆ...[V */
    $"4945 4240 3E3B 3A37 3431 2D29 2420 1D19"            /* IEB@>;:741-)$ .. */
    $"1709 73DD FF0A 5600 1015 0A09 090A 0C0B"            /* .ÆsÝÿ.V....ÆÆ... */
    $"09FD 0AFF 0BFF 08FF 0904 0339 7B7C 8111"            /* Æý.ÿ.ÿ.ÿÆ..9{|. */
    $"868A 8D91 9397 9B9D A590 245C 6264 6117"            /* ¥$\bda. */
    $"0002 FD03 3504 0305 5078 7478 7979 7B7C"            /* ..ý.5...Pxtxyy{| */
    $"7D7D 8081 8756 80A7 A4AC 9531 0810 1112"            /* }}V§¤¬1.... */
    $"120B 38A4 BEC3 6C12 1B1C 1E1F 1F21 2223"            /* ..8¤¾Ãl......!"# */
    $"2525 1D7D E2D9 D8DA E3A5 7DE9 FF13 FC82"            /* %%.}âÙØÚã¥}éÿ.ü */
    $"5D61 5E5C 5A58 5552 4F4C 4844 413D 3423"            /* ]a^\ZXUROLHDA=4# */
    $"100A F909 1709 051D 5B55 4945 4240 3E3B"            /* ..ùÆ.Æ..[UIEB@>; */
    $"3A37 3431 2D29 2420 1D19 1709 73DD FF0A"            /* :741-)$ ...ÆsÝÿ. */
    $"5600 1014 0A09 090A 0C0B 09FD 0AFF 0BFF"            /* V....ÆÆ...Æý.ÿ.ÿ */
    $"08FF 0916 0339 7B7C 8186 8A8D 9193 979B"            /* .ÿÆ..9{| */
    $"9DA5 901E 484D 504D 1200 02FD 0313 0403"            /* ¥.HMPM...ý.... */
    $"0541 5F5E 5F5E 6061 6364 6666 686F 4751"            /* .A_^_^`acdffhoGQ */
    $"6A69 216C 5F23 0B10 1112 120E 2B6B 7C7F"            /* ji!l_#......+k|. */
    $"4C15 1B1C 1E1F 1F21 2223 2525 205B 9691"            /* L......!"#%% [ */
    $"9094 9B74 7BE9 FF13 FC82 5D61 5E5C 5A58"            /* t{éÿ.ü]a^\ZX */
    $"5552 4F4C 4844 413D 3523 100A F809 1605"            /* UROLHDA=5#..øÆ.. */
    $"1D5B 5549 4542 403E 3B3A 3734 312D 2924"            /* .[UIEB@>;:741-)$ */
    $"201D 1917 0973 EFFF FFFF 01D3 F2FF 0BB2"            /*  ...Æsïÿÿÿ.Óòÿ.² */
    $"010B 150B 0909 0A0B 0B0A 09FD 0A1C 0B09"            /* ....ÆÆ....Æý...Æ */
    $"0808 0908 1065 7A7C 8186 8A8D 9193 979B"            /* ..Æ..ez| */
    $"9EA9 6C4A 9996 A056 0001 02FC 032E 005B"            /* ©lJ V...ü...[ */
    $"B9B4 B4B6 B9BA BCBF C1C3 C5C6 D17F B6D1"            /* ¹´´¶¹º¼¿ÁÃÅÆÑ.¶Ñ */
    $"D9B2 2B07 1011 1110 084C D2EC E6ED DA3A"            /* Ù²+......LÒìæíÚ: */
    $"171C 1E1F 1F21 2323 2526 2139 E4FD FF02"            /* .....!##%&!9äýÿ. */
    $"D06E FCF8 FFF2 FF12 AB5B 605F 5C5A 5855"            /* Ðnüøÿòÿ.«[`_\ZXU */
    $"524F 4C48 4441 3D38 2A15 0BF8 0917 0805"            /* ROLHDA=8*..øÆ... */
    $"3760 4F47 4341 3E3C 3B39 3633 2F2B 2722"            /* 7`OGCA><;963/+'" */
    $"1E1A 1812 1DD6 DFFF 0BB2 010B 160B 0909"            /* .....Ößÿ.²....ÆÆ */
    $"0A0B 0B0A 09FD 0A0A 0B09 0808 0908 1065"            /* ....Æý...Æ..Æ..e */
    $"7A7C 8111 868A 8D91 9397 9B9E A96E 2D62"            /* z|.©n-b */
    $"6166 3600 0202 FC03 1600 3A78 7475 7778"            /* af6...ü...:xtuwx */
    $"797A 7B7D 7C7E 8189 5690 A4AB 8C23 0910"            /* yz{}|~V¤«#Æ. */
    $"FE11 1B0A 3FA6 BBB8 BDAE 3217 1C1E 1F1F"            /* þ...?¦»¸½®2..... */
    $"2123 2325 2622 36C3 DDD9 D9E2 B069 FCE9"            /* !##%&"6ÃÝÙÙâ°iüé */
    $"FF12 AB5B 605F 5C5A 5855 524F 4C48 4441"            /* ÿ.«[`_\ZXUROLHDA */
    $"3D38 2915 0BF9 0918 0908 0536 604F 4743"            /* =8)..ùÆ.Æ..6`OGC */
    $"413E 3C3B 3936 332F 2B27 221E 1A18 121D"            /* A><;963/+'"..... */
    $"D6DF FF0B B201 0B16 0B09 090A 0B0B 0A09"            /* Ößÿ.²....ÆÆ....Æ */
    $"FD0A 1C0B 0908 0809 0810 657A 7C81 868A"            /* ý...Æ..Æ..ez| */
    $"8D91 9397 9B9E A96E 224B 4C50 2A00 0202"            /* ©n"KLP*... */
    $"FC03 1200 2D5E 5C5D 5D5E 5F61 6364 6567"            /* ü...-^\]]^_acdeg */
    $"686F 445A 686D 035A 1B0C 10FE 111B 0E2E"            /* hoDZhm.Z...þ.... */
    $"6C78 787E 7328 191C 1E1F 1F21 2323 2526"            /* lxx~s(.....!##%& */
    $"2330 8494 9294 9C7A 66FD E9FF 12AB 5B60"            /* #0zfýéÿ.«[` */
    $"5F5C 5A58 5552 4F4C 4844 413D 382A 140B"            /* _\ZXUROLHDA=8*.. */
    $"F809 1708 0535 604F 4743 413E 3C3B 3936"            /* øÆ...5`OGCA><;96 */
    $"332F 2B27 221E 1A18 121D D6F0 FFFF FF01"            /* 3/+'".....Öðÿÿÿ. */
    $"D0F3 FF04 F336 0013 0FFE 0903 0B0C 0909"            /* Ðóÿ.ó6...þÆ...ÆÆ */
    $"FB0A FE08 1809 052C 797A 7E82 878A 8D91"            /* û.þ..Æ.,yz~ */
    $"9397 9CA0 A84F 7498 9990 1900 0202 FD03"            /*  ¨Ot....ý. */
    $"2F00 22A6 B5B2 B5B7 B8BA BCBE C1C3 C5C7"            /* /."¦µ²µ·¸º¼¾ÁÃÅÇ */
    $"C975 BCDB AD2A 060F 1011 1008 55D7 E9E3"            /* Éu¼Û­*......U×éã */
    $"E6E9 F575 101C 1E1F 1F21 2324 2526 251C"            /* æéõu.....!#$%&%. */
    $"AAFD FF02 D56A FBF8 FFF2 FF12 DC67 5F5F"            /* ªýÿ.Õjûøÿòÿ.Üg__ */
    $"5D5B 5855 524F 4C48 4441 3E3A 301B 0DF8"            /* ][XUROLHDA>:0.Âø */
    $"0917 0806 0D4E 5C4A 4442 403D 3C3A 3835"            /* Æ...ÂN\JDB@=<:85 */
    $"302D 2924 1F1B 1916 0886 E0FF 04F3 3600"            /* 0-)$.....àÿ.ó6. */
    $"140F FE09 030B 0C09 09FB 0AFE 0806 0905"            /* ..þÆ...ÆÆû.þ..Æ. */
    $"2C79 7A7E 8211 878A 8D91 9397 9CA0 A84B"            /* ,yz~. ¨K */
    $"4560 625A 0F00 0202 FD03 3600 166B 7471"            /* E`bZ....ý.6..ktq */
    $"7375 7677 797C 7D7E 8184 8554 96AB 8A23"            /* suvwy|}~T«# */
    $"080F 1011 100A 45AA B9B4 B8BA C35F 131C"            /* ......Eª¹´¸ºÃ_.. */
    $"1E1F 1F21 2324 2526 251E 93E4 D9D9 E1B5"            /* ...!#$%&%.äÙÙáµ */
    $"65FA E9FF 12DC 675F 5F5D 5B58 5552 4F4C"            /* eúéÿ.Üg__][XUROL */
    $"4844 413E 3A2F 1B0D F909 1809 0806 0D4D"            /* HDA>:/.ÂùÆ.Æ..ÂM */
    $"5B4A 4442 403D 3C3A 3835 302D 2924 1F1B"            /* [JDB@=<:850-)$.. */
    $"1916 0886 E0FF 04F3 3600 140F FE09 030B"            /* ...àÿ.ó6...þÆ.. */
    $"0C09 09FB 0AFE 0818 0905 2C79 7A7E 8287"            /* .ÆÆû.þ..Æ.,yz~ */
    $"8A8D 9193 979C A0A9 4935 4C4E 480C 0002"            /*  ©I5LNH... */
    $"02FD 0309 0112 555C 5D5E 5F5F 6061 FE64"            /* .ý.Æ..U\]^__`aþd */
    $"0668 6B6C 3F5C 6B59 221A 0C10 1011 110D"            /* .hkl?\kY"......Â */
    $"316E 7776 767A 7F44 171C 1E1F 1F21 2324"            /* 1nwvvz.D.....!#$ */
    $"2526 2622 6A9A 9595 997D 61FB E9FF 12DC"            /* %&&"j}aûéÿ.Ü */
    $"675F 5F5D 5B58 5552 4F4C 4844 413E 3A30"            /* g__][XUROLHDA>:0 */
    $"1A0D F809 1708 060E 4E5C 4A44 4240 3D3C"            /* .ÂøÆ....N\JDB@=< */
    $"3A38 3530 2D29 241F 1B19 1608 86F0 FFFF"            /* :850-)$.....ðÿÿ */
    $"FF01 DFF3 FF0B 9F00 0F14 0A09 090A 0B0B"            /* ÿ.ßóÿ.....ÆÆ... */
    $"0909 FD0A 1A0B 0A08 0809 080C 5777 7A7E"            /* ÆÆý......Æ..Wwz~ */
    $"8286 8A8E 9195 989C A196 348A 959E 4B00"            /* ¡4K. */
    $"FE02 FE03 2B02 007A B7B0 B3B5 B6B8 BABB"            /* þ.þ.+..z·°³µ¶¸º» */
    $"BEC1 C3C5 C8BF 68CF A927 050F 1011 0E02"            /* ¾ÁÃÅÈ¿hÏ©'...... */
    $"55D9 E5E2 E4E6 E9F4 B61A 1B1E 1F20 2223"            /* UÙåâäæéô¶.... "# */
    $"24FE 2601 1A7E FDFF 02E0 57F5 F8FF F2FF"            /* $þ&..~ýÿ.àWõøÿòÿ */
    $"13FE 895A 5F5D 5B58 5552 4F4C 4844 413E"            /* .þZ_][XUROLHDA> */
    $"3A34 2111 0BF9 09FF 0816 0520 5D53 4643"            /* :4!..ùÆÿ... ]SFC */
    $"413E 3D3B 3936 332F 2A26 211E 1A18 1124"            /* A>=;963/*&!....$ */
    $"E3E1 FF0B 9F00 0F14 0A09 090A 0B0B 0909"            /* ãáÿ.....ÆÆ...ÆÆ */
    $"FD0A 0B0B 0A08 0809 080C 5877 7A7E 820E"            /* ý......Æ..Xwz~. */
    $"868A 8E91 9598 9CA2 9727 565F 642F 00FE"            /* ¢'V_d/.þ */
    $"02FE 032B 0200 4C75 7072 7475 7678 797D"            /* .þ.+..Luprtuvxy} */
    $"7E7F 8081 7B4B A486 2108 0F10 100F 0646"            /* ~.{K¤!......F */
    $"ADB5 B3B5 B6B8 C390 1A1C 1E1F 2022 2324"            /* ­µ³µ¶¸Ã.... "#$ */
    $"FE26 081C 6EE1 DBDA E0BF 50F4 E9FF 13FE"            /* þ&..náÛÚà¿Pôéÿ.þ */
    $"895A 5F5D 5B58 5552 4F4C 4844 413E 3A34"            /* Z_][XUROLHDA>:4 */
    $"2111 0BFA 0919 0908 0805 205D 5346 4341"            /* !..úÆ.Æ... ]SFCA */
    $"3E3D 3B39 3633 2F2A 2621 1E1A 1811 24E3"            /* >=;963/*&!....$ã */
    $"E1FF 0B9F 000F 140A 0909 0A0B 0B09 09FD"            /* áÿ.....ÆÆ...ÆÆý */
    $"0A1A 0B0A 0808 0908 0C58 777A 7E82 868A"            /* ......Æ..Xwz~ */
    $"8E91 9598 9CA2 9723 434A 4F25 00FE 02FE"            /* ¢#CJO%.þ.þ */
    $"0314 0201 3D5D 5A5B 5E5E 5F60 6166 6665"            /* ....=]Z[^^_`affe */
    $"6669 6637 6656 1901 0A0F FE10 110B 3270"            /* fif7fV....þ...2p */
    $"7573 7677 787C 5D1A 1C1E 1F20 2223 24FE"            /* usvwx|].... "#$þ */
    $"2608 2053 9A95 9497 834C F4E9 FF13 FE89"            /* &. SLôéÿ.þ */
    $"5A5F 5D5B 5855 524F 4C48 4441 3E3A 3421"            /* Z_][XUROLHDA>:4! */
    $"110B F909 FF08 1605 205D 5346 4341 3E3D"            /* ..ùÆÿ... ]SFCA>= */
    $"3B39 3633 2F2A 2621 1E1A 1811 24E3 F1FF"            /* ;963/*&!....$ãñÿ */
    $"FFFF 01D9 F4FF 04FA 3E02 150C FE0A FF0B"            /* ÿÿ.Ùôÿ.ú>...þ.ÿ. */
    $"020A 0909 FB0A FF08 1609 0427 7073 7B7F"            /* ..ÆÆû.ÿ..Æ.'ps{. */
    $"8387 8A8E 9294 989C A478 3C94 9789 1400"            /* ¤x<.. */
    $"FE02 FE03 2B00 36AE B0B0 B3B4 B6B8 B9BB"            /* þ.þ.+.6®°°³´¶¸¹» */
    $"BEC0 C2C3 CAB5 5F8E 1E05 0E0F 100C 186B"            /* ¾ÀÂÃÊµ_.......k */
    $"CFE4 DFE1 E3E6 E8ED EA44 161E 1F20 2223"            /* ÏäßáãæèíêD... "# */
    $"24FE 2602 1E5F FEFE FF02 E752 F1F8 FFF1"            /* $þ&.._þþÿ.çRñøÿñ */
    $"FF12 AD59 5F5D 5B58 5552 4F4C 4944 413F"            /* ÿ.­Y_][XUROLIDA? */
    $"3A36 2917 0DF9 09FE 0815 0637 5D4C 4541"            /* :6).ÂùÆþ...7]LEA */
    $"3F3D 3C3A 3734 312D 2723 1E1B 1916 0A91"            /* ?=<:741-'#..... */
    $"E2FF 04FA 3E02 150C FE0A FF0B 020A 0909"            /* âÿ.ú>...þ.ÿ...ÆÆ */
    $"FB0A FF08 0709 0427 7073 7B7F 830E 878A"            /* û.ÿ..Æ.'ps{.. */
    $"8E92 9498 9CA4 7B25 5D62 560C 00FE 02FE"            /* ¤{%]bV..þ.þ */
    $"032B 0022 6E72 7172 7476 7777 797D 7F7F"            /* .+."nrqrtvwwy}.. */
    $"8184 7648 701A 070E 0F10 0D16 58A4 B4B1"            /* vHp.....Â.X¤´± */
    $"B3B5 B7B9 BCBA 3A18 1E1F 2022 2324 FE26"            /* ³µ·¹¼º:... "#$þ& */
    $"0820 54D9 DBD8 DEC4 4CF1 E8FF 12AD 595F"            /* . TÙÛØÞÄLñèÿ.­Y_ */
    $"5D5B 5855 524F 4C49 4441 3F3A 3628 170D"            /* ][XUROLIDA?:6(.Â */
    $"FA09 0009 FE08 1506 385D 4B45 413F 3D3C"            /* úÆ.Æþ...8]KEA?=< */
    $"3A37 3431 2D27 231E 1B19 160A 91E2 FF04"            /* :741-'#.....âÿ. */
    $"FA3E 0215 0CFE 0AFF 0B02 0A09 09FB 0AFF"            /* ú>...þ.ÿ...ÆÆû.ÿ */
    $"0816 0904 2770 737B 7F83 878A 8E92 9498"            /* ..Æ.'ps{. */
    $"9CA5 7B1E 494E 4409 00FE 02FE 0314 001B"            /* ¥{.INDÆ.þ.þ.... */
    $"585B 5B5D 5D5E 6061 6266 6768 696B 6033"            /* X[[]]^`abfghik`3 */
    $"4815 0B16 0E0F 100E 143B 6975 7375 7877"            /* H........;iusuxw */
    $"787B 7A2E 1A1E 1F20 2223 24FE 2608 2243"            /* x{z.... "#$þ&."C */
    $"9395 9398 8746 F1E8 FF12 AD59 5F5D 5B58"            /* Fñèÿ.­Y_][X */
    $"5552 4F4C 4944 413F 3A36 2817 0DF9 09FF"            /* UROLIDA?:6(.ÂùÆÿ */
    $"0816 0706 375C 4B45 413F 3D3C 3A37 3431"            /* ....7\KEA?=<:741 */
    $"2D27 231E 1B19 160A 91F1 FFFF FF01 DDF4"            /* -'#.....ñÿÿÿ.Ýô */
    $"FF03 9100 130F FE0A FF0C 020B 0909 FC0A"            /* ÿ....þ.ÿ...ÆÆü. */
    $"1909 0808 0909 0441 7575 7B7F 8387 8B8E"            /* .Æ..ÆÆ.Auu{. */
    $"9294 989C A761 5997 9A4D 00FD 02FF 0332"            /* §aYM.ý.ÿ.2 */
    $"0201 81B5 AEB0 B2B4 B5B8 B9BB BEBF C1C6"            /* ..µ®°²´µ¸¹»¾¿ÁÆ */
    $"D19F 2C13 070D 0E0F 0A17 93E5 DFDD DFE1"            /* Ñ,..Â....åßÝßá */
    $"E2E5 E7EA F46A 111E 1F20 2223 2526 2627"            /* âåçêôj... "#%&&' */
    $"2344 F3FE FF02 EA53 E5F8 FFF1 FF13 D15F"            /* #Dóþÿ.êSåøÿñÿ.Ñ_ */
    $"5E5D 5B58 5552 4F4C 4945 413E 3B37 2E1D"            /* ^][XUROLIEA>;7.. */
    $"0F0A F809 1708 060C 4E57 4843 403D 3B3B"            /* ..øÆ....NWHC@=;; */
    $"3937 342E 2A25 211E 1A17 1026 EAE3 FF0B"            /* 974.*%!....&êãÿ. */
    $"9100 140F 090A 0A0C 0C0B 0909 FC0A 0B09"            /* ...Æ.....ÆÆü..Æ */
    $"0808 0909 0441 7575 7B7F 830D 878B 8E92"            /* ..ÆÆ.Auu{.Â */
    $"9498 9CA8 6135 5F63 2F00 FD02 FF03 3802"            /* ¨a5_c/.ý.ÿ.8. */
    $"0151 7470 7372 7375 7777 7A7D 7F7F 8187"            /* .Qtpsrsuwwz}.. */
    $"6923 1108 0D0E 0F0C 1674 B5B1 AFB2 B2B5"            /* i#..Â....tµ±¯²²µ */
    $"B8B9 BBC2 5714 1E1F 2022 2325 2626 2724"            /* ¸¹»ÂW... "#%&&'$ */
    $"3ECF DDDB DFC7 4DE5 E8FF 12D1 5F5E 5D5B"            /* >ÏÝÛßÇMåèÿ.Ñ_^][ */
    $"5855 524F 4C49 4541 3E3B 372D 1D0F FA09"            /* XUROLIEA>;7-..úÆ */
    $"FE09 1708 060B 4E57 4843 403D 3B3B 3937"            /* þÆ....NWHC@=;;97 */
    $"342E 2A25 211E 1A17 1026 EAE3 FF03 9100"            /* 4.*%!....&êãÿ.. */
    $"130F FE0A FF0C 020B 0909 FC0A 1909 0808"            /* ..þ.ÿ...ÆÆü..Æ.. */
    $"0909 0441 7575 7B7F 8387 8B8E 9294 989C"            /* ÆÆ.Auu{. */
    $"A861 284B 4E25 00FD 02FF 0315 0201 3F5D"            /* ¨a(KN%.ý.ÿ....?] */
    $"5A5A 5B5C 5E60 5F62 6464 6768 6C54 190E"            /* ZZ[\^`_bddghlT.. */
    $"0A0E 220E 0F0D 144D 7471 7073 7675 7477"            /* .."..Â.Mtqpsvutw */
    $"7B7F 3F18 1E1F 2022 2325 2626 2725 368F"            /* {.?... "#%&&'%6 */
    $"9795 9889 45E5 E8FF 13D1 5F5E 5D5B 5855"            /* Eåèÿ.Ñ_^][XU */
    $"524F 4C49 4541 3E3B 372D 1C0F 0AF8 0917"            /* ROLIEA>;7-...øÆ. */
    $"0806 0B4E 5748 4340 3D3B 3B39 3734 2E2A"            /* ...NWHC@=;;974.* */
    $"2521 1E1A 1710 26EA F2FF FFFF 01DE F5FF"            /* %!....&êòÿÿÿ.Þõÿ */
    $"03EF 2907 16FE 0A04 0B0C 0D0A 09FB 0A19"            /* .ï)..þ....Â.Æû.. */
    $"0908 0809 080D 5A76 777B 7F83 878B 8D91"            /* Æ..Æ.ÂZvw{. */
    $"9498 9DA2 4977 9593 2100 FD02 FF03 3200"            /* ¢Iw!.ý.ÿ.2. */
    $"24A5 AEAD B0B2 B4B6 B7B9 BBBD BFC5 C271"            /* $¥®­°²´¶·¹»½¿ÅÂq */
    $"1D04 090D 0D0E 0918 92E2 DCDB DDDF E0E2"            /* ..ÆÂÂ.Æ.âÜÛÝßàâ */
    $"E5E8 E9F9 8A10 1E1F 2022 2324 2626 2726"            /* åèéù... "#$&&'& */
    $"2BC7 FEFF 02EE 5ADE F8FF F1FF 13F4 745B"            /* +Çþÿ.îZÞøÿñÿ.ôt[ */
    $"5C5A 5855 524F 4C49 4541 3E3B 3731 2314"            /* \ZXUROLIEA>;71#. */
    $"0BF8 09FF 0815 032D 604D 4440 3E3B 3B3A"            /* .øÆÿ...-`MD@>;;: */
    $"3734 302C 2723 1E1C 1814 0EB0 E4FF 03EF"            /* 740,'#.....°äÿ.ï */
    $"2907 16FE 0A04 0B0C 0D0A 09FB 0A0B 0908"            /* )..þ....Â.Æû..Æ. */
    $"0809 080D 5B76 777B 7F83 0D87 8B8D 9194"            /* .Æ.Â[vw{.Â */
    $"989D A343 485F 5C14 00FD 02FF 0338 0016"            /* £CH_\..ý.ÿ.8.. */
    $"686F 7072 7374 7577 7879 7B7D 807D 4A13"            /* hoprstuwxy{}}J. */
    $"040A 0D0D 0E0A 1774 B2AF ADAF B2B3 B4B7"            /* ..ÂÂ...t²¯­¯²³´· */
    $"B9BB C76F 131E 1F20 2223 2426 2627 262B"            /* ¹»Ço... "#$&&'&+ */
    $"AAE1 DADE CC51 DEE8 FF13 F474 5B5C 5A58"            /* ªáÚÞÌQÞèÿ.ôt[\ZX */
    $"5552 4F4C 4945 413E 3B37 3123 130A FB09"            /* UROLIEA>;71#..ûÆ */
    $"FE09 FF08 1504 2D61 4E44 403E 3B3B 3A37"            /* þÆÿ...-aND@>;;:7 */
    $"3430 2C27 231E 1C18 140E B0E4 FF03 EF29"            /* 40,'#.....°äÿ.ï) */
    $"0715 FE0A 040B 0C0D 0A09 FB0A 1909 0808"            /* ..þ....Â.Æû..Æ.. */
    $"0908 0D5B 7677 7B7F 8387 8B8D 9194 989D"            /* Æ.Â[vw{. */
    $"A341 374C 4910 00FD 02FF 0315 0012 5258"            /* £A7LI..ý.ÿ....RX */
    $"595A 5B5C 5D5F 5F61 6364 6764 3B10 050B"            /* YZ[\]__acdgd;... */
    $"0D0D 090E 0C14 4E72 7170 6F71 74FE 7515"            /* ÂÂÆ...Nrqpoqtþu. */
    $"7981 4E17 1E1F 2022 2324 2626 2727 2B78"            /* yN... "#$&&''+x */
    $"9894 958B 48DE E8FF 13F4 745B 5C5A 5855"            /* HÞèÿ.ôt[\ZXU */
    $"524F 4C49 4541 3E3B 3730 2213 0BF8 09FF"            /* ROLIEA>;70"..øÆÿ */
    $"0815 032D 604D 4440 3E3B 3B3A 3734 302C"            /* ...-`MD@>;;:740, */
    $"2723 1E1C 1814 0EB0 F2FF FFFF 01DB F5FF"            /* '#.....°òÿÿÿ.Ûõÿ */
    $"0B83 0012 0D0A 0A0B 0B0D 0C08 09FB 0A00"            /* ...Â....Â..Æû.. */
    $"09FE 0815 062D 7276 777B 7F83 878B 8D91"            /* Æþ...-rvw{. */
    $"9498 9F8F 3089 9871 0300 FD02 FF03 3200"            /* 0q..ý.ÿ.2. */
    $"62B4 ABAE B0B2 B3B5 B7B8 BABD C1C4 5A00"            /* b´«®°²³µ·¸º½ÁÄZ. */
    $"1420 080C 0D09 1996 E0DA DADB DCDF E1E2"            /* . ..ÂÆ.àÚÚÛÜßáâ */
    $"E5E8 E9F5 B31C 1D20 2022 2324 2626 2728"            /* åèéõ³..  "#$&&'( */
    $"1F96 FEFF 02F4 5DD1 F8FF F0FF 129B 575C"            /* .þÿ.ô]Ñøÿðÿ.W\ */
    $"5A58 5552 4F4C 4945 413E 3C38 3228 180D"            /* ZXUROLIEA><82(.Â */
    $"F809 FF08 1506 0E4F 5948 423E 3C3B 3A38"            /* øÆÿ....OYHB><;:8 */
    $"3532 2D29 2420 1C19 170A 5DE4 FF0B 8300"            /* 52-)$ ....]äÿ.. */
    $"120D 0A0A 0B0B 0D0C 0809 FB0A 0009 FE08"            /* .Â....Â..Æû..Æþ. */
    $"0706 2C72 7677 7B7F 830D 878B 8D91 9498"            /* ..,rvw{.Â */
    $"9F90 2256 6147 0201 FD02 FF03 3800 3E73"            /* "VaG..ý.ÿ.8.>s */
    $"6D6F 7172 7374 7778 797B 7D7F 3900 1722"            /* moqrstwxy{}.9.." */
    $"080C 0D0A 1678 B1AD ADAE AFB1 B2B4 B7B9"            /* ..Â..x±­­®¯±²´·¹ */
    $"BAC4 8E1B 1D20 2022 2324 2626 2728 2182"            /* ºÄ..  "#$&&'(! */
    $"E4DB DED1 53D1 E7FF 129B 575C 5A58 5552"            /* äÛÞÑSÑçÿ.W\ZXUR */
    $"4F4C 4945 413E 3C38 3227 180D FB09 FE09"            /* OLIEA><82'.ÂûÆþÆ */
    $"FF08 1506 0E4F 5948 423E 3C3B 3A38 3532"            /* ÿ....OYHB><;:852 */
    $"2D29 2420 1C19 170A 5DE4 FF0B 8300 130C"            /* -)$ ....]äÿ.... */
    $"0A0A 0B0B 0D0C 0809 FB0A 0009 FE08 1506"            /* ....Â..Æû..Æþ... */
    $"2C72 7678 7B7F 8387 8B8D 9194 989F 901E"            /* ,rvx{.. */
    $"444D 3902 01FD 02FF 0315 0032 5B58 585B"            /* DM9..ý.ÿ...2[XX[ */
    $"5C5C 5D5F 6161 6365 6631 0017 2108 0C0D"            /* \\]_aacef1..!..Â */
    $"220C 144F 706F 6D6D 6F71 7376 7777 787D"            /* "..Opommoqsvwwx} */
    $"5F1C 1E20 2022 2324 2626 2728 245E 9994"            /* _..  "#$&&'($^ */
    $"958E 47D2 E7FF 129B 575C 5A58 5552 4F4C"            /* GÒçÿ.W\ZXUROL */
    $"4945 413E 3C38 3227 170D F809 FF08 1506"            /* IEA><82'.ÂøÆÿ... */
    $"0F4F 5948 423E 3C3B 3A38 3532 2D29 2420"            /* .OYHB><;:852-)$  */
    $"1C19 170A 5DF2 FFFF FF01 E4F6 FF04 EF29"            /* ....]òÿÿÿ.äöÿ.ï) */
    $"0813 0AFE 0B04 0C0D 0B08 09FB 0A1A 0908"            /* ...þ...Â..Æû..Æ. */
    $"0908 0C51 7775 777B 7F83 888B 8D91 9498"            /* Æ..Qwuw{. */
    $"A174 3891 973F 0001 01FE 0234 0301 0586"            /* ¡t8?...þ.4... */
    $"B0AC ADAF B1B3 B6B9 BABC C0C9 8500 34B7"            /* °¬­¯±³¶¹º¼ÀÉ.4· */
    $"CE54 0609 149C E6DE DEE0 E0E2 E5E6 E8EA"            /* ÎT.Æ.æÞÞààâåæèê */
    $"EBEC F3D6 261B 2020 2224 2526 2727 281E"            /* ëìóÖ&.  "$%&''(. */
    $"7DFE FF02 F95E C5F8 FFF0 FF13 C15A 5B5A"            /* }þÿ.ù^Åøÿðÿ.ÁZ[Z */
    $"5855 524F 4C49 4541 3E3C 3834 2C1C 0F0A"            /* XUROLIEA><84,... */
    $"F909 FE08 1504 235F 4F44 3F3C 3B3A 3936"            /* ùÆþ...#_OD?<;:96 */
    $"332F 2A25 221E 1916 1316 D0E6 FF04 EF29"            /* 3/*%".....Ðæÿ.ï) */
    $"0813 0AFE 0B04 0C0D 0B09 09FB 0A0B 0908"            /* ...þ...Â.ÆÆû..Æ. */
    $"0908 0C51 7775 777B 7F83 0E88 8B8D 9194"            /* Æ..Qwuw{.. */
    $"98A1 7624 5B5E 2700 0101 FE02 3A03 0204"            /* ¡v$[^'...þ.:... */
    $"5470 6E71 7374 7475 7779 7A7C 8157 0137"            /* Tpnqsttuwyz|W.7 */
    $"B8CF 5606 0A12 7BB6 AEAC B1B2 B3B4 B5B7"            /* ¸ÏV...{¶®¬±²³´µ· */
    $"B9BB BBC2 A923 1C20 2022 2425 2627 2728"            /* ¹»»Â©#.  "$%&''( */
    $"206D E0DB DCD5 53C5 E7FF 13C1 5A5B 5A58"            /*  màÛÜÕSÅçÿ.ÁZ[ZX */
    $"5552 4F4C 4945 413E 3C38 342C 1C0F 0AFC"            /* UROLIEA><84,...ü */
    $"09FE 09FE 0815 0424 5E50 443F 3C3B 3A39"            /* ÆþÆþ...$^PD?<;:9 */
    $"3633 2F2A 2522 1E19 1613 16D0 E6FF 04EF"            /* 63/*%".....Ðæÿ.ï */
    $"2908 130A FE0B 040C 0D0B 0809 FB0A 1A09"            /* )...þ...Â..Æû..Æ */
    $"0809 080C 5177 7577 7B7F 8388 8B8D 9194"            /* .Æ..Qwuw{. */
    $"98A1 771D 484C 1E00 0101 FE02 1703 0203"            /* ¡w.HL....þ..... */
    $"425A 595A 595C 5D5D 5F61 6262 6745 0137"            /* BZYZY\]]_abbgE.7 */
    $"B7CD 5507 0B22 1051 736E 6F70 7073 7577"            /* ·ÍU..".Qsnoppsuw */
    $"7778 7A7B 7E74 211D 2020 2224 2526 2727"            /* wxz{~t!.  "$%&'' */
    $"2824 5397 9496 9146 C5E7 FF13 C15A 5B5A"            /* ($SFÅçÿ.ÁZ[Z */
    $"5855 524F 4C49 4541 3E3C 3834 2C1C 0F0A"            /* XUROLIEA><84,... */
    $"F909 FE08 1504 235F 5044 3F3C 3B3A 3936"            /* ùÆþ...#_PD?<;:96 */
    $"332F 2A25 221E 1916 1316 D0F3 FFFF FF01"            /* 3/*%".....Ðóÿÿÿ. */
    $"DEF6 FF03 8300 160E FD0B FF0C 010A 09FA"            /* Þöÿ....ý.ÿ...Æú */
    $"0A1A 0908 0906 1E66 7474 777B 7F83 888B"            /* ..Æ.Æ..fttw{. */
    $"8D91 9498 A35E 4D96 8E1F 0001 01FE 0208"            /* £^M....þ.. */
    $"0300 139F B2B3 B6B5 B4FE B3FF B126 B2B5"            /* ...²³¶µ´þ³ÿ±&²µ */
    $"3908 B5ED F1B3 0D09 5CB2 AEAF B1B2 B4B4"            /* 9.µíñ³ÂÆ\²®¯±²´´ */
    $"B6BA C8CA D0DC E3DA 2A1B 2021 2224 2526"            /* ¶ºÈÊÐÜãÚ*. !"$%& */
    $"2727 291F 75FE FF02 FD66 BBF8 FFF0 FF13"            /* '').uþÿ.ýf»øÿðÿ. */
    $"DA61 5A5A 5754 514F 4C48 4442 3F3C 3834"            /* ÚaZZWTQOLHDB?<84 */
    $"2E20 120B F909 FE08 FF07 133E 5B48 413D"            /* . ..ùÆþ.ÿ..>[HA= */
    $"3A3A 3937 3531 2D28 231F 1A17 1508 8EE6"            /* ::9751-(#.....æ */
    $"FF03 8300 160E FD0B FF0C 010A 09FA 0A0B"            /* ÿ....ý.ÿ...Æú.. */
    $"0908 0906 1E66 7474 777B 7F83 0E88 8B8D"            /* Æ.Æ..fttw{.. */
    $"9194 98A4 5F2E 5F5A 1300 0101 FE02 3A03"            /* ¤_._Z....þ.:. */
    $"010D 6571 7376 7675 7372 7473 7473 7525"            /* .Âeqsvvusrtstsu% */
    $"0BB5 EDF1 B20D 0645 8A85 8788 8A8B 8B8D"            /* .µíñ²Â.E */
    $"929E 9FA5 B0B5 B027 1C20 2122 2425 2627"            /* ¥°µ°'. !"$%&' */
    $"2729 2169 E0DE DDDA 59BB E7FF 13DA 615A"            /* ')!iàÞÝÚY»çÿ.ÚaZ */
    $"5A57 5451 4F4C 4844 423F 3C38 342E 2012"            /* ZWTQOLHDB?<84. . */
    $"0AFC 09FE 09FE 08FF 0713 3F5C 4841 3D3A"            /* .üÆþÆþ.ÿ..?\HA=: */
    $"3A39 3735 312D 2823 1F1A 1715 088E E6FF"            /* :9751-(#.....æÿ */
    $"0383 0016 0EFD 0BFF 0C01 0A09 FA0A 1A09"            /* ....ý.ÿ...Æú..Æ */
    $"0809 061E 6674 7477 7B7F 8388 8B8D 9194"            /* .Æ..fttw{. */
    $"98A4 6123 4B47 0F00 0101 FE02 1703 010B"            /* ¤a#KG....þ..... */
    $"515B 5C5E 5B5C 5B5C 5E5D 5E5C 5C1D 0CB5"            /* Q[\^[\[\^]^\\..µ */
    $"EDF1 B40D 061D 2A53 5253 5557 5758 585C"            /* íñ´Â..*SRSUWWXX\ */
    $"6466 6B72 7673 231D 2021 2224 2526 2627"            /* dfkrvs#. !"$%&&' */
    $"2A28 5097 FE96 0148 BBE7 FF13 DA61 5A5A"            /* *(Pþ.H»çÿ.ÚaZZ */
    $"5754 514F 4C48 4442 3F3C 3834 2E22 130B"            /* WTQOLHDB?<84.".. */
    $"F909 FE08 FF07 133F 5C48 413D 3A3A 3937"            /* ùÆþ.ÿ..?\HA=::97 */
    $"3531 2D28 231F 1A17 1508 8EF3 FFFF FF01"            /* 51-(#.....óÿÿÿ. */
    $"E2F7 FF03 ED23 0D12 FD0B 040C 0D0B 0909"            /* â÷ÿ.í#Â.ý...Â.ÆÆ */
    $"FB0A 0009 FD08 163A 7172 7377 7C7F 8388"            /* û..Æý..:qrsw|. */
    $"8B8E 9193 989F 4B6F 957F 0700 0101 FE02"            /* Ko.....þ. */
    $"3A03 002A 9480 6B5E 5950 4842 3B34 3539"            /* :..*k^YPHB;459 */
    $"380C 26D1 E3ED B00C 1B45 4141 4344 4545"            /* 8.&Ñãí°..EAACDEE */
    $"4647 4344 4642 4443 4520 1E20 2022 2425"            /* FGCDFBDCE .  "$% */
    $"2627 2728 2449 DCFB FDFF 6DAA F8FF F0FF"            /* &''($IÜûýÿmªøÿðÿ */
    $"13F5 7757 5957 5451 4E4B 4844 413F 3B38"            /* .õwWYWTQNKHDA?;8 */
    $"3430 2617 0DF9 09FD 0815 0611 5353 443E"            /* 40&.ÂùÆý....SSD> */
    $"3A3A 3937 3532 2E2A 2420 1C19 160F 30EC"            /* ::9752.*$ ....0ì */
    $"E8FF 03ED 230D 12FD 0B04 0C0D 0B09 09FB"            /* èÿ.í#Â.ý...Â.ÆÆû */
    $"0A00 09FD 0807 3B71 7273 777C 7F83 0E88"            /* ..Æý..;qrsw|.. */
    $"8B8E 9193 98A0 4644 6051 0500 0101 FE02"            /*  FD`Q....þ. */
    $"3A03 001C 6051 433B 3937 3434 322F 333D"            /* :...`QC;97442/3= */
    $"3B0B 26D1 E3ED B008 2A75 7271 7274 7675"            /* ;.&Ñãí°.*urqrtvu */
    $"7679 6B66 695B 5853 4920 1E20 2022 2425"            /* vykfi[XSI .  "$% */
    $"2627 2728 2543 B7D5 D9DC 5EAA E7FF 13F5"            /* &''(%C·ÕÙÜ^ªçÿ.õ */
    $"7757 5957 5451 4E4B 4844 413F 3B38 3430"            /* wWYWTQNKHDA?;840 */
    $"2617 0DFC 09FE 09FD 0815 0611 5252 443E"            /* &.ÂüÆþÆý....RRD> */
    $"3A3A 3937 3532 2E2A 2420 1C19 160F 30EC"            /* ::9752.*$ ....0ì */
    $"E8FF 03ED 230D 12FD 0B04 0C0D 0B09 09FB"            /* èÿ.í#Â.ý...Â.ÆÆû */
    $"0A00 09FE 0817 073A 7172 7377 7C7F 8388"            /* ..Æþ...:qrsw|. */
    $"8B8E 9193 98A1 4533 4B40 0400 0101 FE02"            /* ¡E3K@....þ. */
    $"1703 0017 4C41 3530 2E2D 2A2A 2826 2A33"            /* ....LA50.-**(&*3 */
    $"320A 27D1 E3ED B008 2D22 7C7B 7A7D 7D7F"            /* 2.'Ñãí°.-"|{z}}. */
    $"7E80 8372 6A6E 5D59 5243 201E 2020 2224"            /* ~rjn]YRC .  "$ */
    $"2526 2627 2A29 397C 8F93 964A ABE7 FF13"            /* %&&'*)9|J«çÿ. */
    $"F577 5759 5754 514E 4B48 4441 3F3B 3834"            /* õwWYWTQNKHDA?;84 */
    $"3027 180D F909 FD08 1506 1253 5344 3E3A"            /* 0'.ÂùÆý....SSD>: */
    $"3A39 3735 322E 2A24 201C 1916 0F30 ECF4"            /* :9752.*$ ....0ìô */
    $"FFFF FF01 E4F7 FF03 8500 140C FE0B 050C"            /* ÿÿÿ.ä÷ÿ....þ... */
    $"0D0D 0A09 09FB 0A00 09FE 0817 0E52 7270"            /* ÂÂ.ÆÆû..Æþ...Rrp */
    $"7378 7C7F 8387 8B8E 9193 9A91 3284 996D"            /* sx|.2m */
    $"0100 0101 FE02 3A03 0112 343D 3F41 464D"            /* ....þ.:...4=?AFM */
    $"5559 5F67 6C73 6F19 0EB3 F0E5 5A02 325A"            /* UY_glso..³ðåZ.2Z */
    $"575A 595B 5B5E 6162 6161 625F 5F61 5C21"            /* WZY[[^abaab__a\! */
    $"1D20 2122 2425 2627 2729 292F 5E6A 6677"            /* . !"$%&''))/^jfw */
    $"45A8 F8FF EFFF 1391 5559 5754 514E 4B48"            /* E¨øÿïÿ.UYWTQNKH */
    $"4442 3F3B 3734 312B 1E10 0AFA 09FC 0814"            /* DB?;741+...úÆü.. */
    $"042E 5C49 3F3B 3A39 3735 3330 2C27 221E"            /* ..\I?;:97530,'". */
    $"1A17 140F B7E8 FF03 8500 140C FE0B 050C"            /* ....·èÿ....þ... */
    $"0D0D 0A09 09FB 0A00 09FE 0808 0E52 7270"            /* ÂÂ.ÆÆû..Æþ...Rrp */
    $"7378 7C7F 830E 878B 8E91 939A 9226 5261"            /* sx|..&Ra */
    $"4500 0001 01FE 023A 0301 1139 4B53 5961"            /* E....þ.:...9KSYa */
    $"6B76 7C84 8E92 9A95 200D B2F1 E55B 0061"            /* kv| Â²ñå[.a */
    $"BCB6 B8BA BBBE BFBF C2C0 BEC1 BEBE C1B2"            /* ¼¶¸º»¾¿¿ÂÀ¾Á¾¾Á² */
    $"271C 2021 2224 2526 2727 2927 3784 7D65"            /* '. !"$%&'')'7}e */
    $"713E A7E6 FF13 9155 5957 5451 4E4B 4844"            /* q>§æÿ.UYWTQNKHD */
    $"423F 3B37 3431 2B1D 100A FD09 FE09 FC08"            /* B?;741+...ýÆþÆü. */
    $"1404 2D5C 493F 3B3A 3937 3533 302C 2722"            /* ..-\I?;:97530,'" */
    $"1E1A 1714 0FB7 E8FF 0385 0014 0CFE 0B05"            /* .....·èÿ....þ.. */
    $"0C0D 0D0A 0909 FB0A 0009 FE08 170E 5272"            /* .ÂÂ.ÆÆû..Æþ...Rr */
    $"7073 787C 7F83 878B 8E91 939A 9321 404C"            /* psx|.!@L */
    $"3601 0001 01FE 0217 0301 0E2F 3B42 464D"            /* 6....þ...../;BFM */
    $"555D 6369 7175 7B78 1B0E B3F1 E55B 006C"            /* U]ciqu{x..³ñå[.l */
    $"22D3 CECE D1D2 D6D5 D5D8 D7D8 DAD5 D2D8"            /* "ÓÎÎÑÒÖÕÕØ×ØÚÕÒØ */
    $"C928 1B20 2122 2425 2627 2728 273B 8A78"            /* É(. !"$%&''(';x */
    $"575D 38A7 E6FF 1391 5559 5754 514E 4B48"            /* W]8§æÿ.UYWTQNKH */
    $"4442 3F3B 3734 312B 1D10 0AFA 09FC 0814"            /* DB?;741+...úÆü.. */
    $"042D 5B49 3F3B 3A39 3735 3330 2C27 221E"            /* .-[I?;:97530,'". */
    $"1A17 140F B7F4 FFFF FF01 E1F8 FF05 F930"            /* ....·ôÿÿÿ.áøÿ.ù0 */
    $"0B11 0B0B FE0C 040D 0C0A 0909 FB0A FE08"            /* ....þ..Â..ÆÆû.þ. */
    $"1506 1F65 7070 7478 7C7F 8387 8B8D 9093"            /* ...epptx|. */
    $"9C7C 338A 7B34 00FE 01FE 023A 0300 2F69"            /* |3{4.þ.þ.:../i */
    $"696E 6D6E 706E 6D6E 6E71 7578 3000 317C"            /* inmnpnmnnqux0.1| */
    $"5308 134D 5355 585C 5B58 5A5C 5C5E 6061"            /* S..MSUX\[XZ\\^`a */
    $"6265 695F 201D 2020 2224 2526 2728 2827"            /* bei_ .  "$%&'((' */
    $"3C78 766F 6B3A 9BF8 FFEF FF13 B155 5857"            /* <xvok:øÿïÿ.±UXW */
    $"5350 4E4B 4844 413E 3B37 3332 2E23 140B"            /* SPNKHDA>;732.#.. */
    $"FA09 FC08 1406 0D4D 5341 3C3A 3837 3634"            /* úÆü...ÂMSA<:8764 */
    $"312D 2823 1F1A 1716 0784 E9FF 05F9 300B"            /* 1-(#.....éÿ.ù0. */
    $"110B 0BFE 0C04 0D0C 0A09 09FB 0AFE 0809"            /* ...þ..Â..ÆÆû.þ.Æ */
    $"0620 6570 7074 787C 7F83 0B87 8B8D 9093"            /* . epptx|.. */
    $"9C7E 2157 4E22 00FE 01FE 023A 0300 3E8F"            /* ~!WN".þ.þ.:..> */
    $"8F93 9394 9394 9595 9698 999F 3D00 317C"            /* =.1| */
    $"5205 1C9D ACAA ACAF B1B2 B3B4 B5B8 BABC"            /* R..¬ª¬¯±²³´µ¸º¼ */
    $"BFC1 C6B0 251C 2020 2224 2526 2728 2823"            /* ¿ÁÆ°%.  "$%&'((# */
    $"52DD DAC9 C358 98E6 FF13 B155 5857 5350"            /* RÝÚÉÃXæÿ.±UXWSP */
    $"4E4B 4844 413E 3B37 3332 2E22 140B FD09"            /* NKHDA>;732."..ýÆ */
    $"FE09 FC08 1406 0D4D 5241 3C3A 3837 3634"            /* þÆü...ÂMRA<:8764 */
    $"312D 2823 1F1A 1716 0784 E9FF 05F9 300B"            /* 1-(#.....éÿ.ù0. */
    $"110B 0BFE 0CFF 0D02 0A09 09FB 0AFE 0815"            /* ...þ.ÿÂ..ÆÆû.þ.. */
    $"0620 6570 7074 787C 7F83 878B 8D90 939C"            /* . epptx|. */
    $"7E1B 453E 1A00 FE01 FE02 1703 0032 7370"            /* ~.E>..þ.þ....2sp */
    $"7473 7275 7475 7979 7879 7E31 0032 7C52"            /* tsrutuyyxy~1.2|R */
    $"031F AF22 C1BF C1C1 C4C6 C6C7 C9CC CFD1"            /* ..¯"Á¿ÁÁÄÆÆÇÉÌÏÑ */
    $"D3D4 DEC5 251C 2020 2224 2526 2728 2822"            /* ÓÔÞÅ%.  "$%&'((" */
    $"58F6 F2DF D75E 97E6 FF13 B155 5857 5350"            /* Xöòß×^æÿ.±UXWSP */
    $"4E4B 4844 413E 3B37 3332 2E23 150B FA09"            /* NKHDA>;732.#..úÆ */
    $"FC08 1406 0D4D 5241 3C3A 3837 3634 312D"            /* ü...ÂMRA<:87641- */
    $"2823 1F1A 1716 0784 F4FF FFFF 01D2 F8FF"            /* (#.....ôÿÿÿ.Òøÿ */
    $"02A0 0213 FC0C 020D 0E0B FE09 FB0A FE08"            /* . ..ü..Â..þÆû.þ. */
    $"1507 3B70 6F70 7377 7B7F 8387 898D 9193"            /* ..;popsw{. */
    $"9F68 152D 3317 00FE 01FD 0217 003A 6963"            /* h.-3..þ.ý...:ic */
    $"6466 6A6C 6D6E 6E6C 6F72 7763 1300 0200"            /* dfjlmnnlorwc.... */
    $"0F3E 5454 FE57 FF58 1C59 5A5B 5D5E 6266"            /* .>TTþWÿX.YZ[]^bf */
    $"6667 521D 1E20 2022 2324 2627 2828 273D"            /* fgR..  "#$&'(('= */
    $"797D 8085 468B F8FF EFFF 13CC 5856 5653"            /* y}Føÿïÿ.ÌXVVS */
    $"504E 4B48 4440 3E3B 3733 322F 2719 0EF9"            /* PNKHD@>;732/'..ù */
    $"09FC 0813 0327 5845 3C39 3737 3634 312E"            /* Æü...'XE<977641. */
    $"2924 201B 1816 0B51 E9FF 02A0 0213 FC0C"            /* )$ ....Qéÿ. ..ü. */
    $"020D 0E0B FE09 FB0A FE08 0907 3B70 6F70"            /* .Â..þÆû.þ.Æ.;pop */
    $"7377 7B7F 830B 8789 8D91 939F 680E 233B"            /* sw{..h.#; */
    $"1F00 FE01 FD02 3900 4E8E 8889 8A8C 8D8F"            /* ..þ.ý.9.N */
    $"9192 9496 989F 8216 0002 0015 79AD A9AB"            /* .....y­©« */
    $"ACAF B0B2 B3B4 B5B7 B9BB BDBF C994 1C1D"            /* ¬¯°²³´µ·¹»½¿É.. */
    $"2020 2223 2426 2728 2823 55DB E1E3 F073"            /*   "#$&'((#UÛáãðs */
    $"87E6 FF13 CC58 5656 5350 4E4B 4844 403E"            /* æÿ.ÌXVVSPNKHD@> */
    $"3B37 3332 2F27 180D FD09 FD09 FC08 1303"            /* ;732/'.ÂýÆýÆü... */
    $"2759 453D 3937 3736 3431 2E29 2420 1B18"            /* 'YE=977641.)$ .. */
    $"160B 51E9 FF02 A002 13FC 0C02 0D0E 0BFE"            /* ..Qéÿ. ..ü..Â..þ */
    $"09FB 0AFE 0815 073C 706F 7073 777B 7F83"            /* Æû.þ...<popsw{. */
    $"8789 8D91 939F 680A 1D2F 1900 FE01 FD02"            /* h../..þ.ý. */
    $"1600 3E71 6C6A 6A6C 7170 7275 7477 7B7F"            /* ..>qljjlqprutw{. */
    $"6714 0002 0017 87C3 22BD BFC0 C1C3 C5C6"            /* g.....Ã"½¿ÀÁÃÅÆ */
    $"C8CB CDCD CFD4 D6DE A51C 1D20 2022 2324"            /* ÈËÍÍÏÔÖÞ¥..  "#$ */
    $"2627 2828 225A F0F8 FBFF 7D85 E6FF 13CC"            /* &'(("Zðøûÿ}æÿ.Ì */
    $"5856 5653 504E 4B48 4440 3E3B 3733 322F"            /* XVVSPNKHD@>;732/ */
    $"2719 0DF9 09FC 0813 0327 5945 3C39 3737"            /* '.ÂùÆü...'YE<977 */
    $"3634 312E 2924 201B 1816 0B51 F4FF FFFF"            /* 641.)$ ....Qôÿÿÿ */
    $"01DC F9FF 03FE 4208 11FD 0CFE 0E00 0AFE"            /* .Üùÿ.þB..ý.þ...þ */
    $"09FB 0A18 0908 070F 5270 6E70 7377 7B7F"            /* Æû..Æ...Rpnpsw{. */
    $"8387 898D 9193 A055 264A 5215 00FE 01FD"            /*  U&JR..þ.ý */
    $"0239 0140 6764 6667 6869 6A6D 6F6D 6D71"            /* .9.@gdfghijmommq */
    $"747A 633E 1C29 4353 5052 5554 5457 5A5B"            /* tzc>.)CSPRUTTWZ[ */
    $"5A5D 5D5E 6064 6368 4318 1E20 2122 2324"            /* Z]]^`dchC.. !"#$ */
    $"2627 2828 2641 7B7D 7C81 4D76 F8FF EFFF"            /* &'((&A{}|Mvøÿïÿ */
    $"14E3 6155 5552 4F4D 4A47 4340 3D3B 3834"            /* .ãaUUROMJGC@=;84 */
    $"312F 2A1E 110A FA09 FC08 1406 0B43 4D3F"            /* 1/*...úÆü....CM? */
    $"3937 3736 3433 2F2B 2621 1C19 1712 23DE"            /* 977643/+&!....#Þ */
    $"EBFF 03FE 4208 11FD 0CFE 0E00 0AFE 09FB"            /* ëÿ.þB..ý.þ...þÆû */
    $"0A0C 0908 070F 5170 6E6F 7377 7B7F 830B"            /* ..Æ...Qpnosw{.. */
    $"8789 8D91 93A0 5537 6970 1C00 FE01 FD02"            /*  U7ip..þ.ý. */
    $"3900 558C 8789 8A8B 8D8F 9091 9396 9899"            /* 9.U */
    $"A080 4D29 508A ACA7 A8AB ACAD AFB1 B3B3"            /*  M)P¬§¨«¬­¯±³³ */
    $"B5B6 B9BB BDBF CB77 141E 2021 2223 2426"            /* µ¶¹»½¿Ëw.. !"#$& */
    $"2728 2821 5DDC DEDF E980 75E6 FF13 E361"            /* '((!]ÜÞßéuæÿ.ãa */
    $"5555 524F 4D4A 4743 403D 3B38 3431 2F29"            /* UUROMJGC@=;841/) */
    $"1E11 FD09 FD09 FC08 1406 0B43 4D3F 3937"            /* ..ýÆýÆü....CM?97 */
    $"3736 3433 2F2B 2621 1C19 1712 23DE EBFF"            /* 7643/+&!....#Þëÿ */
    $"03FE 4208 11FD 0CFE 0E00 0AFE 09FB 0A18"            /* .þB..ý.þ...þÆû.. */
    $"0908 070F 5270 6E70 7377 7B7F 8387 898D"            /* Æ...Rpnpsw{. */
    $"9193 A055 2952 5916 00FE 01FD 0216 0042"            /*  U)RY..þ.ý...B */
    $"706A 696A 6E72 7070 7374 7779 7B80 683D"            /* pjijnrppstwy{h= */
    $"2658 9ABE BB04 BBBD C2C4 C6FE C71A C9CB"            /* &X¾».»½ÂÄÆþÇ.ÉË */
    $"CFD3 D3D2 E383 131E 2021 2223 2426 2728"            /* ÏÓÓÒã.. !"#$&'( */
    $"2820 63F2 F5F5 FF8C 73E6 FF13 E361 5555"            /* ( còõõÿsæÿ.ãaUU */
    $"524F 4D4A 4743 403D 3B38 3431 2F2A 1E11"            /* ROMJGC@=;841/*.. */
    $"F909 FC08 1406 0B43 4D3F 3937 3736 3433"            /* ùÆü....CM?977643 */
    $"2F2B 2621 1C19 1712 23DE F5FF FFFF 01E1"            /* /+&!....#Þõÿÿÿ.á */
    $"F9FF 03D8 1110 0DFE 0C03 0D0E 0E0C FD09"            /* ùÿ.Ø..Âþ..Â...ýÆ */
    $"FB0A FF08 1607 1B61 6D6C 6F73 777B 7F82"            /* û.ÿ....amlosw{. */
    $"868A 8D8F 9498 3843 584A 0500 FE01 FC02"            /* 8CXJ..þ.ü. */
    $"0842 6864 6666 6568 686B FD6F 2C70 757D"            /* .Bhdffehhkýo,pu} */
    $"783F 4F52 5053 5352 5354 575A 5A59 595B"            /* x?ORPSSRSTWZZYY[ */
    $"5E5F 6063 6737 191E 1F20 2223 2426 2727"            /* ^_`cg7... "#$&'' */
    $"2825 497C 7B7A 8055 5FFC F9FF EFFF 14F7"            /* (%I|{zU_üùÿïÿ.÷ */
    $"7053 5551 4E4C 4947 4340 3D39 3634 312E"            /* pSUQNLIGC@=9641. */
    $"2B23 150B FA09 FC08 1406 0B4A 5143 3A36"            /* +#..úÆü....JQC:6 */
    $"3536 3433 302C 2822 1E1A 1715 078E EBFF"            /* 56430,(".....ëÿ */
    $"03D8 1110 0DFE 0C03 0D0E 0E0C FD09 FB0A"            /* .Ø..Âþ..Â...ýÆû. */
    $"FF08 0A07 1B61 6D6C 6F73 777B 7F82 0B86"            /* ÿ....amlosw{.. */
    $"8A8D 8F94 983A 5B76 6506 00FE 01FD 023A"            /* :[ve..þ.ý.: */
    $"0159 8B86 8889 8B8C 8E90 9192 9597 999A"            /* .Y */
    $"A29E 67A5 A9A4 A5A8 A9AA ADAF B1B2 B3B4"            /* ¢g¥©¤¥¨©ª­¯±²³´ */
    $"B6B8 BABC BEC7 5C13 1E1F 2022 2324 2627"            /* ¶¸º¼¾Ç\... "#$&' */
    $"2728 2170 DFDC DEE7 8E5F FDE7 FF14 F770"            /* '(!pßÜÞç_ýçÿ.÷p */
    $"5355 514E 4C49 4743 403D 3936 3431 2E2B"            /* SUQNLIGC@=9641.+ */
    $"2315 0BFE 09FD 09FC 0814 060B 4A51 433A"            /* #..þÆýÆü....JQC: */
    $"3635 3634 3330 2C28 221E 1A17 1507 8EEB"            /* 656430,(".....ë */
    $"FF03 D811 100D FE0C 030D 0E0E 0CFD 09FB"            /* ÿ.Ø..Âþ..Â...ýÆû */
    $"0AFF 0816 071B 616D 6C6F 7377 7B7F 8286"            /* .ÿ....amlosw{. */
    $"8A8D 8F94 9839 455B 5005 00FE 01FC 0215"            /* 9E[P..þ.ü.. */
    $"456F 6968 6A6E 6F70 7071 7677 7576 7B82"            /* Eoihjnoppqvwuv{ */
    $"7A65 BABB B6B8 04BA BDC3 C5C4 FEC6 1BC7"            /* zeº»¶¸.º½ÃÅÄþÆ.Ç */
    $"CACD D0D2 D4DB 6413 1E1F 2022 2324 2627"            /* ÊÍÐÒÔÛd... "#$&' */
    $"2728 1F79 F7F3 F5FF 9C61 FDE7 FF14 F770"            /* '(.y÷óõÿaýçÿ.÷p */
    $"5355 514E 4C49 4743 403D 3936 3431 2E2B"            /* SUQNLIGC@=9641.+ */
    $"2314 0AFA 09FC 0814 060C 4A51 433A 3735"            /* #..úÆü....JQC:75 */
    $"3634 3330 2C28 221E 1A17 1507 8EF5 FFFF"            /* 6430,(".....õÿÿ */
    $"FF01 E6F9 FF0A 9709 110D 0C0C 0D0D 0E0E"            /* ÿ.æùÿ.Æ.Â..ÂÂ.. */
    $"0BFD 09FC 0A19 0908 0806 2767 6B6B 6E73"            /* .ýÆü..Æ...'gkkns */
    $"777B 7F82 8589 8D8F 958D 2349 5545 0300"            /* w{.#IUE.. */
    $"FE01 FD02 0600 3B68 6162 6466 FE6A 306E"            /* þ.ý...;habdfþj0n */
    $"7173 7170 7277 723B 4E4F 5156 5653 5355"            /* qsqprwr;NOQVVSSU */
    $"5657 5859 5A5B 5C5E 6063 652D 1A1E 1F20"            /* VWXYZ[\^`ce-...  */
    $"2223 2426 2727 2826 517B 787B 805E 56FA"            /* "#$&''(&Q{x{^Vú */
    $"F9FF EFFF 14FC 7D51 5451 4E4C 4947 4340"            /* ùÿïÿ.ü}QTQNLIGC@ */
    $"3D39 3634 312E 2B26 180C FA09 FC08 1406"            /* =9641.+&..úÆü... */
    $"016B 6047 3C36 3435 3432 302D 2923 1F1B"            /* .k`G<645420-)#.. */
    $"1716 095A EBFF 0A97 0911 0D0C 0C0D 0D0E"            /* ..ÆZëÿ.Æ.Â..ÂÂ. */
    $"0E0B FD09 FC0A 0D09 0808 0627 676B 6B6E"            /* ..ýÆü.ÂÆ...'gkkn */
    $"7377 7B7F 820B 8589 8D8F 958C 2765 735C"            /* sw{..'es\ */
    $"0400 FE01 FD02 3A00 4F8B 8587 898B 8C8E"            /* ..þ.ý.:.O */
    $"9091 9295 9798 9A9D 9462 A0A3 A4A6 A8A9"            /* b £¤¦¨© */
    $"AAAC AEB0 B2B3 B3B5 B7B9 BBBE BF43 171E"            /* ª¬®°²³³µ·¹»¾¿C.. */
    $"1F20 2223 2426 2727 2821 81E0 DADE E69E"            /* . "#$&''(!àÚÞæ */
    $"5AFA E7FF 14FC 7D51 5451 4E4C 4947 4340"            /* Zúçÿ.ü}QTQNLIGC@ */
    $"3D39 3634 312E 2B26 180D FE09 FD09 FC08"            /* =9641.+&.ÂþÆýÆü. */
    $"1406 016B 6047 3C36 3435 3432 302D 2923"            /* ...k`G<645420-)# */
    $"1F1B 1716 095A EBFF 0A97 0911 0D0C 0C0D"            /* ....ÆZëÿ.Æ.Â..Â */
    $"0D0E 0E0B FD09 FC0A 1909 0808 0627 676B"            /* Â...ýÆü..Æ...'gk */
    $"6B6E 7377 7B7F 8285 898D 8F95 8D24 4E5A"            /* knsw{.$NZ */
    $"4904 00FE 01FD 0207 003D 706C 6B69 696C"            /* I..þ.ý...=plkiil */
    $"FE70 FE74 0875 7880 7361 B7B6 B8B8 23BA"            /* þpþt.uxsa·¶¸¸#º */
    $"BDC1 C4C3 C6C6 C7C9 CACA CCCF D4D1 4816"            /* ½ÁÄÃÆÆÇÉÊÊÌÏÔÑH. */
    $"1E1F 2022 2324 2627 2728 208C F6F0 F6FE"            /* .. "#$&''( öðöþ */
    $"AD5B FAE7 FF14 FC7D 5154 514E 4C49 4743"            /* ­[úçÿ.ü}QTQNLIGC */
    $"403D 3936 3431 2E2B 2618 0CFA 09FC 0814"            /* @=9641.+&..úÆü.. */
    $"0601 6B60 473C 3634 3534 3230 2D29 231F"            /* ..k`G<645420-)#. */
    $"1B17 1609 5AF5 FFFF FF01 E1FA FF02 FA3C"            /* ...ÆZõÿÿÿ.áúÿ.ú< */
    $"0BFB 0DFF 0E00 0AFD 09FD 0A00 09FE 0801"            /* .ûÂÿ...ýÆý..Æþ.. */
    $"0635 FE6A 116D 7277 7B7E 8185 898C 8E96"            /* .5þj.mrw{~ */
    $"7C1D 4E55 4002 00FE 01FD 023A 0033 6661"            /* |.NU@..þ.ý.:.3fa */
    $"6467 686A 6C6A 6B6F 7273 7271 766F 394D"            /* dghjljkorsrqvo9M */
    $"4E51 5351 5253 5455 5758 5B5B 5C5D 5E5F"            /* NQSQRSTUWX[[\]^_ */
    $"625D 221C 1E1F 2022 2324 2626 2828 265A"            /* b]"... "#$&&((&Z */
    $"7C78 7A7F 6441 F3F9 FFEE FF13 934E 5351"            /* |xz.dAóùÿîÿ.NSQ */
    $"4E4C 4946 4240 3D39 3633 302D 2B27 1C0F"            /* NLIFB@=9630-+'.. */
    $"FA09 FB08 1400 6A78 443F 3733 3433 3230"            /* úÆû...jxD?734320 */
    $"2E2A 2420 1C18 150F 34F6 EDFF 02FA 3C0B"            /* .*$ ....4öíÿ.ú<. */
    $"FB0D 020E 0D0A FD09 FD0A 0009 FE08 0106"            /* ûÂ..Â.ýÆý..Æþ... */
    $"35FE 6A05 6D72 777B 7E81 0B85 898C 8E96"            /* 5þj.mrw{~. */
    $"7B24 6A73 5602 00FE 01FD 023A 0044 8B86"            /* {$jsV..þ.ý.:.D */
    $"8789 8A8B 8D8F 9091 9496 9799 9D8F 63A3"            /* c£ */
    $"A2A3 A5A7 A8AA ACAD AFB1 B3B4 B4B5 B8BB"            /* ¢£¥§¨ª¬­¯±³´´µ¸» */
    $"C0AE 291A 1E1F 2022 2324 2626 2827 2495"            /* À®)... "#$&&('$ */
    $"DFD9 DBE4 A847 F4E6 FF13 934E 5351 4E4C"            /* ßÙÛä¨Gôæÿ.NSQNL */
    $"4946 4240 3D39 3633 302D 2B27 1C0F FE09"            /* IFB@=9630-+'..þÆ */
    $"FD09 FB08 1400 6A78 4540 3733 3433 3230"            /* ýÆû...jxE@734320 */
    $"2E2A 2420 1C18 150F 34F6 EDFF 02FA 3C0B"            /* .*$ ....4öíÿ.ú<. */
    $"FB0D 010E 0DFC 09FD 0A00 09FE 0801 0635"            /* ûÂ..ÂüÆý..Æþ...5 */
    $"FE6A 116D 7277 7B7E 8185 898C 8E96 7C1D"            /* þj.mrw{~|. */
    $"525B 4402 00FE 01FD 0216 0036 6D6B 6D6C"            /* R[D..þ.ý...6mkml */
    $"696E 6E6D 6E70 7273 7477 7E6F 63B7 B5B6"            /* innmnprstw~oc·µ¶ */
    $"B823 BBBF BEBE C1C2 C5CA CDCD CBCC CFD5"            /* ¸#»¿¾¾ÁÂÅÊÍÍËÌÏÕ */
    $"C42C 191E 1F20 2223 2426 2628 2724 A2F4"            /* Ä,... "#$&&('$¢ô */
    $"EDF2 FCB8 47F3 E6FF 1493 4E53 514E 4C49"            /* íòü¸Góæÿ.NSQNLI */
    $"4642 403D 3936 3330 2D2B 271C 100A FB09"            /* FB@=9630-+'...ûÆ */
    $"FB08 1400 6A78 443F 3733 3433 3230 2E2A"            /* û...jxD?734320.* */
    $"2420 1C18 150F 34F6 F6FF FFFF 01E7 FAFF"            /* $ ....4ööÿÿÿ.çúÿ */
    $"02C4 0D10 FD0D 030E 0F0F 0CFC 09FD 0A1A"            /* .ÄÂ.ýÂ.....üÆý.. */
    $"0908 0807 0741 6B69 696D 7276 7A7D 8185"            /* Æ....Akiimrvz} */
    $"888A 8E98 6C21 5255 3E02 00FE 01FD 023A"            /* l!RU>..þ.ý.: */
    $"002A 6663 6464 6567 696A 6D6F 7273 7474"            /* .*fcddegijmorstt */
    $"766D 364D 4D4F 5050 5252 5356 5B5D 5B5A"            /* vm6MMOPPRRSV[][Z */
    $"5B5C 5D5F 6544 181D 1E1F 2121 2324 2526"            /* [\]_eD....!!#$%& */
    $"2727 2B64 7877 7A7F 6A41 EEF9 FFEE FF14"            /* ''+dxwz.jAîùÿîÿ. */
    $"AA4B 5250 4D4B 4845 413F 3B39 3633 302D"            /* ªKRPMKHEA?;9630- */
    $"2B28 2012 0BFB 09FB 0805 005B B443 4438"            /* +( ..ûÆû...[´CD8 */
    $"FE33 0B32 312E 2B25 211D 1A17 1315 C7ED"            /* þ3.21.+%!.....Çí */
    $"FF02 C40D 10FD 0D03 0E0F 0F0C FC09 FD0A"            /* ÿ.ÄÂ.ýÂ.....üÆý. */
    $"0E09 0808 0707 426C 6969 6D72 767A 7D81"            /* .Æ....Bliimrvz} */
    $"0B85 888A 8E98 6A2B 6E71 5301 00FE 01FD"            /* .j+nqS..þ.ý */
    $"023A 0038 8885 8688 898A 8C8E 8F90 9395"            /* .:.8 */
    $"9698 9C8D 5FA3 A1A2 A4A5 A7A9 ABAC AEB0"            /* _£¡¢¤¥§©«¬®° */
    $"B3B3 B4B6 B7B9 C578 141D 1E1F 2121 2324"            /* ³³´¶·¹Åx....!!#$ */
    $"2526 2726 2DAD DAD8 DBE2 BA47 EEE6 FF16"            /* %&'&-­ÚØÛâºGîæÿ. */
    $"AA4B 5250 4D4B 4845 413F 3B39 3633 302D"            /* ªKRPMKHEA?;9630- */
    $"2B28 2012 0B09 09FD 09FB 0805 005B B443"            /* +( ..ÆÆýÆû...[´C */
    $"4438 FE33 0B32 312E 2B25 211D 1A17 1315"            /* D8þ3.21.+%!..... */
    $"C7ED FF02 C40D 10FD 0D03 0E0F 0F0C FC09"            /* Çíÿ.ÄÂ.ýÂ.....üÆ */
    $"FD0A 1A09 0808 0707 416B 6969 6D72 767A"            /* ý..Æ....Akiimrvz */
    $"7D81 8588 8A8E 986C 2255 5940 0200 FE01"            /* }l"UY@..þ. */
    $"FD02 1600 2C69 6A6C 6C6A 6E70 6F6E 7074"            /* ý...,ijlljnponpt */
    $"7778 767A 6C63 B8B7 B6B8 23BD C0C0 BFBF"            /* wxvzlc¸·¶¸#½ÀÀ¿¿ */
    $"C1C4 C7C9 C9CC CBCF DA86 131C 1E1F 2121"            /* ÁÄÇÉÉÌËÏÚ....!! */
    $"2324 2526 2726 2DBE F0EE F1FA CC49 EEE6"            /* #$%&'&-¾ðîñúÌIîæ */
    $"FF14 AA4B 5250 4D4B 4845 413F 3B39 3633"            /* ÿ.ªKRPMKHEA?;963 */
    $"302D 2B28 2012 0BFB 09FB 0805 005B B443"            /* 0-+( ..ûÆû...[´C */
    $"4338 FE33 0B32 312E 2B25 211D 1A17 1315"            /* C8þ3.21.+%!..... */
    $"C7F6 FFFF FF01 E9FA FF02 8906 10FD 0D03"            /* Çöÿÿÿ.éúÿ...ýÂ. */
    $"0E0F 0F0B FC09 FD0A 1909 0808 070B 486A"            /* ....üÆý..Æ....Hj */
    $"6869 6D72 7679 7C80 8487 8A8D 995B 2653"            /* himrvy|[&S */
    $"533C 03FD 01FE 0206 0300 1E62 6363 64FE"            /* S<.ý.þ.....bccdþ */
    $"6514 686C 6E6F 7274 7574 6935 4E4F 5250"            /* e.hlnortuti5NORP */
    $"5155 5654 575B 5CFE 5A19 5C5D 5D63 2F18"            /* QUVTW[\þZ.\]]c/. */
    $"1D1E 1F20 2123 2325 2627 2533 6F77 7879"            /* ... !##%&'%3owxy */
    $"7E6D 3DE4 F9FF EEFF 14B7 4D51 4F4C 4A47"            /* ~m=äùÿîÿ.·MQOLJG */
    $"4440 3E3C 3936 322F 2D2A 2923 150C FB09"            /* D@><962/-*)#..ûÆ */
    $"FB08 1400 39F5 6741 3B34 3132 3230 2D2B"            /* û...9õgA;41220-+ */
    $"2622 1D19 1715 0581 EDFF 0289 0610 FD0D"            /* &".....íÿ...ýÂ */
    $"030E 0F0F 0BFC 09FD 0A0E 0908 0807 0B48"            /* .....üÆý..Æ....H */
    $"6A68 696D 7276 797C 800B 8487 8A8D 995A"            /* jhimrvy|.Z */
    $"326F 7152 0100 FE01 FE02 3B03 0026 8385"            /* 2oqR..þ.þ.;..& */
    $"8687 888A 8C8C 8F90 9195 9697 9C8A 60A6"            /* `¦ */
    $"A0A2 A3A5 A7A8 ABAD AEB0 B2B3 B4B4 B2B3"            /*  ¢£¥§¨«­®°²³´´²³ */
    $"BD4A 131D 1E1F 2021 2323 2526 2722 41C8"            /* ½J.... !##%&'"AÈ */
    $"D7D8 DAE1 BB43 E4E6 FF16 B74D 514F 4C4A"            /* ×ØÚá»Cäæÿ.·MQOLJ */
    $"4744 403E 3C39 3632 2F2D 2A29 2315 0C09"            /* GD@><962/-*)#..Æ */
    $"09FD 09FB 0814 0039 F567 413A 3431 3232"            /* ÆýÆû...9õgA:4122 */
    $"302D 2B26 221D 1917 1505 81ED FF02 8906"            /* 0-+&".....íÿ.. */
    $"10FD 0D03 0E0F 0F0B FC09 FD0A 1A09 0808"            /* .ýÂ.....üÆý..Æ.. */
    $"070B 486B 6869 6D72 7679 7C80 8487 8A8D"            /* ..Hkhimrvy| */
    $"995B 2757 5740 0100 FE01 FE02 0803 001F"            /* ['WW@..þ.þ..... */
    $"6668 6A6A 6B6D FE70 0172 75FE 7706 7968"            /* fhjjkmþp.ruþw.yh */
    $"67BA B5B5 B623 BCBD BEBE C1C2 C3C4 C5C8"            /* gºµµ¶#¼½¾¾ÁÂÃÄÅÈ */
    $"CBC6 C8D1 5012 1D1E 1F20 2123 2325 2627"            /* ËÆÈÑP.... !##%&' */
    $"2244 DEEB EDF0 F9CD 44E4 E6FF 14B7 4D51"            /* "DÞëíðùÍDäæÿ.·MQ */
    $"4F4C 4A47 4440 3E3C 3936 322F 2D2A 2923"            /* OLJGD@><962/-*)# */
    $"150C FB09 FB08 1400 3AF5 6641 3B34 3132"            /* ..ûÆû...:õfA;412 */
    $"3230 2D2B 2622 1D19 1715 0581 F6FF FFFF"            /* 20-+&".....öÿÿÿ */
    $"01EA FBFF 03F3 2E10 0EFE 0DFF 0E01 0F0D"            /* .êûÿ.ó...þÂÿ...Â */
    $"FB09 FD0A 1A09 0808 0710 5269 6768 6C72"            /* ûÆý..Æ....Righlr */
    $"7579 7C80 8487 8A8D 994F 2E51 533C 0100"            /* uy|O.QS<.. */
    $"FE01 FE02 3B03 0110 5C63 6366 6765 6568"            /* þ.þ.;...\ccfgeeh */
    $"6C6B 6E6F 7372 726B 324E 4F52 5353 5456"            /* lknosrrk2NORSSTV */
    $"5457 595A 5B5C 5D5F 5A5A 4E1F 1B1C 1E1F"            /* TWYZ[\]_ZZN..... */
    $"2021 2223 2525 2623 4276 7776 797D 6F3D"            /*  !"#%%&#Bvwvy}o= */
    $"DAF9 FFEE FF14 C650 4F4D 4B49 4744 403E"            /* Úùÿîÿ.ÆPOMKIGD@> */
    $"3C39 3632 2F2D 2A29 2519 0EFB 09FB 0806"            /* <962/-*)%..ûÆû.. */
    $"021D FBB6 3F3E 34FD 3009 2E2C 2722 1E1A"            /* ..û¶?>4ý0Æ.,'".. */
    $"1715 095B EEFF 03F3 2E10 0EFE 0DFF 0E01"            /* ..Æ[îÿ.ó...þÂÿ.. */
    $"0F0D FB09 FD0A 0E09 0808 0710 5269 6768"            /* .ÂûÆý..Æ....Righ */
    $"6C72 7579 7C80 0B84 878A 8D99 4F40 6F70"            /* lruy|.O@op */
    $"5101 00FE 01FE 023B 0300 147B 8584 8687"            /* Q..þ.þ.;...{ */
    $"898B 8B8E 9092 9495 979C 895D A6A0 A1A2"            /* ]¦ ¡¢ */
    $"A5A7 A8AA ACAD AFB1 B1B2 B2AF B294 2019"            /* ¥§¨ª¬­¯±±²²¯² . */
    $"1C1E 1F20 2122 2325 2526 1E63 D4D4 D6D9"            /* ... !"#%%&.cÔÔÖÙ */
    $"DFC2 4ADB E6FF 16C6 504F 4D4B 4947 4440"            /* ßÂJÛæÿ.ÆPOMKIGD@ */
    $"3E3C 3936 322F 2D2A 2925 190F 0909 FD09"            /* ><962/-*)%..ÆÆýÆ */
    $"FB08 0602 1DFB B640 3F34 FD30 092E 2C27"            /* û....û¶@?4ý0Æ.,' */
    $"221E 1A17 1509 5BEE FF03 F32E 100E FE0D"            /* "....Æ[îÿ.ó...þÂ */
    $"FF0E 010F 0DFB 09FD 0A1A 0908 0807 1052"            /* ÿ...ÂûÆý..Æ....R */
    $"6967 686C 7275 797C 8084 878A 8D99 4F30"            /* ighlruy|O0 */
    $"5557 3F01 00FE 01FE 0217 0300 1161 6868"            /* UW?..þ.þ.....ahh */
    $"6A6D 6C6E 6F6F 7275 7474 7779 6964 BBB2"            /* jmlnooruttwyid»² */
    $"B3B5 04BA B9BD BFC0 FEC3 1BC4 C6C5 C4C8"            /* ³µ.º¹½¿ÀþÃ.ÄÆÅÄÈ */
    $"A421 191C 1E1F 2021 2223 2525 261D 6CED"            /* ¤!.... !"#%%&.lí */
    $"EBEB EFF6 D54A DAE6 FF14 C650 4F4D 4B49"            /* ëëïöÕJÚæÿ.ÆPOMKI */
    $"4744 403E 3C39 3632 2F2D 2A29 2519 0FFB"            /* GD@><962/-*)%..û */
    $"09FB 0806 021D FBB5 3F3E 34FD 3009 2E2C"            /* Æû....ûµ?>4ý0Æ., */
    $"2722 1E1A 1715 095B F6FF FFFF 01E9 FBFF"            /* '"....Æ[öÿÿÿ.éûÿ */
    $"02C3 0F10 FC0E FF0F 000C FB09 FD0A 1B09"            /* .Ã..ü.ÿ...ûÆý..Æ */
    $"0808 0715 5A67 6668 6C71 7578 7B7E 8285"            /* ....Zgfhlqux{~ */
    $"898C 9645 3951 543F 0200 01FC 023B 0302"            /* E9QT?...ü.;.. */
    $"054F 6562 6467 6565 686C 6A6B 6E71 6F73"            /* .Oebdgeehljknqos */
    $"6334 4D4D 4E4F 5251 5252 5458 5D5F 605C"            /* c4MMNORQRRTX]_`\ */
    $"5859 5C30 1A1D 1C1E 1F1F 2122 2324 2425"            /* XY\0......!"#$$% */
    $"234E 7775 7678 7E70 3BD4 F9FF EEFF 15CC"            /* #Nwuvx~p;Ôùÿîÿ.Ì */
    $"504D 4C4A 4845 423F 3C3A 3634 322E 2B2A"            /* PMLJHEB?<:642.+* */
    $"2925 1C11 0AFC 09FB 0815 0311 E4FD 5E3D"            /* )%...üÆû....äý^= */
    $"3630 2F30 2F2D 2B27 231F 1B17 150E 38F7"            /* 60/0/-+'#.....8÷ */
    $"EFFF 02C3 0F10 FC0E FF0F 000C FB09 FD0A"            /* ïÿ.Ã..ü.ÿ...ûÆý. */
    $"0E09 0808 0715 5B67 6668 6C71 7578 7B7E"            /* .Æ....[gfhlqux{~ */
    $"0C82 8589 8C96 454E 6C6F 5402 0001 FC02"            /* .ENloT...ü. */
    $"3B03 0205 6B87 8385 8688 8A8C 8D8F 9193"            /* ;...k */
    $"9497 9C7F 62A3 9EA0 A2A2 A6A7 A9AA ACAE"            /* .b£ ¢¢¦§©ª¬® */
    $"B0B1 B0AF ACB0 5113 1B1C 1E1F 1F21 2223"            /* °±°¯¬°Q......!"# */
    $"2424 251E 82D8 D3D6 D8DE C345 D3E6 FF16"            /* $$%.ØÓÖØÞÃEÓæÿ. */
    $"CC50 4D4C 4A48 4542 3F3C 3A36 3432 2E2B"            /* ÌPMLJHEB?<:642.+ */
    $"2A29 251C 100A 09FD 09FB 0815 0311 E4FE"            /* *)%...ÆýÆû....äþ */
    $"5F3C 3630 2F30 2F2D 2B27 231F 1B17 150E"            /* _<60/0/-+'#..... */
    $"38F7 EFFF 02C3 0F10 FC0E FF0F 000C FB09"            /* 8÷ïÿ.Ã..ü.ÿ...ûÆ */
    $"FD0A 1B09 0808 0716 5B67 6668 6C71 7578"            /* ý..Æ....[gfhlqux */
    $"7B7E 8285 898C 9645 3B53 5742 0200 01FC"            /* {~E;SWB...ü */
    $"0217 0302 0553 6B6A 6B6C 6D6B 6B6D 6F72"            /* .....Skjklmkkmor */
    $"7273 7579 626B B8B1 B1B4 23B6 B7BB BCBD"            /* rsuybk¸±±´#¶·»¼½ */
    $"BFC1 C3C4 C5C4 C0C6 5912 1B1C 1E1F 1F21"            /* ¿ÁÃÄÅÄÀÆY......! */
    $"2223 2424 251D 8EEE E8EA EFF3 D748 D4E6"            /* "#$$%.îèêïó×HÔæ */
    $"FF15 CC50 4D4C 4A48 4542 3F3C 3A36 3432"            /* ÿ.ÌPMLJHEB?<:642 */
    $"2E2B 2A29 251C 110A FC09 FB08 1503 11E4"            /* .+*)%...üÆû....ä */
    $"FE5F 3C36 302F 302F 2D2B 2723 1F1B 1715"            /* þ_<60/0/-+'#.... */
    $"0E38 F7F7 FFFF FF01 ECFB FF02 9409 0FFD"            /* .8÷÷ÿÿÿ.ìûÿ.Æ.ý */
    $"0EFF 0F01 0E0A FB09 FD0A 1B09 0808 071E"            /* .ÿ....ûÆý..Æ.... */
    $"6166 6468 6C71 7478 7B7E 8185 898D 923F"            /* afdhlqtx{~? */
    $"3F50 5142 0300 01FC 02FF 0311 0036 6763"            /* ?PQB...ü.ÿ...6gc */
    $"6567 6464 6668 696D 6E6F 7174 5A31 FE4E"            /* egddfhimnoqtZ1þN */
    $"004D FE51 2052 5356 595B 5A58 595A 4A18"            /* .MþQ RSVY[ZXYZJ. */
    $"1A1B 1C1D 1E1F 2122 2323 2424 255B 7574"            /* ......!"##$$%[ut */
    $"757A 7A6F 3CCE F9FF EEFF 15CC 504D 4C4A"            /* uzzo<Îùÿîÿ.ÌPMLJ */
    $"4744 423E 3C3A 3733 312E 2B29 2825 1F12"            /* GDB><:731.+)(%.. */
    $"0BFB 09FC 0815 040B CAFF 9638 3930 2D2E"            /* .ûÆü....Êÿ890-. */
    $"2E2D 2B27 2320 1C18 1611 1DE0 EFFF 0294"            /* .-+'# .....àïÿ. */
    $"090F FD0E FF0F 010E 0AFB 09FD 0A0E 0908"            /* Æ.ý.ÿ....ûÆý..Æ. */
    $"0807 1E60 6564 686C 7174 787B 7E0C 8185"            /* ...`edhlqtx{~. */
    $"898D 9142 566A 6D59 0300 01FC 02FF 032D"            /* BVjmY...ü.ÿ.- */
    $"0049 8983 8586 8789 8B8D 8E90 9293 969C"            /* .I */
    $"7360 A49E 9FA1 A3A4 A6A8 A9AB ADB0 B0AC"            /* s`¤¡£¤¦¨©«­°°¬ */
    $"AAB0 8D1B 171B 1C1D 1E1F 2122 2323 FE24"            /* ª°.......!"##þ$ */
    $"089D D6D2 D6D7 DCC7 4BCE E6FF 16CC 504D"            /* .ÖÒÖ×ÜÇKÎæÿ.ÌPM */
    $"4C4A 4744 423E 3C3A 3733 312E 2B29 2825"            /* LJGDB><:731.+)(% */
    $"1E13 0B09 FC09 FC08 1504 0BCB FF96 3839"            /* ...ÆüÆü....Ëÿ89 */
    $"302D 2E2E 2D2B 2723 201C 1816 111D E0EF"            /* 0-..-+'# .....àï */
    $"FF02 9409 0FFD 0EFF 0F01 0E0A FB09 FD0A"            /* ÿ.Æ.ý.ÿ....ûÆý. */
    $"1B09 0808 071E 6165 6468 6C71 7478 7B7E"            /* .Æ....aedhlqtx{~ */
    $"8185 898D 9140 4252 5445 0400 01FC 02FF"            /* @BRTE...ü.ÿ */
    $"0315 0039 6D68 6768 6869 6D71 7374 7374"            /* ...9mhghhimqstst */
    $"787D 596A B9B0 B1B5 23B9 BAB9 BABB BFC2"            /* x}Yj¹°±µ#¹º¹º»¿Â */
    $"C5C4 C0C0 C49D 1B17 1B1C 1D1E 1F21 2223"            /* ÅÄÀÀÄ.......!"# */
    $"2324 2324 ADED E7EA ECF2 DA4E CDE6 FF15"            /* #$#$­íçêìòÚNÍæÿ. */
    $"CC50 4D4C 4A47 4442 3E3C 3A37 3331 2E2B"            /* ÌPMLJGDB><:731.+ */
    $"2928 251E 130C FB09 FC08 1504 0BCA FF96"            /* )(%...ûÆü....Êÿ */
    $"3839 302D 2E2E 2D2B 2723 201C 1816 111D"            /* 890-..-+'# ..... */
    $"E0F7 FFFF FF01 E6FB FF01 530C FD0E FE0F"            /* à÷ÿÿÿ.æûÿ.S.ý.þ. */
    $"000C FA09 FD0A 0409 0808 062E FE64 1366"            /* ..úÆý..Æ....þd.f */
    $"6B70 7376 7A7D 8184 888D 8E3A 424C 5046"            /* kpsvz}:BLPF */
    $"0500 01FC 02FF 0339 0114 5D65 6364 6565"            /* ...ü.ÿ.9..]ecdee */
    $"6668 696C 6C6D 7274 5A31 4D4E 504F 5051"            /* fhillmrtZ1MNPOPQ */
    $"5152 5354 5557 5858 5957 2914 1A1A 1C1D"            /* QRSTUWXXYW)..... */
    $"1E1F 2022 2223 2423 2B66 7274 7576 7972"            /* .. ""#$#+frtuvyr */
    $"39C3 F9FF EEFF 15C9 4D4C 4B49 4644 413E"            /* 9Ãùÿîÿ.ÉMLKIFDA> */
    $"3B39 3633 302D 2C29 2726 2015 0CFB 09FC"            /* ;9630-,)'& ..ûÆü */
    $"0815 0504 B3FF E44C 3930 2B2B 2D2C 2A28"            /* ....³ÿäL90++-,*( */
    $"2420 1C18 1613 0CA9 EFFF 0153 0CFD 0EFE"            /* $ .....©ïÿ.S.ý.þ */
    $"0F00 0DFA 09FD 0A0E 0908 0806 2E64 6564"            /* ..ÂúÆý..Æ....ded */
    $"666B 7073 767A 7D0C 8184 888D 8D3D 5C69"            /* fkpsvz}.=\i */
    $"6C5E 0700 01FC 02FF 0339 0019 7B84 8485"            /* l^...ü.ÿ.9..{ */
    $"8789 8A8C 8D8F 9293 9499 735F A29E 9F9F"            /* s_¢ */
    $"A0A3 A6A8 A9AA ADAE ABA9 ACAE 420F 1A1A"            /*  £¦¨©ª­®«©¬®B... */
    $"1C1D 1E1F 2022 2223 2421 32B9 D1D1 D4D6"            /* .... ""#$!2¹ÑÑÔÖ */
    $"DACA 49C4 E6FF 16C9 4D4C 4B49 4644 413E"            /* ÚÊIÄæÿ.ÉMLKIFDA> */
    $"3B39 3633 302D 2C29 2726 2016 0D09 FC09"            /* ;9630-,)'& .ÂÆüÆ */
    $"FC08 1505 04B3 FFE4 4C39 302B 2B2D 2C2A"            /* ü....³ÿäL90++-,* */
    $"2824 201C 1816 130C A9EF FF01 530C FD0E"            /* ($ .....©ïÿ.S.ý. */
    $"FE0F 000C FA09 FD0A 1B09 0808 062E 6465"            /* þ...úÆý..Æ....de */
    $"6466 6B70 7376 7A7D 8184 888D 8E3A 4551"            /* dfkpsvz}:EQ */
    $"5449 0600 01FC 02FF 0315 0014 6369 6869"            /* TI...ü.ÿ....cihi */
    $"6A69 6B6F 7072 7475 767B 5A69 B7AF B0B2"            /* jikoprtuv{Zi·¯°² */
    $"02B6 B9BB FEBD 1DBF C3C2 BEC1 C148 0E1A"            /* .¶¹»þ½.¿ÃÂ¾ÁÁH.. */
    $"1A1C 1D1E 1F20 2222 2324 2034 CCE8 E5E8"            /* ..... ""#$ 4Ìèåè */
    $"EAF0 DE4C C3E6 FF15 C94D 4C4B 4946 4441"            /* êðÞLÃæÿ.ÉMLKIFDA */
    $"3E3B 3936 3330 2D2C 2927 2620 160C FB09"            /* >;9630-,)'& ..ûÆ */
    $"FC08 1505 04B3 FFE4 4B39 302B 2B2D 2C2A"            /* ü....³ÿäK90++-,* */
    $"2824 201C 1816 130C A9F7 FFFF FF01 E8FC"            /* ($ .....©÷ÿÿÿ.èü */
    $"FF02 E219 0FFE 0EFD 0F00 0CFA 09FD 0A1B"            /* ÿ.â..þ.ý...úÆý.. */
    $"0908 0806 3C67 6363 666A 6F73 767A 7D81"            /* Æ...<gccfjosvz} */
    $"8387 8C89 3345 4B4E 4B10 0001 FC02 FE03"            /* 3EKNK...ü.þ. */
    $"1201 3F66 6061 6665 666A 6B6D 6D6F 7073"            /* ..?f`afefjkmmops */
    $"5933 4C4D FE51 2252 5051 5355 5758 5956"            /* Y3LMþQ"RPQSUWXYV */
    $"5C46 1618 1A1A 1C1D 1E1E 2021 2223 2320"            /* \F........ !"##  */
    $"3E70 7071 7476 7771 3AC4 F9FF EEFF 15C7"            /* >ppqtvwq:Äùÿîÿ.Ç */
    $"4C4B 4A48 4543 403D 3B38 3634 302D 2C29"            /* LKJHEC@=;8640-,) */
    $"2726 2117 0EFB 09FC 0815 0600 A2FF FF75"            /* '&!..ûÆü....¢ÿÿu */
    $"3332 2B2B 2C2C 2A28 2420 1C19 1614 047F"            /* 32++,,*($ ...... */
    $"F0FF 02E2 190F FE0E FE0F 0110 0BFA 09FD"            /* ðÿ.â..þ.þ....úÆý */
    $"0A0E 0908 0806 3B67 6363 666A 6F73 767A"            /* ..Æ...;gccfjosvz */
    $"7D0C 8183 878C 8839 5F68 6A66 1500 01FC"            /* }.9_hjf...ü */
    $"02FF 031B 0200 5289 8384 8688 898B 8D90"            /* .ÿ....R */
    $"9193 9399 7365 A19C 9E9E A0A3 A4A6 A8A9"            /* se¡ £¤¦¨© */
    $"FDAA 19B7 8416 181A 1A1C 1D1E 1E20 2122"            /* ýª.·........ !" */
    $"2323 1B5D CFCD CFD2 D4D8 CB4D C3E6 FF16"            /* ##.]ÏÍÏÒÔØËMÃæÿ. */
    $"C74C 4B4A 4845 4340 3D3B 3836 3430 2D2C"            /* ÇLKJHEC@=;8640-, */
    $"2927 2621 180F 09FC 09FC 0815 0600 A2FF"            /* )'&!..ÆüÆü....¢ÿ */
    $"FF75 3232 2B2B 2C2C 2A28 2420 1C19 1614"            /* ÿu22++,,*($ .... */
    $"047F F0FF 02E2 190F FE0E FD0F 000B FA09"            /* ..ðÿ.â..þ.ý...úÆ */
    $"FD0A 1B09 0808 063B 6663 6366 6A6F 7376"            /* ý..Æ...;fccfjosv */
    $"7A7D 8183 878C 8934 4951 5350 1100 01FC"            /* z}4IQSP...ü */
    $"02FF 0315 0200 416C 6A6C 6C6B 6B6D 7172"            /* .ÿ....Aljllkkmqr */
    $"7474 757A 5A71 B6AF AFB1 23B3 B7BA BCBD"            /* ttuzZq¶¯¯±#³·º¼½ */
    $"BCBF BEBF BDCB 9216 171A 1A1C 1D1E 1E20"            /* ¼¿¾¿½Ë........  */
    $"2122 2323 1A64 E6E5 E6E7 EAEF E151 C2E6"            /* !"##.dæåæçêïáQÂæ */
    $"FF15 C74C 4B4A 4845 4340 3D3B 3836 3430"            /* ÿ.ÇLKJHEC@=;8640 */
    $"2D2C 2927 2621 190E FB09 FC08 1506 00A2"            /* -,)'&!..ûÆü....¢ */
    $"FFFF 7532 322B 2B2C 2C2A 2824 201C 1916"            /* ÿÿu22++,,*($ ... */
    $"1404 7FF7 FFFF FF01 E7FC FF01 BA13 FB0F"            /* ...÷ÿÿÿ.çüÿ.º.û. */
    $"0210 0E0A F909 FF0A 0009 FE08 1807 4267"            /* ....ùÆÿ..Æþ...Bg */
    $"6363 666A 6E71 7578 7B7F 8386 8B85 2F47"            /* ccfjnqux{./G */
    $"4A4E 511D 0001 FC02 FE03 1200 1056 655F"            /* JNQ...ü.þ....Ve_ */
    $"6465 6669 696C 6C6E 6F73 4C32 4D4D FE4E"            /* defiillnosL2MMþN */
    $"224F 5151 5258 5956 575B 4A1E 1519 1A1B"            /* "OQQRXYVW[J..... */
    $"1B1D 1E1E 1F21 2223 2223 5970 6E70 7274"            /* .....!"#"#Ypnprt */
    $"7573 39B7 F9FF EEFF 16CD 4C49 4846 4441"            /* us9·ùÿîÿ.ÍLIHFDA */
    $"3E3B 3836 3431 2E2B 2B29 2624 221B 100A"            /* >;8641.++)&$"... */
    $"FC09 FC08 1507 008B FFFF C13B 342B 2A2B"            /* üÆü....ÿÿÁ;4+*+ */
    $"2A29 2724 211D 1917 1408 64F0 FF01 BA13"            /* *)'$!.....dðÿ.º. */
    $"FB0F 0210 0F0A F909 FF0A 0009 FD08 0A43"            /* û.....ùÆÿ..Æý..C */
    $"6763 6366 6A6E 7175 787B 0C7F 8386 8B83"            /* gccfjnqux{.. */
    $"3661 6768 6B26 0001 FC02 FE03 3800 1573"            /* 6aghk&..ü.þ.8..s */
    $"8783 8687 888A 8D8F 9092 939B 6263 A19C"            /* bc¡ */
    $"9D9F A0A2 A3A4 A7A9 AAAA ADB4 8D29 1319"            /*  ¢£¤§©ªª­´).. */
    $"1A1B 1B1D 1E1E 1F21 2223 2122 9DD0 CBCE"            /* .......!"#!"ÐËÎ */
    $"D1D2 D6D0 50B6 E6FF 16CD 4C49 4846 4441"            /* ÑÒÖÐP¶æÿ.ÍLIHFDA */
    $"3E3B 3836 3431 2E2B 2B29 2624 221B 100A"            /* >;8641.++)&$"... */
    $"FC09 FC08 1507 008B FFFF C13B 342B 2A2B"            /* üÆü....ÿÿÁ;4+*+ */
    $"2A29 2724 211D 1917 1408 64F0 FF01 BA13"            /* *)'$!.....dðÿ.º. */
    $"FB0F 0210 0F0A F909 FF0A 0009 FE08 1807"            /* û.....ùÆÿ..Æþ... */
    $"4267 6363 666A 6E71 7578 7B7F 8386 8B84"            /* Bgccfjnqux{. */
    $"304A 5053 561F 0001 FC02 FE03 1400 115B"            /* 0JPSV...ü.þ....[ */
    $"6C6A 6B6C 6C6E 7172 7476 777E 4D6F B4AD"            /* ljkllnqrtvw~Mo´­ */
    $"AEB0 23B2 B4B7 B8BB BCBF BDC0 C89C 2B12"            /* ®°#²´·¸»¼¿½ÀÈ+. */
    $"191A 1B1B 1D1E 1E1F 2122 2321 22AD E9E4"            /* ........!"#!"­éä */
    $"E6E5 E7EC E654 B6E6 FF16 CD4C 4948 4644"            /* æåçìæT¶æÿ.ÍLIHFD */
    $"413E 3B38 3634 312E 2B2B 2926 2422 1B11"            /* A>;8641.++)&$".. */
    $"0BFC 09FC 0815 0700 8BFF FFC1 3B34 2B2A"            /* .üÆü....ÿÿÁ;4+* */
    $"2B2A 2927 2421 1D19 1714 0864 F7FF FFFF"            /* +*)'$!.....d÷ÿÿÿ */
    $"01DC FCFF 0296 0D0E FC0F 0110 0EF6 09FD"            /* .Üüÿ.Â.ü....öÆý */
    $"0818 0A48 6763 6365 696D 7174 777B 7F81"            /* ...Hgcceimqtw{. */
    $"858B 812B 4849 4D53 2D00 01FC 02FD 0306"            /* +HIMS-..ü.ý.. */
    $"0025 6162 6364 67FE 692D 6C6D 6B72 4A30"            /* .%abcdgþi-lmkrJ0 */
    $"4D4B 4B4C 4D4E 5254 5457 5856 5B4D 1B12"            /* MKKLMNRTTWXV[M.. */
    $"1618 1919 1B1C 1D1D 1F20 2121 1F39 6C6C"            /* ......... !!.9ll */
    $"6E6F 7071 7372 37B3 F9FF EEFF 16CA 4A48"            /* nopqsr7³ùÿîÿ.ÊJH */
    $"4745 4340 3E3B 3936 3432 2E2B 2A28 2524"            /* GEC@>;9642.+*(%$ */
    $"221D 120B FC09 FC08 1607 0073 FFFF FB5F"            /* "...üÆü....sÿÿû_ */
    $"2F2C 2929 2A29 2624 211D 1917 140A 4FFE"            /* /,))*)&$!.....Oþ */
    $"F1FF 0296 0D0E FC0F 0110 0DF6 09FD 080B"            /* ñÿ.Â.ü...ÂöÆý.. */
    $"0B48 6763 6365 696D 7174 777B 0C7F 8185"            /* .Hgcceimqtw{.. */
    $"8B7F 3463 6567 6D3B 0001 FC02 FD03 3700"            /* .4cegm;..ü.ý.7. */
    $"3082 8584 8687 8A8C 8E8F 9192 9A60 629F"            /* 0`b */
    $"9A9C 9D9F A0A2 A5A7 AAAC ABB5 9223 0E16"            /*  ¢¥§ª¬«µ#.. */
    $"1819 191B 1C1D 1D1F 2021 211B 54C8 C9CB"            /* ........ !!.TÈÉË */
    $"CDCF D0D3 D14D B2E6 FF16 CA4A 4847 4543"            /* ÍÏÐÓÑM²æÿ.ÊJHGEC */
    $"403E 3B39 3634 322E 2B2A 2825 2422 1D12"            /* @>;9642.+*(%$".. */
    $"0BFC 09FC 0816 0700 73FF FFFB 6030 2C29"            /* .üÆü....sÿÿû`0,) */
    $"292A 2926 2421 1D19 1714 0A4F FEF1 FF02"            /* )*)&$!.....Oþñÿ. */
    $"960D 0EFC 0F01 100E F609 FD08 180A 4866"            /* Â.ü....öÆý...Hf */
    $"6363 6569 6D71 7477 7B7F 8185 8A81 2D4B"            /* cceimqtw{.-K */
    $"4E52 572F 0001 FC02 FD03 1300 2767 6B69"            /* NRW/..ü.ý...'gki */
    $"6A6A 6B6C 6D71 7372 7C4D 6EB2 ACAD AE23"            /* jjklmqsr|Mn²¬­®# */
    $"B1B5 B7BA BBBD BFBE C9A0 250D 1618 1919"            /* ±µ·º»½¿¾É %Â.... */
    $"1B1C 1D1D 1F20 2121 1B5A DEE0 E3E6 E6E4"            /* ..... !!.ZÞàãææä */
    $"E8E6 52B1 E6FF 16CA 4A48 4745 4340 3E3B"            /* èæR±æÿ.ÊJHGEC@>; */
    $"3936 3432 2E2B 2A28 2524 221D 130C FC09"            /* 9642.+*(%$"...üÆ */
    $"FC08 1607 0074 FFFF FB60 2F2C 2929 2A29"            /* ü....tÿÿû`/,))*) */
    $"2624 211D 1917 140A 4FFE F8FF FFFF 01D8"            /* &$!.....Oþøÿÿÿ.Ø */
    $"FCFF 016E 07FD 0FFE 1000 0CF6 09FE 0819"            /* üÿ.n.ý.þ...öÆþ.. */
    $"070D 4E66 6364 6568 6C70 7376 7A7E 8184"            /* .ÂNfcdehlpsvz~ */
    $"897D 2748 4B4C 513B 0100 FC02 FC03 0702"            /* }'HKLQ;..ü.ü... */
    $"3764 6264 6567 68FD 6A2A 724B 304B 494B"            /* 7dbdeghýj*rK0KIK */
    $"4B4C 4E4F 545A 5958 5E48 1C12 1517 1819"            /* KLNOTZYX^H...... */
    $"1A1A 1C1D 1D1F 1F20 2120 526E 6B6D 6F6F"            /* ....... ! Rnkmoo */
    $"7072 7337 B2F9 FFEE FF16 C849 4746 4342"            /* prs7²ùÿîÿ.ÈIGFCB */
    $"3F3D 3A37 3533 312D 2A29 2825 2422 1F15"            /* ?=:7531-*)(%$".. */
    $"0DFC 09FB 0801 0051 FEFF 1090 2A2C 2726"            /* ÂüÆû...Qþÿ.*,'& */
    $"2928 2624 211D 1A17 140D 3BF8 F1FF 016E"            /* )(&$!....Â;øñÿ.n */
    $"07FD 0FFE 1000 0CF6 09FE 080C 070D 4E66"            /* .ý.þ...öÆþ...ÂNf */
    $"6464 6568 6C70 7376 7A0C 7E81 8489 7C31"            /* ddehlpsvz.~|1 */
    $"6464 656C 4E01 00FC 02FC 0336 0147 8685"            /* ddelN..ü.ü.6.G */
    $"8587 888B 8D8E 9091 985F 619E 999A 9C9E"            /* _a */
    $"9FA1 A5AA AAAE B788 250E 1617 1819 1A1A"            /* ¡¥ªª®·%....... */
    $"1C1D 1D1F 1F20 211D 8FCD C7CA CCCD CED1"            /* ..... !.ÍÇÊÌÍÎÑ */
    $"CF4F B1E6 FF16 C849 4746 4342 3F3D 3A37"            /* ÏO±æÿ.ÈIGFCB?=:7 */
    $"3533 312D 2A29 2825 2422 1F15 0DFC 09FB"            /* 531-*)(%$"..ÂüÆû */
    $"0801 0051 FEFF 1090 2A2C 2726 2928 2624"            /* ...Qþÿ.*,'&)(&$ */
    $"211D 1A17 140D 3BF8 F1FF 016E 07FD 0FFE"            /* !....Â;øñÿ.n.ý.þ */
    $"1000 0CF6 09FE 0819 070D 4E66 6464 6568"            /* ...öÆþ...ÂNfddeh */
    $"6C70 7376 7A7E 8184 897D 284E 5150 553D"            /* lpsvz~}(NQPU= */
    $"0100 FC02 FC03 1201 3969 6A6A 6C6B 6E6D"            /* ..ü.ü...9ijjlknm */
    $"6E6F 7079 4C6D B0AB ACAE 23B0 B2B4 BABE"            /* nopyLm°«¬®#°²´º¾ */
    $"BFC0 C996 270E 1517 1819 1A1A 1C1D 1D1F"            /* ¿ÀÉ'........... */
    $"1F20 211C 9EE2 DDE0 E5E7 E6E7 E454 B0E6"            /* . !.âÝàåçæçäT°æ */
    $"FF16 C849 4746 4342 3F3D 3A37 3533 312D"            /* ÿ.ÈIGFCB?=:7531- */
    $"2A29 2825 2422 1F15 0DFC 09FB 0801 0052"            /* *)(%$"..ÂüÆû...R */
    $"FEFF 1090 2A2D 2726 2928 2624 211D 1A17"            /* þÿ.*-'&)(&$!... */
    $"140D 3BF8 F8FF FFFF 01E1 FDFF 02F3 300D"            /* .Â;øøÿÿÿ.áýÿ.ó0Â */
    $"FD0F FE10 000B F609 FE08 1907 0F52 6664"            /* ý.þ...öÆþ....Rfd */
    $"6465 676B 6F72 7578 7C80 838A 6E26 4A4B"            /* degkorux|n&JK */
    $"4C4C 4507 00FC 02FD 0337 0402 053D 6563"            /* LLE..ü.ý.7...=ec */
    $"6465 6769 6A6B 6C71 4A2F 4C4C 4B4A 4C4F"            /* degijklqJ/LLKJLO */
    $"5153 5859 5A42 1913 1515 1717 191A 1A1B"            /* QSXYZB.......... */
    $"1C1D 1E1F 201F 2962 6B6B 6C6D 6E6F 7173"            /* .... .)bkklmnoqs */
    $"35A4 F9FF EEFF 16BB 4345 4442 3F3E 3B38"            /* 5¤ùÿîÿ.»CEDB?>;8 */
    $"3634 3230 2C29 2927 2523 211E 160D FC09"            /* 6420,))'%#!..ÂüÆ */
    $"FB08 0900 32F8 FFFF DD3C 2B27 25FE 2608"            /* û.Æ.2øÿÿÝ<+'%þ&. */
    $"2320 1D19 1714 0F28 F3F2 FF02 F330 0DFD"            /* # .....(óòÿ.ó0Âý */
    $"0FFF 1001 0F0B F609 FE08 0C07 0F52 6664"            /* .ÿ....öÆþ....Rfd */
    $"6465 676B 6F72 7578 0C7C 8083 8A6C 3164"            /* degkorux.|l1d */
    $"6365 695D 0A00 FC02 FD03 3704 0205 5388"            /* cei]..ü.ý.7...S */
    $"8685 8889 8B8C 8F90 975F 609D 989A 9B9C"            /* _` */
    $"9FA3 A6AA AEB1 771F 1015 1517 1719 1A1A"            /* £¦ª®±w......... */
    $"1B1C 1D1E 1F20 1D33 B3C8 C6C9 CACB CDD0"            /* ..... .3³ÈÆÉÊËÍÐ */
    $"D152 A3E6 FF16 BB43 4544 423F 3E3B 3836"            /* ÑR£æÿ.»CEDB?>;86 */
    $"3432 302C 2929 2725 2321 1E16 0DFC 09FB"            /* 420,))'%#!..ÂüÆû */
    $"0809 0032 F8FF FFDD 3C2C 2725 FE26 0823"            /* .Æ.2øÿÿÝ<,'%þ&.# */
    $"201D 1917 140F 28F3 F2FF 02F3 300D FD0F"            /*  .....(óòÿ.ó0Âý. */
    $"FF10 010F 0BF6 09FE 0819 070F 5266 6464"            /* ÿ....öÆþ....Rfdd */
    $"6567 6B6F 7275 787C 8083 8A6D 2750 504F"            /* egkorux|m'PPO */
    $"524A 0800 FC02 FD03 1304 0206 416B 6A6B"            /* RJ..ü.ý.....Akjk */
    $"6C6F 6D6D 7172 774A 6CAF A9AB AC23 AEB3"            /* lommqrwJl¯©«¬#®³ */
    $"B7BA BDC3 C584 210F 1515 1717 191A 1A1B"            /* ·º½ÃÅ!......... */
    $"1C1D 1E1F 201C 35C5 DCDB DFE2 E3E3 E5E6"            /* .... .5ÅÜÛßâããåæ */
    $"58A1 E6FF 16BB 4345 4442 3F3E 3B38 3634"            /* X¡æÿ.»CEDB?>;864 */
    $"3230 2C29 2927 2523 211E 170E FC09 FB08"            /* 20,))'%#!...üÆû. */
    $"0900 32F8 FFFF DD3C 2C27 25FE 2608 2320"            /* Æ.2øÿÿÝ<,'%þ&.#  */
    $"1D19 1714 0F28 F3F8 FFFF FF01 DAFD FF01"            /* .....(óøÿÿÿ.Úýÿ. */
    $"D518 FA10 010F 0AF6 09FE 0819 070F 5466"            /* Õ.ú....öÆþ....Tf */
    $"6464 6566 6A6E 7174 777B 7F82 8969 264B"            /* ddefjnqtw{.i&K */
    $"484B 4C4C 1500 FC02 FE03 FE04 1A02 0641"            /* HKLL..ü.þ.þ....A */
    $"6565 6768 686A 6D6D 7049 304C 4C4B 4B4E"            /* eeghhjmmpI0LLKKN */
    $"5154 5459 5739 1312 FE15 1716 1719 1A1A"            /* QTTYW9..þ....... */
    $"1B1C 1C1E 1F1F 1D43 6E68 6A6C 6C6E 6F70"            /* .......Cnhjllnop */
    $"7134 A1F9 FFEE FF16 AE3D 4543 403F 3D3A"            /* q4¡ùÿîÿ.®=EC@?=: */
    $"3735 3331 2E2B 2928 2724 2321 1F18 0FFC"            /* 7531.+)('$#!...ü */
    $"09FB 0815 0316 F0FF FFFD 6328 2724 2626"            /* Æû....ðÿÿýc('$&& */
    $"2523 211D 1A17 1410 1CE3 F2FF 01D5 18FA"            /* %#!......ãòÿ.Õ.ú */
    $"1001 0F0A F609 FE08 0C07 0F53 6664 6465"            /* ....öÆþ....Sfdde */
    $"666A 6E71 7477 0C7B 7F82 8967 3063 6364"            /* fjnqtw.{.g0ccd */
    $"6667 1C00 FC02 FE03 FE04 1A02 0854 8987"            /* fg..ü.þ.þ....T */
    $"8688 8B8C 8E8F 975F 609C 9799 9A9E A2A3"            /* _`¢£ */
    $"A8B1 AF68 1311 FE15 1716 1719 1A1A 1B1C"            /* ¨±¯h..þ......... */
    $"1C1E 1F20 196E C8C3 C5C8 C8C9 CBCE CF51"            /* ... .nÈÃÅÈÈÉËÎÏQ */
    $"A0E6 FF16 AE3D 4543 403F 3D3A 3735 3331"            /*  æÿ.®=EC@?=:7531 */
    $"2E2B 2928 2724 2321 1F18 0FFC 09FB 0815"            /* .+)('$#!...üÆû.. */
    $"0316 F0FF FFFE 6328 2724 2626 2523 211D"            /* ..ðÿÿþc('$&&%#!. */
    $"1A17 1410 1CE3 F2FF 01D5 18FA 1001 0F0A"            /* .....ãòÿ.Õ.ú.... */
    $"F609 FE08 1907 0F54 6664 6465 666A 6E71"            /* öÆþ....Tfddefjnq */
    $"7477 7B7F 8289 6926 4E4E 4C50 5316 00FC"            /* tw{.i&NNLPS..ü */
    $"02FE 03FE 0411 0207 436D 6C6C 6D6C 6F74"            /* .þ.þ....Cmllmlot */
    $"7579 4A6C ADA7 A9AB 08AF B7B9 BAC4 C273"            /* uyJl­§©«.¯·¹ºÄÂs */
    $"1310 FE15 1716 1719 1A1A 1B1C 1C1E 1F1F"            /* ..þ............. */
    $"1979 DFD8 D9DC DBDD DEE2 E557 9FE6 FF17"            /* .yßØÙÜÛÝÞâåWæÿ. */
    $"AE3D 4543 403F 3D3A 3735 3331 2E2B 2928"            /* ®=EC@?=:7531.+)( */
    $"2724 2321 1F18 0F0A FD09 FB08 1503 16F0"            /* '$#!....ýÆû....ð */
    $"FFFF FE64 2727 2426 2625 2321 1D1A 1714"            /* ÿÿþd''$&&%#!.... */
    $"101C E3F8 FFFF FF01 E1FD FF02 B817 0EFB"            /* ..ãøÿÿÿ.áýÿ.¸..û */
    $"1000 0DF6 091D 0805 0908 070D 5266 6363"            /* ..ÂöÆ...Æ..ÂRfcc */
    $"6566 696D 7073 767A 7E80 895E 254A 4847"            /* efimpsvz~^%JHG */
    $"4B50 3300 FD02 FD03 FD04 1903 052C 6168"            /* KP3.ý.ý.ý....,ah */
    $"6567 6A6A 696E 492F 4A48 494D 4F52 5456"            /* egjjinI/JHIMORTV */
    $"4925 1212 14FE 1517 1617 1819 191B 1C1C"            /* I%...þ.......... */
    $"1D1E 1E2A 616C 686A 6B6B 6D6F 6E6F 33A1"            /* ...*alhjkkmono3¡ */
    $"F9FF EEFF 1793 3C43 413F 3C3B 3936 3331"            /* ùÿîÿ.<CA?<;9631 */
    $"2F2D 2A27 2725 2321 201F 1B11 0BFD 09FB"            /* /-*''%#! ....ýÆû */
    $"0802 0410 DEFE FF0F 9625 2824 2425 2422"            /* ....Þþÿ.%($$%$" */
    $"201D 1917 1411 14C5 F2FF 02B8 170E FB10"            /*  ......Åòÿ.¸..û. */
    $"000D F609 1008 0509 0807 0D52 6763 6365"            /* .ÂöÆ...Æ..ÂRgcce */
    $"6669 6D70 7376 0D7A 7E80 895D 3063 6262"            /* fimpsvÂz~]0cbb */
    $"646A 4400 01FE 02FD 03FD 0419 0205 3981"            /* djD..þ.ý.ý....9 */
    $"8A87 898B 8C8E 955D 609A 9597 999E A2A7"            /* ]`¢§ */
    $"AC89 3C11 1014 FE15 1716 1718 1919 1B1C"            /* ¬<...þ......... */
    $"1C1D 1D1B 34AD C6C2 C4C5 C6C7 C9CB CD50"            /* ....4­ÆÂÄÅÆÇÉËÍP */
    $"9FE6 FF16 933C 4341 3F3C 3B39 3633 312F"            /* æÿ.<CA?<;9631/ */
    $"2D2A 2727 2523 2120 1F1B 1100 0AFD 09FB"            /* -*''%#! .....ýÆû */
    $"0802 0410 DEFE FF0F 9625 2824 2425 2422"            /* ....Þþÿ.%($$%$" */
    $"201D 1917 1411 14C5 F2FF 02B8 170E FB10"            /*  ......Åòÿ.¸..û. */
    $"000D F609 1D08 0509 0807 0E53 6763 6365"            /* .ÂöÆ...Æ...Sgcce */
    $"6669 6D70 7376 7A7E 8089 5E26 4D4A 4B4D"            /* fimpsvz~^&MJKM */
    $"5336 00FD 02FD 03FD 0410 0305 2F67 6B69"            /* S6.ý.ý.ý..../gki */
    $"696E 7271 7448 6BAC A7A9 AA08 B0B6 BBBF"            /* inrqtHk¬§©ª.°¶»¿ */
    $"9B42 1010 14FE 1517 1617 1819 191B 1C1C"            /* B...þ.......... */
    $"1D1E 1B37 BFDB D7D8 DBDA DCDD E0E3 569E"            /* ...7¿Û×ØÛÚÜÝàãV */
    $"E6FF 1793 3C43 413F 3C3B 3936 3331 2F2D"            /* æÿ.<CA?<;9631/- */
    $"2A27 2725 2321 201F 1910 0AFD 09FB 0802"            /* *''%#! ....ýÆû.. */
    $"0410 DEFE FF0F 9625 2824 2425 2422 201D"            /* ..Þþÿ.%($$%$" . */
    $"1917 1411 14C5 F8FF FFFF 01F2 FDFF 02A1"            /* .....Åøÿÿÿ.òýÿ.¡ */
    $"100F FD10 0211 100B F709 1F08 0D27 0708"            /* ..ý.....÷Æ..Â'.. */
    $"080C 5067 6464 6566 686B 6E71 7579 7C7F"            /* ..Pgddefhknquy|. */
    $"8854 2349 4846 484B 4B0E 00FE 02FD 03FE"            /* T#IHFHKK..þ.ý.þ */
    $"04FF 0523 0403 184E 6969 6869 6B6F 482F"            /* .ÿ.#...NiihikoH/ */
    $"4A48 4B4F 5052 462D 160E 1113 1314 1516"            /* JHKOPRF-........ */
    $"1617 1819 191A 1B1B FE1D 003D FE68 0869"            /* ........þ..=þh.i */
    $"6C6A 6B6B 6D6F 35A0 F9FF EFFF 18FC 6D3D"            /* ljkkmo5 ùÿïÿ.üm= */
    $"423F 3D3C 3A37 3433 312F 2C2A 2726 2523"            /* B?=<:7431/,*'&%# */
    $"211F 1E1B 120C FB09 FD08 0204 0DD3 FEFF"            /* !.....ûÆý...ÂÓþÿ */
    $"0FC4 2C27 2322 2423 2220 1D19 1714 120D"            /* .Ä,'#"$#" .....Â */
    $"ADF2 FF02 A110 0FFD 1002 1110 0BF7 0911"            /* ­òÿ.¡..ý.....÷Æ. */
    $"080D 2707 0808 0C50 6764 6465 6668 6B6E"            /* .Â'....Pgddefhkn */
    $"7175 0D79 7C7F 8853 2F62 6062 6366 6313"            /* quÂy|.S/b`bcfc. */
    $"00FE 02FD 03FE 04FF 0533 0401 1E69 8E8C"            /* .þ.ý.þ.ÿ.3...i */
    $"8B8B 8D95 5C5E 9994 969A A0A1 8B52 1B0A"            /* \^ ¡R.. */
    $"1113 1314 1516 1617 1819 191A 1B1B 1D1D"            /* ................ */
    $"1763 C6BE C0C3 C2C5 C6C7 C8CB 559E E7FF"            /* .cÆ¾ÀÃÂÅÆÇÈËUçÿ */
    $"17FC 6D3D 423F 3D3C 3A37 3433 312F 2C2A"            /* .üm=B?=<:7431/,* */
    $"2726 2523 211F 1E1B 1200 0BFB 09FD 0802"            /* '&%#!......ûÆý.. */
    $"040D D3FE FF0F C42D 2723 2224 2322 201D"            /* .ÂÓþÿ.Ä-'#"$#" . */
    $"1917 1412 0DAD F2FF 02A1 100F FD10 0211"            /* ....Â­òÿ.¡..ý... */
    $"100B F709 1F08 0D27 0708 080D 5167 6464"            /* ..÷Æ..Â'...ÂQgdd */
    $"6566 686B 6E71 7579 7C7F 8854 254D 4B4D"            /* efhknquy|.T%MKM */
    $"4F50 4F0F 00FE 02FD 03FE 04FF 050F 0402"            /* OPO..þ.ý.þ.ÿ.... */
    $"1953 6F6E 6E70 6D72 496A ABA6 A9AB 1BB3"            /* .SonnpmrIj«¦©«.³ */
    $"B59A 5B1D 0910 1313 1415 1616 1718 1919"            /* µ[.Æ........... */
    $"1A1B 1B1D 1D18 6DDC D5D6 D7FE D904 DBDD"            /* ......mÜÕÖ×þÙ.ÛÝ */
    $"E15C 9DE7 FF18 FC6D 3D42 3F3D 3C3A 3734"            /* á\çÿ.üm=B?=<:74 */
    $"3331 2F2C 2A27 2625 2321 1F1E 1B12 0BFB"            /* 31/,*'&%#!.....û */
    $"09FD 0802 040D D3FE FF0F C32C 2723 2224"            /* Æý...ÂÓþÿ.Ã,'#"$ */
    $"2322 201D 1917 1412 0DAD F8FF FFFF 01EF"            /* #" .....Â­øÿÿÿ.ï */
    $"FDFF 018E 05FC 1002 110F 0AF7 0918 0144"            /* ýÿ..ü.....÷Æ..D */
    $"7B00 0808 0C50 6865 6465 6667 6A6D 7074"            /* {....Phedefgjmpt */
    $"787B 7E87 5522 48FE 4703 4950 2800 FE02"            /* x{~U"HþG.IP(.þ. */
    $"FD03 FE04 FF05 FF06 1702 0F36 5365 6C6F"            /* ý.þ.ÿ.ÿ....6Selo */
    $"744B 314C 4B4A 463D 2614 0E0F 1111 1313"            /* tK1LKJF=&....... */
    $"14FE 1506 1617 1818 1A1B 1BFE 1D0C 2658"            /* .þ.........þ..&X */
    $"6966 686B 6969 6B6C 6F36 A0F9 FFEF FF18"            /* ifhkiiklo6 ùÿïÿ. */
    $"E951 3E3F 3E3B 3A38 3633 3130 2E2C 2926"            /* éQ>?>;:86310.,)& */
    $"2624 2221 1E1D 1C14 0CFB 09FD 0802 050A"            /* &$"!.....ûÆý.... */
    $"C9FE FF0F EE40 2623 2022 2321 1E1D 1A17"            /* Éþÿ.î@&# "#!.... */
    $"1413 0AA3 F2FF 018E 05FC 1002 110F 0AF7"            /* ...£òÿ..ü.....÷ */
    $"0911 0144 7B00 0808 0C50 6865 6465 6667"            /* Æ..D{....Phedefg */
    $"6A6D 7074 0D78 7B7E 8753 2F61 5F61 6364"            /* jmptÂx{~S/a_acd */
    $"6B36 00FE 02FD 03FE 04FF 05FF 0617 0013"            /* k6.þ.ý.þ.ÿ.ÿ.... */
    $"466D 868D 929A 6061 9E99 9890 7744 1A0A"            /* Fm`awD.. */
    $"0E11 1113 1314 FE15 1616 1718 181A 1B1B"            /* ......þ......... */
    $"1D1D 1B2F 9BC6 BFC1 C1C2 C3C4 C6CB 569E"            /* .../Æ¿ÁÁÂÃÄÆËV */
    $"E7FF 17E9 513E 3F3E 3B3A 3836 3331 302E"            /* çÿ.éQ>?>;:86310. */
    $"2C29 2626 2422 211E 1D1C 1500 0CFB 09FD"            /* ,)&&$"!......ûÆý */
    $"0802 050A C9FE FF0F EF3F 2523 2022 2321"            /* ....Éþÿ.ï?%# "#! */
    $"1E1D 1A17 1413 0AA3 F2FF 018E 05FC 1002"            /* .......£òÿ..ü.. */
    $"110F 0AF7 091F 0144 7B00 0808 0C50 6865"            /* ...÷Æ..D{....Phe */
    $"6465 6667 6A6D 7074 787B 7E87 5424 4B49"            /* defgjmptx{~T$KI */
    $"4B4C 4D54 2B00 FE02 FD03 FE04 FF05 FF06"            /* KLMT+.þ.ý.þ.ÿ.ÿ. */
    $"0D01 0F39 576A 7174 794C 6EB1 ABA9 A009"            /* Â..9WjqtyLn±«© Æ */
    $"854C 1D09 0D11 1113 1314 FE15 1616 1718"            /* L.ÆÂ.....þ..... */
    $"181A 1B1B 1D1D 1B32 ACDB D3D5 D7D8 D7D7"            /* .......2¬ÛÓÕ×Ø×× */
    $"DAE0 5E9D E7FF 18E9 513E 3F3E 3B3A 3836"            /* Úà^çÿ.éQ>?>;:86 */
    $"3331 302E 2C29 2626 2422 211E 1D1C 140C"            /* 310.,)&&$"!..... */
    $"FB09 FD08 0205 0AC9 FEFF 0FEF 4026 2320"            /* ûÆý....Éþÿ.ï@&#  */
    $"2223 211E 1D1A 1714 130A A3F8 FFFF FF01"            /* "#!.......£øÿÿÿ. */
    $"EFFD FF02 7D05 11FE 10FF 1100 0DF6 0922"            /* ïýÿ.}..þ.ÿ..ÂöÆ" */
    $"0095 9000 0908 0B4F 6865 6465 6666 686C"            /* ..Æ..Ohedeffhl */
    $"6F71 7578 7C86 5322 4747 4847 494E 470C"            /* oqux|S"GGHGING. */
    $"0002 02FD 03FE 04FF 05FE 0615 0504 0C1F"            /* ...ý.þ.ÿ.þ...... */
    $"343F 4934 2330 2821 1911 0D0E 0F10 1111"            /* 4?I4#0(!..Â..... */
    $"1313 FE14 1715 1617 1818 1A1B 1B1D 1D1E"            /* ..þ............. */
    $"1B2B 6068 666A 6767 6C6B 6B33 A0F9 FFEF"            /* .+`hfjgglkk3 ùÿï */
    $"FF18 D443 3E3D 3C3A 3837 3432 302E 2C2A"            /* ÿ.ÔC>=<:87420.,* */
    $"2826 2524 2221 1E1D 1C16 0DFB 09FD 0802"            /* (&%$"!....ÂûÆý.. */
    $"0508 C2FD FF0E 861F 2320 2122 211E 1D1A"            /* ..Âýÿ..# !"!... */
    $"1714 1402 89F2 FF02 7D05 11FE 10FF 1100"            /* ....òÿ.}..þ.ÿ.. */
    $"0EF6 0911 0095 9000 0908 0B4F 6865 6465"            /* .öÆ...Æ..Ohede */
    $"6666 686C 6F71 1075 787C 8652 2E60 5E5F"            /* ffhloq.ux|R.`^_ */
    $"6063 675E 1000 0202 FD03 FE04 FF05 FE06"            /* `cg^....ý.þ.ÿ.þ. */
    $"1504 030F 2743 525E 4242 604F 3D29 150B"            /* ....'CR^BB`O=).. */
    $"0D0F 1011 1113 13FE 140F 1516 1718 181A"            /* Â......þ........ */
    $"1B1B 1D1D 1E18 37B0 C4BF FEC0 04C2 C4C7"            /* ......7°Ä¿þÀ.ÂÄÇ */
    $"529E E7FF 17D4 433E 3D3C 3A38 3734 3230"            /* Rçÿ.ÔC>=<:87420 */
    $"2E2C 2A28 2625 2422 211E 1D1C 1600 0DFB"            /* .,*(&%$"!.....Âû */
    $"09FD 0802 0508 C2FD FF0E 861F 2320 2122"            /* Æý....Âýÿ..# !" */
    $"211E 1D1A 1714 1402 89F2 FF02 7D05 11FE"            /* !.......òÿ.}..þ */
    $"10FF 1100 0DF6 0922 0095 9000 0908 0B4F"            /* .ÿ..ÂöÆ"..Æ..O */
    $"6865 6465 6666 686C 6F71 7578 7C86 5223"            /* hedeffhloqux|R# */
    $"4947 4A4A 4B50 4B0D 0002 02FD 03FE 04FF"            /* IGJJKPKÂ...ý.þ.ÿ */
    $"05FE 060C 0504 0D21 3642 4C35 4B6A 5642"            /* .þ....Â!6BL5KjVB */
    $"2D08 150A 0C0F 1011 1113 13FE 1417 1516"            /* -..........þ.... */
    $"1718 181A 1B1B 1D1D 1E18 39C0 D9D2 D4D6"            /* ..........9ÀÙÒÔÖ */
    $"D6D7 D8DC 599C E7FF 18D4 433E 3D3C 3A38"            /* Ö×ØÜYçÿ.ÔC>=<:8 */
    $"3734 3230 2E2C 2A28 2625 2422 211E 1D1C"            /* 7420.,*(&%$"!... */
    $"160D FB09 FD08 0205 08C2 FDFF 0E86 1F23"            /* .ÂûÆý....Âýÿ..# */
    $"2021 2221 1E1D 1A17 1414 0289 F8FF FFFF"            /*  !"!.......øÿÿÿ */
    $"01EB FDFF 016E 07FC 1101 100B F709 2305"            /* .ëýÿ.n.ü....÷Æ#. */
    $"11DF 6A00 0908 0A4A 6965 6465 6667 686B"            /* .ßj.Æ..Jiedefghk */
    $"6E70 7477 7B84 5221 4646 4746 484B 4E2B"            /* nptw{R!FFGFHKN+ */
    $"0002 02FE 03FD 04FF 05FE 06FE 0705 0506"            /* ...þ.ý.ÿ.þ.þ.... */
    $"0709 0B0B FE0A 010C 0DFE 0F04 1011 1113"            /* .Æ..þ...Âþ...... */
    $"13FE 140E 1516 1718 1819 191A 1A1C 1D1D"            /* .þ.............. */
    $"1934 62FE 6805 6768 6A69 2F9F F9FF EFFF"            /* .4bþh.ghji/ùÿïÿ */
    $"18BC 3A3C 3C3B 3936 3533 312F 2E2B 2927"            /* .¼:<<;96531/.+)' */
    $"2523 2321 201E 1D1B 170E FB09 FD08 FF05"            /* %##! .....ûÆý.ÿ. */
    $"00B9 FDFF 0EBA 2622 1F1F 2020 1E1D 1A17"            /* .¹ýÿ.º&"..  .... */
    $"1413 0288 F2FF 016E 07FC 1101 100B F709"            /* ...òÿ.n.ü....÷Æ */
    $"1205 11DF 6A00 0908 0A4A 6965 6465 6667"            /* ...ßj.Æ..Jiedefg */
    $"686B 6E70 1074 777B 8451 2D5E 5C5C 6062"            /* hknp.tw{Q-^\\`b */
    $"646B 3A00 0102 FE03 FD04 FF05 FE06 FF07"            /* dk:...þ.ý.ÿ.þ.ÿ. */
    $"0B06 0406 0608 0B0B 0A08 0809 0CFE 0F04"            /* ...........Æ.þ.. */
    $"1011 1113 13FE 1410 1516 1718 1819 191A"            /* .....þ.......... */
    $"1A1C 1D1D 154C B7C3 C0FE BF03 C2C3 4A9E"            /* .....L·ÃÀþ¿.ÂÃJ */
    $"E7FF 17BC 3A3C 3C3B 3936 3533 312F 2E2B"            /* çÿ.¼:<<;96531/.+ */
    $"2927 2523 2321 201E 1D1B 1600 0DFB 09FD"            /* )'%##! .....ÂûÆý */
    $"08FF 0500 B9FD FF0E BA27 221F 1F20 201E"            /* .ÿ..¹ýÿ.º'"..  . */
    $"1D1A 1714 1302 88F2 FF01 6E07 FC11 0110"            /* ......òÿ.n.ü... */
    $"0CF7 0923 0511 DF6A 0009 080A 4A69 6564"            /* .÷Æ#..ßj.Æ..Jied */
    $"6566 6768 6B6E 7074 777B 8452 2349 4748"            /* efghknptw{R#IGH */
    $"4A4A 4B53 2E00 0202 FE03 FD04 FF05 FE06"            /* JJKS....þ.ý.ÿ.þ. */
    $"FF07 0A06 0506 0608 0B0C 0B07 0709 080C"            /* ÿ............Æ.. */
    $"0E0F 0F10 1111 1313 FE14 1715 1617 1818"            /* ........þ....... */
    $"1919 1A1A 1C1D 1D14 54CB D7D4 D3D2 D5D6"            /* ........TË×ÔÓÒÕÖ */
    $"D84F 9DE7 FF18 BC3A 3C3C 3B39 3635 3331"            /* ØOçÿ.¼:<<;96531 */
    $"2F2E 2B29 2725 2323 2120 1E1D 1B16 0DFB"            /* /.+)'%##! ....Âû */
    $"09FD 08FF 0500 B9FD FF0E BA26 221F 1F20"            /* Æý.ÿ..¹ýÿ.º&"..  */
    $"201E 1D1A 1714 1302 88F8 FFFF FF01 E3FD"            /*  .......øÿÿÿ.ãý */
    $"FF01 5E09 FC11 010F 0AF7 0923 007D FF5A"            /* ÿ.^Æü....÷Æ#.}ÿZ */
    $"0009 0809 4369 6564 6566 6769 6A6B 6E72"            /* .Æ.ÆCiedefgijknr */
    $"7579 815D 2244 4446 4547 4A4C 4D1A 0002"            /* uy]"DDFEGJLM... */
    $"FE03 FD04 FF05 FE06 0007 FE08 FE09 010A"            /* þ.ý.ÿ.þ...þ.þÆ.. */
    $"0BFE 0C01 0D0E FE0F 0410 1111 1313 FE14"            /* .þ..Â.þ.......þ. */
    $"0215 1617 FE18 FF19 FC1B 0A18 3562 6969"            /* ....þ.ÿ.ü...5bii */
    $"6869 6968 2D9F F9FF EFFF 19A6 343B 3A39"            /* hiih-ùÿïÿ.¦4;:9 */
    $"3634 3331 2F2D 2C2A 2926 2423 2221 1F1D"            /* 6431/-,*)&$#"!.. */
    $"1C1B 170F 0AFC 09FD 0802 0506 B9FD FF0E"            /* .....üÆý....¹ýÿ. */
    $"E333 211F 1F20 201E 1C19 1714 1302 89F2"            /* ã3!..  .......ò */
    $"FF01 5E09 FC11 010F 0AF7 0912 007D FF5A"            /* ÿ.^Æü....÷Æ..}ÿZ */
    $"0009 0809 4369 6564 6566 6769 6A6B 6E10"            /* .Æ.ÆCiedefgijkn. */
    $"7275 7981 5C2D 5C5B 5C5F 6062 6466 2200"            /* ruy\-\[\_`bdf". */
    $"02FE 03FD 04FF 05FE 0600 07FE 08FE 0900"            /* .þ.ý.ÿ.þ...þ.þÆ. */
    $"0AFE 0BFF 0D00 0EFE 0F04 1011 1113 13FE"            /* .þ.ÿÂ..þ.......þ */
    $"1402 1516 17FE 18FF 19FC 1B0A 1350 B7C3"            /* .....þ.ÿ.ü...P·Ã */
    $"C0BE BDBE C048 9EE7 FF17 A634 3B3A 3936"            /* À¾½¾ÀHçÿ.¦4;:96 */
    $"3433 312F 2D2C 2A29 2624 2322 211F 1D1C"            /* 431/-,*)&$#"!... */
    $"1B17 010F 0AFC 09FD 0802 0506 B9FD FF0E"            /* .....üÆý....¹ýÿ. */
    $"E433 211F 1F20 201E 1C19 1714 1302 89F2"            /* ä3!..  .......ò */
    $"FF01 5E09 FC11 010F 0AF7 0923 007D FF5A"            /* ÿ.^Æü....÷Æ#.}ÿZ */
    $"0009 0809 4369 6564 6566 6769 6A6B 6E72"            /* .Æ.ÆCiedefgijknr */
    $"7579 815D 2449 4846 494A 4A4E 511B 0002"            /* uy]$IHFIJJNQ... */
    $"FE03 FD04 FF05 FE06 0007 FE08 FE09 000A"            /* þ.ý.ÿ.þ...þ.þÆ.. */
    $"FE0B FF0D 000E FE0F 0410 1111 1313 FE14"            /* þ.ÿÂ..þ.......þ. */
    $"0215 1617 FE18 FF19 FD1B 0B1A 1256 CBD8"            /* ....þ.ÿ.ý....VËØ */
    $"D4D1 D0D3 D34D 9DE7 FF19 A634 3B3A 3936"            /* ÔÑÐÓÓMçÿ.¦4;:96 */
    $"3433 312F 2D2C 2A29 2624 2322 211F 1D1C"            /* 431/-,*)&$#"!... */
    $"1B17 0F0A FC09 FD08 0205 06B9 FDFF 0EE3"            /* ....üÆý....¹ýÿ.ã */
    $"3321 1F1F 2020 1E1C 1917 1413 0289 F8FF"            /* 3!..  .......øÿ */
    $"FFFF 01ED FDFF 0157 0AFC 1100 0EF7 090A"            /* ÿÿ.íýÿ.W.ü...÷Æ. */
    $"0512 DAFF 6000 0909 0838 67FE 6516 6668"            /* ..Úÿ`.ÆÆ.8gþe.fh */
    $"6969 6A6D 7074 777E 5F21 4342 4243 464A"            /* iijmptw~_!CBBCFJ */
    $"4B4D 440E 00FE 03FF 04FD 05FE 0600 07FE"            /* KMD..þ.ÿ.ý.þ...þ */
    $"0800 09FE 0A00 0BFE 0C01 0D0E FE0F 0210"            /* ..Æþ...þ..Â.þ... */
    $"1111 FE13 FE14 0515 1617 1718 19FE 1A0D"            /* ..þ.þ........þ.Â */
    $"1B1A 1B1B 163D 6B69 6867 6667 2C9F F9FF"            /* .....=kihgfg,ùÿ */
    $"F0FF 1AFD 7733 3938 3634 3331 2F2E 2C2A"            /* ðÿ.ýw3986431/.,* */
    $"2927 2523 2221 201E 1C1B 1B18 100A FC09"            /* )'%#"! .......üÆ */
    $"FD08 0206 04B5 FCFF 026D 1A1F FE1E 071D"            /* ý....µüÿ.m..þ... */
    $"1B19 1714 1302 89F2 FF01 570A FC11 010E"            /* ......òÿ.W.ü... */
    $"0AF8 090A 0512 DAFF 6000 0909 0838 67FE"            /* .øÆ...Úÿ`.ÆÆ.8gþ */
    $"6505 6668 6969 6A6D 1070 7477 7E5E 2B5A"            /* e.fhiijm.ptw~^+Z */
    $"595C 5D5F 6062 675B 1200 FE03 FF04 FD05"            /* Y\]_`bg[..þ.ÿ.ý. */
    $"FE06 0007 FE08 0009 FE0A 000B FE0C 010D"            /* þ...þ..Æþ...þ..Â */
    $"0EFE 0F02 1011 11FE 13FE 1405 1516 1717"            /* .þ.....þ.þ...... */
    $"1819 FE1A 0D1B 1A1B 1B10 64C8 C1BE BCBC"            /* ..þ.Â.....dÈÁ¾¼¼ */
    $"BD47 9DE8 FF18 FD77 3339 3836 3433 312F"            /* ½Gèÿ.ýw3986431/ */
    $"2E2C 2A29 2725 2322 2120 1E1C 1B1B 1801"            /* .,*)'%#"! ...... */
    $"100A FC09 FD08 0206 04B5 FCFF 026E 1A1F"            /* ..üÆý....µüÿ.n.. */
    $"FE1E 071D 1B19 1714 1302 89F2 FF01 570A"            /* þ.........òÿ.W. */
    $"FC11 000E F709 0A05 12DA FF60 0009 0908"            /* ü...÷Æ...Úÿ`.ÆÆ. */
    $"3867 FE65 1666 6869 696A 6D70 7477 7E5F"            /* 8gþe.fhiijmptw~_ */
    $"2247 4645 484A 4D4E 5249 0F00 FE03 FF04"            /* "GFEHJMNRI..þ.ÿ. */
    $"FD05 FE06 0007 FE08 0009 FE0A 000B FE0C"            /* ý.þ...þ..Æþ...þ. */
    $"000D 000E FE0F 0210 1111 FE13 FE14 0515"            /* .Â..þ.....þ.þ... */
    $"1617 1718 19FE 1A0D 1B1A 1B1B 0F6E DDD6"            /* .....þ.Â.....nÝÖ */
    $"D3CF D1D1 4C9C E8FF 1AFD 7733 3938 3634"            /* ÓÏÑÑLèÿ.ýw39864 */
    $"3331 2F2E 2C2A 2927 2523 2221 201E 1C1B"            /* 31/.,*)'%#"! ... */
    $"1B18 100A FC09 FD08 0206 04B5 FCFF 026E"            /* ....üÆý....µüÿ.n */
    $"1A1F FE1E 071D 1B19 1714 1302 89F8 FFFF"            /* ..þ.........øÿÿ */
    $"FF01 ECFE FF02 FC4F 0BFC 1100 0DF7 091A"            /* ÿ.ìþÿ.üO.ü..Â÷Æ. */
    $"0070 FFFF 5E00 0909 072B 6466 6565 6667"            /* .pÿÿ^.ÆÆ.+dfeefg */
    $"6969 6A6B 6F73 767C 6721 40FE 420B 4447"            /* iijkosv|g!@þB.DG */
    $"4948 4C38 0401 0303 0404 FD05 FF06 FF07"            /* IHL8......ý.ÿ.ÿ. */
    $"FE08 0009 FE0A 000B FE0C 080D 0E0E 0F0F"            /* þ..Æþ...þ..Â.... */
    $"1011 1212 FD13 0214 1516 FE17 0118 19FE"            /* ....ý.....þ....þ */
    $"1AFE 1B09 1A1B 4D6D 6867 6564 2A9D F9FF"            /* .þ.Æ..Mmhged*ùÿ */
    $"F0FF 1AE9 5034 3836 3533 3230 2F2C 2B29"            /* ðÿ.éP4865320/,+) */
    $"2826 2423 2121 1F1D 1C1B 1A18 110A FC09"            /* (&$#!!........üÆ */
    $"FD08 0206 00A7 FCFF 02A6 1C1E FD1D 061B"            /* ý....§üÿ.¦..ý... */
    $"1916 1413 0287 F3FF 02FC 4F0B FC11 000C"            /* .....óÿ.üO.ü... */
    $"F709 1300 70FF FF5E 0009 0907 2B64 6665"            /* ÷Æ..pÿÿ^.ÆÆ.+dfe */
    $"6566 6769 696A 6B15 6F73 767C 652A 5757"            /* efgiijk.osv|e*WW */
    $"5A5C 5E5F 6163 694A 0401 0303 0404 FD05"            /* Z\^_aciJ......ý. */
    $"FF06 FF07 FE08 0009 FE0A 000B FE0C 080D"            /* ÿ.ÿ.þ..Æþ...þ..Â */
    $"0E0E 0F0F 1011 1212 FD13 0214 1516 FE17"            /* ........ý.....þ. */
    $"0118 19FE 1AFE 1B09 181A 87CB C0BC BCBB"            /* ...þ.þ.Æ..ËÀ¼¼» */
    $"449D E8FF 18E9 5034 3836 3533 3230 2F2C"            /* Dèÿ.éP4865320/, */
    $"2B29 2826 2423 2121 1F1D 1C1B 1A18 0111"            /* +)(&$#!!........ */
    $"0AFC 09FD 0802 0600 A7FC FF02 A61C 1EFD"            /* .üÆý....§üÿ.¦..ý */
    $"1D06 1B19 1614 1302 87F3 FF02 FC4F 0BFC"            /* ........óÿ.üO.ü */
    $"1100 0DF7 0929 0070 FFFF 5E00 0909 072B"            /* ..Â÷Æ).pÿÿ^.ÆÆ.+ */
    $"6466 6565 6667 6969 6A6B 6F73 767C 6623"            /* dfeefgiijkosv|f# */
    $"4445 4647 484C 4E4E 523C 0401 0303 0404"            /* DEFGHLNNR<...... */
    $"FD05 FF06 FF07 FE08 0009 FE0A 000B FE0C"            /* ý.ÿ.ÿ.þ..Æþ...þ. */
    $"000D FF0E FF0F 0310 1112 12FD 1302 1415"            /* .Âÿ.ÿ......ý.... */
    $"16FE 1701 1819 FE1A FE1B 0919 1D95 DFD5"            /* .þ....þ.þ.Æ..ßÕ */
    $"D0CF CE4A 9BE8 FF1A E950 3438 3635 3332"            /* ÐÏÎJèÿ.éP486532 */
    $"302F 2C2B 2928 2624 2321 211F 1D1C 1B1A"            /* 0/,+)(&$#!!..... */
    $"1811 0AFC 09FD 0802 0600 A7FC FF02 A61C"            /* ...üÆý....§üÿ.¦. */
    $"1EFD 1D06 1B19 1614 1302 87F8 FFFF FF01"            /* .ý........øÿÿÿ. */
    $"F7FE FF08 FA45 0C12 1111 1211 0BF8 091B"            /* ÷þÿ.úE.......øÆ. */
    $"0708 C6FF FF56 0009 0907 2062 6665 6566"            /* ..ÆÿÿV.ÆÆ. bfeef */
    $"6769 696A 6B6E 7073 7970 233F FE41 0B43"            /* giijknpsyp#?þA.C */
    $"4648 4747 4F2F 0102 0304 04FE 05FF 06FE"            /* FHGGO/.....þ.ÿ.þ */
    $"07FE 0800 09FE 0A00 0BFE 0C00 0DFE 0E02"            /* .þ..Æþ...þ..Âþ.. */
    $"0F10 11FE 12FE 1302 1415 16FD 1703 181A"            /* ...þ.þ.....ý.... */
    $"1A19 FE1B 091A 1822 546A 6865 612A A4F9"            /* ..þ.Æ.."Tjhea*¤ù */
    $"FFF0 FF1A C136 3536 3533 3230 2F2D 2B2A"            /* ÿðÿ.Á6565320/-+* */
    $"2827 2524 2221 1F1F 1D1C 1B1A 1811 0BFC"            /* ('%$"!.........ü */
    $"09FD 0802 0600 A7FC FF0D CB26 1D1B 1C1D"            /* Æý....§üÿÂË&.... */
    $"1C1A 1816 1413 0592 F3FF 08FA 450C 1211"            /* .......óÿ.úE... */
    $"1112 110A F809 1407 08C6 FFFF 5600 0909"            /* ....øÆ...ÆÿÿV.ÆÆ */
    $"0720 6266 6565 6667 6969 6A6B 156E 7073"            /* . bfeefgiijk.nps */
    $"796F 2B54 5658 5A5C 5E60 6163 693D 0001"            /* yo+TVXZ\^`aci=.. */
    $"0304 04FE 05FF 06FE 07FE 0800 09FE 0A00"            /* ...þ.ÿ.þ.þ..Æþ.. */
    $"0BFE 0C00 0DFE 0E02 0F10 11FE 12FE 1302"            /* .þ..Âþ.....þ.þ.. */
    $"1415 16FD 1703 181A 1A19 FE1B 091A 1627"            /* ...ý......þ.Æ..' */
    $"91C4 BEBA B744 A3E8 FF18 C136 3536 3533"            /* Ä¾º·D£èÿ.Á65653 */
    $"3230 2F2D 2B2A 2827 2524 2221 1F1F 1D1C"            /* 20/-+*('%$"!.... */
    $"1B1A 1801 110A FC09 FD08 0206 00A7 FCFF"            /* ......üÆý....§üÿ */
    $"0DCB 261D 1B1C 1D1C 1A18 1614 1305 92F3"            /* ÂË&...........ó */
    $"FF08 FA45 0C12 1111 1211 0AF8 092A 0708"            /* ÿ.úE.......øÆ*.. */
    $"C6FF FF56 0009 0907 2062 6665 6566 6769"            /* ÆÿÿV.ÆÆ. bfeefgi */
    $"696A 6B6E 7073 7970 2443 4444 4748 494C"            /* ijknpsyp$CDDGHIL */
    $"4B4C 5432 0102 0304 04FE 05FF 06FE 07FE"            /* KLT2.....þ.ÿ.þ.þ */
    $"0800 09FE 0A00 0BFE 0C00 0DFE 0E02 0F10"            /* ..Æþ...þ..Âþ.... */
    $"11FE 12FE 1302 1415 16FD 1710 181A 1A19"            /* .þ.þ.....ý...... */
    $"1B1B 1A1B 1728 9FD9 D2CE CB4A A2E8 FF1A"            /* .....(ÙÒÎËJ¢èÿ. */
    $"C136 3536 3533 3230 2F2D 2B2A 2827 2524"            /* Á6565320/-+*('%$ */
    $"2221 1F1F 1D1C 1B1A 1811 0AFC 09FD 0802"            /* "!.........üÆý.. */
    $"0600 A7FC FF0D CB26 1D1B 1C1D 1C1A 1816"            /* ..§üÿÂË&........ */
    $"1413 0592 F8FF FFFF 01EA FEFF 02FA 460C"            /* ...øÿÿÿ.êþÿ.úF. */
    $"FD12 0110 0AF8 0901 004D FEFF 1A65 0009"            /* ý....øÆ..Mþÿ.e.Æ */
    $"0907 165E 6766 6566 6667 696A 6A6C 6E72"            /* Æ..^gfeffgijjlnr */
    $"7670 263C 3F40 4143 FD46 064A 4C24 0003"            /* vp&<?@ACýF.JL$.. */
    $"0404 FE05 FF06 FD07 FE09 FE0A 000B FE0C"            /* ..þ.ÿ.ý.þÆþ...þ. */
    $"000D FE0E 030F 1011 11FD 12FF 14FE 1500"            /* .Âþ......ý.ÿ.þ.. */
    $"16FE 17FE 190C 1A1B 1B19 191A 2052 6761"            /* .þ.þ........ Rga */
    $"5E29 ADF9 FFF0 FF1A 882E 3534 3232 302F"            /* ^)­ùÿðÿ..54220/ */
    $"2D2C 2928 2726 2423 2120 1E1D 1D1B 1A1A"            /* -,)('&$#! ...... */
    $"1913 0BFC 09FD 0802 0701 A9FC FF0D E82B"            /* ...üÆý....©üÿÂè+ */
    $"1C1A 1B1D 1B1A 1816 1312 0BA9 F3FF 02FA"            /* ...........©óÿ.ú */
    $"460C FD12 0110 0AF8 0901 004D FEFF 0F65"            /* F.ý....øÆ..Mþÿ.e */
    $"0009 0907 165E 6766 6566 6667 696A 6A15"            /* .ÆÆ..^gfeffgijj. */
    $"6C6E 7276 6F2C 5156 5759 5A5D 5F60 6064"            /* lnrvo,QVWYZ]_``d */
    $"672E 0002 0404 FE05 FF06 FD07 FE09 FE0A"            /* g.....þ.ÿ.ý.þÆþ. */
    $"000B FE0C 000D FE0E 030F 1011 11FD 12FF"            /* ..þ..Âþ......ý.ÿ */
    $"14FE 1500 16FE 17FE 190C 1A1B 1B19 1A16"            /* .þ...þ.þ........ */
    $"2292 BEB7 B33F ACE8 FF18 882E 3534 3232"            /* "¾·³?¬èÿ..5422 */
    $"302F 2D2C 2928 2726 2423 2120 1E1D 1D1B"            /* 0/-,)('&$#! .... */
    $"1A1A 1901 130B FC09 FD08 0207 01A9 FCFF"            /* ......üÆý....©üÿ */
    $"0DE9 2C1C 1A1B 1D1B 1A18 1613 120B A9F3"            /* Âé,...........©ó */
    $"FF02 FA46 0CFD 1201 100A F809 0100 4DFE"            /* ÿ.úF.ý....øÆ..Mþ */
    $"FF25 6500 0909 0716 5E67 6665 6666 6769"            /* ÿ%e.ÆÆ..^gfeffgi */
    $"6A6A 6C6E 7276 7026 3F43 4547 484B 4C4A"            /* jjlnrvp&?CEGHKLJ */
    $"4B4E 5126 0003 0404 FE05 FF06 FD07 FE09"            /* KNQ&....þ.ÿ.ý.þÆ */
    $"FE0A 000B FE0C 000D FE0E 030F 1011 11FD"            /* þ...þ..Âþ......ý */
    $"12FF 14FE 1500 16FE 17FE 190C 1A1B 1B19"            /* .ÿ.þ...þ.þ...... */
    $"1A16 22A1 D3CB C644 ABE8 FF1A 882E 3534"            /* .."¡ÓËÆD«èÿ..54 */
    $"3232 302F 2D2C 2928 2726 2423 2120 1E1D"            /* 220/-,)('&$#! .. */
    $"1D1B 1A1A 1912 0BFC 09FD 0802 0701 A9FC"            /* .......üÆý....©ü */
    $"FF0D E92B 1D1A 1B1D 1B1A 1816 1312 0BA9"            /* ÿÂé+...........© */
    $"F8FF FFFF 01F5 FEFF 02FA 470C FD12 000E"            /* øÿÿÿ.õþÿ.úG.ý... */
    $"F809 0208 00AA FEFF 257D 0009 0908 0E54"            /* øÆ...ªþÿ%}.ÆÆ..T */
    $"6866 6566 6668 6869 696B 6D6F 7471 2939"            /* hfeffhhiikmotq)9 */
    $"3F3E 3F42 4544 4445 474B 4C24 0402 04FE"            /* ?>?BEDDEGKL$...þ */
    $"05FF 06FD 07FE 09FE 0A00 0BFE 0C00 0DFE"            /* .ÿ.ý.þÆþ...þ..Âþ */
    $"0E00 0FFE 10FE 12FE 1300 14FE 1500 16FE"            /* ...þ.þ.þ...þ...þ */
    $"1702 1819 19FD 1A09 1B1A 4261 5E5E 26AB"            /* .....ý.Æ..Ba^^&« */
    $"FFFC FDFD FFFF F1FF 1BE7 4531 3332 3130"            /* ÿüýýÿÿñÿ.çE13210 */
    $"2F2D 2C2A 2827 2524 2322 201F 1D1C 1C1B"            /* /-,*('%$#" ..... */
    $"1919 1813 0BFB 09FE 0802 0605 B5FB FF0C"            /* .....ûÆþ....µûÿ. */
    $"6015 1B1B 1C1B 1918 1613 110E B4F3 FF02"            /* `...........´óÿ. */
    $"FA47 0CFD 1200 0EF8 0902 0800 AAFE FF0F"            /* úG.ý...øÆ...ªþÿ. */
    $"7D00 0909 080E 5468 6665 6666 6868 6969"            /* }.ÆÆ..Thfeffhhii */
    $"156B 6D6F 7470 2D4E 5556 5759 5B5D 5E5F"            /* .kmotp-NUVWY[]^_ */
    $"6165 652F 0401 04FE 05FF 06FD 07FE 09FE"            /* aee/...þ.ÿ.ý.þÆþ */
    $"0A00 0BFE 0C00 0DFE 0E00 0FFE 10FE 12FE"            /* ...þ..Âþ...þ.þ.þ */
    $"1300 14FE 1500 16FE 1702 1819 19FC 1A08"            /* ...þ...þ.....ü.. */
    $"1675 B5B3 AF39 ABFF FCFD FDEF FF19 E745"            /* .uµ³¯9«ÿüýýïÿ.çE */
    $"3133 3231 302F 2D2C 2A28 2725 2423 2220"            /* 13210/-,*('%$#"  */
    $"1F1D 1C1C 1B19 1918 0113 0BFB 09FE 0802"            /* ...........ûÆþ.. */
    $"0605 B5FB FF0C 6015 1B1B 1C1B 1918 1613"            /* ..µûÿ.`......... */
    $"110E B4F3 FF02 FA47 0CFD 1200 0EF8 0902"            /* ..´óÿ.úG.ý...øÆ. */
    $"0800 AAFE FF25 7D00 0909 080E 5468 6665"            /* ..ªþÿ%}.ÆÆ..Thfe */
    $"6666 6868 6969 6B6D 6F74 7129 3C42 4243"            /* ffhhiikmotq)<BBC */
    $"464A 4B4B 4C4D 5051 2704 0204 FE05 FF06"            /* FJKKLMPQ'...þ.ÿ. */
    $"FD07 FE09 FE0A 000B FE0C 000D FE0E 000F"            /* ý.þÆþ...þ..Âþ... */
    $"FE10 FE12 FE13 0014 FE15 0016 FE17 0218"            /* þ.þ.þ...þ...þ... */
    $"1919 FC1A 0816 81CA C7C2 3DAA FFFC FDFD"            /* ..ü...ÊÇÂ=ªÿüýý */
    $"EFFF 1BE7 4531 3332 3130 2F2D 2C2A 2827"            /* ïÿ.çE13210/-,*(' */
    $"2524 2322 201F 1D1C 1C1B 1919 1813 0BFB"            /* %$#" ..........û */
    $"09FE 0802 0605 B5FB FF0C 5F15 1B1B 1C1B"            /* Æþ....µûÿ._..... */
    $"1918 1613 110E B4F8 FFFF FF02 10FD FF01"            /* ......´øÿÿÿ..ýÿ. */
    $"560B FD12 000C F809 0202 28EF FEFF 2A83"            /* V.ý...øÆ..(ïþÿ* */
    $"0008 0909 0642 6965 6566 6668 6869 696B"            /* ..ÆÆ.Bieeffhhiik */
    $"6B6E 7272 2C35 3D3D 3E3F 4243 4345 4748"            /* knrr,5==>?BCCEGH */
    $"4D4E 340A 0104 0505 0606 FD07 FE09 FE0A"            /* MN4.......ý.þÆþ. */
    $"020B 0C0C FE0D 000E FE0F 0210 1111 FE12"            /* ....þÂ..þ.....þ. */
    $"FE13 0014 FE15 0216 1717 FE18 FE19 101A"            /* þ...þ.....þ.þ... */
    $"1919 475D 5D59 28B3 FFF7 F8FA FBFB FDFD"            /* ..G]]Y(³ÿ÷øúûûýý */
    $"FEFD F6FE 1DFD FFB3 2D31 3130 2F2E 2D2C"            /* þýöþ.ýÿ³-110/.-, */
    $"2A29 2726 2523 2220 1F1E 1D1C 1B1A 1919"            /* *)'&%#" ........ */
    $"1813 0BFB 09FE 08FF 0600 B9FB FF0C 9E15"            /* ...ûÆþ.ÿ..¹ûÿ.. */
    $"1A1A 1B1A 1918 1513 1016 D0F2 FF01 560B"            /* ..........Ðòÿ.V. */
    $"FE12 0111 0CF8 0902 0228 EFFE FF0F 8300"            /* þ....øÆ..(ïþÿ.. */
    $"0809 0906 4269 6565 6666 6868 6969 FF6B"            /* .ÆÆ.Bieeffhhiiÿk */
    $"186E 7271 2E48 5354 5658 595A 5D5E 6060"            /* .nrq.HSTVXYZ]^`` */
    $"6466 450C 0104 0505 0606 FD07 FE09 FE0A"            /* dfE.......ý.þÆþ. */
    $"020B 0C0C FE0D 000E FE0F 0210 1111 FE12"            /* ....þÂ..þ.....þ. */
    $"0313 1212 14FE 1502 1617 17FE 18FE 190E"            /* .....þ.....þ.þ.. */
    $"1A19 1A81 B3B1 A83A B2FF F7F8 FAFB FBFC"            /* ...³±¨:²ÿ÷øúûûü */
    $"FDF6 FE1B FDFF B32D 3131 302F 2E2D 2C2A"            /* ýöþ.ýÿ³-110/.-,* */
    $"2927 2625 2322 201F 1E1D 1C1B 1A19 1918"            /* )'&%#" ......... */
    $"0113 0BFB 09FE 08FF 0600 B9FB FF0C 9E15"            /* ...ûÆþ.ÿ..¹ûÿ.. */
    $"1A1A 1B1A 1918 1513 1016 D0F2 FF01 560B"            /* ..........Ðòÿ.V. */
    $"FD12 000C F809 0202 28EF FEFF 1D83 0008"            /* ý...øÆ..(ïþÿ... */
    $"0909 0642 6965 6566 6668 6869 696B 6B6E"            /* ÆÆ.Bieeffhhiikkn */
    $"7272 2C38 4041 4344 4547 4AFE 4C09 4E52"            /* rr,8@ACDEGJþLÆNR */
    $"370B 0104 0505 0606 FD07 FE09 FE0A 040B"            /* 7.......ý.þÆþ... */
    $"0C0C 0D0D 010D 0EFE 0F02 1011 11FE 1203"            /* ..ÂÂ.Â.þ.....þ.. */
    $"1312 1114 FE15 0216 1717 FE18 FE19 0E1A"            /* ....þ.....þ.þ... */
    $"1919 8EC8 C5BA 3EB3 FFF7 F8FA FBFB FCFD"            /* ..ÈÅº>³ÿ÷øúûûüý */
    $"F6FE 1DFD FFB3 2D31 3130 2F2E 2D2C 2A29"            /* öþ.ýÿ³-110/.-,*) */
    $"2726 2523 2220 1F1E 1D1C 1B1A 1919 1813"            /* '&%#" .......... */
    $"0BFB 09FE 08FF 0600 B9FB FF0C 9E15 1A1A"            /* .ûÆþ.ÿ..¹ûÿ.... */
    $"1B1A 1918 1513 1016 D0F8 FFFF FF02 1DFD"            /* ........Ðøÿÿÿ..ý */
    $"FF01 590B FE12 0211 0A08 F909 0100 89FD"            /* ÿ.Y.þ.....ùÆ..ý */
    $"FF1D 9200 0709 0904 2D66 6465 6666 6868"            /* ÿ...ÆÆ.-fdeffhh */
    $"6969 6B6B 6C6F 7332 2F3B 3D3E 3E40 4243"            /* iikklos2/;=>>@BC */
    $"FE46 FF48 074C 3D11 0104 0506 06FD 07FE"            /* þFÿH.L=......ý.þ */
    $"09FE 0A02 0B0C 0CFE 0D00 0EFE 0F00 10FE"            /* Æþ.....þÂ..þ...þ */
    $"11FF 1204 1114 1A13 14FE 1518 1617 1618"            /* .ÿ.......þ...... */
    $"1718 1919 1818 1947 5D5C 5624 B5FC F4F5"            /* .......G]\V$µüôõ */
    $"F6F7 F7F9 F9FF FAFE FBF9 FC1E FBFC FF78"            /* ö÷÷ùùÿúþûùü.ûüÿx */
    $"2730 2F2E 2D2C 2A2A 2827 2625 2322 211F"            /* '0/.-,**('&%#"!. */
    $"1F1D 1C1B 1A1A 1919 1814 0BFB 09FE 08FF"            /* ...........ûÆþ.ÿ */
    $"0600 B8FB FF02 BF20 18FD 1905 1715 140F"            /* ..¸ûÿ.¿ .ý...... */
    $"20EF F2FF 0159 0BFE 1202 110A 08F9 0901"            /*  ïòÿ.Y.þ.....ùÆ. */
    $"0089 FDFF 0F92 0007 0909 042D 6664 6566"            /* .ýÿ...ÆÆ.-fdef */
    $"6668 6869 69FF 6B18 6C6F 7233 4151 5254"            /* fhhiiÿk.lor3AQRT */
    $"5657 585B 5C5D 5F60 6469 5115 0004 0506"            /* VWX[\]_`diQ..... */
    $"06FD 07FE 09FE 0A02 0B0C 0CFE 0D00 0EFE"            /* .ý.þÆþ.....þÂ..þ */
    $"0F00 10FC 1104 1016 2113 14FE 151A 1617"            /* ...ü....!..þ.... */
    $"1618 1718 1919 1818 1982 B1AE A132 B6FC"            /* .........±®¡2¶ü */
    $"F4F5 F6F7 F7F9 F9FA FAFE FBF9 FC1C FBFC"            /* ôõö÷÷ùùúúþûùü.ûü */
    $"FF78 2730 2F2E 2D2C 2A2A 2827 2625 2322"            /* ÿx'0/.-,**('&%#" */
    $"211F 1F1D 1C1B 1A1A 1919 1801 140B FB09"            /* !.............ûÆ */
    $"FE08 FF06 00B8 FBFF 02BF 2018 FD19 0517"            /* þ.ÿ..¸ûÿ.¿ .ý... */
    $"1514 0F20 EFF2 FF01 590B FE12 0211 0A08"            /* ... ïòÿ.Y.þ..... */
    $"F909 0100 89FD FF18 9200 0709 0904 2D66"            /* ùÆ..ýÿ...ÆÆ.-f */
    $"6465 6666 6868 6969 6B6B 6C6F 7331 3340"            /* deffhhiikklos13@ */
    $"41FE 430E 4549 4B4A 494D 4F52 4112 0104"            /* AþC.EIKJIMORA... */
    $"0506 06FD 07FE 09FE 0A04 0B0C 0C0D 0D01"            /* ...ý.þÆþ.....ÂÂ. */
    $"0D0E FE0F 0010 FD11 0512 0F16 2313 14FE"            /* Â.þ...ý.....#..þ */
    $"1507 1617 1618 1718 1919 FE18 0F8D C5C2"            /* ..........þ..ÅÂ */
    $"B235 B5FC F4F5 F6F7 F7F9 F9FA FAFE FBF9"            /* ²5µüôõö÷÷ùùúúþûù */
    $"FC1E FBFC FF78 2730 2F2E 2D2C 2A2A 2827"            /* ü.ûüÿx'0/.-,**(' */
    $"2625 2322 211F 1F1D 1C1B 1A1A 1919 1814"            /* &%#"!........... */
    $"0BFB 09FE 08FF 0600 B8FB FF02 BF20 18FD"            /* .ûÆþ.ÿ..¸ûÿ.¿ .ý */
    $"1905 1715 140F 20EF F8FF FFFF 0212 FDFF"            /* ...... ïøÿÿÿ..ýÿ */
    $"0767 0913 1212 0F09 08FA 0902 0708 C9FD"            /* .gÆ....Æ.úÆ...Éý */
    $"FF1E 9C00 0709 0906 1963 6665 6666 6868"            /* ÿ...ÆÆ..cfeffhh */
    $"6969 6B6B 6C6D 7537 273B 3A3D 3E3D 3F43"            /* iikklmu7';:=>=?C */
    $"45FD 4607 494F 4423 0603 0606 FD07 FE09"            /* EýF.IOD#....ý.þÆ */
    $"FE0A FE0B FE0D 000E FE0F FF10 FF11 0710"            /* þ.þ.þÂ..þ.ÿ.ÿ... */
    $"0F16 344A 2311 14FE 15FE 16FB 170E 1947"            /* ..4J#..þ.þ.û...G */
    $"5D5A 5326 BCF8 F0F2 F2F3 F3F5 F5FF F6FE"            /* ]ZS&¼øðòòóóõõÿöþ */
    $"F7F9 F81E F7FB E346 2B2E 2E2D 2B2A 2928"            /* ÷ùø.÷ûãF+..-+*)( */
    $"2727 2423 2221 1F1E 1E1D 1A1A 1918 1817"            /* ''$#"!.......... */
    $"1613 0CFB 09FE 0802 050A C6FB FF0C DD23"            /* ...ûÆþ....Æûÿ.Ý# */
    $"1819 1918 1717 1513 0C2F F5F2 FF07 6709"            /* ........./õòÿ.gÆ */
    $"1312 120F 0908 FA09 0207 08C9 FDFF 0F9C"            /* ....Æ.úÆ...Éýÿ. */
    $"0007 0909 0619 6366 6566 6668 6869 69FF"            /* ..ÆÆ..cfeffhhiiÿ */
    $"6B18 6C6D 7537 3751 5052 5456 5759 5A5B"            /* k.lmu77QPRTVWYZ[ */
    $"5D5F 6063 685A 2E06 0105 06FD 07FE 09FE"            /* ]_`chZ.....ý.þÆþ */
    $"0AFE 0BFE 0D00 0EFE 0FFF 10FF 1107 0F0C"            /* .þ.þÂ..þ.ÿ.ÿ.... */
    $"1D64 8B34 0D14 FE15 FE16 FC17 1116 1B81"            /* .d4Â.þ.þ.ü.... */
    $"AEAC 9B33 BBF8 F0F2 F2F3 F3F5 F5F6 F6FE"            /* ®¬3»øðòòóóõõööþ */
    $"F7F9 F81C F7FB E346 2B2E 2E2D 2B2A 2928"            /* ÷ùø.÷ûãF+..-+*)( */
    $"2727 2423 2221 1F1E 1E1D 1A1A 1918 1817"            /* ''$#"!.......... */
    $"1601 130C FB09 FE08 0205 0AC6 FBFF 0CDD"            /* ....ûÆþ....Æûÿ.Ý */
    $"2318 1919 1817 1715 130C 2FF5 F2FF 0767"            /* #........./õòÿ.g */
    $"0913 1212 0F08 08FA 0902 0708 C9FD FF2A"            /* Æ......úÆ...Éýÿ* */
    $"9C00 0709 0906 1963 6665 6666 6868 6969"            /* ..ÆÆ..cfeffhhii */
    $"6B6B 6C6D 7537 293F 4141 4244 4547 4948"            /* kklmu7)?AABDEGIH */
    $"474C 4E4C 4F48 2505 0206 06FD 07FE 09FE"            /* GLNLOH%....ý.þÆþ */
    $"0AFE 0BFF 0D01 0D0E FE0F FF10 FF11 070F"            /* .þ.ÿÂ.Â.þ.ÿ.ÿ... */
    $"0B1F 6E9B 3B0D 14FE 15FE 16FC 1711 161A"            /* ..n;Â.þ.þ.ü.... */
    $"8CC3 BFAD 36BB F8F0 F2F2 F3F3 F5F5 F6F6"            /* Ã¿­6»øðòòóóõõöö */
    $"FEF7 F9F8 1EF7 FBE3 462B 2E2E 2D2B 2A29"            /* þ÷ùø.÷ûãF+..-+*) */
    $"2827 2724 2322 211F 1E1E 1D1A 1A19 1818"            /* (''$#"!......... */
    $"1716 130C FB09 FE08 0205 0AC6 FBFF 0CDD"            /* ....ûÆþ....Æûÿ.Ý */
    $"2318 1919 1817 1715 130C 2FF5 F8FF FFFF"            /* #........./õøÿÿÿ */
    $"0212 FDFF 0175 08FE 1302 0E08 08FA 0902"            /* ..ýÿ.u.þ.....úÆ. */
    $"003B FBFD FF2B A802 0609 0907 0F5A 6865"            /* .;ûýÿ+¨..ÆÆ..Zhe */
    $"6666 6868 6969 6B6B 6C6D 743D 1E3B 383A"            /* ffhhiikklmt=.;8: */
    $"3C3D 3E42 4445 4646 4547 4C4F 4E34 1302"            /* <=>BDEFFEGLON4.. */
    $"0306 FE07 FE09 FE0A FE0B FE0D FE0E 0F0F"            /* ..þ.þÆþ.þ.þÂþ... */
    $"1010 0E0D 1326 3F4E 5045 1B12 1415 15FE"            /* ...Â.&?NPE.....þ */
    $"16FB 170E 1B49 5B59 4E24 C1F3 EDED EFEF"            /* .û...I[YN$Áóííïï */
    $"F0F0 F2FF F2FE F3F8 F41D FD97 2A2D 2C2C"            /* ððòÿòþóøô.ý*-,, */
    $"2B29 2927 2626 2423 2221 201E 1E1D 1C1B"            /* +))'&&$#"! ..... */
    $"1919 1817 1716 140D FB09 FE08 0205 0CCD"            /* .......ÂûÆþ....Í */
    $"FBFF 0CF6 3B15 1919 1817 1614 130A 40FA"            /* ûÿ.ö;.........@ú */
    $"F2FF 0175 08FE 1302 0E08 08FA 0902 003B"            /* òÿ.u.þ.....úÆ..; */
    $"FBFD FF0F A802 0609 0907 0F5A 6865 6666"            /* ûýÿ.¨..ÆÆ..Zheff */
    $"6868 6969 FF6B 196C 6D74 3C29 504E 5053"            /* hhiiÿk.lmt<)PNPS */
    $"5456 5758 5A5C 5D5F 6062 6666 4517 0201"            /* TVWXZ\]_`bffE... */
    $"05FE 07FE 09FE 0AFE 0BFE 0DFE 0E0F 0F10"            /* .þ.þÆþ.þ.þÂþ.... */
    $"100C 0915 3F78 969A 8324 0E14 1515 FE16"            /* ..Æ.?x$....þ. */
    $"FC17 0E15 1F87 AAAA 932E C0F3 EDED EFEF"            /* ü....ªª.Àóííïï */
    $"F0F0 FEF2 FEF3 F8F4 1BFD 972A 2D2C 2C2B"            /* ððþòþóøô.ý*-,,+ */
    $"2929 2726 2624 2322 2120 1E1E 1D1C 1B19"            /* ))'&&$#"! ...... */
    $"1918 1717 1601 140D FB09 FE08 0205 0CCD"            /* .......ÂûÆþ....Í */
    $"FBFF 0CF6 3B15 1919 1817 1614 130A 40FA"            /* ûÿ.ö;.........@ú */
    $"F2FF 0175 08FE 1302 0E08 08FA 0902 003B"            /* òÿ.u.þ.....úÆ..; */
    $"FBFD FF2B A802 0609 0907 0F5A 6865 6666"            /* ûýÿ+¨..ÆÆ..Zheff */
    $"6868 6969 6B6B 6C6D 743D 1F3E 3F3F 3E41"            /* hhiikklmt=.>??>A */
    $"4243 4545 474B 4B4A 4B51 5236 1302 0306"            /* BCEEGKKJKQR6.... */
    $"FE07 FE09 FE0A FE0B FF0D 000D FE0E 0F0F"            /* þ.þÆþ.þ.ÿÂ.Âþ... */
    $"1010 0C08 1846 86A7 AB91 260D 1415 15FE"            /* .....F§«&Â...þ */
    $"16FC 170E 151F 94BD BBA4 30C0 F3ED EDEF"            /* .ü....½»¤0Àóííï */
    $"EFF0 F0FE F2FE F3F8 F41D FD97 2A2D 2C2C"            /* ïððþòþóøô.ý*-,, */
    $"2B29 2927 2626 2423 2221 201E 1E1D 1C1B"            /* +))'&&$#"! ..... */
    $"1919 1817 1716 140D FB09 FE08 0205 0CCD"            /* .......ÂûÆþ....Í */
    $"FBFF 0CF6 3B15 1919 1817 1614 130A 40FA"            /* ûÿ.ö;.........@ú */
    $"F8FF FFFF 0217 FDFF 0187 06FE 1302 0C08"            /* øÿÿÿ..ýÿ..þ.... */
    $"08FB 0902 0800 97FC FF02 BE08 06FE 0930"            /* .ûÆ...üÿ.¾..þÆ0 */
    $"063C 6965 6666 6868 6969 6B6B 6C6E 7349"            /* .<ieffhhiikklnsI */
    $"173A 3A39 3B3E 3F42 4241 4344 4447 4A4C"            /* .::9;>?BBACDDGJL */
    $"4D4F 4833 1A0A 0404 0708 0809 090A 0A0B"            /* MOH3.......ÆÆ... */
    $"0BFE 0CFE 0DFF 0E0E 0D0F 182A 3B48 494A"            /* .þ.þÂÿ..Â..*;HIJ */
    $"4A4C 3E18 1114 14FE 15FB 160E 1A49 5958"            /* JL>....þ.û...IYX */
    $"4B24 C6EE E8EA EAEB EBED EDFF EEFE EFF9"            /* K$Æîèêêëëííÿîþïù */
    $"F014 F6D4 4327 2B2A 2928 2826 2625 2322"            /* ð.öÔC'+*)((&&%#" */
    $"2221 1F1E 1E1D 1BFE 1A06 1918 1717 1614"            /* "!.....þ........ */
    $"0DFB 09FE 0802 0510 DBFA FF01 7F0D FE18"            /* ÂûÆþ....Ûúÿ..Âþ. */
    $"0517 1614 1207 58F1 FF01 8706 FE13 020C"            /* ......Xñÿ..þ... */
    $"0808 FB09 0208 0097 FCFF 02BE 0806 FE09"            /* ..ûÆ...üÿ.¾..þÆ */
    $"0906 3C69 6566 6668 6869 69FF 6B24 6C6E"            /* Æ.<ieffhhiiÿk$ln */
    $"7348 1F4D 4D4F 5152 5455 5658 5A5B 5D5E"            /* sH.MMOQRTUVXZ[]^ */
    $"6061 6469 5F43 220B 0304 0608 0809 090A"            /* `adi_C"......ÆÆ. */
    $"0A0B 0BFE 0CFC 0D0E 0B0E 2447 718D 928F"            /* ...þ.üÂ...$Gq */
    $"9097 7420 0F14 14FE 15FC 1611 151F 87A8"            /* t ...þ.ü....¨ */
    $"A78C 2DC6 EEE8 EAEA EBEB EDED EEEE FEEF"            /* §-Æîèêêëëííîîþï */
    $"F9F0 14F6 D443 272B 2A29 2828 2626 2523"            /* ùð.öÔC'+*)((&&%# */
    $"2222 211F 1E1E 1D1B FE1A 0419 1817 1716"            /* ""!.....þ....... */
    $"0114 0DFB 09FE 0802 0510 DBFA FF01 7F0D"            /* ..ÂûÆþ....Ûúÿ..Â */
    $"FE18 0517 1614 1207 58F1 FF01 8706 FE13"            /* þ.......Xñÿ..þ. */
    $"020C 0808 FB09 0208 0097 FCFF 02BE 0806"            /* ....ûÆ...üÿ.¾.. */
    $"FE09 3006 3C69 6566 6668 6869 696B 6B6C"            /* þÆ0.<ieffhhiikkl */
    $"6E73 4918 3C3D 3D3E 4142 4243 4545 4749"            /* nsI.<==>ABBCEEGI */
    $"4B4D 4D4F 544C 351C 0A04 0407 0808 0909"            /* KMMOTL5.......ÆÆ */
    $"0A0A 0B0B FE0C FC0D 0E0A 0E27 4F7D 9CA2"            /* ....þ.üÂ...'O}¢ */
    $"A0A0 A881 220F 1414 FE15 FC16 1114 2093"            /*   ¨"...þ.ü...  */
    $"B9BA 9C2D C6EE E8EA EAEB EBED EDEE EEFE"            /* ¹º-Æîèêêëëííîîþ */
    $"EFF9 F014 F6D4 4327 2B2A 2928 2826 2625"            /* ïùð.öÔC'+*)((&&% */
    $"2322 2221 1F1E 1E1D 1BFE 1A06 1918 1717"            /* #""!.....þ...... */
    $"1614 0DFB 09FE 0802 0510 DBFA FF01 7F0D"            /* ..ÂûÆþ....Ûúÿ..Â */
    $"FE18 0517 1614 1207 58F7 FFFF FF02 20FD"            /* þ.......X÷ÿÿÿ. ý */
    $"FF07 9D0B 1313 110B 0808 FB09 0206 0DD3"            /* ÿ........ûÆ..ÂÓ */
    $"FCFF 02D2 0D05 FE09 3206 1761 6766 6668"            /* üÿ.ÒÂ.þÆ2..agffh */
    $"6869 6A6B 6B6C 6E72 5A13 3638 393A 3D3E"            /* hijkklnrZ.689:=> */
    $"3F3F 4040 4144 4647 494B 4B4C 514F 3D29"            /* ??@@ADFGIKKLQO=) */
    $"1409 0405 0708 0909 0A0B 0A0A FE0B 100C"            /* .Æ....ÆÆ....þ... */
    $"0F14 1D2F 3F48 4947 4646 484A 4E38 1412"            /* .../?HIGFFHJN8.. */
    $"FD14 FB15 0E1C 4956 5646 24CC E9E4 E6E6"            /* ý.û...IVVF$Ìéäææ */
    $"E7E7 E9E9 02E9 EAEA FEEB FBEC 15ED F176"            /* ççéé.éêêþëûì.íñv */
    $"212A 2929 2827 2626 2523 2222 211F 1E1D"            /* !*))('&&%#""!... */
    $"1D1C 1AFE 1906 1817 1716 1514 0DFB 09FE"            /* ...þ........ÂûÆþ */
    $"0802 0413 E8FA FF03 A111 1718 FE16 0314"            /* ....èúÿ.¡...þ... */
    $"1204 6EF1 FF07 9D0B 1313 110B 0808 FB09"            /* ..nñÿ........ûÆ */
    $"0206 0DD3 FCFF 02D2 0D05 FE09 0906 1761"            /* ..ÂÓüÿ.ÒÂ.þÆÆ..a */
    $"6766 6668 6869 6AFF 6B3A 6C6E 7259 1849"            /* gffhhijÿk:lnrY.I */
    $"4B4C 4F51 5254 5556 595A 5C5D 5F60 6263"            /* KLOQRTUVYZ\]_`bc */
    $"676C 6750 3419 0902 0406 0708 090A 0A09"            /* glgP4.Æ.....Æ..Æ */
    $"0A0A 0908 090F 182E 577E 8F8F 8B8B 8D8E"            /* ..Æ.Æ...W~ */
    $"8F98 6916 11FD 14FC 150D 1324 8CA3 A385"            /* i..ý.ü.Â.$££ */
    $"29CD E8E4 E6E6 E7E7 FEE9 FFEA FEEB FBEC"            /* )Íèäææççþéÿêþëûì */
    $"15ED F176 212A 2929 2827 2626 2523 2222"            /* .íñv!*))('&&%#"" */
    $"211F 1E1D 1D1C 1AFE 1904 1817 1716 1501"            /* !......þ........ */
    $"140D FB09 FE08 0204 13E8 FAFF 03A1 1117"            /* .ÂûÆþ....èúÿ.¡.. */
    $"18FE 1603 1412 046E F1FF 079D 0B13 1311"            /* .þ.....nñÿ..... */
    $"0B08 08FB 0902 060D D3FC FF02 D20D 05FE"            /* ...ûÆ..ÂÓüÿ.ÒÂ.þ */
    $"0930 0617 6167 6666 6868 696A 6B6B 6C6E"            /* Æ0..agffhhijkkln */
    $"725A 1438 3B3A 3C40 4141 4344 4546 484B"            /* rZ.8;:<@AACDEFHK */
    $"4D4D 4B4E 5457 5340 2B16 0804 0507 0709"            /* MMKNTWS@+......Æ */
    $"090A 0AFE 0912 0807 090F 1A32 618C 9EA0"            /* Æ..þÆ...Æ..2a  */
    $"9A9B 9C9D 9FAA 7517 10FD 14FC 150D 1325"            /* ªu..ý.ü.Â.% */
    $"9AB5 B793 29CC E8E4 E6E6 E7E7 FEE9 FFEA"            /* µ·)Ìèäææççþéÿê */
    $"FEEB FBEC 15ED F176 212A 2929 2827 2626"            /* þëûì.íñv!*))('&& */
    $"2523 2222 211F 1E1D 1D1C 1AFE 1906 1817"            /* %#""!......þ.... */
    $"1716 1514 0DFB 09FE 0802 0413 E8FA FF03"            /* ....ÂûÆþ....èúÿ. */
    $"A111 1718 FE16 0314 1204 6EF7 FFFF FF02"            /* ¡...þ.....n÷ÿÿÿ. */
    $"24FD FF06 B214 1213 120A 08FA 0902 022A"            /* $ýÿ.²......úÆ..* */
    $"F6FC FF02 E814 04FE 0924 0807 486A 6666"            /* öüÿ.è..þÆ$..Hjff */
    $"6868 696A 6C6C 6D6E 7068 1832 3738 383A"            /* hhijllmnph.2788: */
    $"3C3C 3E40 3F41 4345 4445 494B 4A4A 4EFE"            /* <<>@?ACEDEIKJJNþ */
    $"5106 3B26 1D14 0F0B 0BFE 0C08 0F13 191F"            /* Q.;&.....þ...... */
    $"2834 3A42 46FE 4409 4645 4548 4B4B 4C2C"            /* (4:BFþDÆFEEHKKL, */
    $"1012 FE13 0014 FD15 0F13 1B49 5253 4026"            /* ..þ...ý....IRS@& */
    $"D3E3 E1E1 E3E3 E4E5 E502 E5E6 E6FE E7FB"            /* Óãááããäåå.åææþçû */
    $"E819 F0BE 3326 2928 2827 2625 2524 2221"            /* è.ð¾3&)(('&%%$"! */
    $"211F 1E1E 1D1C 1B1A 1919 1817 FE16 0215"            /* !...........þ... */
    $"140D FB09 FE08 0201 2CF7 FAFF 0ABD 1A16"            /* .ÂûÆþ...,÷úÿ.½.. */
    $"1717 1615 1312 038E F1FF 06B2 1412 1312"            /* .......ñÿ.².... */
    $"0A08 FA09 0202 2AF6 FCFF 02E8 1404 FE09"            /* ..úÆ..*öüÿ.è..þÆ */
    $"0908 0748 6A66 6668 6869 6AFF 6C3B 6D6E"            /* Æ..Hjffhhijÿl;mn */
    $"7068 1A44 4B4A 4C4F 5153 5456 5758 5A5B"            /* ph.DKJLOQSTVWXZ[ */
    $"5D5F 6062 6364 676B 6C6A 4E30 2318 110C"            /* ]_`bcdgkljN0#... */
    $"0B0B 0D0F 141D 2A39 4A62 7180 8987 8586"            /* ..Â...*9Jbq */
    $"8789 8A8B 8C8F 954D 0B10 FE12 FC14 0D11"            /* M..þ.ü.Â. */
    $"248C A0A2 7B2B D3E3 E1E1 E3E3 E4FE E5FF"            /* $ ¢{+Óãááããäþåÿ */
    $"E6FE E7FB E819 F0BE 3326 2928 2827 2625"            /* æþçûè.ð¾3&)(('&% */
    $"2524 2221 211F 1E1E 1D1C 1B1A 1919 1817"            /* %$"!!........... */
    $"FE16 0015 0114 0DFB 09FE 0802 012C F7FA"            /* þ.....ÂûÆþ...,÷ú */
    $"FF0A BD1A 1617 1716 1513 1203 8EF1 FF06"            /* ÿ.½.........ñÿ. */
    $"B214 1213 120A 08FA 0902 022A F6FC FF02"            /* ²......úÆ..*öüÿ. */
    $"E814 04FE 0933 0807 486A 6666 6868 696A"            /* è..þÆ3..Hjffhhij */
    $"6C6C 6D6E 7068 1834 3A39 3B3C 3E41 4243"            /* llmnph.4:9;<>ABC */
    $"4647 4547 4B4C 4A4D 5151 5356 5755 3F28"            /* FGEGKLJMQQSVWU?( */
    $"1D15 0F0A 0B0B 0D10 151F 132D 3D51 6C7F"            /* ......Â....-=Ql. */
    $"9198 9795 9898 9A9A 999B A0A5 540B 10FE"            /*  ¥T..þ */
    $"12FC 140D 1125 9BB2 B588 2BD3 E3E1 E1E3"            /* .ü.Â.%²µ+Óãááã */
    $"E3E4 FEE5 FFE6 FEE7 FBE8 19F0 BE33 2629"            /* ãäþåÿæþçûè.ð¾3&) */
    $"2828 2726 2525 2422 2121 1F1E 1E1D 1C1B"            /* (('&%%$"!!...... */
    $"1A19 1918 17FE 1602 1514 0DFB 09FE 0802"            /* .....þ....ÂûÆþ.. */
    $"012C F7FA FF0A BD1A 1617 1716 1513 1203"            /* .,÷úÿ.½......... */
    $"8EF7 FFFF FF02 27FD FF06 CB1D 1113 1009"            /* ÷ÿÿÿ.'ýÿ.Ë....Æ */
    $"08FA 0901 0059 FBFF 02F9 3400 FD09 3506"            /* .úÆ..Yûÿ.ù4.ýÆ5. */
    $"1C63 6766 6869 6A6A 6C6C 6D6E 6F73 2F28"            /* .cgfhijjllmnos/( */
    $"3936 3737 393B 3D3E 3F41 4243 4444 4848"            /* 96779;=>?ABCDDHH */
    $"494A 4A4D 4E50 5355 534E 4740 472F 2533"            /* IJJMNPSUSNG@G/%3 */
    $"3437 3D40 41FE 4204 4143 4546 46FE 4508"            /* 47=@AþB.ACEFFþE. */
    $"474A 4A46 2217 1614 13FC 110B 101B 4D51"            /* GJJF"....ü....MQ */
    $"5137 34D4 DFDD DEDE FEE0 00E1 FFE2 FEE3"            /* Q74ÔßÝÞÞþà.áÿâþã */
    $"FDE4 FFE5 FFE6 1867 1F28 2826 2625 2424"            /* ýäÿåÿæ.g.((&&%$$ */
    $"2222 2120 201E 1E1D 1C1B 1A1A 1919 1717"            /* ""!  ........... */
    $"FE16 0215 140D FB09 FE08 0100 54F9 FF02"            /* þ....ÂûÆþ...Tùÿ. */
    $"D31F 14FE 1604 1513 1011 C1F1 FF06 CB1D"            /* Ó..þ......Áñÿ.Ë. */
    $"1113 1109 08FA 0901 0059 FBFF 02F9 3400"            /* ...Æ.úÆ..Yûÿ.ù4. */
    $"FD09 0806 1C63 6766 6869 6A6A FF6C 186D"            /* ýÆ...cgfhijjÿl.m */
    $"6E6F 732F 364C 4A4B 4C4F 5152 5455 5657"            /* nos/6LJKLOQRTUVW */
    $"595B 5C5D 5F61 6262 FE66 336D 726C 655B"            /* Y[\]_abbþf3mrle[ */
    $"535B 3C47 6567 6E79 8083 8381 8080 8282"            /* S[<Gegny */
    $"8485 8687 898A 8A8E 8638 1E1C 1713 1010"            /* 8...... */
    $"0E0E 0F0B 2592 9CA0 6B37 D5DF DDDE DEFE"            /* ....% k7ÕßÝÞÞþ */
    $"E002 E1E2 E2FE E3FD E4FF E5FF E618 671F"            /* à.áââþãýäÿåÿæ.g. */
    $"2828 2626 2524 2422 2221 2020 1E1E 1D1C"            /* ((&&%$$""!  .... */
    $"1B1A 1A19 1917 17FE 1600 1501 140D FB09"            /* .......þ.....ÂûÆ */
    $"FE08 0100 54F9 FF02 D31F 14FE 1604 1513"            /* þ...Tùÿ.Ó..þ.... */
    $"1011 C1F1 FF06 CB1D 1113 1009 08FA 0901"            /* ..Áñÿ.Ë....Æ.úÆ. */
    $"0059 FBFF 02F9 3400 FD09 1006 1C63 6766"            /* .Yûÿ.ù4.ýÆ...cgf */
    $"6869 6A6A 6C6C 6D6E 6F73 2E2A FE3B 1E3C"            /* hijjllmnos.*þ;.< */
    $"3E3E 4143 4443 4444 4748 494C 4E4C 4F51"            /* >>ACDCDDGHILNLOQ */
    $"5153 595A 5752 4942 4A31 4F71 737B 0987"            /* QSYZWRIBJ1Oqs{Æ */
    $"8F92 928F 8E8E 8F91 93FE 961A 9798 9A9D"            /* þ. */
    $"953F 201D 1814 100F 0D0D 0E0A 28A3 ADB1"            /* ? .....ÂÂ..(£­± */
    $"7537 D4DF DDDE DEFE E002 E1E2 E2FE E3FD"            /* u7ÔßÝÞÞþà.áââþãý */
    $"E4FF E5FF E618 671F 2828 2626 2524 2422"            /* äÿåÿæ.g.((&&%$$" */
    $"2221 2020 1E1E 1D1C 1B1A 1A19 1917 17FE"            /* "!  ...........þ */
    $"1602 1514 0DFB 09FE 0801 0054 F9FF 02D3"            /* ....ÂûÆþ...Tùÿ.Ó */
    $"1F14 FE16 0415 1310 11C1 F7FF FFFF 022A"            /* ..þ......Á÷ÿÿÿ.* */
    $"FDFF 05E7 2311 1410 09FE 08FD 0902 0800"            /* ýÿ.ç#...Æþ.ýÆ... */
    $"90FA FF01 6A00 FD09 3008 074B 6C67 6969"            /* úÿ.j.ýÆ0..Klgii */
    $"6A6A 6C6C 6D6E 6E76 431C 3B38 3738 3A3B"            /* jjllmnnvC.;878:; */
    $"3B3C 3F41 4041 4445 4747 494A 4A4B 4C4E"            /* ;<?A@ADEGGIJJKLN */
    $"4F4F 5254 5659 5C3C 283D FE3B FE3C 233D"            /* OORTVY\<(=þ;þ<#= */
    $"3F40 4041 4243 4546 4644 4646 4745 4242"            /* ?@@ABCEFFDFFGEBB */
    $"4039 3232 2E29 2620 284C 5050 2E46 D7DA"            /* @922.)& (LPP.F×Ú */
    $"D9DA DBFE DC00 DDFF DEFE DFFE E0FF E10B"            /* ÙÚÛþÜ.ÝÿÞþßþàÿá. */
    $"E2EB A72A 2527 2625 2524 2222 FE20 FF1F"            /* âë§*%'&%%$""þ ÿ. */
    $"FF1D 051C 1B1A 1919 18FE 1700 16FE 1501"            /* ÿ........þ...þ.. */
    $"140D FB09 FE08 0100 7CF9 FF02 EB24 13FE"            /* .ÂûÆþ...|ùÿ.ë$.þ */
    $"1504 1413 0C26 F3F1 FF04 E723 1114 10FD"            /* .....&óñÿ.ç#...ý */
    $"08FD 0902 0800 90FA FF01 6A00 FD09 0808"            /* .ýÆ...úÿ.j.ýÆ.. */
    $"074B 6C67 6969 6A6A FF6C 256D 6E6E 7643"            /* .Klgiijjÿl%mnnvC */
    $"264E 4B4B 4C4D 4E50 5153 5556 585A 5B5D"            /* &NKKLMNPQSUVXZ[] */
    $"5E5F 6061 6364 6567 6A6C 6E71 747A 4E4E"            /* ^_`acdegjlnqtzNN */
    $"7DFD 79FF 7A23 7B7C 7D80 8081 8284 8586"            /* }ýyÿz#{|} */
    $"8889 898D 897F 7E78 685B 5A52 473F 3242"            /* .~xh[ZRG?2B */
    $"9398 9D5A 45D7 DAD9 DADB FEDC 02DD DEDE"            /* ZE×ÚÙÚÛþÜ.ÝÞÞ */
    $"FEDF FEE0 FFE1 0BE2 EBA7 2A25 2726 2525"            /* þßþàÿá.âë§*%'&%% */
    $"2422 22FE 20FF 1FFF 1D05 1C1B 1A19 1918"            /* $""þ ÿ.ÿ........ */
    $"FE17 0016 FE15 0114 0DFB 09FE 0801 007C"            /* þ...þ...ÂûÆþ...| */
    $"F9FF 02EB 2413 FE15 0414 130C 26F3 F1FF"            /* ùÿ.ë$.þ.....&óñÿ */
    $"04E7 2311 140F FD08 FD09 0208 0090 FAFF"            /* .ç#...ý.ýÆ...úÿ */
    $"016A 00FD 0911 0807 4B6C 6769 696A 6A6C"            /* .j.ýÆ...Klgiijjl */
    $"6C6D 6E6E 7643 1D3B FE3A FF3C 1B3F 4242"            /* lmnnvC.;þ:ÿ<.?BB */
    $"4144 4647 4848 4A4C 4B4D 4E4F 4F51 5256"            /* ADFGHHJLKMNOOQRV */
    $"595C 5D5F 3E57 8C89 8809 8688 8989 888A"            /* Y\]_>WÆ */
    $"8C8D 8E8F FE92 1A96 9897 989D 998B 8B84"            /* þ. */
    $"7162 6158 4D44 3648 A4A9 AE63 46D7 DAD9"            /* qbaXMD6H¤©®cF×ÚÙ */
    $"DADB FEDC 02DD DEDE FEDF FEE0 FFE1 0BE2"            /* ÚÛþÜ.ÝÞÞþßþàÿá.â */
    $"EBA7 2A25 2726 2525 2422 22FE 20FF 1FFF"            /* ë§*%'&%%$""þ ÿ.ÿ */
    $"1D05 1C1B 1A19 1918 FE17 0016 FE15 0114"            /* ........þ...þ... */
    $"0DFB 09FE 0801 007C F9FF 02EB 2413 FE15"            /* ÂûÆþ...|ùÿ.ë$.þ. */
    $"0414 130C 26F3 F7FF FFFF 022E FDFF 04FE"            /* ....&ó÷ÿÿÿ..ýÿ.þ */
    $"550D 140F FD08 FE09 0308 0414 DEFA FF02"            /* UÂ..ý.þÆ....Þúÿ. */
    $"9100 08FD 0910 0525 6768 6969 6A6A 6C6C"            /* ..ýÆ..%ghiijjll */
    $"6D6E 6E74 5515 39FE 3800 3AFE 3B05 3E3F"            /* mnntU.9þ8.:þ;.>? */
    $"3E3F 4245 FE46 0547 4949 4B4D 4DFE 4E1E"            /* >?BEþF.GIIKMMþN. */
    $"5153 553F 223B 3739 393A 3C3C 3B3C 3F40"            /* QSU?";799:<<;<?@ */
    $"3E3F 4042 4445 4546 4544 4648 494A 4BFE"            /* >?@BDEEFEDFHIJKþ */
    $"4D09 4C4D 4A4A 4C4C 4E27 5ADA FED5 FFD7"            /* MÆLMJJLLN'ZÚþÕÿ× */
    $"02D8 D9D9 FFDA FFDB FEDC FEDD 13E2 DE52"            /* .ØÙÙÿÚÿÛþÜþÝ.âÞR */
    $"1E26 2525 2323 2221 211F 1F1E 1E1C 1C1B"            /* .&%%##"!!....... */
    $"1AFE 1900 18FE 1700 16FE 15FF 1400 0DFB"            /* .þ...þ...þ.ÿ..Âû */
    $"09FF 0802 0700 98F9 FF02 FB48 0EFE 1504"            /* Æÿ....ùÿ.ûH.þ.. */
    $"1412 0848 FDF1 FF04 FE55 0D14 0FFD 08FE"            /* ...Hýñÿ.þUÂ..ý.þ */
    $"0903 0804 14DE FAFF 0291 0008 FD09 0705"            /* Æ....Þúÿ...ýÆ.. */
    $"2567 6869 696A 6AFF 6C4B 6D6E 6E74 541B"            /* %ghiijjÿlKmnntT. */
    $"4C4B 4B4C 4D4D 4E50 5152 5456 5859 5B5C"            /* LKKLMMNPQRTVXY[\ */
    $"5D5E 5F61 6264 6567 6969 6A6D 724F 3D78"            /* ]^_abdegiijmrO=x */
    $"7374 7577 7778 7979 7A7E 7E7F 8082 8384"            /* stuwwxyyz~~. */
    $"8486 8687 8B8D 8E90 9395 9597 9694 908F"            /*  */
    $"9394 9B4C 59DA FED5 FFD7 06D8 D9D9 DADA"            /* LYÚþÕÿ×.ØÙÙÚÚ */
    $"DBDB FEDC FEDD 13E2 DF52 1E26 2525 2323"            /* ÛÛþÜþÝ.âßR.&%%## */
    $"2221 211F 1F1E 1E1C 1C1B 1AFE 1900 18FE"            /* "!!........þ...þ */
    $"1700 16FE 1500 1401 140D FB09 FF08 0207"            /* ...þ.....ÂûÆÿ... */
    $"0098 F9FF 02FB 480E FE15 0414 1208 48FD"            /* .ùÿ.ûH.þ.....Hý */
    $"F1FF 04FE 550D 140F FD08 FE09 0308 0414"            /* ñÿ.þUÂ..ý.þÆ.... */
    $"DEFA FF02 9100 08FD 090F 0525 6768 6969"            /* Þúÿ...ýÆ..%ghii */
    $"6A6A 6C6C 6D6E 6E74 5516 FB3B 0B3C 3E40"            /* jjllmnntU.û;.<>@ */
    $"4142 4445 4647 4849 4BFD 4D0B 4F52 5355"            /* ABDEFGHIKýM.ORSU */
    $"5556 593D 4486 8384 2382 8486 8586 888A"            /* UVY=D# */
    $"8B8C 8D8E 9092 9597 9595 979B 9D9E A0A3"            /*  £ */
    $"A5A5 A7A6 A49E 9DA5 A5AB 5358 DAFE D5FF"            /* ¥¥§¦¤¥¥«SXÚþÕÿ */
    $"D706 D8D9 D9DA DADB DBFE DCFE DD13 E2DF"            /* ×.ØÙÙÚÚÛÛþÜþÝ.âß */
    $"521E 2625 2523 2322 2121 1F1F 1E1E 1C1C"            /* R.&%%##"!!...... */
    $"1B1A FE19 0018 FE17 0016 FE15 FF14 000D"            /* ..þ...þ...þ.ÿ..Â */
    $"FB09 FF08 0207 0098 F9FF 02FB 480E FE15"            /* ûÆÿ....ùÿ.ûH.þ. */
    $"0414 1208 48FD F7FF FFFF 0222 FCFF 0397"            /* ....Hý÷ÿÿÿ."üÿ. */
    $"0A13 0CFD 08FE 0903 0800 40FC FAFF 02B4"            /* ...ý.þÆ...@üúÿ.´ */
    $"0507 FD09 1008 074B 6C68 696A 6A6C 6C6D"            /* ..ýÆ...Klhijjllm */
    $"6E6E 716B 1D31 FD39 073A 3B3B 3A3D 3D3C"            /* nnqk.1ý9.:;;:==< */
    $"3FFD 4312 4549 4B4E 4E4D 4F50 5152 5355"            /* ?ýC.EIKNNMOPQRSU */
    $"481F 3A3A 3B3A 3BFE 3DFF 3E02 3F40 40FE"            /* H.::;:;þ=ÿ>.?@@þ */
    $"4103 4347 4647 FD45 FF46 FC48 FF4B 0D4A"            /* A.CGFGýEÿFüHÿKÂJ */
    $"494C 1C6D DCD0 D0D2 D2D3 D4D4 D504 D5D6"            /* IL.mÜÐÐÒÒÓÔÔÕ.ÕÖ */
    $"D6D7 D7FE D80D D9DB E47F 2025 2524 2322"            /* Ö××þØÂÙÛä. %%$#" */
    $"2221 2020 FE1E 0B1D 1C1C 1A1A 1819 1818"            /* "!  þ........... */
    $"1617 16FD 15FF 1400 0DFB 09FF 0802 0604"            /* ...ý.ÿ..ÂûÆÿ.... */
    $"AFF8 FF01 7B07 FE15 0314 1203 6BEF FF03"            /* ¯øÿ.{.þ.....kïÿ. */
    $"970A 130C FD08 FE09 0308 0040 FCFA FF02"            /* ...ý.þÆ...@üúÿ. */
    $"B405 07FD 0907 0807 4B6C 6869 6A6A FF6C"            /* ´..ýÆ...Klhijjÿl */
    $"096D 6E6E 716A 1E44 4D4C 4CFE 4D18 4E4F"            /* Æmnnqj.DMLLþM.NO */
    $"5052 5456 5758 595B 5E60 6265 6566 686A"            /* PRTVWXY[^`beefhj */
    $"6B6C 6E72 5C35 77FE 7606 7578 7A7A 7C7D"            /* klnr\5wþv.uxzz|} */
    $"7EFE 80FF 8200 84FE 8704 8889 8888 89FD"            /* ~þÿ.þ.ý */
    $"8B01 8C8E FD90 1096 3A6A DCD0 D0D2 D2D3"            /* .ý.:jÜÐÐÒÒÓ */
    $"D4D4 D5D5 D6D6 D7D7 FED8 0DD9 DBE4 7F20"            /* ÔÔÕÕÖÖ××þØÂÙÛä.  */
    $"2525 2423 2222 2120 20FE 1E0B 1D1C 1C1A"            /* %%$#""!  þ...... */
    $"1A18 1918 1816 1716 FD15 0014 0114 0DFB"            /* ........ý.....Âû */
    $"09FF 0802 0604 AFF8 FF01 7B07 FE15 0314"            /* Æÿ....¯øÿ.{.þ... */
    $"1203 6BEF FF03 970A 130C FD08 FE09 0308"            /* ..kïÿ....ý.þÆ.. */
    $"0040 FCFA FF02 B405 07FD 0911 0807 4B6C"            /* .@üúÿ.´..ýÆ...Kl */
    $"6869 6A6A 6C6C 6D6E 6E71 6B1D 353D FE3C"            /* hijjllmnnqk.5=þ< */
    $"FF3B 0B3C 3D40 4140 4143 4748 494B 4EFE"            /* ÿ;.<=@A@ACGHIKNþ */
    $"500B 5354 5456 5657 5B47 3A85 8485 0E84"            /* P.STTVVW[G:. */
    $"8387 8989 8A8B 8D8E 8E90 9293 9699 FE97"            /* þ */
    $"1E98 9A98 9A9D 9B9A 9B9D 9D9F A0A0 A2A7"            /* .  ¢§ */
    $"4069 DCD0 D0D2 D2D3 D4D4 D5D5 D6D6 D7D7"            /* @iÜÐÐÒÒÓÔÔÕÕÖÖ×× */
    $"FED8 0DD9 DBE4 7F20 2525 2423 2222 2120"            /* þØÂÙÛä. %%$#""!  */
    $"20FE 1E0B 1D1C 1C1A 1A18 1918 1816 1716"            /*  þ.............. */
    $"FD15 FF14 000D FB09 FF08 0206 04AF F8FF"            /* ý.ÿ..ÂûÆÿ....¯øÿ */
    $"017B 07FE 1503 1412 036B F6FF FFFF 021A"            /* .{.þ.....köÿÿÿ.. */
    $"FCFF 03BD 1811 09FD 08FE 0902 0800 66F9"            /* üÿ.½..Æý.þÆ...fù */
    $"FF02 D60D 05FC 0912 0620 676A 696A 6A6C"            /* ÿ.ÖÂ.üÆ.. gjijjl */
    $"6C6D 6E6E 7076 3A22 3B3A 3AFC 3B1A 3E3F"            /* lmnnpv:";::ü;.>? */
    $"3E40 4243 4443 413D 3A38 3632 312C 2C28"            /* >@BCDCA=:8621,,( */
    $"2325 230C 1A1C 1D1B 17FE 1926 1A1C 1C1D"            /* #%#......þ.&.... */
    $"2025 272D 3034 3739 3E43 4445 4746 4648"            /*  %'-0479>CDEGFFH */
    $"484A 4948 4847 4749 1B77 D7CC CCCE CECF"            /* HJIHHGGI.w×ÌÌÎÎÏ */
    $"D0D0 D104 D1D2 D2D3 D3FE D406 D5DF C02E"            /* ÐÐÑ.ÑÒÒÓÓþÔ.ÕßÀ. */
    $"2124 22FD 2103 201F 1E1E FE1C FF1A 0019"            /* !$"ý!. ...þ.ÿ... */
    $"FE18 0017 FE16 FE15 FE14 0113 0DFB 09FF"            /* þ...þ.þ.þ...ÂûÆÿ */
    $"0802 050C CBF8 FF08 9509 1515 1413 1106"            /* ....Ëøÿ.Æ...... */
    $"9CEF FF03 BD18 120A FD08 FE09 0208 0066"            /* ïÿ.½...ý.þÆ...f */
    $"F9FF 02D6 0D05 FC09 0606 2067 6A69 6A6A"            /* ùÿ.ÖÂ.üÆ.. gjijj */
    $"FF6C 096D 6E6E 7076 3930 4F4C 4CFE 4D2F"            /* ÿlÆmnnpv90OLLþM/ */
    $"5052 5253 5456 5859 5A59 5652 4E4A 4945"            /* PRRSTVXYZYVRNJIE */
    $"443C 3D37 3133 2D15 3638 3A35 2A30 3231"            /* D<=713-.68:5*021 */
    $"3135 3B3A 3F4A 4D5A 5F64 6B70 7882 8689"            /* 15;:?JMZ_dkpx */
    $"FE8C 188B 8D8F 8F8E 8E8D 8E91 3575 D7CC"            /* þ.5u×Ì */
    $"CCCE CECF D0D0 D1D1 D2D2 D3D3 FED4 06D5"            /* ÌÎÎÏÐÐÑÑÒÒÓÓþÔ.Õ */
    $"DFC0 2E21 2422 FD21 0320 1F1E 1EFE 1CFF"            /* ßÀ.!$"ý!. ...þ.ÿ */
    $"1A00 19FE 1800 17FE 16FE 15FE 1401 130D"            /* ...þ...þ.þ.þ...Â */
    $"FB09 FF08 0205 0CCB F8FF 0895 0915 1514"            /* ûÆÿ....Ëøÿ.Æ... */
    $"1311 069C EFFF 03BD 1812 0AFD 08FE 0902"            /* ...ïÿ.½...ý.þÆ. */
    $"0800 66F9 FF02 D60D 05FC 091C 0620 676A"            /* ..fùÿ.ÖÂ.üÆ.. gj */
    $"696A 6A6C 6C6D 6E6E 7076 3A24 3C3A 3C3D"            /* ijjllmnnpv:$<:<= */
    $"3B3B 3D3F 4241 4344 45FE 4710 4440 3D3A"            /* ;;=?BACDEþG.D@=: */
    $"3937 342E 2F2A 2628 2316 3D3F 4014 3B2E"            /* 974./*&(#.=?@.;. */
    $"3436 3736 3C43 4145 5255 6369 6F76 7C86"            /* 4676<CAERUciov| */
    $"9097 9AFD 9C03 9DA0 9F9E FEA0 10A3 3B75"            /* ý. þ .£;u */
    $"D7CC CCCE CECF D0D0 D1D1 D2D2 D3D3 FED4"            /* ×ÌÌÎÎÏÐÐÑÑÒÒÓÓþÔ */
    $"06D5 DFC0 2E21 2422 FD21 0320 1F1E 1EFE"            /* .ÕßÀ.!$"ý!. ...þ */
    $"1CFF 1A00 19FE 1800 17FE 16FE 15FE 1401"            /* .ÿ...þ...þ.þ.þ.. */
    $"130D FB09 FF08 0205 0CCB F8FF 0895 0915"            /* .ÂûÆÿ....Ëøÿ.Æ. */
    $"1514 1311 069C F6FF FFFF 0213 FCFF 03E5"            /* .....öÿÿÿ..üÿ.å */
    $"2311 09FD 08FF 0903 0807 0096 F9FF 02F5"            /* #.Æý.ÿÆ....ùÿ.õ */
    $"2602 FB09 1E05 396D 696A 6A6C 6C6D 6E6E"            /* &.ûÆ..9mijjllmnn */
    $"7075 5016 3A3C 3B3B 3D3C 3932 2C28 2722"            /* puP.:<;;=<92,('" */
    $"1814 1312 FE11 1B10 1321 2633 353A 4546"            /* ....þ....!&35:EF */
    $"4649 4746 464C 5653 5456 595A 5254 5043"            /* FIGFFLVSTVYZRTPC */
    $"3F32 25FD 1A19 191B 1B1C 1D1D 252E 3639"            /* ?2%ý........%.69 */
    $"3F42 4749 491C 81D1 C8C9 C9CB CBCC CDCD"            /* ?BGII.ÑÈÉÉËËÌÍÍ */
    $"01CD CEFE CFFE D00E D6CC 511E 2322 2121"            /* .ÍÎþÏþÐ.ÖÌQ.#"!! */
    $"2020 1F1E 1E1D 1DFD 1BFF 19FE 18FD 16FF"            /*   .....ý.ÿ.þ.ý.ÿ */
    $"15FE 14FF 1300 0DFB 09FF 0802 0418 EDF8"            /* .þ.ÿ..ÂûÆÿ....íø */
    $"FF08 A70E 1314 1413 0D1E E5EF FF03 E523"            /* ÿ.§.....Â.åïÿ.å# */
    $"1109 FD08 FF09 0308 0700 96F9 FF02 F526"            /* .Æý.ÿÆ....ùÿ.õ& */
    $"02FB 0905 0539 6D69 6A6A FF6C 076D 6E6E"            /* .ûÆ..9mijjÿl.mnn */
    $"7075 4F1D 4EFE 4F46 5251 4C43 3D38 3730"            /* puO.NþOFRQLC=870 */
    $"241D 1B19 1614 1413 1422 2733 3639 4345"            /* $........"'369CE */
    $"4747 4646 434A 5451 5252 5456 5151 4E42"            /* GGFFCJTQRRTVQQNB */
    $"3E33 271C 2021 2428 2B30 3639 3C4C 5C68"            /* >3'. !$(+069<L\h */
    $"6F7A 828B 9091 317F D1C8 C9C9 CBCB CCFE"            /* oz1.ÑÈÉÉËËÌþ */
    $"CD00 CEFE CFFE D00E D6CC 511E 2322 2121"            /* Í.ÎþÏþÐ.ÖÌQ.#"!! */
    $"2020 1F1E 1E1D 1DFD 1BFF 19FE 18FD 16FF"            /*   .....ý.ÿ.þ.ý.ÿ */
    $"15FE 1400 1301 130D FB09 FF08 0204 18ED"            /* .þ.....ÂûÆÿ....í */
    $"F8FF 08A7 0E13 1414 130D 1EE5 EFFF 02E5"            /* øÿ.§.....Â.åïÿ.å */
    $"2311 FC08 FF09 0308 0700 96F9 FF02 F526"            /* #.ü.ÿÆ....ùÿ.õ& */
    $"02FB 0910 0539 6D69 6A6A 6C6C 6D6E 6E70"            /* .ûÆ..9mijjllmnnp */
    $"7550 173D 3DFE 3F0B 3E3C 342F 2B2A 251B"            /* uP.==þ?.><4/+*%. */
    $"1615 1313 FE12 0C14 2328 3536 3A45 4547"            /* ....þ...#(56:EEG */
    $"4845 4443 2949 5450 5052 5558 5050 4D43"            /* HEDC)ITPPRUXPPMC */
    $"3E32 261D 2123 272A 2F35 3B3F 4354 6672"            /* >2&.!#'*.5;?CTfr */
    $"7B88 909B A0A2 377F D1C8 C9C9 CBCB CCFE"            /* { ¢7.ÑÈÉÉËËÌþ */
    $"CD00 CEFE CFFE D00E D6CC 521E 2322 2121"            /* Í.ÎþÏþÐ.ÖÌR.#"!! */
    $"2020 1F1E 1E1D 1DFD 1BFF 19FE 18FD 16FF"            /*   .....ý.ÿ.þ.ý.ÿ */
    $"15FE 14FF 1300 0DFB 09FF 0802 0418 EDF8"            /* .þ.ÿ..ÂûÆÿ....íø */
    $"FF08 A70E 1314 1413 0D1E E5F6 FFFF FF02"            /* ÿ.§.....Â.åöÿÿÿ. */
    $"08FB FF02 6409 09FA 0802 0510 DBF8 FF02"            /* .ûÿ.dÆÆú....Ûøÿ. */
    $"7500 08FC 092B 080E 546D 6A6A 6C6C 6D6E"            /* u..üÆ+..Tmjjllmn */
    $"6F70 7268 1933 3229 2013 0F0D 0C0B 1013"            /* oprh.32) ..Â.... */
    $"273A 444C 5660 6870 787D 8385 8B8D 9097"            /* ':DLV`hpx} */
    $"9798 FD9A 2B9B 9D9E A1A2 A4A8 AAAC ADAA"            /* ý+¡¢¤¨ª¬­ª */
    $"AAA7 A4A2 9B95 8D84 7D73 6A6A 624F 3A22"            /* ª§¤¢}sjjbO:" */
    $"1A1B 1A1B 1C1B 0B8B CCC4 C4C6 C6C7 C7C9"            /* .......ÌÄÄÆÆÇÇÉ */
    $"C9FF CAFF CB08 CCCD CDD1 C958 1922 21FE"            /* ÉÿÊÿË.ÌÍÍÑÉX."!þ */
    $"20FF 1FFD 1DFF 1BFE 1A01 1918 FE17 FE16"            /*  ÿ.ý.ÿ.þ....þ.þ. */
    $"FF15 FE14 FF13 0112 0DFB 09FF 0802 0034"            /* ÿ.þ.ÿ...ÂûÆÿ...4 */
    $"F9F8 FF08 B712 1214 1313 0942 FBEE FF02"            /* ùøÿ.·.....ÆBûîÿ. */
    $"6408 09FA 0802 0510 DBF8 FF02 7500 08FC"            /* d.Æú....Ûøÿ.u..ü */
    $"0905 080E 546D 6A6A FF6C 606D 6E6F 7072"            /* Æ...Tmjjÿl`mnopr */
    $"681B 4544 392D 1D16 120F 0D10 1327 3943"            /* h.ED9-....Â..'9C */
    $"4B55 5F67 6F77 7C82 858B 8D90 9698 999A"            /* KU_gow| */
    $"9B9A 9A9C 9D9F A1A2 A5A8 ABAD ADA9 A9A7"            /* ¡¢¥¨«­­©©§ */
    $"A3A1 9994 8B81 7A70 6767 5F4E 3B24 2025"            /* £¡zpgg_N;$ % */
    $"272B 3336 128A CCC4 C4C6 C6C7 C7C9 C9CA"            /* '+36.ÌÄÄÆÆÇÇÉÉÊ */
    $"CACB CBCC CDCD D1C9 5819 2221 FE20 FF1F"            /* ÊËËÌÍÍÑÉX."!þ ÿ. */
    $"FD1D FF1B FE1A 0119 18FE 17FE 16FF 15FE"            /* ý.ÿ.þ....þ.þ.ÿ.þ */
    $"14FF 1301 120D FB09 FF08 0200 34F9 F8FF"            /* .ÿ...ÂûÆÿ...4ùøÿ */
    $"08B7 1212 1413 1309 42FB EEFF 0264 0909"            /* .·.....ÆBûîÿ.dÆÆ */
    $"FA08 0205 10DB F8FF 0275 0008 FC09 2B08"            /* ú....Ûøÿ.u..üÆ+. */
    $"0E54 6D6A 6A6C 6C6D 6E6F 7072 6819 3635"            /* .Tmjjllmnoprh.65 */
    $"2C23 1410 0F0D 0D11 1428 3A44 4D56 6068"            /* ,#...ÂÂ..(:DMV`h */
    $"7078 7D83 858B 8D90 9797 99FD 9A38 9B9E"            /* px}ý8 */
    $"9EA0 A2A6 A9AA ACAD AAA9 A6A3 A199 938A"            /*  ¢¦©ª¬­ª©¦£¡ */
    $"817A 6F66 665F 4D3A 2420 2629 2E36 3C15"            /* zoff_M:$ &).6<. */
    $"8BCC C4C4 C6C6 C7C7 C9C9 CACA CBCB CCCD"            /* ÌÄÄÆÆÇÇÉÉÊÊËËÌÍ */
    $"CDD1 C958 1922 21FE 20FF 1FFD 1DFF 1BFE"            /* ÍÑÉX."!þ ÿ.ý.ÿ.þ */
    $"1A01 1918 FE17 FE16 FF15 FE14 FF13 0112"            /* ....þ.þ.ÿ.þ.ÿ... */
    $"0DFB 09FF 0802 0034 F9F8 FF08 B712 1214"            /* ÂûÆÿ...4ùøÿ.·... */
    $"1313 0942 FBF6 FFFF FF02 11FB FF02 A60A"            /* ..ÆBûöÿÿÿ..ûÿ.¦. */
    $"07FA 0802 012C F6F8 FF02 A400 07FC 091A"            /* .ú...,öøÿ.¤..üÆ. */
    $"0A05 1F69 6C6A 6C6C 6D6E 6F70 7077 3905"            /* ...iljllmnoppw9. */
    $"0A0C 2238 4654 616D 7273 7AFE 813D 8281"            /* .."8FTamrszþ= */
    $"8283 8486 8689 8A8B 8D8D 8E90 9193 9596"            /*  */
    $"9799 999B 9C9C 9FA0 A1A3 A5A7 A9AB ACAE"            /*  ¡£¥§©«¬® */
    $"B1B3 B5B8 BABC BCBF BAB5 AFA5 988E 8679"            /* ±³µ¸º¼¼¿ºµ¯¥y */
    $"6B56 9EC4 C0C0 C2C2 C3C3 C5C5 00C6 FEC7"            /* kVÄÀÀÂÂÃÃÅÅ.ÆþÇ */
    $"FFC8 04CF CB64 141D FE20 FF1F 031E 1D1D"            /* ÿÈ.ÏËd..þ ÿ..... */
    $"1CFE 1BFF 1A08 1819 1918 1717 1615 16FE"            /* .þ.ÿ...........þ */
    $"15FF 14FE 1301 120D FB09 FF08 0100 56F7"            /* .ÿ.þ...ÂûÆÿ...V÷ */
    $"FF07 C516 1214 1312 036A EDFF 02A6 0A07"            /* ÿ.Å......jíÿ.¦.. */
    $"FA08 0201 2CF6 F8FF 02A4 0007 FC09 050A"            /* ú...,öøÿ.¤..üÆ.. */
    $"051F 696C 6AFF 6C12 6D6E 6F70 7077 3909"            /* ..iljÿl.mnoppw9Æ */
    $"0E0D 2237 4654 616C 7273 7AFE 813E 8281"            /* .Â"7FTalrszþ> */
    $"8283 8486 8689 8A8B 8D8D 8E90 9193 9596"            /*  */
    $"9898 999B 9C9C 9EA1 A1A3 A5A7 A9AB ACAE"            /* ¡¡£¥§©«¬® */
    $"B1B3 B5B8 BABC BCBF BAB4 AEA4 968C 8376"            /* ±³µ¸º¼¼¿º´®¤v */
    $"6856 9FC4 C0C0 C2C2 C3C3 C5C5 C6FE C7FF"            /* hVÄÀÀÂÂÃÃÅÅÆþÇÿ */
    $"C804 CFCB 6414 1DFE 20FF 1F03 1E1D 1D1C"            /* È.ÏËd..þ ÿ...... */
    $"FE1B FF1A 0818 1919 1817 1716 1516 FE15"            /* þ.ÿ...........þ. */
    $"FF14 FE13 0112 0DFB 09FF 0801 0056 F7FF"            /* ÿ.þ...ÂûÆÿ...V÷ÿ */
    $"07C5 1612 1413 1203 6AED FF02 A60A 07FA"            /* .Å......jíÿ.¦..ú */
    $"0802 012C F6F8 FF02 A400 07FC 091A 0A05"            /* ...,öøÿ.¤..üÆ... */
    $"1F69 6C6A 6C6C 6D6E 6F70 7077 3906 0C0D"            /* .iljllmnoppw9..Â */
    $"2338 4754 626D 7274 7AFE 8111 8281 8283"            /* #8GTbmrtzþ. */
    $"8485 8789 8A8B 8D8D 8F8F 9193 9596 FF98"            /* ÿ */
    $"2A99 9B9C 9C9F A0A1 A3A5 A7A9 ABAC AEB1"            /* * ¡£¥§©«¬®± */
    $"B3B5 B8BA BCBC BEBA B4AE A495 8B82 7567"            /* ³µ¸º¼¼¾º´®¤ug */
    $"569F C4C0 C0C2 C2C3 C3C5 C5C6 FEC7 FFC8"            /* VÄÀÀÂÂÃÃÅÅÆþÇÿÈ */
    $"04CF CB64 141D FE20 FF1F 031E 1D1D 1CFE"            /* .ÏËd..þ ÿ......þ */
    $"1BFF 1A08 1819 1918 1717 1615 16FE 15FF"            /* .ÿ...........þ.ÿ */
    $"14FE 1301 120D FB09 FF08 0100 56F7 FF07"            /* .þ...ÂûÆÿ...V÷ÿ. */
    $"C516 1214 1312 036A F5FF FFFF 020C FBFF"            /* Å......jõÿÿÿ..ûÿ */
    $"02DD 1B04 FA08 0100 4FF7 FF02 D50D 05FD"            /* .Ý..ú...O÷ÿ.ÕÂ.ý */
    $"09FE 0A19 0631 6C6D 6B6C 6D6E 6E70 7073"            /* Æþ...1lmklmnnpps */
    $"634A 5B6B 757C 7C7B 7A79 797A 7979 FE7A"            /* cJ[ku||{zyyzyyþz */
    $"FF7B 3A7D 7F80 8184 8687 8889 898A 8B8C"            /* ÿ{:}. */
    $"8E8E 9091 9294 9596 989B 9E9F A0A2 A3A4"            /*  ¢£¤ */
    $"A5A7 A8A9 AAAC ADAD AEAF B0B3 B5B7 BABC"            /* ¥§¨©ª¬­­®¯°³µ·º¼ */
    $"BFC0 C3C1 BBBA BCBC BEBE BFBF C0C1 FFC2"            /* ¿ÀÃÁ»º¼¼¾¾¿¿ÀÁÿÂ */
    $"FFC3 09C4 CBB3 5318 1C1F 1F1E 1EFE 1D07"            /* ÿÃÆÄË³S......þ.. */
    $"1C1B 1B1A 1A19 1918 FC17 0716 1515 1415"            /* ........ü....... */
    $"1514 14FE 13FF 1200 0DFB 09FF 0801 0088"            /* ...þ.ÿ..ÂûÆÿ... */
    $"F7FF 07D5 1C11 1413 100E B9ED FF02 DD1B"            /* ÷ÿ.Õ......¹íÿ.Ý. */
    $"04FA 0801 004F F7FF 02D5 0D05 FD09 FE0A"            /* .ú...O÷ÿ.ÕÂ.ýÆþ. */
    $"0306 316C 6D15 6B6C 6D6E 6E70 7074 644A"            /* ..1lm.klmnnpptdJ */
    $"5A6A 757C 7C7B 7A79 797A 7979 FE7A FF7B"            /* Zju||{zyyzyyþzÿ{ */
    $"487D 7F80 8184 8687 8889 898A 8B8D 8E8F"            /* H}. */
    $"9091 9294 9596 989A 9E9F A0A2 A3A4 A5A7"            /*  ¢£¤¥§ */
    $"A8A9 AAAC ADAD AEAF B0B3 B5B7 BABC BFC0"            /* ¨©ª¬­­®¯°³µ·º¼¿À */
    $"C3C1 BBBA BCBC BEBE BFBF C0C1 C2C2 C3C3"            /* ÃÁ»º¼¼¾¾¿¿ÀÁÂÂÃÃ */
    $"C4CB B353 181C 1F1F 1E1E FE1D 071C 1B1B"            /* ÄË³S......þ..... */
    $"1A1A 1919 18FC 1707 1615 1514 1515 1414"            /* .....ü.......... */
    $"FE13 0012 0112 0DFB 09FF 0801 0088 F7FF"            /* þ.....ÂûÆÿ...÷ÿ */
    $"07D5 1C11 1413 100E B9ED FF02 DD1B 04FA"            /* .Õ......¹íÿ.Ý..ú */
    $"0801 004F F7FF 02D5 0D05 FD09 FE0A 1906"            /* ...O÷ÿ.ÕÂ.ýÆþ... */
    $"316C 6D6B 6C6D 6E6E 7070 7464 4A5B 6B75"            /* 1lmklmnnpptdJ[ku */
    $"7C7C 7B7A 7979 7A79 79FE 7AFF 7B0E 7D7F"            /* ||{zyyzyyþzÿ{.}. */
    $"8081 8486 8788 8989 8A8B 8D8E 8E39 9091"            /* 9 */
    $"9294 9596 989A 9E9F A0A2 A3A4 A5A7 A8A9"            /*  ¢£¤¥§¨© */
    $"AAAC ADAD AEAF B0B3 B5B7 BABC BFC0 C3C1"            /* ª¬­­®¯°³µ·º¼¿ÀÃÁ */
    $"BBBA BCBC BEBE BFBF C0C1 C2C2 C3C3 C4CB"            /* »º¼¼¾¾¿¿ÀÁÂÂÃÃÄË */
    $"B353 181C 1F1F 1E1E FE1D 071C 1B1B 1A1A"            /* ³S......þ....... */
    $"1919 18FC 1707 1615 1514 1515 1414 FE13"            /* ...ü..........þ. */
    $"FF12 000D FB09 FF08 0100 88F7 FF07 D51C"            /* ÿ..ÂûÆÿ...÷ÿ.Õ. */
    $"1114 1310 0EB9 F5FF FFFF 01F6 FAFF 0161"            /* .....¹õÿÿÿ.öúÿ.a */
    $"00FA 0801 006C F7FF 02FE 4300 FD09 FE0A"            /* .ú...l÷ÿ.þC.ýÆþ. */
    $"0F09 0534 6E6D 6C6D 6E6E 7070 7174 7877"            /* .Æ.4nmlmnnppqtxw */
    $"76FE 75FE 76FE 7800 79FE 7A00 7BFE 7CFF"            /* vþuþvþx.yþz.{þ|ÿ */
    $"7D36 8082 8383 8485 8686 8788 8989 8C8D"            /* }6 */
    $"8E8F 9092 9599 9B9C 9E9F A0A1 A2A3 A4A6"            /*  ¡¢£¤¦ */
    $"A7A9 A9AA ABAC ADAE AFB0 B1B1 B3B3 B5B5"            /* §©©ª«¬­®¯°±±³³µµ */
    $"B6B7 B8B9 B9BB BBBC BCFE BE08 BFC7 AA3C"            /* ¶·¸¹¹»»¼¼þ¾.¿Çª< */
    $"111B 1E1F 1EFE 1DFF 1CFE 1B00 1AFE 1900"            /* .....þ.ÿ.þ...þ.. */
    $"18FE 17FF 16FE 15FD 14FF 13FD 1200 0DFB"            /* .þ.ÿ.þ.ý.ÿ.ý..Âû */
    $"0903 0805 0FD6 F7FF 07E4 2010 1212 0A35"            /* Æ....Ö÷ÿ.ä ....5 */
    $"F7EC FF01 6100 FA08 0100 6CF7 FF02 FE43"            /* ÷ìÿ.a.ú...l÷ÿ.þC */
    $"00FD 09FE 0A03 0905 346E 0B6D 6C6D 6E6E"            /* .ýÆþ..Æ.4n.mlmnn */
    $"7070 7174 7877 76FE 75FE 76FE 7800 79FE"            /* ppqtxwvþuþvþx.yþ */
    $"7A00 7BFE 7CFF 7D36 8082 8384 8485 8686"            /* z.{þ|ÿ}6 */
    $"8788 898A 8C8D 8E8F 9092 9599 9B9C 9E9F"            /*  */
    $"A0A1 A2A3 A4A6 A7A9 A9AA ABAC ADAE AFB0"            /*  ¡¢£¤¦§©©ª«¬­®¯° */
    $"B1B1 B3B3 B5B5 B6B7 B8B9 B9BB BBBC BCFE"            /* ±±³³µµ¶·¸¹¹»»¼¼þ */
    $"BE08 BFC7 AA3C 111B 1E1F 1EFE 1DFF 1CFE"            /* ¾.¿Çª<.....þ.ÿ.þ */
    $"1B00 1AFE 1900 18FE 17FF 16FE 15FD 14FF"            /* ...þ...þ.ÿ.þ.ý.ÿ */
    $"13FE 1201 120D FB09 0308 050F D6F7 FF07"            /* .þ...ÂûÆ....Ö÷ÿ. */
    $"E420 1012 120A 35F7 ECFF 0161 00FA 0801"            /* ä ....5÷ìÿ.a.ú.. */
    $"006C F7FF 02FE 4300 FD09 FE0A 0F09 0534"            /* .l÷ÿ.þC.ýÆþ..Æ.4 */
    $"6E6D 6C6D 6E6E 7070 7174 7877 76FE 75FE"            /* nmlmnnppqtxwvþuþ */
    $"76FE 7800 79FE 7A00 7BFE 7CFF 7D0A 8082"            /* vþx.yþz.{þ|ÿ}. */
    $"8383 8585 8686 8788 882B 8A8B 8D8E 8F90"            /* + */
    $"9295 999B 9C9E 9FA0 A1A2 A3A4 A6A7 A9A9"            /*  ¡¢£¤¦§©© */
    $"AAAB ACAD AEAF B0B1 B1B3 B3B5 B5B6 B7B8"            /* ª«¬­®¯°±±³³µµ¶·¸ */
    $"B9B9 BBBB BCBC FEBE 08BF C7AA 3C11 1B1E"            /* ¹¹»»¼¼þ¾.¿Çª<... */
    $"1F1E FE1D FF1C FE1B 001A FE19 0018 FE17"            /* ..þ.ÿ.þ...þ...þ. */
    $"FF16 FE15 FD14 FF13 FD12 000D FB09 0308"            /* ÿ.þ.ý.ÿ.ý..ÂûÆ.. */
    $"050F D6F7 FF07 E420 1012 120A 35F7 F5FF"            /* ..Ö÷ÿ.ä ....5÷õÿ */
    $"FFFF 01F0 FAFF 02AD 0207 FB08 0100 8BF6"            /* ÿÿ.ðúÿ.­..û...ö */
    $"FF02 9600 08FD 09FE 0A09 0906 3870 6D6D"            /* ÿ...ýÆþ.ÆÆ.8pmm */
    $"6E6E 7070 FE71 0172 73FE 7400 75FE 7600"            /* nnppþq.rsþt.uþv. */
    $"77FE 7800 79FE 7AFD 7C36 7D7F 8080 8182"            /* wþx.yþzý|6}. */
    $"8283 8484 8587 8889 8A8A 8B8E 9295 9799"            /*  */
    $"9A9B 9C9D 9E9F A0A2 A3A4 A5A6 A7A8 A9AA"            /*  ¢£¤¥¦§¨©ª */
    $"ABAC ADAD AFB0 B1B1 B2B3 B4B5 B6B6 B8B8"            /* «¬­­¯°±±²³´µ¶¶¸¸ */
    $"B9FF BA09 BCC2 AA42 141B 1E1E 1D1D FE1C"            /* ¹ÿºÆ¼ÂªB......þ. */
    $"FF1B 001A FE19 FE18 FE17 FF16 FE15 FF14"            /* ÿ...þ.þ.þ.ÿ.þ.ÿ. */
    $"FD13 FD12 0111 0CFB 0903 0800 31F8 F7FF"            /* ý.ý....ûÆ...1ø÷ÿ */
    $"06F1 210F 1312 0466 EBFF 02AD 0207 FB08"            /* .ñ!....fëÿ.­..û. */
    $"0100 8BF6 FF02 9600 08FD 09FE 0A02 0906"            /* ..öÿ...ýÆþ..Æ. */
    $"3806 706D 6D6E 6E70 70FE 7101 7273 FE74"            /* 8.pmmnnppþq.rsþt */
    $"0075 FE76 0077 FE78 0079 FE7A FD7C 427D"            /* .uþv.wþx.yþzý|B} */
    $"7F80 8081 8282 8384 8586 8788 898A 8A8B"            /* . */
    $"8E92 9597 999A 9B9C 9D9E 9FA0 A2A3 A4A5"            /*  ¢£¤¥ */
    $"A6A7 A8A9 AAAB ACAD ADAF B0B1 B1B2 B3B4"            /* ¦§¨©ª«¬­­¯°±±²³´ */
    $"B5B6 B6B8 B8B9 BABA BCC2 AA42 141B 1E1E"            /* µ¶¶¸¸¹ºº¼ÂªB.... */
    $"1D1D FE1C FF1B 001A FE19 FE18 FE17 FF16"            /* ..þ.ÿ...þ.þ.þ.ÿ. */
    $"FE15 FF14 FD13 FD12 0111 0CFB 0903 0800"            /* þ.ÿ.ý.ý....ûÆ... */
    $"31F8 F7FF 06F1 210F 1312 0466 EBFF 02AD"            /* 1ø÷ÿ.ñ!....fëÿ.­ */
    $"0207 FB08 0100 8BF6 FF02 9600 08FD 09FE"            /* ..û...öÿ...ýÆþ */
    $"0A09 0906 3870 6D6D 6E6E 7070 FE71 0172"            /* .ÆÆ.8pmmnnppþq.r */
    $"73FE 7400 75FE 7600 77FE 7800 79FE 7AFD"            /* sþt.uþv.wþx.yþzý */
    $"7C02 7D7F 80FE 8104 8384 8385 8637 8688"            /* |.}.þ.7 */
    $"898A 8A8B 8E92 9597 999A 9B9C 9D9E 9FA0"            /*   */
    $"A2A3 A4A5 A6A7 A8A9 AAAB ACAD ADAF B0B1"            /* ¢£¤¥¦§¨©ª«¬­­¯°± */
    $"B1B2 B3B4 B5B6 B6B8 B8B9 BABA BCC2 AA42"            /* ±²³´µ¶¶¸¸¹ºº¼ÂªB */
    $"141B 1E1E 1D1D FE1C FF1B 001A FE19 FE18"            /* ......þ.ÿ...þ.þ. */
    $"FE17 FF16 FE15 FF14 FD13 FD12 0111 0CFB"            /* þ.ÿ.þ.ÿ.ý.ý....û */
    $"0903 0800 31F8 F7FF 06F1 210F 1312 0466"            /* Æ...1ø÷ÿ.ñ!....f */
    $"F4FF FFFF 01DC FAFF 02E8 2103 FC08 0206"            /* ôÿÿÿ.Üúÿ.è!.ü... */
    $"07B9 F6FF 02CD 0906 FD09 FD0A 0809 0845"            /* .¹öÿ.ÍÆ.ýÆý..Æ.E */
    $"726F 6E6E 7070 FE71 0172 73FE 7402 7576"            /* ronnppþq.rsþt.uv */
    $"76FE 7700 78FE 79FE 7AFD 7C01 7D7E FE7F"            /* vþw.xþyþzý|.}~þ. */
    $"0580 8182 8384 85FE 8618 8788 8C8F 9293"            /* .þ. */
    $"9596 9798 999B 9C9D 9E9F A0A1 A1A3 A3A5"            /*  ¡¡££¥ */
    $"A6A7 A8FE AA0B ACAD ADAE AFB0 B1B2 B3B3"            /* ¦§¨þª.¬­­®¯°±²³³ */
    $"B5B5 05B6 BABF 9337 18FD 1DFE 1CFF 1BFE"            /* µµ.¶º¿7.ý.þ.ÿ.þ */
    $"1AFD 18FF 17FE 16FF 15FD 14FD 13FD 1202"            /* .ý.ÿ.þ.ÿ.ý.ý.ý.. */
    $"1110 0BFB 0902 0800 61F6 FF06 F329 0E12"            /* ...ûÆ...aöÿ.ó).. */
    $"1005 99EB FF02 E821 03FC 0802 0607 B9F6"            /* ..ëÿ.è!.ü....¹ö */
    $"FF02 CD09 06FD 09FD 0A01 0908 0645 726F"            /* ÿ.ÍÆ.ýÆý..Æ..Ero */
    $"6E6E 7070 FE71 0172 73FE 7402 7576 76FE"            /* nnppþq.rsþt.uvvþ */
    $"7700 78FE 79FE 7AFD 7C01 7D7E FE7F 0580"            /* w.xþyþzý|.}~þ.. */
    $"8182 8384 85FE 8618 8788 8C90 9293 9596"            /* þ. */
    $"9798 999B 9C9D 9E9F A0A1 A1A3 A3A5 A6A7"            /*  ¡¡££¥¦§ */
    $"A8FE AA11 ACAD ADAE AFB0 B1B2 B3B3 B5B5"            /* ¨þª.¬­­®¯°±²³³µµ */
    $"B6BA BF93 3718 FD1D FE1C FF1B FE1A FD18"            /* ¶º¿7.ý.þ.ÿ.þ.ý. */
    $"FF17 FE16 FF15 FD14 FD13 FD12 0011 0110"            /* ÿ.þ.ÿ.ý.ý.ý..... */
    $"0BFB 0902 0800 61F6 FF06 F329 0E12 1005"            /* .ûÆ...aöÿ.ó).... */
    $"99EB FF02 E821 03FC 0802 0607 B9F6 FF02"            /* ëÿ.è!.ü....¹öÿ. */
    $"CD09 06FD 09FD 0A08 0908 4572 6F6E 6E70"            /* ÍÆ.ýÆý..Æ.Eronnp */
    $"70FE 7101 7273 FE74 0275 7676 FE77 0078"            /* pþq.rsþt.uvvþw.x */
    $"FE79 FE7A FD7C 017D 7EFE 7F04 8081 8283"            /* þyþzý|.}~þ.. */
    $"8400 85FE 8618 8788 8C90 9293 9596 9798"            /* .þ. */
    $"999B 9C9D 9E9F A0A1 A1A3 A3A5 A6A7 A8FE"            /*  ¡¡££¥¦§¨þ */
    $"AA11 ACAD ADAE AFB0 B1B2 B3B3 B5B5 B6BA"            /* ª.¬­­®¯°±²³³µµ¶º */
    $"BF93 3718 FD1D FE1C FF1B FE1A FD18 FF17"            /* ¿7.ý.þ.ÿ.þ.ý.ÿ. */
    $"FE16 FF15 FD14 FD13 FD12 0211 100B FB09"            /* þ.ÿ.ý.ý.ý.....ûÆ */
    $"0208 0061 F6FF 06F3 290E 1210 0599 F4FF"            /* ...aöÿ.ó)....ôÿ */
    $"FFFF 01E2 F9FF 0181 00FC 0802 0415 E7F6"            /* ÿÿ.âùÿ..ü....çö */
    $"FF02 FC3E 00FD 09FC 0AFF 0905 4370 716E"            /* ÿ.ü>.ýÆü.ÿÆ.Cpqn */
    $"7070 FE71 0172 73FE 7402 7576 76FE 7700"            /* ppþq.rsþt.uvvþw. */
    $"78FE 79FE 7A05 7B7C 7B7C 7D7D FE7E 217F"            /* xþyþz.{|{|}}þ~!. */
    $"8081 8283 8485 8586 8788 8B8E 8F90 9192"            /*  */
    $"9495 9697 9899 9A9B 9C9D 9E9F A0A0 A1A3"            /*   ¡£ */
    $"A4FE A60B A8A9 AAAA ABAC ADAF AFB0 B0B2"            /* ¤þ¦.¨©ªª«¬­¯¯°°² */
    $"04B8 B077 2417 FC1C FE1B FE1A FF19 FE18"            /* .¸°w$.ü.þ.þ.ÿ.þ. */
    $"FE17 FE16 0515 1414 1314 14FD 13FD 1202"            /* þ.þ........ý.ý.. */
    $"1110 0AFB 0902 0700 A6F6 FF06 F632 0D12"            /* ...ûÆ...¦öÿ.ö2Â. */
    $"0E13 CFEA FF01 8100 FC08 0204 15E7 F6FF"            /* ..Ïêÿ..ü....çöÿ */
    $"02FC 3E00 FD09 FC0A 0009 0609 4370 716E"            /* .ü>.ýÆü..Æ.ÆCpqn */
    $"7070 FE71 0172 73FE 7402 7576 76FE 7700"            /* ppþq.rsþt.uvvþw. */
    $"78FE 79FE 7A05 7B7C 7B7C 7D7D FE7E 217F"            /* xþyþz.{|{|}}þ~!. */
    $"8081 8283 8485 8586 8788 8B8E 8F90 9192"            /*  */
    $"9495 9697 9899 9A9B 9C9D 9E9F A0A0 A1A3"            /*   ¡£ */
    $"A4FE A610 A8A9 AAAA ABAC ADAF AFB0 B0B2"            /* ¤þ¦.¨©ªª«¬­¯¯°°² */
    $"B8B0 7724 17FC 1CFE 1BFE 1AFF 19FE 18FE"            /* ¸°w$.ü.þ.þ.ÿ.þ.þ */
    $"17FE 1605 1514 1413 1414 FD13 FD12 0011"            /* .þ........ý.ý... */
    $"0110 0AFB 0902 0700 A6F6 FF06 F632 0D12"            /* ...ûÆ...¦öÿ.ö2Â. */
    $"0E13 CFEA FF01 8100 FC08 0204 15E7 F6FF"            /* ..Ïêÿ..ü....çöÿ */
    $"02FC 3E00 FD09 FC0A FF09 0543 7071 6E70"            /* .ü>.ýÆü.ÿÆ.Cpqnp */
    $"70FE 7101 7273 FE74 0275 7676 FE77 0078"            /* pþq.rsþt.uvvþw.x */
    $"FE79 FE7A 057B 7C7B 7C7D 7DFE 7E04 7F80"            /* þyþz.{|{|}}þ~.. */
    $"8182 831C 8485 8586 8788 8B8E 8F90 9192"            /* . */
    $"9495 9697 9899 9A9B 9C9D 9E9F A0A0 A1A3"            /*   ¡£ */
    $"A4FE A610 A8A9 AAAA ABAC ADAF AFB0 B0B2"            /* ¤þ¦.¨©ªª«¬­¯¯°°² */
    $"B8B0 7724 17FC 1CFE 1BFE 1AFF 19FE 18FE"            /* ¸°w$.ü.þ.þ.ÿ.þ.þ */
    $"17FE 1605 1514 1413 1414 FD13 FD12 0211"            /* .þ........ý.ý... */
    $"100A FB09 0207 00A6 F6FF 06F6 320D 120E"            /* ..ûÆ...¦öÿ.ö2Â.. */
    $"13CF F4FF FFFF 01DA F9FF 02D8 1105 FD08"            /* .Ïôÿÿÿ.Úùÿ.Ø..ý. */
    $"0202 28F5 F5FF 029F 0008 FE09 FB0A 0609"            /* ..(õõÿ...þÆû..Æ */
    $"082D 6573 6F70 FE71 0072 FE73 0274 7575"            /* .-esopþq.rþs.tuu */
    $"FE76 0077 FE78 FF79 FD7A FF7B 007C FE7D"            /* þv.wþxÿyýzÿ{.|þ} */
    $"FF7E FE7F 1181 8283 8484 8587 888A 8B8C"            /* ÿ~þ.. */
    $"8D8E 8F91 9293 94FE 9517 9798 9A9B 9C9C"            /* þ. */
    $"9E9F 9FA1 A1A2 A3A4 A5A6 A7A7 A8AA ABAB"            /* ¡¡¢£¤¥¦§§¨ª«« */
    $"AEB4 068F 3C18 191B 1A1B FD1A FE19 FE18"            /* ®´.<.....ý.þ.þ. */
    $"FE17 FF16 FF15 0016 FE15 FF14 FD13 FC12"            /* þ.ÿ.ÿ...þ.ÿ.ý.ü. */
    $"FE11 0110 0AFC 0903 0801 2BF4 F6FF 05F8"            /* þ....üÆ...+ôöÿ.ø */
    $"3B0B 1104 5CE9 FF02 D811 05FD 0802 0228"            /* ;...\éÿ.Ø..ý...( */
    $"F5F5 FF02 9F00 08FE 09FB 0A06 0908 2D65"            /* õõÿ...þÆû..Æ.-e */
    $"736F 70FE 7100 72FE 7302 7475 75FE 7600"            /* sopþq.rþs.tuuþv. */
    $"77FE 78FF 79FD 7AFF 7B00 7CFE 7DFF 7EFE"            /* wþxÿyýzÿ{.|þ}ÿ~þ */
    $"7F11 8182 8384 8485 8788 8A8B 8C8D 8E8F"            /* .. */
    $"9192 9394 FE95 1E97 989A 9B9C 9C9E 9F9F"            /* þ. */
    $"A1A1 A2A3 A4A5 A6A7 A7A8 AAAB ABAE B48F"            /* ¡¡¢£¤¥¦§§¨ª««®´ */
    $"3C18 191B 1A1B FD1A FE19 FE18 FE17 FF16"            /* <.....ý.þ.þ.þ.ÿ. */
    $"FF15 0016 FE15 FF14 FD13 FC12 FE11 0110"            /* ÿ...þ.ÿ.ý.ü.þ... */
    $"0AFC 0903 0801 2BF4 F6FF 05F8 3B0B 1104"            /* .üÆ...+ôöÿ.ø;... */
    $"5CE9 FF02 D811 05FD 0802 0228 F5F5 FF02"            /* \éÿ.Ø..ý...(õõÿ. */
    $"9F00 08FE 09FB 0A06 0908 2D65 736F 70FE"            /* ..þÆû..Æ.-esopþ */
    $"7100 72FE 7302 7475 75FE 7600 77FE 78FF"            /* q.rþs.tuuþv.wþxÿ */
    $"79FD 7AFF 7B00 7CFE 7DFF 7EFE 7F00 8110"            /* yýzÿ{.|þ}ÿ~þ... */
    $"8283 8484 8587 888A 8B8C 8D8E 8F91 9293"            /*  */
    $"94FE 951E 9798 9A9B 9C9C 9E9F 9FA1 A1A2"            /* þ.¡¡¢ */
    $"A3A4 A5A6 A7A7 A8AA ABAB AEB4 8F3C 1819"            /* £¤¥¦§§¨ª««®´<.. */
    $"1B1A 1BFD 1AFE 19FE 18FE 17FF 16FF 1500"            /* ...ý.þ.þ.þ.ÿ.ÿ.. */
    $"16FE 15FF 14FD 13FC 12FE 1101 100A FC09"            /* .þ.ÿ.ý.ü.þ....üÆ */
    $"0308 012B F4F6 FF05 F83B 0B11 045C F3FF"            /* ...+ôöÿ.ø;...\óÿ */
    $"FFFF 01B3 F9FF 02FE 4100 FD08 0200 3BFB"            /* ÿÿ.³ùÿ.þA.ý...;û */
    $"F5FF 02DE 1105 FE09 FA0A 0709 051C 6575"            /* õÿ.Þ..þÆú..Æ..eu */
    $"6F70 70FE 7200 73FE 74FF 75FE 7600 77FE"            /* oppþr.sþtÿuþv.wþ */
    $"78FF 79FE 7AFE 7BFF 7CFE 7DFD 7E10 7F80"            /* xÿyþzþ{ÿ|þ}ý~.. */
    $"8181 8284 8586 8788 898A 8B8D 8E8F 90FE"            /* þ */
    $"9117 9394 9697 9898 9A9B 9B9D 9D9E 9FA0"            /* .  */
    $"A1A2 A3A3 A4A6 A7AD AC77 0225 1319 FC1A"            /* ¡¢££¤¦§­¬w.%..ü. */
    $"FD19 FD18 FD17 FE16 FF15 FD14 FE13 FC12"            /* ý.ý.ý.þ.ÿ.ý.þ.ü. */
    $"FC11 010F 0AFC 0902 0800 63F5 FF05 FB45"            /* ü....üÆ...cõÿ.ûE */
    $"090F 09AA E9FF 02FE 4100 FD08 0200 3BFB"            /* Æ.Æªéÿ.þA.ý...;û */
    $"F5FF 02DE 1105 FE09 FB0A 080A 0905 1C65"            /* õÿ.Þ..þÆû...Æ..e */
    $"756F 7070 FE72 0073 FE74 FF75 FE76 0077"            /* uoppþr.sþtÿuþv.w */
    $"FE78 FF79 FE7A FE7B FF7C FE7D FD7E 107F"            /* þxÿyþzþ{ÿ|þ}ý~.. */
    $"8081 8182 8485 8687 8889 8A8B 8D8E 8F90"            /*  */
    $"FE91 1A93 9496 9798 989A 9B9B 9D9D 9E9F"            /* þ. */
    $"A0A1 A2A3 A3A4 A6A7 ADAC 7725 1319 FC1A"            /*  ¡¢££¤¦§­¬w%..ü. */
    $"FD19 FD18 FD17 FE16 FF15 FD14 FE13 FC12"            /* ý.ý.ý.þ.ÿ.ý.þ.ü. */
    $"FC11 010F 0AFC 0902 0800 63F5 FF05 FB45"            /* ü....üÆ...cõÿ.ûE */
    $"090F 09AA E9FF 02FE 4100 FD08 0200 3BFB"            /* Æ.Æªéÿ.þA.ý...;û */
    $"F5FF 02DE 1105 FE09 FA0A 0709 051C 6575"            /* õÿ.Þ..þÆú..Æ..eu */
    $"6F70 70FE 7200 73FE 74FF 75FE 7600 77FE"            /* oppþr.sþtÿuþv.wþ */
    $"78FF 79FE 7AFE 7BFF 7CFE 7DFD 7E10 7F80"            /* xÿyþzþ{ÿ|þ}ý~.. */
    $"8181 8284 8586 8788 898A 8B8D 8E8F 90FE"            /* þ */
    $"911A 9394 9697 9898 9A9B 9B9D 9D9E 9FA0"            /* .  */
    $"A1A2 A3A3 A4A6 A7AD AC77 2513 19FC 1AFD"            /* ¡¢££¤¦§­¬w%..ü.ý */
    $"19FD 18FD 17FE 16FF 15FD 14FE 13FC 12FC"            /* .ý.ý.þ.ÿ.ý.þ.ü.ü */
    $"1101 0F0A FC09 0208 0063 F5FF 05FB 4509"            /* ....üÆ...cõÿ.ûEÆ */
    $"0F09 AAF3 FFFF FF01 9AF8 FF02 A101 07FE"            /* .Æªóÿÿÿ.øÿ.¡..þ */
    $"0801 004B F4FF 02FE 4000 FD09 F90A 0A07"            /* ...Kôÿ.þ@.ýÆù... */
    $"1D5B 7570 7071 7172 7373 FE74 0075 FE76"            /* .[uppqqrssþt.uþv */
    $"FF77 FE78 FD79 FE7A FF7B FF7C FC7D FD7E"            /* ÿwþxýyþzÿ{ÿ|ü}ý~ */
    $"2780 8181 8284 8585 8788 898A 8B8C 8D8E"            /* ' */
    $"8E8F 9192 9394 9596 9799 9A9A 9B9C 9D9E"            /*  */
    $"9FA0 A0A1 A4A9 904A 1A00 16F9 19FD 18FD"            /*   ¡¤©J...ù.ý.ý */
    $"17FE 16FD 15FE 14FD 13FC 12FC 1102 100D"            /* .þ.ý.þ.ý.ü.ü...Â */
    $"0AFC 0902 0605 B7F5 FF05 FB44 0A0D 1AE2"            /* .üÆ...·õÿ.ûD.Â.â */
    $"E8FF 02A1 0107 FE08 0100 4BF4 FF02 FE40"            /* èÿ.¡..þ...Kôÿ.þ@ */
    $"00FD 09FC 0AFE 0A0A 071D 5B75 7070 7171"            /* .ýÆü.þ....[uppqq */
    $"7273 73FE 7400 75FE 76FF 77FE 78FD 79FE"            /* rssþt.uþvÿwþxýyþ */
    $"7AFF 7BFF 7CFC 7DFD 7E28 8081 8182 8485"            /* zÿ{ÿ|ü}ý~( */
    $"8587 8889 8A8B 8C8D 8E8E 8F91 9293 9495"            /*  */
    $"9697 999A 9A9B 9C9D 9E9F A0A0 A1A4 A990"            /*   ¡¤© */
    $"4A1A 16F9 19FD 18FD 17FE 16FD 15FE 14FD"            /* J..ù.ý.ý.þ.ý.þ.ý */
    $"13FC 12FC 1100 1001 0D0A FC09 0206 05B7"            /* .ü.ü....Â.üÆ...· */
    $"F5FF 05FB 440A 0D1A E2E8 FF02 A101 07FE"            /* õÿ.ûD.Â.âèÿ.¡..þ */
    $"0801 004B F4FF 02FE 4000 FD09 F90A 0A07"            /* ...Kôÿ.þ@.ýÆù... */
    $"1D5B 7570 7071 7172 7373 FE74 0075 FE76"            /* .[uppqqrssþt.uþv */
    $"FF77 FE78 FD79 FE7A FF7B FF7C FC7D FD7E"            /* ÿwþxýyþzÿ{ÿ|ü}ý~ */
    $"2880 8181 8284 8585 8788 898A 8B8C 8D8E"            /* ( */
    $"8E8F 9192 9394 9596 9799 9A9A 9B9C 9D9E"            /*  */
    $"9FA0 A0A1 A4A9 904A 1A16 F919 FD18 FD17"            /*   ¡¤©J..ù.ý.ý. */
    $"FE16 FD15 FE14 FD13 FC12 FC11 0210 0D0A"            /* þ.ý.þ.ý.ü.ü...Â. */
    $"FC09 0206 05B7 F5FF 05FB 440A 0D1A E2F3"            /* üÆ...·õÿ.ûD.Â.âó */
    $"FFFF FF01 BAF8 FF02 F934 00FE 0801 005A"            /* ÿÿÿ.ºøÿ.ù4.þ...Z */
    $"F3FF 0294 0008 FE09 F90A 080B 0612 4E77"            /* óÿ...þÆù.....Nw */
    $"7371 7172 FE73 FE74 FE76 0877 7676 7877"            /* sqqrþsþtþv.wvvxw */
    $"7879 7879 FE7A FF7B FE7C FD7D FF7E FF7D"            /* xyxyþzÿ{þ|ý}ÿ~ÿ} */
    $"FE7E FF80 2281 8284 8586 8788 8889 8A8B"            /* þ~ÿ" */
    $"8D8D 8E90 9191 9293 9596 9697 9899 9A9B"            /*  */
    $"9C9E A39A 6325 1117 FC19 FF18 0017 FD18"            /* £c%..ü.ÿ...ý. */
    $"FD17 0D15 1616 1514 1515 1413 1414 1212"            /* ý.Â............. */
    $"13FB 12FC 1101 100D FB09 0200 35FA F5FF"            /* .û.ü...ÂûÆ..5úõÿ */
    $"04FA 3B07 0063 E7FF 02F9 3400 FE08 0100"            /* .ú;..cçÿ.ù4.þ... */
    $"5AF3 FF02 9400 08FE 09FC 0AFE 0A08 0B06"            /* Zóÿ...þÆü.þ.... */
    $"124E 7773 7171 72FE 73FE 74FE 7608 7776"            /* .Nwsqqrþsþtþv.wv */
    $"7678 7778 7978 79FE 7AFF 7BFE 7CFD 7DFF"            /* vxwxyxyþzÿ{þ|ý}ÿ */
    $"7EFF 7DFE 7EFF 8022 8182 8485 8687 8888"            /* ~ÿ}þ~ÿ" */
    $"898A 8B8D 8D8E 9091 9192 9395 9696 9798"            /*  */
    $"999A 9B9C 9EA3 9A63 2511 17FC 19FF 1800"            /* £c%..ü.ÿ.. */
    $"17FD 18FD 170D 1516 1615 1415 1514 1314"            /* .ý.ý.Â.......... */
    $"1412 1213 FB12 FC11 0010 000D FB09 0200"            /* ....û.ü....ÂûÆ.. */
    $"35FA F5FF 04FA 3B07 0063 E7FF 02F9 3400"            /* 5úõÿ.ú;..cçÿ.ù4. */
    $"FE08 0100 5AF3 FF02 9400 08FE 09F9 0A08"            /* þ...Zóÿ...þÆù.. */
    $"0B06 124E 7773 7171 72FE 73FE 74FE 7608"            /* ...Nwsqqrþsþtþv. */
    $"7776 7678 7778 7978 79FE 7AFF 7BFE 7CFD"            /* wvvxwxyxyþzÿ{þ|ý */
    $"7DFF 7EFF 7DFE 7EFF 8022 8182 8485 8687"            /* }ÿ~ÿ}þ~ÿ" */
    $"8888 898A 8B8D 8D8E 9091 9192 9395 9696"            /*  */
    $"9798 999A 9B9C 9EA3 9A63 2511 17FC 19FF"            /* £c%..ü.ÿ */
    $"1800 17FD 18FD 170D 1516 1615 1415 1514"            /* ...ý.ý.Â........ */
    $"1314 1412 1213 FB12 FC11 0110 0DFB 0902"            /* ......û.ü...ÂûÆ. */
    $"0035 FAF5 FF04 FA3B 0700 63F2 FFFF FF01"            /* .5úõÿ.ú;..còÿÿÿ. */
    $"81F7 FF06 9500 0708 0800 64F3 FF02 F126"            /* ÷ÿ......dóÿ.ñ& */
    $"01FE 09F9 0AFF 0B07 080F 3B6D 7774 7272"            /* .þÆù.ÿ....;mwtrr */
    $"FE73 0074 FE75 FC76 FE77 0878 7978 797A"            /* þs.tþuüvþw.xyxyz */
    $"797B 7B7A FD7B FD7C FD7D FE7E 217F 8081"            /* y{{zý{ý|ý}þ~!. */
    $"8283 8384 8586 8889 898B 8C8D 8E8F 9090"            /*  */
    $"9292 9395 9696 999E 9D77 3313 1418 1700"            /* w3..... */
    $"18FD 17F9 16FC 15FD 14FB 13FC 12FC 11FD"            /* .ý.ù.ü.ý.û.ü.ü.ý */
    $"1000 0DFC 0902 0800 7EF3 FF03 4400 00B2"            /* ..ÂüÆ...~óÿ.D..² */
    $"E6FF 0695 0007 0808 0064 F3FF 02F1 2601"            /* æÿ......dóÿ.ñ&. */
    $"FE09 FC0A FE0A FF0B 0708 0F3B 6D77 7472"            /* þÆü.þ.ÿ....;mwtr */
    $"72FE 7300 74FE 75FC 76FE 7708 7879 7879"            /* rþs.tþuüvþw.xyxy */
    $"7A79 7B7B 7AFD 7BFD 7CFD 7DFD 7E21 8081"            /* zy{{zý{ý|ý}ý~! */
    $"8283 8384 8586 8889 898B 8C8D 8E8F 9090"            /*  */
    $"9292 9395 9696 999E 9D77 3313 1418 1718"            /* w3..... */
    $"FD17 F916 FC15 FD14 FB13 FC12 FC11 FD10"            /* ý.ù.ü.ý.û.ü.ü.ý. */
    $"000D FC09 0208 007D F3FF 0344 0000 B2E6"            /* .ÂüÆ...}óÿ.D..²æ */
    $"FF06 9500 0708 0800 64F3 FF02 F126 01FE"            /* ÿ......dóÿ.ñ&.þ */
    $"09F9 0AFF 0B07 080F 3B6D 7774 7272 FE73"            /* Æù.ÿ....;mwtrrþs */
    $"0074 FE75 FC76 FE77 0878 7978 797A 797B"            /* .tþuüvþw.xyxyzy{ */
    $"7B7A FD7B 007C FE7C FD7D FD7E 2180 8182"            /* {zý{.|þ|ý}ý~! */
    $"8383 8485 8688 8989 8B8C 8D8E 8F90 9092"            /*  */
    $"9293 9596 9699 9E9D 7733 1314 1817 18FD"            /* w3.....ý */
    $"17F9 16FC 15FD 14FB 13FC 12FC 11FD 1000"            /* .ù.ü.ý.û.ü.ü.ý.. */
    $"0DFC 0902 0800 7DF3 FF03 4400 00B2 F2FF"            /* ÂüÆ...}óÿ.D..²òÿ */
    $"FFFF 015E F7FF 06FA 3B00 0808 0071 F2FF"            /* ÿÿ.^÷ÿ.ú;....qòÿ */
    $"0180 00FE 09F8 0AFF 0B0B 0905 1D45 6876"            /* ..þÆø.ÿ..Æ..Ehv */
    $"7472 7373 7474 FD75 FE76 FF77 FD78 FE79"            /* trssttýuþvÿwýxþy */
    $"FD7A FD7B FD7C FC7D FD7E 007F FE80 1A82"            /* ýzý{ý|ü}ý~..þ. */
    $"8383 8486 8788 888A 8B8C 8C8E 8F8F 9094"            /*  */
    $"988C 6A42 1A10 1617 1616 F516 FC15 FD14"            /* jB......õ.ü.ý. */
    $"FB13 FE12 FA11 FC10 000C FD09 0308 0222"            /* û.þ.ú.ü...ýÆ..." */
    $"E4F3 FF03 D192 BDFD E6FF 06FA 3B00 0808"            /* äóÿ.Ñ½ýæÿ.ú;... */
    $"0071 F2FF 0180 00FE 09FC 0AFD 0AFF 0B0B"            /* .qòÿ..þÆü.ý.ÿ.. */
    $"0905 1D45 6876 7472 7373 7474 FD75 FE76"            /* Æ..Ehvtrssttýuþv */
    $"FF77 FD78 FE79 FD7A FD7B FD7C FC7D FD7E"            /* ÿwýxþyýzý{ý|ü}ý~ */
    $"007F FE80 1882 8383 8486 8788 888A 8B8C"            /* ..þ. */
    $"8C8E 8F8F 9094 988C 6A42 1A10 1617 F316"            /* jB....ó. */
    $"FC15 FD14 FB13 FE12 FA11 FC10 000C FD09"            /* ü.ý.û.þ.ú.ü...ýÆ */
    $"0308 0221 E4F3 FF03 D192 BDFD E6FF 06FA"            /* ...!äóÿ.Ñ½ýæÿ.ú */
    $"3B00 0808 0071 F2FF 0180 00FE 09F8 0AFF"            /* ;....qòÿ..þÆø.ÿ */
    $"0B0B 0905 1D45 6876 7472 7373 7474 FD75"            /* ..Æ..Ehvtrssttýu */
    $"FE76 FF77 FD78 FE79 FD7A FD7B FD7C FC7D"            /* þvÿwýxþyýzý{ý|ü} */
    $"FD7E 007F FE80 1882 8383 8486 8788 888A"            /* ý~..þ. */
    $"8B8C 8C8E 8F8F 9094 988C 6A42 1A10 1617"            /* jB.... */
    $"F316 FC15 FD14 FB13 FE12 FA11 FC10 000C"            /* ó.ü.ý.û.þ.ú.ü... */
    $"FD09 0308 0222 E4F3 FF03 D192 BDFD F2FF"            /* ýÆ..."äóÿ.Ñ½ýòÿ */
    $"FFFF 0131 F6FF 05AD 0504 0700 75F2 FF02"            /* ÿÿ.1öÿ.­....uòÿ. */
    $"ED25 01FE 09F9 0AFF 0BFF 0A08 0705 194B"            /* í%.þÆù.ÿ.ÿ.....K */
    $"6C78 7573 73FE 74FD 75FF 76FD 77FD 78FE"            /* lxussþtýuÿvýwýxþ */
    $"79FE 7AFB 7BFC 7CFB 7DFE 7EFF 7F12 8082"            /* yþzû{ü|û}þ~ÿ.. */
    $"8384 8685 8688 888A 8D90 9286 6430 120F"            /* d0.. */
    $"13FC 15F5 15FA 14FC 13FD 12FB 11FA 1001"            /* .ü.õ.ú.ü.ý.û.ú.. */
    $"0F0B FD09 0208 0071 D2FF 05AD 0504 0700"            /* ..ýÆ...qÒÿ.­.... */
    $"75F2 FF02 ED25 01FE 09FD 0AFD 0AFF 0BFF"            /* uòÿ.í%.þÆý.ý.ÿ.ÿ */
    $"0A08 0705 194B 6C78 7573 73FE 74FD 75FF"            /* .....Klxussþtýuÿ */
    $"76FD 77FD 78FE 79FE 7AFB 7BFC 7CFB 7DFE"            /* výwýxþyþzû{ü|û}þ */
    $"7EFF 7F12 8082 8384 8685 8688 888A 8D90"            /* ~ÿ.. */
    $"9286 6430 120F 13F0 15FA 14FC 13FD 12FB"            /* d0...ð.ú.ü.ý.û */
    $"11FA 1000 0F00 0BFD 0902 0800 72D2 FF05"            /* .ú.....ýÆ...rÒÿ. */
    $"AD05 0407 0075 F2FF 02ED 2501 FE09 F90A"            /* ­....uòÿ.í%.þÆù. */
    $"FF0B FF0A 0807 0519 4B6C 7875 7373 FE74"            /* ÿ.ÿ.....Klxussþt */
    $"FD75 FF76 FD77 FD78 FE79 FE7A FF7B FD7B"            /* ýuÿvýwýxþyþzÿ{ý{ */
    $"FC7C FB7D FE7E FF7F 1280 8283 8486 8586"            /* ü|û}þ~ÿ.. */
    $"8888 8A8D 9092 8664 3012 0F13 F015 FA14"            /* d0...ð.ú. */
    $"FC13 FD12 FB11 FA10 010F 0BFD 0902 0800"            /* ü.ý.û.ú....ýÆ... */
    $"72DF FFFF FF01 16F5 FF00 49FE 0000 71F1"            /* rßÿÿÿ..õÿ.Iþ..qñ */
    $"FF01 7400 FE09 F80A FC0B FF08 061B 4969"            /* ÿ.t.þÆø.ü.ÿ...Ii */
    $"7777 7473 FE74 FE75 FD76 FD77 FD78 FE79"            /* wwtsþtþuývýwýxþy */
    $"FC7A FC7B FA7C FD7D 117E 7F7F 8081 8283"            /* üzü{ú|ý}.~.. */
    $"8385 898C 806F 5325 1110 13FA 14F3 14FB"            /* oS%...ú.ó.û */
    $"13FC 12FA 11FB 10FE 0F01 0E0A FD09 0203"            /* .ü.ú.û.þ....ýÆ.. */
    $"1ADC D1FF 0049 FE00 0071 F1FF 0174 00FE"            /* .ÜÑÿ.Iþ..qñÿ.t.þ */
    $"09FD 0AFC 0AFC 0BFF 0806 1B49 6977 7774"            /* Æý.ü.ü.ÿ...Iiwwt */
    $"73FE 74FE 75FD 76FD 77FD 78FE 79FC 7AFC"            /* sþtþuývýwýxþyüzü */
    $"7BFA 7CFD 7D11 7E7F 7F80 8182 8383 8589"            /* {ú|ý}.~.. */
    $"8C80 6F53 2511 1013 EC14 FB13 FC12 FA11"            /* oS%...ì.û.ü.ú. */
    $"FB10 FE0F 000E 000A FD09 0203 1ADC D1FF"            /* û.þ.....ýÆ...ÜÑÿ */
    $"0049 FE00 0071 F1FF 0174 00FE 09F8 0AFC"            /* .Iþ..qñÿ.t.þÆø.ü */
    $"0BFF 0806 1B49 6977 7774 73FE 74FE 75FD"            /* .ÿ...Iiwwtsþtþuý */
    $"76FD 77FD 78FE 79FF 7AFE 7AFC 7BFA 7CFD"            /* výwýxþyÿzþzü{ú|ý */
    $"7D11 7E7F 7F80 8182 8383 8589 8C80 6F53"            /* }.~..oS */
    $"2511 1013 EC14 FB13 FC12 FA11 FB10 FE0F"            /* %...ì.û.ü.ú.û.þ. */
    $"010E 0AFD 0902 031B DCDF FFFF FF01 44F5"            /* ...ýÆ...Üßÿÿÿ.Dõ */
    $"FF04 C015 0000 7EF1 FF04 E120 0209 09F8"            /* ÿ.À...~ñÿ.á .ÆÆø */
    $"0AFA 0BFF 0812 133B 5F73 7877 7574 7475"            /* .ú.ÿ...;_sxwuttu */
    $"7576 7575 7677 7676 77FD 78FF 7901 7879"            /* uvuuvwvvwýxÿy.xy */
    $"FC7A FB7B FA7C 007D FD7C FF7D 0F7E 8185"            /* üzû{ú|.}ý|ÿ}.~ */
    $"836F 5027 130E 0F12 1312 1213 13FD 14F3"            /* oP'.........ý.ó */
    $"1402 1312 12FE 13FF 12FF 1100 12FA 11FB"            /* .....þ.ÿ.ÿ...ú.û */
    $"10FE 0F00 0DFC 0901 005F D0FF 04C0 1500"            /* .þ..ÂüÆ.._Ðÿ.À.. */
    $"007E F1FF 04E1 2002 0909 FD0A FC0A FA0B"            /* .~ñÿ.á .ÆÆý.ü.ú. */
    $"FF08 1213 3B5F 7378 7775 7474 7575 7675"            /* ÿ...;_sxwuttuuvu */
    $"7576 7776 7677 FD78 FF79 0178 79FC 7AFB"            /* uvwvvwýxÿy.xyüzû */
    $"7BFA 7C00 7DFD 7CFF 7D0F 7E81 8583 6F50"            /* {ú|.}ý|ÿ}.~oP */
    $"2713 0E0F 1213 1212 1313 EF14 0213 1212"            /* '.........ï..... */
    $"FE13 FF12 FF11 0012 FA11 FB10 FE0F 000D"            /* þ.ÿ.ÿ...ú.û.þ..Â */
    $"FC09 0100 5FD0 FF04 C015 0000 7EF1 FF04"            /* üÆ.._Ðÿ.À...~ñÿ. */
    $"E120 0209 09F8 0AFA 0BFF 0812 133B 5F73"            /* á .ÆÆø.ú.ÿ...;_s */
    $"7877 7574 7475 7576 7575 7677 7676 77FD"            /* xwuttuuvuuvwvvwý */
    $"78FF 7902 7879 7AFD 7AFB 7BFA 7C00 7DFD"            /* xÿy.xyzýzû{ú|.}ý */
    $"7CFF 7D0F 7E81 8583 6F50 2713 0E0F 1213"            /* |ÿ}.~oP'..... */
    $"1212 1313 EF14 0213 1212 FE13 FF12 FF11"            /* ....ï.....þ.ÿ.ÿ. */
    $"0012 FA11 FB10 FE0F 000D FC09 0100 60DE"            /* ..ú.û.þ..ÂüÆ..`Þ */
    $"FFFF FF00 EEF4 FF03 D87B 87EF F0FF 017F"            /* ÿÿÿ.îôÿ.Ø{ïðÿ.. */
    $"00FD 09FA 0AF8 0B08 0907 0E26 4963 767A"            /* .ýÆú.ø..Æ..&Icvz */
    $"77FD 75FD 76FD 77FC 78FB 79FB 7AFA 7BFD"            /* wýuývýwüxûyûzú{ý */
    $"7C0A 7D7E 8083 7960 3915 0D0E 11F9 12FD"            /* |.}~y`9.Â..ù.ý */
    $"13F2 13F9 12FC 11F9 10FC 0F00 0CFD 0902"            /* .ò.ù.ü.ù.ü...ýÆ. */
    $"0601 B4CF FF03 D87B 87EF F0FF 017F 00FD"            /* ..´Ïÿ.Ø{ïðÿ...ý */
    $"09FF 0AFC 0AF8 0B08 0907 0E26 4963 767A"            /* Æÿ.ü.ø..Æ..&Icvz */
    $"77FD 75FD 76FD 77FC 78FB 79FB 7AFA 7BFD"            /* wýuývýwüxûyûzú{ý */
    $"7C0A 7D7E 8083 7960 3915 0D0E 11F9 12EE"            /* |.}~y`9.Â..ù.î */
    $"13F9 12FC 11F9 10FC 0F00 0CFD 0902 0602"            /* .ù.ü.ù.ü...ýÆ... */
    $"B4CF FF03 D87B 87EF F0FF 017F 00FD 09FA"            /* ´Ïÿ.Ø{ïðÿ...ýÆú */
    $"0AF8 0B08 0907 0E26 4963 767A 77FD 75FD"            /* .ø..Æ..&Icvzwýuý */
    $"76FD 77FC 78FF 79FD 79FB 7AFA 7BFD 7C0A"            /* výwüxÿyýyûzú{ý|. */
    $"7D7E 8083 7960 3915 0D0E 11F9 12EE 13F9"            /* }~y`9.Â..ù.î.ù */
    $"12FC 11F9 10FC 0F00 0CFD 0902 0601 B5DE"            /* .ü.ù.ü...ýÆ...µÞ */
    $"FFFF FF00 E2DF FF02 EA28 01FE 09F8 0AF8"            /* ÿÿÿ.âßÿ.ê(.þÆø.ø */
    $"0B0E 0A08 0811 2F54 6570 7779 7877 7675"            /* ....../Tepwyxwvu */
    $"75FE 76FC 77FA 78FB 79FA 7A0D 7C7D 7F80"            /* uþvüwúxûyúzÂ|}. */
    $"7C72 604C 290F 0D0E 1010 F611 FF12 F012"            /* |r`L).Â...ö.ÿ.ð. */
    $"F911 F910 F90F 000B FE09 0308 004B FABA"            /* ù.ù.ù...þÆ...Kúº */
    $"FF02 EA28 01FE 09FF 0AFA 0AF8 0B0E 0A08"            /* ÿ.ê(.þÆÿ.ú.ø.... */
    $"0811 2F54 6570 7779 7877 7675 75FE 76FC"            /* ../Tepwyxwvuuþvü */
    $"77FA 78FB 79FA 7A0D 7C7D 7F80 7C72 604C"            /* wúxûyúzÂ|}.|r`L */
    $"290F 0D0E 1010 F611 EE12 F911 F910 F90F"            /* ).Â...ö.î.ù.ù.ù. */
    $"000B FE09 0308 004C FABA FF02 EA28 01FE"            /* ..þÆ...Lúºÿ.ê(.þ */
    $"09F8 0AF8 0B0E 0A08 0811 2F54 6570 7779"            /* Æø.ø....../Tepwy */
    $"7877 7675 75FE 76FC 77FE 78FD 78FB 79FA"            /* xwvuuþvüwþxýxûyú */
    $"7A0D 7C7D 7F80 7C72 604C 290F 0D0E 1010"            /* zÂ|}.|r`L).Â... */
    $"F611 EE12 F911 F910 F90F 000B FE09 0308"            /* ö.î.ù.ù.ù...þÆ.. */
    $"004A FADE FFFF FF00 E4DE FF04 A704 0709"            /* .JúÞÿÿÿ.äÞÿ.§..Æ */
    $"09F8 0AF7 0BFF 0C0C 0A08 0A12 1D30 4763"            /* Æø.÷.ÿ.......0Gc */
    $"7377 7A7A 78FE 77FE 76FC 77FA 78FF 79FD"            /* swzzxþwþvüwúxÿyý */
    $"7A0C 7C7D 7F7D 735F 442E 1B10 0A0C 0FF3"            /* z.|}.}s_D......ó */
    $"10FE 11EC 11F9 10F8 0FFF 0E01 0D0A FE09"            /* .þ.ì.ù.ø.ÿ..Â.þÆ */
    $"0205 19D0 B8FF 06A7 0407 0909 0A0A FA0A"            /* ...Ð¸ÿ.§..ÆÆ..ú. */
    $"F70B FF0C 0C0A 080A 121D 3047 6373 777A"            /* ÷.ÿ.......0Gcswz */
    $"7A78 FE77 FE76 FC77 FA78 FF79 FD7A 0C7C"            /* zxþwþvüwúxÿyýz.| */
    $"7D7F 7D73 5F44 2E1B 100A 0C0F F310 E911"            /* }.}s_D......ó.é. */
    $"F910 F80F FF0E 010D 09FE 0902 0519 D0B8"            /* ù.ø.ÿ..ÂÆþÆ...Ð¸ */
    $"FF04 A704 0709 09F8 0AF7 0BFF 0C0C 0A08"            /* ÿ.§..ÆÆø.÷.ÿ.... */
    $"0A12 1D30 4763 7377 7A7A 78FE 77FE 76FD"            /* ...0Gcswzzxþwþvý */
    $"7700 77FA 78FF 79FD 7A0C 7C7D 7F7D 735F"            /* w.wúxÿyýz.|}.}s_ */
    $"442E 1B10 0A0C 0FF3 10E9 11F9 10F8 0FFF"            /* D......ó.é.ù.ø.ÿ */
    $"0E00 0DFD 0902 0519 D0DD FFFF FF01 0CDD"            /* ..ÂýÆ...ÐÝÿÿÿ..Ý */
    $"FF03 5000 0909 F80A F70B FC0C 1B0B 0907"            /* ÿ.P.ÆÆø.÷.ü...Æ. */
    $"0812 1F2F 4259 6772 7679 7B7B 7A79 7A7A"            /* .../BYgrvy{{zyzz */
    $"7979 7A79 797A 7A7C 7CFE 7D0E 7C79 7568"            /* yyzyyzz||þ}.|yuh */
    $"5844 311E 110A 0A0D 0E0F 0FFC 10F8 0F00"            /* XD1....Â...ü.ø.. */
    $"10FE 11FB 11F6 10FD 11F9 10F8 0FFF 0E00"            /* .þ.û.ö.ý.ù.ø.ÿ.. */
    $"0CFE 0902 0800 80B6 FF05 5000 0909 0A0A"            /* .þÆ...¶ÿ.P.ÆÆ.. */
    $"FA0A F70B FC0C 1B0B 0907 0812 1F2F 4259"            /* ú.÷.ü...Æ..../BY */
    $"6772 7679 7B7B 7A79 7A7A 7979 7A79 797A"            /* grvy{{zyzzyyzyyz */
    $"7A7C 7CFE 7D0E 7C79 7568 5844 311E 110A"            /* z||þ}.|yuhXD1... */
    $"0A0D 0E0F 0FFC 10F8 0F00 10F8 11F6 10FD"            /* .Â...ü.ø...ø.ö.ý */
    $"11F9 10F8 0FFF 0E01 0C09 FF09 0208 0080"            /* .ù.ø.ÿ...ÆÿÆ... */
    $"B6FF 0350 0009 09F8 0AF7 0BFC 0C13 0B09"            /* ¶ÿ.P.ÆÆø.÷.ü...Æ */
    $"0708 121F 2F42 5967 7276 797B 7B7A 797A"            /* ..../BYgrvy{{zyz */
    $"7A79 0779 7A79 797A 7A7C 7CFE 7D0E 7C79"            /* zy.yzyyzz||þ}.|y */
    $"7568 5844 311E 110A 0A0D 0E0F 0FFC 10F8"            /* uhXD1....Â...ü.ø */
    $"0F00 10F8 11F6 10FD 11F9 10F8 0FFF 0E00"            /* ...ø.ö.ý.ù.ø.ÿ.. */
    $"0CFE 0902 0801 80DC FFFF FF00 F9DD FF04"            /* .þÆ...Üÿÿÿ.ùÝÿ. */
    $"B703 0709 09F8 0AF5 0BFB 0C23 0A08 0707"            /* ·..ÆÆø.õ.û.#.... */
    $"0C13 1F2A 3341 5160 6B66 666D 716E 7170"            /* ...*3AQ`kffmqnqp */
    $"6E67 5D55 5254 4334 2A20 160E 0909 0B0E"            /* ng]URTC4* ..ÆÆ.. */
    $"FB0F FE0E F60F FF10 FF0F FC0F F210 000F"            /* û.þ.ö.ÿ.ÿ.ü.ò... */
    $"FD10 F60F FE0E 010D 0AFE 0902 042B E2B6"            /* ý.ö.þ..Â.þÆ..+â¶ */
    $"FF05 B703 0709 090A F90A F50B FB0C 230A"            /* ÿ.·..ÆÆ.ù.õ.û.#. */
    $"0807 070C 131F 2A33 4151 606B 6666 6D71"            /* ......*3AQ`kffmq */
    $"6E71 706E 675D 5552 5443 342A 2016 0E09"            /* nqpng]URTC4* ..Æ */
    $"090B 0EFB 0FFE 0EF6 0FFF 10FA 0FF2 1000"            /* Æ..û.þ.ö.ÿ.ú.ò.. */
    $"0FFD 10F6 0FFE 0E02 0D0B 09FF 0902 042B"            /* .ý.ö.þ..Â.ÆÿÆ..+ */
    $"E2B6 FF04 B703 0709 09F8 0AF5 0BFB 0C0F"            /* â¶ÿ.·..ÆÆø.õ.û.. */
    $"0A08 0707 0C13 1F2A 3341 5160 6B66 666D"            /* .......*3AQ`kffm */
    $"1371 6E71 706E 675D 5552 5443 342A 2016"            /* .qnqpng]URTC4* . */
    $"0E09 090B 0EFB 0FFE 0EF6 0FFF 10FA 0FF2"            /* .ÆÆ..û.þ.ö.ÿ.ú.ò */
    $"1000 0FFD 10F6 0FFE 0E01 0D0A FE09 0204"            /* ...ý.ö.þ..Â.þÆ.. */
    $"2BE2 DCFF FFFF 00BC DCFF 0166 00FE 09F8"            /* +âÜÿÿÿ.¼Üÿ.f.þÆø */
    $"0AF5 0BF8 0C1B 0B0A 0907 0708 0B10 1412"            /* .õ.ø....Æ....... */
    $"151B 1F1B 1D1D 1A17 110D 0C0D 0908 090B"            /* .........Â.ÂÆ.Æ. */
    $"0C0D F40E F20F FC0F F210 F50F FA0E 060D"            /* .Âô.ò.ü.ò.õ.ú..Â */
    $"0A09 0907 09A7 B4FF 0166 00FE 09F8 0AF5"            /* .ÆÆ.Æ§´ÿ.f.þÆø.õ */
    $"0BF8 0C1B 0B0A 0907 0708 0B10 1412 151B"            /* .ø....Æ......... */
    $"1F1B 1D1D 1A17 110D 0C0D 0908 090B 0C0D"            /* .......Â.ÂÆ.Æ..Â */
    $"F40E ED0F F210 F50F FA0E 020D 0909 0309"            /* ô.í.ò.õ.ú..ÂÆÆ.Æ */
    $"0708 A6B4 FF01 6600 FE09 F80A F50B F80C"            /* ..¦´ÿ.f.þÆø.õ.ø. */
    $"0B0B 0A09 0707 080B 1014 1215 1B0F 1F1B"            /* ...Æ............ */
    $"1D1D 1A17 110D 0C0D 0908 090B 0C0D F40E"            /* .....Â.ÂÆ.Æ..Âô. */
    $"ED0F F210 F50F FA0E 060D 0A09 0907 09A6"            /* í.ò.õ.ú..Â.ÆÆ.Æ¦ */
    $"DBFF FFFF 007E DCFF 04E4 3000 0909 F70A"            /* Ûÿÿÿ.~Üÿ.ä0.ÆÆ÷. */
    $"F40B F30C 000B F80A 000B FD0C FA0D E60E"            /* ô.ó...ø...ý.úÂæ. */
    $"FF0E E70F F70E 070D 0C09 0908 0163 FBB4"            /* ÿ.ç.÷..Â.ÆÆ..cû´ */
    $"FF04 E430 0009 09F7 0AF4 0BF3 0C00 0BF8"            /* ÿ.ä0.ÆÆ÷.ô.ó...ø */
    $"0A00 0BFD 0CFA 0DE4 0EE7 0FF7 0E03 0D0C"            /* ...ý.úÂä.ç.÷..Â. */
    $"0909 0308 0163 FBB4 FF04 E430 0009 09F7"            /* ÆÆ...cû´ÿ.ä0.ÆÆ÷ */
    $"0AF4 0BF3 0C00 0BFD 0AFC 0A00 0BFD 0CFA"            /* .ô.ó...ý.ü...ý.ú */
    $"0DE4 0EE7 0FF7 0E07 0D0C 0909 0801 63FB"            /* Âä.ç.÷..Â.ÆÆ..cû */
    $"DBFF FFFF 0067 DBFF 04C0 0B05 0909 F60A"            /* Ûÿÿÿ.gÛÿ.À..ÆÆö. */
    $"F20B ED0C EA0D F10E F20E FF0F EE0E FE0D"            /* ò.í.êÂñ.ò.ÿ.î.þÂ */
    $"050B 0909 0227 DDB2 FF03 C00B 0509 0009"            /* ..ÆÆ.'Ý²ÿ.À..Æ.Æ */
    $"F60A F20B ED0C EA0D E20E FF0F EE0E FE0D"            /* ö.ò.í.êÂâ.ÿ.î.þÂ */
    $"020B 0909 0202 27DD B2FF 04C0 0B05 0909"            /* ..ÆÆ..'Ý²ÿ.À..ÆÆ */
    $"F60A F20B F20C FC0C EA0D E20E FF0F EE0E"            /* ö.ò.ò.ü.êÂâ.ÿ.î. */
    $"FE0D 050B 0909 0228 DDDA FFFF FF00 6FDA"            /* þÂ..ÆÆ.(ÝÚÿÿÿ.oÚ */
    $"FF04 8300 0809 09F7 0AF2 0BED 0CEA 0DF1"            /* ÿ...ÆÆ÷.ò.í.êÂñ */
    $"0EFD 0EFF 0DF8 0EFF 0FEE 0EFE 0D04 0B09"            /* .ý.ÿÂø.ÿ.î.þÂ..Æ */
    $"0703 A6B0 FF02 8300 08FF 09F7 0AF2 0BED"            /* ..¦°ÿ...ÿÆ÷.ò.í */
    $"0CEA 0DED 0EFF 0DF8 0EFF 0FEE 0EFE 0D02"            /* .êÂí.ÿÂø.ÿ.î.þÂ. */
    $"0B09 0701 03A6 B0FF 0483 0008 0909 F70A"            /* .Æ...¦°ÿ...ÆÆ÷. */
    $"F20B F20C FC0C EA0D ED0E FF0D F80E FF0F"            /* ò.ò.ü.êÂí.ÿÂø.ÿ. */
    $"EE0E FE0D 040B 0907 03A6 D9FF FFFF 0066"            /* î.þÂ..Æ..¦Ùÿÿÿ.f */
    $"DAFF 04F3 3E00 0909 F60A F00B E80C E20D"            /* Úÿ.ó>.ÆÆö.ð.è.âÂ */
    $"000D FD0E 000D E70E FB0D 050B 0909 0043"            /* .Âý..Âç.ûÂ..ÆÆ.C */
    $"FAB0 FF02 F33E 00FF 09F6 0AF0 0BE8 0CE1"            /* ú°ÿ.ó>.ÿÆö.ð.è.á */
    $"0DFD 0E00 0DE7 0EFB 0D03 0B09 0900 0143"            /* Âý..Âç.ûÂ..ÆÆ..C */
    $"FAB0 FF04 F33E 0009 09F6 0AF0 0BF5 0CF4"            /* ú°ÿ.ó>.ÆÆö.ð.õ.ô */
    $"0CE1 0DFD 0E00 0DE7 0EFB 0D05 0B09 0900"            /* .áÂý..Âç.ûÂ..ÆÆ. */
    $"42FA D9FF FFFF 005B D9FF 04D4 1A02 0909"            /* BúÙÿÿÿ.[Ùÿ.Ô..ÆÆ */
    $"F70A EC0B E30C EB0D EF0D FC0E F30D 050C"            /* ÷.ì.ã.ëÂïÂü.óÂ.. */
    $"0A09 0218 C9AE FF01 D41A 0202 0909 F70A"            /* .Æ..É®ÿ.Ô...ÆÆ÷. */
    $"EC0B E30C D90D FC0E F30D 040C 0A09 0318"            /* ì.ã.ÙÂü.óÂ...Æ.. */
    $"00C9 AEFF 04D4 1A02 0909 F70A EC0B F90C"            /* .É®ÿ.Ô..ÆÆ÷.ì.ù. */
    $"EB0C D90D FC0E F30D 050C 0A09 0218 C9D8"            /* ë.ÙÂü.óÂ...Æ..ÉØ */
    $"FFFF FF00 51D8 FF04 AB04 0609 09F6 0AE9"            /* ÿÿÿ.QØÿ.«..ÆÆö.é */
    $"0BE0 0CF3 0DDE 0DFF 0C04 0A09 0605 9BAC"            /* .à.óÂÞÂÿ...Æ..¬ */
    $"FF00 AB03 0406 0909 F60A E90B E00C D00D"            /* ÿ.«...ÆÆö.é.à.ÐÂ */
    $"FF0C 040A 0906 059B ACFF 04AB 0406 0909"            /* ÿ...Æ..¬ÿ.«..ÆÆ */
    $"F60A E90B FE0C E30C D00D FF0C 040A 0906"            /* ö.é.þ.ã.ÐÂÿ...Æ. */
    $"059B D7FF FFFF 004B D7FF 036D 0009 09F5"            /* .×ÿÿÿ.K×ÿ.m.ÆÆõ */
    $"0AEA 0BDF 0CF4 0DDF 0DFE 0C03 0A08 0081"            /* .ê.ß.ôÂßÂþ..... */
    $"AAFF 036D 0009 09F5 0AEA 0BDF 0CD2 0DFE"            /* ªÿ.m.ÆÆõ.ê.ß.ÒÂþ */
    $"0C04 0A08 0081 FFAB FF03 6D00 0909 F50A"            /* .....ÿ«ÿ.m.ÆÆõ. */
    $"EA0B FE0C E20C D20D FE0C 030A 0800 81D6"            /* ê.þ.â.ÒÂþ.....Ö */
    $"FFFF FF00 5AD7 FF03 F74F 0009 F40A E40B"            /* ÿÿÿ.Z×ÿ.÷O.Æô.ä. */
    $"DB0C FF0D F90D FA0C F00D FD0C 040B 0900"            /* Û.ÿÂùÂú.ðÂý...Æ. */
    $"59FD AAFF 03F7 4F00 09F4 0AE4 0BDB 0CF7"            /* Yýªÿ.÷O.Æô.ä.Û.÷ */
    $"0DFA 0CF0 0DFD 0C05 0B09 005A FDFF ABFF"            /* Âú.ðÂý...Æ.Zýÿ«ÿ */
    $"03F7 4F00 09F4 0AE8 0BFD 0BDB 0CF7 0DFA"            /* .÷O.Æô.è.ý.Û.÷Âú */
    $"0CF0 0DFD 0C04 0B09 0059 FDD6 FFFF FF00"            /* .ðÂý...Æ.YýÖÿÿÿ. */
    $"44D6 FF03 E837 0009 F40A DC0B E20C DE0C"            /* DÖÿ.è7.Æô.Ü.â.Þ. */
    $"040B 0900 39EA A9FF 04FF E837 0009 F40A"            /* ..Æ.9ê©ÿ.ÿè7.Æô. */
    $"DC0B BF0C 060B 0900 3AEA FFFF AAFF 03E8"            /* Ü.¿...Æ.:êÿÿªÿ.è */
    $"3700 09F4 0AE9 0BF4 0BBF 0C04 0B09 0038"            /* 7.Æô.é.ô.¿...Æ.8 */
    $"EAD5 FFFF FF00 48D5 FF03 D320 0009 F40A"            /* êÕÿÿÿ.HÕÿ.Ó .Æô. */
    $"D60B E90C E00C FF0B 030A 0129 D5A8 FFFF"            /* Ö.é.à.ÿ....)Õ¨ÿÿ */
    $"FF03 D320 0009 F40A D60B C80C FF0B 030A"            /* ÿ.Ó .Æô.Ö.È.ÿ... */
    $"0027 D5FE FFA9 FF03 D320 0009 F40A EA0B"            /* .'Õþÿ©ÿ.Ó .Æô.ê. */
    $"ED0B C80C FF0B 030A 0128 D5D4 FFFF FF00"            /* í.È.ÿ....(ÕÔÿÿÿ. */
    $"42D4 FF02 C714 01F3 0AD7 0BE9 0CE0 0CFF"            /* BÔÿ.Ç..ó.×.é.à.ÿ */
    $"0B02 0501 A7A7 FFFE FF02 C714 01F3 0AD7"            /* ....§§ÿþÿ.Ç..ó.× */
    $"0BC8 0CFF 0B02 0501 A7FD FFA8 FF02 C714"            /* .È.ÿ....§ýÿ¨ÿ.Ç. */
    $"01F3 0AEB 0BED 0BC8 0CFF 0B02 0501 A7D3"            /* .ó.ë.í.È.ÿ....§Ó */
    $"FFFF FF00 51D3 FF03 BD1C 0109 F30A D00B"            /* ÿÿÿ.QÓÿ.½..Æó.Ð. */
    $"F20C F00C FF0B F60C FD0B 0205 0691 A6FF"            /* ò.ð.ÿ.ö.ý....¦ÿ */
    $"FDFF 03BD 1C01 09F3 0AD0 0BE1 0CFF 0BF6"            /* ýÿ.½..Æó.Ð.á.ÿ.ö */
    $"0CFD 0B02 0506 91FC FFA7 FF03 BD1C 0109"            /* .ý....üÿ§ÿ.½..Æ */
    $"F30A ED0B E40B E10C FF0B F60C FD0B 0205"            /* ó.í.ä.á.ÿ.ö.ý... */
    $"0691 D2FF FFFF 0042 D2FF 02AD 0703 F00A"            /* .Òÿÿÿ.BÒÿ.­..ð. */
    $"C80B FD0C F10C F00B 0206 0394 A5FF FCFF"            /* È.ý.ñ.ð....¥ÿüÿ */
    $"02AD 0703 F00A C80B ED0C F00B 0206 0394"            /* .­..ð.È.í.ð.... */
    $"FBFF A6FF 02AD 0703 F00A F00B D90B ED0C"            /* ûÿ¦ÿ.­..ð.ð.Ù.í. */
    $"F00B 0206 0394 D1FF FFFF 0042 D1FF 02A2"            /* ð....Ñÿÿÿ.BÑÿ.¢ */
    $"0A03 EF0A C60B FC0B FB0C EC0B 0207 0089"            /* ..ï.Æ.ü.û.ì.... */
    $"A4FF FBFF 02A2 0A03 EF0A C10B FB0C EC0B"            /* ¤ÿûÿ.¢..ï.Á.û.ì. */
    $"0207 0089 FAFF A5FF 02A2 0A03 EF0A F20B"            /* ...úÿ¥ÿ.¢..ï.ò. */
    $"D00B FB0C EC0B 0207 0089 D0FF FFFF 003C"            /* Ð.û.ì....Ðÿÿÿ.< */
    $"D0FF 02A7 0902 ED0A C90B E40B FF0A 0207"            /* Ðÿ.§Æ.í.É.ä.ÿ... */
    $"0077 A3FF FAFF 02A7 0902 ED0A AC0B FF0A"            /* .w£ÿúÿ.§Æ.í.¬.ÿ. */
    $"0207 0077 F9FF A4FF 02A7 0902 ED0A F50B"            /* ...wùÿ¤ÿ.§Æ.í.õ. */
    $"B80B FF0A 0207 0078 CFFF FFFF 0039 CFFF"            /* ¸.ÿ....xÏÿÿÿ.9Ïÿ */
    $"02A7 0C01 EE0A C90B E40B 030A 0600 78A2"            /* .§..î.É.ä.....x¢ */
    $"FFF9 FF02 A70C 01EE 0AAC 0B03 0A06 0078"            /* ÿùÿ.§..î.¬.....x */
    $"F8FF A3FF 02A7 0C01 EE0A F50B B80B 030A"            /* øÿ£ÿ.§..î.õ.¸... */
    $"0600 78CE FFFF FF00 3CCE FF02 CB23 00EB"            /* ..xÎÿÿÿ.<Îÿ.Ë#.ë */
    $"0ACD 0BE6 0BFF 0A02 0503 8FA1 FFF8 FF02"            /* .Í.æ.ÿ....¡ÿøÿ. */
    $"CB23 00EB 0AB2 0BFF 0A02 0503 8FF7 FFA2"            /* Ë#.ë.².ÿ....÷ÿ¢ */
    $"FF02 CB23 00EB 0AF9 0BBA 0BFF 0A02 0503"            /* ÿ.Ë#.ë.ù.º.ÿ.... */
    $"8FCD FFFF FF00 3ACD FF02 D41D 00E4 0AD5"            /* Íÿÿÿ.:Íÿ.Ô..ä.Õ */
    $"0BEA 0BFC 0A02 0409 97A0 FFF7 FF02 D41D"            /* .ê.ü...Æ ÿ÷ÿ.Ô. */
    $"00E4 0ABE 0BFC 0A02 0409 97F6 FFA1 FF02"            /* .ä.¾.ü...Æöÿ¡ÿ. */
    $"D41D 00E4 0ABE 0BFC 0A02 0409 97CC FFFF"            /* Ô..ä.¾.ü...ÆÌÿÿ */
    $"FF00 3FCC FF03 CC2C 0009 DC0A DF0B EB0B"            /* ÿ.?Ìÿ.Ì,.ÆÜ.ß.ë. */
    $"FC0A 0201 0EA8 9FFF F6FF 03CC 2C00 09DC"            /* ü....¨ÿöÿ.Ì,.ÆÜ */
    $"0AC9 0BFC 0A02 010E A8F5 FFA0 FF03 CC2C"            /* .É.ü....¨õÿ ÿ.Ì, */
    $"0009 E60A F70A C90B FC0A 0201 0EA8 CBFF"            /* .Ææ.÷.É.ü....¨Ëÿ */
    $"FFFF 003F CBFF 03DD 3E00 09DD 0ADF 0BEC"            /* ÿÿ.?Ëÿ.Ý>.ÆÝ.ß.ì */
    $"0BFC 0A02 001F BC9E FFF5 FF03 DD3E 0009"            /* .ü....¼ÿõÿ.Ý>.Æ */
    $"DD0A CA0B FC0A 0200 1FBC F4FF 9FFF 03DD"            /* Ý.Ê.ü....¼ôÿÿ.Ý */
    $"3E00 09E7 0AF7 0ACA 0BFC 0A02 001F BCCA"            /* >.Æç.÷.Ê.ü....¼Ê */
    $"FFFF FF00 42CA FF03 F25C 0006 D20A EB0B"            /* ÿÿÿ.BÊÿ.ò\..Ò.ë. */
    $"EC0B FE0A 0309 002C D29D FFF4 FF03 F25C"            /* ì.þ..Æ.,Òÿôÿ.ò\ */
    $"0006 D20A D60B FE0A 0309 002C D2F3 FF9E"            /* ..Ò.Ö.þ..Æ.,Òóÿ */
    $"FF03 F25C 0006 E80A EB0A D60B FE0A 0309"            /* ÿ.ò\..è.ë.Ö.þ..Æ */
    $"002C D2C9 FFFF FF00 42C9 FF03 FA87 0901"            /* .,ÒÉÿÿÿ.BÉÿ.úÆ. */
    $"CC0A F20B ED0B FE0A 0307 004C D89C FFF3"            /* Ì.ò.í.þ....LØÿó */
    $"FF03 FA87 0901 CC0A DE0B FE0A 0307 004C"            /* ÿ.úÆ.Ì.Þ.þ....L */
    $"D8F2 FF9D FF03 FA87 0901 E90A E40A DE0B"            /* Øòÿÿ.úÆ.é.ä.Þ. */
    $"FE0A 0307 004C D8C8 FFFF FF00 3FC7 FF02"            /* þ....LØÈÿÿÿ.?Çÿ. */
    $"B41F 00C6 0AF9 0BEE 0BFE 0A03 0305 71F8"            /* ´..Æ.ù.î.þ....qø */
    $"9BFF F1FF 02B4 1F00 C60A E60B FE0A 0303"            /* ÿñÿ.´..Æ.æ.þ... */
    $"0571 F8F1 FF9B FF02 B41F 00EA 0ADD 0AE6"            /* .qøñÿÿ.´..ê.Ý.æ */
    $"0BFE 0A03 0305 71F8 C7FF FFFF 004A C6FF"            /* .þ....qøÇÿÿÿ.JÆÿ */
    $"03DA 4000 08C3 0AFE 0B01 0B0A FD09 FF0A"            /* .Ú@..Ã.þ....ýÆÿ. */
    $"F60B FF0A 0201 17A6 99FF F0FF 03DA 4000"            /* ö.ÿ....¦ÿðÿ.Ú@. */
    $"08C3 0AFC 0BFB 0AF6 0BFF 0A02 0117 A6EF"            /* .Ã.ü.û.ö.ÿ....¦ï */
    $"FF9A FF03 DA40 0008 EC0A D80A EB0B FF0A"            /* ÿÿ.Ú@..ì.Ø.ë.ÿ. */
    $"0201 17A6 C5FF FFFF 0075 C5FF 03F4 6C06"            /* ...¦Åÿÿÿ.uÅÿ.ôl. */
    $"04FA 0A00 09FD 08FF 0701 0809 D20A 0009"            /* .ú..Æý.ÿ...ÆÒ..Æ */
    $"020A 0E12 FE13 0411 0E0A 0809 F90B 0307"            /* ....þ......Æù... */
    $"0025 CC98 FFEF FF03 F46C 0604 FA0A 0109"            /* .%Ìÿïÿ.ôl..ú..Æ */
    $"08FE 09FE 08D1 0A0B 090A 0D10 1211 1010"            /* .þÆþ.Ñ..Æ.Â..... */
    $"0D0A 090A F90B 0307 0025 CCEE FF99 FF03"            /* Â.Æ.ù....%Ìîÿÿ. */
    $"F46C 0604 F50A 0009 FA0A D50A 060B 0C0C"            /* ôl..õ..Æú.Õ..... */
    $"0D0C 0D0C F50B 0307 0025 CCC4 FFFF FF00"            /* Â.Â.õ....%ÌÄÿÿÿ. */
    $"BBC3 FF03 A811 0008 FE0B FF0A 0A14 232D"            /* »Ãÿ.¨...þ.ÿ...#- */
    $"302E 271F 150C 0808 ED0A 050B 0702 0204"            /* 0.'.....í....... */
    $"08F0 0A02 080A 1C02 303F 4AFE 4D0F 4B43"            /* .ð......0?JþM.KC */
    $"3421 130B 090A 0B0B 0C09 0100 46E2 97FF"            /* 4!..Æ....Æ..Fâÿ */
    $"EDFF 03A8 1100 08FE 0B0C 0A0B 121D 2425"            /* íÿ.¨...þ......$% */
    $"2420 1913 0C08 08ED 0A05 0B07 0202 0408"            /* $ .....í........ */
    $"F00A 1809 0B17 2731 393B 3C3B 3833 281C"            /* ð..Æ..'19;<;83(. */
    $"110B 0A0A 0B0B 0C09 0100 46E2 EDFF 97FF"            /* .......Æ..Fâíÿÿ */
    $"03A8 1100 08FE 0BFF 0A09 0D0E 0F11 100F"            /* .¨...þ.ÿ.ÆÂ..... */
    $"0E0C 0A09 FE0A EF0A 050B 0702 0204 08EE"            /* ...Æþ.ï........î */
    $"0A03 0D11 1415 FE16 0515 1412 0F0D 0CFD"            /* ..Â...þ......Â.ý */
    $"0B05 0C09 0100 46E2 C3FF FFFF 00D4 C2FF"            /* ...Æ..FâÃÿÿÿ.ÔÂÿ */
    $"14C0 3602 030B 0B0C 2547 585C 5F60 5F5B"            /* .À6.....%GX\_`_[ */
    $"513F 2916 0C0A FC0C F80D FE0C 0808 0002"            /* Q?)...ü.øÂþ..... */
    $"101C 1304 0008 F30B 030A 1536 5004 5B5F"            /* ......ó....6P.[_ */
    $"6266 6BFE 6E0C 6B61 4E33 1B0D 090A 0800"            /* bfkþn.kaN3.ÂÆ... */
    $"1681 FA96 FFEC FF03 C036 0203 FE0B 0E1F"            /* .úÿìÿ.À6..þ... */
    $"3742 4647 4848 463E 3120 130C 0B0B FD0C"            /* 7BFGHHF>1 ....ý. */
    $"F80D FE0C 0808 0002 101C 1304 0008 F30B"            /* øÂþ...........ó. */
    $"180A 122A 3C44 4749 4C50 5354 5250 483B"            /* ...*<DGILPSTRPH; */
    $"2716 0D0A 0B08 0016 81FA ECFF 96FF 03C0"            /* '.Â.....úìÿÿ.À */
    $"3602 03FE 0B04 0F14 1618 18FE 1905 1613"            /* 6..þ.......þ.... */
    $"0F0D 0C0C FC0C F80D FE0C 0808 0002 101C"            /* .Â..ü.øÂþ....... */
    $"1304 0008 F30B 070C 0D12 1517 1819 1BFC"            /* ....ó...Â......ü */
    $"1C0B 1917 120F 0C0B 0B09 0016 81FA C2FF"            /* .........Æ..úÂÿ */
    $"FFFF 00DA C1FF 15FA A61E 0008 2A54 5C5C"            /* ÿÿ.ÚÁÿ.ú¦...*T\\ */
    $"5E60 6162 6362 615D 513B 200D 0CFE 0DF8"            /* ^`abcba]Q; Â.þÂø */
    $"0E0C 0D0C 0900 40B8 E6F1 E6BF 4D00 05FE"            /* ..Â.Æ.@¸æñæ¿M..þ */
    $"0BF8 0C04 0B1C 475B 6012 6C7A 8A9A A8B4"            /* .ø....G[`.lz¨´ */
    $"BCBF BEBA B09A 7E57 2C0E 005E EB94 FFEB"            /* ¼¿¾º°~W,..^ëÿë */
    $"FF0B FAA6 1E00 0922 4045 4547 4849 FD4A"            /* ÿ.ú¦..Æ"@EEGHIýJ */
    $"0545 3D2E 1A0D 0CFE 0DF8 0E0C 0D0C 0900"            /* .E=..Â.þÂø..Â.Æ. */
    $"40B8 E6F1 E6BF 4D00 05FE 0BF8 0C17 0B18"            /* @¸æñæ¿M..þ.ø.... */
    $"3644 4851 5C68 747E 878D 908F 8B84 745E"            /* 6DHQ\ht~t^ */
    $"4224 0E00 5DEC EAFF 95FF 06FA A61E 000A"            /* B$..]ìêÿÿ.ú¦... */
    $"1016 FE17 FD19 FE18 0217 130F FC0D F80E"            /* ..þ.ý.þ.....üÂø. */
    $"0C0D 0C09 0040 B8E6 F1E6 BF4D 0005 FE0B"            /* .Â.Æ.@¸æñæ¿M..þ. */
    $"F70C 090F 1517 191B 1F24 292C 2FFE 3109"            /* ÷.Æ......$),/þ1Æ */
    $"302D 2821 1A12 0C00 5BEC C0FF FFFF 00DC"            /* 0-(!....[ìÀÿÿÿ.Ü */
    $"BFFF 08E3 561B 535B 5B5D 5F60 FE61 FF60"            /* ¿ÿ.ãV.S[[]_`þaÿ` */
    $"FF5E 055D 5336 140B 0DF7 0E04 0C06 017F"            /* ÿ^.]S6..Â÷...... */
    $"FBFC FF06 FBAD 2000 0A0B 0BFB 0C06 0D0B"            /* ûüÿ.û­ ....û..Â. */
    $"1846 5D6A 7E11 98B0 C4D4 E1EB F2F5 F7F7"            /* .F]j~.°ÄÔáëòõ÷÷ */
    $"F5EC DEC6 9F66 3C92 93FF E9FF 0CE3 5716"            /* õìÞÆf<ÿéÿ.ãW. */
    $"3E44 4446 4849 4A49 4948 FE47 0546 3E2A"            /* >DDFHIJIIHþG.F>* */
    $"120C 0DF7 0E04 0C06 017F FBFC FF06 FBAD"            /* ..Â÷......ûüÿ.û­ */
    $"2000 0A0B 0BF9 0C16 1535 464F 5F72 8495"            /*  ....ù...5FO_r */
    $"A1A9 B1B6 B8BA BAB8 B1A7 9678 4E2C 87E9"            /* ¡©±¶¸ºº¸±§xN,é */
    $"FF93 FF0B E359 0B15 1617 1719 191A 1A19"            /* ÿÿ.ãY.......... */
    $"FD18 0117 1603 130E 0D0D F70E 040C 0601"            /* ý.......ÂÂ÷..... */
    $"7FFB FCFF 06FB AD20 000A 0B0B FB0C FF0D"            /* .ûüÿ.û­ ....û.ÿÂ */
    $"0B0E 1417 1A21 282F 3438 3C3D 3EFE 4007"            /* .....!(/48<=>þ@. */
    $"3F3D 3933 2A1D 0B70 BFFF FFFF 00E5 BEFF"            /* ?=93*..p¿ÿÿÿ.å¾ÿ */
    $"16E7 6156 5A5D 5E60 6162 6261 6060 5E5D"            /* .çaVZ]^`abba``^] */
    $"5C5C 5942 1D0C 0E0E FC0F 060E 0D0A 0014"            /* \\YB....ü...Â... */
    $"A1FE F9FF 04DD 4C00 050A FD0C FF0D 060C"            /* ¡þùÿ.ÝL...ý.ÿÂ.. */
    $"123C 5F74 8FAA 06C3 D4E3 EDF5 FAFE FEFF"            /* .<_tª.ÃÔãíõúþþÿ */
    $"08FE FDFA F3E8 D0A9 93E4 94FF E8FF 16E6"            /* .þýúóèÐ©äÿèÿ.æ */
    $"4F3F 4445 4748 4A4B 4949 4848 4646 4545"            /* O?DEGHJKIIHHFFEE */
    $"4432 180D 0E0E FC0F 060E 0D0A 0014 A1FE"            /* D2.Â..ü...Â...¡þ */
    $"F9FF 04DD 4C00 050A FD0C FF0D 0E0C 102E"            /* ùÿ.ÝL...ý.ÿÂ.... */
    $"4757 6C80 93A0 ACB4 B9BD BEBF FEC0 07BE"            /* GWl ¬´¹½¾¿þÀ.¾ */
    $"BCB8 AF9D 7F77 DFEA FF92 FF02 E42D 11FE"            /* ¼¸¯.wßêÿÿ.ä-.þ */
    $"1700 19FE 1AFE 19FF 18FF 1702 1714 0FFE"            /* ...þ.þ.ÿ.ÿ.....þ */
    $"0EFC 0F06 0E0D 0A00 14A1 FEF9 FF04 DD4C"            /* .ü...Â...¡þùÿ.ÝL */
    $"0005 0AFD 0CFE 0D0B 0E13 181D 252D 3438"            /* ...ý.þÂ.....%-48 */
    $"3C3E 3F40 FC41 FF40 053F 3B35 293D D6C0"            /* <>?@üAÿ@.?;5)=ÖÀ */
    $"FFFF FF00 E3BF FF17 FE8F 5358 5B5D 5E60"            /* ÿÿÿ.ã¿ÿ.þSX[]^` */
    $"6162 6261 6060 5E5D 5B5A 5959 4820 0E0F"            /* abba``^][ZYYH .. */
    $"FD10 050E 0800 0354 D5F6 FF10 F38F 1900"            /* ý......TÕöÿ.ó.. */
    $"0007 0C0D 0E0D 0B30 627C 98AF C206 D4DF"            /* ...Â.Â.0b|¯Â.Ôß */
    $"E9F2 F7FB FDFE FE08 FDFC FAF6 F1EC E4D2"            /* éò÷ûýþþ.ýüúöñìäÒ */
    $"E394 FFE9 FF07 FE81 3C42 4546 4749 FE4A"            /* ãÿéÿ.þ<BEFGIþJ */
    $"0C49 4848 4646 4544 4342 371B 0F0F FD10"            /* .IHHFFEDCB7...ý. */
    $"050E 0800 0354 D5F6 FF17 F38F 1900 0007"            /* .....TÕöÿ.ó.... */
    $"0C0D 0E0D 0C26 4A5D 7284 929F A8B0 B6BB"            /* .Â.Â.&J]r¨°¶» */
    $"BDBD FDBF 07BE BBB9 B6B2 AB9E CCEA FF93"            /* ½½ý¿.¾»¹¶²«Ìêÿ */
    $"FF06 FE64 0E16 1718 18FD 1AFE 19FF 18FF"            /* ÿ.þd.....ý.þ.ÿ.ÿ */
    $"1703 1716 1411 FB10 050E 0800 0354 D5F6"            /* ......û......TÕö */
    $"FF07 F38F 1900 0007 0C0D FE0E 0B12 1920"            /* ÿ.ó.....Âþ....  */
    $"272D 3237 3A3D 3E3F 40FC 4107 403F 3E3C"            /* '-27:=>?@üA.@?>< */
    $"3C3A 369F C0FF FFFF 00DE C0FF 07F5 9450"            /* <:6Àÿÿÿ.ÞÀÿ.õP */
    $"585B 5C5D 5FFC 6114 605F 5E5D 5B5A 5856"            /* X[\]_üa.`_^][ZXV */
    $"554B 3016 0E0B 0500 0423 68B5 F9F3 FF0E"            /* UK0......#hµùóÿ. */
    $"E193 531E 0100 0406 2C69 8798 AABB CA06"            /* áS.....,iª»Ê. */
    $"D7E2 EBF3 F8FB FCFE FD09 FCFB F8F4 F0F0"            /* ×âëóøûüþýÆüûøôðð */
    $"EFE9 E3FC 95FF EAFF 07F3 863A 4244 4546"            /* ïéãüÿêÿ.ó:BDEF */
    $"48FC 49FF 48FF 4610 4543 4241 403A 2614"            /* HüIÿHÿF.ECBA@:&. */
    $"0E0C 0500 0423 68B5 F9F3 FF14 E193 531E"            /* .....#hµùóÿ.áS. */
    $"0100 0408 244F 6572 808D 98A3 AAB1 B7BB"            /* ....$Oer£ª±·» */
    $"BDFC BE08 BDBB B8B5 B4B4 ADB7 FBEB FF94"            /* ½ü¾.½»¸µ´´­·ûëÿ */
    $"FF07 F16B 0D15 1717 1818 FE1A FD19 FF18"            /* ÿ.ñkÂ.....þ.ý.ÿ. */
    $"FF17 0017 FE15 0A14 1110 0D05 0004 2368"            /* ÿ...þ.....Â...#h */
    $"B5F9 F3FF 13E1 9353 1E01 0004 0B12 1C23"            /* µùóÿ.áS.......# */
    $"272C 3034 383A 3D3E 3FFA 4001 3F3E FE3D"            /* ',048:=>?ú@.?>þ= */
    $"0236 61F7 C1FF FFFF 00C5 C1FF 08F6 854B"            /* .6a÷Áÿÿÿ.ÅÁÿ.öK */
    $"5658 5A5C 5D5E FB60 105F 5D5C 5A58 5755"            /* VXZ\]^û`._]\ZXWU */
    $"5456 5540 1E1E 4261 A0F0 EDFF 0BE9 9364"            /* TVU@..Ba ðíÿ.éd */
    $"4238 7F94 97A0 B0C1 CE04 DBE4 EDF5 F9FC"            /* B8. °ÁÎ.Ûäíõùü */
    $"FB09 FAF8 F6F3 F0F0 EFEC E0ED 95FF EBFF"            /* ûÆúøöóððïìàíÿëÿ */
    $"08F4 7634 4143 4445 4647 FA48 0446 4544"            /* .ôv4ACDEFGúH.FED */
    $"4241 FD40 0631 181C 4261 A0F0 EDFF 10E9"            /* BAý@.1..Ba ðíÿ.é */
    $"9264 452D 6070 7178 8491 9CA5 ACB3 B8BB"            /* dE-`pqx¥¬³¸» */
    $"FCBD 09BC BBB9 B7B4 B5B4 B1A6 DCEB FF95"            /* ü½Æ¼»¹·´µ´±¦Üëÿ */
    $"FF03 F256 0515 FE17 0018 FA19 FF18 FE17"            /* ÿ.òV..þ...ú.ÿ.þ. */
    $"FF16 FF15 0716 140E 1B43 61A0 F0ED FF10"            /* ÿ.ÿ......Ca ðíÿ. */
    $"E992 6549 1720 2626 292D 3135 393B 3D3F"            /* éeI. &&)-159;=? */
    $"3FFE 40FC 3FFD 3D02 3B33 B8C1 FFFF FF00"            /* ?þ@ü?ý=.;3¸Áÿÿÿ. */
    $"BAC2 FF02 E57C 4FFE 5803 5A5C 5D5D FE5F"            /* ºÂÿ.å|OþX.Z\]]þ_ */
    $"FE60 075F 5D5C 5958 5655 55FE 5601 467B"            /* þ`._]\YXVUUþV.F{ */
    $"E7FF 09FC C59D A198 9BA6 B6C5 D20D DDE6"            /* çÿÆüÅ¡¦¶ÅÒÂÝæ */
    $"EFF5 F9FB FAFA F9F7 F6F5 F4F1 FEEF 02ED"            /* ïõùûúúù÷öõôñþï.í */
    $"E6E5 95FF ECFF 02E2 6C38 FE42 0343 4546"            /* æåÿìÿ.âl8þB.CEF */
    $"46FA 4803 4645 4342 FC40 0241 3370 E7FF"            /* FúH.FECBü@.A3pçÿ */
    $"1DFD B676 7872 747D 8995 9EA6 ADB5 B9BB"            /* .ý¶vxrt}¦­µ¹» */
    $"BCBC BBBB BAB9 B9B8 B5B4 B4B3 B2AA C1EB"            /* ¼¼»»º¹¹¸µ´´³²ªÁë */
    $"FF96 FF04 DC4A 0A16 16FE 1700 18FB 19FE"            /* ÿÿ.ÜJ...þ...û.þ */
    $"18FF 1700 16FB 1601 0B58 E7FF 01FD 95FD"            /* .ÿ...û...Xçÿ.ýý */
    $"2708 2A2E 3336 393B 3E3F 3FFE 4000 3FFC"            /* '.*.369;>??þ@.?ü */
    $"3EFE 3D02 3C30 78C1 FFFF FF00 C1C3 FF02"            /* >þ=.<0xÁÿÿÿ.ÁÃÿ. */
    $"D56A 51FD 58FF 5A01 5B5C FE5E FD5F 025D"            /* ÕjQýXÿZ.[\þ^ý_.] */
    $"5B58 FE57 0656 5756 5550 64F4 E9FF 0AE7"            /* [XþW.VWVUPdôéÿ.ç */
    $"B4AF B3A0 9B9F ACBC C9D4 03DE E7EF F5FE"            /* ´¯³ ¬¼ÉÔ.Þçïõþ */
    $"F806 F7F4 F0EF F0F1 F0FE EE03 EDEA E2F8"            /* ø.÷ôðïðñðþî.íêâø */
    $"96FF EDFF 02D0 573A FE42 FF43 FF44 0045"            /* ÿíÿ.ÐW:þBÿCÿD.E */
    $"FD47 FF48 0347 4544 42FC 41FF 4002 3B52"            /* ýGÿH.GEDBüAÿ@.;R */
    $"F3E9 FF18 E299 8186 7874 7881 8E98 A0A7"            /* óéÿ.âxtx § */
    $"AEB5 B9BA BBBB B9B8 B5B4 B4B5 B4FE B303"            /* ®µ¹º»»¹¸µ´´µ´þ³. */
    $"B2AF AFF2 ECFF 97FF 05C5 300C 1716 16FE"            /* ²¯¯òìÿÿ.Å0....þ */
    $"17F7 1802 1716 16FB 1602 102E F0E9 FF0E"            /* .÷.....û....ðéÿ. */
    $"D763 252C 2928 292C 3034 3639 3B3E 3EFD"            /* ×c%,)(),0469;>>ý */
    $"3F00 3EF9 3D03 3C38 4AE6 C2FF FFFF 00CC"            /* ?.>ù=.<8JæÂÿÿÿ.Ì */
    $"C5FF 03EB A15A 54FE 5801 5A5C FE5E 035D"            /* Åÿ.ë¡ZTþX.Z\þ^.] */
    $"5C5B 5CFD 5D02 5B59 58FA 5702 544B B7EB"            /* \[\ý].[YXúW.TK·ë */
    $"FF0C F8D1 B0C4 C8AC 9E9E A5B3 C2CE D514"            /* ÿ.øÑ°ÄÈ¬¥³ÂÎÕ. */
    $"DFE9 F0F4 F6F7 F6F4 ECE4 E6EA EDEE ECEC"            /* ßéðôö÷öôìäæêíîìì */
    $"EDEC EBE3 EA96 FFEF FF03 E895 433E FE43"            /* íìëãêÿïÿ.èC>þC */
    $"0144 46FE 4700 46FE 45FD 4604 4543 4241"            /* .DFþG.FþEýF.ECBA */
    $"41FE 4204 4140 3F36 AFEB FF10 F7C3 8790"            /* AþB.A@?6¯ëÿ.÷Ã */
    $"9781 7777 7C87 929B A1A8 B0B5 B8FE B90D"            /* ww|¡¨°µ¸þ¹Â */
    $"B7B2 ABAC B0B2 B3B1 B1B2 B1B1 A7CD ECFF"            /* ·²«¬°²³±±²±±§Íìÿ */
    $"99FF 03E3 7D17 10FC 17FE 18FE 17FC 18FF"            /* ÿ.ã}..ü.þ.þ.ü.ÿ */
    $"17FF 16FB 1602 150C 9FEB FF10 F5A5 3528"            /* .ÿ.û....ëÿ.õ¥5( */
    $"322C 2928 2A2E 3235 3739 3C3D 3DFD 3E02"            /* 2,)(*.2579<==ý>. */
    $"3D3A 3AF9 3C01 2F92 C2FF FFFF 00EA C7FF"            /* =::ù<./Âÿÿÿ.êÇÿ */
    $"23EB AD63 5258 595B 5E65 6C73 797A 7974"            /* #ë­cRXY[^elsyzyt */
    $"6E6A 6662 605F 5E5D 5D5C 5B5A 5757 5657"            /* njfb`_^]]\[ZWWVW */
    $"5756 4C79 FEEE FF0E F8DD B7BD DDDB BAA3"            /* WVLyþîÿ.øÝ·½ÝÛº£ */
    $"A0A3 AEBC C8D1 D815 E1E9 EFF2 F3F3 F2EF"            /*  £®¼ÈÑØ.áéïòóóòï */
    $"E0D3 D9E4 E9EA E9EA EBEA EAE7 E3F8 97FF"            /* àÓÙäéêéêëêêçãøÿ */
    $"F1FF 23E9 A24E 3B41 4345 484C 5258 5B5C"            /* ñÿ#é¢N;ACEHLRX[\ */
    $"5B58 5350 4D4B 4947 4746 4545 4443 4341"            /* [XSPMKIGGFEEDCCA */
    $"4142 4040 366A FEEE FF1A F8D2 978B A4A5"            /* AB@@6jþîÿ.øÒ¤¥ */
    $"8C7B 797B 828D 979D A2AA AFB4 B5B7 B7B6"            /* {y{¢ª¯´µ··¶ */
    $"B4A9 9FA3 ABFA B002 ADB1 F1ED FF9B FF0A"            /* ´©£«ú°.­±ñíÿÿ. */
    $"E48D 250B 1417 1718 191C 1DFE 1F02 1E1C"            /* ä%........þ.... */
    $"1AFE 19FF 1803 1718 1817 FA16 020B 4CFE"            /* .þ.ÿ......ú...Lþ */
    $"EEFF 1AF6 BD57 2734 382F 2A29 292D 3134"            /* îÿ.ö½W'48/*))-14 */
    $"3637 393B 3C3C 3D3E 3D3D 3936 383A FA3B"            /* 679;<<=>==968:ú; */
    $"0236 4AE2 C3FF FFFF 0101 C9FF 25DE 9160"            /* .6JâÃÿÿÿ..Éÿ%Þ` */
    $"5358 5C60 6872 7E8B 97A1 A8AB AAA6 A198"            /* SX\`hr~¡¨«ª¦¡ */
    $"8F85 7D76 7174 7F85 827A 6E64 5D59 5756"            /* }vqt.znd]YWV */
    $"554F AEF0 FF10 F6CA BAC8 E4F6 E6BD A8A5"            /* UO®ðÿ.öÊºÈäöæ½¨¥ */
    $"A5AC B9C4 CDD5 DC10 E3E8 EBED EEEE EDEC"            /* ¥¬¹ÄÍÕÜ.ãèëíîîíì */
    $"D5B9 C6DB E4E6 E6E7 E7FE E802 E4E6 FD98"            /* Õ¹ÆÛäææççþè.äæý */
    $"FFF3 FF25 DA82 4B3C 4245 494F 565F 6972"            /* ÿóÿ%ÚK<BEIOV_ir */
    $"7A7F 8181 7E7A 726C 655F 5A56 585F 6462"            /* z.~zrle_ZVX_db */
    $"5D53 4B46 4341 403F 39A5 F0FF 14F4 B895"            /* ]SKFCA@?9¥ðÿ.ô¸ */
    $"94A9 B9AE 8E7F 7C7C 818B 939A A0A6 ABAF"            /* ©¹®.|| ¦«¯ */
    $"B1B2 FEB3 07B1 A08B 95A5 ABAD ADFD AE03"            /* ±²þ³.± ¥«­­ý®. */
    $"AFA8 BAFB EEFF 9DFF 0CD3 6621 0C13 1718"            /* ¯¨ºûîÿÿ.Óf!.... */
    $"1A1C 2024 282C FE2E 0B2D 2B27 2422 201F"            /* .. $(,þ..-+'$" . */
    $"1C1D 2122 2103 201C 1A17 FE16 0215 0E92"            /* ..!"!. ...þ.... */
    $"F0FF 14F2 944B 2D32 3E3B 312B 2A2A 2C2F"            /* ðÿ.òK-2>;1+**,/ */
    $"3335 3638 3A3B 3C3C FE3D 053C 372F 3239"            /* 3568:;<<þ=.<7/29 */
    $"3AFA 3B02 3164 F8C4 FFFF FF01 17CC FF29"            /* :ú;.1døÄÿÿÿ..Ìÿ) */
    $"F8C7 9264 505C 5D62 6C79 8795 A3B0 BBC5"            /* øÇdP\]bly£°»Å */
    $"CBCE CFCE CCC8 C1B9 B0A8 9990 AABC BCB3"            /* ËÎÏÎÌÈÁ¹°¨ª¼¼³ */
    $"A696 8678 6B61 5851 58C7 F3FF 12F1 CBBE"            /* ¦xkaXQXÇóÿ.ñË¾ */
    $"CEED FDFF EAB9 A9A8 A7AC B6C1 CAD1 D8DE"            /* Îíýÿê¹©¨§¬¶ÁÊÑØÞ */
    $"0DE4 E7E8 EAEB EBEA EAD9 9EA4 D4E0 E2FE"            /* ÂäçèêëëêêÙ¤Ôàâþ */
    $"E300 E4FE E502 E1E9 FD99 FFF6 FF10 F9BE"            /* ã.äþå.áéýÿöÿ.ù¾ */
    $"7F4D 3744 474B 525C 6671 7B85 8E95 99FE"            /* .M7DGKR\fq{þ */
    $"9C15 9A96 928B 857F 736D 7F8E 8D87 7D71"            /* ..sm.}q */
    $"655A 5148 423B 44C0 F3FF 15EE B798 98B2"            /* eZQHB;DÀóÿ.î·² */
    $"C4C7 B08C 7F7E 7D81 8991 989D A2A7 ABAE"            /* ÄÇ°.~}¢§«® */
    $"AEFC B006 A377 7B9F A9AA AAFE ABFF AC03"            /* ®ü°.£w{©ªªþ«ÿ¬. */
    $"ABA6 C6FC EFFF A0FF 1EFA AD5B 1F09 1418"            /* «¦Æüïÿ ÿ.ú­[.Æ.. */
    $"1A1B 1E23 272B 2F32 3335 3738 3837 3532"            /* ...#'+/235788752 */
    $"302E 2B27 252C 3131 0A2F 2B27 221F 1C19"            /* 0.+'%,11./+'"... */
    $"1711 1BB3 F3FF 16E9 8F4A 2936 4244 3C2F"            /* ...³óÿ.éJ)6BD</ */
    $"2B2A 2A2C 2F31 3435 3738 3A3B 3C3C FD3B"            /* +**,/14578:;<<ý; */
    $"0637 282A 3639 3A3A FD39 FF3A 0230 7FFA"            /* .7(*69::ý9ÿ:.0.ú */
    $"C5FF FFFF 012A CFFF 2DFD EACB CDD5 E7E5"            /* Åÿÿÿ.*Ïÿ-ýêËÍÕçå */
    $"9F69 7C8A 949D A8B3 BDC8 CFD6 DCDF E0E2"            /* i|¨³½ÈÏÖÜßàâ */
    $"E3E3 E2E0 DCDB C487 A0D4 DBD9 D5CE C3B4"            /* ããâàÜÛÄ ÔÛÙÕÎÃ´ */
    $"A390 7B68 5560 C0F7 FF0A FBDB C5C8 DAF3"            /* £{hU`À÷ÿ.ûÛÅÈÚó */
    $"FFFF F7D2 B3FE AA07 AEB6 C0C8 CFD5 DBDF"            /* ÿÿ÷Ò³þª.®¶ÀÈÏÕÛß */
    $"0DE3 E5E6 E7E8 E8E7 E6E5 AA68 BADD DEFE"            /* ÂãåæçèèçæåªhºÝÞþ */
    $"E007 E1E2 E3E3 E2DE E5F9 9AFF F9FF 2DFE"            /* à.áâããâÞåùÿùÿ-þ */
    $"E6B7 A6A1 AEB3 804F 5E68 6F76 7F87 8F97"            /* æ·¦¡®³O^hov. */
    $"9CA1 A6A8 A9AB ABAA AAA8 A6A4 9365 79A0"            /* ¡¦¨©««ªª¨¦¤ey  */
    $"A5A4 A09B 9287 7C6E 5D4F 3E4C B8F7 FF0A"            /* ¥¤ |n]O>L¸÷ÿ. */
    $"FACF A99B A2B7 C5D3 C69F 87FE 800D 8389"            /* úÏ©¢·ÅÓÆþÂ */
    $"9097 9BA0 A5A8 ABAC ADAD AEAE FEAD 0380"            /*  ¥¨«¬­­®®þ­. */
    $"4F8C A7FE A8FE A9FF AA03 A9A4 BDF2 F0FF"            /* O§þ¨þ©ÿª.©¤½òðÿ */
    $"A2FF 14DF 8E55 3032 3E30 1B20 2425 282C"            /* ¢ÿ.ßU02>0. $%(, */
    $"2F31 3435 3639 393A FE3B FF3A 0639 3832"            /* /145699:þ;ÿ:.982 */
    $"2129 3738 FF37 0935 322F 2A25 1F1B 1025"            /* !)78ÿ7Æ52/*%...% */
    $"ABF7 FF0A FABA 6F41 2D39 434E 4836 2EFE"            /* «÷ÿ.úºoA-9CNH6.þ */
    $"2B09 2C2E 3133 3536 3839 393A FC3B FF3A"            /* +Æ,.1356899:ü;ÿ: */
    $"022B 1B2F F939 043A 392E 6CE4 C6FF FFFF"            /* .+./ù9.:9.läÆÿÿÿ */
    $"0139 D2FF 1AFE F3D7 D6DC DDE2 E8F6 F4CD"            /* .9Òÿ.þó×ÖÜÝâèöôÍ */
    $"ACAC ABAC B1BA C3CA D1D6 DBDF E1E3 E5E5"            /* ¬¬«¬±ºÃÊÑÖÛßáãåå */
    $"FEE6 06E5 E6E0 966A C2DE FEDF 0ADD D9D2"            /* þæ.åæàjÂÞþß.ÝÙÒ */
    $"C8BC A991 7669 A8F3 FCFF 0BFE EDCF CAD4"            /* È¼©vi¨óüÿ.þíÏÊÔ */
    $"E1E2 E1EE F2D5 B9FE AB09 ACB1 B8C0 C8CE"            /* áâáîòÕ¹þ«Æ¬±¸ÀÈÎ */
    $"D3D9 DDDF 1AE2 E3E4 E4E5 E5E4 E3E5 D97D"            /* ÓÙÝß.âãääååäãåÙ} */
    $"6FC5 DFDE DDDD DEDF E0E0 E1E0 DDE0 EEFE"            /* oÅßÞÝÝÞßààáàÝàîþ */
    $"9CFF FCFF 0AFE F0C4 B3AC A6A9 B1C2 C4A0"            /* ÿüÿ.þðÄ³¬¦©±ÂÄ  */
    $"FE81 0B82 868C 9398 9DA1 A5A8 A9AB ACFD"            /* þ.¡¥¨©«¬ý */
    $"AD05 ACAD A970 5092 FEA7 0BA8 A7A4 A098"            /* ­.¬­©pPþ§.¨§¤  */
    $"8D80 6E57 519E F2FB FF0A E7B8 A3A0 A9AA"            /* nWQòûÿ.ç¸£ ©ª */
    $"ABB8 C1A7 8CFD 810A 858B 9097 9B9F A3A6"            /* «¸Á§ý.£¦ */
    $"A9AA ABFD ACFF AB12 ACA3 5E53 95A8 A7A6"            /* ©ª«ý¬ÿ«.¬£^S¨§¦ */
    $"A6A7 A7A8 A8A9 A9A4 AED8 FEF2 FFA5 FF16"            /* ¦§§¨¨©©¤®Øþòÿ¥ÿ. */
    $"EB9C 6A45 2F34 3D49 4C3A 2C2B 2B2C 2E31"            /* ëjE/4=IL:,++,.1 */
    $"3234 3536 3739 39F9 3A04 3926 1B32 39FC"            /* 2456799ù:.9&.29ü */
    $"3808 3634 312C 251A 2289 F1FB FF0A DE8A"            /* 8.641,%."ñûÿ.Þ */
    $"5332 3036 3A43 493C 30FD 2B09 2E2F 3133"            /* S206:CI<0ý+Æ./13 */
    $"3536 3738 3839 F93A 0437 201D 3239 FD38"            /* 567889ù:.7 .29ý8 */
    $"FC39 032E 4AAC FEC8 FFFF FF01 49D4 FF1C"            /* ü9..J¬þÈÿÿÿ.IÔÿ. */
    $"F7DD D7DA CCC2 B7BB D6D9 C8B4 ADAE AEB1"            /* ÷Ý×ÚÌÂ·»ÖÙÈ´­®®± */
    $"B5BC C4CC D2D7 DBDD E0E2 E3E4 E4FE E523"            /* µ¼ÄÌÒ×ÛÝàâãääþå# */
    $"E4E3 E4CF 747A D2E0 DEDF DFE0 E1E0 DFDC"            /* äãäÏtzÒàÞßßàáàßÜ */
    $"D4C5 AD85 85C5 FDFF F2CE C6CD D2C7 BAB4"            /* ÔÅ­ÅýÿòÎÆÍÒÇº´ */
    $"C8DC CFB9 FDAD 0AB0 B4B9 C0C6 CED4 D8DC"            /* ÈÜÏ¹ý­.°´¹ÀÆÎÔØÜ */
    $"DFE1 12E2 E3E4 E4E5 E5E4 E3E3 E7C9 676E"            /* ßá.âãääååäããçÉgn */
    $"C4E1 DDDE DFDF FEE0 FFE1 03E0 DEE5 F69D"            /* ÄáÝÞßßþàÿá.àÞåö */
    $"FFFE FF1C F6CE B7B0 9992 8B8E A8AB 9C88"            /* ÿþÿ.öÎ·°¨« */
    $"8183 8385 888D 9399 9DA1 A5A7 A8AA ABAB"            /* ¡¥§¨ª«« */
    $"ACFE AD24 ACAB AC9B 575B 9EA7 A6A7 A8A8"            /* ¬þ­$¬«¬W[§¦§¨¨ */
    $"A9A9 A8A5 A096 8163 71BF FEFF EFBC A7A1"            /* ©©¨¥ cq¿þÿï¼§¡ */
    $"9F97 8D88 9BAD A18D 81FE 820C 8487 8C90"            /* ­¡þ. */
    $"959A 9FA3 A5A7 A9AA ABFD ACFF AB07 AAAD"            /* £¥§©ª«ý¬ÿ«.ª­ */
    $"984E 5393 A9A6 FEA7 00A8 FDA9 03A7 A4BD"            /* NS©¦þ§.¨ý©.§¤½ */
    $"EEF3 FFA8 FF18 F6B0 734C 2C2B 2D32 4141"            /* îóÿ¨ÿ.ö°sL,+-2AA */
    $"392E 2B2C 2C2D 2E30 3234 3536 3738 38F7"            /* 9.+,,-.02456788÷ */
    $"3A03 351E 1F36 0039 FE38 FD39 2138 3632"            /* :.5..6.9þ8ý9!862 */
    $"291F 49B3 FDFF EA98 643E 2D2E 2F2E 3842"            /* ).I³ýÿêd>-./.8B */
    $"3B31 2B2C 2C2B 2C2E 3031 3234 3637 38FE"            /* ;1+,,+,.0124678þ */
    $"39F8 3A04 331B 1C32 39FE 38FB 3903 3330"            /* 9ø:.3..29þ8û9.30 */
    $"6DDB C9FF FFFF 0147 D6FF 1CD8 C1DB D6CD"            /* mÛÉÿÿÿ.GÖÿ.ØÁÛÖÍ */
    $"BAA7 A2BC C6AE 9790 9094 9AA4 B1C2 D5E4"            /* º§¢¼Æ®¤±ÂÕä */
    $"EAEE F0F2 F4F5 F6F6 FCF7 FFF6 06F8 D98B"            /* êîðòôõööü÷ÿö.øÙ */
    $"5781 E0F3 FDF1 25EF EEE9 E4E0 DED4 B688"            /* Wàóýñ%ïîéäàÞÔ¶ */
    $"8DAF C1D7 D7C9 B1A1 AFC9 BAA1 9190 9092"            /* ¯Á××É±¡¯Éº¡ */
    $"959C A7B4 C3D6 E3EA EEF1 F3F5 F500 F6FC"            /* §´ÃÖãêîñóõõ.öü */
    $"F7FD F606 D585 5565 BDF2 F2FE F1FF F007"            /* ÷ýö.ÕUe½òòþñÿð. */
    $"EFEC EAE7 E0DB E5FE 9FFF 1BFF D3A9 B4A4"            /* ïìêçàÛåþÿ.ÿÓ©´¤ */
    $"9A8B 7C79 8E9B 8671 6B6C 6F73 7A85 91A0"            /* |yqklosz  */
    $"ADB3 B7B8 B8B9 B9FC BAFE BB07 BCC0 A768"            /* ­³·¸¸¹¹üºþ».¼À§h */
    $"4060 AAB7 FEB5 FFB4 22B2 AEAA A9A7 9F86"            /* @`ª·þµÿ´"²®ª©§ */
    $"667D 9C9B A5A4 9985 7883 9D92 7A6C 6B6C"            /* f}¥¤xzlkl */
    $"6D70 747D 8693 A1AB B3B7 B8B8 FEB9 FABA"            /* mpt}¡«³·¸¸þ¹úº */
    $"09BB BDA4 643F 4B8E B7B6 B5FD B407 B3B0"            /* Æ»½¤d?K·¶µý´.³° */
    $"AFAD A5A7 CBFE F5FF AAFF 15C7 7658 342C"            /* ¯­¥§Ëþõÿªÿ.ÇvX4, */
    $"2B27 262F 3A30 2421 2223 2528 2B2F 353B"            /* +'&/:0$!"#%(+/5; */
    $"3DFE 3EF9 3DFF 3E05 3F42 3B23 141E 0138"            /* =þ>ù=ÿ>.?B;#...8 */
    $"3DFC 3B1E 3A38 3635 3531 2422 5F78 4933"            /* =ü;.:86551$"_xI3 */
    $"3131 2B26 2A3A 3729 2222 2323 2425 282B"            /* 11+&*:7)""##$%(+ */
    $"3035 3AFD 3EF8 3DFF 3E07 4038 2113 172E"            /* 05:ý>ø=ÿ>.@8!... */
    $"3E3C FB3B 053A 3937 2C3C 97CA FFFF FF01"            /* ><û;.:97,<Êÿÿÿ. */
    $"62D6 FF44 AD91 C1C8 CCD5 DBDF BC73 6362"            /* bÖÿD­ÁÈÌÕÛß¼scb */
    $"6161 6367 6E7B 8DA5 B2B1 B2B3 B2B1 B0AF"            /* aacgn{¥²±²³²±°¯ */
    $"AFB0 AFAE ADAC ABAA AB95 7266 5694 B2AE"            /* ¯°¯®­¬«ª«rfV²® */
    $"ADAC A9A5 A4A6 A5A3 A19E 9C94 7B75 A2C5"            /* ­¬©¥¤¦¥£¡{u¢Å */
    $"C6D2 D9DE D28C 6564 62FE 6109 6468 707C"            /* ÆÒÙÞÒedbþaÆdhp| */
    $"8DA3 AFB1 B2B1 FEB0 1DB0 AFAF AEAD ABAB"            /* £¯±²±þ°.°¯¯®­«« */
    $"AAAA A995 7667 5172 ABAD ABAA A9A8 A6A3"            /* ªª©vgQr«­«ª©¨¦£ */
    $"A5A3 9E98 97B7 FD9F FF1F FFA2 7296 9A9A"            /* ¥£·ýÿ.ÿ¢r */
    $"A1A5 A88F 584B 4B4A 4A4B 4F55 5E6C 7E8D"            /* ¡¥¨XKKJJKOU^l~ */
    $"9394 918D 8B88 8887 8685 FE84 FF83 2086"            /* þÿ  */
    $"7558 4E42 7489 8584 8281 7E7D 8281 807E"            /* uXNBt~}~ */
    $"7B7B 7668 617F 9995 9EA5 A89F 6B4C 4C4B"            /* {{vha.¥¨kLLK */
    $"FE4A 124C 5055 5F6C 7D89 9191 8F8B 8887"            /* þJ.LPU_l} */
    $"8685 8584 8383 FD82 1375 5A4E 3E57 8785"            /* ý.uZN>W */
    $"8281 807F 7D7B 807E 7B76 769F FDF5 FFAA"            /* .}{~{vvýõÿª */
    $"FF09 8E36 3E3C 3739 3A3B 3521 FD1C 0D1D"            /* ÿÆ6><79:;5!ý.Â. */
    $"1E1F 2327 2F38 3D3D 3A36 3432 32FE 31FC"            /* ..#'/8==:6422þ1ü */
    $"3004 322D 221E 1903 2C33 302F FE2E 1430"            /* 0.2-"...,30/þ..0 */
    $"3839 3A3A 3736 3A43 3837 3D35 383A 3B39"            /* 89::76:C87=58:;9 */
    $"281C 1C1D FE1C 0B1D 1E1F 2227 2F36 3C3C"            /* (...þ....."'/6<< */
    $"3834 33FE 31FF 30FC 2F14 312F 241E 1821"            /* 843þ1ÿ0ü/.1/$..! */
    $"3430 2F2F 2E2E 2D2D 3435 3432 346F FCCB"            /* 40//..--45424oüË */
    $"FFFF FF00 F3D5 FF09 F7F2 F2E6 E9F5 FFEF"            /* ÿÿÿ.óÕÿÆ÷òòæéõÿï */
    $"DCDE FCDD 03DC DBD9 D7F0 D606 D9DD DDDE"            /* ÜÞüÝ.ÜÛÙ×ðÖ.ÙÝÝÞ */
    $"D9D5 D5FE D602 D5DB EFFC F10C F4FC FBF2"            /* ÙÕÕþÖ.ÕÛïüñ.ôüûò */
    $"EBE2 E8F0 FFFA E0DE DEFB DD03 DCDB DAD7"            /* ëâèðÿúàÞÞûÝ.ÜÛÚ× */
    $"FAD6 FDD6 FFD7 FFD6 FFD7 01DA DEFE DDFA"            /* úÖýÖÿ×ÿÖÿ×.ÚÞþÝú */
    $"D606 D7EA EFEE EFF2 FB9E FFFF FF08 F7F1"            /* Ö.×êïîïòûÿÿÿ.÷ñ */
    $"EFE0 E2EB F3E6 D8FE D906 D8D9 D9D8 D7D6"            /* ïàâëóæØþÙ.ØÙÙØ×Ö */
    $"D3FC D2F5 D300 D5FE D900 D5FB D301 D9EF"            /* ÓüÒõÓ.ÕþÙ.ÕûÓ.Ùï */
    $"FCF1 0AF4 FCFB F2E8 DCE0 E7F3 EEDA F9D9"            /* üñ.ôüûòèÜàçóîÚùÙ */
    $"03D8 D7D6 D4FD D2F4 D304 D5D9 D8D9 D8FA"            /* .Ø×ÖÔýÒôÓ.ÕÙØÙØú */
    $"D306 D4EA F0EF EFF2 FCF4 FFA9 FF07 F8F1"            /* Ó.Ôêðïïòüôÿ©ÿ.øñ */
    $"EAD2 D2D5 D8D4 F8CF 01CE CDFD CCF4 CD00"            /* êÒÒÕØÔøÏ.ÎÍýÌôÍ. */
    $"CEFE CF00 CEFC CD13 CCD4 F0F2 F1F0 F0F1"            /* ÎþÏ.ÎüÍ.ÌÔðòñððñ */
    $"F3FC FAF2 E4D0 D1D4 D8D6 CFD0 F8CF FFCE"            /* óüúòäÐÑÔØÖÏÐøÏÿÎ */
    $"FDCC F4CD 00CE FECF 00CE FACD 06CE EAF0"            /* ýÌôÍ.ÎþÏ.ÎúÍ.Îêð */
    $"EFEF F4FD CAFF FFFF 000C 81FF 81FF 81FF"            /* ïïôýÊÿÿÿ..ÿÿÿ */
    $"81FF 81FF FFFF 000C 81FF 81FF 81FF 81FF"            /* ÿÿÿÿ..ÿÿÿÿ */
    $"81FF FFFF 000C 81FF 81FF 81FF 81FF 81FF"            /* ÿÿÿ..ÿÿÿÿÿ */
    $"FFFF 000C 81FF 81FF 81FF 81FF 81FF FFFF"            /* ÿÿ..ÿÿÿÿÿÿÿ */
    $"000C 81FF 81FF 81FF 81FF 81FF FFFF 000C"            /* ..ÿÿÿÿÿÿÿ.. */
    $"81FF 81FF 81FF 81FF 81FF FFFF 000C 81FF"            /* ÿÿÿÿÿÿÿ..ÿ */
    $"81FF 81FF 81FF 81FF FFFF 000C 81FF 81FF"            /* ÿÿÿÿÿÿ..ÿÿ */
    $"81FF 81FF 81FF FFFF 00FF"                           /* ÿÿÿÿÿ.ÿ */
};

data 'PICT' (129) {
    $"32C4 0000 0000 0066 00DC 0011 02FF 0C00"            /* 2Ä.....f.Ü...ÿ.. */
    $"FFFE 0000 0048 0000 0048 0000 0000 0000"            /* ÿþ...H...H...... */
    $"0066 00DC 0000 0000 0001 000A 0000 0000"            /* .f.Ü............ */
    $"0066 00DC 0098 80DC 0000 0000 0066 00DC"            /* .f.Ü.Ü.....f.Ü */
    $"0000 0000 0000 0000 0048 0000 0048 0000"            /* .........H...H.. */
    $"0000 0008 0001 0008 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0041 599E 0000 0045 0000 FFFF"            /* .....AY...E..ÿÿ */
    $"FFFF FFFF 0001 FFFF FFFF FFFF 0002 FFFF"            /* ÿÿÿÿ..ÿÿÿÿÿÿ..ÿÿ */
    $"FFFF 0000 0003 FFFF FFFF 0000 0004 FFFF"            /* ÿÿ....ÿÿÿÿ....ÿÿ */
    $"9999 9999 0005 FFFF 9999 9999 0006 FFFF"            /* ..ÿÿ..ÿÿ */
    $"6666 6666 0007 FFFF 6666 6666 0008 FFFF"            /* ffff..ÿÿffff..ÿÿ */
    $"6666 0000 0009 FFFF 6666 0000 000A FFFF"            /* ff...Æÿÿff....ÿÿ */
    $"3333 3333 000B FFFF 3333 3333 000C FFFF"            /* 3333..ÿÿ3333..ÿÿ */
    $"0000 9999 000D FFFF 0000 9999 000E FFFF"            /* ...Âÿÿ....ÿÿ */
    $"0000 0000 000F FFFF 0000 0000 0010 EEEE"            /* ......ÿÿ......îî */
    $"EEEE EEEE 0011 EEEE EEEE EEEE 0012 EEEE"            /* îîîî..îîîîîî..îî */
    $"0000 0000 0013 EEEE 0000 0000 0014 DDDD"            /* ......îî......ÝÝ */
    $"DDDD DDDD 0015 DDDD DDDD DDDD 0016 DDDD"            /* ÝÝÝÝ..ÝÝÝÝÝÝ..ÝÝ */
    $"0000 0000 0017 DDDD 0000 0000 0018 CCCC"            /* ......ÝÝ......ÌÌ */
    $"CCCC FFFF 0019 CCCC CCCC FFFF 001A CCCC"            /* ÌÌÿÿ..ÌÌÌÌÿÿ..ÌÌ */
    $"CCCC CCCC 001B CCCC CCCC CCCC 001C CCCC"            /* ÌÌÌÌ..ÌÌÌÌÌÌ..ÌÌ */
    $"0000 0000 001D CCCC 0000 0000 001E BBBB"            /* ......ÌÌ......»» */
    $"BBBB BBBB 001F BBBB BBBB BBBB 0020 BBBB"            /* »»»»..»»»»»». »» */
    $"0000 0000 0021 BBBB 0000 0000 0022 AAAA"            /* .....!»»....."ªª */
    $"AAAA AAAA 0023 AAAA AAAA AAAA 0024 AAAA"            /* ªªªª.#ªªªªªª.$ªª */
    $"0000 0000 0025 AAAA 0000 0000 0026 9999"            /* .....%ªª.....& */
    $"9999 9999 0027 9999 9999 9999 0028 9999"            /* .'.( */
    $"0000 0000 0029 9999 0000 0000 002A 8888"            /* .....).....* */
    $"8888 8888 002B 8888 8888 8888 002C 8888"            /* .+., */
    $"0000 0000 002D 8888 0000 0000 002E 7777"            /* .....-......ww */
    $"7777 7777 002F 7777 7777 7777 0030 7777"            /* wwww./wwwwww.0ww */
    $"0000 0000 0031 7777 0000 0000 0032 6666"            /* .....1ww.....2ff */
    $"6666 6666 0033 6666 6666 6666 0034 5555"            /* ffff.3ffffff.4UU */
    $"5555 5555 0035 5555 5555 5555 0036 5555"            /* UUUU.5UUUUUU.6UU */
    $"0000 0000 0037 5555 0000 0000 0038 4444"            /* .....7UU.....8DD */
    $"4444 4444 0039 4444 4444 4444 003A 4444"            /* DDDD.9DDDDDD.:DD */
    $"0000 0000 003B 4444 0000 0000 003C 2222"            /* .....;DD.....<"" */
    $"2222 2222 003D 2222 2222 2222 003E 1111"            /* """".="""""".>.. */
    $"1111 1111 003F 1111 1111 1111 0040 0000"            /* .....?.......@.. */
    $"BBBB 0000 0041 0000 BBBB 0000 0042 0000"            /* »»...A..»»...B.. */
    $"0000 DDDD 0043 0000 0000 DDDD 0044 0000"            /* ..ÝÝ.C....ÝÝ.D.. */
    $"0000 0000 0045 0000 0000 0000 0000 0000"            /* .....E.......... */
    $"0066 00DC 0000 0000 0066 00DC 0000 B7EB"            /* .f.Ü.....f.Ü..·ë */
    $"00FD 010A 0001 0100 0100 0001 0001 00FE"            /* .ý.............þ */
    $"010C 0001 0100 0001 0001 0000 0100 00FE"            /* ...............þ */
    $"0100 00FE 010D 0001 0100 0001 0100 0001"            /* ...þ.Â.......... */
    $"0001 0000 FE01 0100 01FC 0009 0101 0001"            /* ....þ....ü.Æ.... */
    $"0001 0100 0101 FE00 0101 01FD 0006 0100"            /* ......þ....ý.... */
    $"0101 0000 01FE 00FE 0106 0001 0001 0000"            /* .....þ.þ........ */
    $"01FE 0008 142A 3844 4545 4445 45FE 4403"            /* .þ...*8DEEDEEþD. */
    $"4545 4445 FD44 0239 2A14 FD00 0901 0100"            /* EEDEýD.9*.ý.Æ... */
    $"0001 0100 142B 39FD 3A09 3B38 2B15 0100"            /* .....+9ý:Æ;8+... */
    $"0001 0100 FE01 0100 01FE 0002 0101 00FD"            /* ....þ....þ.....ý */
    $"0102 0000 01FE 0000 01FC 00FD 0103 0001"            /* .....þ...ü.ý.... */
    $"0000 FC01 FE00 CA01 0101 FE00 0201 0100"            /* ..ü.þ.Ê...þ..... */
    $"FD01 0000 FE01 0400 0001 0100 FE01 0100"            /* ý...þ.......þ... */
    $"01FD 0000 01FB 00FE 0109 0000 0101 0001"            /* .ý...û.þ.Æ...... */
    $"0100 0101 FE00 0F01 0100 0001 0001 0001"            /* ....þ........... */
    $"0100 0001 0001 00FE 01FB 0003 0100 0101"            /* .......þ.û...... */
    $"FB00 0401 0100 0100 FE01 0000 FE01 0200"            /* û.......þ...þ... */
    $"0101 FD00 0101 00FE 0106 0001 0000 142B"            /* ..ý....þ.......+ */
    $"39FE 4406 4545 4445 4530 05FD 0411 0507"            /* 9þD.EEDEE0.ý.... */
    $"0606 0706 0706 0707 0606 0706 3044 4445"            /* ............0DDE */
    $"FB44 0245 4544 FE45 0125 24FE 2504 243B"            /* ûD.EEDþE.%$þ%.$; */
    $"3A3B 3AFE 3B02 3A3A 3BFE 3A02 392A 14FD"            /* :;:þ;.::;þ:.9*.ý */
    $"0007 0101 0000 0101 0000 FE01 1300 0001"            /* ..........þ..... */
    $"0000 0101 0001 0000 0100 0101 0000 0100"            /* ................ */
    $"01CA 0300 0101 00FE 0106 0000 0101 0000"            /* .Ê.....þ........ */
    $"01FE 00FE 0106 0000 0101 0000 01FB 0004"            /* .þ.þ.........û.. */
    $"0101 0001 01FE 0009 0101 0000 0100 0100"            /* .....þ.Æ........ */
    $"0101 FD00 0101 00FE 010E 0001 0100 0001"            /* ..ý....þ........ */
    $"0100 0001 0001 0000 01FA 0002 0100 01FD"            /* .........ú.....ý */
    $"000A 0101 0001 0000 0100 0101 00FE 010E"            /* .............þ.. */
    $"0000 0101 0000 142B 3944 4545 4445 31FE"            /* .......+9DEEDE1þ */
    $"04FE 0709 0607 0607 0A0B 0B0A 0A0B FE0A"            /* .þ.Æ..........þ. */
    $"0A0B 0B0A 0B0A 0A0B 0A0B 0B06 FE07 0506"            /* ............þ... */
    $"0607 0730 44FE 4502 4444 45FB 4402 4545"            /* ...0DþE.DDEûD.EE */
    $"44FD 4500 24FE 2504 2425 243B 3AFE 3B02"            /* DýE.$þ%.$%$;:þ;. */
    $"382A 15FE 0000 01FB 0009 0101 0001 0100"            /* 8*.þ...û.Æ...... */
    $"0100 0101 FD00 0401 0001 0100 CDFE 0103"            /* ....ý.......Íþ.. */
    $"0000 0101 FD00 0501 0001 0100 00FE 0108"            /* ....ý........þ.. */
    $"0001 0100 0001 0001 00FE 0102 0000 01FE"            /* .........þ.....þ */
    $"000B 0100 0100 0001 0000 0100 0101 FB00"            /* ..............û. */
    $"0401 0100 0100 FE01 0100 01FE 00FE 0119"            /* ......þ....þ.þ.. */
    $"0000 0100 0001 0100 0100 0001 0001 0100"            /* ................ */
    $"0001 0001 0001 0100 0001 FD00 0B01 0014"            /* ..........ý..... */
    $"2A38 4444 4531 0504 07FE 0602 070B 0AFD"            /* *8DDE1...þ.....ý */
    $"0B03 0A0A 0B0A FC0E 070F 0F0E 0E0F 0E0F"            /* ......ü......... */
    $"0EFD 0F03 0E0E 0A0A FE0B FD0A 050E 0F0F"            /* .ý......þ.ý..... */
    $"0E0F 13FE 1601 1731 FE44 1438 2B14 0115"            /* ...þ...1þD.8+... */
    $"2A39 4444 4544 4545 4445 2525 2424 3A3B"            /* *9DDEDEEDE%%$$:; */
    $"FE3A 0238 2A14 FE01 0000 FE01 0400 0101"            /* þ:.8*.þ...þ..... */
    $"0001 FD00 FD01 0200 0001 CE02 0000 01FB"            /* ..ý.ý.....Î....û */
    $"0007 0100 0001 0100 0100 FE01 0400 0001"            /* ..........þ..... */
    $"0000 FE01 0700 0001 0100 0001 00FE 01FE"            /* ..þ..........þ.þ */
    $"0000 01FB 0002 0100 00FD 0104 0000 0100"            /* ...û.....ý...... */
    $"00FE 0105 0001 0000 0101 FE00 0901 0100"            /* .þ........þ.Æ... */
    $"0001 0001 0001 01FD 0001 0100 FE01 0400"            /* .......ý....þ... */
    $"0001 0000 FE01 0C15 2A38 4544 3005 0606"            /* ....þ...*8ED0... */
    $"0707 0B0A FE0B 060A 0A0F 0F0E 0E0F FB0E"            /* ....þ.........û. */
    $"010F 0FFE 0E05 0F0F 0E0F 0F0E FD0F 000E"            /* ...þ........ý... */
    $"FE0F 000E FE0F 040E 0E0F 0E0E FD12 1113"            /* þ...þ.......ý... */
    $"1312 1316 1617 1617 2131 4438 2B15 0000"            /* ........!1D8+... */
    $"01FD 0015 142A 3945 4544 4445 2524 2525"            /* .ý...*9EEDDE%$%% */
    $"3A3B 3A3A 3B38 2B15 0000 FE01 0300 0101"            /* :;::;8+...þ..... */
    $"00FE 0104 0000 0101 00CA 1601 0000 0100"            /* .þ.......Ê...... */
    $"0101 0000 0101 0000 0101 0001 0000 0100"            /* ................ */
    $"0101 FE00 0401 0100 0101 FD00 0401 0001"            /* ..þ.......ý..... */
    $"0100 FE01 0100 00FE 0101 0001 FD00 0301"            /* ..þ....þ....ý... */
    $"0001 01FB 0014 0101 0001 0001 0100 0001"            /* ...û............ */
    $"0100 0001 0100 0100 0001 00FD 01FD 000C"            /* ...........ý.ý.. */
    $"0101 0000 152A 3944 3107 0606 07FD 0A00"            /* .....*9D1....ý.. */
    $"0BFB 0E01 0F0F FE0E 020F 0E0E FE0F 080E"            /* .û....þ.....þ... */
    $"0F0E 0F0E 0F0F 0E0E FE0F 000E FE0F 090E"            /* ........þ...þ.Æ. */
    $"0E0F 0F0E 0E0F 0E13 13FB 121F 1313 1213"            /* .........û...... */
    $"1213 1312 1217 1D1D 1C21 3144 4438 2A15"            /* .........!1DD8*. */
    $"0001 0100 0100 0001 0015 2B38 FE45 0E44"            /* ..........+8þE.D */
    $"4425 2524 243B 3A3B 3A3B 392A 1401 FD00"            /* D%%$$;:;:;9*..ý. */
    $"0001 FC00 CE00 00FE 0100 00FE 0114 0001"            /* ..ü.Î..þ...þ.... */
    $"0100 0001 0001 0001 0100 0100 0001 0001"            /* ................ */
    $"0100 00FE 0104 0001 0100 01FD 00FE 0101"            /* ...þ.......ý.þ.. */
    $"0001 FD00 0301 0001 01FB 0009 0101 0001"            /* ..ý......û.Æ.... */
    $"0001 0100 0001 FE00 0C01 0100 0100 0001"            /* ......þ......... */
    $"0001 0100 0001 FD00 0001 FE00 0214 2A38"            /* ......ý...þ...*8 */
    $"FE45 0044 FE45 0A44 4545 4444 4544 4544"            /* þE.DþE.DEEDDEDED */
    $"4431 FB0E 120F 0F0E 0F0F 0E0F 0E0F 0F0E"            /* D1û............. */
    $"0E0F 0E0F 0E0F 0F0E FE0F 010E 0EFE 0F01"            /* ........þ....þ.. */
    $"0E31 FE44 0A45 4544 4530 1617 1213 1312"            /* .1þD.EEDE0...... */
    $"FD17 0316 1717 16FE 1D09 1C1C 2031 4444"            /* ý......þ.Æ.. 1DD */
    $"382A 1400 FE01 0100 01FE 0004 0101 142B"            /* 8*..þ....þ.....+ */
    $"38FE 440A 4545 4406 0B20 4544 4439 1EFC"            /* 8þD.EED.. EDD9.ü */
    $"00FE 01C8 FC00 0101 01FD 0001 0100 FD01"            /* .þ.Èü....ý....ý. */
    $"0500 0001 0000 01FB 0007 0101 0000 0101"            /* .......û........ */
    $"0000 FE01 1400 0001 0000 0101 0000 0100"            /* ..þ............. */
    $"0100 0101 0000 0100 0100 FD01 0C00 0100"            /* ..........ý..... */
    $"0001 0100 0001 0001 0000 FB01 2800 0001"            /* ..........û.(... */
    $"0001 0100 0014 2A44 4445 4544 2322 2345"            /* ......*DDEED#"#E */
    $"4444 4545 4444 4545 4414 1514 4544 4545"            /* DDEEDDEED...EDEE */
    $"4445 4530 0E0E FE0F 010E 0FFD 0E00 0FFB"            /* DEE0..þ....ý...û */
    $"0EFE 0F08 0E0F 3044 4445 4544 45FD 4409"            /* .þ....0DDEEDEýDÆ */
    $"4545 3016 1716 1716 1617 FB16 2E17 1716"            /* EE0.......û..... */
    $"1C1C 1D1C 1C21 3145 4439 2A15 0001 0100"            /* .....!1ED9*..... */
    $"0100 0001 0001 0100 0101 142A 4407 0B16"            /* ...........*D... */
    $"1621 2444 381E 1500 0101 0001 CD00 00FE"            /* .!$D8.......Í..þ */
    $"0104 0001 0001 00FE 01FB 0000 01FB 000A"            /* .......þ.û...û.. */
    $"0101 0001 0000 0100 0101 00FE 01FE 0000"            /* ...........þ.þ.. */
    $"01FB 0002 0101 00FD 0100 00FE 0104 0001"            /* .û.....ý...þ.... */
    $"0001 00FE 0102 0000 01FE 0000 01FB 0001"            /* ...þ.....þ...û.. */
    $"0101 FD00 0901 0001 152B 3844 2322 44FE"            /* ..ý.Æ....+8D#"Dþ */
    $"450C 4435 141A 1E1F 1518 1411 141F 34FE"            /* E.D5..........4þ */
    $"4514 4444 4514 1423 2344 4544 4445 300F"            /* E.DDE..##DEDDE0. */
    $"0F0E 0E0F 0E0F 0EFE 0F4F 0E0E 0F0F 3044"            /* .......þ.O....0D */
    $"4544 351F 1A10 1014 1410 1135 4445 3021"            /* ED5........5DE0! */
    $"1D1D 1616 1716 161D 211C 1617 1617 1617"            /* ........!....... */
    $"1716 1D1D 1C1D 1C21 3144 382A 1401 0001"            /* .......!1D8*.... */
    $"0100 0100 0001 0001 0100 1545 070A 0E17"            /* ...........E.... */
    $"1720 2445 4439 1401 0100 D301 0001 FD00"            /* . $ED9....Ó...ý. */
    $"0001 FB00 0101 01FE 0005 0101 0001 0100"            /* ..û....þ........ */
    $"FD01 0800 0101 0001 0100 0100 FE01 FC00"            /* ý...........þ.ü. */
    $"0101 01FD 0001 0100 FE01 0100 01FE 0009"            /* ...ý....þ....þ.Æ */
    $"0101 0001 0000 0100 0101 FE00 0701 0000"            /* ..........þ..... */
    $"0101 0001 01FE 0032 0101 0014 1F44 4544"            /* .....þ.2.....DED */
    $"4445 341B 0504 1814 0414 141B 1514 1518"            /* DE4............. */
    $"1519 1814 1015 1014 1111 3444 4544 4544"            /* ..........4DEDED */
    $"2323 2222 4445 4544 310F 0EFD 0F28 0E0F"            /* ##""DEED1..ý.(.. */
    $"3144 4535 101F 101F 151E 1011 1011 1410"            /* 1DE5............ */
    $"1F34 4444 3020 1C17 1716 1C21 1C16 1C21"            /* .4DD0 .....!...! */
    $"1D17 1616 1716 16FE 1723 1C17 1617 1C31"            /* .......þ.#.....1 */
    $"4544 392B 1500 0001 0100 0100 0101 0015"            /* ED9+............ */
    $"4507 0E0E 0F0B 0606 2524 3915 0000 D2FD"            /* E.......%$9...Òý */
    $"0009 0101 0001 0001 0100 0101 FE00 0201"            /* .Æ..........þ... */
    $"0100 FD01 0000 FE01 0400 0001 0100 FE01"            /* ..ý...þ.......þ. */
    $"0100 01FD 0000 01FB 0003 0101 0001 FD00"            /* ...ý...û......ý. */
    $"0101 01FD 0009 0100 0101 0001 0000 0100"            /* ...ý.Æ.......... */
    $"FE01 0200 0001 FE00 1E01 0001 0114 1E2E"            /* þ.....þ......... */
    $"4422 1E19 051E 0504 1905 1805 111E 1518"            /* D".............. */
    $"0119 1815 1115 1510 FE11 2110 1111 1514"            /* ........þ.!..... */
    $"1111 1010 3544 4544 4545 4422 2B44 300E"            /* ....5DEDEED"+D0. */
    $"0E0F 0E0E 4444 3410 111B 1114 15FE 1019"            /* ....DD4......þ.. */
    $"1111 1411 1014 101E 4535 4420 1D16 1716"            /* ........E5D .... */
    $"171D 2021 1D16 1D20 1C17 FC16 101C 1713"            /* .. !... ..ü..... */
    $"1212 1716 161C 3145 4445 392B 1500 FE01"            /* ......1EDE9+..þ. */
    $"0F14 2B31 070E 0B07 060B 1721 2444 1E01"            /* ..+1.......!$D.. */
    $"00CE FC00 0201 0100 FD01 0300 0101 00FE"            /* .Îü.....ý......þ */
    $"01FE 0000 01FB 0007 0100 0100 0001 0100"            /* .þ...û.......... */
    $"FE01 0100 01FD 0001 0100 FE01 FE00 0001"            /* þ....ý....þ.þ... */
    $"FB00 0901 0001 0001 0100 0001 01FD 0006"            /* û.Æ..........ý.. */
    $"0100 0101 0001 01FE 0022 1F2F 4404 051E"            /* .......þ."./D... */
    $"051E 1B05 0419 1515 1E18 1519 1500 1514"            /* ................ */
    $"1014 1915 1415 1814 1110 1111 10FE 110D"            /* .............þ.Â */
    $"1014 1115 101E 1514 1944 4445 2A44 FE0F"            /* .........DDE*Dþ. */
    $"0A44 3545 1510 1411 1110 1011 FE10 1F14"            /* .D5E........þ... */
    $"1010 1114 1E10 1544 3444 211D 1616 1C20"            /* .......D4D!....  */
    $"1D16 1D21 211D 161C 211C 1617 1617 13FE"            /* ...!!...!......þ */
    $"0EFE 1206 1317 1617 161D 31FE 4411 4544"            /* .þ........1þD.ED */
    $"4431 1D0A 0607 0A13 1213 1720 2444 1F01"            /* D1......... $D.. */
    $"D203 0001 0100 FD01 1200 0101 0001 0100"            /* Ò.....ý......... */
    $"0100 0101 0000 0100 0100 0001 FB00 0301"            /* ............û... */
    $"0100 00FE 0103 0001 0100 FD01 0000 FE01"            /* ...þ......ý...þ. */
    $"0100 01FE 0003 0101 0001 FD00 FE01 0900"            /* ...þ......ý.þ.Æ. */
    $"0001 0100 0001 0001 01FC 0021 141F 4522"            /* .........ü.!..E" */
    $"1F04 1919 041A 0418 1F14 1B19 141B 1514"            /* ................ */
    $"1814 1919 1011 1110 1810 1115 1415 FE11"            /* ..............þ. */
    $"0010 FE11 1710 1511 1510 1515 1400 1914"            /* ..þ............. */
    $"452A 450F 4434 4514 1014 1011 14FE 101C"            /* E*E.D4E......þ.. */
    $"1414 1111 1015 151F 1514 151B 4534 4520"            /* ............E4E  */
    $"1D16 1717 1D20 201D 161C 2021 1CFD 1602"            /* .....  ... !.ý.. */
    $"120F 0FFE 0E02 0F0F 0EFD 1316 1212 1316"            /* ...þ.....ý...... */
    $"1717 1613 0B07 060A 1313 1213 1212 1720"            /* ...............  */
    $"2539 00D3 0C00 0001 0100 0101 0001 0000"            /* %9.Ó............ */
    $"0100 FE01 0E00 0001 0100 0101 0001 0100"            /* ..þ............. */
    $"0100 0001 FB00 0101 01FD 0004 0100 0101"            /* ....û....ý...... */
    $"00FE 0106 0000 0101 0000 01FD 0000 01FB"            /* .þ.........ý...û */
    $"0024 0101 0001 0001 0000 0101 0000 141E"            /* .$.............. */
    $"2F44 1F19 1E04 1F1E 1A1A 1919 1814 051A"            /* /D.............. */
    $"1514 1515 1014 19FE 140F 1115 1415 1111"            /* .......þ........ */
    $"1010 1111 1010 1114 1510 FE15 0410 181B"            /* ..........þ..... */
    $"1518 FE15 0944 2A45 4534 3411 1010 1AFE"            /* ..þ.ÆD*EE44....þ */
    $"141F 1511 1510 111E 1414 1515 0415 1915"            /* ................ */
    $"1944 3445 201C 161C 201C 171D 2120 1C17"            /* .D4E ... ...! .. */
    $"1616 FE17 0612 0F0E 0F0E 0F0F FE0E 000F"            /* ..þ.........þ... */
    $"FE0E 010F 0EFD 1203 0A07 0B12 FD13 0712"            /* þ....ý......ý... */
    $"1313 1620 2545 00CF 0600 0101 0000 0101"            /* ... %E.Ï........ */
    $"FE00 0001 FB00 0201 0100 FD01 0300 0101"            /* þ...û.....ý..... */
    $"00FE 01FE 0000 01FB 0001 0101 FD00 0401"            /* .þ.þ...û....ý... */
    $"0001 0100 FE01 FE00 0001 FB00 0A01 0100"            /* ....þ.þ...û..... */
    $"0100 0001 0001 0100 FE01 1F00 141F 4523"            /* ........þ.....E# */
    $"0405 1E1E 041B 1B1E 181F 1805 1419 1911"            /* ................ */
    $"1000 1514 0015 1110 1519 11FE 1000 11FE"            /* ...........þ...þ */
    $"1000 14FE 1002 1114 11FE 1443 1015 1518"            /* ...þ.....þ.C.... */
    $"1411 1A15 1445 4535 4415 1B10 1411 1514"            /* .....EE5D....... */
    $"1411 1415 101B 1118 1105 1510 1E1A 051A"            /* ................ */
    $"0444 2A30 1C17 1716 1C20 211C 1617 1716"            /* .D*0..... !..... */
    $"1617 1613 0E0F 0F0E 0E0F 0F0E 0E0F 0F0E"            /* ................ */
    $"FD0F 130E 0F0B 0706 0A13 1212 1313 1212"            /* ý............... */
    $"1312 1720 2445 00D2 FC00 0301 0100 01FD"            /* ... $E.Òü......ý */
    $"0009 0101 0000 0100 0100 0001 FB00 0101"            /* .Æ..........û... */
    $"01FE 000C 0100 0001 0100 0001 0001 0001"            /* .þ.............. */
    $"01FE 0004 0101 0001 01FD 0016 0100 0101"            /* .þ.......ý...... */
    $"0001 0100 0100 0101 0000 0100 0100 0001"            /* ................ */
    $"1E2E 44FE 040A 0505 181E 1E04 191E 1815"            /* ..Dþ............ */
    $"14FE 181F 1414 1515 1810 111B 1110 1111"            /* .þ.............. */
    $"1011 1010 1110 1111 1001 1114 1110 1915"            /* ................ */
    $"1518 1810 FE14 4815 1015 1444 2F34 1415"            /* ....þ.H....D/4.. */
    $"1415 1510 141A 101E 1815 1110 1B10 151B"            /* ................ */
    $"051A 1E1A 1A14 352B 4420 1C16 1D20 1D17"            /* ......5+D ... .. */
    $"1716 1617 1716 1713 0F0E 0E0F 0F0E 0F0F"            /* ................ */
    $"0E0E 0F0E 0F0E 0F0F 0E0A 0706 0A12 1213"            /* ................ */
    $"FB12 0613 1316 2125 4515 CE00 00FE 0104"            /* û.....!%E.Î..þ.. */
    $"0001 0001 00FE 0101 0001 FD00 0001 FB00"            /* .....þ....ý...û. */
    $"0201 0100 FD01 0300 0101 00FE 01FE 0000"            /* ....ý......þ.þ.. */
    $"01FB 00FE 0101 0001 FE00 0301 0100 01FD"            /* .û.þ....þ......ý */
    $"0032 0101 0000 0100 0100 0001 0000 141E"            /* .2.............. */
    $"4422 051F 1A1B 1819 1F18 1919 1414 151A"            /* D".............. */
    $"1518 1515 1915 1414 1B14 1511 1014 1011"            /* ................ */
    $"1010 1111 10FD 1132 1011 1114 1010 1E15"            /* .....ý.2........ */
    $"1415 1B19 1814 1518 1035 2F44 1411 1410"            /* .........5/D.... */
    $"1414 1F10 1119 101A 1410 1E04 1105 1A05"            /* ................ */
    $"0419 0515 1A1B 441E 301D 17FD 1601 1716"            /* ......D.0..ý.... */
    $"FE17 0812 130E 0F0E 0F0F 0E0E FE0F 0D0E"            /* þ...........þ.Â. */
    $"0F0F 0E0F 0E0A 0606 0B13 1312 13FD 1200"            /* .............ý.. */
    $"13FD 1204 1620 2545 1ED4 FD01 0000 FE01"            /* .ý... %E.Ôý...þ. */
    $"0400 0100 0100 FE01 0400 0001 0000 FE01"            /* ......þ.......þ. */
    $"1100 0001 0100 0101 0000 0100 0100 0101"            /* ................ */
    $"0001 01FE 00FE 010C 0001 0100 0001 0100"            /* ...þ.þ.......... */
    $"0001 0001 00FE 0106 0000 0101 0000 01FC"            /* .....þ.........ü */
    $"006A 1E2F 4504 041F 0519 1E15 1F05 141F"            /* .j./E........... */
    $"141F 1415 1518 191B 1114 1814 0114 1810"            /* ................ */
    $"1014 1011 1115 1010 1110 1011 1114 1015"            /* ................ */
    $"101B 1011 1915 1418 1014 1019 1510 1044"            /* ...............D */
    $"2E45 1415 1B1A 111A 1411 1011 111B 181A"            /* .E.............. */
    $"1118 041A 1B14 1814 041A 041B 451E 451C"            /* ............E.E. */
    $"1617 1617 1716 1717 1312 0E0E 0FFB 0E02"            /* .............û.. */
    $"0F0F 0EFD 0F0E 0A07 070B 1213 122D 3645"            /* ...ý.........-6E */
    $"4537 2C12 13FE 1205 1316 1620 2438 D203"            /* E7,..þ..... $8Ò. */
    $"0001 0100 FD01 0000 FE01 0000 FE01 0300"            /* ....ý...þ...þ... */
    $"0101 00FE 01FE 0000 01FB 0003 0101 0001"            /* ...þ.þ...û...... */
    $"FD00 0201 0100 FD01 1000 0101 0001 0100"            /* ý.....ý......... */
    $"0100 0101 0000 0100 0100 FE01 1700 0001"            /* ..........þ..... */
    $"0100 0015 1E44 221E 181A 151F 1419 041E"            /* .....D"......... */
    $"1918 151B 1EFE 15FE 1409 0110 141A 1014"            /* .....þ.þ.Æ...... */
    $"0011 1110 FD11 0010 FE11 3710 1110 1510"            /* ....ý...þ.7..... */
    $"1115 1114 1815 101E 141B 141A 141A 1814"            /* ................ */
    $"452F 2E14 1015 111E 1511 1015 1115 1B14"            /* E/.............. */
    $"1919 1B04 101A 1404 1B1F 0405 0434 1F44"            /* .............4.D */
    $"211D 16FD 1708 1613 130F 0E0F 0E0F 0EFE"            /* !..ý...........þ */
    $"0F09 0E0E 0F0F 0E0E 0B06 060A FE12 0A25"            /* .Æ..........þ..% */
    $"3745 3C3E 4545 4437 2513 FD12 0316 2125"            /* 7E<>EED7%.ý...!% */
    $"44CF FE00 0101 00FE 010E 0000 0100 0001"            /* DÏþ....þ........ */
    $"0100 0001 0001 0000 01FB 00FE 0101 0001"            /* .........û.þ.... */
    $"FE00 1C01 0100 0100 0001 0001 0100 0101"            /* þ............... */
    $"0001 0001 0100 0001 0001 0000 0100 0101"            /* ................ */
    $"FB00 2601 1F2E 4518 1F1B 051E 1415 041A"            /* û.&...E......... */
    $"1B19 1810 1518 1514 151B 1514 1814 1014"            /* ................ */
    $"1111 1010 1110 1110 0111 FD10 0111 10FE"            /* ..........ý....þ */
    $"1138 1015 1410 1415 1514 1A1B 1811 181B"            /* .8.............. */
    $"1510 2E2B 441E 1415 1514 1515 1018 1419"            /* ...+D........... */
    $"1B1F 1514 1815 1404 1904 1404 1A1A 1E05"            /* ................ */
    $"1B44 1E31 1C17 1617 1713 13FD 0EFE 0FFC"            /* .D.1.......ý.þ.ü */
    $"0E1E 0F0F 0E0B 0706 0A12 1313 1224 363C"            /* .............$6< */
    $"3F44 4545 4445 4436 2512 1313 1217 2125"            /* ?DEEDED6%.....!% */
    $"44CE 0D00 0101 0000 0100 0100 0101 0000"            /* DÎÂ............. */
    $"01FD 0000 01FB 00FE 0101 0001 FE00 0301"            /* .ý...û.þ....þ... */
    $"0100 01FD 0001 0101 FD00 0101 00FE 0101"            /* ...ý....ý....þ.. */
    $"0001 FD00 0001 FB00 FE01 0E00 0101 151E"            /* ..ý...û.þ....... */
    $"4523 0418 0518 1F1A 181F FD18 0614 141F"            /* E#........ý..... */
    $"1518 1415 FE14 0C15 1510 1514 1411 1011"            /* ....þ........... */
    $"1110 1011 FE10 0511 1110 1511 15FE 1041"            /* ....þ........þ.A */
    $"1110 1011 1519 1415 1511 141B 1410 442A"            /* ..............D* */
    $"451E 1010 1A10 101F 1518 1405 1B19 1A01"            /* E............... */
    $"051E 1819 1A1B 1A15 051B 041B 1A34 2A44"            /* .............4*D */
    $"2116 1612 120E 0E0F 0F0E 0F0E 0E0F 0E0F"            /* !............... */
    $"0F0E FE0F 030A 060A 13FC 120B 363D 4544"            /* ..þ......ü..6=ED */
    $"4445 4445 4445 4536 FE12 0413 1621 2545"            /* DEDEDEE6þ....!%E */
    $"CE09 0000 0100 0001 0100 0101 FE00 FD01"            /* ÎÆ..........þ.ý. */
    $"0500 0001 0000 01FB 00FE 0101 0001 FE00"            /* .......û.þ....þ. */
    $"0201 0100 FD01 0500 0101 0000 01FE 0001"            /* ....ý........þ.. */
    $"0101 FD00 0101 00FD 011D 0000 0100 001F"            /* ..ý....ý........ */
    $"2E45 051E 141E 1E14 1805 1504 1514 1B1F"            /* .E.............. */
    $"1F1E 1018 1810 1515 FE14 0A1A 1114 1515"            /* ........þ....... */
    $"1110 1411 1010 FE11 4114 1110 1014 1111"            /* ......þ.A....... */
    $"1011 1010 111A 1B15 1E1A 1A11 1510 1115"            /* ................ */
    $"1445 2244 1114 1511 1518 1E04 1E14 1515"            /* .E"D............ */
    $"0414 0404 191E 1B05 1F04 1B00 041A 1B1F"            /* ................ */
    $"1A44 2F30 1712 0F0F 0E0E 0FFD 0E00 0FFB"            /* .D/0.......ý...û */
    $"0E0D 0B07 060B 1212 1312 1313 2C45 3D45"            /* .Â..........,E=E */
    $"FE44 0045 FC44 072C 1313 1216 2024 45CC"            /* þD.EüD.,.... $EÌ */
    $"0300 0101 00FE 01FE 0000 01FB 0004 0100"            /* .....þ.þ...û.... */
    $"0001 01FE 0000 01FE 0000 01FD 0011 0100"            /* ...þ...þ...ý.... */
    $"0101 0001 0000 0101 0001 0001 0000 0101"            /* ................ */
    $"FB00 0001 FB00 FE01 0900 1E45 2304 051B"            /* û...û.þ.Æ..E#... */
    $"1904 1FFE 1819 1511 1914 1518 1910 151B"            /* ...þ............ */
    $"1410 1110 141E 1511 1511 1010 1110 1011"            /* ................ */
    $"FB10 0311 1110 15FE 1156 1011 1B1A 1015"            /* û......þ.V...... */
    $"111A 141A 1B1A 1010 141E 4423 2F10 141E"            /* ..........D#/... */
    $"1F15 1415 1518 041A 1819 1A1B 1F18 1A15"            /* ................ */
    $"0504 041B 1B1A 1E1B 1B1E 4445 130A 0A0B"            /* ..........DE.... */
    $"0A0F 0E0F 0F0E 0F0E 0E0F 0E0F 0F0A 0707"            /* ................ */
    $"0B12 1213 1312 1213 1237 3C44 4544 453D"            /* .........7<DEDE= */
    $"3CFC 4407 3713 1213 1631 3145 D91F 0000"            /* <üD.7....11EÙ... */
    $"0100 0001 0100 0001 0001 0001 0100 0101"            /* ................ */
    $"0001 0001 0100 0100 0001 0001 0100 FE01"            /* ..............þ. */
    $"0900 0001 0100 0100 0001 00FE 0106 0000"            /* Æ..........þ.... */
    $"0101 0001 01FE 002D 0101 0001 0100 0001"            /* .....þ.-........ */
    $"0015 1E45 1F04 1A05 1A1E 1A18 1F14 1418"            /* ...E............ */
    $"1414 1011 1B14 1814 1815 1415 0110 1014"            /* ................ */
    $"1910 1011 1110 FD11 0010 FE11 0410 1110"            /* ......ý...þ..... */
    $"1510 FE11 0610 1B10 1A10 141F FE14 1D10"            /* ..þ.........þ... */
    $"1414 1115 2F2A 451B 1114 1515 1015 1804"            /* ..../*E......... */
    $"1818 051F 0404 051A 1504 1B1F 04FE 1B06"            /* .............þ.. */
    $"1A1A 1E1B 3430 16FE 1C03 1D1D 0B0A FE0B"            /* ....40.þ......þ. */
    $"0A0E 0F0F 0E0E 0B06 070A 1213 FB12 1613"            /* ............û... */
    $"2D44 3C44 443D 3835 3538 3C44 4545 442D"            /* -D<DD=8558<DEED- */
    $"1331 3007 0644 CE00 00FE 0106 0001 0001"            /* .10..DÎ..þ...... */
    $"0001 01FD 0006 0100 0101 0001 01FE 0004"            /* ...ý.........þ.. */
    $"0101 0001 01FE 00FD 0105 0000 0100 0001"            /* .....þ.ý........ */
    $"FB00 0901 0100 0101 0001 0001 01FD 0023"            /* û.Æ..........ý.# */
    $"0100 011F 2E44 1904 0418 1B15 1818 151E"            /* .....D.......... */
    $"191E 141F 141E 1418 1010 1B19 1814 1010"            /* ................ */
    $"1114 1011 FB10 0211 0111 FC10 FE11 2B10"            /* ....û.....ü.þ.+. */
    $"1415 1A1A 1515 1015 191B 151A 1B11 1014"            /* ................ */
    $"111B 442A 4505 041B 1018 051E 1515 0518"            /* ..D*E........... */
    $"1F1A 1418 0405 041F 051E 04FD 1A06 0535"            /* ...........ý...5 */
    $"3017 0E0F 0FFE 0E1D 0F1C 1C1D 1D1C 0A0B"            /* 0....þ.......... */
    $"0E0B 0607 0B12 1213 1213 1213 1312 1313"            /* ................ */
    $"373C 4444 4538 FD34 0B38 4545 4445 3731"            /* 7<DDE8ý4.8EEDE71 */
    $"0606 212D 44CE 0600 0100 0100 0101 FD00"            /* ..!-DÎ........ý. */
    $"0101 00FE 0109 0000 0100 0001 0100 0101"            /* ...þ.Æ.......... */
    $"FE00 FD01 0500 0001 0000 01FB 00FE 0104"            /* þ.ý........û.þ.. */
    $"0000 0101 00FE 0101 0001 FE00 FE01 1E00"            /* .....þ....þ.þ... */
    $"1E45 221A 1B05 1B04 1B14 1518 1F15 1E14"            /* .E"............. */
    $"1E15 1B1E 151B 1811 101B 0110 1415 FB10"            /* ..............û. */
    $"0111 11FE 1002 1110 10FD 113D 1010 1110"            /* ...þ.....ý.=.... */
    $"141B 1410 1A14 1A14 1B1B 1514 101A 1014"            /* ................ */
    $"1B15 452E 451A 1B10 1505 1904 1819 1E1A"            /* ..E.E........... */
    $"1919 1F1E 1A1E 0404 1F05 1E1F 1B1A 3430"            /* ..............40 */
    $"170F 0E0E 0F0E 0F0E 0E0F FC0E 051C 1D07"            /* ..........ü..... */
    $"060B 13FE 120B 1313 1213 1212 1312 1345"            /* ...þ...........E */
    $"3C44 FE45 0434 3535 3435 FD44 0645 0721"            /* <DþE.45545ýD.E.! */
    $"2021 2C44 D803 0001 0100 FE01 0C00 0001"            /*  !,DØ.....þ..... */
    $"0100 0100 0001 0001 0100 FE01 0500 0001"            /* ..........þ..... */
    $"0100 00FE 0103 0000 0100 FE01 FE00 0101"            /* ...þ......þ.þ... */
    $"00FE 01FE 0001 0100 FE01 FE00 0001 FD00"            /* .þ.þ....þ.þ...ý. */
    $"2114 1E44 051E 0504 1A18 041F 1F1B 1415"            /* !..D............ */
    $"1E1E 1419 191E 1B14 1014 001F 1518 1014"            /* ................ */
    $"1011 10FE 1102 1011 14FE 1018 1110 1011"            /* ...þ.....þ...... */
    $"1511 1011 111B 1010 1511 141A 1B1A 141A"            /* ................ */
    $"1014 1411 15FE 1422 1E45 2E2F 051A 1B1B"            /* .....þ.".E./.... */
    $"1418 1815 0505 1E1F 1515 0405 191E 1A1E"            /* ................ */
    $"0405 0435 3117 0F0E 0E0F 0EFE 0F0E 0E0E"            /* ...51......þ.... */
    $"0F0F 0E0E 0F0A 0606 200A 1213 13FD 120D"            /* ........ ....ý.Â */
    $"1312 1213 1212 2C44 3C44 453D 4432 FE33"            /* ......,D<DE=D2þ3 */
    $"0B32 3D45 4445 452D 2120 212D 44D3 FD01"            /* .2=EDEE-! !-DÓý. */
    $"0500 0101 0000 01FD 0000 01FB 00FE 0110"            /* .......ý...û.þ.. */
    $"0000 0101 0001 0100 0100 0001 0001 0100"            /* ................ */
    $"00FE 0103 0001 0100 FE01 FE00 2901 0001"            /* .þ......þ.þ.)... */
    $"0000 0100 001F 2E45 1B04 1A18 0404 1A15"            /* .......E........ */
    $"1B14 151E 1818 1A15 1918 1518 1115 1010"            /* ................ */
    $"1414 1110 1511 10FE 1106 1010 1511 1010"            /* .......þ........ */
    $"11FD 1002 1110 1AFE 1035 1411 1115 1A10"            /* .ý.....þ.5...... */
    $"1B1B 1415 1510 151B 1B11 1011 3534 4515"            /* ............54E. */
    $"1E05 1E05 0504 141B 1A05 1A04 051E 041E"            /* ................ */
    $"041E 1A05 1B34 3116 0E0F 0E0F 0F0E 0E0F"            /* .....41......... */
    $"FE0E 0A0F 0F0E 0F0A 0607 0A13 1D0A FD13"            /* þ.............ý. */
    $"0012 FE13 0112 13FE 1201 363D FE44 023C"            /* ..þ....þ..6=þD.< */
    $"3E3C FE33 0B32 3545 4544 4537 2021 202C"            /* ><þ3.25EEDE7 ! , */
    $"44D4 0300 0101 00FD 0102 0000 01FB 0007"            /* DÔ.....ý.....û.. */
    $"0101 0001 0001 0000 FE01 0400 0100 0100"            /* ........þ....... */
    $"FE01 0400 0001 0100 FE01 0100 01FD 0000"            /* þ.......þ....ý.. */
    $"01FB 0019 0101 0000 1F44 2204 051B 0405"            /* .û.......D"..... */
    $"1A1E 1F18 1915 191A 1415 1514 1911 FE10"            /* ..............þ. */
    $"0611 1114 1115 1015 FE11 1010 1511 1110"            /* ........þ....... */
    $"1111 1010 1111 1010 1110 1110 FE11 1C10"            /* ............þ... */
    $"1411 1414 1B1B 1A14 1B10 1B10 1115 1A14"            /* ................ */
    $"1544 3444 0405 0404 1E1E 1404 FE05 011E"            /* .D4D........þ... */
    $"05FE 0411 0505 1A1B 3430 160E 0F0F 0E0E"            /* .þ......40...... */
    $"0F0E 0F0E 0E0F FD0E 0C0A 0607 0A12 1312"            /* ......ý......... */
    $"161D 0A13 1312 FE13 0112 12FE 1317 1245"            /* ......þ....þ...E */
    $"3C44 4445 3D3E 4433 3233 3233 4545 4444"            /* <DDE=>D32323EEDD */
    $"4520 2021 2D44 CEFE 0109 0000 0101 0000"            /* E  !-DÎþ.Æ...... */
    $"0100 0100 FE01 0100 01FD 0000 01FB 0007"            /* ....þ....ý...û.. */
    $"0101 0001 0000 0100 FE01 0600 0001 0100"            /* ........þ....... */
    $"0001 FB00 FE01 2600 0001 011E 4505 051E"            /* ..û.þ.&.....E... */
    $"0514 1818 1B1F 1A19 1410 1514 1511 1415"            /* ................ */
    $"191A 1010 1111 1015 1114 1410 1011 FB10"            /* ..............û. */
    $"0311 1110 10FE 1123 1011 1110 1115 1111"            /* .....þ.#........ */
    $"101B 1B10 151B 151E 1415 1510 1115 1514"            /* ................ */
    $"1415 4534 4404 1E1F 1E1A 151A FE04 0B1A"            /* ..E4D.......þ... */
    $"1E1F 1F05 1E04 1F35 3017 0FFD 0E01 0F0E"            /* .......50..ý.... */
    $"FD0F 070E 0E0F 0E0A 0706 0AFD 1207 1313"            /* ý..........ý.... */
    $"200B 1212 1312 FE13 0112 13FE 1207 443D"            /*  .....þ....þ..D= */
    $"4444 3C3E 3E32 FE2F 0B2E 2E3D 4544 4545"            /* DD<>>2þ/...=EDEE */
    $"2120 2530 45D1 0200 0101 FE00 0A01 0100"            /* ! %0EÑ....þ..... */
    $"0101 0001 0001 0100 FE01 0700 0001 0100"            /* ........þ....... */
    $"0001 00FE 01FC 0003 0101 0001 FD00 0801"            /* ...þ.ü......ý... */
    $"0100 0100 0100 0100 FE01 0D00 0115 1E44"            /* ........þ.Â....D */
    $"051E 1918 1515 0415 05FE 1412 1915 1415"            /* .........þ...... */
    $"1514 1410 1415 1411 1510 101A 1415 14FC"            /* ...............ü */
    $"1003 1115 1110 FE11 3310 1111 1010 111A"            /* ......þ.3....... */
    $"1110 1015 1010 1A10 141A 1B15 1A14 101B"            /* ................ */
    $"1114 1115 1414 1044 3544 051B 1E1B 1B1F"            /* .......D5D...... */
    $"041A 0405 1E1A 041E 1A04 3531 16FD 0F03"            /* ..........51.ý.. */
    $"0E0F 0F0E FE0F 090E 0E0F 0F0A 0707 0A12"            /* ....þ.Æ......... */
    $"12FD 1305 1212 210A 1213 FB12 FE13 172C"            /* .ý....!...û.þ.., */
    $"443F 4544 3D23 2A32 2E2E 2F2E 2F35 4545"            /* D?ED=#*2.././5EE */
    $"4444 2120 2431 45D8 0201 0001 FC00 0301"            /* DD! $1EØ....ü... */
    $"0100 01FD 0021 0101 0001 0001 0001 0000"            /* ...ý.!.......... */
    $"0101 0001 0001 0100 0001 0001 0001 0000"            /* ................ */
    $"0101 0001 0001 0001 FE00 0001 FE00 1E15"            /* ........þ...þ... */
    $"2E45 1A1F 0404 191F 1815 0414 1514 0418"            /* .E.............. */
    $"141E 1814 1919 1801 1101 1400 1110 FE11"            /* ..............þ. */
    $"FE10 0811 1110 1110 1110 1011 FE10 2F00"            /* þ...........þ./. */
    $"1010 1110 111A 1015 1B1A 1114 1114 151E"            /* ................ */
    $"1B1A 151A 1414 1A15 1510 1F44 3435 1E05"            /* ...........D45.. */
    $"1F1E 1B04 1B1E 0405 1B1E 041F 3430 16FE"            /* ............40.þ */
    $"0E04 0F0E 0E0F 0FFE 0E00 0FFE 0E12 0B06"            /* .......þ...þ.... */
    $"070A 1312 1312 1213 1312 1312 210A 1213"            /* ............!... */
    $"13FD 1213 1313 1213 363C 4444 4523 2A2F"            /* .ý......6<DDE#*. */
    $"2E32 2E2E 2F2F 2E45 FE44 042C 2125 3045"            /* .2..//.EþD.,!%0E */
    $"CFFD 0003 0101 0001 FD00 0301 0100 01FD"            /* Ïý......ý......ý */
    $"0003 0101 0001 FD00 0301 0100 01FD 0003"            /* ......ý......ý.. */
    $"0101 0001 FD00 0301 0100 01FD 0023 0101"            /* ....ý......ý.#.. */
    $"0001 1E38 3804 0505 0405 1A04 1804 1115"            /* ...88........... */
    $"1819 1A1A 1018 1F15 1415 1014 0010 1115"            /* ................ */
    $"1011 FD10 0311 1100 11FE 1004 1411 1110"            /* ..ý......þ...... */
    $"11FD 101B 1111 1011 1410 101A 111B 1A1B"            /* .ý.............. */
    $"1A14 1A1E 1111 1011 1014 1014 1535 3445"            /* .............54E */
    $"FD04 0E05 0504 1F1E 051E 0434 4431 160E"            /* ý..........4D1.. */
    $"0F0F FD0E 010F 0EFE 0F16 0E0E 0F0B 0607"            /* ..ý....þ........ */
    $"0B13 1212 1313 1213 1312 1313 1220 0A13"            /* ............. .. */
    $"13FD 120F 1312 131D 3044 3C45 4444 2A2F"            /* .ý......0D<EDD*. */
    $"2F33 322B FE2A 002B FD44 042C 2025 3045"            /* /32+þ*.+ýD., %0E */
    $"D100 00FE 010C 0001 0100 0001 0001 0000"            /* Ñ..þ............ */
    $"0100 00FE 0100 00FE 010E 0000 0100 0001"            /* ...þ...þ........ */
    $"0100 0001 0001 0000 01FB 0003 152B 3839"            /* .........û...+89 */
    $"FE45 1D44 4545 4445 3505 041E 041B 1E04"            /* þE.DEEDE5....... */
    $"1A18 181E 1511 111E 1B14 1814 1915 1019"            /* ................ */
    $"14FE 1009 1B15 1010 1110 1110 1415 FB10"            /* .þ.Æ..........û. */
    $"FE11 2E10 1011 1110 111B 1014 101B 1B1A"            /* þ............... */
    $"111F 1A10 1F14 1B14 1B15 1A15 1115 1014"            /* ................ */
    $"4535 441A 1B18 051E 1A1B 0434 4444 3016"            /* E5D........4DD0. */
    $"0F0F FD0E 040F 0E0F 0F0E FE0F 060E 0E0F"            /* ..ý.......þ..... */
    $"0B06 0A13 FD12 0013 FB12 0313 1321 0AFE"            /* ....ý...û....!.þ */
    $"131F 1213 1312 1C31 3007 443E 4544 442F"            /* .......10.D>EDD/ */
    $"2F33 383D 2B2B 2A2A 2B44 4445 4536 202D"            /* /38=++**+DDEE6 - */
    $"3039 D002 0000 01FB 0002 0101 00FE 0104"            /* 09Ð....û.....þ.. */
    $"0000 0101 00FD 0100 00FE 0101 0001 FD00"            /* .....ý...þ....ý. */
    $"0001 FE00 0D14 2A38 3945 4444 300F 0704"            /* ..þ.Â.*89EDD0... */
    $"0505 04FD 0503 0405 3145 FC44 1145 3515"            /* ...ý....1EüD.E5. */
    $"1E14 1915 1A1E 1B14 1511 1514 1010 15FB"            /* ...............û */
    $"1000 11FE 1003 0111 1510 FE11 1410 1011"            /* ...þ......þ..... */
    $"1010 111B 1010 1110 1114 1B11 1A14 151A"            /* ................ */
    $"1B1E FE1B 0F10 1514 1010 1115 1111 4435"            /* ..þ...........D5 */
    $"441E 1A1B 34FE 4401 3016 FE0F 010E 0FFE"            /* D...4þD.0.þ....þ */
    $"0E02 0F0F 0EFD 0F09 0E0E 0F0E 0A06 060A"            /* .....ý.Æ........ */
    $"1213 FE12 0013 FE12 FE13 1B12 1312 1D0A"            /* ..þ...þ.þ....... */
    $"1313 1213 121C 3030 0607 0A44 3E44 4544"            /* ......00...D>DED */
    $"2E32 383F 3D2A 2BFE 2A08 3445 4544 4520"            /* .28?=*+þ*.4EEDE  */
    $"2C44 1ECC 0301 0100 01FD 0003 0101 0001"            /* ,D.Ì.....ý...... */
    $"FD00 0301 0100 01FD 0003 0101 0001 FD00"            /* ý......ý......ý. */
    $"1301 0100 152A 3830 0E0F 0704 0504 0406"            /* .....*80........ */
    $"0607 0706 07FD 0603 0707 0607 FD06 0307"            /* .....ý......ý... */
    $"0716 31FD 440B 4545 4435 1414 1010 1111"            /* ..1ýD.EED5...... */
    $"1001 FD10 0311 1110 15FD 1403 1111 1011"            /* ..ý......ý...... */
    $"FD10 0311 1114 11FE 1015 1415 1510 1B1A"            /* ý......þ........ */
    $"1B1A 1B14 1010 141A 1515 1410 1014 151E"            /* ................ */
    $"FE45 0944 4530 0B0A 0B0F 0E0F 0FFD 0E00"            /* þEÆDE0.......ý.. */
    $"0FFB 0E11 0F0F 0E0F 0E0A 0706 0B13 1312"            /* .û.............. */
    $"1213 1312 1213 FB12 2613 1316 1C0B 1212"            /* ......û.&....... */
    $"1C31 3106 060B 1217 4445 4544 2E32 383F"            /* .11.....DEED.28? */
    $"3E45 2B26 2627 262E 4444 4544 212D 4514"            /* >E+&&'&.DDED!-E. */
    $"72FD 0003 0100 0001 E900 0514 2A38 3830"            /* rý......é...*880 */
    $"06FE 04FC 06E4 0E01 1630 FA44 0034 FE10"            /* .þ.ü.ä...0úD.4þ. */
    $"0114 00FD 1000 14F6 100E 141A 101A 1010"            /* ...ý...ö........ */
    $"1414 1A1A 101A 141A 1EFD 1403 1A14 1E34"            /* .........ý.....4 */
    $"FD44 0324 160E 16FC 1CFB 0AF5 0E03 0A06"            /* ýD.$...ü.û.õ.... */
    $"060A ED12 0720 0A1C 3030 0606 0AFE 1200"            /* ..í.. ..00...þ.. */
    $"16FC 4400 38FE 3E01 442E FC26 FD44 0324"            /* .üD.8þ>.D.ü&ýD.$ */
    $"3044 0044 E400 0714 2A38 380E 0604 04FD"            /* 0D.Dä...*88....ý */
    $"06D6 0E01 1630 D844 0130 16F4 0EFB 1CFE"            /* .Ö...0ØD.0.ô.û.þ */
    $"0AFA 0E03 0A06 060A EC12 061C 2020 3006"            /* .ú......ì...  0. */
    $"060A FC12 0016 FC44 FD3E 0144 2EFC 2607"            /* ..ü...üDý>.D.ü&. */
    $"443E 4444 2430 4400 3BE6 0006 1438 380E"            /* D>DD$0D.;æ...88. */
    $"0604 04FE 0692 0EFE 1C00 0AFD 0E03 0A06"            /* ...þ..þ...ý.... */
    $"060A EC12 061C 2430 3006 060A FA12 0016"            /* ..ì...$00...ú... */
    $"FC44 0022 FE3E 0144 2AFC 2207 443E 4444"            /* üD."þ>.D*ü".D>DD */
    $"2C30 3800 3FE8 0005 1438 300E 0604 FE06"            /* ,08.?è...80...þ. */
    $"8D0E 070A 1C0A 0E0A 0606 0AEC 1206 1C30"            /* ..........ì...0 */
    $"3006 060A 0AFE 1201 2020 FD12 0016 FD44"            /* 0....þ..  ý...ýD */
    $"062E 2A2A 3E3E 442A FD22 0826 443E 4444"            /* ..**>>D*ý".&D>DD */
    $"2C44 1E00 42EA 0007 142A 300E 0604 0606"            /* ,D..Bê...*0..... */
    $"EE0E FE0A A60E FB0A 0506 061C 0A06 0AEC"            /* î.þ.¦.û........ì */
    $"120D 1C30 3006 060A 1220 0A12 2030 3A06"            /* .Â.00.... .. 0:. */
    $"FC12 FC44 052E 2A38 3E44 26FD 2208 3444"            /* ü.üD..*8>D&ý".4D */
    $"3E44 3630 4400 0047 EB00 0614 380E 0604"            /* >D60D..Gë...8... */
    $"0606 EE0E 040A 0A06 060A AE0E F90A FB06"            /* ..î.......®.ù.û. */
    $"FE0A 011C 0AED 1205 1C30 3006 060A FE12"            /* þ....í...00...þ. */
    $"0620 2030 3A44 4406 FC12 FC44 052E 2A22"            /* .  0:DD.ü.üD..*" */
    $"3E3C 22FD 1E08 443C 4444 2C30 3800 004C"            /* ><"ý..D<DD,08..L */
    $"ED00 0614 2A30 0E04 0606 EE0E 050A 0A06"            /* í...*0....î..... */
    $"060A 0AB3 0EFB 0AF9 06FB 0AFE 1201 200A"            /* ...³.û.ù.û.þ.. . */
    $"EF12 051C 3030 0606 0AFE 1202 2030 3AFD"            /* ï...00...þ.. 0:ý */
    $"4401 3E06 FC12 0036 FD44 042E 2E2A 223C"            /* D.>.ü..6ýD...*"< */
    $"FC1E 0844 3C44 442C 441E 0000 4DEE 0005"            /* ü..D<DD,D...Mî.. */
    $"142A 3004 0606 ED0E 040A 0606 0A0A DF0E"            /* .*0...í.......ß. */
    $"FE12 D90E FE0A FB06 F90A F812 0120 0AF2"            /* þ.Ù.þ.û.ù.ø.. .ò */
    $"1206 1C24 3030 0606 0AFE 1202 2024 3AFC"            /* ...$00...þ.. $:ü */
    $"4402 3E3E 06FC 1200 2CFD 4400 32FE 2EFB"            /* D.>>.ü..,ýD.2þ.û */
    $"1E05 443C 4444 3038 FE00 52EF 0004 1438"            /* ..D<DD08þ.Rï...8 */
    $"0E04 06ED 0E04 0A0A 060A 0ADF 0E04 1212"            /* ...í.......ß.... */
    $"1616 12DC 0EFE 0AFE 06FB 0AF0 1201 1C0A"            /* ...Ü.þ.þ.û.ð.... */
    $"F412 021C 3030 FE06 FD12 0420 2030 363A"            /* ô...00þ.ý..  06: */
    $"FD44 FE3E 0006 FC12 002C FD44 0338 322E"            /* ýDþ>..ü..,ýD.82. */
    $"32FC 1A02 1E44 3CFE 4400 1EFE 0057 F100"            /* 2ü...D<þD..þ.Wñ. */
    $"0514 2A30 0406 06ED 0E03 0A06 060A E00E"            /* ..*0...í......à. */
    $"FE12 0316 1612 12DD 0E01 0A0A FE06 FE0A"            /* þ......Ý....þ.þ. */
    $"EA12 0216 1C0A F712 051C 3030 0606 0AFD"            /* ê.....÷...00...ý */
    $"1206 2020 2C2C 3030 3AFE 44FD 3E00 06FC"            /* ..  ,,00:þDý>..ü */
    $"1200 24FD 4403 3C38 3232 FC1A 0534 3C44"            /* ..$ýD.<822ü..4<D */
    $"3C44 38FD 0056 F200 0414 380E 0406 ED0E"            /* <D8ý.Vò...8...í. */
    $"040A 0A06 0A0A E10E 0112 12FE 1601 1212"            /* ......á....þ.... */
    $"DD0E 030A 0A06 06FE 0AE6 1201 200A F912"            /* Ý......þ.æ.. .ù. */
    $"051C 3030 0606 0AFD 1201 2020 FE24 052C"            /* ..00...ý..  þ$., */
    $"2C30 3A44 44FC 3E00 06FB 12FC 4402 3C38"            /* ,0:DDü>..û.üD.<8 */
    $"32FC 1A05 443C 4434 441E FD00 52F3 0004"            /* 2ü..D<D4D.ý.Ró.. */
    $"1430 0406 06ED 0E03 0A06 060A E10E 0312"            /* .0...í......á... */
    $"1216 16FE 12DC 0E04 0A06 060A 0AE3 1201"            /* ...þ.Ü.......ã.. */
    $"200A FC12 061C 2430 3006 060A FE12 FD20"            /*  .ü...$00...þ.ý  */
    $"FE1C 0520 242C 3036 44FB 3E00 06FB 1200"            /* þ.. $,06Dû>..û.. */
    $"36FD 4401 3C38 FB1A 0344 3C44 1EFB 005A"            /* 6ýD.<8û..D<D.û.Z */
    $"F500 0414 2A30 0406 EC0E 030A 060A 0AE2"            /* õ...*0..ì......â */
    $"0E05 1212 1616 1212 DB0E 040A 0A06 0A0A"            /* ........Û....... */
    $"FE12 012C 36FE 4402 360A 0AEC 1201 200A"            /* þ..,6þD.6..ì.. . */
    $"FE12 021C 3030 FE06 FD12 0120 20F9 1C03"            /* þ...00þ.ý..  ù.. */
    $"202C 3036 FA3E 0006 FB12 002C FD44 013C"            /*  ,06ú>..û..,ýD.< */
    $"44FC 1403 343C 4438 FA00 5EF6 0004 1438"            /* Dü..4<D8ú.^ö...8 */
    $"0E04 06ED 0E03 0A0A 060A E10E 0412 1616"            /* ...í......á..... */
    $"1212 DA0E 030A 0606 0AFE 1205 2C36 443C"            /* ..Ú......þ..,6D< */
    $"3C3E FE44 0236 0A0A EE12 0820 0A1C 2430"            /* <>þD.6..î.. ..$0 */
    $"3006 060A FD12 0120 20FD 1CFE 1606 1C1C"            /* 0...ý..  ý.þ.... */
    $"2020 2830 36FB 3E01 3C06 FB12 0024 FC44"            /*   (06û>.<.û..$üD */
    $"FB14 0344 3C44 1EFA 0058 F700 0414 380E"            /* û..D<D.ú.X÷...8. */
    $"0406 ED0E 030A 0606 0AE2 0E04 1212 1612"            /* ..í......â...... */
    $"12DA 0E0B 0A0A 060A 0A12 122C 3644 3C3C"            /* .Ú.........,6D<< */
    $"F944 012C 0AEF 1202 2020 30FE 06FC 1201"            /* ùD.,.ï..  0þ.ü.. */
    $"2020 FE1C FA16 001C FE28 012C 36FC 3E02"            /*   þ.ú...þ(.,6ü>. */
    $"3C3C 06FA 12FC 4400 34FD 1403 3444 3C44"            /* <<.ú.üD.4ý..4D<D */
    $"F900 67F8 0004 1438 0E04 06FE 0E01 2036"            /* ù.gø...8...þ.. 6 */
    $"FC44 0136 20F9 0E03 0A06 0A0A E30E 0412"            /* üD.6 ù......ã... */
    $"1216 1612 D90E 030A 0606 0AFE 1203 2C36"            /* ....Ù......þ..,6 */
    $"3C3C F644 000A F112 051C 3036 0606 0AFD"            /* <<öD..ñ...06...ý */
    $"12FE 2001 1C1C FC16 FE12 0716 1C24 1620"            /* .þ ...ü.þ....$.  */
    $"242C 30FD 3EFE 3C00 06FA 1200 36FC 4407"            /* $,0ý>þ<..ú..6üD. */
    $"3410 1034 443C 4438 F900 6EF9 0004 142A"            /* 4..4D<D8ù.nù...* */
    $"0E04 06FE 0E02 2044 30FC 2201 1E34 FE44"            /* ...þ.. D0ü"..4þD */
    $"0136 20FE 0E01 0A0A E20E 0412 1616 1212"            /* .6 þ....â....... */
    $"DA0E 040A 0A06 0A0A FD12 0136 3CF4 4401"            /* Ú.......ý..6<ôD. */
    $"360A F512 061C 2430 3006 060A FD12 0320"            /* 6.õ...$00...ý..  */
    $"201C 1CFC 16FD 1209 161C 2012 161C 2024"            /*  ..ü.ý.Æ.. ... $ */
    $"2C30 FE3E FD3C 0006 FB12 0116 2CFB 4406"            /* ,0þ>ý<..û...,ûD. */
    $"3434 443C 4444 1EF9 006B F900 032A 3004"            /* 44D<DD.ù.kù..*0. */
    $"06FE 0E03 2044 2430 FD22 011E 14FC 2200"            /* .þ.. D$0ý"...ü". */
    $"36DF 0E04 1212 1612 12D9 0E03 0A06 060A"            /* 6ß.......Ù...... */
    $"FC12 022C 443C F344 0136 0AF8 1202 1C30"            /* ü..,D<óD.6.ø...0 */
    $"30FE 0603 1220 0A12 FE20 011C 1CFE 16FA"            /* 0þ... ..þ ...þ.ú */
    $"1212 1620 0E12 161C 1C20 242C 3030 2C24"            /* ... ..... $,00,$ */
    $"2436 3C3C 06FD 1203 161C 202C F944 033C"            /* $6<<.ý.... ,ùD.< */
    $"4444 38F8 0073 FA00 0314 3004 06FE 0E0A"            /* DD8ø.sú...0..þ.. */
    $"2044 2024 3022 222E 2E00 00FD 2201 3420"            /*  D $0""....ý".4  */
    $"E00E 0312 1616 12D9 0E04 0A0A 060A 0AFB"            /* à......Ù.......û */
    $"1201 363C FC44 043C 3834 383C FB44 000A"            /* ..6<üD.<848<ûD.. */
    $"FA12 051C 3030 0606 0AFE 1200 20FE 1CFE"            /* ú...00...þ.. þ.þ */
    $"16F8 1210 161C 200E 1216 161C 1C20 242C"            /* .ø.... ...... $, */
    $"2424 201C 16FE 0605 1212 161C 202C F844"            /* $$ ..þ...... ,øD */
    $"013E 3EFE 4400 1EF8 0071 FB00 0314 3004"            /* .>>þD..ø.qû...0. */
    $"06FE 0E08 2044 2020 2430 221E 14FE 0004"            /* .þ.. D  $0"..þ.. */
    $"2222 1E14 36DF 0EFE 12D9 0E03 0A06 060A"            /* ""..6ß.þ.Ù...... */
    $"FA12 022C 443C FD44 072A 3238 3844 3438"            /* ú..,D<ýD.*288D48 */
    $"3CFD 4401 360A FE12 061C 2430 3006 060A"            /* <ýD.6.þ...$00... */
    $"FD12 011C 1CFD 16F8 120A 161C 200E 0E12"            /* ý....ý.ø.... ... */
    $"1216 161C 1CFE 2001 1C16 FE06 FE12 041C"            /* .....þ ...þ.þ... */
    $"202C 2C36 F444 0138 1EF7 006D FC00 0314"            /*  ,,6ôD.8.÷.mü... */
    $"380E 06FE 0E01 2044 FE20 0324 3022 14FE"            /* 8..þ.. Dþ .$0".þ */
    $"0005 1422 1E14 3420 B60E 040A 0A06 0A0A"            /* ..."..4 ¶....... */
    $"F912 0136 3CFD 4409 3C26 2E2E 383E 4434"            /* ù..6<ýDÆ<&..8>D4 */
    $"383C FD44 040A 121C 3030 FE06 FD12 0416"            /* 8<ýD....00þ.ý... */
    $"1C1C 160E F612 0416 1C20 0E0E FD12 0816"            /* ....ö.... ..ý... */
    $"1620 201C 1616 0606 FE12 061C 202C 2C36"            /* .  .....þ... ,,6 */
    $"443C F544 0138 1EF5 006E FC00 072A 0E06"            /* D<õD.8.õ.nü..*.. */
    $"060E 0E20 44FD 20F9 0E03 221E 0036 D90E"            /* ... Dý ù.."..6Ù. */
    $"0120 36FB 4401 3620 E80E 030A 0606 0AF7"            /* . 6ûD.6 è......÷ */
    $"1201 443C FE44 0A3C 3E1E 2A2A 383E 3E44"            /* ..D<þD.<>.**8>>D */
    $"3438 FC44 0430 3006 060A FD12 0116 16FE"            /* 48üD.00...ý....þ */
    $"1201 200E F812 0416 1C20 0E0E FD12 0316"            /* .. .ø.... ..ý... */
    $"1620 20FE 1609 0606 1212 1C20 2C2C 3644"            /* .  þ.Æ..... ,,6D */
    $"F33C 0238 2A14 F400 6DFD 0007 1438 0E04"            /* ó<.8*.ô.mý...8.. */
    $"060E 2044 FE20 F90E FE0A 0206 3620 DB0E"            /* .. Dþ ù.þ...6 Û. */
    $"0220 3644 FA22 011E 34F8 4401 3620 F40E"            /* . 6Dú"..4øD.6 ô. */
    $"030A 060A 0AF7 1202 2C44 3CFE 4405 3C38"            /* .....÷..,D<þD.<8 */
    $"1E2A 2A34 FE3E 023C 343C FD44 0136 0AF5"            /* .**4þ>.<4<ýD.6.õ */
    $"1201 200E F912 0316 200E 0EFD 120F 1616"            /* .. .ù... ..ý.... */
    $"2020 1616 0A06 0612 1C20 2C2C 3644 F33C"            /*   ....... ,,6Dó< */
    $"0238 2A14 F100 6FFD 0008 2A0E 0606 0E0E"            /* .8*.ñ.oý..*..... */
    $"3620 20FD 0EFB 0A04 0606 0404 36DC 0E04"            /* 6  ý.û......6Ü.. */
    $"2036 3624 30FB 2203 1E14 0014 FA22 021E"            /*  66$0û".....ú".. */
    $"1E44 F50E 020A 060A F512 0136 3CFE 440C"            /* .Dõ.....õ..6<þD. */
    $"3C3E 3226 2A2A 323C 3E3E 4434 38FC 4400"            /* <>2&**2<>>D48üD. */
    $"0AF5 1201 200E FB12 0316 1C20 0EFC 120D"            /* .õ.. .û.... .ü.Â */
    $"1620 2016 1606 0612 121C 202C 2C36 F33C"            /* .  ....... ,,6ó< */
    $"0238 2A14 EE00 78FE 000F 1438 0E04 060E"            /* .8*.î.xþ...8.... */
    $"0E20 3644 442C 0A0A 0606 FA04 0136 20DE"            /* . 6DD,....ú..6 Þ */
    $"0E06 2036 3620 2424 30FD 2201 1E14 FE00"            /* .. 66 $$0ý"...þ. */
    $"0014 FC22 041E 1400 4420 F60E 020A 060A"            /* ..ü"....D ö..... */
    $"F512 022C 443C FE44 023C 3E26 FD2A 053C"            /* õ..,D<þD.<>&ý*.< */
    $"3E3E 4434 2EFC 4400 0AF5 1201 200E FD12"            /* >>D4.üD..õ.. .ý. */
    $"0416 1C20 0E0E FD12 0D16 1620 1616 0606"            /* ... ..ý.Â.. .... */
    $"1212 1C20 2C2C 36F4 3C02 382A 14EB 0076"            /* ... ,,6ô<.8*.ë.v */
    $"FE00 042A 300E 0406 FB0E 0120 36FD 4400"            /* þ..*0...û.. 6ýD. */
    $"2CFC 0400 36DF 0E02 2036 36FE 2002 2424"            /* ,ü..6ß.. 66þ .$$ */
    $"30FD 2205 2E2E 0000 1014 FE22 051E 1400"            /* 0ý".......þ".... */
    $"0044 20F6 0E02 0A06 0AF4 1201 2C3C FD44"            /* .D ö.....ô..,<ýD */
    $"023C 3E1E FD2A 0038 FE3E 023C 2E3C FD44"            /* .<>.ý*.8þ>.<.<ýD */
    $"000A F512 081C 0E12 1216 1C20 0E0E FD12"            /* ..õ........ ..ý. */
    $"0C16 1620 2016 0606 121C 202C 2C36 F43C"            /* ...  ..... ,,6ô< */
    $"0238 2A14 E800 7307 0000 1438 0E0E 0406"            /* .8*.è.s....8.... */
    $"F50E 0120 36FE 4401 3620 E10E 0220 3636"            /* õ.. 6þD.6 á.. 66 */
    $"FC20 0224 2430 FE22 0E1E 1400 0010 141A"            /* ü .$$0þ"........ */
    $"2222 1E14 0000 4420 F60E 020A 060A F312"            /* ""....D ö.....ó. */
    $"0136 3CFE 4403 3C3E 3E1E FD2A 0038 FE3E"            /* .6<þD.<>>.ý*.8þ> */
    $"0244 2E34 FD44 0136 0AF5 1200 1CFE 2001"            /* .D.4ýD.6.õ...þ . */
    $"0E0E FD12 0C16 1620 2016 0606 121C 202C"            /* ..ý....  ..... , */
    $"2C36 F53C 0238 2A14 E500 5C07 0000 2A30"            /* ,6õ<.8*.å.\...*0 */
    $"0E06 0406 CF0E 0136 36FA 2005 2424 3022"            /* ....Ï..66ú .$$0" */
    $"1E14 FE00 0910 1414 1A22 1E14 0044 36F5"            /* ..þ.Æ...."...D6õ */
    $"0E02 0A06 0AF2 1201 363E FE44 033C 3E3E"            /* .....ò..6>þD.<>> */
    $"1EFD 2A00 38FE 3E02 442E 2EFC 4400 0AED"            /* .ý*.8þ>.D..üD..í */
    $"120C 1616 2020 0A06 0612 1C20 2C2C 36F6"            /* ....  ..... ,,6ö */
    $"3C02 382A 14E2 004F 0700 0038 0E0E 0604"            /* <.8*.â.O...8.... */
    $"06D1 0E01 2044 FA20 F70E 0114 14FE 1A04"            /* .Ñ.. Dú ÷....þ.. */
    $"221E 0044 20F5 0E02 0A06 0AF1 1201 443E"            /* "..D õ.....ñ..D> */
    $"FE44 FE1E FC2A FD22 022E 2A2A FC44 000A"            /* þDþ.ü*ý"..**üD.. */
    $"EF12 0C16 1620 2006 0612 121C 202C 2C36"            /* ï....  ..... ,,6 */
    $"F63C 0138 1EDF 004A 0700 0044 0E0E 0604"            /* ö<.8.ß.J...D.... */
    $"06D1 0E00 44FE 20F1 0EFC 0A02 0644 20F5"            /* .Ñ..Dþ ñ.ü...D õ */
    $"0E02 0A06 0AF0 12FD 4407 3C32 2E2A 2A1A"            /* .....ð.ýD.<2.**. */
    $"1E1E FC2A 0326 2E2A 34FD 4400 0AEF 120A"            /* ..ü*.&.*4ýD..ï.. */
    $"1C1C 0606 1212 1C20 2C2C 36F6 3C01 381E"            /* ....... ,,6ö<.8. */
    $"DD00 5507 001E 360E 0E06 0406 E70E 002A"            /* Ý.U...6.....ç..* */
    $"EC0E 0120 36FB 4400 2CFD 0EF9 0A05 0606"            /* ì.. 6ûD.,ý.ù.... */
    $"0404 4420 F50E 020A 060A EF12 FD44 0432"            /* ..D õ.....ï.ýD.2 */
    $"2E2E 2A14 FE22 001E FD2A 0326 2E2A 2EFD"            /* ..*.þ"..ý*.&.*.ý */
    $"4400 0AF1 1209 1C1C 0606 121C 202C 2C36"            /* D..ñ.Æ...... ,,6 */
    $"F63C 0238 2A14 DB00 5408 0038 1C24 0E0E"            /* ö<.8*.Û.T..8.$.. */
    $"0604 06E9 0E02 0040 34E5 0E01 2036 FB44"            /* ...é...@4å.. 6ûD */
    $"022C 0606 FC04 0144 20F5 0E02 0A06 0AEF"            /* .,..ü..D õ.....ï */
    $"1200 30FD 4404 322E 2A2A 14FE 22FC 2A03"            /* ..0ýD.2.**.þ"ü*. */
    $"262E 2A2A FD44 0136 0AF4 1209 161C 0A06"            /* &.**ýD.6.ô.Æ.... */
    $"121C 202C 2C36 F63C 0138 1ED8 0052 0800"            /* .. ,,6ö<.8.Ø.R.. */
    $"4412 0630 240E 0406 EA0E 0400 0802 4038"            /* D..0$...ê.....@8 */
    $"DE0E 0120 36FC 4401 3620 F50E 020A 060A"            /* Þ.. 6üD.6 õ..... */
    $"F112 0324 3024 06FD 4404 382E 2A2A 1EFE"            /* ñ..$0$.ýD.8.**.þ */
    $"22FC 2A03 3844 2222 FC44 000A F612 0916"            /* "ü*.8D""üD..ö.Æ. */
    $"1C1C 0612 1C20 2C2C 36F6 3C01 381E D600"            /* ..... ,,6ö<.8.Ö. */
    $"4E09 0044 1212 0A06 240E 0406 EB0E 0400"            /* NÆ.D....$...ë... */
    $"0C0C 0844 CA0E 020A 060A F212 0530 2406"            /* ...DÊ.....ò..0$. */
    $"060A 12FD 4410 3C38 2A1A 2222 1422 222E"            /* ...ýD.<8*.""."". */
    $"2A2A 383E 442E 22FC 4400 0AF8 1209 1616"            /* **8>D."üD..ø.Æ.. */
    $"0A0A 121C 202C 2C36 F63C 0138 1ED4 0052"            /* .... ,,6ö<.8.Ô.R */
    $"0100 44FD 1205 0624 3024 0406 ED0E 031E"            /* ..Dý...$0$..í... */
    $"4242 44CA 0E02 0A06 0AF4 1208 2430 2406"            /* BBDÊ.....ô..$0$. */
    $"060A 1212 2CFE 440C 3C3C 382A 1A22 141C"            /* ....,þD.<<8*.".. */
    $"1E22 2E2A 38FE 3E01 2E22 FC44 000A FA12"            /* .".*8þ>.."üD..ú. */
    $"0916 160A 1212 1C20 2C2C 36F6 3C01 381E"            /* Æ...... ,,6ö<.8. */
    $"D200 4F01 0044 FC12 020A 0606 FD30 EE0E"            /* Ò.O..Dü.....ý0î. */
    $"012A 38CA 0E02 0A06 0AF5 1204 3024 0606"            /* .*8Ê.....õ..0$.. */
    $"0AFC 1200 2CFE 440B 3C3E 3E38 1A22 1E2C"            /* .ü..,þD.<>>8."., */
    $"2E22 3838 FD3E 032E 2244 3EFE 4400 0AFB"            /* ."88ý>.."D>þD..û */
    $"1207 160A 121C 202C 2C36 F63C 0238 2A14"            /* ...... ,,6ö<.8*. */
    $"D000 4601 1E36 F912 000A FE06 B60E 020A"            /* Ð.F..6ù...þ.¶... */
    $"060A F712 0524 3024 0606 0AFA 1200 36FE"            /* ..÷..$0$...ú..6þ */
    $"440B 3C3C 3E38 1E22 2E2C 3822 3838 FE3E"            /* D.<<>8.".,8"88þ> */
    $"0444 2A22 443E FE44 000A FA12 041C 202C"            /* .D*"D>þD..ú... , */
    $"2C36 F63C 0138 1ECD 0040 0138 2CF5 12B7"            /* ,6ö<.8.Í.@.8,õ.· */
    $"0E02 0A06 0AFA 1206 2430 3024 0606 0AF7"            /* .....ú..$00$...÷ */
    $"12FC 440A 3C3E 381E 2222 3822 2238 2EFE"            /* .üD.<>8.""8""8.þ */
    $"3E04 4422 1E44 3CFE 4400 0AFC 1204 1C20"            /* >.D".D<þD..ü...  */
    $"2C2C 36F6 3C01 381E CB00 4901 4420 F412"            /* ,,6ö<.8.Ë.I.D ô. */
    $"0120 36FD 4402 3630 20C2 0E02 0A06 0AFC"            /* . 6ýD.60 Â.....ü */
    $"1202 3030 24FE 0600 0AF4 12FC 4404 3C3E"            /* ..00$þ...ô.üD.<> */
    $"2A2A 1EFE 2202 2E2A 22FE 3E04 441E 1E44"            /* **.þ"..*"þ>.D..D */
    $"3CFE 4400 0AFE 1204 1C20 2C2C 36F6 3C01"            /* <þD..þ... ,,6ö<. */
    $"381E C900 4801 441C F412 0030 FD36 F944"            /* 8.É.H.D.ô..0ý6ùD */
    $"0236 3020 C90E 070A 060A 1224 3030 24FE"            /* .60 É......$00$þ */
    $"0600 0AF1 1200 36FD 4403 3C3E 222A FD22"            /* ...ñ..6ýD.<>"*ý" */
    $"0238 2A26 FE3E 0444 1E2A 443C FE44 060A"            /* .8*&þ>.D.*D<þD.. */
    $"121C 202C 2C36 F63C 0138 1EC7 004A 0044"            /* .. ,,6ö<.8.Ç.J.D */
    $"F412 021C 3030 FE36 F144 0236 3020 F10E"            /* ô...00þ6ñD.60 ñ. */
    $"0230 3024 E60E 0024 FD30 0024 FE06 000A"            /* .00$æ..$ý0.$þ... */
    $"ED12 002C FC44 033C 262A 2AFE 2209 382A"            /* í..,üD.<&**þ"Æ8* */
    $"2A34 3E3E 3C1E 343C FD44 040A 202C 2C36"            /* *4>><.4<ýD.. ,,6 */
    $"F73C 0238 2A14 C500 4400 44F4 1200 1CFE"            /* ÷<.8*.Å.D.Dô...þ */
    $"3001 3636 E944 0236 3020 F90E FE06 0024"            /* 0.66éD.60 ù.þ..$ */
    $"E830 0024 FC06 000A E912 002C FC44 012A"            /* è0.$ü...é..,üD.* */
    $"2EFE 2A01 2E38 FE2A 0C22 3E44 221E 443C"            /* .þ*..8þ*.">D".D< */
    $"4444 3C44 2C36 F63C 0138 1EC2 003B 0044"            /* DD<D,6ö<.8.Â.;.D */
    $"F412 001C FD30 0036 E444 0136 20FA 1200"            /* ô...ý0.6äD.6 ú.. */
    $"0AE8 0604 0A12 0A06 0AE6 12FC 4401 222E"            /* .è.......æ.üD.". */
    $"FE2A 0038 FD2A 0A22 3E44 1E1E 443C 4444"            /* þ*.8ý*.">D..D<DD */
    $"3C44 F63C 0138 1EC0 0031 0044 F412 001C"            /* <Dö<.8.À.1.Dô... */
    $"FC30 E344 0036 DF12 020A 060A E512 FC44"            /* ü0ãD.6ß.....å.üD */
    $"0632 2E2A 2A38 3E38 FE2A 0826 3444 1A22"            /* .2.**8>8þ*.&4D." */
    $"443C 4444 F63C 0138 1EBE 0034 0244 120A"            /* D<DDö<.8.¾.4.D.. */
    $"F612 001C F830 E744 0036 DF12 020A 060A"            /* ö...ø0çD.6ß..... */
    $"E512 0036 FD44 0332 2E2A 32FE 3E00 32FE"            /* å..6ýD.2.*2þ>.2þ */
    $"2A06 223C 1A34 3C44 44F7 3C01 381E BC00"            /* *."<.4<DD÷<.8.¼. */
    $"3803 441C 060A F612 FD30 FD20 FA30 EE44"            /* 8.D...ö.ý0ý ú0îD */
    $"0136 20DF 1202 0A06 0AE5 1200 2CFD 4403"            /* .6 ß.....å..,ýD. */
    $"3C2E 2A38 FE3E 0A38 2A2A 262A 221A 443C"            /* <.*8þ>.8**&*".D< */
    $"4444 F93C 0138 1EBA 003A 0444 200A 060A"            /* DDù<.8.º.:.D ... */
    $"F712 0520 3012 060A 12F9 20FA 30F5 4401"            /* ÷.. 0....ù ú0õD. */
    $"3620 DE12 020A 060A E412 FC44 0132 32FC"            /* 6 Þ.....ä.üD.22ü */
    $"3E09 322A 262A 1A22 443C 4444 FC3C 0238"            /* >Æ2*&*."D<DDü<.8 */
    $"2A14 B800 3E04 382C 120A 06FE 0AF9 1204"            /* *.¸.>.8,...þ.ù.. */
    $"2030 3020 0AFD 0601 0A12 F920 F830 FE44"            /*  00 .ý....ù ø0þD */
    $"0136 20DD 1202 0A06 0AE4 12FC 4401 3238"            /* .6 Ý.....ä.üD.28 */
    $"FC3E 0838 2626 2A14 343C 3C44 FD3C 0138"            /* ü>.8&&*.4<<Dý<.8 */
    $"1EB5 003D 0400 441C 120A FE06 FC0A FC12"            /* .µ.=..D...þ.ü.ü. */
    $"011C 20FC 3001 200A FD06 010A 12F7 20FE"            /* .. ü0. .ý....÷ þ */
    $"3001 3620 DC12 020A 060A E412 FB44 003C"            /* 0.6 Ü.....ä.ûD.< */
    $"FB3E 0B38 2A14 2244 3C44 443C 3C38 1EB3"            /* û>.8*."D<DD<<8.³ */
    $"0042 0400 2E36 1C12 FE0A FC06 FB0A FC12"            /* .B...6..þ.ü.û.ü. */
    $"011C 20FC 3001 200A FB06 010A 12FD 2001"            /* .. ü0. .û....ý . */
    $"3020 DB12 020A 060A EE12 FE0A FA12 0036"            /* 0 Û.....î.þ.ú..6 */
    $"FC44 013C 3CFC 3E09 4414 1434 3C3C 443C"            /* üD.<<ü>ÆD..4<<D< */
    $"381E B100 4307 0000 2E44 2C20 1C12 FC0A"            /* 8.±.C....D, ..ü. */
    $"FB06 FA0A FD12 011C 20FA 3006 200A 0606"            /* û.ú.ý... ú0. ... */
    $"3030 20DB 1203 0A06 060A F212 FD0A 0206"            /* 00 Û......ò.ý... */
    $"060A FA12 002C FB44 FD3C 0A44 3C22 1434"            /* ..ú..,ûDý<.D<".4 */
    $"3C3C 4444 2E1E B000 40FE 0009 1E38 4444"            /* <<DD..°.@þ.Æ.8DD */
    $"362C 2C20 1C12 FB0A FA06 FB0A FB12 011C"            /* 6,, ..û.ú.û.û... */
    $"20FE 3000 20D9 1200 0AFE 0600 0AF8 12FC"            /*  þ0. Ù...þ...ø.ü */
    $"0AFD 0601 0A0A F912 002C F744 052A 101E"            /* .ý....ù..,÷D.*.. */
    $"343C 3CFE 4400 10AF 003D 0400 0014 2A38"            /* 4<<þD..¯.=....*8 */
    $"FD3C FD44 0536 2C2C 201C 12FA 0AFB 06F9"            /* ý<ýD.6,, ..ú.û.ù */
    $"0AD7 1201 0A0A FC06 000A FE12 FC0A FC06"            /* .×....ü...þ.ü.ü. */
    $"FD0A F812 012C 36F9 4406 3C22 2234 3C44"            /* ý.ø..,6ùD.<""4<D */
    $"3CFE 4400 1EAE 0033 0300 002A 38F6 3CFE"            /* <þD..®.3...*8ö<þ */
    $"4404 362C 2C20 1CFE 12FB 0AF9 06EE 0AED"            /* D.6,, .þ.û.ù.î.í */
    $"12FE 0AF9 06FE 0AFC 06FC 0AF6 1200 36F3"            /* .þ.ù.þ.ü.ü.ö..6ó */
    $"4402 3E3C 3CFE 4400 1EAD 0029 0300 002A"            /* D.><<þD..­.)...* */
    $"38F1 3CFD 4404 362C 2C20 1CFE 12F9 0AEE"            /* 8ñ<ýD.6,, .þ.ù.î */
    $"06ED 0AF3 06FC 0AF8 1204 1C20 2C2C 36EB"            /* .í.ó.ü.ø... ,,6ë */
    $"4400 1EAC 002B 0400 0014 2A38 EC3C FD44"            /* D..¬.+....*8ì<ýD */
    $"0436 2C2C 201C FC12 EE0A ED06 F30A F812"            /* .6,, .ü.î.í.ó.ø. */
    $"041C 202C 2C36 FE44 FC3C F044 0138 1EAB"            /* .. ,,6þDü<ðD.8.« */
    $"002A FE00 0514 142A 2A38 38EA 3CFC 4404"            /* .*þ....**88ê<üD. */
    $"362C 2C20 1CF0 12ED 0AEE 1203 1C20 2C2C"            /* 6,, .ð.í.î... ,, */
    $"FE44 EF3C FB44 023C 341E A900 1FFA 0003"            /* þDï<ûD.<4.©..ú.. */
    $"1414 2A2A FE38 E83C F944 D212 061C 202C"            /* ..**þ8è<ùDÒ... , */
    $"2C36 4444 F13C 0238 2A14 9D00 25F5 0003"            /* ,6DDñ<.8*..%õ.. */
    $"1414 3232 FE38 E43C F944 0436 2C2C 201C"            /* ..22þ8ä<ùD.6,, . */
    $"E812 041C 202C 2C36 FB44 F03C 0238 2A14"            /* è... ,,6ûDð<.8*. */
    $"9A00 20F0 0003 1414 2A2A FD38 E03C FA44"            /* . ð....**ý8à<úD */
    $"0736 2C2C 2020 2C2C 36F1 44EB 3C02 382A"            /* .6,,  ,,6ñDë<.8* */
    $"1497 0018 EA00 0314 142A 2AFD 38DD 3CFD"            /* ...ê....**ý8Ý<ý */
    $"44DF 3C05 3838 2A2A 1414 9400 14E4 0003"            /* Dß<.88**....ä.. */
    $"1414 2A2A FC38 C33C 0538 382A 2A14 148F"            /* ..**ü8Ã<.88**.. */
    $"0014 DC00 0314 142A 2AFA 38D1 3C05 3838"            /* ..Ü....**ú8Ñ<.88 */
    $"2A2A 1414 8B00 14D3 0003 1414 2A2A FA38"            /* **....Ó....**ú8 */
    $"E03C FD38 032A 2A14 1487 0017 C800 0314"            /* à<ý8.**....È... */
    $"142A 2AFA 38F8 3CF8 3803 2A2A 1414 8100"            /* .**ú8ø<ø8.**... */
    $"0100 000E BF00 0114 14F8 2A01 1414 8100"            /* ....¿....ø*.... */
    $"F400 00FF"                                          /* ô..ÿ */
};

data 'PICT' (130) {
    $"12F4 0000 0000 00C2 00A4 0011 02FF 0C00"            /* .ô.....Â.¤...ÿ.. */
    $"FFFE 0000 0048 0000 0048 0000 0000 0000"            /* ÿþ...H...H...... */
    $"00C2 00A4 0000 0000 0001 000A 0000 0000"            /* .Â.¤............ */
    $"00C2 00A4 0098 8054 0000 0000 00C2 00A4"            /* .Â.¤.T.....Â.¤ */
    $"0000 0000 0000 0000 0048 0000 0048 0000"            /* .........H...H.. */
    $"0000 0004 0001 0004 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0047 5F75 0000 000C 0000 FFFF"            /* .....G_u......ÿÿ */
    $"FFFF FFFF 0001 FFFF FFFF 0000 0002 FFFF"            /* ÿÿÿÿ..ÿÿÿÿ....ÿÿ */
    $"CECE 6363 0003 FFFF 0000 0000 0004 CECE"            /* ÎÎcc..ÿÿ......ÎÎ */
    $"9C9C 3131 0005 9C9C 3131 FFFF 0006 9C9C"            /* 11..11ÿÿ.. */
    $"3131 0000 0007 6363 0000 FFFF 0008 6363"            /* 11....cc..ÿÿ..cc */
    $"0000 0000 0009 3131 9C9C 6363 000A 3131"            /* .....Æ11cc..11 */
    $"6363 3131 000B 0000 6363 0000 000C 0000"            /* cc11....cc...... */
    $"0000 0000 0000 0000 00C2 00A4 0000 0000"            /* .........Â.¤.... */
    $"00C2 00A4 0000 06CA 00FF 44E6 000F E700"            /* .Â.¤...Ê.ÿDæ..ç. */
    $"0104 44E9 0000 04FC 4400 40E8 000C E800"            /* ..Dé...üD.@è..è. */
    $"FD44 0040 EC00 F944 E800 0EEA 0000 04FA"            /* ýD.@ì.ùDè..ê...ú */
    $"44EE 00F8 4400 40E9 000E EA00 F844 F000"            /* Dî.øD.@é..ê.øDð. */
    $"0004 F744 0040 EA00 0CEB 00F7 4400 40F1"            /* ..÷D.@ê..ë.÷D.@ñ */
    $"00F5 44EA 0010 EC00 0004 F644 0040 F300"            /* .õDê..ì...öD.@ó. */
    $"F444 0040 EB00 13ED 0000 04F4 44FD 00FB"            /* ôD.@ë..í...ôDý.û */
    $"4403 4000 0004 F344 EB00 12ED 00F3 4401"            /* D.@...óDë..í.óD. */
    $"4000 F744 0140 04F3 4400 40EC 0008 EE00"            /* @.÷D.@.óD.@ì..î. */
    $"0004 D644 EC00 0CEE 0000 04DE 4400 66FA"            /* ..ÖDì..î...ÞD.fú */
    $"44EC 0012 EE00 FA44 0246 6664 E944 0046"            /* Dì..î.úD.FfdéD.F */
    $"FE66 FB44 EC00 14EF 0000 04FB 44FD 66EA"            /* þfûDì..ï...ûDýfê */
    $"4400 46FC 66FC 4400 40ED 0016 EF00 0004"            /* D.FüfüD.@í..ï... */
    $"FD44 0046 FB66 EA44 FC66 0064 FD44 0040"            /* ýD.FûfêDüf.dýD.@ */
    $"ED00 1AEF 0000 04FD 4400 46FC 6600 64EA"            /* í..ï...ýD.Füf.dê */
    $"4400 46FD 6600 64FD 4400 40ED 0012 EF00"            /* D.Fýf.dýD.@í..ï. */
    $"FC44 FB66 E844 FD66 0064 FD44 0040 ED00"            /* üDûfèDýf.dýD.@í. */
    $"10EF 00FC 44FC 66E7 4400 46FD 66FC 44ED"            /* .ï.üDüfçD.FýfüDí */
    $"0010 EF00 FC44 FD66 0064 E644 FD66 FC44"            /* ..ï.üDýf.dæDýfüD */
    $"ED00 12EF 00FD 4400 46FD 66E5 4400 46FE"            /* í..ï.ýD.FýfåD.Fþ */
    $"66FC 44ED 0012 EF00 FD44 0046 FE66 0064"            /* füDí..ï.ýD.Fþf.d */
    $"E444 FE66 FC44 ED00 14EF 00FD 4400 46FE"            /* äDþfüDí..ï.ýD.Fþ */
    $"66E3 4402 4666 64FD 4400 40ED 0013 EF00"            /* fãD.FfdýD.@í..ï. */
    $"FC44 FF66 0064 E244 0166 64FD 4400 40ED"            /* üDÿf.dâD.fdýD.@í */
    $"0010 EF00 FC44 FF66 E144 0046 FC44 0040"            /* ..ï.üDÿfáD.FüD.@ */
    $"ED00 11EF 00FC 4401 4666 E144 0046 FC44"            /* í..ï.üD.FfáD.FüD */
    $"0040 ED00 0CEF 0000 04FC 4400 64DB 44EC"            /* .@í..ï...üD.dÛDì */
    $"0008 EF00 0004 D544 EC00 06EE 00D5 44EC"            /* ..ï...ÕDì..î.ÕDì */
    $"000A EE00 0004 D744 0040 EC00 0AEE 0000"            /* ..î...×D.@ì..î.. */
    $"04D7 4400 40EC 0006 ED00 D744 EB00 08ED"            /* .×D.@ì..í.×Dë..í */
    $"00D8 4400 40EB 0008 ED00 0004 D944 EA00"            /* .ØD.@ë..í...ÙDê. */
    $"08EC 00DA 4400 40EA 000A EC00 0004 DB44"            /* .ì.ÚD.@ê..ì...ÛD */
    $"0040 EA00 08EB 00DB 4400 40EA 0008 EB00"            /* .@ê..ë.ÛD.@ê..ë. */
    $"DB44 0040 EA00 08EC 0000 04DA 44EA 0008"            /* ÛD.@ê..ì...ÚDê.. */
    $"EC00 0004 DA44 EA00 08EC 0000 04DA 44EA"            /* ì...ÚDê..ì...ÚDê */
    $"0008 EC00 0004 DA44 EA00 11EC 0000 04F8"            /* ..ì...ÚDê..ì...ø */
    $"44FF CCF1 4401 4CCC F744 EA00 15EC 00F8"            /* DÿÌñD.LÌ÷Dê..ì.ø */
    $"4403 4CBB BBC4 F244 02CB BBC4 F844 0040"            /* D.L»»ÄòD.Ë»ÄøD.@ */
    $"EB00 1EEC 00F8 4403 CBBB BBBC FC44 0042"            /* ë..ì.øD.Ë»»¼üD.B */
    $"FE22 0024 FD44 034C BBBB BCF8 4400 40EB"            /* þ".$ýD.L»»¼øD.@ë */
    $"001E EC00 F844 03CB BBBB BCFD 4400 42FC"            /* ..ì.øD.Ë»»¼ýD.Bü */
    $"2200 24FE 4403 4CBB BBBC F844 0040 EB00"            /* ".$þD.L»»¼øD.@ë. */
    $"1DEC 00F8 4403 CBBB BBBC FE44 0042 FA22"            /* .ì.øD.Ë»»¼þD.Bú" */
    $"0624 4444 4CBB BBBC F844 0040 EB00 21EC"            /* .$DDL»»¼øD.@ë.!ì */
    $"00F8 440C CBBB BBBC 4444 4222 222C CCCC"            /* .øD.Ë»»¼DDB"",ÌÌ */
    $"C2FE 22FF 4403 4CBB BBBC F844 0040 EB00"            /* Âþ"ÿD.L»»¼øD.@ë. */
    $"21EC 00F8 440D 4CBB BBC4 4442 2222 2CC8"            /* !ì.øDÂL»»ÄDB"",È */
    $"8888 8CC2 FE22 FF44 02CB BBC4 F844 0040"            /* Âþ"ÿD.Ë»ÄøD.@ */
    $"EB00 1DEC 00F7 44FF CCFF 44FE 2200 C8FD"            /* ë..ì.÷DÿÌÿDþ".Èý */
    $"8800 8CFE 2203 2444 4CCC F744 0040 EB00"            /* .þ".$DLÌ÷D.@ë. */
    $"15EC 00F4 4403 4222 222C FB88 00C2 FE22"            /* .ì.ôD.B"",û.Âþ" */
    $"F444 0040 EB00 14EC 00F4 44FE 2200 2CFB"            /* ôD.@ë..ì.ôDþ".,û */
    $"8800 C8FD 22F5 4400 40EB 0018 EC00 F544"            /* .Èý"õD.@ë..ì.õD */
    $"0042 FE22 00C8 FB88 008C FD22 0024 F644"            /* .Bþ".Èû.ý".$öD */
    $"0040 EB00 14EC 00F5 44FD 2200 C8FB 8800"            /* .@ë..ì.õDý".Èû. */
    $"8CFC 22F6 4400 40EB 0018 EC00 F644 0042"            /* ü"öD.@ë..ì.öD.B */
    $"FD22 00C8 FB88 008C FC22 0024 F744 0040"            /* ý".Èû.ü".$÷D.@ */
    $"EB00 16EC 0000 04F7 44FC 2200 C8FB 8800"            /* ë..ì...÷Dü".Èû. */
    $"8CFC 2200 24F7 44EA 0016 EC00 0004 F844"            /* ü".$÷Dê..ì...øD */
    $"0042 FC22 002C FB88 00C8 FB22 F744 EA00"            /* .Bü".,û.Èû"÷Dê. */
    $"16EC 0000 04F8 4400 42FC 2200 2CFB 8800"            /* .ì...øD.Bü".,û. */
    $"C2FB 22F7 44EA 0016 EC00 0004 F844 FA22"            /* Âû"÷Dê..ì...øDú" */
    $"00C8 FD88 008C FA22 0024 F844 EA00 17EC"            /* .Èý.ú".$øDê..ì */
    $"0000 04F8 44FA 2205 2CC8 8888 8CC2 FA22"            /* ...øDú".,ÈÂú" */
    $"0024 F844 EA00 13EB 00F8 44F9 2203 2CCC"            /* .$øDê..ë.øDù".,Ì */
    $"CCC2 F822 F944 0040 EA00 0EEB 00F9 4400"            /* ÌÂø"ùD.@ê..ë.ùD. */
    $"42EC 22F9 4400 40EA 0010 EB00 F944 0042"            /* Bì"ùD.@ê..ë.ùD.B */
    $"EC22 0024 FA44 0040 EA00 10EB 0000 04FA"            /* ì".$úD.@ê..ë...ú */
    $"4400 42EC 2200 24FA 44E9 0010 EB00 0004"            /* D.Bì".$úDé..ë... */
    $"FA44 0042 EC22 0024 FA44 E900 0EEA 00FA"            /* úD.Bì".$úDé..ê.ú */
    $"44EB 2200 24FB 4400 40E9 000E EA00 FA44"            /* Dë".$ûD.@é..ê.úD */
    $"EB22 0024 FB44 0040 E900 0EEA 0000 04FB"            /* ë".$ûD.@é..ê...û */
    $"44EB 2200 24FB 44E8 000E EA00 0004 FB44"            /* Dë".$ûDè..ê...ûD */
    $"EB22 0024 FB44 E800 10E9 00FB 4400 42EC"            /* ë".$ûDè..é.ûD.Bì */
    $"2200 24FC 4400 40E8 0010 E900 FB44 0042"            /* ".$üD.@è..é.ûD.B */
    $"EC22 0024 FC44 0040 E800 10E9 0000 04FC"            /* ì".$üD.@è..é...ü */
    $"4400 42EC 2200 24FC 44E7 000E E800 FC44"            /* D.Bì".$üDç..è.üD */
    $"0042 EC22 FC44 0040 E700 16E8 00FB 44FB"            /* .Bì"üD.@ç..è.ûDû */
    $"2201 2CC2 FC22 012C C2FB 22FC 4400 40E7"            /* ".,Âü".,Âû"üD.@ç */
    $"0018 E800 0004 FC44 FB22 012C C2FC 2201"            /* ..è...üDû".,Âü". */
    $"C3C2 FC22 0024 FC44 E600 26FE 0000 04FC"            /* ÃÂü".$üDæ.&þ...ü */
    $"44F0 0000 C4FD 44FB 2201 2C3C FD22 012C"            /* Dð..ÄýDû".,<ý"., */
    $"3CFB 2200 24FD 4400 C0F1 0000 04FC 44FC"            /* <û".$ýD.Àñ...üDü */
    $"0036 FE00 FF66 0064 FB44 FF00 000C F600"            /* .6þ.ÿf.dûDÿ...ö. */
    $"FFCC FE44 0042 FB22 01C3 CCFE 2201 C3C2"            /* ÿÌþD.Bû".ÃÌþ".ÃÂ */
    $"FB22 FE44 024C CCC0 F700 030C 0000 04FC"            /* û"þD.LÌÀ÷......ü */
    $"4403 4666 6660 FD00 3CFF 0003 0666 6664"            /* D.Fff`ý.<ÿ...ffd */
    $"FA44 03CC C5CC C0FC 0000 0CFE CC02 C777"            /* úD.ÌÅÌÀü...þÌ.Çw */
    $"CCFE 44FB 2201 2CC3 FDCC FB22 0524 4444"            /* ÌþDû".,ÃýÌû".$DD */
    $"4CC7 77FD CCFC 0004 04CC C5CC C4FB 4400"            /* LÇwýÌü...ÌÅÌÄûD. */
    $"46FE 66FD 0044 FF00 FE66 0064 FB44 004C"            /* Fþfý.Dÿ.þf.dûD.L */
    $"FE55 015C CCFE 0004 0CC9 9999 9CFE 77FF"            /* þU.\Ìþ...Éþwÿ */
    $"CC00 44FA 2200 2CFE CCFA 2206 244C CCC7"            /* Ì.Dú".,þÌú".$LÌÇ */
    $"7777 7CFE 9900 CCFE 0001 0CCC FE55 00C4"            /* ww|þ.Ìþ...ÌþU.Ä */
    $"FB44 0046 FE66 0040 FE00 3501 0004 FD66"            /* ûD.Fþf.@þ.5...ýf */
    $"FB44 004C FC55 FDCC FE99 009C FC77 FECC"            /* ûD.LüUýÌþ.üwþÌ */
    $"F222 FFCC 00C7 FD77 007C FE99 009C FECC"            /* ò"ÿÌ.Çýw.|þ.þÌ */
    $"00C5 FD55 005C FB44 0046 FE66 0060 FE00"            /* .ÅýU.\ûD.Fþf.`þ. */
    $"3101 0006 FD66 FB44 004C F955 005C FE99"            /* 1...ýfûD.LùU.\þ */
    $"009C F977 FFCC 00C2 F822 022C CCCC FA77"            /* .ùwÿÌ.Âø".,ÌÌúw */
    $"007C FE99 009C F955 005C FB44 FD66 0064"            /* .|þ.ùU.\ûDýf.d */
    $"FE00 2E01 0046 FD66 FB44 00C5 F955 005C"            /* þ....FýfûD.ÅùU.\ */
    $"FE99 009C F777 017C CCFB 2202 2CCC C7F8"            /* þ.÷w.|Ìû".,ÌÇø */
    $"7700 7CFE 9900 9CF8 5500 C4FC 44FC 66FE"            /* w.|þ.øU.ÄüDüfþ */
    $"002E 0000 FC66 FB44 00C5 F955 005C FD99"            /* ....üfûD.ÅùU.\ý */
    $"00C7 F877 027C 77C7 FD22 022C C77C F777"            /* .Çøw.|wÇý".,Ç|÷w */
    $"00C9 FE99 009C F855 00C4 FC44 FC66 FE00"            /* .Éþ.øU.ÄüDüfþ. */
    $"3000 00FC 66FC 4400 4CF8 5500 5CFD 9901"            /* 0..üfüD.LøU.\ý. */
    $"9CC7 F977 097C CC7C C722 222C C77C CCF8"            /* ÇùwÆ|Ì|Ç"",Ç|Ìø */
    $"7700 CCFD 9900 9CF8 5500 C4FC 44FC 66FE"            /* w.Ìý.øU.ÄüDüfþ */
    $"0031 0000 FC66 FC44 004C F855 005C FC99"            /* .1..üfüD.LøU.\ü */
    $"009C F977 097C 55CC 7C72 22C7 7CC5 5CF9"            /* .ùwÆ|UÌ|r"Ç|Å\ù */
    $"7700 7CFC 9900 9CF8 5500 C4FC 44FC 6602"            /* w.|ü.øU.ÄüDüf. */
    $"6000 0033 0006 FC66 FC44 004C F855 005C"            /* `..3..üfüD.LøU.\ */
    $"FB99 00CC FA77 0AC5 5555 CCC9 2C7C C555"            /* û.Ìúw.ÅUUÌÉ,|ÅU */
    $"55C7 FB77 017C C9FC 9900 9CF8 5500 C4FC"            /* UÇûw.|Éü.øU.Äü */
    $"44FC 6602 6000 0034 0006 FC66 FC44 004C"            /* Düf.`..4..üfüD.L */
    $"F855 005C FB99 01C5 C7FB 7700 C5FE 5502"            /* øU.\û.ÅÇûw.ÅþU. */
    $"CC9C C5FE 5500 C7FB 7701 C5C9 FC99 009C"            /* ÌÅþU.Çûw.ÅÉü. */
    $"F855 00C4 FC44 FC66 0260 0000 3600 06FC"            /* øU.ÄüDüf.`..6..ü */
    $"66FC 4400 4CF8 5500 5CFB 9902 C55C CCFD"            /* füD.LøU.\û.Å\Ìý */
    $"7700 CCFD 5501 C7CC FD55 005C FD77 037C"            /* w.ÌýU.ÇÌýU.\ýw.| */
    $"CC55 C9FC 9900 9CF8 5500 C4FC 44FC 6602"            /* ÌUÉü.øU.ÄüDüf. */
    $"6000 0038 0006 FC66 FC44 00C5 F855 005C"            /* `..8..üfüD.ÅøU.\ */
    $"FB99 06C5 5555 CCC7 77CC FC55 015C C5FC"            /* û.ÅUUÌÇwÌüU.\Åü */
    $"5507 CCC7 77CC C555 55C9 FC99 009C F855"            /* U.ÌÇwÌÅUUÉü.øU */
    $"005C FC44 0046 FD66 0260 0000 3600 06FD"            /* .\üD.Fýf.`..6..ý */
    $"6600 64FC 4400 C5F8 5500 5CFB 9900 C5FE"            /* f.düD.ÅøU.\û.Åþ */
    $"5501 5CCC FA55 00C5 FB55 015C CCFD 5500"            /* U.\ÌúU.ÅûU.\ÌýU. */
    $"C9FC 9900 9CF8 5500 5CFC 4400 46FD 6602"            /* Éü.øU.\üD.Fýf. */
    $"6400 002C 0046 FD66 0064 FC44 00C5 F855"            /* d..,.Fýf.düD.ÅøU */
    $"005C FB99 00C5 F555 00C5 F555 00C9 FC99"            /* .\û.ÅõU.ÅõU.Éü */
    $"009C F855 005C FC44 0046 FD66 0264 0000"            /* .øU.\üD.Fýf.d.. */
    $"2C00 46FD 6600 64FC 4400 C5F8 5500 5CFB"            /* ,.Fýf.düD.ÅøU.\û */
    $"9900 C5F5 5500 C5F5 5500 C9FC 9900 9CF8"            /* .ÅõU.ÅõU.Éü.ø */
    $"5500 5CFC 4400 46FD 6602 6400 002C 0046"            /* U.\üD.Fýf.d..,.F */
    $"FD66 0064 FC44 00C5 F855 005C FB99 00C5"            /* ýf.düD.ÅøU.\û.Å */
    $"F555 00C5 F555 00C9 FC99 009C F855 005C"            /* õU.ÅõU.Éü.øU.\ */
    $"FC44 0046 FD66 0264 0000 2400 46FD 6600"            /* üD.Fýf.d..$.Fýf. */
    $"64FC 4400 C5F8 5500 5CFB 99E7 CC00 C9FC"            /* düD.ÅøU.\ûçÌ.Éü */
    $"9900 9CF8 5500 5CFB 44FD 6602 6400 0024"            /* .øU.\ûDýf.d..$ */
    $"0006 FD66 FB44 00C5 F855 005C FB99 00C9"            /* ..ýfûD.ÅøU.\û.É */
    $"E899 00C9 FC99 009C F755 00C4 FC44 FD66"            /* è.Éü.÷U.ÄüDýf */
    $"0264 0000 2400 06FD 66FB 4400 C5F8 5500"            /* .d..$..ýfûD.ÅøU. */
    $"5CFB 9900 C9E8 9900 C9FC 9900 9CF7 5500"            /* \û.Éè.Éü.÷U. */
    $"C4FC 44FD 6602 6000 0024 0004 FD66 FB44"            /* ÄüDýf.`..$..ýfûD */
    $"00C5 F855 005C FB99 00C9 E899 00C9 FC99"            /* .ÅøU.\û.Éè.Éü */
    $"009C F755 00C4 FC44 FD66 0260 0000 2F00"            /* .÷U.ÄüDýf.`../. */
    $"04FD 66FB 4400 C5F8 5507 5C99 99CC CC99"            /* .ýfûD.ÅøU.\ÌÌ */
    $"99C9 FD99 F1CC 00C9 FD99 06C9 99CC CCC9"            /* ÉýñÌ.Éý.ÉÌÌÉ */
    $"999C F755 00C4 FC44 FD66 0240 0000 3300"            /* ÷U.ÄüDýf.@..3. */
    $"00FD 66FB 4400 C5F8 5507 5C99 9CC1 1CC9"            /* .ýfûD.ÅøU.\Á.É */
    $"99C9 FD99 00C0 F200 00C9 FD99 06C9 9CC1"            /* Éý.Àò..Éý.ÉÁ */
    $"11CC 999C F755 00C4 FC44 0046 FE66 0240"            /* .Ì÷U.ÄüD.Fþf.@ */
    $"0000 3304 0046 6666 64FB 4400 C5F8 5507"            /* ..3..FffdûD.ÅøU. */
    $"5C99 9C11 11C9 99C9 FD99 00C0 F200 00C9"            /* \..ÉÉý.Àò..É */
    $"FD99 06C9 9C11 111C 999C F755 00C4 FC44"            /* ý.É...÷U.ÄüD */
    $"0046 FE66 FE00 3104 0046 6666 64FB 4400"            /* .Fþfþ.1..FffdûD. */
    $"C5F8 5507 5C99 9C11 11C9 99C9 FD99 F1CC"            /* ÅøU.\..ÉÉýñÌ */
    $"00C9 FD99 06C9 9C11 111C 999C F855 005C"            /* .Éý.É...øU.\ */
    $"FA44 FF66 0064 FE00 3203 0004 6666 FA44"            /* úDÿf.dþ.2...ffúD */
    $"00C5 F855 075C 999C C11C C999 C9FD 9900"            /* .ÅøU.\Á.ÉÉý. */
    $"C5F2 5500 C9FD 9906 C99C C111 CC99 9CF8"            /* ÅòU.Éý.ÉÁ.Ìø */
    $"5500 5CFA 4402 4666 64FE 0032 FF00 0146"            /* U.\úD.Ffdþ.2ÿ..F */
    $"64FA 4400 C5F8 5507 5C99 99CC CC99 99C9"            /* dúD.ÅøU.\ÌÌÉ */
    $"FD99 00C5 F255 00C9 FD99 06C9 99CC CCC9"            /* ý.ÅòU.Éý.ÉÌÌÉ */
    $"999C F855 005C FA44 0246 6640 FE00 28FF"            /* øU.\úD.Ff@þ.(ÿ */
    $"0000 04F9 4400 C5F7 5500 C9FD 9900 9CFC"            /* ...ùD.Å÷U.Éý.ü */
    $"9900 C5F2 5500 C9FD 9900 9CFC 9900 C5F8"            /* .ÅòU.Éý.ü.Åø */
    $"5500 5CF8 44FD 002A FF00 0004 F944 004C"            /* U.\øDý.*ÿ...ùD.L */
    $"F755 005C FD99 00C9 FC99 00C5 F255 00C9"            /* ÷U.\ý.Éü.ÅòU.É */
    $"FC99 00C9 FE99 009C F755 005C F944 0040"            /* ü.Éþ.÷U.\ùD.@ */
    $"FD00 28FE 0000 04FA 4400 4CF7 5504 5CC9"            /* ý.(þ...úD.L÷U.\É */
    $"9999 9CFB 9900 C5F2 5500 C9FC 9900 9CFE"            /* û.ÅòU.Éü.þ */
    $"9900 CCF7 5500 5CF9 44FC 0026 FC00 FB44"            /* .Ì÷U.\ùDü.&ü.ûD */
    $"004C F755 04C9 9CCC CCC9 FB99 00C5 F255"            /* .L÷U.ÉÌÌÉû.ÅòU */
    $"00C9 FB99 FECC 009C F755 005C FB44 0040"            /* .ÉûþÌ.÷U.\ûD.@ */
    $"FB00 20FB 0000 04FD 4400 4CF7 5500 C9F7"            /* û. û...ýD.L÷U.É÷ */
    $"9900 C5F2 5500 C9F7 9900 C5F8 5500 5CFC"            /* .ÅòU.É÷.ÅøU.\ü */
    $"44F9 0020 F900 FD44 00C5 F855 00C9 F799"            /* Dù. ù.ýD.ÅøU.É÷ */
    $"00C5 F255 00C9 F799 00C5 F855 00C4 FE44"            /* .ÅòU.É÷.ÅøU.ÄþD */
    $"0040 F800 1AF5 0000 C5F8 5500 C9F7 9900"            /* .@ø..õ..ÅøU.É÷. */
    $"C5F2 5500 C9F7 9900 C5F8 5500 C0F4 001A"            /* ÅòU.É÷.ÅøU.Àô.. */
    $"F500 000C F955 005C F699 00C5 F255 00C9"            /* õ...ùU.\ö.ÅòU.É */
    $"F799 009C F955 005C F300 1CF4 0001 CCC5"            /* ÷.ùU.\ó..ô..ÌÅ */
    $"FB55 005C F699 00C5 F255 00C9 F799 009C"            /* ûU.\ö.ÅòU.É÷. */
    $"FA55 01CC C0F3 001F F300 030C CCCC C5FE"            /* úU.ÌÀó..ó...ÌÌÅþ */
    $"5500 C9F6 9900 C5F2 5500 C9F6 9900 C5FE"            /* U.Éö.ÅòU.Éö.Åþ */
    $"5502 5CCC CCF1 0016 F000 000C FECC F599"            /* U.\ÌÌñ..ð...þÌõ */
    $"00C5 F255 00C9 F699 009C FDCC EF00 12ED"            /* .ÅòU.Éö.ýÌï..í */
    $"0000 09F5 9900 C5F2 5500 C9F6 9900 C0EB"            /* ..Æõ.ÅòU.Éö.Àë */
    $"0012 ED00 0009 F599 00C5 F255 00C9 F699"            /* ..í..Æõ.ÅòU.Éö */
    $"009C EB00 10ED 00F4 9900 C5F2 5500 C9F6"            /* .ë..í.ô.ÅòU.Éö */
    $"9900 9CEB 0010 ED00 F499 00C5 F255 00C9"            /* .ë..í.ô.ÅòU.É */
    $"F699 009C EB00 10EE 0000 09F4 9900 C5F2"            /* ö.ë..î..Æô.Åò */
    $"5500 C9F5 99EB 0014 EE00 0009 F499 019C"            /* U.Éõë..î..Æô. */
    $"CCF5 5501 5CCC F499 00C0 EC00 14EE 0000"            /* ÌõU.\Ìô.Àì..î.. */
    $"09F2 9901 CCC5 F855 01CC C9F3 9900 C0EC"            /* Æò.ÌÅøU.ÌÉó.Àì */
    $"0013 EE00 0009 F199 019C C5FA 5500 CCF1"            /* ..î..Æñ.ÅúU.Ìñ */
    $"9900 C0EC 0014 EE00 0009 F099 019C CCFD"            /* .Àì..î..Æð.Ìý */
    $"5501 5CCC F099 00C0 EC00 12EE 0000 C9EE"            /* U.\Ìð.Àì..î..Éî */
    $"9904 CCC5 55CC C9EF 9900 9CEC 000D EE00"            /* .ÌÅUÌÉï.ì.Âî. */
    $"EC99 019C CCED 9900 9CEC 0008 EE00 D699"            /* ì.Ìí.ì..î.Ö */
    $"009C EC00 08EE 00D6 9900 9CEC 0006 EE00"            /* .ì..î.Ö.ì..î. */
    $"D599 EC00 08EE 00D5 9900 C0ED 0008 EE00"            /* Õì..î.Õ.Àí..î. */
    $"D599 00C0 ED00 08EE 00D5 9900 C0ED 0008"            /* Õ.Àí..î.Õ.Àí.. */
    $"EE00 D599 00C0 ED00 08EE 00D6 9900 9CEC"            /* î.Õ.Àí..î.Ö.ì */
    $"0008 EE00 D699 009C EC00 08EE 00D6 9900"            /* ..î.Ö.ì..î.Ö. */
    $"9CEC 000A EE00 00C9 D799 009C EC00 0AEE"            /* ì..î..É×.ì..î */
    $"0000 09D7 9900 9CEC 000A EE00 0009 D799"            /* ..Æ×.ì..î..Æ× */
    $"009C EC00 0AEE 0000 09D7 9900 9CEC 000A"            /* .ì..î..Æ×.ì.. */
    $"EE00 0009 D799 00C0 EC00 0AEE 0000 09D7"            /* î..Æ×.Àì..î..Æ× */
    $"9900 C0EC 000A EE00 0009 D799 0090 EC00"            /* .Àì..î..Æ×.ì. */
    $"0AEE 0000 09D7 9900 9CEC 0008 EE00 0009"            /* .î..Æ×.ì..î..Æ */
    $"D699 EC00 08EE 00D5 9900 C0ED 000A EF00"            /* Öì..î.Õ.Àí..ï. */
    $"0009 D599 0090 ED00 0AEF 0000 09D5 9900"            /* .ÆÕ.í..ï..ÆÕ. */
    $"9CED 0006 EF00 D399 ED00 08EF 00D3 9900"            /* í..ï.Óí..ï.Ó. */
    $"C0EE 000A F000 0009 D399 0090 EE00 0AF0"            /* Àî..ð..ÆÓ.î..ð */
    $"0000 09D3 9900 9CEE 0006 F000 D199 EE00"            /* ..ÆÓ.î..ð.Ñî. */
    $"0AF1 0000 0CD1 9900 C0EF 000B F100 010C"            /* .ñ...Ñ.Àï..ñ... */
    $"C9D2 9900 CCEF 000E F100 02CC ACCC D599"            /* ÉÒ.Ìï..ñ..Ì¬ÌÕ */
    $"029C CCAC EF00 16F1 0004 CAAA AACC C9ED"            /* .Ì¬ï..ñ..ÊªªÌÉí */
    $"9900 CCED 9904 CCCA AAAA C0F0 001A F200"            /* .Ìí.ÌÊªªÀð..ò. */
    $"000C FDAA 01AC C9F0 9903 9CCC 00CC EF99"            /* ..ýª.¬Éð.Ì.Ìï */
    $"00CC FDAA 00AC F000 1CF2 0000 CAFC AA01"            /* .Ìýª.¬ð..ò..Êüª. */
    $"ACC9 F299 019C C0FE 0000 CCF1 9900 CCFC"            /* ¬Éò.Àþ..Ìñ.Ìü */
    $"AA00 ACF0 001C F200 00CA FBAA 01AC CCF3"            /* ª.¬ð..ò..Êûª.¬Ìó */
    $"9900 C0FC 0000 C9F4 9901 9CCC FAAA 00C0"            /* .Àü..Éô.Ìúª.À */
    $"F100 1BF3 0000 0CF8 AA00 CCF5 9900 9CFB"            /* ñ..ó...øª.Ìõ.û */
    $"0000 09F5 9901 9CCA F9AA 00AC F100 1CF3"            /* ..Æõ.Êùª.¬ñ..ó */
    $"0000 0CF7 AA01 CCC9 F799 009C FB00 0009"            /* ...÷ª.ÌÉ÷.û..Æ */
    $"F699 01CC CAF8 AA00 ACF1 001B F300 00CA"            /* ö.ÌÊøª.¬ñ..ó..Ê */
    $"F6AA 01AC C9F8 9900 9CFB 0000 0CF7 9900"            /* öª.¬Éø.û...÷. */
    $"CCF6 AA00 ACF1 0019 F300 000C F5AA 01AC"            /* Ìöª.¬ñ..ó...õª.¬ */
    $"C9F9 9900 C0FA 00F8 9900 CCF5 AA00 ACF1"            /* Éù.Àú.ø.Ìõª.¬ñ */
    $"001A F200 00CA F5AA 01AC CCFA 9900 C0FA"            /* ..ò..Êõª.¬Ìú.Àú */
    $"00FA 9901 9CCC F4AA 00C4 F100 1BF3 0001"            /* .ú.Ìôª.Äñ..ó.. */
    $"044C F3AA 00CC FB99 00C0 FA00 FB99 019C"            /* .Lóª.Ìû.Àú.û. */
    $"CAF4 AA01 AC44 F100 1EF3 0003 0444 CCCA"            /* Êôª.¬Dñ..ó...DÌÊ */
    $"F4AA 00CC FC99 00C0 FA00 FC99 019C CAF4"            /* ôª.Ìü.Àú.ü.Êô */
    $"AA02 ACC4 44F1 0020 F300 FE44 014C CAF4"            /* ª.¬ÄDñ. ó.þD.LÊô */
    $"AA00 CCFD 9900 C0FA 00FD 9901 CCCA F4AA"            /* ª.Ìý.Àú.ý.ÌÊôª */
    $"04CC C444 4440 F200 1DF5 00FB 4401 4CCA"            /* .ÌÄDD@ò..õ.ûD.LÊ */
    $"F4AA 03CC C999 9CF9 0003 C999 99CC F3AA"            /* ôª.ÌÉù..ÉÌóª */
    $"00CC FA44 F400 1FF7 0000 04F9 4401 CCCA"            /* .ÌúDô..÷...ùD.ÌÊ */
    $"F4AA 02AC C99C F900 02C9 9CCC F3AA 00CC"            /* ôª.¬Éù..ÉÌóª.Ì */
    $"F844 0040 F600 1BF8 00F6 44FF CCF4 AA01"            /* øD.@ö..ø.öDÿÌôª. */
    $"ACCC F900 01C9 CAF4 AA01 ACCC F644 0040"            /* ¬Ìù..ÉÊôª.¬ÌöD.@ */
    $"F700 1BF9 00F4 4402 4CCC CAF5 AA00 ACF9"            /* ÷..ù.ôD.LÌÊõª.¬ù */
    $"0000 0CF4 AA01 CCC4 F444 0040 F800 19FA"            /* ...ôª.ÌÄôD.@ø..ú */
    $"0000 04F2 4401 CCCA F6AA 00AC F900 000C"            /* ...òD.ÌÊöª.¬ù... */
    $"F5AA 00CC F144 F800 17FA 00F0 44FF CCF7"            /* õª.ÌñDø..ú.ðDÿÌ÷ */
    $"AA00 ACF9 0000 0CF7 AA01 ACCC F044 F800"            /* ª.¬ù...÷ª.¬ÌðDø. */
    $"19FA 00EF 4402 4CCC CAF9 AA00 ACF9 0000"            /* .ú.ïD.LÌÊùª.¬ù.. */
    $"0CF8 AA01 CCC4 EF44 F800 1EFA 0002 4666"            /* .øª.ÌÄïDø..ú..Ff */
    $"64F0 44FF CCFA AA00 C0F8 0000 CAFB AA01"            /* dðDÿÌúª.Àø..Êûª. */
    $"ACCC EF44 0146 64F8 0021 FA00 0246 6666"            /* ¬ÌïD.Fdø.!ú..Fff */
    $"EF44 024C CCCA FCAA 00C0 F800 00CA FCAA"            /* ïD.LÌÊüª.Àø..Êüª */
    $"01CC C4EF 4402 4666 64F8 0020 FA00 0346"            /* .ÌÄïD.Ffdø. ú..F */
    $"6666 64EE 44FF CCFE AA00 ACF7 0000 0CFE"            /* ffdîDÿÌþª.¬÷...þ */
    $"AA01 ACCC ED44 FF66 0064 F800 21FA 0000"            /* ª.¬ÌíDÿf.dø.!ú.. */
    $"46FE 6600 64EE 44FF CC02 CAAA CCF7 0004"            /* Fþf.dîDÿÌ.ÊªÌ÷.. */
    $"0CAA AACC C4ED 4403 4666 6664 F800 18FA"            /* .ªªÌÄíD.Fffdø..ú */
    $"0000 46FD 66EC 44FF CC00 C0F6 00FF CCEB"            /* ..FýfìDÿÌ.Àö.ÿÌë */
    $"44FE 6600 64F8 0016 FA00 0046 FD66 EB44"            /* Dþf.dø..ú..FýfëD */
    $"0040 F400 EB44 0046 FE66 0064 F800 16FA"            /* .@ô.ëD.Fþf.dø..ú */
    $"0000 46FD 6600 64EC 44F3 0000 04EC 44FD"            /* ..Fýf.dìDó...ìDý */
    $"6600 64F8 0014 FA00 0006 FC66 EC44 F200"            /* f.dø..ú...üfìDò. */
    $"ED44 0046 FD66 0064 F800 16FA 0000 06FC"            /* íD.Fýf.dø..ú...ü */
    $"6600 64EE 4400 40F2 00ED 44FC 6600 60F8"            /* f.dîD.@ò.íDüf.`ø */
    $"0018 FA00 0004 FB66 EE44 0040 F200 0004"            /* ..ú...ûfîD.@ò... */
    $"EF44 0046 FC66 0060 F800 16F9 0000 44FC"            /* ïD.Füf.`ø..ù..Dü */
    $"6600 64EF 44F1 0000 04EF 44FC 6600 64F7"            /* f.dïDñ...ïDüf.d÷ */
    $"0017 F900 0144 46FC 66F0 4400 40F0 00F0"            /* ..ù..DFüfðD.@ð.ð */
    $"4400 46FC 6600 40F7 0016 F900 0104 44FC"            /* D.Füf.@÷..ù...Dü */
    $"6600 64F1 44EF 00F0 44FC 6601 6440 F700"            /* f.dñDï.ðDüf.d@÷. */
    $"17F8 0001 0446 FC66 F144 EF00 0004 F244"            /* .ø...FüfñDï...òD */
    $"0046 FC66 0044 F600 17F7 0001 0446 FD66"            /* .Füf.Dö..÷...Fýf */
    $"0064 F344 0040 EE00 F244 FC66 0044 F500"            /* .dóD.@î.òDüf.Dõ. */
    $"16F6 0001 4446 FD66 F344 ED00 F344 0046"            /* .ö..DFýfóDí.óD.F */
    $"FD66 0144 40F5 001A F600 0204 4444 FD66"            /* ýf.D@õ..ö...DDýf */
    $"F444 ED00 0004 F544 0046 FE66 0264 4444"            /* ôDí...õD.Fþf.dDD */
    $"F400 17F4 00FF 4403 4666 6664 F644 0040"            /* ô..ô.ÿD.FffdöD.@ */
    $"EC00 F544 FE66 FE44 F300 17F3 0004 0444"            /* ì.õDþfþDó..ó...D */
    $"4466 66F6 44EB 00F6 4405 4666 6444 4440"            /* DfföDë.öD.FfdDD@ */
    $"F200 18F2 0005 0444 4446 6664 F944 0040"            /* ò..ò...DDFfdùD.@ */
    $"EA00 F844 0146 66FE 44F0 0018 F100 0004"            /* ê.øD.FfþDð..ñ... */
    $"FD44 0066 FB44 E700 0004 FB44 0064 FE44"            /* ýD.fûDç...ûD.dþD */
    $"0040 EF00 0CEF 0000 04F9 44E4 00F9 44ED"            /* .@ï..ï...ùDä.ùDí */
    $"0000 00FF"                                          /* ...ÿ */
};

data 'PICT' (131) {
    $"144A 0000 0000 00C4 0086 0011 02FF 0C00"            /* .J.....Ä....ÿ.. */
    $"FFFF FFFF 0000 0000 0000 0000 0086 0000"            /* ÿÿÿÿ........... */
    $"00C4 0000 0000 0000 0001 000A 0000 0000"            /* .Ä.............. */
    $"00C4 0086 0098 8044 0000 0000 00C4 0086"            /* .Ä..D.....Ä. */
    $"0000 0000 0000 0000 0048 0000 0048 0000"            /* .........H...H.. */
    $"0000 0004 0001 0004 0000 0000 0107 5328"            /* ..............S( */
    $"0000 0000 0000 04D7 0000 0007 0000 FFFF"            /* .......×......ÿÿ */
    $"FFFF FFFF 0001 FFFF CCCC 3333 0002 0000"            /* ÿÿÿÿ..ÿÿÌÌ33.... */
    $"0000 0000 0003 FFFF 6666 6666 0004 0000"            /* ......ÿÿffff.... */
    $"9999 9999 0005 FFFF CCCC CCCC 0006 CCCC"            /* ..ÿÿÌÌÌÌ..ÌÌ */
    $"3333 3333 0007 3333 CCCC 9999 0000 0000"            /* 3333..33ÌÌ.... */
    $"00C4 0086 0000 0000 00C4 0086 0000 08FB"            /* .Ä......Ä....û */
    $"0000 11C5 0000 FF0A FC00 0201 1110 C600"            /* ...Å..ÿ.ü.....Æ. */
    $"00FF 0AFC 0002 F111 10C6 0000 FF09 FC00"            /* .ÿ.ü..ñ..Æ..ÿÆü. */
    $"010F 11C5 0000 FF08 FB00 00F1 C500 00CC"            /* ...Å..ÿ.û..ñÅ..Ì */
    $"04BE 0000 CC08 D800 0030 E800 00CC 08D8"            /* .¾..Ì.Ø..0è..Ì.Ø */
    $"0000 30E8 0000 CC08 D800 0033 E800 0099"            /* ..0è..Ì.Ø..3è.. */
    $"08D8 0000 33E8 0000 990D EA00 0103 30F1"            /* .Ø..3è..Âê...0ñ */
    $"0000 33E8 0000 990D EA00 0133 30F1 0000"            /* ..3è..Âê..30ñ.. */
    $"FFE8 0000 9909 EA00 0133 30D7 0000 6604"            /* ÿè..Æê..30×..f. */
    $"BE00 0066 04BE 0000 6604 BE00 0066 04BE"            /* ¾..f.¾..f.¾..f.¾ */
    $"0000 3304 BE00 0033 04BE 0000 3308 E000"            /* ..3.¾..3.¾..3.à. */
    $"0011 E000 0033 08E1 0002 0111 10E0 0008"            /* ..à..3.á.....à.. */
    $"E100 0201 1110 E000 08E1 0002 0F11 F0E0"            /* á.....à..á....ðà */
    $"000B E000 00FF FB00 0104 40E7 0009 D900"            /* ..à..ÿû...@ç.ÆÙ. */
    $"0144 F4E8 0000 220B F200 0044 E900 0144"            /* .Dôè..".ò..Dé..D */
    $"44E7 000C F300 0204 4440 E900 0040 E700"            /* Dç..ó...D@é..@ç. */
    $"0AF3 0002 0444 40CF 0000 7708 F200 0044"            /* .ó...D@Ï..w.ò..D */
    $"CE00 00FF 09E7 0001 0550 DA00 0066 0EE7"            /* Î..ÿÆç...PÚ..f.ç */
    $"0001 0555 EB00 0111 F0F2 0000 FF0F E700"            /* ...Uë...ðò..ÿ.ç. */
    $"0150 55EC 0002 0111 11F2 0000 660F E700"            /* .PUì.....ò..f.ç. */
    $"0105 50EC 0002 0111 11F2 0000 FF09 CF00"            /* ..Pì.....ò..ÿÆÏ. */
    $"0111 F0F2 0000 6604 BE00 00FF 04BE 0000"            /* ..ðò..f.¾..ÿ.¾.. */
    $"6604 BE00 00FF 04BE 0000 660D F000 010F"            /* f.¾..ÿ.¾..fÂð... */
    $"F0F5 0000 03DE 0000 FF18 F000 00F0 FB00"            /* ðõ...Þ..ÿ.ð..ðû. */
    $"0304 4444 40FE 0000 30F7 0001 055F EA00"            /* ..DD@þ..0÷..._ê. */
    $"0066 10E9 0003 4414 1440 F300 0155 55EA"            /* .f.é..D..@ó..UUê */
    $"0000 FF10 E900 0341 4331 44F3 0001 0555"            /* ..ÿ.é..AC1Dó...U */
    $"EA00 0066 17F1 0000 F0FA 0006 4433 3414"            /* ê..f.ñ..ðú..D34. */
    $"0000 0FF6 0001 0550 EA00 00FF 19F1 0000"            /* ...ö...Pê..ÿ.ñ.. */
    $"F0FE 0007 4000 0001 4130 0041 FC00 0244"            /* ðþ..@...A0.Aü..D */
    $"4440 E200 0066 19F2 0001 0FFF FB00 0504"            /* D@â..f.ò...ÿû... */
    $"1433 3014 40FE 0003 4413 1314 E200 00FF"            /* .30.@þ..D...â..ÿ */
    $"19F2 0000 0FFA 0005 0141 4330 4140 FE00"            /* .ò...ú...AC0A@þ. */
    $"0441 3130 3140 E300 0066 18F2 0000 0FF9"            /* .A101@ã..f.ò...ù */
    $"000C 1413 0004 1000 0004 1310 0303 10E3"            /* ...............ã */
    $"0000 FF11 E600 0901 4400 0004 3130 0031"            /* ..ÿ.æ.Æ.D...10.1 */
    $"30E3 0000 6614 E900 0C04 4400 0F14 0000"            /* 0ã..f.é...D..... */
    $"4413 0000 0444 E300 00FF 16EA 000E 4443"            /* D....Dã..ÿ.ê..DC */
    $"1340 01F4 4000 4130 4444 4141 44E4 0000"            /* .@.ô@.A0DDAADä.. */
    $"6618 EB00 0A01 4131 3140 001F 4004 1344"            /* f.ë...A11@..@..D */
    $"FE41 0204 1440 E500 00FF 18EB 000B 0343"            /* þA...@å..ÿ.ë...C */
    $"1313 4F00 4F40 4131 4410 FE00 0141 44E5"            /* ..O.O@A1D.þ..ADå */
    $"0000 661F F000 0030 FD00 0C31 4400 013F"            /* ..f.ð..0ý..1D..? */
    $"003F 1443 1410 0030 FE00 0014 F500 010F"            /* .?.C...0þ...õ... */
    $"03F2 0021 F100 0003 FD00 0D03 1310 0003"            /* .ò.!ñ...ý.Â..... */
    $"14F0 3344 4141 0000 33FE 0000 44F5 0002"            /* .ð3DAA..3þ..Dõ.. */
    $"0F03 33F3 001D F100 0030 FD00 0101 30FE"            /* ..3ó..ñ..0ý...0þ */
    $"0005 344F 0334 4410 FB00 0014 F400 01F0"            /* ..4O.4D.û...ô..ð */
    $"33F3 0022 F100 0130 01FE 0000 03FD 000C"            /* 3ó."ñ..0.þ...ý.. */
    $"0341 F034 3130 4440 0000 1400 41F4 0001"            /* .Að410D@....Aô.. */
    $"F030 F400 0022 1DF1 0001 3330 FD00 1030"            /* ð0ô..".ñ..30ý..0 */
    $"00FF F000 331F 3413 FF11 1140 0004 4444"            /* .ÿð.3.4.ÿ..@..DD */
    $"E500 0044 15EA 000F 0444 4FFF 0331 311F"            /* å..D.ê...DOÿ.11. */
    $"4411 1144 0001 4141 E400 2203 0000 F111"            /* D..D..AAä."...ñ. */
    $"FC00 0105 50F6 0010 4441 4144 4FF5 3341"            /* ü...Pö..DAADOõ3A */
    $"F411 1001 1440 0414 10E5 0000 0A22 0300"            /* ô....@...å...".. */
    $"0F11 11FC 0001 3FF3 F700 0904 1414 1000"            /* ...ü..?ó÷.Æ..... */
    $"4444 3311 14FE 0001 1144 FC00 0004 E700"            /* DD3..þ...Dü...ç. */
    $"2303 000F 1111 FC00 0133 33F7 0002 4141"            /* #.....ü..33÷..AA */
    $"40FE 0003 44F1 4F44 FE00 0201 1440 FD00"            /* @þ..DñODþ....@ý. */
    $"0040 E700 2303 000F 1110 FC00 0103 30F7"            /* .@ç.#.....ü...0÷ */
    $"0001 1410 FE00 0E14 1441 1F14 000F FF00"            /* ....þ....A....ÿ. */
    $"1140 4400 0004 E600 20ED 0001 0141 FE00"            /* .@D...æ. í...Aþ. */
    $"0D03 3001 4F1F 100F 0333 F004 0000 40F4"            /* Â.0.O....3ð...@ô */
    $"0002 FFFF F0F5 0000 C221 EC00 0010 FE00"            /* ..ÿÿðõ..Â!ì...þ. */
    $"093F 3335 144F FF3F F113 3FFE 0000 40F5"            /* Æ?35.Oÿ?ñ.?þ..@õ */
    $"0006 0FF0 00F0 0060 60F7 0020 EC00 1040"            /* ...ð.ð.``÷. ì..@ */
    $"0000 33FF F444 1341 FF31 3111 33F0 0004"            /* ..3ÿôD.Aÿ11.3ð.. */
    $"F300 020F 000F FE06 F800 000A 1DEC 000E"            /* ó.....þ.ø....ì.. */
    $"0400 05FF 0001 04F4 3F13 1000 0113 3FF1"            /* ...ÿ...ô?.....?ñ */
    $"0003 0F00 0F00 FE60 F800 1DEA 000D 0F01"            /* ......þ`ø..ê.Â.. */
    $"1103 334F 433F F000 0331 13F0 F100 04F0"            /* ..3OC?ð..1.ðñ..ð */
    $"00F0 0606 F800 00C2 20EA 0007 FF11 FF33"            /* .ð..ø..Â ê..ÿ.ÿ3 */
    $"3334 FF1F FE00 0203 1130 FE00 000F F500"            /* 34ÿ.þ....0þ...õ. */
    $"05F0 00F0 0060 60F8 001C EB00 0E0F F110"            /* .ð.ð.``ø..ë...ñ. */
    $"0333 4343 4F31 44FF 0000 3133 F100 040F"            /* .3CCO1Dÿ..13ñ... */
    $"00F0 0606 F700 1DEB 000E 0F10 0003 3430"            /* .ð..÷..ë......40 */
    $"043F 1313 44FF 0001 13F1 0005 0F00 F000"            /* .?..Dÿ...ñ....ð. */
    $"6060 F800 22EB 000E 0110 0003 4300 33F1"            /* ``ø."ë......C.3ñ */
    $"1331 3144 F000 11F1 0004 0F00 F006 06FE"            /* .11Dð..ñ....ð..þ */
    $"0000 04FC 0000 FF20 EB00 0D01 0000 3340"            /* ...ü..ÿ ë.Â...3@ */
    $"0444 1F1F 0313 1440 0FF0 0002 0F00 F0FE"            /* .D.....@.ð....ðþ */
    $"6003 0000 0440 FC00 23EB 000C 0104 3434"            /* `....@ü.#ë....44 */
    $"0114 FFFF 1FF0 0131 34F4 0000 11FD 0004"            /* ..ÿÿ.ð.14ô...ý.. */
    $"0F00 F006 06FE 0001 0440 FC00 23E9 000B"            /* ..ð..þ...@ü.#é.. */
    $"4F00 014F 5F53 1FF0 0013 1340 F600 0201"            /* O..O_S.ð...@ö... */
    $"1110 FE00 040F 00F0 6060 FE00 0004 FB00"            /* ..þ....ð``þ...û. */
    $"23F4 0000 44F7 000B F001 14F5 5F31 15F0"            /* #ô..D÷..ð..õ_1.ð */
    $"0001 3140 F600 0201 1111 FE00 040F 00F6"            /* ..1@ö.....þ....ö */
    $"0606 F700 23F5 0002 0444 40F7 0009 110F"            /* ..÷.#õ...D@÷.Æ.. */
    $"55FF 5153 FF00 0013 F500 020F 1111 FE00"            /* UÿQSÿ...õ.....þ. */
    $"040F 00F0 6060 F700 21F5 0002 0444 40F7"            /* ...ð``÷.!õ...D@÷ */
    $"0009 1105 55F5 3535 FF00 0001 F400 01F1"            /* .Æ..Uõ55ÿ...ô..ñ */
    $"1FFE 0003 0F06 F606 F600 1FF4 0001 44F0"            /* .þ....ö.ö..ô..Dð */
    $"F700 0801 F55F F353 530F 00F0 F300 010F"            /* ÷...õ_óSS..ðó... */
    $"F0FE 0003 F00F 6060 F600 12E7 0006 055F"            /* ðþ..ð.``ö..ç..._ */
    $"F535 355F F0ED 0002 F006 06F5 0013 E700"            /* õ55_ðí..ð..õ..ç. */
    $"0105 5FFE 5301 05F0 EE00 030F 0060 60F5"            /* .._þS..ðî....``õ */
    $"0018 FB00 0033 EE00 0605 FF55 3555 50F0"            /* ..û..3î...ÿU5UPð */
    $"EE00 020F 06F6 F500 00C2 17FB 0001 3330"            /* î....öõ..Â.û..30 */
    $"EF00 0655 FF55 5355 35F0 EE00 02F0 6F60"            /* ï..UÿUSU5ðî..ðo` */
    $"F400 17FC 0001 0330 EE00 0155 F5FE 5501"            /* ô..ü...0î..UõþU. */
    $"300F EF00 020F 06FF F300 17FC 0001 0333"            /* 0.ï....ÿó..ü...3 */
    $"EE00 0155 F5FE 5501 500F EF00 02F0 6FF0"            /* î..UõþU.P.ï..ðoð */
    $"F300 18EB 0005 0330 0000 5FF5 FE55 0150"            /* ó..ë...0.._õþU.P */
    $"0FF0 0002 0FF6 FFF3 0000 0A1C EF00 0030"            /* .ð...öÿó....ï..0 */
    $"FE00 0403 0000 055F FD55 0250 0FF0 F300"            /* þ......_ýU.P.ðó. */
    $"0406 06FF 6FF0 F200 1CF0 0000 03FA 0001"            /* ...ÿoðò..ð...ú.. */
    $"055F FD55 0250 00F0 F200 036F F0FF F0F9"            /* ._ýU.P.ðò..oðÿðù */
    $"0000 F0FB 001B F000 0033 FA00 0105 5FFC"            /* ..ðû..ð..3ú..._ü */
    $"5501 00F0 F300 0306 FFFF F6F8 0000 F0FB"            /* U..ðó...ÿÿöø..ðû */
    $"001D F000 0030 FA00 0155 FFFE 5503 5F55"            /* ..ð..0ú..UÿþU._U */
    $"00FF F200 03FF 0060 60F9 0000 F0FB 001D"            /* .ÿò..ÿ.``ù..ðû.. */
    $"F000 0030 FA00 0155 FFFE 5503 5F55 000F"            /* ð..0ú..UÿþU._U.. */
    $"F200 030F F006 06F9 0000 F0FB 0019 F000"            /* ò...ð..ù..ðû..ð. */
    $"0030 FA00 0155 F5FE 5503 1F55 000F F100"            /* .0ú..UõþU..U..ñ. */
    $"03FF 0060 60F3 001E F000 0030 FB00 0905"            /* .ÿ.``ó..ð..0û.Æ. */
    $"55F5 5555 5F1F F550 0FF1 0003 0FF0 0606"            /* UõUU_.õP.ñ...ð.. */
    $"FB00 000F FA00 1BE9 0009 055F F555 55F1"            /* û...ú..é.Æ._õUUñ */
    $"1FF5 500F F100 030F FF00 60FB 0001 F110"            /* .õP.ñ...ÿ.`û..ñ. */
    $"FB00 1DE9 0001 555F FE55 05F1 11F5 500F"            /* û..é..U_þU.ñ.õP. */
    $"F0F1 0002 FFF6 06FB 0001 F111 FC00 00FF"            /* ðñ..ÿö.û..ñ.ü..ÿ */
    $"1AE9 000A 555F 5555 5F11 11F5 5000 F0F1"            /* .é..U_UU_..õP.ðñ */
    $"0002 FFF0 60FB 0000 0FFA 0018 E900 0A55"            /* ..ÿð`û...ú..é..U */
    $"FF55 5FF1 1111 F550 00F0 F200 0260 F0F6"            /* ÿU_ñ..õP.ðò..`ðö */
    $"F300 00C2 1CE9 000A 55F5 5355 F111 11F5"            /* ó..Â.é..UõSUñ..õ */
    $"5500 FFFE 0001 3FF0 F900 FE06 01FF 60F2"            /* U.ÿþ..?ðù.þ..ÿ`ò */
    $"001D EA00 0B05 55F5 5535 5F11 11F5 5500"            /* ..ê...UõU5_..õU. */
    $"0FFE 0001 FFF0 F900 0360 FF6F FFF1 0026"            /* .þ..ÿðù..`ÿoÿñ.& */
    $"F900 0044 F300 0B05 55F5 5553 55F1 11FF"            /* ù..Dó...UõUSUñ.ÿ */
    $"5500 0FFE 0004 FFF0 0000 03FC 0003 06FF"            /* U..þ..ÿð...ü...ÿ */
    $"FFF6 F200 00FF 27FA 0001 0444 F300 0155"            /* ÿöò..ÿ'ú...Dó..U */
    $"5FFD 5505 5F11 FF55 500F FE00 05FF F000"            /* _ýU._.ÿUP.þ..ÿð. */
    $"0033 30FC 0003 FFF0 0060 F300 0099 25FA"            /* .30ü..ÿð.`ó..%ú */
    $"0002 0404 40F4 0001 555F FD55 0E5F F11F"            /* ....@ô..U_ýU._ñ. */
    $"5550 0FF0 0000 F0F0 000F 3330 FB00 02FF"            /* UP.ð..ðð..30û..ÿ */
    $"0006 F200 2901 4055 FB00 0004 F400 0205"            /* ..ò.).@Uû...ô... */
    $"555F FC55 08FF 1F55 5000 F000 00FF FE00"            /* U_üU.ÿ.UP.ð..ÿþ. */
    $"01F3 33FB 0003 0FF0 6060 F400 0099 2602"            /* .ó3û...ð``ô..&. */
    $"4555 50F6 0000 05FA 0002 0555 FFFC 550D"            /* EUPö...ú...UÿüUÂ */
    $"5FFF 5550 00F0 0000 0FF0 0000 0F33 FA00"            /* _ÿUP.ð...ð...3ú. */
    $"01FF 06F2 0026 0205 5550 F600 0155 50FB"            /* .ÿ.ò.&..UPö..UPû */
    $"0002 0555 FFFC 5505 5FFF 5555 00F0 FA00"            /* ...UÿüU._ÿUU.ðú. */
    $"00F0 FA00 02F0 6060 F400 0099 1E02 0055"            /* .ðú..ð``ô.....U */
    $"F0F6 0000 55FA 0002 5555 F5FB 5504 5F55"            /* ðö..Uú..UUõûU._U */
    $"5500 FFF3 0002 0FFF 06F2 001E F400 0105"            /* U.ÿó...ÿ.ò..ô... */
    $"55FE 0000 0FFE 0002 5555 F5F8 5501 000F"            /* Uþ...þ..UUõøU... */
    $"F300 026F 6060 F300 0099 17EF 0000 F1FE"            /* ó..o``ó...ï..ñþ */
    $"0002 5555 F5F8 5501 300F F400 020F FFF0"            /* ..UUõøU.0.ô...ÿð */
    $"F100 1CF0 0007 0F11 0000 0555 5FF5 F955"            /* ñ..ð.......U_õùU */
    $"0353 300F F0F5 0002 0FFF 60F2 0000 9919"            /* .S0.ðõ...ÿ`ò... */
    $"F000 060F 1100 0005 555F F855 0333 000F"            /* ð.......U_øU.3.. */
    $"F0F5 0002 0F06 06F1 0018 EC00 0205 555F"            /* ðõ.....ñ..ì...U_ */
    $"F955 0453 3533 00F0 F500 020F FF60 F200"            /* ùU.S53.ðõ...ÿ`ò. */
    $"0099 13EC 0002 5555 F5F8 5503 5330 00FF"            /* ..ì..UUõøU.S0.ÿ */
    $"F400 00FF F000 13EC 0002 5555 F5F8 5503"            /* ô..ÿð..ì..UUõøU. */
    $"3350 00FF F400 000F F000 0FEC 0002 5555"            /* 3P.ÿô...ð..ì..UU */
    $"F5F6 5501 000F E300 0088 18ED 0005 0555"            /* õöU...ã...í...U */
    $"5F55 51FF F855 0200 0FF0 FB00 0104 40EC"            /* _UQÿøU...ðû...@ì */
    $"0000 AA18 ED00 0505 555F 5554 1FF8 5502"            /* ..ª.í...U_UT.øU. */
    $"000F F0FB 0001 0440 EC00 00FF 17ED 0006"            /* ..ðû...@ì..ÿ.í.. */
    $"0555 5F55 51FF F5F9 5502 0000 F0FB 0001"            /* .U_UQÿõùU...ðû.. */
    $"F44F EB00 17ED 0006 5555 F555 1F41 F5F9"            /* ôOë..í..UUõU.Aõù */
    $"5502 5000 FFFB 0001 F44F EB00 1BFA 0000"            /* U.P.ÿû..ôOë..ú.. */
    $"33F5 0006 5555 F141 4F14 F5F9 5502 5000"            /* 3õ..UUñAO.õùU.P. */
    $"FFFB 0001 0FFF EB00 1CFB 0002 0333 30F6"            /* ÿû...ÿë..û...30ö */
    $"0006 5555 FFF4 1F41 4FF9 5502 5000 0FFA"            /* ..UUÿô.AOùU.P..ú */
    $"0000 F0EB 001E FA00 0133 30F6 0007 5555"            /* ..ðë..ú..30ö..UU */
    $"F41F FF14 1FF5 F955 0200 0FF0 F200 020F"            /* ô.ÿ..õùU...ðò... */
    $"0330 F600 1EFA 0000 33F6 0003 0555 5FFF"            /* .0ö..ú..3ö...U_ÿ */
    $"FE41 004F FDFF FC55 0200 0FF0 F200 010F"            /* þA.OýÿüU...ðò... */
    $"33F5 001A EE00 0305 555F 5FFC 1402 155F"            /* 3õ..î...U__ü..._ */
    $"F5FC 5502 0000 F0F2 0001 0F33 F500 1AEE"            /* õüU...ðò...3õ..î */
    $"0004 0555 5F55 F1FD 4101 55FF FB55 0200"            /* ...U_UñýA.UÿûU.. */
    $"00FF F200 010F FFF5 001A F300 00F0 FD00"            /* .ÿò...ÿõ..ó..ðý. */
    $"0455 55FF 54FF FE14 0215 5FF5 FB55 0250"            /* .UUÿTÿþ..._õûU.P */
    $"00FF E400 1BF3 0000 0FFD 0009 5555 F551"            /* .ÿä..ó...ý.ÆUUõQ */
    $"4F41 4145 55FF FB55 0444 4000 0FF0 E500"            /* OAAEUÿûU.D@..ðå. */
    $"1EF3 0000 F0FE 000A 0555 55F5 54F4 1414"            /* .ó..ðþ...UUõTô.. */
    $"155F F5FB 5504 4444 000F F0E6 0000 0722"            /* ._õûU.DD..ðæ..." */
    $"F300 000F FE00 0505 555F F541 F1FE 4101"            /* ó...þ...U_õAñþA. */
    $"5FF5 FC55 0554 4444 400F F0EE 0001 F555"            /* _õüU.TDD@.ðî..õU */
    $"FA00 2E03 0000 1111 F700 0E0F F000 0055"            /* ú.......÷...ð..U */
    $"555F 551F 141F 1F14 15FF FC55 0544 4555"            /* U_U......ÿüU.DEU */
    $"4400 FFF8 0000 01F8 0002 5555 50FC 0000"            /* D.ÿø...ø..UUPü.. */
    $"0A2E 0300 0011 11F7 000E 0F33 0000 5555"            /* .......÷...3..UU */
    $"5F55 4F41 FFF1 FF45 FFFC 5505 4555 5504"            /* _UOAÿñÿEÿüU.EUU. */
    $"40FF F900 0201 1110 F900 0255 5550 FB00"            /* @ÿù.....ù..UUPû. */
    $"3003 0000 1110 F700 0E03 3330 0055 55FF"            /* 0.....÷...30.UUÿ */
    $"55F4 1FF5 5514 F45F FD55 0654 4554 4440"            /* Uô.õU.ô_ýU.TETD@ */
    $"40FF F900 0201 1110 F900 01F5 55FB 0000"            /* @ÿù.....ù..õUû.. */
    $"FF29 F300 0F33 3300 0555 55FF 51F5 FF54"            /* ÿ)ó..33..UUÿQõÿT */
    $"5555 4FFF F5FE 5506 5455 4555 4040 0FF9"            /* UUOÿõþU.TUEU@@.ù */
    $"0001 0F01 F800 010F FFFA 0020 F300 0F03"            /* ....ø...ÿú. ó... */
    $"3000 0555 55F5 555F 5545 5555 541F F5FE"            /* 0..UUõU_UEUUT.õþ */
    $"5507 4454 5544 4004 0FF0 E600 1CF3 0009"            /* U.DTUD@..ðæ..ó.Æ */
    $"0300 0055 555F F555 F554 F855 0744 5455"            /* ...UU_õUõTøU.DTU */
    $"4440 040F F0E7 0000 C217 F000 0655 555F"            /* D@..ðç..Â.ð..UU_ */
    $"F555 5545 F855 0744 5455 5545 040F F0E6"            /* õUUEøU.DTUUE..ðæ */
    $"0014 F100 0305 5555 5FF4 5501 4454 FE55"            /* ..ñ...UU_ôU.DTþU */
    $"0244 00FF E600 14F1 0003 0555 55FF F455"            /* .D.ÿæ..ñ...UUÿôU */
    $"0744 5444 5554 4400 FFE6 0017 F800 0044"            /* .DTDUTD.ÿæ..ø..D */
    $"FB00 FE55 00FF F455 0744 5544 4554 0000"            /* û.þU.ÿôU.DUDET.. */
    $"FFE6 001F F900 0104 44FB 00FE 5500 F5F4"            /* ÿæ..ù...Dû.þU.õô */
    $"5508 5445 5544 4450 00FF F0EF 0002 1111"            /* U.TEUDDP.ÿðï.... */
    $"10FC 0024 F900 0104 44FB 0003 5555 5FF5"            /* .ü.$ù...Dû..UU_õ */
    $"F455 0154 44FE 5503 0440 0FF0 F000 0001"            /* ôU.TDþU..@.ðð... */
    $"FE11 0010 FE00 0007 27F8 0000 40FC 0003"            /* þ...þ...'ø..@ü.. */
    $"0555 555F F355 0854 4445 5555 4440 0FF0"            /* .UU_óU.TDEUUD@.ð */
    $"FD00 0001 FE11 F800 0411 111F FFFF FD00"            /* ý...þ.ø.....ÿÿý. */
    $"25F2 0006 0555 55FF 5F55 5FF5 5507 4444"            /* %ò...UUÿ_U_õU.DD */
    $"5554 4400 0FFF FD00 FC11 F900 0811 11F1"            /* UTD..ÿý.ü.ù....ñ */
    $"1111 FF00 0007 2AF2 00FE 5503 FF55 F5F5"            /* ..ÿ...*ò.þU.ÿUõõ */
    $"F655 0156 54FE 4403 4500 00FF FD00 0111"            /* öU.VTþD.E..ÿý... */
    $"11FE FF00 F1FA 0006 111F F111 1110 F0FF"            /* .þÿ.ñú....ñ...ðÿ */
    $"0029 F200 FE55 02F5 555F F455 0065 FE44"            /* .)ò.þU.õU_ôU.eþD */
    $"0345 0000 FFFD 0001 111F FE11 011F F0FB"            /* .E..ÿý....þ...ðû */
    $"0008 111F 1FF1 FF10 0F00 072D F200 0655"            /* .....ñÿ....-ò..U */
    $"555F F555 F5F5 F555 0856 5544 4455 0000"            /* U_õUõõõU.VUDDU.. */
    $"FFF0 FE00 0711 0F00 0001 111F F0FC 0006"            /* ÿðþ.........ðü.. */
    $"111F 11FF F1F0 0FFF 002D F300 0705 5555"            /* ...ÿñð.ÿ.-ó...UU */
    $"5FF5 5F55 5FF4 5500 65FE 5503 5000 0FF0"            /* _õ_U_ôU.eþU.P..ð */
    $"FE00 0111 1FFE FF02 F001 1FFC 0008 011F"            /* þ....þÿ.ð..ü.... */
    $"1101 F11F 0FF0 0026 F300 0405 5555 5FF5"            /* ..ñ..ð.&ó...UU_õ */
    $"ED55 0350 000F F0FE 0002 111F F0FE 0F02"            /* íU.P..ðþ....ðþ.. */
    $"0011 F0FC 0007 0F00 01F1 10FF 0F00 2FFD"            /* ..ðü.....ñ.ÿ../ý */
    $"0001 0111 F900 0305 5555 FFF8 5501 5FFF"            /* ....ù...UUÿøU._ÿ */
    $"F755 0350 000F F0FE 0002 111F 0FFE F003"            /* ÷U.P..ðþ.....þð. */
    $"FF00 1FF0 FC00 06FF FFF1 10FF F000 29F3"            /* ÿ..ðü..ÿÿñ.ÿð.)ó */
    $"00FE 5500 FFF8 5502 FF5F F5F7 5502 000F"            /* .þU.ÿøU.ÿ_õ÷U... */
    $"FFFE 000A 011F 000F FF00 0FFF 001F 10FE"            /* ÿþ......ÿ..ÿ...þ */
    $"00FD 1103 1F0F 0F00 26F3 0003 5555 5FF5"            /* .ý......&ó..UU_õ */
    $"F855 FEFF F755 0200 00FF FD00 090F 0000"            /* øUþÿ÷U...ÿý.Æ... */
    $"0F00 00F0 F001 FFFB 1104 1FF0 0FF0 0030"            /* ...ðð.ÿû...ð.ð.0 */
    $"F500 0540 0555 555F F5FB 5505 FFF5 55FF"            /* õ..@.UU_õûU.ÿõUÿ */
    $"555F F755 0300 00FF F0FD 0009 FF00 0F0F"            /* U_÷U...ÿðý.Æÿ... */
    $"0000 0FF0 11FF FE11 061F FFF0 000F 0F00"            /* ...ð.ÿþ...ÿð.... */
    $"36F7 00FE 0404 0555 55FF F5FC 5507 5FFF"            /* 6÷.þ...UUÿõüU._ÿ */
    $"FF55 FF55 5665 FC55 0753 3FF5 55F0 00FF"            /* ÿUÿUVeüU.S?õUð.ÿ */
    $"F0FC 0002 FFF0 F0FE 0002 FF00 11FE FF06"            /* ðü..ÿððþ..ÿ..þÿ. */
    $"F000 000F F0F0 0034 F700 0640 4FFF FFF5"            /* ð...ðð.4÷..@Oÿÿõ */
    $"55FF FB55 07FF F55F FFFF 5555 66FC 5507"            /* UÿûU.ÿõ_ÿÿUUfüU. */
    $"33F3 3F5F FF00 0FF0 FC00 FE0F FE00 0C0F"            /* 3ó?_ÿ..ðü.þ.þ... */
    $"F000 1111 1000 000F FF0F 0F07 3900 10F9"            /* ð.......ÿ...9..ù */
    $"0007 040F FFF0 05F5 55FF FE55 0AFF 5555"            /* ....ÿð.õUÿþU.ÿUU */
    $"FFF5 55FF F555 5556 FD55 0853 3F33 3FF3"            /* ÿõUÿõUUVýU.S?3?ó */
    $"3FF0 0FFF FB00 01F0 F0FD 0001 0FF0 FD00"            /* ?ð.ÿû..ððý...ðý. */
    $"00FF FDF0 0000 2F00 10F9 000E 40FF 4000"            /* .ÿýð../..ù..@ÿ@. */
    $"00F5 5FF5 5555 5FFF FF5F FFF5 550B 33F3"            /* .õ_õUU_ÿÿ_ÿõU.3ó */
    $"3333 350F 0FFF 0000 0555 F800 000F FDFF"            /* 335..ÿ...Uø...ýÿ */
    $"FE0F 0200 0007 2D00 10FC 0011 0400 040F"            /* þ.....-..ü...... */
    $"F400 FFFF F55F F555 555F F55F FFF5 F555"            /* ô.ÿÿõ_õUU_õ_ÿõõU */
    $"0753 3F33 335F FF00 FFFE 0001 55F0 F800"            /* .S?33_ÿ.ÿþ..Uðø. */
    $"FAF0 FE00 2C00 F0FA 000E 404F 40FF 0000"            /* úðþ.,.ðú..@O@ÿ.. */
    $"F55F F555 55FF 5555 FFF4 550C 333F 3333"            /* õ_õUUÿUUÿôU.3?33 */
    $"FF00 00FF F000 00FF F0F8 00FC 0FFD 0000"            /* ÿ..ÿð..ÿðø.ü.ý.. */
    $"0720 0010 FA00 0204 FF0F FE00 0505 FF55"            /* . ..ú...ÿ.þ...ÿU */
    $"555F F5F2 5509 333F F333 335F F000 FFF0"            /* U_õòUÆ3?ó33_ð.ÿð */
    $"EA00 1AF9 0002 40FF F0FD 0000 FFEF 550A"            /* ê..ù..@ÿðý..ÿïU. */
    $"5333 F333 3F33 35FF 000F F0EA 001B FA00"            /* S3ó3?35ÿ..ðê..ú. */
    $"0204 04FF FD00 020F FF05 EF55 093F 333F"            /* ...ÿý...ÿ.ïUÆ?3? */
    $"FFF3 335F 000F FFEA 0019 F900 0140 F0FD"            /* ÿó3_..ÿê..ù..@ðý */
    $"0002 0FF0 00EE 5508 F33F 33FF 3FF5 000F"            /* ...ð.îU.ó?3ÿ?õ.. */
    $"FFEA 001B FA00 0204 04F0 FD00 030F FF00"            /* ÿê..ú....ðý...ÿ. */
    $"05EF 5508 FFF5 533F FF50 0000 FFEA 001F"            /* .ïU.ÿõS?ÿP..ÿê.. */
    $"FE00 0003 FD00 0140 FFFD 0004 0FFF FF00"            /* þ...ý..@ÿý...ÿÿ. */
    $"05F0 5508 5F55 553F F500 000F FFEA 001B"            /* .ðU._UU?õ...ÿê.. */
    $"FE00 0030 FE00 0304 04FF FFFD 00FE FF00"            /* þ..0þ....ÿÿý.þÿ. */
    $"00EC 5504 5000 00FF F4EA 0029 FE00 0033"            /* .ìU.P..ÿôê.)þ..3 */
    $"FD00 0340 F00F F0FE 0005 0FFF FFF0 0000"            /* ý..@ð.ðþ...ÿÿð.. */
    $"F055 0050 FE00 02FF FF40 FA00 0104 40FA"            /* ðU.Pþ..ÿÿ@ú...@ú */
    $"0000 11FB 002C FE00 0033 FD00 0304 FF00"            /* ...û.,þ..3ý...ÿ. */
    $"0FFD 0006 0FFF FFF0 0000 05F4 55FD 0004"            /* .ý...ÿÿð...ôUý.. */
    $"0FFF FFF4 14FA 0002 4444 F0FC 0001 0111"            /* .ÿÿô.ú..DDðü.... */
    $"FB00 2AF9 0003 404F F00F FC00 FDFF FC00"            /* û.*ù..@Oð.ü.ýÿü. */
    $"0005 FD55 0050 FB00 000F FEFF 02F1 4140"            /* ..ýU.Pû...þÿ.ñA@ */
    $"FA00 0104 4FFB 0002 011F F0FC 0026 F900"            /* ú...Oû....ðü.&ù. */
    $"0A04 04F0 0F00 0007 1000 000F FDFF 00F0"            /* ...ð........ýÿ.ð */
    $"F500 FCFF 02F4 1414 F800 00F0 FB00 0201"            /* õ.üÿ.ô..ø..ðû... */
    $"11F0 FC00 23F8 0002 40F0 0FFE 0000 11FD"            /* .ðü.#ø..@ð.þ...ý */
    $"00FB FF00 F0FC 0000 0FFB FF02 F141 41FE"            /* .ûÿ.ðü...ûÿ.ñAAþ */
    $"40F1 0001 11F0 FC00 16F9 0003 0404 F00F"            /* @ñ...ðü..ù....ð. */
    $"FE00 0011 FB00 F1FF FD14 0104 04E9 0017"            /* þ...û.ñÿý....é.. */
    $"F900 0340 40F0 FFFE 0000 F1FA 0000 41F5"            /* ù..@@ðÿþ..ñú..Aõ */
    $"FFFD 41FE 40E8 001B FA00 FE04 01FF F0FE"            /* ÿýAþ@è..ú.þ..ÿðþ */
    $"0000 10F9 0002 0414 1FFB FF00 F4FC 14FD"            /* ...ù.....ûÿ.ôü.ý */
    $"04E8 0013 FA00 0340 4FFF FFF2 00FA 41F8"            /* .è..ú..@Oÿÿò.úAø */
    $"40F6 0000 01F3 0012 FB00 0404 04FF 00F0"            /* @ö...ó..û....ÿ.ð */
    $"F800 0003 F800 F904 E300 0DFB 0003 404F"            /* ø...ø.ù.ã.Âû..@O */
    $"F00F F700 000F D200 12FC 0004 0404 FF00"            /* ð.÷...Ò..ü....ÿ. */
    $"F0DE 0000 0FF6 0000 44F7 0013 FC00 0340"            /* ðÞ...ö..D÷..ü..@ */
    $"FFF0 0FDD 0000 04F7 0002 0444 40F8 0014"            /* ÿð.Ý...÷...D@ø.. */
    $"FD00 0404 0FFF 00F0 FD00 0010 D700 0204"            /* ý....ÿ.ðý...×... */
    $"4440 F800 13FD 0003 40FF 000F D700 0103"            /* D@ø..ý..@ÿ..×... */
    $"30FD 0001 0F44 F700 13FE 0004 04FF F00F"            /* 0ý...D÷..þ...ÿð. */
    $"F0FB 0001 0330 D800 00FF F700 13FE 0003"            /* ðû...0Ø..ÿ÷..þ.. */
    $"FFF0 00F0 FB00 020F 3333 F200 00F1 DD00"            /* ÿð.ðû...33ò..ñÝ. */
    $"0F05 0000 0FF4 04FF FA00 020F FFF0 CD00"            /* .....ô.ÿú...ÿðÍ. */
    $"1204 0000 FF00 4FED 0001 0440 F500 0103"            /* ....ÿ.Oí...@õ... */
    $"30E6 0012 0400 00F0 0FF0 F900 0001 E800"            /* 0æ.....ð.ðù...è. */
    $"0233 33F0 E700 0E04 0000 F0F0 40DF 0002"            /* .33ðç.....ðð@ß.. */
    $"3333 F0E7 0010 0300 00FF 04E5 0000 55FB"            /* 33ðç.....ÿ.å..Uû */
    $"0001 033F E600 1906 0000 FF40 0000 F0F3"            /* ...?æ.....ÿ@..ðó */
    $"0000 40F8 0002 0555 50FC 0001 0FF0 E600"            /* ..@ø...UPü...ðæ. */
    $"1906 0000 FF04 000F FFF4 0001 0444 F800"            /* ....ÿ...ÿô...Dø. */
    $"0205 5550 F300 0001 EE00 1B01 0000 FDFF"            /* ..UPó...î.....ýÿ */
    $"02F0 F040 F700 020F 4444 F800 020F 55F0"            /* .ðð@÷...DDø...Uð */
    $"F300 0001 EE00 1A08 0000 F004 0000 0F04"            /* ó...î.....ð..... */
    $"04F6 0001 F440 F700 00FF F200 0101 F0EF"            /* .ö..ô@÷..ÿò...ðï */
    $"0015 0800 000F 4040 FFF0 4040 F600 010F"            /* ......@@ÿð@@ö... */
    $"F0E7 0000 0FEE 0009 FE00 01FF FFFD 04C6"            /* ðç...î.Æþ..ÿÿý.Æ */
    $"000E FD00 FD40 EE00 0001 F600 0001 E500"            /* ..ý.ý@î...ö...å. */
    $"06FD 00FE 04C4 0002 BD00 06DF 0000 3FE0"            /* .ý.þ.Ä..½..ß..?à */
    $"0006 DF00 000F E000 00FF"                           /* ..ß...à..ÿ */
};

data 'CNTL' (133, purgeable, preload) {
    $"0005 0005 0019 0118 00FF 0100 0032 0085"            /* .........ÿ...2. */
    $"03F0 0000 0000 0845 6666 6563 7473 3A"              /* .ð.....Effects: */
};

data 'CNTL' (134, purgeable, preload) {
    $"0004 0081 0018 0194 0000 0000 0000 0086"            /* ............. */
    $"03F0 0000 0000 00"                                  /* .ð..... */
};

data 'crsr' (128) {
    $"8001 0000 0060 0000 0092 0000 0000 0000"            /* ....`......... */
    $"0000 0000 3F00 3F00 3F00 3F00 4080 8040"            /* ....?.?.?.?.@@ */
    $"8140 8240 9C40 8040 8040 4080 3F00 3F00"            /* @@@@@@?.?. */
    $"3F00 3F00 3F00 3F00 3F00 3F00 7F80 FFC0"            /* ?.?.?.?.?.?..ÿÀ */
    $"FFC0 FFC0 FFC0 FFC0 FFC0 7F80 3F00 3F00"            /* ÿÀÿÀÿÀÿÀÿÀ.?.?. */
    $"3F00 3F00 0008 0004 0000 0000 0000 0000"            /* ?.?............. */
    $"0000 0000 8008 0000 0000 0010 0010 0000"            /* ............... */
    $"0000 0000 0000 0048 0000 0048 0000 0000"            /* .......H...H.... */
    $"0004 0001 0004 0000 0000 0000 0112 0000"            /* ................ */
    $"0000 00FF FFFF 0000 0000 00FF FFFF 0000"            /* ...ÿÿÿ.....ÿÿÿ.. */
    $"0000 00FF FFFF 0000 0000 03FF FFFF 3000"            /* ...ÿÿÿ.....ÿÿÿ0. */
    $"0000 3F11 1111 F300 0000 2111 1111 1F00"            /* ..?...ó...!..... */
    $"0000 F111 111F 1F00 0000 F111 11F1 1F00"            /* ..ñ.......ñ..ñ.. */
    $"0000 F11F FF11 1F00 0000 F111 1111 1F00"            /* ..ñ.ÿ.....ñ..... */
    $"0000 F111 1111 1F00 0000 3F11 1111 F300"            /* ..ñ.......?...ó. */
    $"0000 03FF FFFF 3000 0000 00FF FFFF 0000"            /* ...ÿÿÿ0....ÿÿÿ.. */
    $"0000 00FF FFFF 0000 0000 00FF FFFF 0000"            /* ...ÿÿÿ.....ÿÿÿ.. */
    $"0000 0000 0000 0000 0004 0000 FFFF FFFF"            /* ............ÿÿÿÿ */
    $"FFFF 0001 CCCC CCCC CCCC 0002 1111 1111"            /* ÿÿ..ÌÌÌÌÌÌ...... */
    $"1111 0003 DDDD DDDD DDDD 000F 0000 0000"            /* ....ÝÝÝÝÝÝ...... */
    $"0000"                                               /* .. */
};

data 'dlgx' (132) {
    $"0000 0000 000D"                                     /* .....Â */
};

data 'dctb' (132, purgeable) {
    $"0000 0000 0001 0000 0000 FFFF FFFF FFFF"            /* ..........ÿÿÿÿÿÿ */
};
```

[Next](Document%20Revision%20History.md)[Previous](QTShowEffect.h.md)

