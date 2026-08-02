---
title: ColorTextureSample
apple_id: DTS10000131
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ColorTextureSample/Listings/Source_Headers_Structs_h.html
archived_at: '2026-07-18T03:04:02.397611Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ColorTextureSample](ColorTextureSample.md)


[Next](Source-Main.c.md)[Previous](Source-Headers-QD3DSupport.h.md)

# Source/Headers/Structs.h

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
    long        AnimNum;            // sub type (anim type)
    long        ModeFlags;      
    void        (*MoveCall)(void);  // pointer to object's move routine
    TQ3Point3D  Coord;
    TQ3Vector3D Velocity;
    float       RotX,RotY,RotZ;
    float       ScaleX,ScaleY,ScaleZ;
    Boolean             Flag[4];
    long                Special[4];
    float               Floats[4];
    unsigned long       CType;      // collision type bits
    unsigned long       CBits;      // collision attribute bits
    long            Kind;           // kind
    long            Health;         // health
    Byte        ControlMode;        // keyboard,mouse,network, etc.

    TQ3Matrix4x4        BaseTransformMatrix;
    TQ3TransformObject  BaseTransformObject;        // illegal ref to BaseTransformMatrix

    TQ3GroupObject  BaseGroup;      // group containing all geometry,etc. for this object (for drawing)


};
typedef struct ObjNode ObjNode;


        /* NEW OBJECT DEFINITION TYPE */

typedef struct
{
    long    genre,type,animNum;
    TQ3Point3D  coord;
    unsigned long   flags;
    long    slot;
    void    (*moveCall)(void);
}NewObjectDefinitionType;
```

[Next](Source-Main.c.md)[Previous](Source-Headers-QD3DSupport.h.md)

