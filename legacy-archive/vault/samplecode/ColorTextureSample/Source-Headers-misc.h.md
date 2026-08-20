---
title: ColorTextureSample
apple_id: DTS10000131
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ColorTextureSample/Listings/Source_Headers_misc_h.html
archived_at: '2026-07-18T03:04:02.453044Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ColorTextureSample](ColorTextureSample.md)


[Next](Source-Headers-myevents.h.md)[Previous](Source-Headers-main.h.md)

# Source/Headers/misc.h

```
//
// misc.h
//



extern  void ShowSystemErr(long err);
extern void ErrorHandler(short);
extern void DoAlert(Str255);
extern void DoFatalAlert(Str255);
extern void Wait(long);
extern Handle   LoadAFile(Str255, short, long *);
extern unsigned char    *NumToHex(unsigned short);
extern unsigned char    *NumToHex2(unsigned long, short);
extern unsigned char    *NumToDec(unsigned long);
extern  void CleanQuit(void);
extern  float Absolute(float f);
extern  void RegulateSpeed(long speed);
extern  void SetMyRandomSeed(unsigned long seed);
extern  unsigned long MyRandomLong(void);
extern  void FloatToString(float num, Str255 string);
extern  Handle  AllocHandle(long size);
extern  Ptr AllocPtr(long size);
extern  void PrintFPS(void);
extern  void AngleToVector(float angle, TQ3Vector2D *theVector);
extern  unsigned short  RandomRange(unsigned short min, unsigned short max);
extern  Boolean PointsAreCloseEnough(TQ3Point3D *v1, TQ3Point3D *v2);
extern  Boolean VectorsAreCloseEnough(TQ3Vector3D *v1, TQ3Vector3D *v2);
extern  Boolean UVsAreCloseEnough(TQ3Param2D *v1, TQ3Param2D *v2);
extern  void CopyPStr(ConstStr255Param  inSourceStr, StringPtr  outDestStr);
```

[Next](Source-Headers-myevents.h.md)[Previous](Source-Headers-main.h.md)

