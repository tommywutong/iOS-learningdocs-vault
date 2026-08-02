---
title: CullGroupSample
apple_id: DTS10000133
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CullGroupSample/Listings/Headers_Structs_h.html
archived_at: '2026-07-18T03:05:31.304953Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CullGroupSample](CullGroupSample.md)


[Next](Source-3DMF.c.md)[Previous](Headers-QD3DSupport.h.md)

# Headers/Structs.h

```
//
// structs.h
//


            /*  OBJECT RECORD STRUCTURE */


struct ObjNode
{
    long            NodeNum;        // node # in array (for internal use)
    struct ObjNode  *PrevNode;      // address of previous node in linked list
    struct ObjNode  *NextNode;      // address of next node in linked list
    long        Genre;              // obj genre: 0=sprite, 1=nonsprite
    long        SortSlot;           // sort value
    long        Type;               // obj type
    long        ModeFlags;      
    void        (*MoveCall)(void);  // pointer to object's move routine
    TQ3Point3D  Coord;
    float       RotX,RotY,RotZ;
    float       ScaleX,ScaleY,ScaleZ;

    TQ3Matrix4x4        BaseTransformMatrix;
    TQ3TransformObject  BaseTransformObject;        // illegal ref to BaseTransformMatrix

    TQ3GroupObject  BaseGroup;      // group containing all geometry,etc. for this object (for drawing)


};
typedef struct ObjNode ObjNode;


        /* NEW OBJECT DEFINITION TYPE */

typedef struct
{
    long        genre,type;
    TQ3Point3D  coord;
    unsigned long   flags;
    long        slot;
    void        (*moveCall)(void);
}NewObjectDefinitionType;
```

[Next](Source-3DMF.c.md)[Previous](Headers-QD3DSupport.h.md)

