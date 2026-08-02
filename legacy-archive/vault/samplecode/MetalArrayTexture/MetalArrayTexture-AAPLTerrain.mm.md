---
title: MetalArrayTexture
apple_id: TP40016608
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/samplecode/MetalArrayTexture/Listings/MetalArrayTexture_AAPLTerrain_mm.html
archived_at: '2026-07-18T03:14:46.452830Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalArrayTexture](MetalArrayTexture.md)


[Next](MetalArrayTexture-AAPLTerrain.h.md)[Previous](MetalArrayTexture-AAPLTransforms.mm.md)

# MetalArrayTexture/AAPLTerrain.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for creating a terrain object.
 */

#ifdef TARGET_IOS
#import <UIKit/UIKit.h>
#else
#import <AppKit/AppKit.h>
#endif

#import <QuartzCore/QuartzCore.h>
#import <Metal/Metal.h>
#import <simd/simd.h>

#import "AAPLTerrain.h"
#import "GeoUtils.h"

const uint32_t kHeightMapDefaultSize = 64;

@interface AAPLTerrain ()

@property (nonatomic, readwrite) uint32_t heightMapSize;
@property (nonatomic, readwrite) uint32_t numOfSlices;

@end

@implementation AAPLTerrain
{
@private

    id <MTLBuffer> m_IndexBuffer;
    id <MTLBuffer> m_VertexBuffer;
    NSUInteger _indexCount;

    // height map
    GLfloat* _map;

    // Indicies
    NSUInteger  _vertexIndex;
    NSUInteger  _texCoordIndex;
    NSUInteger  _samplerIndex;
}

- (instancetype) initWithDevice:(id <MTLDevice>)device
{
    self = [super init];

    if(self)
    {
        self.heightMapSize = kHeightMapDefaultSize;
        self.numOfSlices = self.heightMapSize - 1;

        [self createTerrainWithDevice:device];

        _vertexIndex   = 0;
        _texCoordIndex = 1;
        _samplerIndex  = 0;
    }

    return self;
}

- (void)createTerrainWithDevice:(id <MTLDevice>)device
{
    if (!device)
    {
        NSLog(@">> ERROR: Invalid device!");

        return;
    }

    // Generate a heightmap
    // You can play around with the terrain generation here...
    _map = GenHeightMap(_heightMapSize, _heightMapSize, 0xDEADBEEF);
    //_map = GenHeightMap(_heightMapSize, _heightMapSize, 0xBEEFBEEF);

    // Now let's load this heightmap into the buffers

    // vertex buffer..
    size_t bufsize = _heightMapSize*_heightMapSize*3*sizeof(GLfloat);
    GLfloat* buf = (GLfloat*)malloc(bufsize);

    // the map buffer has 6 floats per vertex, position and normal
    // we are skipping the normals here since they are not used in our sample shader
    for (int n=0; n < _heightMapSize*_heightMapSize; n++)
        memcpy(&buf[n*3], &_map[n*6], sizeof(GLfloat)*3);

    // index buffer..
    _indexCount = (_heightMapSize-1) * (_heightMapSize*2+2);
    size_t indexBufsize = _indexCount * sizeof(uint16_t);
    uint16_t* indexBuf = (uint16_t*)malloc(indexBufsize);

    int i, j, ndx = 0;

    // This loads the terrain in, as vertical slices (think a cross section)
    // We load from the current row and row+1 to fill out the tristrips
    // number of slices = heightMapSize - 1
    for (j = 0; j < _heightMapSize-1; j++)
    {
        for (i = 0; i < _heightMapSize; i++)
        {
            // add an additional index to create degenerate triangles between consistent terrain strips
            if (i == 0) {
                indexBuf[ndx++] = (j *_heightMapSize + i);
            }

            indexBuf[ndx++] = (j *_heightMapSize + i);
            indexBuf[ndx++] = ((j+1) *_heightMapSize + i);

            // add an additional index to create degenerate triangles between consistent terrain strips
            if (i == _heightMapSize-1) {
                indexBuf[ndx++] = ((j+1) *_heightMapSize + i);
            }
        }
    }


    m_VertexBuffer = [device newBufferWithBytes:buf
                                         length:bufsize
                                        options:MTLResourceOptionCPUCacheModeDefault];
    if(!m_VertexBuffer)
    {
        NSLog(@">> ERROR: Failed creating vertex buffer!");
        return;
    }

    m_IndexBuffer = [device newBufferWithBytes:indexBuf
                                        length:indexBufsize
                                       options:MTLResourceOptionCPUCacheModeDefault];
    if(!m_IndexBuffer)
    {
        NSLog(@">> ERROR: Failed creating index buffer!");
        return;
    }


    free(buf);
    free(indexBuf);
}

- (void)encode:(id <MTLRenderCommandEncoder>)renderEncoder
{    
    [renderEncoder setVertexBuffer:m_VertexBuffer
                            offset:0
                           atIndex:_vertexIndex];

    // we use the vertex coordinates as texture coordinates too to index into the array texture
    [renderEncoder setVertexBuffer:m_VertexBuffer
                            offset:0
                           atIndex:_texCoordIndex];
}

- (void)draw:(id <MTLRenderCommandEncoder>)renderEncoder
{
    [renderEncoder drawIndexedPrimitives:MTLPrimitiveTypeTriangleStrip
                              indexCount:_indexCount
                               indexType:MTLIndexTypeUInt16
                             indexBuffer:m_IndexBuffer
                       indexBufferOffset:0
                           instanceCount:1];
}

@end
```

[Next](MetalArrayTexture-AAPLTerrain.h.md)[Previous](MetalArrayTexture-AAPLTransforms.mm.md)

