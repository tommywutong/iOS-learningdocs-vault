---
title: Snapshot
apple_id: DTS10000170
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-10'
source_url: https://developer.apple.com/library/archive/samplecode/Snapshot/Listings/Snapshot_r.html
archived_at: '2026-07-18T03:24:53.795062Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Snapshot](Snapshot.md)


[Next](Document%20Revision%20History.md)[Previous](Snapshot.c.md)

# Snapshot.r

```
data 'BNDL' (128) {
    $"534E 4150 0000 0001 4652 4546 0000 0000"            /* SNAP....FREF.... */
    $"0080 4943 4E23 0000 0000 0080"                      /* .ICN#..... */
};

data 'FREF' (128) {
    $"4150 504C 0000 00"                                  /* APPL... */
};

data 'ics8' (128) {
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 FFFF FFFF 0000 00F7 FF00"            /* ......ÿÿÿÿ...÷ÿ. */
    $"FFFF FF00 00FF FFFF FFFF FF00 FFFF FFFF"            /* ÿÿÿ..ÿÿÿÿÿÿ.ÿÿÿÿ */
    $"FFFF FFFF FFFF FFFB FBFF FFFF FFFF FFFF"            /* ÿÿÿÿÿÿÿûûÿÿÿÿÿÿÿ */
    $"FFFF FAFF FFFF FFFF FFFF FFFF FFFF FFFF"            /* ÿÿúÿÿÿÿÿÿÿÿÿÿÿÿÿ */
    $"FFFF FAFF FFFF FFF8 F8FF FFFF FFFF FFFF"            /* ÿÿúÿÿÿÿøøÿÿÿÿÿÿÿ */
    $"FFFF FAFF FFFF ABAB ABAB FFFF FFFF FFFF"            /* ÿÿúÿÿÿ««««ÿÿÿÿÿÿ */
    $"FFFF FAFF FFF8 ABAB ABAB F8FF FFFF FFFF"            /* ÿÿúÿÿø««««øÿÿÿÿÿ */
    $"FFFF FAFF FFF8 ABAB ABAB F8FF FFFF FFFF"            /* ÿÿúÿÿø««««øÿÿÿÿÿ */
    $"FFFF FFFA FFFF ABAB ABAB FFFF D8FF FFFF"            /* ÿÿÿúÿÿ««««ÿÿØÿÿÿ */
    $"FFFF FFFA FFFF FFF8 F8FF FFFF FFFF FFFF"            /* ÿÿÿúÿÿÿøøÿÿÿÿÿÿÿ */
    $"FFFF FFFA FFFF FFFF FFFF FFFF FFFF FFFF"            /* ÿÿÿúÿÿÿÿÿÿÿÿÿÿÿÿ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
};

data 'icl4' (128) {
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 000C F000"            /* ..............ð. */
    $"0FFF 0000 0000 0FFF FFF0 0000 0FFF 3F00"            /* .ÿ.....ÿÿð...ÿ?. */
    $"F555 F000 000F FFFF FFFF F000 FFFF 3FF0"            /* õUð...ÿÿÿÿð.ÿÿ?ð */
    $"F555 FDFF FFFF FFEE EEFF FFFF FFFF FFF0"            /* õUýÿÿÿÿîîÿÿÿÿÿÿð */
    $"FFFF FCFF FFFF FFEE EEFF FFFF FFFF FFFF"            /* ÿÿüÿÿÿÿîîÿÿÿÿÿÿÿ */
    $"FCFF FCFF FFFF FFFF FFFF FFFF FFFF FFFF"            /* üÿüÿÿÿÿÿÿÿÿÿÿÿÿÿ */
    $"FCFF FCFF FFFF FFFF FFFF FFDD FDFD FDFF"            /* üÿüÿÿÿÿÿÿÿÿÝýýýÿ */
    $"FCFF FCFF FFFF FFCC CCFF FFDF DDDF DDFF"            /* üÿüÿÿÿÿÌÌÿÿßÝßÝÿ */
    $"FCFF FCFF F0FF CC55 55CC FFFF FFFF FFFF"            /* üÿüÿðÿÌUUÌÿÿÿÿÿÿ */
    $"FCFF FCFF FFFC 5555 5555 CFFF FFFF FFFF"            /* üÿüÿÿüUUUUÏÿÿÿÿÿ */
    $"FCFF FCFF FFFC 5555 5555 CFFF FFFF FFCF"            /* üÿüÿÿüUUUUÏÿÿÿÿÏ */
    $"FCFF FFCF FFC5 5555 5055 5CFF FFFF FFCF"            /* üÿÿÏÿÅUUPU\ÿÿÿÿÏ */
    $"FCFF FFCF FFC5 5505 0555 5CFF FFFF FFCF"            /* üÿÿÏÿÅU..U\ÿÿÿÿÏ */
    $"FCFF FFCF FFC5 5550 5055 5CFF FFFF FFCF"            /* üÿÿÏÿÅUPPU\ÿÿÿÿÏ */
    $"FCFF FFFC FFC5 5505 0555 5CFF FFFF FFCF"            /* üÿÿüÿÅU..U\ÿÿÿÿÏ */
    $"FCFF FFFC FFFC 5555 5555 CFF3 3FFF FFCF"            /* üÿÿüÿüUUUUÏó?ÿÿÏ */
    $"FCFF FFFC FFFC 5555 5555 CFF3 3FFF FFCF"            /* üÿÿüÿüUUUUÏó?ÿÿÏ */
    $"FCFF FFFC FFFF CC55 55CC FFFF FFFF FFCF"            /* üÿÿüÿÿÌUUÌÿÿÿÿÿÏ */
    $"FCFF FFFC FFFF FFCC CCFF FFFF FFFF FFCF"            /* üÿÿüÿÿÿÌÌÿÿÿÿÿÿÏ */
    $"0FFF FFFC FFFF FFFF FFFF FFFF FFFF FFCF"            /* .ÿÿüÿÿÿÿÿÿÿÿÿÿÿÏ */
    $"0FFF FFCC FFFF FFFF FFFF FFFF FFFF FFF0"            /* .ÿÿÌÿÿÿÿÿÿÿÿÿÿÿð */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
};

data 'ics4' (128) {
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 00FF FF00 0CF0"            /* ...........ÿÿ..ð */
    $"FFF0 0FFF FFF0 FFFF FFFF FFFE EFFF FFFF"            /* ÿð.ÿÿðÿÿÿÿÿþïÿÿÿ */
    $"FFDF FFFF FFFF FFFF FFDF FFFC CFFF FFFF"            /* ÿßÿÿÿÿÿÿÿßÿüÏÿÿÿ */
    $"FFDF FF55 55FF FFFF FFDF FC55 55CF FFFF"            /* ÿßÿUUÿÿÿÿßüUUÏÿÿ */
    $"FFFD FC55 55CF FFFF FFFD FF55 55FF 3FFF"            /* ÿýüUUÏÿÿÿýÿUUÿ?ÿ */
    $"FFFD FFFC CFFF FFFF FFFD FFFF FFFF FFFF"            /* ÿýÿüÏÿÿÿÿýÿÿÿÿÿÿ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
};

data 'ics#' (128) {
    $"0000 0000 0000 03C6 67EF FE7F DFFF DE35"            /* .......Ægïþ.ßÿÞ5 */
    $"DDDF DDDF EDDF EE3F EFF7 EFFF 0000 0000"            /* ÝßÝßíßî?ï÷ïÿ.... */
    $"0000 0000 0000 03C6 E7EF FFFF FFFF FFFF"            /* .......Æçïÿÿÿÿÿÿ */
    $"FFFF FFFF FFFF FFFF FFFF FFFF 0000 0000"            /* ÿÿÿÿÿÿÿÿÿÿÿÿ.... */
};

data 'icl8' (128) {
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 00F7 FF00 0000"            /* ...........÷ÿ... */
    $"00FF FFFF 0000 0000 0000 0000 00FF FFFF"            /* .ÿÿÿ.........ÿÿÿ */
    $"FFFF FF00 0000 0000 00FF FFFF D8FF 0000"            /* ÿÿÿ......ÿÿÿØÿ.. */
    $"FFB0 B0B0 FF00 0000 0000 00FF FFFF FFFF"            /* ÿ°°°ÿ......ÿÿÿÿÿ */
    $"FFFF FFFF FF00 0000 FFFF FFFF D8FF FF00"            /* ÿÿÿÿÿ...ÿÿÿÿØÿÿ. */
    $"FFB0 B0B0 FFFA FFFF FFFF FFFF FFFF FBFB"            /* ÿ°°°ÿúÿÿÿÿÿÿÿÿûû */
    $"FBFB FFFF FFFF FFFF FFFF FFFF FFFF FF00"            /* ûûÿÿÿÿÿÿÿÿÿÿÿÿÿ. */
    $"FFFF FFFF FFF7 FFFF FFFF FFFF FFFF FBFB"            /* ÿÿÿÿÿ÷ÿÿÿÿÿÿÿÿûû */
    $"FBFB FFFF FFFF FFFF FFFF FFFF FFFF FFFF"            /* ûûÿÿÿÿÿÿÿÿÿÿÿÿÿÿ */
    $"FFF8 FFFF FFF7 FFFF FFFF FFFF FFFF FFFF"            /* ÿøÿÿÿ÷ÿÿÿÿÿÿÿÿÿÿ */
    $"FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF"            /* ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ */
    $"FFF8 FFFF FFF7 FFFF FFFF FFFF FFFF FFFF"            /* ÿøÿÿÿ÷ÿÿÿÿÿÿÿÿÿÿ */
    $"FFFF FFFF FFFF 7F7F FF7F FF7F FF7F FFFF"            /* ÿÿÿÿÿÿ..ÿ.ÿ.ÿ.ÿÿ */
    $"FFF8 FFFF FFF7 FFFF FFFF FFFF FFFF F8F8"            /* ÿøÿÿÿ÷ÿÿÿÿÿÿÿÿøø */
    $"F8F8 FFFF FFFF 7FFF 7F7F 7FFF 7F7F FFFF"            /* øøÿÿÿÿ.ÿ...ÿ..ÿÿ */
    $"FFF8 FFFF FFF7 FFFF FF00 FFFF F8F8 ABAB"            /* ÿøÿÿÿ÷ÿÿÿ.ÿÿøø«« */
    $"ABAB F8F8 FFFF FFFF FFFF FFFF FFFF FFFF"            /* ««øøÿÿÿÿÿÿÿÿÿÿÿÿ */
    $"FFF8 FFFF FFF7 FFFF FFFF FFF8 ABAB ABAB"            /* ÿøÿÿÿ÷ÿÿÿÿÿø«««« */
    $"ABAB ABAB F8FF FFFF FFFF FFFF FFFF FFFF"            /* ««««øÿÿÿÿÿÿÿÿÿÿÿ */
    $"FFF8 FFFF FFF7 FFFF FFFF FFF8 ABAB ABAB"            /* ÿøÿÿÿ÷ÿÿÿÿÿø«««« */
    $"ABAB ABAB F8FF FFFF FFFF FFFF FFFF 2BFF"            /* ««««øÿÿÿÿÿÿÿÿÿ+ÿ */
    $"FFF8 FFFF FFFF F7FF FFFF F8AB ABAB ABAB"            /* ÿøÿÿÿÿ÷ÿÿÿø««««« */
    $"ABF5 ABAB ABF8 FFFF FFFF FFFF FFFF 2BFF"            /* «õ«««øÿÿÿÿÿÿÿÿ+ÿ */
    $"FFF8 FFFF FFFF F7FF FFFF F8AB ABAB F5AB"            /* ÿøÿÿÿÿ÷ÿÿÿø«««õ« */
    $"F5AB ABAB ABF8 FFFF FFFF FFFF FFFF 2BFF"            /* õ««««øÿÿÿÿÿÿÿÿ+ÿ */
    $"FFF8 FFFF FFFF F7FF FFFF F8AB ABAB ABF5"            /* ÿøÿÿÿÿ÷ÿÿÿø««««õ */
    $"ABF5 ABAB ABF8 FFFF FFFF FFFF FFFF 2BFF"            /* «õ«««øÿÿÿÿÿÿÿÿ+ÿ */
    $"FFF8 FFFF FFFF FFF7 FFFF F8AB ABAB F5AB"            /* ÿøÿÿÿÿÿ÷ÿÿø«««õ« */
    $"F5AB ABAB ABF8 FFFF FFFF FFFF FFFF 2BFF"            /* õ««««øÿÿÿÿÿÿÿÿ+ÿ */
    $"FFF8 FFFF FFFF FFF7 FFFF FFF8 ABAB ABAB"            /* ÿøÿÿÿÿÿ÷ÿÿÿø«««« */
    $"ABAB ABAB F8FF FFD8 D8FF FFFF FFFF 2BFF"            /* ««««øÿÿØØÿÿÿÿÿ+ÿ */
    $"FFF8 FFFF FFFF FFF7 FFFF FFF8 ABAB ABAB"            /* ÿøÿÿÿÿÿ÷ÿÿÿø«««« */
    $"ABAB ABAB F8FF FFD8 D8FF FFFF FFFF 2BFF"            /* ««««øÿÿØØÿÿÿÿÿ+ÿ */
    $"FFF8 FFFF FFFF FFF7 FFFF FFFF F8F8 ABAB"            /* ÿøÿÿÿÿÿ÷ÿÿÿÿøø«« */
    $"ABAB F8F8 FFFF FFFF FFFF FFFF FFFF 2BFF"            /* ««øøÿÿÿÿÿÿÿÿÿÿ+ÿ */
    $"FFF8 FFFF FFFF FFF7 FFFF FFFF FFFF F8F8"            /* ÿøÿÿÿÿÿ÷ÿÿÿÿÿÿøø */
    $"F8F8 FFFF FFFF FFFF FFFF FFFF FFFF 2BFF"            /* øøÿÿÿÿÿÿÿÿÿÿÿÿ+ÿ */
    $"00FF FFFF FFFF FFF7 FFFF FFFF FFFF FFFF"            /* .ÿÿÿÿÿÿ÷ÿÿÿÿÿÿÿÿ */
    $"FFFF FFFF FFFF FFFF FFFF FFFF FFFF 2BFF"            /* ÿÿÿÿÿÿÿÿÿÿÿÿÿÿ+ÿ */
    $"00FF FFFF FFFF F7F7 FFFF FFFF FFFF FFFF"            /* .ÿÿÿÿÿ÷÷ÿÿÿÿÿÿÿÿ */
    $"FFFF FFFF FFFF FFFF FFFF FFFF FFFF FF00"            /* ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ. */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
};

data 'ICN#' (128) {
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0008 7007 E074"            /* ............p.àt */
    $"A81F F8F6 FFFC 3FFE FBFC 3FFF FBFF FFFF"            /* ¨.øöÿü?þûü?ÿûÿÿÿ */
    $"FBFF FCAB FBFC 3D13 FBB3 CFFF FBEF F7FF"            /* ûÿü«ûü=.û³Ïÿûï÷ÿ */
    $"FBEF F7FD FBDF BBFD FDDD 7BFD FDDE BBFD"            /* ûï÷ýûß»ýýÝ{ýýÞ»ý */
    $"FEDD 7BFD FEEF F67D FEEF F67D FEF3 CFFD"            /* þÝ{ýþïö}þïö}þóÏý */
    $"FEFC 3FFD 7EFF FFFD 7CFF FFFE 0000 0000"            /* þü?ý~ÿÿý|ÿÿþ.... */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
    $"0000 0000 0000 0000 0000 0008 7007 E07C"            /* ............p.à| */
    $"F81F F8FE FFFF FFFE FFFF FFFF FFFF FFFF"            /* ø.øþÿÿÿþÿÿÿÿÿÿÿÿ */
    $"FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF"            /* ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ */
    $"FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF"            /* ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ */
    $"FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF"            /* ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ */
    $"FFFF FFFF 7FFF FFFF 7CFF FFFE 0000 0000"            /* ÿÿÿÿ.ÿÿÿ|ÿÿþ.... */
    $"0000 0000 0000 0000 0000 0000 0000 0000"            /* ................ */
};

data 'SNAP' (0, "Owner resource") {
    $"00"                                                 /* . */
};

data 'MBAR' (128) {
    $"0001 0080"                                          /* ... */
};

data 'MBAR' (129) {
    $"0001 0081"                                          /* ... */
};

data 'MENU' (128) {
    $"0080 0000 0000 0000 0000 FFFF FFFD 0446"            /* .........ÿÿÿý.F */
    $"696C 6503 4E65 7700 4E00 0007 5265 6672"            /* ile.New.N...Refr */
    $"6573 6800 5200 0005 436C 6F73 6500 5700"            /* esh.R...Close.W. */
    $"0004 5361 7665 0053 0000 0451 7569 7400"            /* ..Save.S...Quit. */
    $"5100 0000"                                          /* Q... */
};

data 'MENU' (129) {
    $"0081 0000 0000 0000 0000 FFFF FFFD 0446"            /* .........ÿÿÿý.F */
    $"696C 6503 4E65 7700 4E00 0007 5265 6672"            /* ile.New.N...Refr */
    $"6573 6800 5200 0005 436C 6F73 6500 5700"            /* esh.R...Close.W. */
    $"0004 5361 7665 0053 0000 00"                        /* ..Save.S... */
};
```

[Next](Document%20Revision%20History.md)[Previous](Snapshot.c.md)

