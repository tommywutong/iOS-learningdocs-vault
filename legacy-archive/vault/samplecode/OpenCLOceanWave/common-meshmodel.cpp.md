---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_mesh_model_cpp.html
archived_at: '2026-07-18T03:17:47.375975Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-meshmodel.h.md)[Previous](common-memorybuffer.h.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/mesh_model.cpp

```c
// Version:    <1.0>
//
// Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple Inc. ("Apple")
//             in consideration of your agreement to the following terms, and your use,
//             installation, modification or redistribution of this Apple software
//             constitutes acceptance of these terms.  If you do not agree with these
//             terms, please do not use, install, modify or redistribute this Apple
//             software.
//
//             In consideration of your agreement to abide by the following terms, and
//             subject to these terms, Apple grants you a personal, non - exclusive
//             license, under Apple's copyrights in this original Apple software ( the
//             "Apple Software" ), to use, reproduce, modify and redistribute the Apple
//             Software, with or without modifications, in source and / or binary forms;
//             provided that if you redistribute the Apple Software in its entirety and
//             without modifications, you must retain this notice and the following text
//             and disclaimers in all such redistributions of the Apple Software. Neither
//             the name, trademarks, service marks or logos of Apple Inc. may be used to
//             endorse or promote products derived from the Apple Software without specific
//             prior written permission from Apple.  Except as expressly stated in this
//             notice, no other rights or licenses, express or implied, are granted by
//             Apple herein, including but not limited to any patent rights that may be
//             infringed by your derivative works or by other works in which the Apple
//             Software may be incorporated.
//
//             The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO
//             WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED
//             WARRANTIES OF NON - INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A
//             PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND OPERATION
//             ALONE OR IN COMBINATION WITH YOUR PRODUCTS.
//
//             IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR
//             CONSEQUENTIAL DAMAGES ( INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
//             SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
//             INTERRUPTION ) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION, MODIFICATION
//             AND / OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED AND WHETHER
//             UNDER THEORY OF CONTRACT, TORT ( INCLUDING NEGLIGENCE ), STRICT LIABILITY OR
//             OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
// Copyright ( C ) 2008 Apple Inc. All Rights Reserved.
//
////////////////////////////////////////////////////////////////////////////////////////////////////

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <fstream>
#include <vector>
#include <OpenGL/gl.h>
#include <OpenGL/glu.h>

#include "compute_types.h"
#include "compute_math.h"
#include "mesh_model.h"
#include "data_loader.h"

/////////////////////////////////////////////////////////////////////////////

#define MM_3DS_PRIMARY_ID                                            0x4D4D
#define MM_3DS_VERSION_ID                                            0x0002             
#define MM_3DS_KEYFRAME_ID                                           0xB000             
#define MM_3DS_MATERIAL_ID                                           0xAFFF             
#define MM_3DS_OBJECT_ID                                             0x4000             
#define MM_3DS_MATERIAL_NAME_ID                                      0xA000             
#define MM_3DS_MATERIAL_DIFFUSE_ID                                   0xA020             
#define MM_3DS_MATERIAL_TEXTURE_ID                                   0xA200             
#define MM_3DS_MATERIAL_TEXTURE_FILENAME_ID                          0xA300             
#define MM_3DS_OBJECT_INFO_ID                                        0x3D3D             
#define MM_3DS_OBJECT_MESH_ID                                        0x4100             
#define MM_3DS_OBJECT_VERTICES_ID                                    0x4110         
#define MM_3DS_OBJECT_FACES_ID                                       0x4120         
#define MM_3DS_OBJECT_MATERIAL_ID                                    0x4130         
#define MM_3DS_OBJECT_UV_ID                                          0x4140         

/////////////////////////////////////////////////////////////////////////////

#define MAX_TEXTURES 1024
static unsigned int gs_auiTextureLibrary[MAX_TEXTURES];

/////////////////////////////////////////////////////////////////////////////

struct FaceData
{
    uint m_uiVertexIndex[3];
    uint m_uiCoordIndex[3];
};

/////////////////////////////////////////////////////////////////////////////

struct MaterialData
{
    char  m_acName[255];            
    char  m_acFileName[255];            
    uchar m_aucColor[3];                
    int   m_iTextureId;             
    float m_fTileU;             
    float m_fTileV;             
    float m_fOffsetU;               
    float m_fOffsetV;               
} ;

/////////////////////////////////////////////////////////////////////////////

struct ObjectData
{
    char m_acName[255];         
    uint m_uiMaterialId;            
    bool m_bHasTexture;         
    uint m_uiVertexCount;           
    uint m_uiFaceCount;         
    uint m_uiTexCoordCount;         
    float3 *m_akVertices;           
    float3 *m_akNormals;        
    float2 *m_akTexCoords;      
    FaceData *m_akFaces;                
};

/////////////////////////////////////////////////////////////////////////////

struct ModelData
{
    uint m_uiObjectCount;                   
    uint m_uiMaterialCount;                 
    std::vector<MaterialData> m_akMaterials;    
    std::vector<ObjectData> m_akObjects;            
};

/////////////////////////////////////////////////////////////////////////////

struct VertexIndices
{

    unsigned short a;
    unsigned short b;
    unsigned short c;
    bool bIsVisible;        
};

/////////////////////////////////////////////////////////////////////////////

struct DataChunk
{
    unsigned short int m_usId;                  
    unsigned int m_uiLength;                    
    unsigned int m_uiBytesRead;                 
};

/////////////////////////////////////////////////////////////////////////////

bool CreateTexture(
    unsigned int auiTextureLibrary[], 
    char* acFileName, 
    int iTextureId)
{
    if (!acFileName)
        return false;

    int iWidth = 0;
    int iHeight = 0;

    printf("MeshModel: Loading texture map '%s'...\n", acFileName);

    unsigned char *acRgb = LoadImageFromFile(acFileName, &iWidth, &iHeight);
    if ( acRgb == NULL )
    {
        printf("Error: Failed to load texture map : %s\n", acFileName);
        return false;
    }

    glGenTextures(1, &auiTextureLibrary[iTextureId]);
    printf("MeshModel: Creating texture [%d] id[%d] width[%d] height[%d]\n", iTextureId, auiTextureLibrary[iTextureId], iWidth, iHeight);
    glBindTexture(GL_TEXTURE_2D, auiTextureLibrary[iTextureId]);
    glTexImage2D( GL_TEXTURE_2D, 0, GL_RGB8, iWidth, iHeight, 0, GL_RGB,  GL_UNSIGNED_BYTE, acRgb );
    gluBuild2DMipmaps( GL_TEXTURE_2D, GL_RGB8, iWidth, iHeight, GL_RGB, GL_UNSIGNED_BYTE, acRgb  );
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST);//GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR_MIPMAP_LINEAR);//GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT); // CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT); // CLAMP_TO_EDGE);
    glBindTexture(GL_TEXTURE_2D, 0);

    free(acRgb);
    return true;
}

/////////////////////////////////////////////////////////////////////////////

class ModelImporter
{
public:
    ModelImporter();                                

    bool load3DS(ModelData *pkModel, const char *acFileName, float afScale[3]);

private:
    int readString(char *);

    void readChunk(DataChunk *);
    void processNextDataChunk(ModelData *pkModel, DataChunk *);
    void processNextObjecDataChunk(ModelData *pkModel, ObjectData *m_akObjects, DataChunk *);
    void processNextMaterialChunk(ModelData *pkModel, DataChunk *);
    void readColorChunk(MaterialData *pkMaterial, DataChunk *pkChunk);
    void readVertices(ObjectData *m_akObjects, DataChunk *);
    void readVertexIndices(ObjectData *m_akObjects, DataChunk *);
    void readTexCoords(ObjectData *m_akObjects, DataChunk *);
    void readObjectMaterial(ModelData *pkModel, ObjectData *m_akObjects, DataChunk *pkPrevChunk);
    void computeNormals(ModelData *pkModel);
    void destroy();

    FILE *m_pkFileHandle;
    DataChunk *m_pkCurrentChunk;
    DataChunk *m_pkTempkChunk;
    float m_afScale[3];
};

ModelImporter::ModelImporter()
{
    m_pkCurrentChunk = new DataChunk;               
    m_pkTempkChunk = new DataChunk;             
}


bool 
ModelImporter::load3DS(
    ModelData *pkModel, 
    const char *acFileName, 
    float afScale[3])
{
    m_afScale[0] = afScale[0];
    m_afScale[1] = afScale[1];
    m_afScale[2] = afScale[2];

    m_pkFileHandle = fopen(acFileName, "rb");
    if (!m_pkFileHandle)
    {
        fprintf(stderr, "MeshModel: Error: Unable to locate file '%s'\n", acFileName);
        return false;
    }

    readChunk(m_pkCurrentChunk);
    if (m_pkCurrentChunk->m_usId != MM_3DS_PRIMARY_ID)
    {
        fprintf(stderr, "MeshModel: Error: Unable to locate primary chunk in '%s'\n", acFileName);
        return false;
    }
    processNextDataChunk(pkModel, m_pkCurrentChunk);
    computeNormals(pkModel);
    destroy();

    return true;
}

void
ModelImporter::destroy()
{

    fclose(m_pkFileHandle);                     
    delete m_pkCurrentChunk;                        
    delete m_pkTempkChunk;                          
}


void 
ModelImporter::processNextDataChunk(
    ModelData *pkModel, 
    DataChunk *pkPrevChunk)
{
    ObjectData kObject;                 
    MaterialData kMaterial;             
    unsigned int uiVersion = 0;                 
    int aiBuffer[50000] = {0};                  

    m_pkCurrentChunk = new DataChunk;               

    while (pkPrevChunk->m_uiBytesRead < pkPrevChunk->m_uiLength)
    {
        readChunk(m_pkCurrentChunk);
        switch (m_pkCurrentChunk->m_usId)
        {

        case MM_3DS_VERSION_ID:                         

            m_pkCurrentChunk->m_uiBytesRead += fread(&uiVersion, 1, m_pkCurrentChunk->m_uiLength - m_pkCurrentChunk->m_uiBytesRead, m_pkFileHandle);
            if (uiVersion > 0x03)
                fprintf(stderr, "MeshModel: Invalid 3ds file version.  Model may load incorrectly!\n");
            break;

        case MM_3DS_OBJECT_INFO_ID:                 

            readChunk(m_pkTempkChunk);
            m_pkTempkChunk->m_uiBytesRead += fread(&uiVersion, 1, m_pkTempkChunk->m_uiLength - m_pkTempkChunk->m_uiBytesRead, m_pkFileHandle);
            m_pkCurrentChunk->m_uiBytesRead += m_pkTempkChunk->m_uiBytesRead;
            processNextDataChunk(pkModel, m_pkCurrentChunk);
            break;

        case MM_3DS_MATERIAL_ID:                            

            pkModel->m_uiMaterialCount++;
            memset(&(kMaterial), 0, sizeof(MaterialData));
            pkModel->m_akMaterials.push_back(kMaterial);
            processNextMaterialChunk(pkModel, m_pkCurrentChunk);
            break;

        case MM_3DS_OBJECT_ID:                          

            pkModel->m_uiObjectCount++;
            memset(&(kObject), 0, sizeof(ObjectData));
            pkModel->m_akObjects.push_back(kObject);
            m_pkCurrentChunk->m_uiBytesRead += readString(&(pkModel->m_akObjects[pkModel->m_uiObjectCount - 1].m_acName[0]));
            processNextObjecDataChunk(pkModel, &(pkModel->m_akObjects[pkModel->m_uiObjectCount - 1]), m_pkCurrentChunk);
            break;

        case MM_3DS_KEYFRAME_ID:
        default:

            m_pkCurrentChunk->m_uiBytesRead += fread(aiBuffer, 1, m_pkCurrentChunk->m_uiLength - m_pkCurrentChunk->m_uiBytesRead, m_pkFileHandle);
            break;
        }
        pkPrevChunk->m_uiBytesRead += m_pkCurrentChunk->m_uiBytesRead;
    }

    delete m_pkCurrentChunk;
    m_pkCurrentChunk = pkPrevChunk;
}


void 
ModelImporter::processNextObjecDataChunk(
    ModelData *pkModel, 
    ObjectData *akObjects, 
    DataChunk *pkPrevChunk)
{
    int aiBuffer[50000] = {0};                  

    m_pkCurrentChunk = new DataChunk;

    while (pkPrevChunk->m_uiBytesRead < pkPrevChunk->m_uiLength)
    {
        readChunk(m_pkCurrentChunk);
        switch (m_pkCurrentChunk->m_usId)
        {
        case MM_3DS_OBJECT_MESH_ID:                 
            processNextObjecDataChunk(pkModel, akObjects, m_pkCurrentChunk);
            break;

        case MM_3DS_OBJECT_VERTICES_ID:             
            readVertices(akObjects, m_pkCurrentChunk);
            break;

        case MM_3DS_OBJECT_FACES_ID:                    
            readVertexIndices(akObjects, m_pkCurrentChunk);
            break;

        case MM_3DS_OBJECT_MATERIAL_ID:             
            readObjectMaterial(pkModel, akObjects, m_pkCurrentChunk);
            break;

        case MM_3DS_OBJECT_UV_ID:                       
            readTexCoords(akObjects, m_pkCurrentChunk);
            break;

        default:
            m_pkCurrentChunk->m_uiBytesRead += fread(aiBuffer, 1, m_pkCurrentChunk->m_uiLength - m_pkCurrentChunk->m_uiBytesRead, m_pkFileHandle);
            break;
        }

        pkPrevChunk->m_uiBytesRead += m_pkCurrentChunk->m_uiBytesRead;
    }

    delete m_pkCurrentChunk;
    m_pkCurrentChunk = pkPrevChunk;
}


void 
ModelImporter::processNextMaterialChunk(
    ModelData *pkModel, 
    DataChunk *pkPrevChunk)
{
    int aiBuffer[50000] = {0};                  
    m_pkCurrentChunk = new DataChunk;

    while (pkPrevChunk->m_uiBytesRead < pkPrevChunk->m_uiLength)
    {
        readChunk(m_pkCurrentChunk);
        switch (m_pkCurrentChunk->m_usId)
        {
        case MM_3DS_MATERIAL_NAME_ID:                           
            m_pkCurrentChunk->m_uiBytesRead += fread(pkModel->m_akMaterials[pkModel->m_uiMaterialCount - 1].m_acName, 1, m_pkCurrentChunk->m_uiLength - m_pkCurrentChunk->m_uiBytesRead, m_pkFileHandle);
            break;

        case MM_3DS_MATERIAL_DIFFUSE_ID:                        
            readColorChunk(&(pkModel->m_akMaterials[pkModel->m_uiMaterialCount - 1]), m_pkCurrentChunk);
            break;

        case MM_3DS_MATERIAL_TEXTURE_ID:                            
            processNextMaterialChunk(pkModel, m_pkCurrentChunk);
            break;

        case MM_3DS_MATERIAL_TEXTURE_FILENAME_ID:                       
            m_pkCurrentChunk->m_uiBytesRead += fread(pkModel->m_akMaterials[pkModel->m_uiMaterialCount - 1].m_acFileName, 1, m_pkCurrentChunk->m_uiLength - m_pkCurrentChunk->m_uiBytesRead, m_pkFileHandle);
            break;

        default:
            m_pkCurrentChunk->m_uiBytesRead += fread(aiBuffer, 1, m_pkCurrentChunk->m_uiLength - m_pkCurrentChunk->m_uiBytesRead, m_pkFileHandle);
            break;
        }

        pkPrevChunk->m_uiBytesRead += m_pkCurrentChunk->m_uiBytesRead;
    }

    delete m_pkCurrentChunk;
    m_pkCurrentChunk = pkPrevChunk;
}

void 
ModelImporter::readChunk(
    DataChunk *pkChunk)
{
    pkChunk->m_uiBytesRead = fread(&pkChunk->m_usId, 1, 2, m_pkFileHandle);
    pkChunk->m_uiBytesRead += fread(&pkChunk->m_uiLength, 1, 4, m_pkFileHandle);
}


int 
ModelImporter::readString(
    char *pBuffer)
{
    int index = 0;
    fread(pBuffer, 1, 1, m_pkFileHandle);
    while (*(pBuffer + index++) != 0)
    {
        fread(pBuffer + index, 1, 1, m_pkFileHandle);
    }
    return strlen(pBuffer) + 1;
}


void 
ModelImporter::readColorChunk(
    MaterialData *pkMaterial, 
    DataChunk *pkChunk)
{
    readChunk(m_pkTempkChunk);
    m_pkTempkChunk->m_uiBytesRead += fread(pkMaterial->m_aucColor, 1, m_pkTempkChunk->m_uiLength - m_pkTempkChunk->m_uiBytesRead, m_pkFileHandle);
    pkChunk->m_uiBytesRead += m_pkTempkChunk->m_uiBytesRead;
}


void 
ModelImporter::readVertexIndices(
    ObjectData *akObjects, 
    DataChunk *pkPrevChunk)
{
    unsigned short index = 0;                   

    pkPrevChunk->m_uiBytesRead += fread(&akObjects->m_uiFaceCount, 1, 2, m_pkFileHandle);
    akObjects->m_akFaces = new FaceData [akObjects->m_uiFaceCount];
    memset(akObjects->m_akFaces, 0, sizeof(FaceData) * akObjects->m_uiFaceCount);
    for (uint i = 0; i < akObjects->m_uiFaceCount; i++)
    {
        for (uint j = 0; j < 4; j++)
        {
            pkPrevChunk->m_uiBytesRead += fread(&index, 1, sizeof(index), m_pkFileHandle);

            if (j < 3)
            {
                akObjects->m_akFaces[i].m_uiVertexIndex[j] = index;
            }
        }
    }
}


void 
ModelImporter::readTexCoords(
    ObjectData *akObjects, 
    DataChunk *pkPrevChunk)
{
    pkPrevChunk->m_uiBytesRead += fread(&akObjects->m_uiTexCoordCount, 1, 2, m_pkFileHandle);
    akObjects->m_akTexCoords = new float2 [akObjects->m_uiTexCoordCount];
    pkPrevChunk->m_uiBytesRead += fread(akObjects->m_akTexCoords, 1, pkPrevChunk->m_uiLength - pkPrevChunk->m_uiBytesRead, m_pkFileHandle);
}


void 
ModelImporter::readVertices(
    ObjectData *akObjects, 
    DataChunk *pkPrevChunk)
{
    pkPrevChunk->m_uiBytesRead += fread(&(akObjects->m_uiVertexCount), 1, 2, m_pkFileHandle);
    akObjects->m_akVertices = new float3 [akObjects->m_uiVertexCount];
    memset(akObjects->m_akVertices, 0, sizeof(float3) * akObjects->m_uiVertexCount);

    pkPrevChunk->m_uiBytesRead += fread(akObjects->m_akVertices, 1, pkPrevChunk->m_uiLength - pkPrevChunk->m_uiBytesRead, m_pkFileHandle);
}


void 
ModelImporter::readObjectMaterial(
    ModelData *pkModel, 
    ObjectData *akObjects, 
    DataChunk *pkPrevChunk)
{
    char strMaterial[255] = {0};            
    int aiBuffer[50000] = {0};              
    pkPrevChunk->m_uiBytesRead += readString(strMaterial);
    for (uint i = 0; i < pkModel->m_uiMaterialCount; i++)
    {
        if (strcmp(strMaterial, pkModel->m_akMaterials[i].m_acName) == 0)
        {
            akObjects->m_uiMaterialId = i;
            if (strlen(pkModel->m_akMaterials[i].m_acFileName) > 0)
            {
                akObjects->m_bHasTexture = true;
            }
            break;
        }
        else
        {
            akObjects->m_uiMaterialId = -1;
        }
    }
    pkPrevChunk->m_uiBytesRead += fread(aiBuffer, 1, pkPrevChunk->m_uiLength - pkPrevChunk->m_uiBytesRead, m_pkFileHandle);
}

void 
ModelImporter::computeNormals(
    ModelData *pkModel)
{
    float3 kV1, kV2, kNormal, kTriangle[3];

    if (pkModel->m_uiObjectCount <= 0)
        return;

    for (uint index = 0; index < pkModel->m_uiObjectCount; index++)
    {
        uint i = 0;
        ObjectData *m_akObjects = &(pkModel->m_akObjects[index]);

        float3 *akNormals = new float3 [m_akObjects->m_uiFaceCount];
        float3 *akTemp = new float3 [m_akObjects->m_uiFaceCount];
        m_akObjects->m_akNormals = new float3 [m_akObjects->m_uiVertexCount];

        for (i = 0; i < m_akObjects->m_uiFaceCount; i++)
        {
            kTriangle[0] = m_akObjects->m_akVertices[m_akObjects->m_akFaces[i].m_uiVertexIndex[0]];
            kTriangle[1] = m_akObjects->m_akVertices[m_akObjects->m_akFaces[i].m_uiVertexIndex[1]];
            kTriangle[2] = m_akObjects->m_akVertices[m_akObjects->m_akFaces[i].m_uiVertexIndex[2]];

            kV1 = (kTriangle[0] - kTriangle[2]);        
            kV2 = (kTriangle[2] - kTriangle[1]);        

            kNormal  = cross(kV1, kV2);     
            akTemp[i] = kNormal;                    
            akNormals[i] = normalize(kNormal);      
        }


        float3 kZero = make_float3(0.0f, 0.0f, 0.0f);
        float3 kSum = kZero;
        int iShared = 0;

        for (i = 0; i < m_akObjects->m_uiVertexCount; i++)          
        {
            for (uint j = 0; j < m_akObjects->m_uiFaceCount; j++)   
            {                                               
                if (m_akObjects->m_akFaces[j].m_uiVertexIndex[0] == i ||
                    m_akObjects->m_akFaces[j].m_uiVertexIndex[1] == i ||
                    m_akObjects->m_akFaces[j].m_uiVertexIndex[2] == i)
                {
                    kSum += akTemp[j];
                    iShared++;                              
                }
            }

            m_akObjects->m_akNormals[i] = (kSum / (float)(-iShared));
            m_akObjects->m_akNormals[i] = normalize(m_akObjects->m_akNormals[i]);

            kSum = kZero;                                   
            iShared = 0;                                        
        }

        delete [] akTemp;
        delete [] akNormals;
    }
}

/////////////////////////////////////////////////////////////////////////////

MeshModel::MeshModel() : 
    m_iPrimitiveType(GL_TRIANGLES)
{
    m_pkModelImporter = new ModelImporter;
    m_pkModelData = new ModelData;
    memset(m_pkModelData, 0, sizeof(ModelData));
}

MeshModel::~MeshModel()
{
    for (uint i = 0; i < m_pkModelData->m_uiObjectCount; i++)
    {
        delete [] m_pkModelData->m_akObjects[i].m_akFaces;
        delete [] m_pkModelData->m_akObjects[i].m_akNormals;
        delete [] m_pkModelData->m_akObjects[i].m_akVertices;
        delete [] m_pkModelData->m_akObjects[i].m_akTexCoords;
    }

    delete m_pkModelImporter;
    delete m_pkModelData;
}

void MeshModel::render() const
{
    glCallList(m_iDisplayList);
}

bool MeshModel::load(
    const char *acFilename, 
    float afScale[3], 
    unsigned int uiTexUnit, 
    bool *bIsVisibleMeshes, 
    unsigned int uiMeshCount,
    const char* acTexturePath)
{
    m_pkModelImporter->load3DS(m_pkModelData, acFilename, afScale);  

    char *acFullpath = 0;
    for (uint i = 0; i < m_pkModelData->m_uiMaterialCount; i++)
    {
        char* acTextureFile = m_pkModelData->m_akMaterials[i].m_acFileName;
        if (strlen(acTextureFile) > 0)
        {
            if(acTexturePath)
            {
                acFullpath = new char[strlen(acTexturePath) + strlen(acTextureFile) + 2];
                sprintf(acFullpath, "%s/%s", acTexturePath, acTextureFile);
            }
            else
            {
                acFullpath = acTextureFile;
            }

            CreateTexture(gs_auiTextureLibrary, acFullpath, i);

            if(acTexturePath)
                delete [] acFullpath;
            acFullpath = 0;
        }

        m_pkModelData->m_akMaterials[i].m_iTextureId = i;
    }

    m_iDisplayList = glGenLists(1);
    glNewList(m_iDisplayList, GL_COMPILE);

    glEnable(GL_COLOR_MATERIAL);
    glColor3f(1, 1, 1);

    if(uiTexUnit == 0)
        uiTexUnit = GL_TEXTURE7_ARB;

    if(uiMeshCount == 0)
        uiMeshCount = m_pkModelData->m_uiObjectCount;

    for (uint i = 0; i < m_pkModelData->m_uiObjectCount; i++)
    {
        if (m_pkModelData->m_akObjects.size() <= 0) 
            break;

        ObjectData *akObjects = &(m_pkModelData->m_akObjects[i]);

        if(i < uiMeshCount && bIsVisibleMeshes && !bIsVisibleMeshes[i])
            continue;

        if (akObjects->m_bHasTexture)
        {
            glActiveTexture(uiTexUnit);
            glEnable(GL_TEXTURE_2D);
            glColor3ub(255, 255, 255);
            glBindTexture(GL_TEXTURE_2D, gs_auiTextureLibrary[akObjects->m_uiMaterialId]);
        }
        else
        {
            glDisable(GL_TEXTURE_2D);
            glColor3ub(255, 255, 255);
        }

        glMatrixMode(GL_MODELVIEW);
        glPushMatrix();
        glScalef(afScale[0], afScale[1], afScale[2]);
        glBegin(m_iPrimitiveType);                  

        for (uint j = 0; j < akObjects->m_uiFaceCount; j++)
        {
            for (uint uiVertex = 0; uiVertex < 3; uiVertex++)
            {
                int uiIndex = akObjects->m_akFaces[j].m_uiVertexIndex[uiVertex];

                glNormal3f(akObjects->m_akNormals[ uiIndex ].x, 
                           akObjects->m_akNormals[ uiIndex ].y, 
                           akObjects->m_akNormals[ uiIndex ].z);

                if (akObjects->m_bHasTexture)
                {
                    if (akObjects->m_akTexCoords)
                    {
                        glMultiTexCoord2f(uiTexUnit, 
                            +1.0f * akObjects->m_akTexCoords[ uiIndex ].x, 
                            -1.0f * akObjects->m_akTexCoords[ uiIndex ].y);
                    }
                }
                else
                {
                    if (m_pkModelData->m_akMaterials.size() && akObjects->m_uiMaterialId >= 0)
                    {
                        uint uiMaterialId = akObjects->m_uiMaterialId;
                        unsigned char *aucColor = m_pkModelData->m_akMaterials[uiMaterialId].m_aucColor;
                        glColor3ubv(aucColor); 
                    }
                }

                glVertex3f(akObjects->m_akVertices[ uiIndex ].x,
                           akObjects->m_akVertices[ uiIndex ].y,
                           akObjects->m_akVertices[ uiIndex ].z);
            }
        }

        glEnd();                                
        glPopMatrix();
    }

    glBindTexture(GL_TEXTURE_2D, 0);
    glDisable(GL_TEXTURE_2D);
    glActiveTexture(GL_TEXTURE0_ARB);
    glDisable(GL_COLOR_MATERIAL);
    glEndList();
    return true;
}
```

[Next](common-meshmodel.h.md)[Previous](common-memorybuffer.h.md)

