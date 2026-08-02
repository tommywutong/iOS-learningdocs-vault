---
title: STD File Saver
apple_id: DTS10000307
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/STD_File_Saver/Listings/Source_SettingsUtils_h.html
archived_at: '2026-07-18T03:22:48.975655Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [STD File Saver](STD%20File%20Saver.md)


[Next](Source-StdFileSaver.a.md)[Previous](Source-SettingsUtils.c.md)

# Source/SettingsUtils.h

```
typedef struct {
    short   selectedItemNumber;
    Boolean isRadioOptionOn;
} settings, **settingsHandle;

/* settings utils */
void SaveSettings(settingsHandle theSettings);
settingsHandle RetrieveSettings(void);
void SaveItemNumber(short item);
short GetSavedItemNumber(void);
void SaveRadioOption(Boolean state);
Boolean GetSavedRadioOption(void);
```

[Next](Source-StdFileSaver.a.md)[Previous](Source-SettingsUtils.c.md)

