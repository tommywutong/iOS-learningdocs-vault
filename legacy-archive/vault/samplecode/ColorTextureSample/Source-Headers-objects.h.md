---
title: ColorTextureSample
apple_id: DTS10000131
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ColorTextureSample/Listings/Source_Headers_objects_h.html
archived_at: '2026-07-18T03:04:02.599165Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ColorTextureSample](ColorTextureSample.md)


[Next](Source-Headers-process.h.md)[Previous](Source-Headers-mywindows.h.md)

# Source/Headers/objects.h

```c
//
// Object.h
//

#include "qd3d_support.h"

#define     MAX_OBJECTS 150

enum
{
    SKELETON_GENRE,
    EVENT_GENRE,
    GEOMETRY_GENRE,
    DISPLAY_GROUP_GENRE
};

    /* OBJ_MODE FLAGS */

#define OBJ_MODE_MOVE       1
#define OBJ_MODE_DRAW       (1<<1)
#define OBJ_MODE_ANIM       (1<<2)



//========================================================

extern  void InitObjectManager(void);
extern  ObjNode *MakeNewObject(NewObjectDefinitionType *newObjDef);
extern  void MoveObjects(void);
extern  void DrawObjects(QD3DSetupOutputType *viewInfo);
extern  void DeleteAllObjects(void);
extern  void DeleteObject(ObjNode   *theNode);
extern  void GetObjectInfo(ObjNode *theNode);
extern  void UpdateObject(ObjNode *theNode);
extern  ObjNode *MakeNewDisplayGroupObject(NewObjectDefinitionType *newObjDef);
extern  void AttachGeometryToDisplayGroupObject(ObjNode *theNode, TQ3GeometryObject geometry);
extern  void CreateBaseGroup(ObjNode *theNode);
extern  void UpdateObjectTransforms(ObjNode *theNode);
extern  void SetObjectTransformMatrix(ObjNode *theNode);
extern  void TransformObjectBaseMatrix(ObjNode *theNode, TQ3Matrix4x4 *inMatrix);
extern  void TranslateObjectBaseMatrixByXYZ(ObjNode *theNode);
```

[Next](Source-Headers-process.h.md)[Previous](Source-Headers-mywindows.h.md)

