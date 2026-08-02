---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/SpriteKit.html
archived_at: '2026-07-18T02:55:38.420306Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# SpriteKit Changes for Swift

### SpriteKit

Removed [SKUniform.init(name: String, texture: SKTexture)](https://developer.apple.com/documentation/spritekit/skuniform/1455470-uniformwithname)Added [SKAction.animate(withWarps: [SKWarpGeometry], times: [NSNumber]) -> SKAction? [class]](https://developer.apple.com/documentation/spritekit/skaction/1690937-animate)Added [SKAction.animate(withWarps: [SKWarpGeometry], times: [NSNumber], restore: Bool) -> SKAction? [class]](https://developer.apple.com/documentation/spritekit/skaction/1690936-animate)Added [SKAction.scale(to: CGSize, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1643619-scaletosize)Added [SKAction.warp(to: SKWarpGeometry, duration: TimeInterval) -> SKAction? [class]](https://developer.apple.com/documentation/spritekit/skaction/1690951-warp)Added [SKAttribute](https://developer.apple.com/documentation/spritekit/skattribute)Added [SKAttribute.init(name: String, type: SKAttributeType)](https://developer.apple.com/documentation/spritekit/skattribute/1643431-initwithname)Added [SKAttribute.name](https://developer.apple.com/documentation/spritekit/skattribute/1643444-name)Added [SKAttribute.type](https://developer.apple.com/documentation/spritekit/skattribute/1643432-type)Added [SKAttributeType [enum]](https://developer.apple.com/documentation/spritekit/skattributetype)Added [SKAttributeType.float](https://developer.apple.com/documentation/spritekit/skattributetype/skattributetypefloat)Added [SKAttributeType.halfFloat](https://developer.apple.com/documentation/spritekit/skattributetype/skattributetypehalffloat)Added [SKAttributeType.none](https://developer.apple.com/documentation/spritekit/skattributetype/none)Added [SKAttributeType.vectorFloat2](https://developer.apple.com/documentation/spritekit/skattributetype/skattributetypevectorfloat2)Added [SKAttributeType.vectorFloat3](https://developer.apple.com/documentation/spritekit/skattributetype/vectorfloat3)Added [SKAttributeType.vectorFloat4](https://developer.apple.com/documentation/spritekit/skattributetype/vectorfloat4)Added [SKAttributeType.vectorHalfFloat2](https://developer.apple.com/documentation/spritekit/skattributetype/skattributetypevectorhalffloat2)Added [SKAttributeType.vectorHalfFloat3](https://developer.apple.com/documentation/spritekit/skattributetype/skattributetypevectorhalffloat3)Added [SKAttributeType.vectorHalfFloat4](https://developer.apple.com/documentation/spritekit/skattributetype/vectorhalffloat4)Added [SKAttributeValue](https://developer.apple.com/documentation/spritekit/skattributevalue)Added [SKAttributeValue.floatValue](https://developer.apple.com/documentation/spritekit/skattributevalue/1643424-floatvalue)Added [SKAttributeValue.init()](https://developer.apple.com/documentation/spritekit/skattributevalue/1643441-init)Added [SKAttributeValue.init(float: Float)](https://developer.apple.com/documentation/spritekit/skattributevalue/1643428-valuewithfloat)Added [SKAttributeValue.init(vectorFloat2: vector_float2)](https://developer.apple.com/documentation/spritekit/skattributevalue/1643427-valuewithvectorfloat2)Added [SKAttributeValue.init(vectorFloat3: vector_float3)](https://developer.apple.com/documentation/spritekit/skattributevalue/1643421-valuewithvectorfloat3)Added [SKAttributeValue.init(vectorFloat4: vector_float4)](https://developer.apple.com/documentation/spritekit/skattributevalue/1643436-init)Added [SKAttributeValue.vectorFloat2Value](https://developer.apple.com/documentation/spritekit/skattributevalue/1643435-vectorfloat2value)Added [SKAttributeValue.vectorFloat3Value](https://developer.apple.com/documentation/spritekit/skattributevalue/1643434-vectorfloat3value)Added [SKAttributeValue.vectorFloat4Value](https://developer.apple.com/documentation/spritekit/skattributevalue/1643442-vectorfloat4value)Added [SKNode.attributeValues](https://developer.apple.com/documentation/spritekit/sknode/1644181-attributevalues)Added [SKNode.setValue(_: SKAttributeValue, forAttribute: String)](https://developer.apple.com/documentation/spritekit/sknode/1644180-setvalue)Added [SKNode.value(forAttributeNamed: String) -> SKAttributeValue?](https://developer.apple.com/documentation/spritekit/sknode/1644182-value)Added [SKScene.sceneDidLoad()](https://developer.apple.com/documentation/spritekit/skscene/1645216-scenedidload)Added [SKShader.attributes](https://developer.apple.com/documentation/spritekit/skshader/1645287-attributes)Added [SKShapeNode.customPlaygroundQuickLook](https://developer.apple.com/documentation/spritekit/skshapenode/1645784-customplaygroundquicklook)Added [SKSpriteNode.customPlaygroundQuickLook](https://developer.apple.com/documentation/spritekit/skspritenode/1645797-customplaygroundquicklook)Added [SKSpriteNode.scale(to: CGSize)](https://developer.apple.com/documentation/spritekit/skspritenode/1645445-scaletosize)Added [SKTexture.customPlaygroundQuickLook](https://developer.apple.com/documentation/spritekit/sktexture/1645801-customplaygroundquicklook)Added [SKTextureAtlas.customPlaygroundQuickLook](https://developer.apple.com/documentation/spritekit/sktextureatlas/1645798-customplaygroundquicklook)Added [SKTileAdjacencyMask [struct]](https://developer.apple.com/documentation/spritekit/sktileadjacencymask)Added [SKTileAdjacencyMask.adjacencyAll](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643886-adjacencyall)Added [SKTileAdjacencyMask.adjacencyDown](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643890-adjacencydown)Added [SKTileAdjacencyMask.adjacencyDownEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencydownedge)Added [SKTileAdjacencyMask.adjacencyLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencyleft)Added [SKTileAdjacencyMask.adjacencyLeftEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencyleftedge)Added [SKTileAdjacencyMask.adjacencyLowerLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643828-adjacencylowerleft)Added [SKTileAdjacencyMask.adjacencyLowerLeftCorner](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1690894-adjacencylowerleftcorner)Added [SKTileAdjacencyMask.adjacencyLowerLeftEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencylowerleftedge)Added [SKTileAdjacencyMask.adjacencyLowerRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencylowerright)Added [SKTileAdjacencyMask.adjacencyLowerRightCorner](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencylowerrightcorner)Added [SKTileAdjacencyMask.adjacencyLowerRightEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1690896-adjacencylowerrightedge)Added [SKTileAdjacencyMask.adjacencyRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencyright)Added [SKTileAdjacencyMask.adjacencyRightEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1690892-adjacencyrightedge)Added [SKTileAdjacencyMask.adjacencyUp](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643824-adjacencyup)Added [SKTileAdjacencyMask.adjacencyUpEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1690889-adjacencyupedge)Added [SKTileAdjacencyMask.adjacencyUpperLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencyupperleft)Added [SKTileAdjacencyMask.adjacencyUpperLeftCorner](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1690899-adjacencyupperleftcorner)Added [SKTileAdjacencyMask.adjacencyUpperLeftEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1690897-adjacencyupperleftedge)Added [SKTileAdjacencyMask.adjacencyUpperRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencyupperright)Added [SKTileAdjacencyMask.adjacencyUpperRightCorner](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1690895-adjacencyupperrightcorner)Added [SKTileAdjacencyMask.adjacencyUpperRightEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1690898-adjacencyupperrightedge)Added [SKTileAdjacencyMask.hexFlatAdjacencyAll](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643899-hexflatadjacencyall)Added [SKTileAdjacencyMask.hexFlatAdjacencyDown](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktilehexflatadjacencydown)Added [SKTileAdjacencyMask.hexFlatAdjacencyLowerLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643821-hexflatadjacencylowerleft)Added [SKTileAdjacencyMask.hexFlatAdjacencyLowerRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643870-hexflatadjacencylowerright)Added [SKTileAdjacencyMask.hexFlatAdjacencyUp](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643844-hexflatadjacencyup)Added [SKTileAdjacencyMask.hexFlatAdjacencyUpperLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktilehexflatadjacencyupperleft)Added [SKTileAdjacencyMask.hexFlatAdjacencyUpperRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643869-hexflatadjacencyupperright)Added [SKTileAdjacencyMask.hexPointyAdjacencyAdd](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktilehexpointyadjacencyadd)Added [SKTileAdjacencyMask.hexPointyAdjacencyLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktilehexpointyadjacencyleft)Added [SKTileAdjacencyMask.hexPointyAdjacencyLowerLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktilehexpointyadjacencylowerleft)Added [SKTileAdjacencyMask.hexPointyAdjacencyLowerRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643892-hexpointyadjacencylowerright)Added [SKTileAdjacencyMask.hexPointyAdjacencyRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643859-hexpointyadjacencyright)Added [SKTileAdjacencyMask.hexPointyAdjacencyUpperLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktilehexpointyadjacencyupperleft)Added [SKTileAdjacencyMask.hexPointyAdjacencyUpperRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643900-hexpointyadjacencyupperright)Added [SKTileAdjacencyMask.init(rawValue: UInt)](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1645773-init)Added [SKTileDefinition](https://developer.apple.com/documentation/spritekit/sktiledefinition)Added [SKTileDefinition.flipHorizontally](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645804-fliphorizontally)Added [SKTileDefinition.flipVertically](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645800-flipvertically)Added [SKTileDefinition.init(texture: SKTexture)](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645815-initwithtexture)Added [SKTileDefinition.init(texture: SKTexture, normalTexture: SKTexture, size: CGSize)](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645778-initwithtexture)Added [SKTileDefinition.init(texture: SKTexture, size: CGSize)](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645787-initwithtexture)Added [SKTileDefinition.init(textures: [SKTexture], normalTextures: [SKTexture], size: CGSize, timePerFrame: CGFloat)](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645814-init)Added [SKTileDefinition.init(textures: [SKTexture], size: CGSize, timePerFrame: CGFloat)](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645776-initwithtextures)Added [SKTileDefinition.name](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645779-name)Added [SKTileDefinition.normalTextures](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645780-normaltextures)Added [SKTileDefinition.placementWeight](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645820-placementweight)Added [SKTileDefinition.rotation](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645775-rotation)Added [SKTileDefinition.size](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645790-size)Added [SKTileDefinition.textures](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645802-textures)Added [SKTileDefinition.timePerFrame](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645811-timeperframe)Added [SKTileDefinition.userData](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645813-userdata)Added [SKTileDefinitionRotation [enum]](https://developer.apple.com/documentation/spritekit/sktiledefinitionrotation)Added [SKTileDefinitionRotation.rotation0](https://developer.apple.com/documentation/spritekit/sktiledefinitionrotation/sktiledefinitionrotation0)Added [SKTileDefinitionRotation.rotation180](https://developer.apple.com/documentation/spritekit/sktiledefinitionrotation/rotation180)Added [SKTileDefinitionRotation.rotation270](https://developer.apple.com/documentation/spritekit/sktiledefinitionrotation/sktiledefinitionrotation270)Added [SKTileDefinitionRotation.rotation90](https://developer.apple.com/documentation/spritekit/sktiledefinitionrotation/sktiledefinitionrotation90)Added [SKTileGroup](https://developer.apple.com/documentation/spritekit/sktilegroup)Added [SKTileGroup.empty() -> Self [class]](https://developer.apple.com/documentation/spritekit/sktilegroup/1643840-empty)Added [SKTileGroup.init(rules: [SKTileGroupRule])](https://developer.apple.com/documentation/spritekit/sktilegroup/1643839-initwithrules)Added [SKTileGroup.init(tileDefinition: SKTileDefinition)](https://developer.apple.com/documentation/spritekit/sktilegroup/1643832-init)Added [SKTileGroup.name](https://developer.apple.com/documentation/spritekit/sktilegroup/1643893-name)Added [SKTileGroup.rules](https://developer.apple.com/documentation/spritekit/sktilegroup/1643867-rules)Added [SKTileGroupRule](https://developer.apple.com/documentation/spritekit/sktilegrouprule)Added [SKTileGroupRule.adjacency](https://developer.apple.com/documentation/spritekit/sktilegrouprule/1643818-adjacency)Added [SKTileGroupRule.init(adjacency: SKTileAdjacencyMask, tileDefinitions: [SKTileDefinition])](https://developer.apple.com/documentation/spritekit/sktilegrouprule/1643837-init)Added [SKTileGroupRule.name](https://developer.apple.com/documentation/spritekit/sktilegrouprule/1643860-name)Added [SKTileGroupRule.tileDefinitions](https://developer.apple.com/documentation/spritekit/sktilegrouprule/1643823-tiledefinitions)Added [SKTileMapNode](https://developer.apple.com/documentation/spritekit/sktilemapnode)Added [SKTileMapNode.anchorPoint](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643608-anchorpoint)Added [SKTileMapNode.blendMode](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643598-blendmode)Added [SKTileMapNode.centerOfTile(atColumn: Int, row: Int) -> CGPoint](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643599-centeroftileatcolumn)Added [SKTileMapNode.color](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643601-color)Added [SKTileMapNode.colorBlendFactor](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643607-colorblendfactor)Added [SKTileMapNode.enableAutomapping](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643604-enableautomapping)Added [SKTileMapNode.fill(with: SKTileGroup?)](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643615-fillwithtilegroup)Added [SKTileMapNode.init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize)](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643609-initwithtileset)Added [SKTileMapNode.init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, fillWith: SKTileGroup)](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643612-init)Added [SKTileMapNode.init(tileSet: SKTileSet, columns: Int, rows: Int, tileSize: CGSize, tileGroupLayout: [SKTileGroup])](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643597-init)Added [SKTileMapNode.lightingBitMask](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643618-lightingbitmask)Added [SKTileMapNode.mapSize](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643595-mapsize)Added [SKTileMapNode.numberOfColumns](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643600-numberofcolumns)Added [SKTileMapNode.numberOfRows](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643611-numberofrows)Added [SKTileMapNode.setTileGroup(_: SKTileGroup, andTileDefinition: SKTileDefinition, forColumn: Int, row: Int)](https://developer.apple.com/documentation/spritekit/sktilemapnode/1690935-settilegroup)Added [SKTileMapNode.setTileGroup(_: SKTileGroup?, forColumn: Int, row: Int)](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643605-settilegroup)Added [SKTileMapNode.shader](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643596-shader)Added [SKTileMapNode.tileColumnIndex(fromPosition: CGPoint) -> Int](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643617-tilecolumnindex)Added [SKTileMapNode.tileDefinition(atColumn: Int, row: Int) -> SKTileDefinition?](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643602-tiledefinitionatcolumn)Added [SKTileMapNode.tileGroup(atColumn: Int, row: Int) -> SKTileGroup?](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643613-tilegroupatcolumn)Added [SKTileMapNode.tileRowIndex(fromPosition: CGPoint) -> Int](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643614-tilerowindex)Added [SKTileMapNode.tileSet](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643610-tileset)Added [SKTileMapNode.tileSize](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643594-tilesize)Added [SKTileSet](https://developer.apple.com/documentation/spritekit/sktileset)Added [SKTileSet.defaultTileGroup](https://developer.apple.com/documentation/spritekit/sktileset/1643878-defaulttilegroup)Added [SKTileSet.defaultTileSize](https://developer.apple.com/documentation/spritekit/sktileset/1643889-defaulttilesize)Added [SKTileSet.init(from: URL)](https://developer.apple.com/documentation/spritekit/sktileset/1643830-tilesetfromurl)Added [SKTileSet.init(named: String)](https://developer.apple.com/documentation/spritekit/sktileset/1643819-tilesetnamed)Added [SKTileSet.init(tileGroups: [SKTileGroup])](https://developer.apple.com/documentation/spritekit/sktileset/1643885-init)Added [SKTileSet.init(tileGroups: [SKTileGroup], tileSetType: SKTileSetType)](https://developer.apple.com/documentation/spritekit/sktileset/1643896-init)Added [SKTileSet.name](https://developer.apple.com/documentation/spritekit/sktileset/1643888-name)Added [SKTileSet.tileGroups](https://developer.apple.com/documentation/spritekit/sktileset/1643874-tilegroups)Added [SKTileSet.type](https://developer.apple.com/documentation/spritekit/sktileset/1643836-type)Added [SKTileSetType [enum]](https://developer.apple.com/documentation/spritekit/sktilesettype)Added [SKTileSetType.grid](https://developer.apple.com/documentation/spritekit/sktilesettype/sktilesettypegrid)Added [SKTileSetType.hexagonalFlat](https://developer.apple.com/documentation/spritekit/sktilesettype/hexagonalflat)Added [SKTileSetType.hexagonalPointy](https://developer.apple.com/documentation/spritekit/sktilesettype/hexagonalpointy)Added [SKTileSetType.isometric](https://developer.apple.com/documentation/spritekit/sktilesettype/isometric)Added [SKUniform.init(name: String, matrixFloat2x2: matrix_float2x2)](https://developer.apple.com/documentation/spritekit/skuniform/1645806-initwithname)Added [SKUniform.init(name: String, matrixFloat3x3: matrix_float3x3)](https://developer.apple.com/documentation/spritekit/skuniform/1645799-init)Added [SKUniform.init(name: String, matrixFloat4x4: matrix_float4x4)](https://developer.apple.com/documentation/spritekit/skuniform/1645816-initwithname)Added [SKUniform.init(name: String, vectorFloat2: vector_float2)](https://developer.apple.com/documentation/spritekit/skuniform/1645782-init)Added [SKUniform.init(name: String, vectorFloat3: vector_float3)](https://developer.apple.com/documentation/spritekit/skuniform/1645803-initwithname)Added [SKUniform.init(name: String, vectorFloat4: vector_float4)](https://developer.apple.com/documentation/spritekit/skuniform/1645808-initwithname)Added [SKUniform.matrixFloat2x2Value](https://developer.apple.com/documentation/spritekit/skuniform/1645818-matrixfloat2x2value)Added [SKUniform.matrixFloat3x3Value](https://developer.apple.com/documentation/spritekit/skuniform/1645810-matrixfloat3x3value)Added [SKUniform.matrixFloat4x4Value](https://developer.apple.com/documentation/spritekit/skuniform/1645817-matrixfloat4x4value)Added [SKUniform.vectorFloat2Value](https://developer.apple.com/documentation/spritekit/skuniform/1645819-vectorfloat2value)Added [SKUniform.vectorFloat3Value](https://developer.apple.com/documentation/spritekit/skuniform/1645805-vectorfloat3value)Added [SKUniform.vectorFloat4Value](https://developer.apple.com/documentation/spritekit/skuniform/1645789-vectorfloat4value)Added [SKView.delegate](https://developer.apple.com/documentation/spritekit/skview/1642774-delegate)Added [SKView.preferredFrameRate](https://developer.apple.com/documentation/spritekit/skview/1642777-preferredframerate)Added [SKView.preferredFramesPerSecond](https://developer.apple.com/documentation/spritekit/skview/1642773-preferredframespersecond)Added [SKViewDelegate](https://developer.apple.com/documentation/spritekit/skviewdelegate)Added [SKViewDelegate.view(_: SKView, shouldRenderAtTime: TimeInterval) -> Bool](https://developer.apple.com/documentation/spritekit/skviewdelegate/1642775-view)Added [SKWarpable](https://developer.apple.com/documentation/spritekit/skwarpable)Added [SKWarpable.subdivisionLevels](https://developer.apple.com/documentation/spritekit/skwarpable/1690947-subdivisionlevels)Added [SKWarpable.warpGeometry](https://developer.apple.com/documentation/spritekit/skwarpable/1690953-warpgeometry)Added [SKWarpGeometry](https://developer.apple.com/documentation/spritekit/skwarpgeometry)Added [SKWarpGeometryGrid](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid)Added [SKWarpGeometryGrid.destPosition(at: Int) -> vector_float2](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690944-destpositionatindex)Added [SKWarpGeometryGrid.init(__columns: Int, rows: Int, sourcePositions: UnsafePointer<vector_float2>?, destPositions: UnsafePointer<vector_float2>?)](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690945-initwithcolumns)Added [SKWarpGeometryGrid.init(coder: NSCoder)](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690949-initwithcoder)Added [SKWarpGeometryGrid.init(columns: Int, rows: Int)](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690938-gridwithcolumns)Added [SKWarpGeometryGrid.init(columns: Int, rows: Int, sourcePositions: [float2], destinationPositions: [float2])](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/2325579-init)Added [SKWarpGeometryGrid.numberOfColumns](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690942-numberofcolumns)Added [SKWarpGeometryGrid.numberOfRows](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690943-numberofrows)Added [SKWarpGeometryGrid.replacingByDestinationPositions(positions: [float2]) -> SKWarpGeometryGrid](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/2292355-replacingbydestinationpositions)Added [SKWarpGeometryGrid.replacingBySourcePositions(positions: [float2]) -> SKWarpGeometryGrid](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/2292354-replacingbysourcepositions)Added [SKWarpGeometryGrid.sourcePosition(at: Int) -> vector_float2](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690952-sourceposition)Added [SKWarpGeometryGrid.vertexCount](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690940-vertexcount)Added SKVIEW_AVAILABLEModified [SK3DNode](https://developer.apple.com/documentation/spritekit/sk3dnode)

|  | Declaration |
| --- | --- |
| From | ``` class SK3DNode : SKNode {     init(viewportSize viewportSize: CGSize)     init?(coder aDecoder: NSCoder)     class func nodeWithViewportSize(_ viewportSize: CGSize) -> Self     var viewportSize: CGSize     var scnScene: SCNScene?     var sceneTime: NSTimeInterval     func hitTest(_ point: CGPoint, options options: [String : AnyObject]?) -> [SCNHitTestResult]     func projectPoint(_ point: vector_float3) -> vector_float3     func unprojectPoint(_ point: vector_float3) -> vector_float3     var playing: Bool     var loops: Bool     var pointOfView: SCNNode?     var autoenablesDefaultLighting: Bool } ``` |
| To | ``` class SK3DNode : SKNode {     init(viewportSize viewportSize: CGSize)     init?(coder aDecoder: NSCoder)     class func withViewportSize(_ viewportSize: CGSize) -> Self     var viewportSize: CGSize     var scnScene: SCNScene?     var sceneTime: TimeInterval     func hitTest(_ point: CGPoint, options options: [String : Any]? = nil) -> [SCNHitTestResult]     func projectPoint(_ point: vector_float3) -> vector_float3     func unprojectPoint(_ point: vector_float3) -> vector_float3     var isPlaying: Bool     var loops: Bool     var pointOfView: SCNNode?     var autoenablesDefaultLighting: Bool } ``` |

Modified [SK3DNode.hitTest(_: CGPoint, options: [String : Any]?) -> [SCNHitTestResult]](https://developer.apple.com/documentation/spritekit/sk3dnode/1519782-hittest)

|  | Declaration |
| --- | --- |
| From | ``` func hitTest(_ point: CGPoint, options options: [String : AnyObject]?) -> [SCNHitTestResult] ``` |
| To | ``` func hitTest(_ point: CGPoint, options options: [String : Any]? = nil) -> [SCNHitTestResult] ``` |

Modified [SK3DNode.isPlaying](https://developer.apple.com/documentation/spritekit/sk3dnode/1520297-playing)

|  | Declaration |
| --- | --- |
| From | ``` var playing: Bool ``` |
| To | ``` var isPlaying: Bool ``` |

Modified [SK3DNode.sceneTime](https://developer.apple.com/documentation/spritekit/sk3dnode/1519738-scenetime)

|  | Declaration |
| --- | --- |
| From | ``` var sceneTime: NSTimeInterval ``` |
| To | ``` var sceneTime: TimeInterval ``` |

Modified [SKAction](https://developer.apple.com/documentation/spritekit/skaction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKAction : NSObject, NSCopying, NSCoding {     var duration: NSTimeInterval     var timingMode: SKActionTimingMode     var timingFunction: SKActionTimingFunction     var speed: CGFloat     func reversedAction() -> SKAction } extension SKAction {     class func moveBy(_ delta: CGVector, duration sec: NSTimeInterval) -> SKAction     class func moveByX(_ deltaX: CGFloat, y deltaY: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func moveTo(_ location: CGPoint, duration sec: NSTimeInterval) -> SKAction     class func moveToX(_ x: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func moveToY(_ y: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func rotateByAngle(_ radians: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func rotateToAngle(_ radians: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func rotateToAngle(_ radians: CGFloat, duration sec: NSTimeInterval, shortestUnitArc shortestUnitArc: Bool) -> SKAction     class func resizeByWidth(_ width: CGFloat, height height: CGFloat, duration duration: NSTimeInterval) -> SKAction     class func resizeToWidth(_ width: CGFloat, height height: CGFloat, duration duration: NSTimeInterval) -> SKAction     class func resizeToWidth(_ width: CGFloat, duration duration: NSTimeInterval) -> SKAction     class func resizeToHeight(_ height: CGFloat, duration duration: NSTimeInterval) -> SKAction     class func scaleBy(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func scaleXBy(_ xScale: CGFloat, y yScale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func scaleTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func scaleXTo(_ xScale: CGFloat, y yScale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func scaleXTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func scaleYTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func sequence(_ actions: [SKAction]) -> SKAction     class func group(_ actions: [SKAction]) -> SKAction     class func repeatAction(_ action: SKAction, count count: Int) -> SKAction     class func repeatActionForever(_ action: SKAction) -> SKAction     class func fadeInWithDuration(_ sec: NSTimeInterval) -> SKAction     class func fadeOutWithDuration(_ sec: NSTimeInterval) -> SKAction     class func fadeAlphaBy(_ factor: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func fadeAlphaTo(_ alpha: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func hide() -> SKAction     class func unhide() -> SKAction     class func setTexture(_ texture: SKTexture) -> SKAction     class func setNormalTexture(_ texture: SKTexture) -> SKAction     class func setTexture(_ texture: SKTexture, resize resize: Bool) -> SKAction     class func setNormalTexture(_ texture: SKTexture, resize resize: Bool) -> SKAction     class func animateWithTextures(_ textures: [SKTexture], timePerFrame sec: NSTimeInterval) -> SKAction     class func animateWithNormalTextures(_ textures: [SKTexture], timePerFrame sec: NSTimeInterval) -> SKAction     class func animateWithTextures(_ textures: [SKTexture], timePerFrame sec: NSTimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction     class func animateWithNormalTextures(_ textures: [SKTexture], timePerFrame sec: NSTimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction     class func playSoundFileNamed(_ soundFile: String, waitForCompletion wait: Bool) -> SKAction     class func colorizeWithColor(_ color: UIColor, colorBlendFactor colorBlendFactor: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func colorizeWithColorBlendFactor(_ colorBlendFactor: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func falloffTo(_ falloff: Float, duration sec: NSTimeInterval) -> SKAction     class func falloffBy(_ falloff: Float, duration sec: NSTimeInterval) -> SKAction     class func followPath(_ path: CGPath, duration sec: NSTimeInterval) -> SKAction     class func followPath(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, duration sec: NSTimeInterval) -> SKAction     class func followPath(_ path: CGPath, speed speed: CGFloat) -> SKAction     class func followPath(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, speed speed: CGFloat) -> SKAction     class func speedBy(_ speed: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func speedTo(_ speed: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func reachTo(_ position: CGPoint, rootNode root: SKNode, duration sec: NSTimeInterval) -> SKAction     class func reachTo(_ position: CGPoint, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction     class func reachToNode(_ node: SKNode, rootNode root: SKNode, duration sec: NSTimeInterval) -> SKAction     class func reachToNode(_ node: SKNode, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction     class func strengthTo(_ strength: Float, duration sec: NSTimeInterval) -> SKAction     class func strengthBy(_ strength: Float, duration sec: NSTimeInterval) -> SKAction     class func waitForDuration(_ sec: NSTimeInterval) -> SKAction     class func waitForDuration(_ sec: NSTimeInterval, withRange durationRange: NSTimeInterval) -> SKAction     class func removeFromParent() -> SKAction     class func performSelector(_ selector: Selector, onTarget target: AnyObject) -> SKAction     class func runBlock(_ block: dispatch_block_t) -> SKAction     class func runBlock(_ block: dispatch_block_t, queue queue: dispatch_queue_t) -> SKAction     class func runAction(_ action: SKAction, onChildWithName name: String) -> SKAction     class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: (SKNode, CGFloat) -> Void) -> SKAction      init?(named name: String)     class func actionNamed(_ name: String) -> SKAction?      init?(named name: String, duration sec: NSTimeInterval)     class func actionNamed(_ name: String, duration sec: NSTimeInterval) -> SKAction?      init?(named name: String, fromURL url: NSURL)     class func actionNamed(_ name: String, fromURL url: NSURL) -> SKAction?      init?(named name: String, fromURL url: NSURL, duration sec: NSTimeInterval)     class func actionNamed(_ name: String, fromURL url: NSURL, duration sec: NSTimeInterval) -> SKAction? } extension SKAction {     class func changeChargeTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeChargeBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeMassTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeMassBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func applyForce(_ force: CGVector, duration sec: NSTimeInterval) -> SKAction     class func applyForce(_ force: CGVector, atPoint point: CGPoint, duration sec: NSTimeInterval) -> SKAction     class func applyTorque(_ torque: CGFloat, duration sec: NSTimeInterval) -> SKAction     class func applyImpulse(_ impulse: CGVector, duration sec: NSTimeInterval) -> SKAction     class func applyImpulse(_ impulse: CGVector, atPoint point: CGPoint, duration sec: NSTimeInterval) -> SKAction     class func applyAngularImpulse(_ impulse: CGFloat, duration sec: NSTimeInterval) -> SKAction } extension SKAction {     class func play() -> SKAction     class func pause() -> SKAction     class func stop() -> SKAction     class func changePlaybackRateTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changePlaybackRateBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction } extension SKAction {     class func changeVolumeTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeVolumeBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction } extension SKAction {     class func stereoPanTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func stereoPanBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeReverbTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeReverbBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeObstructionTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeObstructionBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeOcclusionTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction     class func changeOcclusionBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction } ``` | NSCoding, NSCopying |
| To | ``` class SKAction : NSObject, NSCopying, NSCoding {     var duration: TimeInterval     var timingMode: SKActionTimingMode     var timingFunction: SpriteKit.SKActionTimingFunction     var speed: CGFloat     func reversed() -> SKAction     class func stereoPan(to v: Float, duration duration: TimeInterval) -> SKAction     class func stereoPan(by v: Float, duration duration: TimeInterval) -> SKAction     class func changeReverb(to v: Float, duration duration: TimeInterval) -> SKAction     class func changeReverb(by v: Float, duration duration: TimeInterval) -> SKAction     class func changeObstruction(to v: Float, duration duration: TimeInterval) -> SKAction     class func changeObstruction(by v: Float, duration duration: TimeInterval) -> SKAction     class func changeOcclusion(to v: Float, duration duration: TimeInterval) -> SKAction     class func changeOcclusion(by v: Float, duration duration: TimeInterval) -> SKAction     class func warp(to warp: SKWarpGeometry, duration duration: TimeInterval) -> SKAction?     class func animate(withWarps warps: [SKWarpGeometry], times times: [NSNumber]) -> SKAction?     class func animate(withWarps warps: [SKWarpGeometry], times times: [NSNumber], restore restore: Bool) -> SKAction?     class func changeVolume(to v: Float, duration duration: TimeInterval) -> SKAction     class func changeVolume(by v: Float, duration duration: TimeInterval) -> SKAction     class func play() -> SKAction     class func pause() -> SKAction     class func stop() -> SKAction     class func changePlaybackRate(to v: Float, duration duration: TimeInterval) -> SKAction     class func changePlaybackRate(by v: Float, duration duration: TimeInterval) -> SKAction     class func changeCharge(to v: Float, duration duration: TimeInterval) -> SKAction     class func changeCharge(by v: Float, duration duration: TimeInterval) -> SKAction     class func changeMass(to v: Float, duration duration: TimeInterval) -> SKAction     class func changeMass(by v: Float, duration duration: TimeInterval) -> SKAction     class func applyForce(_ force: CGVector, duration sec: TimeInterval) -> SKAction     class func applyForce(_ force: CGVector, at point: CGPoint, duration sec: TimeInterval) -> SKAction     class func applyTorque(_ torque: CGFloat, duration sec: TimeInterval) -> SKAction     class func applyImpulse(_ impulse: CGVector, duration sec: TimeInterval) -> SKAction     class func applyImpulse(_ impulse: CGVector, at point: CGPoint, duration sec: TimeInterval) -> SKAction     class func applyAngularImpulse(_ impulse: CGFloat, duration sec: TimeInterval) -> SKAction     class func move(by delta: CGVector, duration sec: TimeInterval) -> SKAction     class func moveBy(x deltaX: CGFloat, y deltaY: CGFloat, duration sec: TimeInterval) -> SKAction     class func move(to location: CGPoint, duration sec: TimeInterval) -> SKAction     class func moveTo(x x: CGFloat, duration sec: TimeInterval) -> SKAction     class func moveTo(y y: CGFloat, duration sec: TimeInterval) -> SKAction     class func rotate(byAngle radians: CGFloat, duration sec: TimeInterval) -> SKAction     class func rotate(toAngle radians: CGFloat, duration sec: TimeInterval) -> SKAction     class func rotate(toAngle radians: CGFloat, duration sec: TimeInterval, shortestUnitArc shortestUnitArc: Bool) -> SKAction     class func resize(byWidth width: CGFloat, height height: CGFloat, duration duration: TimeInterval) -> SKAction     class func resize(toWidth width: CGFloat, height height: CGFloat, duration duration: TimeInterval) -> SKAction     class func resize(toWidth width: CGFloat, duration duration: TimeInterval) -> SKAction     class func resize(toHeight height: CGFloat, duration duration: TimeInterval) -> SKAction     class func scale(by scale: CGFloat, duration sec: TimeInterval) -> SKAction     class func scaleX(by xScale: CGFloat, y yScale: CGFloat, duration sec: TimeInterval) -> SKAction     class func scale(to scale: CGFloat, duration sec: TimeInterval) -> SKAction     class func scaleX(to xScale: CGFloat, y yScale: CGFloat, duration sec: TimeInterval) -> SKAction     class func scaleX(to scale: CGFloat, duration sec: TimeInterval) -> SKAction     class func scaleY(to scale: CGFloat, duration sec: TimeInterval) -> SKAction     class func scale(to size: CGSize, duration sec: TimeInterval) -> SKAction     class func sequence(_ actions: [SKAction]) -> SKAction     class func group(_ actions: [SKAction]) -> SKAction     class func `repeat`(_ action: SKAction, count count: Int) -> SKAction     class func repeatForever(_ action: SKAction) -> SKAction     class func fadeIn(withDuration sec: TimeInterval) -> SKAction     class func fadeOut(withDuration sec: TimeInterval) -> SKAction     class func fadeAlpha(by factor: CGFloat, duration sec: TimeInterval) -> SKAction     class func fadeAlpha(to alpha: CGFloat, duration sec: TimeInterval) -> SKAction     class func hide() -> SKAction     class func unhide() -> SKAction     class func setTexture(_ texture: SKTexture) -> SKAction     class func setNormalTexture(_ texture: SKTexture) -> SKAction     class func setTexture(_ texture: SKTexture, resize resize: Bool) -> SKAction     class func setNormalTexture(_ texture: SKTexture, resize resize: Bool) -> SKAction     class func animate(with textures: [SKTexture], timePerFrame sec: TimeInterval) -> SKAction     class func animate(withNormalTextures textures: [SKTexture], timePerFrame sec: TimeInterval) -> SKAction     class func animate(with textures: [SKTexture], timePerFrame sec: TimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction     class func animate(withNormalTextures textures: [SKTexture], timePerFrame sec: TimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction     class func playSoundFileNamed(_ soundFile: String, waitForCompletion wait: Bool) -> SKAction     class func colorize(with color: UIColor, colorBlendFactor colorBlendFactor: CGFloat, duration sec: TimeInterval) -> SKAction     class func colorize(withColorBlendFactor colorBlendFactor: CGFloat, duration sec: TimeInterval) -> SKAction     class func falloff(to falloff: Float, duration sec: TimeInterval) -> SKAction     class func falloff(by falloff: Float, duration sec: TimeInterval) -> SKAction     class func follow(_ path: CGPath, duration sec: TimeInterval) -> SKAction     class func follow(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, duration sec: TimeInterval) -> SKAction     class func follow(_ path: CGPath, speed speed: CGFloat) -> SKAction     class func follow(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, speed speed: CGFloat) -> SKAction     class func speed(by speed: CGFloat, duration sec: TimeInterval) -> SKAction     class func speed(to speed: CGFloat, duration sec: TimeInterval) -> SKAction     class func reach(to position: CGPoint, rootNode root: SKNode, duration sec: TimeInterval) -> SKAction     class func reach(to position: CGPoint, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction     class func reach(to node: SKNode, rootNode root: SKNode, duration sec: TimeInterval) -> SKAction     class func reach(to node: SKNode, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction     class func strength(to strength: Float, duration sec: TimeInterval) -> SKAction     class func strength(by strength: Float, duration sec: TimeInterval) -> SKAction     class func wait(forDuration sec: TimeInterval) -> SKAction     class func wait(forDuration sec: TimeInterval, withRange durationRange: TimeInterval) -> SKAction     class func removeFromParent() -> SKAction     class func perform(_ selector: Selector, onTarget target: Any) -> SKAction     class func run(_ block: @escaping () -> Swift.Void) -> SKAction     class func run(_ block: @escaping () -> Swift.Void, queue queue: DispatchQueue) -> SKAction     class func run(_ action: SKAction, onChildWithName name: String) -> SKAction     class func customAction(withDuration seconds: TimeInterval, actionBlock block: @escaping (SKNode, CGFloat) -> Swift.Void) -> SKAction      init?(named name: String)     class func actionNamed(_ name: String) -> SKAction?      init?(named name: String, duration sec: TimeInterval)     class func actionNamed(_ name: String, duration sec: TimeInterval) -> SKAction?      init?(named name: String, from url: URL)     class func actionNamed(_ name: String, from url: URL) -> SKAction?      init?(named name: String, from url: URL, duration sec: TimeInterval)     class func actionNamed(_ name: String, from url: URL, duration sec: TimeInterval) -> SKAction?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKAction : CVarArg { } extension SKAction : Equatable, Hashable {     var hashValue: Int { get } } extension SKAction {     class func move(by delta: CGVector, duration sec: TimeInterval) -> SKAction     class func moveBy(x deltaX: CGFloat, y deltaY: CGFloat, duration sec: TimeInterval) -> SKAction     class func move(to location: CGPoint, duration sec: TimeInterval) -> SKAction     class func moveTo(x x: CGFloat, duration sec: TimeInterval) -> SKAction     class func moveTo(y y: CGFloat, duration sec: TimeInterval) -> SKAction     class func rotate(byAngle radians: CGFloat, duration sec: TimeInterval) -> SKAction     class func rotate(toAngle radians: CGFloat, duration sec: TimeInterval) -> SKAction     class func rotate(toAngle radians: CGFloat, duration sec: TimeInterval, shortestUnitArc shortestUnitArc: Bool) -> SKAction     class func resize(byWidth width: CGFloat, height height: CGFloat, duration duration: TimeInterval) -> SKAction     class func resize(toWidth width: CGFloat, height height: CGFloat, duration duration: TimeInterval) -> SKAction     class func resize(toWidth width: CGFloat, duration duration: TimeInterval) -> SKAction     class func resize(toHeight height: CGFloat, duration duration: TimeInterval) -> SKAction     class func scale(by scale: CGFloat, duration sec: TimeInterval) -> SKAction     class func scaleX(by xScale: CGFloat, y yScale: CGFloat, duration sec: TimeInterval) -> SKAction     class func scale(to scale: CGFloat, duration sec: TimeInterval) -> SKAction     class func scaleX(to xScale: CGFloat, y yScale: CGFloat, duration sec: TimeInterval) -> SKAction     class func scaleX(to scale: CGFloat, duration sec: TimeInterval) -> SKAction     class func scaleY(to scale: CGFloat, duration sec: TimeInterval) -> SKAction     class func scale(to size: CGSize, duration sec: TimeInterval) -> SKAction     class func sequence(_ actions: [SKAction]) -> SKAction     class func group(_ actions: [SKAction]) -> SKAction     class func `repeat`(_ action: SKAction, count count: Int) -> SKAction     class func repeatForever(_ action: SKAction) -> SKAction     class func fadeIn(withDuration sec: TimeInterval) -> SKAction     class func fadeOut(withDuration sec: TimeInterval) -> SKAction     class func fadeAlpha(by factor: CGFloat, duration sec: TimeInterval) -> SKAction     class func fadeAlpha(to alpha: CGFloat, duration sec: TimeInterval) -> SKAction     class func hide() -> SKAction     class func unhide() -> SKAction     class func setTexture(_ texture: SKTexture) -> SKAction     class func setNormalTexture(_ texture: SKTexture) -> SKAction     class func setTexture(_ texture: SKTexture, resize resize: Bool) -> SKAction     class func setNormalTexture(_ texture: SKTexture, resize resize: Bool) -> SKAction     class func animate(with textures: [SKTexture], timePerFrame sec: TimeInterval) -> SKAction     class func animate(withNormalTextures textures: [SKTexture], timePerFrame sec: TimeInterval) -> SKAction     class func animate(with textures: [SKTexture], timePerFrame sec: TimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction     class func animate(withNormalTextures textures: [SKTexture], timePerFrame sec: TimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction     class func playSoundFileNamed(_ soundFile: String, waitForCompletion wait: Bool) -> SKAction     class func colorize(with color: UIColor, colorBlendFactor colorBlendFactor: CGFloat, duration sec: TimeInterval) -> SKAction     class func colorize(withColorBlendFactor colorBlendFactor: CGFloat, duration sec: TimeInterval) -> SKAction     class func falloff(to falloff: Float, duration sec: TimeInterval) -> SKAction     class func falloff(by falloff: Float, duration sec: TimeInterval) -> SKAction     class func follow(_ path: CGPath, duration sec: TimeInterval) -> SKAction     class func follow(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, duration sec: TimeInterval) -> SKAction     class func follow(_ path: CGPath, speed speed: CGFloat) -> SKAction     class func follow(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, speed speed: CGFloat) -> SKAction     class func speed(by speed: CGFloat, duration sec: TimeInterval) -> SKAction     class func speed(to speed: CGFloat, duration sec: TimeInterval) -> SKAction     class func reach(to position: CGPoint, rootNode root: SKNode, duration sec: TimeInterval) -> SKAction     class func reach(to position: CGPoint, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction     class func reach(to node: SKNode, rootNode root: SKNode, duration sec: TimeInterval) -> SKAction     class func reach(to node: SKNode, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction     class func strength(to strength: Float, duration sec: TimeInterval) -> SKAction     class func strength(by strength: Float, duration sec: TimeInterval) -> SKAction     class func wait(forDuration sec: TimeInterval) -> SKAction     class func wait(forDuration sec: TimeInterval, withRange durationRange: TimeInterval) -> SKAction     class func removeFromParent() -> SKAction     class func perform(_ selector: Selector, onTarget target: Any) -> SKAction     class func run(_ block: @escaping () -> Swift.Void) -> SKAction     class func run(_ block: @escaping () -> Swift.Void, queue queue: DispatchQueue) -> SKAction     class func run(_ action: SKAction, onChildWithName name: String) -> SKAction     class func customAction(withDuration seconds: TimeInterval, actionBlock block: @escaping (SKNode, CGFloat) -> Swift.Void) -> SKAction      init?(named name: String)     class func actionNamed(_ name: String) -> SKAction?      init?(named name: String, duration sec: TimeInterval)     class func actionNamed(_ name: String, duration sec: TimeInterval) -> SKAction?      init?(named name: String, from url: URL)     class func actionNamed(_ name: String, from url: URL) -> SKAction?      init?(named name: String, from url: URL, duration sec: TimeInterval)     class func actionNamed(_ name: String, from url: URL, duration sec: TimeInterval) -> SKAction? } extension SKAction {     class func changeCharge(to v: Float, duration duration: TimeInterval) -> SKAction     class func changeCharge(by v: Float, duration duration: TimeInterval) -> SKAction     class func changeMass(to v: Float, duration duration: TimeInterval) -> SKAction     class func changeMass(by v: Float, duration duration: TimeInterval) -> SKAction     class func applyForce(_ force: CGVector, duration sec: TimeInterval) -> SKAction     class func applyForce(_ force: CGVector, at point: CGPoint, duration sec: TimeInterval) -> SKAction     class func applyTorque(_ torque: CGFloat, duration sec: TimeInterval) -> SKAction     class func applyImpulse(_ impulse: CGVector, duration sec: TimeInterval) -> SKAction     class func applyImpulse(_ impulse: CGVector, at point: CGPoint, duration sec: TimeInterval) -> SKAction     class func applyAngularImpulse(_ impulse: CGFloat, duration sec: TimeInterval) -> SKAction } extension SKAction {     class func play() -> SKAction     class func pause() -> SKAction     class func stop() -> SKAction     class func changePlaybackRate(to v: Float, duration duration: TimeInterval) -> SKAction     class func changePlaybackRate(by v: Float, duration duration: TimeInterval) -> SKAction } extension SKAction {     class func changeVolume(to v: Float, duration duration: TimeInterval) -> SKAction     class func changeVolume(by v: Float, duration duration: TimeInterval) -> SKAction } extension SKAction {     class func stereoPan(to v: Float, duration duration: TimeInterval) -> SKAction     class func stereoPan(by v: Float, duration duration: TimeInterval) -> SKAction     class func changeReverb(to v: Float, duration duration: TimeInterval) -> SKAction     class func changeReverb(by v: Float, duration duration: TimeInterval) -> SKAction     class func changeObstruction(to v: Float, duration duration: TimeInterval) -> SKAction     class func changeObstruction(by v: Float, duration duration: TimeInterval) -> SKAction     class func changeOcclusion(to v: Float, duration duration: TimeInterval) -> SKAction     class func changeOcclusion(by v: Float, duration duration: TimeInterval) -> SKAction } extension SKAction {     class func warp(to warp: SKWarpGeometry, duration duration: TimeInterval) -> SKAction?     class func animate(withWarps warps: [SKWarpGeometry], times times: [NSNumber]) -> SKAction?     class func animate(withWarps warps: [SKWarpGeometry], times times: [NSNumber], restore restore: Bool) -> SKAction? } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying |

Modified [SKAction.animate(with: [SKTexture], timePerFrame: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417828-animate)

|  | Declaration |
| --- | --- |
| From | ``` class func animateWithTextures(_ textures: [SKTexture], timePerFrame sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func animate(with textures: [SKTexture], timePerFrame sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.animate(with: [SKTexture], timePerFrame: TimeInterval, resize: Bool, restore: Bool) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417656-animatewithtextures)

|  | Declaration |
| --- | --- |
| From | ``` class func animateWithTextures(_ textures: [SKTexture], timePerFrame sec: NSTimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction ``` |
| To | ``` class func animate(with textures: [SKTexture], timePerFrame sec: TimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction ``` |

Modified [SKAction.animate(withNormalTextures: [SKTexture], timePerFrame: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417746-animate)

|  | Declaration |
| --- | --- |
| From | ``` class func animateWithNormalTextures(_ textures: [SKTexture], timePerFrame sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func animate(withNormalTextures textures: [SKTexture], timePerFrame sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.animate(withNormalTextures: [SKTexture], timePerFrame: TimeInterval, resize: Bool, restore: Bool) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417810-animatewithnormaltextures)

|  | Declaration |
| --- | --- |
| From | ``` class func animateWithNormalTextures(_ textures: [SKTexture], timePerFrame sec: NSTimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction ``` |
| To | ``` class func animate(withNormalTextures textures: [SKTexture], timePerFrame sec: TimeInterval, resize resize: Bool, restore restore: Bool) -> SKAction ``` |

Modified [SKAction.applyAngularImpulse(_: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417775-applyangularimpulse)

|  | Declaration |
| --- | --- |
| From | ``` class func applyAngularImpulse(_ impulse: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func applyAngularImpulse(_ impulse: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.applyForce(_: CGVector, at: CGPoint, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417823-applyforce)

|  | Declaration |
| --- | --- |
| From | ``` class func applyForce(_ force: CGVector, atPoint point: CGPoint, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func applyForce(_ force: CGVector, at point: CGPoint, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.applyForce(_: CGVector, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417782-applyforce)

|  | Declaration |
| --- | --- |
| From | ``` class func applyForce(_ force: CGVector, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func applyForce(_ force: CGVector, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.applyImpulse(_: CGVector, at: CGPoint, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417732-applyimpulse)

|  | Declaration |
| --- | --- |
| From | ``` class func applyImpulse(_ impulse: CGVector, atPoint point: CGPoint, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func applyImpulse(_ impulse: CGVector, at point: CGPoint, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.applyImpulse(_: CGVector, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417770-applyimpulse)

|  | Declaration |
| --- | --- |
| From | ``` class func applyImpulse(_ impulse: CGVector, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func applyImpulse(_ impulse: CGVector, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.applyTorque(_: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417756-applytorque)

|  | Declaration |
| --- | --- |
| From | ``` class func applyTorque(_ torque: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func applyTorque(_ torque: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.changeCharge(by: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417714-changechargeby)

|  | Declaration |
| --- | --- |
| From | ``` class func changeChargeBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func changeCharge(by v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.changeCharge(to: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417752-changechargeto)

|  | Declaration |
| --- | --- |
| From | ``` class func changeChargeTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func changeCharge(to v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.changeMass(by: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417710-changemassby)

|  | Declaration |
| --- | --- |
| From | ``` class func changeMassBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func changeMass(by v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.changeMass(to: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417780-changemassto)

|  | Declaration |
| --- | --- |
| From | ``` class func changeMassTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func changeMass(to v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.changeObstruction(by: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1520346-changeobstructionby)

|  | Declaration |
| --- | --- |
| From | ``` class func changeObstructionBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func changeObstruction(by v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.changeObstruction(to: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1519718-changeobstructionto)

|  | Declaration |
| --- | --- |
| From | ``` class func changeObstructionTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func changeObstruction(to v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.changeOcclusion(by: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1520117-changeocclusionby)

|  | Declaration |
| --- | --- |
| From | ``` class func changeOcclusionBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func changeOcclusion(by v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.changeOcclusion(to: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1520433-changeocclusionto)

|  | Declaration |
| --- | --- |
| From | ``` class func changeOcclusionTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func changeOcclusion(to v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.changePlaybackRate(by: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417670-changeplaybackrate)

|  | Declaration |
| --- | --- |
| From | ``` class func changePlaybackRateBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func changePlaybackRate(by v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.changePlaybackRate(to: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417808-changeplaybackrate)

|  | Declaration |
| --- | --- |
| From | ``` class func changePlaybackRateTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func changePlaybackRate(to v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.changeReverb(by: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1519568-changereverb)

|  | Declaration |
| --- | --- |
| From | ``` class func changeReverbBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func changeReverb(by v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.changeReverb(to: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1520320-changereverbto)

|  | Declaration |
| --- | --- |
| From | ``` class func changeReverbTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func changeReverb(to v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.changeVolume(by: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417726-changevolumeby)

|  | Declaration |
| --- | --- |
| From | ``` class func changeVolumeBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func changeVolume(by v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.changeVolume(to: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417682-changevolumeto)

|  | Declaration |
| --- | --- |
| From | ``` class func changeVolumeTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func changeVolume(to v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.colorize(with: UIColor, colorBlendFactor: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417678-colorizewithcolor)

|  | Declaration |
| --- | --- |
| From | ``` class func colorizeWithColor(_ color: UIColor, colorBlendFactor colorBlendFactor: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func colorize(with color: UIColor, colorBlendFactor colorBlendFactor: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.colorize(withColorBlendFactor: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417736-colorize)

|  | Declaration |
| --- | --- |
| From | ``` class func colorizeWithColorBlendFactor(_ colorBlendFactor: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func colorize(withColorBlendFactor colorBlendFactor: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.customAction(withDuration: TimeInterval, actionBlock: (SKNode, CGFloat) -> Swift.Void) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417745-customactionwithduration)

|  | Declaration |
| --- | --- |
| From | ``` class func customActionWithDuration(_ seconds: NSTimeInterval, actionBlock block: (SKNode, CGFloat) -> Void) -> SKAction ``` |
| To | ``` class func customAction(withDuration seconds: TimeInterval, actionBlock block: @escaping (SKNode, CGFloat) -> Swift.Void) -> SKAction ``` |

Modified [SKAction.duration](https://developer.apple.com/documentation/spritekit/skaction/1417790-duration)

|  | Declaration |
| --- | --- |
| From | ``` var duration: NSTimeInterval ``` |
| To | ``` var duration: TimeInterval ``` |

Modified [SKAction.fadeAlpha(by: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417716-fadealpha)

|  | Declaration |
| --- | --- |
| From | ``` class func fadeAlphaBy(_ factor: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func fadeAlpha(by factor: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.fadeAlpha(to: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417673-fadealphato)

|  | Declaration |
| --- | --- |
| From | ``` class func fadeAlphaTo(_ alpha: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func fadeAlpha(to alpha: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.fadeIn(withDuration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417818-fadeinwithduration)

|  | Declaration |
| --- | --- |
| From | ``` class func fadeInWithDuration(_ sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func fadeIn(withDuration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.fadeOut(withDuration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417738-fadeout)

|  | Declaration |
| --- | --- |
| From | ``` class func fadeOutWithDuration(_ sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func fadeOut(withDuration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.falloff(by: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417766-falloffby)

|  | Declaration |
| --- | --- |
| From | ``` class func falloffBy(_ falloff: Float, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func falloff(by falloff: Float, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.falloff(to: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417758-falloff)

|  | Declaration |
| --- | --- |
| From | ``` class func falloffTo(_ falloff: Float, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func falloff(to falloff: Float, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.follow(_: CGPath, asOffset: Bool, orientToPath: Bool, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417662-followpath)

|  | Declaration |
| --- | --- |
| From | ``` class func followPath(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func follow(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.follow(_: CGPath, asOffset: Bool, orientToPath: Bool, speed: CGFloat) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417798-followpath)

|  | Declaration |
| --- | --- |
| From | ``` class func followPath(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, speed speed: CGFloat) -> SKAction ``` |
| To | ``` class func follow(_ path: CGPath, asOffset offset: Bool, orientToPath orient: Bool, speed speed: CGFloat) -> SKAction ``` |

Modified [SKAction.follow(_: CGPath, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417822-follow)

|  | Declaration |
| --- | --- |
| From | ``` class func followPath(_ path: CGPath, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func follow(_ path: CGPath, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.follow(_: CGPath, speed: CGFloat) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417786-follow)

|  | Declaration |
| --- | --- |
| From | ``` class func followPath(_ path: CGPath, speed speed: CGFloat) -> SKAction ``` |
| To | ``` class func follow(_ path: CGPath, speed speed: CGFloat) -> SKAction ``` |

Modified [SKAction.init(named: String, duration: TimeInterval)](https://developer.apple.com/documentation/spritekit/skaction/1417697-actionnamed)

|  | Declaration |
| --- | --- |
| From | ``` init?(named name: String, duration sec: NSTimeInterval) ``` |
| To | ``` init?(named name: String, duration sec: TimeInterval) ``` |

Modified [SKAction.init(named: String, from: URL)](https://developer.apple.com/documentation/spritekit/skaction/1417680-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(named name: String, fromURL url: NSURL) ``` |
| To | ``` init?(named name: String, from url: URL) ``` |

Modified [SKAction.init(named: String, from: URL, duration: TimeInterval)](https://developer.apple.com/documentation/spritekit/skaction/1417754-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(named name: String, fromURL url: NSURL, duration sec: NSTimeInterval) ``` |
| To | ``` init?(named name: String, from url: URL, duration sec: TimeInterval) ``` |

Modified [SKAction.move(by: CGVector, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417739-move)

|  | Declaration |
| --- | --- |
| From | ``` class func moveBy(_ delta: CGVector, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func move(by delta: CGVector, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.move(to: CGPoint, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417768-moveto)

|  | Declaration |
| --- | --- |
| From | ``` class func moveTo(_ location: CGPoint, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func move(to location: CGPoint, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.moveBy(x: CGFloat, y: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417722-moveby)

|  | Declaration |
| --- | --- |
| From | ``` class func moveByX(_ deltaX: CGFloat, y deltaY: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func moveBy(x deltaX: CGFloat, y deltaY: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.moveTo(x: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417779-moveto)

|  | Declaration |
| --- | --- |
| From | ``` class func moveToX(_ x: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func moveTo(x x: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.moveTo(y: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417781-movetoy)

|  | Declaration |
| --- | --- |
| From | ``` class func moveToY(_ y: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func moveTo(y y: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.perform(_: Selector, onTarget: Any) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417764-perform)

|  | Declaration |
| --- | --- |
| From | ``` class func performSelector(_ selector: Selector, onTarget target: AnyObject) -> SKAction ``` |
| To | ``` class func perform(_ selector: Selector, onTarget target: Any) -> SKAction ``` |

Modified [SKAction.reach(to: SKNode, rootNode: SKNode, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417827-reachtonode)

|  | Declaration |
| --- | --- |
| From | ``` class func reachToNode(_ node: SKNode, rootNode root: SKNode, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func reach(to node: SKNode, rootNode root: SKNode, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.reach(to: CGPoint, rootNode: SKNode, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417773-reachto)

|  | Declaration |
| --- | --- |
| From | ``` class func reachTo(_ position: CGPoint, rootNode root: SKNode, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func reach(to position: CGPoint, rootNode root: SKNode, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.reach(to: SKNode, rootNode: SKNode, velocity: CGFloat) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417801-reachtonode)

|  | Declaration |
| --- | --- |
| From | ``` class func reachToNode(_ node: SKNode, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction ``` |
| To | ``` class func reach(to node: SKNode, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction ``` |

Modified [SKAction.reach(to: CGPoint, rootNode: SKNode, velocity: CGFloat) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417720-reach)

|  | Declaration |
| --- | --- |
| From | ``` class func reachTo(_ position: CGPoint, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction ``` |
| To | ``` class func reach(to position: CGPoint, rootNode root: SKNode, velocity velocity: CGFloat) -> SKAction ``` |

Modified [SKAction.repeat(_: SKAction, count: Int) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417750-repeataction)

|  | Declaration |
| --- | --- |
| From | ``` class func repeatAction(_ action: SKAction, count count: Int) -> SKAction ``` |
| To | ``` class func `repeat`(_ action: SKAction, count count: Int) -> SKAction ``` |

Modified [SKAction.repeatForever(_: SKAction) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417676-repeatforever)

|  | Declaration |
| --- | --- |
| From | ``` class func repeatActionForever(_ action: SKAction) -> SKAction ``` |
| To | ``` class func repeatForever(_ action: SKAction) -> SKAction ``` |

Modified [SKAction.resize(byWidth: CGFloat, height: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417812-resizebywidth)

|  | Declaration |
| --- | --- |
| From | ``` class func resizeByWidth(_ width: CGFloat, height height: CGFloat, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func resize(byWidth width: CGFloat, height height: CGFloat, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.resize(toHeight: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417825-resizetoheight)

|  | Declaration |
| --- | --- |
| From | ``` class func resizeToHeight(_ height: CGFloat, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func resize(toHeight height: CGFloat, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.resize(toWidth: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417686-resize)

|  | Declaration |
| --- | --- |
| From | ``` class func resizeToWidth(_ width: CGFloat, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func resize(toWidth width: CGFloat, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.resize(toWidth: CGFloat, height: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417724-resize)

|  | Declaration |
| --- | --- |
| From | ``` class func resizeToWidth(_ width: CGFloat, height height: CGFloat, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func resize(toWidth width: CGFloat, height height: CGFloat, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.reversed() -> SKAction](https://developer.apple.com/documentation/spritekit/skaction/1417803-reversedaction)

|  | Declaration |
| --- | --- |
| From | ``` func reversedAction() -> SKAction ``` |
| To | ``` func reversed() -> SKAction ``` |

Modified [SKAction.rotate(byAngle: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417805-rotate)

|  | Declaration |
| --- | --- |
| From | ``` class func rotateByAngle(_ radians: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func rotate(byAngle radians: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.rotate(toAngle: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417668-rotatetoangle)

|  | Declaration |
| --- | --- |
| From | ``` class func rotateToAngle(_ radians: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func rotate(toAngle radians: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.rotate(toAngle: CGFloat, duration: TimeInterval, shortestUnitArc: Bool) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417700-rotate)

|  | Declaration |
| --- | --- |
| From | ``` class func rotateToAngle(_ radians: CGFloat, duration sec: NSTimeInterval, shortestUnitArc shortestUnitArc: Bool) -> SKAction ``` |
| To | ``` class func rotate(toAngle radians: CGFloat, duration sec: TimeInterval, shortestUnitArc shortestUnitArc: Bool) -> SKAction ``` |

Modified [SKAction.run(_: () -> Swift.Void) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417692-runblock)

|  | Declaration |
| --- | --- |
| From | ``` class func runBlock(_ block: dispatch_block_t) -> SKAction ``` |
| To | ``` class func run(_ block: @escaping () -> Swift.Void) -> SKAction ``` |

Modified [SKAction.run(_: SKAction, onChildWithName: String) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417671-run)

|  | Declaration |
| --- | --- |
| From | ``` class func runAction(_ action: SKAction, onChildWithName name: String) -> SKAction ``` |
| To | ``` class func run(_ action: SKAction, onChildWithName name: String) -> SKAction ``` |

Modified [SKAction.run(_: () -> Swift.Void, queue: DispatchQueue) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417799-runblock)

|  | Declaration |
| --- | --- |
| From | ``` class func runBlock(_ block: dispatch_block_t, queue queue: dispatch_queue_t) -> SKAction ``` |
| To | ``` class func run(_ block: @escaping () -> Swift.Void, queue queue: DispatchQueue) -> SKAction ``` |

Modified [SKAction.scale(by: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417741-scaleby)

|  | Declaration |
| --- | --- |
| From | ``` class func scaleBy(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func scale(by scale: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.scale(to: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417712-scale)

|  | Declaration |
| --- | --- |
| From | ``` class func scaleTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func scale(to scale: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.scaleX(by: CGFloat, y: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417796-scalex)

|  | Declaration |
| --- | --- |
| From | ``` class func scaleXBy(_ xScale: CGFloat, y yScale: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func scaleX(by xScale: CGFloat, y yScale: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.scaleX(to: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417699-scalexto)

|  | Declaration |
| --- | --- |
| From | ``` class func scaleXTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func scaleX(to scale: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.scaleX(to: CGFloat, y: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417728-scalex)

|  | Declaration |
| --- | --- |
| From | ``` class func scaleXTo(_ xScale: CGFloat, y yScale: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func scaleX(to xScale: CGFloat, y yScale: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.scaleY(to: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417708-scaleyto)

|  | Declaration |
| --- | --- |
| From | ``` class func scaleYTo(_ scale: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func scaleY(to scale: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.speed(by: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417690-speedby)

|  | Declaration |
| --- | --- |
| From | ``` class func speedBy(_ speed: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func speed(by speed: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.speed(to: CGFloat, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417684-speedto)

|  | Declaration |
| --- | --- |
| From | ``` class func speedTo(_ speed: CGFloat, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func speed(to speed: CGFloat, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.stereoPan(by: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1519713-stereopan)

|  | Declaration |
| --- | --- |
| From | ``` class func stereoPanBy(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func stereoPan(by v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.stereoPan(to: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1519976-stereopanto)

|  | Declaration |
| --- | --- |
| From | ``` class func stereoPanTo(_ v: Float, duration duration: NSTimeInterval) -> SKAction ``` |
| To | ``` class func stereoPan(to v: Float, duration duration: TimeInterval) -> SKAction ``` |

Modified [SKAction.strength(by: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417762-strength)

|  | Declaration |
| --- | --- |
| From | ``` class func strengthBy(_ strength: Float, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func strength(by strength: Float, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.strength(to: Float, duration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417815-strength)

|  | Declaration |
| --- | --- |
| From | ``` class func strengthTo(_ strength: Float, duration sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func strength(to strength: Float, duration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.timingFunction](https://developer.apple.com/documentation/spritekit/skaction/1417666-timingfunction)

|  | Declaration |
| --- | --- |
| From | ``` var timingFunction: SKActionTimingFunction ``` |
| To | ``` var timingFunction: SpriteKit.SKActionTimingFunction ``` |

Modified [SKAction.wait(forDuration: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417788-waitforduration)

|  | Declaration |
| --- | --- |
| From | ``` class func waitForDuration(_ sec: NSTimeInterval) -> SKAction ``` |
| To | ``` class func wait(forDuration sec: TimeInterval) -> SKAction ``` |

Modified [SKAction.wait(forDuration: TimeInterval, withRange: TimeInterval) -> SKAction [class]](https://developer.apple.com/documentation/spritekit/skaction/1417760-wait)

|  | Declaration |
| --- | --- |
| From | ``` class func waitForDuration(_ sec: NSTimeInterval, withRange durationRange: NSTimeInterval) -> SKAction ``` |
| To | ``` class func wait(forDuration sec: TimeInterval, withRange durationRange: TimeInterval) -> SKAction ``` |

Modified [SKActionTimingMode [enum]](https://developer.apple.com/documentation/spritekit/skactiontimingmode)

|  | Declaration |
| --- | --- |
| From | ``` enum SKActionTimingMode : Int {     case Linear     case EaseIn     case EaseOut     case EaseInEaseOut } ``` |
| To | ``` enum SKActionTimingMode : Int {     case linear     case easeIn     case easeOut     case easeInEaseOut } ``` |

Modified [SKActionTimingMode.easeIn](https://developer.apple.com/documentation/spritekit/skactiontimingmode/easein)

|  | Declaration |
| --- | --- |
| From | ``` case EaseIn ``` |
| To | ``` case easeIn ``` |

Modified [SKActionTimingMode.easeInEaseOut](https://developer.apple.com/documentation/spritekit/skactiontimingmode/easeineaseout)

|  | Declaration |
| --- | --- |
| From | ``` case EaseInEaseOut ``` |
| To | ``` case easeInEaseOut ``` |

Modified [SKActionTimingMode.easeOut](https://developer.apple.com/documentation/spritekit/skactiontimingmode/easeout)

|  | Declaration |
| --- | --- |
| From | ``` case EaseOut ``` |
| To | ``` case easeOut ``` |

Modified [SKActionTimingMode.linear](https://developer.apple.com/documentation/spritekit/skactiontimingmode/linear)

|  | Declaration |
| --- | --- |
| From | ``` case Linear ``` |
| To | ``` case linear ``` |

Modified [SKAudioNode](https://developer.apple.com/documentation/spritekit/skaudionode)

|  | Declaration |
| --- | --- |
| From | ``` class SKAudioNode : SKNode, NSCoding {     init(AVAudioNode node: AVAudioNode?)     init?(coder aDecoder: NSCoder)     convenience init(fileNamed name: String)     convenience init(URL url: NSURL)     var avAudioNode: AVAudioNode?     var autoplayLooped: Bool     var positional: Bool } ``` |
| To | ``` class SKAudioNode : SKNode, NSCoding {     init(avAudioNode node: AVAudioNode?)     init?(coder aDecoder: NSCoder)     convenience init(fileNamed name: String)     convenience init(url url: URL)     var avAudioNode: AVAudioNode?     var autoplayLooped: Bool     var isPositional: Bool } ``` |

Modified [SKAudioNode.init(avAudioNode: AVAudioNode?)](https://developer.apple.com/documentation/spritekit/skaudionode/1520232-initwithavaudionode)

|  | Declaration |
| --- | --- |
| From | ``` init(AVAudioNode node: AVAudioNode?) ``` |
| To | ``` init(avAudioNode node: AVAudioNode?) ``` |

Modified [SKAudioNode.init(url: URL)](https://developer.apple.com/documentation/spritekit/skaudionode/1519661-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(URL url: NSURL) ``` |
| To | ``` convenience init(url url: URL) ``` |

Modified [SKAudioNode.isPositional](https://developer.apple.com/documentation/spritekit/skaudionode/1520418-ispositional)

|  | Declaration |
| --- | --- |
| From | ``` var positional: Bool ``` |
| To | ``` var isPositional: Bool ``` |

Modified [SKBlendMode [enum]](https://developer.apple.com/documentation/spritekit/skblendmode)

|  | Declaration |
| --- | --- |
| From | ``` enum SKBlendMode : Int {     case Alpha     case Add     case Subtract     case Multiply     case MultiplyX2     case Screen     case Replace } ``` |
| To | ``` enum SKBlendMode : Int {     case alpha     case add     case subtract     case multiply     case multiplyX2     case screen     case replace } ``` |

Modified [SKBlendMode.add](https://developer.apple.com/documentation/spritekit/skblendmode/skblendmodeadd)

|  | Declaration |
| --- | --- |
| From | ``` case Add ``` |
| To | ``` case add ``` |

Modified [SKBlendMode.alpha](https://developer.apple.com/documentation/spritekit/skblendmode/skblendmodealpha)

|  | Declaration |
| --- | --- |
| From | ``` case Alpha ``` |
| To | ``` case alpha ``` |

Modified [SKBlendMode.multiply](https://developer.apple.com/documentation/spritekit/skblendmode/skblendmodemultiply)

|  | Declaration |
| --- | --- |
| From | ``` case Multiply ``` |
| To | ``` case multiply ``` |

Modified [SKBlendMode.multiplyX2](https://developer.apple.com/documentation/spritekit/skblendmode/skblendmodemultiplyx2)

|  | Declaration |
| --- | --- |
| From | ``` case MultiplyX2 ``` |
| To | ``` case multiplyX2 ``` |

Modified [SKBlendMode.replace](https://developer.apple.com/documentation/spritekit/skblendmode/replace)

|  | Declaration |
| --- | --- |
| From | ``` case Replace ``` |
| To | ``` case replace ``` |

Modified [SKBlendMode.screen](https://developer.apple.com/documentation/spritekit/skblendmode/screen)

|  | Declaration |
| --- | --- |
| From | ``` case Screen ``` |
| To | ``` case screen ``` |

Modified [SKBlendMode.subtract](https://developer.apple.com/documentation/spritekit/skblendmode/skblendmodesubtract)

|  | Declaration |
| --- | --- |
| From | ``` case Subtract ``` |
| To | ``` case subtract ``` |

Modified [SKCameraNode](https://developer.apple.com/documentation/spritekit/skcameranode)

|  | Declaration |
| --- | --- |
| From | ``` class SKCameraNode : SKNode {     func containsNode(_ node: SKNode) -> Bool     func containedNodeSet() -> Set<SKNode> } ``` |
| To | ``` class SKCameraNode : SKNode {     func contains(_ node: SKNode) -> Bool     func containedNodeSet() -> Set<SKNode> } ``` |

Modified [SKCameraNode.contains(_: SKNode) -> Bool](https://developer.apple.com/documentation/spritekit/skcameranode/1434224-containsnode)

|  | Declaration |
| --- | --- |
| From | ``` func containsNode(_ node: SKNode) -> Bool ``` |
| To | ``` func contains(_ node: SKNode) -> Bool ``` |

Modified [SKConstraint](https://developer.apple.com/documentation/spritekit/skconstraint)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKConstraint : NSObject, NSCoding, NSCopying {     var enabled: Bool     var referenceNode: SKNode?     class func positionX(_ range: SKRange) -> Self     class func positionY(_ range: SKRange) -> Self     class func positionX(_ xRange: SKRange, y yRange: SKRange) -> Self     class func distance(_ range: SKRange, toNode node: SKNode) -> Self     class func distance(_ range: SKRange, toPoint point: CGPoint) -> Self     class func distance(_ range: SKRange, toPoint point: CGPoint, inNode node: SKNode) -> Self     class func zRotation(_ zRange: SKRange) -> Self     class func orientToNode(_ node: SKNode, offset radians: SKRange) -> Self     class func orientToPoint(_ point: CGPoint, offset radians: SKRange) -> Self     class func orientToPoint(_ point: CGPoint, inNode node: SKNode, offset radians: SKRange) -> Self } ``` | NSCoding, NSCopying |
| To | ``` class SKConstraint : NSObject, NSCoding, NSCopying {     var enabled: Bool     var referenceNode: SKNode?     class func positionX(_ range: SKRange) -> Self     class func positionY(_ range: SKRange) -> Self     class func positionX(_ xRange: SKRange, y yRange: SKRange) -> Self     class func distance(_ range: SKRange, to node: SKNode) -> Self     class func distance(_ range: SKRange, to point: CGPoint) -> Self     class func distance(_ range: SKRange, to point: CGPoint, in node: SKNode) -> Self     class func zRotation(_ zRange: SKRange) -> Self     class func orient(to node: SKNode, offset radians: SKRange) -> Self     class func orient(to point: CGPoint, offset radians: SKRange) -> Self     class func orient(to point: CGPoint, in node: SKNode, offset radians: SKRange) -> Self     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKConstraint : CVarArg { } extension SKConstraint : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying |

Modified [SKConstraint.distance(_: SKRange, to: SKNode) -> Self [class]](https://developer.apple.com/documentation/spritekit/skconstraint/1519750-distance)

|  | Declaration |
| --- | --- |
| From | ``` class func distance(_ range: SKRange, toNode node: SKNode) -> Self ``` |
| To | ``` class func distance(_ range: SKRange, to node: SKNode) -> Self ``` |

Modified [SKConstraint.distance(_: SKRange, to: CGPoint) -> Self [class]](https://developer.apple.com/documentation/spritekit/skconstraint/1519688-distance)

|  | Declaration |
| --- | --- |
| From | ``` class func distance(_ range: SKRange, toPoint point: CGPoint) -> Self ``` |
| To | ``` class func distance(_ range: SKRange, to point: CGPoint) -> Self ``` |

Modified [SKConstraint.distance(_: SKRange, to: CGPoint, in: SKNode) -> Self [class]](https://developer.apple.com/documentation/spritekit/skconstraint/1519746-distance)

|  | Declaration |
| --- | --- |
| From | ``` class func distance(_ range: SKRange, toPoint point: CGPoint, inNode node: SKNode) -> Self ``` |
| To | ``` class func distance(_ range: SKRange, to point: CGPoint, in node: SKNode) -> Self ``` |

Modified [SKConstraint.orient(to: CGPoint, in: SKNode, offset: SKRange) -> Self [class]](https://developer.apple.com/documentation/spritekit/skconstraint/1519627-orient)

|  | Declaration |
| --- | --- |
| From | ``` class func orientToPoint(_ point: CGPoint, inNode node: SKNode, offset radians: SKRange) -> Self ``` |
| To | ``` class func orient(to point: CGPoint, in node: SKNode, offset radians: SKRange) -> Self ``` |

Modified [SKConstraint.orient(to: CGPoint, offset: SKRange) -> Self [class]](https://developer.apple.com/documentation/spritekit/skconstraint/1519686-orient)

|  | Declaration |
| --- | --- |
| From | ``` class func orientToPoint(_ point: CGPoint, offset radians: SKRange) -> Self ``` |
| To | ``` class func orient(to point: CGPoint, offset radians: SKRange) -> Self ``` |

Modified [SKConstraint.orient(to: SKNode, offset: SKRange) -> Self [class]](https://developer.apple.com/documentation/spritekit/skconstraint/1519744-orient)

|  | Declaration |
| --- | --- |
| From | ``` class func orientToNode(_ node: SKNode, offset radians: SKRange) -> Self ``` |
| To | ``` class func orient(to node: SKNode, offset radians: SKRange) -> Self ``` |

Modified [SKEffectNode](https://developer.apple.com/documentation/spritekit/skeffectnode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKEffectNode : SKNode {     var filter: CIFilter?     var shouldCenterFilter: Bool     var shouldEnableEffects: Bool     var shouldRasterize: Bool     var blendMode: SKBlendMode     var shader: SKShader? } ``` | -- |
| To | ``` class SKEffectNode : SKNode, SKWarpable {     var filter: CIFilter?     var shouldCenterFilter: Bool     var shouldEnableEffects: Bool     var shouldRasterize: Bool     var blendMode: SKBlendMode     var shader: SKShader? } ``` | SKWarpable |

Modified [SKEmitterNode](https://developer.apple.com/documentation/spritekit/skemitternode)

|  | Declaration |
| --- | --- |
| From | ``` class SKEmitterNode : SKNode {     func advanceSimulationTime(_ sec: NSTimeInterval)     func resetSimulation()     var particleTexture: SKTexture?     var particleBlendMode: SKBlendMode     var particleColor: UIColor     var particleColorRedRange: CGFloat     var particleColorGreenRange: CGFloat     var particleColorBlueRange: CGFloat     var particleColorAlphaRange: CGFloat     var particleColorRedSpeed: CGFloat     var particleColorGreenSpeed: CGFloat     var particleColorBlueSpeed: CGFloat     var particleColorAlphaSpeed: CGFloat     var particleColorSequence: SKKeyframeSequence?     var particleColorBlendFactor: CGFloat     var particleColorBlendFactorRange: CGFloat     var particleColorBlendFactorSpeed: CGFloat     var particleColorBlendFactorSequence: SKKeyframeSequence?     var particlePosition: CGPoint     var particlePositionRange: CGVector     var particleSpeed: CGFloat     var particleSpeedRange: CGFloat     var emissionAngle: CGFloat     var emissionAngleRange: CGFloat     var xAcceleration: CGFloat     var yAcceleration: CGFloat     var particleBirthRate: CGFloat     var numParticlesToEmit: Int     var particleLifetime: CGFloat     var particleLifetimeRange: CGFloat     var particleRotation: CGFloat     var particleRotationRange: CGFloat     var particleRotationSpeed: CGFloat     var particleSize: CGSize     var particleScale: CGFloat     var particleScaleRange: CGFloat     var particleScaleSpeed: CGFloat     var particleScaleSequence: SKKeyframeSequence?     var particleAlpha: CGFloat     var particleAlphaRange: CGFloat     var particleAlphaSpeed: CGFloat     var particleAlphaSequence: SKKeyframeSequence?     @NSCopying var particleAction: SKAction?     var fieldBitMask: UInt32     weak var targetNode: SKNode?     var shader: SKShader?     var particleZPosition: CGFloat     var particleRenderOrder: SKParticleRenderOrder     var particleZPositionRange: CGFloat     var particleZPositionSpeed: CGFloat } ``` |
| To | ``` class SKEmitterNode : SKNode {     func advanceSimulationTime(_ sec: TimeInterval)     func resetSimulation()     var particleTexture: SKTexture?     var particleBlendMode: SKBlendMode     var particleColor: UIColor     var particleColorRedRange: CGFloat     var particleColorGreenRange: CGFloat     var particleColorBlueRange: CGFloat     var particleColorAlphaRange: CGFloat     var particleColorRedSpeed: CGFloat     var particleColorGreenSpeed: CGFloat     var particleColorBlueSpeed: CGFloat     var particleColorAlphaSpeed: CGFloat     var particleColorSequence: SKKeyframeSequence?     var particleColorBlendFactor: CGFloat     var particleColorBlendFactorRange: CGFloat     var particleColorBlendFactorSpeed: CGFloat     var particleColorBlendFactorSequence: SKKeyframeSequence?     var particlePosition: CGPoint     var particlePositionRange: CGVector     var particleSpeed: CGFloat     var particleSpeedRange: CGFloat     var emissionAngle: CGFloat     var emissionAngleRange: CGFloat     var xAcceleration: CGFloat     var yAcceleration: CGFloat     var particleBirthRate: CGFloat     var numParticlesToEmit: Int     var particleLifetime: CGFloat     var particleLifetimeRange: CGFloat     var particleRotation: CGFloat     var particleRotationRange: CGFloat     var particleRotationSpeed: CGFloat     var particleSize: CGSize     var particleScale: CGFloat     var particleScaleRange: CGFloat     var particleScaleSpeed: CGFloat     var particleScaleSequence: SKKeyframeSequence?     var particleAlpha: CGFloat     var particleAlphaRange: CGFloat     var particleAlphaSpeed: CGFloat     var particleAlphaSequence: SKKeyframeSequence?     @NSCopying var particleAction: SKAction?     var fieldBitMask: UInt32     weak var targetNode: SKNode?     var shader: SKShader?     var particleZPosition: CGFloat     var particleRenderOrder: SKParticleRenderOrder     var particleZPositionRange: CGFloat     var particleZPositionSpeed: CGFloat } ``` |

Modified [SKEmitterNode.advanceSimulationTime(_: TimeInterval)](https://developer.apple.com/documentation/spritekit/skemitternode/1398027-advancesimulationtime)

|  | Declaration |
| --- | --- |
| From | ``` func advanceSimulationTime(_ sec: NSTimeInterval) ``` |
| To | ``` func advanceSimulationTime(_ sec: TimeInterval) ``` |

Modified [SKFieldNode](https://developer.apple.com/documentation/spritekit/skfieldnode)

|  | Declaration |
| --- | --- |
| From | ``` class SKFieldNode : SKNode {     var region: SKRegion?     var strength: Float     var falloff: Float     var minimumRadius: Float     var enabled: Bool     var exclusive: Bool     var categoryBitMask: UInt32     var direction: vector_float3     var smoothness: Float     var animationSpeed: Float     var texture: SKTexture?     class func dragField() -> SKFieldNode     class func vortexField() -> SKFieldNode     class func radialGravityField() -> SKFieldNode     class func linearGravityFieldWithVector(_ direction: vector_float3) -> SKFieldNode     class func velocityFieldWithVector(_ direction: vector_float3) -> SKFieldNode     class func velocityFieldWithTexture(_ velocityTexture: SKTexture) -> SKFieldNode     class func noiseFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode     class func turbulenceFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode     class func springField() -> SKFieldNode     class func electricField() -> SKFieldNode     class func magneticField() -> SKFieldNode     class func customFieldWithEvaluationBlock(_ block: SKFieldForceEvaluator) -> SKFieldNode } ``` |
| To | ``` class SKFieldNode : SKNode {     var region: SKRegion?     var strength: Float     var falloff: Float     var minimumRadius: Float     var isEnabled: Bool     var isExclusive: Bool     var categoryBitMask: UInt32     var direction: vector_float3     var smoothness: Float     var animationSpeed: Float     var texture: SKTexture?     class func dragField() -> SKFieldNode     class func vortexField() -> SKFieldNode     class func radialGravityField() -> SKFieldNode     class func linearGravityField(withVector direction: vector_float3) -> SKFieldNode     class func velocityField(withVector direction: vector_float3) -> SKFieldNode     class func velocityField(with velocityTexture: SKTexture) -> SKFieldNode     class func noiseField(withSmoothness smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode     class func turbulenceField(withSmoothness smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode     class func springField() -> SKFieldNode     class func electricField() -> SKFieldNode     class func magneticField() -> SKFieldNode     class func customField(evaluationBlock block: SpriteKit.SKFieldForceEvaluator) -> SKFieldNode } ``` |

Modified [SKFieldNode.customField(evaluationBlock: SpriteKit.SKFieldForceEvaluator) -> SKFieldNode [class]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519710-customfieldwithevaluationblock)

|  | Declaration |
| --- | --- |
| From | ``` class func customFieldWithEvaluationBlock(_ block: SKFieldForceEvaluator) -> SKFieldNode ``` |
| To | ``` class func customField(evaluationBlock block: SpriteKit.SKFieldForceEvaluator) -> SKFieldNode ``` |

Modified [SKFieldNode.isEnabled](https://developer.apple.com/documentation/spritekit/skfieldnode/1520079-enabled)

|  | Declaration |
| --- | --- |
| From | ``` var enabled: Bool ``` |
| To | ``` var isEnabled: Bool ``` |

Modified [SKFieldNode.isExclusive](https://developer.apple.com/documentation/spritekit/skfieldnode/1520365-isexclusive)

|  | Declaration |
| --- | --- |
| From | ``` var exclusive: Bool ``` |
| To | ``` var isExclusive: Bool ``` |

Modified [SKFieldNode.linearGravityField(withVector: vector_float3) -> SKFieldNode [class]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520145-lineargravityfieldwithvector)

|  | Declaration |
| --- | --- |
| From | ``` class func linearGravityFieldWithVector(_ direction: vector_float3) -> SKFieldNode ``` |
| To | ``` class func linearGravityField(withVector direction: vector_float3) -> SKFieldNode ``` |

Modified [SKFieldNode.noiseField(withSmoothness: CGFloat, animationSpeed: CGFloat) -> SKFieldNode [class]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519947-noisefield)

|  | Declaration |
| --- | --- |
| From | ``` class func noiseFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode ``` |
| To | ``` class func noiseField(withSmoothness smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode ``` |

Modified [SKFieldNode.turbulenceField(withSmoothness: CGFloat, animationSpeed: CGFloat) -> SKFieldNode [class]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520018-turbulencefield)

|  | Declaration |
| --- | --- |
| From | ``` class func turbulenceFieldWithSmoothness(_ smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode ``` |
| To | ``` class func turbulenceField(withSmoothness smoothness: CGFloat, animationSpeed speed: CGFloat) -> SKFieldNode ``` |

Modified [SKFieldNode.velocityField(with: SKTexture) -> SKFieldNode [class]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519778-velocityfield)

|  | Declaration |
| --- | --- |
| From | ``` class func velocityFieldWithTexture(_ velocityTexture: SKTexture) -> SKFieldNode ``` |
| To | ``` class func velocityField(with velocityTexture: SKTexture) -> SKFieldNode ``` |

Modified [SKFieldNode.velocityField(withVector: vector_float3) -> SKFieldNode [class]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520271-velocityfieldwithvector)

|  | Declaration |
| --- | --- |
| From | ``` class func velocityFieldWithVector(_ direction: vector_float3) -> SKFieldNode ``` |
| To | ``` class func velocityField(withVector direction: vector_float3) -> SKFieldNode ``` |

Modified [SKInterpolationMode [enum]](https://developer.apple.com/documentation/spritekit/skinterpolationmode)

|  | Declaration |
| --- | --- |
| From | ``` enum SKInterpolationMode : Int {     case Linear     case Spline     case Step } ``` |
| To | ``` enum SKInterpolationMode : Int {     case linear     case spline     case step } ``` |

Modified [SKInterpolationMode.linear](https://developer.apple.com/documentation/spritekit/skinterpolationmode/linear)

|  | Declaration |
| --- | --- |
| From | ``` case Linear ``` |
| To | ``` case linear ``` |

Modified [SKInterpolationMode.spline](https://developer.apple.com/documentation/spritekit/skinterpolationmode/skinterpolationmodespline)

|  | Declaration |
| --- | --- |
| From | ``` case Spline ``` |
| To | ``` case spline ``` |

Modified [SKInterpolationMode.step](https://developer.apple.com/documentation/spritekit/skinterpolationmode/skinterpolationmodestep)

|  | Declaration |
| --- | --- |
| From | ``` case Step ``` |
| To | ``` case step ``` |

Modified [SKKeyframeSequence](https://developer.apple.com/documentation/spritekit/skkeyframesequence)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKKeyframeSequence : NSObject, NSCoding, NSCopying {     init(keyframeValues values: [AnyObject], times times: [NSNumber])     convenience init(capacity numItems: Int)     init?(coder aDecoder: NSCoder)     func count() -> Int     func addKeyframeValue(_ value: AnyObject, time time: CGFloat)     func removeLastKeyframe()     func removeKeyframeAtIndex(_ index: Int)     func setKeyframeValue(_ value: AnyObject, forIndex index: Int)     func setKeyframeTime(_ time: CGFloat, forIndex index: Int)     func setKeyframeValue(_ value: AnyObject, time time: CGFloat, forIndex index: Int)     func getKeyframeValueForIndex(_ index: Int) -> AnyObject     func getKeyframeTimeForIndex(_ index: Int) -> CGFloat     func sampleAtTime(_ time: CGFloat) -> AnyObject?     var interpolationMode: SKInterpolationMode     var repeatMode: SKRepeatMode } ``` | NSCoding, NSCopying |
| To | ``` class SKKeyframeSequence : NSObject, NSCoding, NSCopying {     init(keyframeValues values: [Any], times times: [NSNumber])     convenience init(capacity numItems: Int)     init?(coder aDecoder: NSCoder)     func count() -> Int     func addKeyframeValue(_ value: Any, time time: CGFloat)     func removeLastKeyframe()     func removeKeyframe(at index: Int)     func setKeyframeValue(_ value: Any, for index: Int)     func setKeyframeTime(_ time: CGFloat, for index: Int)     func setKeyframeValue(_ value: Any, time time: CGFloat, for index: Int)     func getKeyframeValue(for index: Int) -> Any     func getKeyframeTime(for index: Int) -> CGFloat     func sample(atTime time: CGFloat) -> Any?     var interpolationMode: SKInterpolationMode     var repeatMode: SKRepeatMode     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKKeyframeSequence : CVarArg { } extension SKKeyframeSequence : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying |

Modified [SKKeyframeSequence.addKeyframeValue(_: Any, time: CGFloat)](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390894-addkeyframevalue)

|  | Declaration |
| --- | --- |
| From | ``` func addKeyframeValue(_ value: AnyObject, time time: CGFloat) ``` |
| To | ``` func addKeyframeValue(_ value: Any, time time: CGFloat) ``` |

Modified [SKKeyframeSequence.getKeyframeTime(for: Int) -> CGFloat](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390908-getkeyframetime)

|  | Declaration |
| --- | --- |
| From | ``` func getKeyframeTimeForIndex(_ index: Int) -> CGFloat ``` |
| To | ``` func getKeyframeTime(for index: Int) -> CGFloat ``` |

Modified [SKKeyframeSequence.getKeyframeValue(for: Int) -> Any](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390898-getkeyframevalueforindex)

|  | Declaration |
| --- | --- |
| From | ``` func getKeyframeValueForIndex(_ index: Int) -> AnyObject ``` |
| To | ``` func getKeyframeValue(for index: Int) -> Any ``` |

Modified [SKKeyframeSequence.init(keyframeValues: [Any], times: [NSNumber])](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390896-initwithkeyframevalues)

|  | Declaration |
| --- | --- |
| From | ``` init(keyframeValues values: [AnyObject], times times: [NSNumber]) ``` |
| To | ``` init(keyframeValues values: [Any], times times: [NSNumber]) ``` |

Modified [SKKeyframeSequence.removeKeyframe(at: Int)](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390920-removekeyframeatindex)

|  | Declaration |
| --- | --- |
| From | ``` func removeKeyframeAtIndex(_ index: Int) ``` |
| To | ``` func removeKeyframe(at index: Int) ``` |

Modified [SKKeyframeSequence.sample(atTime: CGFloat) -> Any?](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390904-sample)

|  | Declaration |
| --- | --- |
| From | ``` func sampleAtTime(_ time: CGFloat) -> AnyObject? ``` |
| To | ``` func sample(atTime time: CGFloat) -> Any? ``` |

Modified [SKKeyframeSequence.setKeyframeTime(_: CGFloat, for: Int)](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390924-setkeyframetime)

|  | Declaration |
| --- | --- |
| From | ``` func setKeyframeTime(_ time: CGFloat, forIndex index: Int) ``` |
| To | ``` func setKeyframeTime(_ time: CGFloat, for index: Int) ``` |

Modified [SKKeyframeSequence.setKeyframeValue(_: Any, for: Int)](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390883-setkeyframevalue)

|  | Declaration |
| --- | --- |
| From | ``` func setKeyframeValue(_ value: AnyObject, forIndex index: Int) ``` |
| To | ``` func setKeyframeValue(_ value: Any, for index: Int) ``` |

Modified [SKKeyframeSequence.setKeyframeValue(_: Any, time: CGFloat, for: Int)](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390890-setkeyframevalue)

|  | Declaration |
| --- | --- |
| From | ``` func setKeyframeValue(_ value: AnyObject, time time: CGFloat, forIndex index: Int) ``` |
| To | ``` func setKeyframeValue(_ value: Any, time time: CGFloat, for index: Int) ``` |

Modified [SKLabelHorizontalAlignmentMode [enum]](https://developer.apple.com/documentation/spritekit/sklabelhorizontalalignmentmode)

|  | Declaration |
| --- | --- |
| From | ``` enum SKLabelHorizontalAlignmentMode : Int {     case Center     case Left     case Right } ``` |
| To | ``` enum SKLabelHorizontalAlignmentMode : Int {     case center     case left     case right } ``` |

Modified [SKLabelHorizontalAlignmentMode.center](https://developer.apple.com/documentation/spritekit/sklabelhorizontalalignmentmode/sklabelhorizontalalignmentmodecenter)

|  | Declaration |
| --- | --- |
| From | ``` case Center ``` |
| To | ``` case center ``` |

Modified [SKLabelHorizontalAlignmentMode.left](https://developer.apple.com/documentation/spritekit/sklabelhorizontalalignmentmode/sklabelhorizontalalignmentmodeleft)

|  | Declaration |
| --- | --- |
| From | ``` case Left ``` |
| To | ``` case left ``` |

Modified [SKLabelHorizontalAlignmentMode.right](https://developer.apple.com/documentation/spritekit/sklabelhorizontalalignmentmode/sklabelhorizontalalignmentmoderight)

|  | Declaration |
| --- | --- |
| From | ``` case Right ``` |
| To | ``` case right ``` |

Modified [SKLabelNode](https://developer.apple.com/documentation/spritekit/sklabelnode)

|  | Declaration |
| --- | --- |
| From | ``` class SKLabelNode : SKNode {     convenience init(text text: String?)     class func labelNodeWithText(_ text: String?) -> Self     convenience init(fontNamed fontName: String?)     class func labelNodeWithFontNamed(_ fontName: String?) -> Self     init(fontNamed fontName: String?)     var verticalAlignmentMode: SKLabelVerticalAlignmentMode     var horizontalAlignmentMode: SKLabelHorizontalAlignmentMode     var fontName: String?     var text: String?     var fontSize: CGFloat     var fontColor: UIColor?     var colorBlendFactor: CGFloat     var color: UIColor?     var blendMode: SKBlendMode } ``` |
| To | ``` class SKLabelNode : SKNode {     convenience init(text text: String?)     class func withText(_ text: String?) -> Self     convenience init(fontNamed fontName: String?)     class func withFontNamed(_ fontName: String?) -> Self     init(fontNamed fontName: String?)     var verticalAlignmentMode: SKLabelVerticalAlignmentMode     var horizontalAlignmentMode: SKLabelHorizontalAlignmentMode     var fontName: String?     var text: String?     var fontSize: CGFloat     var fontColor: UIColor?     var colorBlendFactor: CGFloat     var color: UIColor?     var blendMode: SKBlendMode } ``` |

Modified [SKLabelVerticalAlignmentMode [enum]](https://developer.apple.com/documentation/spritekit/sklabelverticalalignmentmode)

|  | Declaration |
| --- | --- |
| From | ``` enum SKLabelVerticalAlignmentMode : Int {     case Baseline     case Center     case Top     case Bottom } ``` |
| To | ``` enum SKLabelVerticalAlignmentMode : Int {     case baseline     case center     case top     case bottom } ``` |

Modified [SKLabelVerticalAlignmentMode.baseline](https://developer.apple.com/documentation/spritekit/sklabelverticalalignmentmode/sklabelverticalalignmentmodebaseline)

|  | Declaration |
| --- | --- |
| From | ``` case Baseline ``` |
| To | ``` case baseline ``` |

Modified [SKLabelVerticalAlignmentMode.bottom](https://developer.apple.com/documentation/spritekit/sklabelverticalalignmentmode/bottom)

|  | Declaration |
| --- | --- |
| From | ``` case Bottom ``` |
| To | ``` case bottom ``` |

Modified [SKLabelVerticalAlignmentMode.center](https://developer.apple.com/documentation/spritekit/sklabelverticalalignmentmode/center)

|  | Declaration |
| --- | --- |
| From | ``` case Center ``` |
| To | ``` case center ``` |

Modified [SKLabelVerticalAlignmentMode.top](https://developer.apple.com/documentation/spritekit/sklabelverticalalignmentmode/sklabelverticalalignmentmodetop)

|  | Declaration |
| --- | --- |
| From | ``` case Top ``` |
| To | ``` case top ``` |

Modified [SKLightNode](https://developer.apple.com/documentation/spritekit/sklightnode)

|  | Declaration |
| --- | --- |
| From | ``` class SKLightNode : SKNode {     var enabled: Bool     var lightColor: UIColor     var ambientColor: UIColor     var shadowColor: UIColor     var falloff: CGFloat     var categoryBitMask: UInt32 } ``` |
| To | ``` class SKLightNode : SKNode {     var isEnabled: Bool     var lightColor: UIColor     var ambientColor: UIColor     var shadowColor: UIColor     var falloff: CGFloat     var categoryBitMask: UInt32 } ``` |

Modified [SKLightNode.isEnabled](https://developer.apple.com/documentation/spritekit/sklightnode/1519826-isenabled)

|  | Declaration |
| --- | --- |
| From | ``` var enabled: Bool ``` |
| To | ``` var isEnabled: Bool ``` |

Modified [SKMutableTexture](https://developer.apple.com/documentation/spritekit/skmutabletexture)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKMutableTexture : SKTexture {     init(size size: CGSize)     class func mutableTextureWithSize(_ size: CGSize) -> Self     init(size size: CGSize, pixelFormat format: Int32)     func modifyPixelDataWithBlock(_ block: (UnsafeMutablePointer<Void>, Int) -> Void) } ``` | -- |
| To | ``` class SKMutableTexture : SKTexture {     init(size size: CGSize)     class func withSize(_ size: CGSize) -> Self     init(size size: CGSize, pixelFormat format: Int32)     func modifyPixelData(_ block: @escaping (UnsafeMutableRawPointer?, Int) -> Swift.Void)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKMutableTexture : CustomPlaygroundQuickLookable {     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } extension SKMutableTexture : CVarArg { } extension SKMutableTexture : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, CustomPlaygroundQuickLookable, Equatable, Hashable |

Modified [SKMutableTexture.modifyPixelData(_: (UnsafeMutableRawPointer?, Int) -> Swift.Void)](https://developer.apple.com/documentation/spritekit/skmutabletexture/1397881-modifypixeldata)

|  | Declaration |
| --- | --- |
| From | ``` func modifyPixelDataWithBlock(_ block: (UnsafeMutablePointer<Void>, Int) -> Void) ``` |
| To | ``` func modifyPixelData(_ block: @escaping (UnsafeMutableRawPointer?, Int) -> Swift.Void) ``` |

Modified [SKNode](https://developer.apple.com/documentation/spritekit/sknode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKNode : UIResponder, NSCopying, NSCoding {     init()     init?(coder aDecoder: NSCoder)     class func node() -> Self     convenience init?(fileNamed filename: String)     class func nodeWithFileNamed(_ filename: String) -> Self?     var frame: CGRect { get }     func calculateAccumulatedFrame() -> CGRect     var position: CGPoint     var zPosition: CGFloat     var zRotation: CGFloat     var xScale: CGFloat     var yScale: CGFloat     var speed: CGFloat     var alpha: CGFloat     var paused: Bool     var hidden: Bool     var userInteractionEnabled: Bool     var parent: SKNode? { get }     var children: [SKNode] { get }     var name: String?     var scene: SKScene? { get }     var physicsBody: SKPhysicsBody?     var userData: NSMutableDictionary?     @NSCopying var reachConstraints: SKReachConstraints?     var constraints: [SKConstraint]?     func setScale(_ scale: CGFloat)     func addChild(_ node: SKNode)     func insertChild(_ node: SKNode, atIndex index: Int)     func removeChildrenInArray(_ nodes: [SKNode])     func removeAllChildren()     func removeFromParent()     func moveToParent(_ parent: SKNode)     func childNodeWithName(_ name: String) -> SKNode?     func enumerateChildNodesWithName(_ name: String, usingBlock block: (SKNode, UnsafeMutablePointer<ObjCBool>) -> Void)     subscript (_ name: String) -> [SKNode] { get }     func objectForKeyedSubscript(_ name: String) -> [SKNode]     func inParentHierarchy(_ parent: SKNode) -> Bool     func runAction(_ action: SKAction)     func runAction(_ action: SKAction, completion block: () -> Void)     func runAction(_ action: SKAction, withKey key: String)     func hasActions() -> Bool     func actionForKey(_ key: String) -> SKAction?     func removeActionForKey(_ key: String)     func removeAllActions()     func containsPoint(_ p: CGPoint) -> Bool     func nodeAtPoint(_ p: CGPoint) -> SKNode     func nodesAtPoint(_ p: CGPoint) -> [SKNode]     func convertPoint(_ point: CGPoint, fromNode node: SKNode) -> CGPoint     func convertPoint(_ point: CGPoint, toNode node: SKNode) -> CGPoint     func intersectsNode(_ node: SKNode) -> Bool     func isEqualToNode(_ node: SKNode) -> Bool     class func obstaclesFromSpriteTextures(_ sprites: [SKNode], accuracy accuracy: Float) -> [GKPolygonObstacle]     class func obstaclesFromNodeBounds(_ nodes: [SKNode]) -> [GKPolygonObstacle]     class func obstaclesFromNodePhysicsBodies(_ nodes: [SKNode]) -> [GKPolygonObstacle] } ``` | NSCoding, NSCopying |
| To | ``` class SKNode : UIResponder, NSCopying, NSCoding, UIFocusItem {     init()     init?(coder aDecoder: NSCoder)     class func node() -> Self     convenience init?(fileNamed filename: String)     class func withFileNamed(_ filename: String) -> Self?     var frame: CGRect { get }     func calculateAccumulatedFrame() -> CGRect     var position: CGPoint     var zPosition: CGFloat     var zRotation: CGFloat     var xScale: CGFloat     var yScale: CGFloat     var speed: CGFloat     var alpha: CGFloat     var isPaused: Bool     var isHidden: Bool     var isUserInteractionEnabled: Bool     var parent: SKNode? { get }     var children: [SKNode] { get }     var name: String?     var scene: SKScene? { get }     var physicsBody: SKPhysicsBody?     var userData: NSMutableDictionary?     @NSCopying var reachConstraints: SKReachConstraints?     var constraints: [SKConstraint]?     var attributeValues: [String : SKAttributeValue]     func value(forAttributeNamed key: String) -> SKAttributeValue?     func setValue(_ value: SKAttributeValue, forAttribute key: String)     func setScale(_ scale: CGFloat)     func addChild(_ node: SKNode)     func insertChild(_ node: SKNode, at index: Int)     func removeChildren(in nodes: [SKNode])     func removeAllChildren()     func removeFromParent()     func move(toParent parent: SKNode)     func childNode(withName name: String) -> SKNode?     func enumerateChildNodes(withName name: String, using block: @escaping (SKNode, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)     subscript(_ name: String) -> [SKNode] { get }     func objectForKeyedSubscript(_ name: String) -> [SKNode]     func inParentHierarchy(_ parent: SKNode) -> Bool     func run(_ action: SKAction)     func run(_ action: SKAction, completion block: @escaping () -> Swift.Void)     func run(_ action: SKAction, withKey key: String)     func hasActions() -> Bool     func action(forKey key: String) -> SKAction?     func removeAction(forKey key: String)     func removeAllActions()     func contains(_ p: CGPoint) -> Bool     func atPoint(_ p: CGPoint) -> SKNode     func nodes(at p: CGPoint) -> [SKNode]     func convert(_ point: CGPoint, from node: SKNode) -> CGPoint     func convert(_ point: CGPoint, to node: SKNode) -> CGPoint     func intersects(_ node: SKNode) -> Bool     func isEqual(to node: SKNode) -> Bool     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity)     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews()     var keyCommands: [UIKeyCommand]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKNode {     class func obstacles(fromSpriteTextures sprites: [SKNode], accuracy accuracy: Float) -> [GKPolygonObstacle]     class func obstacles(fromNodeBounds nodes: [SKNode]) -> [GKPolygonObstacle]     class func obstacles(fromNodePhysicsBodies nodes: [SKNode]) -> [GKPolygonObstacle]     weak var entity: GKEntity? } extension SKNode : CVarArg { } extension SKNode : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying, UIFocusItem |

Modified [SKNode.action(forKey: String) -> SKAction?](https://developer.apple.com/documentation/spritekit/sknode/1483138-action)

|  | Declaration |
| --- | --- |
| From | ``` func actionForKey(_ key: String) -> SKAction? ``` |
| To | ``` func action(forKey key: String) -> SKAction? ``` |

Modified [SKNode.atPoint(_: CGPoint) -> SKNode](https://developer.apple.com/documentation/spritekit/sknode/1483099-atpoint)

|  | Declaration |
| --- | --- |
| From | ``` func nodeAtPoint(_ p: CGPoint) -> SKNode ``` |
| To | ``` func atPoint(_ p: CGPoint) -> SKNode ``` |

Modified [SKNode.childNode(withName: String) -> SKNode?](https://developer.apple.com/documentation/spritekit/sknode/1483060-childnodewithname)

|  | Declaration |
| --- | --- |
| From | ``` func childNodeWithName(_ name: String) -> SKNode? ``` |
| To | ``` func childNode(withName name: String) -> SKNode? ``` |

Modified [SKNode.contains(_: CGPoint) -> Bool](https://developer.apple.com/documentation/spritekit/sknode/1483044-containspoint)

|  | Declaration |
| --- | --- |
| From | ``` func containsPoint(_ p: CGPoint) -> Bool ``` |
| To | ``` func contains(_ p: CGPoint) -> Bool ``` |

Modified [SKNode.convert(_: CGPoint, from: SKNode) -> CGPoint](https://developer.apple.com/documentation/spritekit/sknode/1483058-convert)

|  | Declaration |
| --- | --- |
| From | ``` func convertPoint(_ point: CGPoint, fromNode node: SKNode) -> CGPoint ``` |
| To | ``` func convert(_ point: CGPoint, from node: SKNode) -> CGPoint ``` |

Modified [SKNode.convert(_: CGPoint, to: SKNode) -> CGPoint](https://developer.apple.com/documentation/spritekit/sknode/1483056-convert)

|  | Declaration |
| --- | --- |
| From | ``` func convertPoint(_ point: CGPoint, toNode node: SKNode) -> CGPoint ``` |
| To | ``` func convert(_ point: CGPoint, to node: SKNode) -> CGPoint ``` |

Modified [SKNode.enumerateChildNodes(withName: String, using: (SKNode, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)](https://developer.apple.com/documentation/spritekit/sknode/1483024-enumeratechildnodeswithname)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateChildNodesWithName(_ name: String, usingBlock block: (SKNode, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateChildNodes(withName name: String, using block: @escaping (SKNode, UnsafeMutablePointer<ObjCBool>) -> Swift.Void) ``` |

Modified [SKNode.insertChild(_: SKNode, at: Int)](https://developer.apple.com/documentation/spritekit/sknode/1483062-insertchild)

|  | Declaration |
| --- | --- |
| From | ``` func insertChild(_ node: SKNode, atIndex index: Int) ``` |
| To | ``` func insertChild(_ node: SKNode, at index: Int) ``` |

Modified [SKNode.intersects(_: SKNode) -> Bool](https://developer.apple.com/documentation/spritekit/sknode/1483140-intersectsnode)

|  | Declaration |
| --- | --- |
| From | ``` func intersectsNode(_ node: SKNode) -> Bool ``` |
| To | ``` func intersects(_ node: SKNode) -> Bool ``` |

Modified [SKNode.isEqual(to: SKNode) -> Bool](https://developer.apple.com/documentation/spritekit/sknode/1483078-isequaltonode)

|  | Declaration |
| --- | --- |
| From | ``` func isEqualToNode(_ node: SKNode) -> Bool ``` |
| To | ``` func isEqual(to node: SKNode) -> Bool ``` |

Modified [SKNode.isHidden](https://developer.apple.com/documentation/spritekit/sknode/1483048-hidden)

|  | Declaration |
| --- | --- |
| From | ``` var hidden: Bool ``` |
| To | ``` var isHidden: Bool ``` |

Modified [SKNode.isPaused](https://developer.apple.com/documentation/spritekit/sknode/1483113-ispaused)

|  | Declaration |
| --- | --- |
| From | ``` var paused: Bool ``` |
| To | ``` var isPaused: Bool ``` |

Modified [SKNode.isUserInteractionEnabled](https://developer.apple.com/documentation/spritekit/sknode/1483109-isuserinteractionenabled)

|  | Declaration |
| --- | --- |
| From | ``` var userInteractionEnabled: Bool ``` |
| To | ``` var isUserInteractionEnabled: Bool ``` |

Modified [SKNode.move(toParent: SKNode)](https://developer.apple.com/documentation/spritekit/sknode/1483021-move)

|  | Declaration |
| --- | --- |
| From | ``` func moveToParent(_ parent: SKNode) ``` |
| To | ``` func move(toParent parent: SKNode) ``` |

Modified [SKNode.nodes(at: CGPoint) -> [SKNode]](https://developer.apple.com/documentation/spritekit/sknode/1483072-nodes)

|  | Declaration |
| --- | --- |
| From | ``` func nodesAtPoint(_ p: CGPoint) -> [SKNode] ``` |
| To | ``` func nodes(at p: CGPoint) -> [SKNode] ``` |

Modified [SKNode.obstacles(fromNodeBounds: [SKNode]) -> [GKPolygonObstacle] [class]](https://developer.apple.com/documentation/spritekit/sknode/1483132-obstacles)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func obstaclesFromNodeBounds(_ nodes: [SKNode]) -> [GKPolygonObstacle] ``` | SpriteKit |
| To | ``` class func obstacles(fromNodeBounds nodes: [SKNode]) -> [GKPolygonObstacle] ``` | GameplayKit |

Modified [SKNode.obstacles(fromNodePhysicsBodies: [SKNode]) -> [GKPolygonObstacle] [class]](https://developer.apple.com/documentation/spritekit/sknode/1483085-obstacles)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func obstaclesFromNodePhysicsBodies(_ nodes: [SKNode]) -> [GKPolygonObstacle] ``` | SpriteKit |
| To | ``` class func obstacles(fromNodePhysicsBodies nodes: [SKNode]) -> [GKPolygonObstacle] ``` | GameplayKit |

Modified [SKNode.obstacles(fromSpriteTextures: [SKNode], accuracy: Float) -> [GKPolygonObstacle] [class]](https://developer.apple.com/documentation/spritekit/sknode/1483134-obstacles)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func obstaclesFromSpriteTextures(_ sprites: [SKNode], accuracy accuracy: Float) -> [GKPolygonObstacle] ``` | SpriteKit |
| To | ``` class func obstacles(fromSpriteTextures sprites: [SKNode], accuracy accuracy: Float) -> [GKPolygonObstacle] ``` | GameplayKit |

Modified [SKNode.removeAction(forKey: String)](https://developer.apple.com/documentation/spritekit/sknode/1483076-removeaction)

|  | Declaration |
| --- | --- |
| From | ``` func removeActionForKey(_ key: String) ``` |
| To | ``` func removeAction(forKey key: String) ``` |

Modified [SKNode.removeChildren(in: [SKNode])](https://developer.apple.com/documentation/spritekit/sknode/1483091-removechildren)

|  | Declaration |
| --- | --- |
| From | ``` func removeChildrenInArray(_ nodes: [SKNode]) ``` |
| To | ``` func removeChildren(in nodes: [SKNode]) ``` |

Modified [SKNode.run(_: SKAction)](https://developer.apple.com/documentation/spritekit/sknode/1483093-runaction)

|  | Declaration |
| --- | --- |
| From | ``` func runAction(_ action: SKAction) ``` |
| To | ``` func run(_ action: SKAction) ``` |

Modified [SKNode.run(_: SKAction, completion: () -> Swift.Void)](https://developer.apple.com/documentation/spritekit/sknode/1483103-run)

|  | Declaration |
| --- | --- |
| From | ``` func runAction(_ action: SKAction, completion block: () -> Void) ``` |
| To | ``` func run(_ action: SKAction, completion block: @escaping () -> Swift.Void) ``` |

Modified [SKNode.run(_: SKAction, withKey: String)](https://developer.apple.com/documentation/spritekit/sknode/1483042-run)

|  | Declaration |
| --- | --- |
| From | ``` func runAction(_ action: SKAction, withKey key: String) ``` |
| To | ``` func run(_ action: SKAction, withKey key: String) ``` |

Modified [SKNode.subscript(_: String) -> [SKNode]](https://developer.apple.com/documentation/spritekit/sknode/1483070-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ name: String) -> [SKNode] { get } ``` |
| To | ``` subscript(_ name: String) -> [SKNode] { get } ``` |

Modified [SKParticleRenderOrder [enum]](https://developer.apple.com/documentation/spritekit/skparticlerenderorder)

|  | Declaration |
| --- | --- |
| From | ``` enum SKParticleRenderOrder : UInt {     case OldestLast     case OldestFirst     case DontCare } ``` |
| To | ``` enum SKParticleRenderOrder : UInt {     case oldestLast     case oldestFirst     case dontCare } ``` |

Modified [SKParticleRenderOrder.dontCare](https://developer.apple.com/documentation/spritekit/skparticlerenderorder/skparticlerenderorderdontcare)

|  | Declaration |
| --- | --- |
| From | ``` case DontCare ``` |
| To | ``` case dontCare ``` |

Modified [SKParticleRenderOrder.oldestFirst](https://developer.apple.com/documentation/spritekit/skparticlerenderorder/oldestfirst)

|  | Declaration |
| --- | --- |
| From | ``` case OldestFirst ``` |
| To | ``` case oldestFirst ``` |

Modified [SKParticleRenderOrder.oldestLast](https://developer.apple.com/documentation/spritekit/skparticlerenderorder/oldestlast)

|  | Declaration |
| --- | --- |
| From | ``` case OldestLast ``` |
| To | ``` case oldestLast ``` |

Modified [SKPhysicsBody](https://developer.apple.com/documentation/spritekit/skphysicsbody)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKPhysicsBody : NSObject, NSCopying, NSCoding {      init(circleOfRadius r: CGFloat)     class func bodyWithCircleOfRadius(_ r: CGFloat) -> SKPhysicsBody      init(circleOfRadius r: CGFloat, center center: CGPoint)     class func bodyWithCircleOfRadius(_ r: CGFloat, center center: CGPoint) -> SKPhysicsBody      init(rectangleOfSize s: CGSize)     class func bodyWithRectangleOfSize(_ s: CGSize) -> SKPhysicsBody      init(rectangleOfSize s: CGSize, center center: CGPoint)     class func bodyWithRectangleOfSize(_ s: CGSize, center center: CGPoint) -> SKPhysicsBody      init(polygonFromPath path: CGPath)     class func bodyWithPolygonFromPath(_ path: CGPath) -> SKPhysicsBody      init(edgeFromPoint p1: CGPoint, toPoint p2: CGPoint)     class func bodyWithEdgeFromPoint(_ p1: CGPoint, toPoint p2: CGPoint) -> SKPhysicsBody      init(edgeChainFromPath path: CGPath)     class func bodyWithEdgeChainFromPath(_ path: CGPath) -> SKPhysicsBody      init(edgeLoopFromPath path: CGPath)     class func bodyWithEdgeLoopFromPath(_ path: CGPath) -> SKPhysicsBody      init(edgeLoopFromRect rect: CGRect)     class func bodyWithEdgeLoopFromRect(_ rect: CGRect) -> SKPhysicsBody      init(texture texture: SKTexture, size size: CGSize)     class func bodyWithTexture(_ texture: SKTexture, size size: CGSize) -> SKPhysicsBody      init(texture texture: SKTexture, alphaThreshold alphaThreshold: Float, size size: CGSize)     class func bodyWithTexture(_ texture: SKTexture, alphaThreshold alphaThreshold: Float, size size: CGSize) -> SKPhysicsBody      init(bodies bodies: [SKPhysicsBody])     class func bodyWithBodies(_ bodies: [SKPhysicsBody]) -> SKPhysicsBody     var dynamic: Bool     var usesPreciseCollisionDetection: Bool     var allowsRotation: Bool     var pinned: Bool     var resting: Bool     var friction: CGFloat     var charge: CGFloat     var restitution: CGFloat     var linearDamping: CGFloat     var angularDamping: CGFloat     var density: CGFloat     var mass: CGFloat     var area: CGFloat { get }     var affectedByGravity: Bool     var fieldBitMask: UInt32     var categoryBitMask: UInt32     var collisionBitMask: UInt32     var contactTestBitMask: UInt32     var joints: [SKPhysicsJoint] { get }     weak var node: SKNode? { get }     var velocity: CGVector     var angularVelocity: CGFloat     func applyForce(_ force: CGVector)     func applyForce(_ force: CGVector, atPoint point: CGPoint)     func applyTorque(_ torque: CGFloat)     func applyImpulse(_ impulse: CGVector)     func applyImpulse(_ impulse: CGVector, atPoint point: CGPoint)     func applyAngularImpulse(_ impulse: CGFloat)     func allContactedBodies() -> [SKPhysicsBody] } ``` | NSCoding, NSCopying |
| To | ``` class SKPhysicsBody : NSObject, NSCopying, NSCoding {      init(circleOfRadius r: CGFloat)     class func withCircleOfRadius(_ r: CGFloat) -> SKPhysicsBody      init(circleOfRadius r: CGFloat, center center: CGPoint)     class func withCircleOfRadius(_ r: CGFloat, center center: CGPoint) -> SKPhysicsBody      init(rectangleOf s: CGSize)     class func withRectangleOf(_ s: CGSize) -> SKPhysicsBody      init(rectangleOf s: CGSize, center center: CGPoint)     class func withRectangleOf(_ s: CGSize, center center: CGPoint) -> SKPhysicsBody      init(polygonFrom path: CGPath)     class func withPolygonFrom(_ path: CGPath) -> SKPhysicsBody      init(edgeFrom p1: CGPoint, to p2: CGPoint)     class func withEdgeFrom(_ p1: CGPoint, to p2: CGPoint) -> SKPhysicsBody      init(edgeChainFrom path: CGPath)     class func withEdgeChain(from path: CGPath) -> SKPhysicsBody      init(edgeLoopFrom path: CGPath)     class func withEdgeLoop(from path: CGPath) -> SKPhysicsBody      init(edgeLoopFrom rect: CGRect)     class func withEdgeLoop(from rect: CGRect) -> SKPhysicsBody      init(texture texture: SKTexture, size size: CGSize)     class func withTexture(_ texture: SKTexture, size size: CGSize) -> SKPhysicsBody      init(texture texture: SKTexture, alphaThreshold alphaThreshold: Float, size size: CGSize)     class func withTexture(_ texture: SKTexture, alphaThreshold alphaThreshold: Float, size size: CGSize) -> SKPhysicsBody      init(bodies bodies: [SKPhysicsBody])     class func withBodies(_ bodies: [SKPhysicsBody]) -> SKPhysicsBody     var isDynamic: Bool     var usesPreciseCollisionDetection: Bool     var allowsRotation: Bool     var pinned: Bool     var isResting: Bool     var friction: CGFloat     var charge: CGFloat     var restitution: CGFloat     var linearDamping: CGFloat     var angularDamping: CGFloat     var density: CGFloat     var mass: CGFloat     var area: CGFloat { get }     var affectedByGravity: Bool     var fieldBitMask: UInt32     var categoryBitMask: UInt32     var collisionBitMask: UInt32     var contactTestBitMask: UInt32     var joints: [SKPhysicsJoint] { get }     weak var node: SKNode? { get }     var velocity: CGVector     var angularVelocity: CGFloat     func applyForce(_ force: CGVector)     func applyForce(_ force: CGVector, at point: CGPoint)     func applyTorque(_ torque: CGFloat)     func applyImpulse(_ impulse: CGVector)     func applyImpulse(_ impulse: CGVector, at point: CGPoint)     func applyAngularImpulse(_ impulse: CGFloat)     func allContactedBodies() -> [SKPhysicsBody]     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKPhysicsBody : CVarArg { } extension SKPhysicsBody : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying |

Modified [SKPhysicsBody.applyForce(_: CGVector, at: CGPoint)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520032-applyforce)

|  | Declaration |
| --- | --- |
| From | ``` func applyForce(_ force: CGVector, atPoint point: CGPoint) ``` |
| To | ``` func applyForce(_ force: CGVector, at point: CGPoint) ``` |

Modified [SKPhysicsBody.applyImpulse(_: CGVector, at: CGPoint)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520407-applyimpulse)

|  | Declaration |
| --- | --- |
| From | ``` func applyImpulse(_ impulse: CGVector, atPoint point: CGPoint) ``` |
| To | ``` func applyImpulse(_ impulse: CGVector, at point: CGPoint) ``` |

Modified [SKPhysicsBody.init(edgeChainFrom: CGPath)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519871-bodywithedgechainfrompath)

|  | Declaration |
| --- | --- |
| From | ``` init(edgeChainFromPath path: CGPath) ``` |
| To | ``` init(edgeChainFrom path: CGPath) ``` |

Modified [SKPhysicsBody.init(edgeFrom: CGPoint, to: CGPoint)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520401-bodywithedgefrompoint)

|  | Declaration |
| --- | --- |
| From | ``` init(edgeFromPoint p1: CGPoint, toPoint p2: CGPoint) ``` |
| To | ``` init(edgeFrom p1: CGPoint, to p2: CGPoint) ``` |

Modified [SKPhysicsBody.init(edgeLoopFrom: CGPath)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519732-bodywithedgeloopfrompath)

|  | Declaration |
| --- | --- |
| From | ``` init(edgeLoopFromPath path: CGPath) ``` |
| To | ``` init(edgeLoopFrom path: CGPath) ``` |

Modified [SKPhysicsBody.init(edgeLoopFrom: CGRect)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520055-bodywithedgeloopfromrect)

|  | Declaration |
| --- | --- |
| From | ``` init(edgeLoopFromRect rect: CGRect) ``` |
| To | ``` init(edgeLoopFrom rect: CGRect) ``` |

Modified [SKPhysicsBody.init(polygonFrom: CGPath)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520379-init)

|  | Declaration |
| --- | --- |
| From | ``` init(polygonFromPath path: CGPath) ``` |
| To | ``` init(polygonFrom path: CGPath) ``` |

Modified [SKPhysicsBody.init(rectangleOf: CGSize)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520295-bodywithrectangleofsize)

|  | Declaration |
| --- | --- |
| From | ``` init(rectangleOfSize s: CGSize) ``` |
| To | ``` init(rectangleOf s: CGSize) ``` |

Modified [SKPhysicsBody.init(rectangleOf: CGSize, center: CGPoint)](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519936-bodywithrectangleofsize)

|  | Declaration |
| --- | --- |
| From | ``` init(rectangleOfSize s: CGSize, center center: CGPoint) ``` |
| To | ``` init(rectangleOf s: CGSize, center center: CGPoint) ``` |

Modified [SKPhysicsBody.isDynamic](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520132-isdynamic)

|  | Declaration |
| --- | --- |
| From | ``` var dynamic: Bool ``` |
| To | ``` var isDynamic: Bool ``` |

Modified [SKPhysicsBody.isResting](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520256-isresting)

|  | Declaration |
| --- | --- |
| From | ``` var resting: Bool ``` |
| To | ``` var isResting: Bool ``` |

Modified [SKPhysicsContact](https://developer.apple.com/documentation/spritekit/skphysicscontact)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKPhysicsContact : NSObject {     var bodyA: SKPhysicsBody { get }     var bodyB: SKPhysicsBody { get }     var contactPoint: CGPoint { get }     var contactNormal: CGVector { get }     var collisionImpulse: CGFloat { get } } ``` | -- |
| To | ``` class SKPhysicsContact : NSObject {     var bodyA: SKPhysicsBody { get }     var bodyB: SKPhysicsBody { get }     var contactPoint: CGPoint { get }     var contactNormal: CGVector { get }     var collisionImpulse: CGFloat { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKPhysicsContact : CVarArg { } extension SKPhysicsContact : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [SKPhysicsContactDelegate](https://developer.apple.com/documentation/spritekit/skphysicscontactdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol SKPhysicsContactDelegate : NSObjectProtocol {     optional func didBeginContact(_ contact: SKPhysicsContact)     optional func didEndContact(_ contact: SKPhysicsContact) } ``` |
| To | ``` protocol SKPhysicsContactDelegate : NSObjectProtocol {     optional func didBegin(_ contact: SKPhysicsContact)     optional func didEnd(_ contact: SKPhysicsContact) } ``` |

Modified [SKPhysicsContactDelegate.didBegin(_: SKPhysicsContact)](https://developer.apple.com/documentation/spritekit/skphysicscontactdelegate/1449595-didbegincontact)

|  | Declaration |
| --- | --- |
| From | ``` optional func didBeginContact(_ contact: SKPhysicsContact) ``` |
| To | ``` optional func didBegin(_ contact: SKPhysicsContact) ``` |

Modified [SKPhysicsContactDelegate.didEnd(_: SKPhysicsContact)](https://developer.apple.com/documentation/spritekit/skphysicscontactdelegate/1449599-didend)

|  | Declaration |
| --- | --- |
| From | ``` optional func didEndContact(_ contact: SKPhysicsContact) ``` |
| To | ``` optional func didEnd(_ contact: SKPhysicsContact) ``` |

Modified [SKPhysicsJoint](https://developer.apple.com/documentation/spritekit/skphysicsjoint)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKPhysicsJoint : NSObject, NSCoding {     var bodyA: SKPhysicsBody     var bodyB: SKPhysicsBody     var reactionForce: CGVector { get }     var reactionTorque: CGFloat { get } } ``` | NSCoding |
| To | ``` class SKPhysicsJoint : NSObject, NSCoding {     var bodyA: SKPhysicsBody     var bodyB: SKPhysicsBody     var reactionForce: CGVector { get }     var reactionTorque: CGFloat { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKPhysicsJoint : CVarArg { } extension SKPhysicsJoint : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding |

Modified [SKPhysicsJointFixed](https://developer.apple.com/documentation/spritekit/skphysicsjointfixed)

|  | Declaration |
| --- | --- |
| From | ``` class SKPhysicsJointFixed : SKPhysicsJoint {     class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint) -> SKPhysicsJointFixed } ``` |
| To | ``` class SKPhysicsJointFixed : SKPhysicsJoint {     class func joint(withBodyA bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint) -> SKPhysicsJointFixed } ``` |

Modified [SKPhysicsJointFixed.joint(withBodyA: SKPhysicsBody, bodyB: SKPhysicsBody, anchor: CGPoint) -> SKPhysicsJointFixed [class]](https://developer.apple.com/documentation/spritekit/skphysicsjointfixed/1520076-jointwithbodya)

|  | Declaration |
| --- | --- |
| From | ``` class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint) -> SKPhysicsJointFixed ``` |
| To | ``` class func joint(withBodyA bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint) -> SKPhysicsJointFixed ``` |

Modified [SKPhysicsJointLimit](https://developer.apple.com/documentation/spritekit/skphysicsjointlimit)

|  | Declaration |
| --- | --- |
| From | ``` class SKPhysicsJointLimit : SKPhysicsJoint {     var maxLength: CGFloat     class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointLimit } ``` |
| To | ``` class SKPhysicsJointLimit : SKPhysicsJoint {     var maxLength: CGFloat     class func joint(withBodyA bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointLimit } ``` |

Modified [SKPhysicsJointLimit.joint(withBodyA: SKPhysicsBody, bodyB: SKPhysicsBody, anchorA: CGPoint, anchorB: CGPoint) -> SKPhysicsJointLimit [class]](https://developer.apple.com/documentation/spritekit/skphysicsjointlimit/1520402-jointwithbodya)

|  | Declaration |
| --- | --- |
| From | ``` class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointLimit ``` |
| To | ``` class func joint(withBodyA bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointLimit ``` |

Modified [SKPhysicsJointPin](https://developer.apple.com/documentation/spritekit/skphysicsjointpin)

|  | Declaration |
| --- | --- |
| From | ``` class SKPhysicsJointPin : SKPhysicsJoint {     class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint) -> SKPhysicsJointPin     var shouldEnableLimits: Bool     var lowerAngleLimit: CGFloat     var upperAngleLimit: CGFloat     var frictionTorque: CGFloat     var rotationSpeed: CGFloat } ``` |
| To | ``` class SKPhysicsJointPin : SKPhysicsJoint {     class func joint(withBodyA bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint) -> SKPhysicsJointPin     var shouldEnableLimits: Bool     var lowerAngleLimit: CGFloat     var upperAngleLimit: CGFloat     var frictionTorque: CGFloat     var rotationSpeed: CGFloat } ``` |

Modified [SKPhysicsJointPin.joint(withBodyA: SKPhysicsBody, bodyB: SKPhysicsBody, anchor: CGPoint) -> SKPhysicsJointPin [class]](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/1519698-jointwithbodya)

|  | Declaration |
| --- | --- |
| From | ``` class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint) -> SKPhysicsJointPin ``` |
| To | ``` class func joint(withBodyA bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint) -> SKPhysicsJointPin ``` |

Modified [SKPhysicsJointSliding](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding)

|  | Declaration |
| --- | --- |
| From | ``` class SKPhysicsJointSliding : SKPhysicsJoint {     class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint, axis axis: CGVector) -> SKPhysicsJointSliding     var shouldEnableLimits: Bool     var lowerDistanceLimit: CGFloat     var upperDistanceLimit: CGFloat } ``` |
| To | ``` class SKPhysicsJointSliding : SKPhysicsJoint {     class func joint(withBodyA bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint, axis axis: CGVector) -> SKPhysicsJointSliding     var shouldEnableLimits: Bool     var lowerDistanceLimit: CGFloat     var upperDistanceLimit: CGFloat } ``` |

Modified [SKPhysicsJointSliding.joint(withBodyA: SKPhysicsBody, bodyB: SKPhysicsBody, anchor: CGPoint, axis: CGVector) -> SKPhysicsJointSliding [class]](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding/1520333-joint)

|  | Declaration |
| --- | --- |
| From | ``` class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint, axis axis: CGVector) -> SKPhysicsJointSliding ``` |
| To | ``` class func joint(withBodyA bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchor anchor: CGPoint, axis axis: CGVector) -> SKPhysicsJointSliding ``` |

Modified [SKPhysicsJointSpring](https://developer.apple.com/documentation/spritekit/skphysicsjointspring)

|  | Declaration |
| --- | --- |
| From | ``` class SKPhysicsJointSpring : SKPhysicsJoint {     class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointSpring     var damping: CGFloat     var frequency: CGFloat } ``` |
| To | ``` class SKPhysicsJointSpring : SKPhysicsJoint {     class func joint(withBodyA bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointSpring     var damping: CGFloat     var frequency: CGFloat } ``` |

Modified [SKPhysicsJointSpring.joint(withBodyA: SKPhysicsBody, bodyB: SKPhysicsBody, anchorA: CGPoint, anchorB: CGPoint) -> SKPhysicsJointSpring [class]](https://developer.apple.com/documentation/spritekit/skphysicsjointspring/1519665-joint)

|  | Declaration |
| --- | --- |
| From | ``` class func jointWithBodyA(_ bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointSpring ``` |
| To | ``` class func joint(withBodyA bodyA: SKPhysicsBody, bodyB bodyB: SKPhysicsBody, anchorA anchorA: CGPoint, anchorB anchorB: CGPoint) -> SKPhysicsJointSpring ``` |

Modified [SKPhysicsWorld](https://developer.apple.com/documentation/spritekit/skphysicsworld)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKPhysicsWorld : NSObject, NSCoding {     var gravity: CGVector     var speed: CGFloat     unowned(unsafe) var contactDelegate: SKPhysicsContactDelegate?     func addJoint(_ joint: SKPhysicsJoint)     func removeJoint(_ joint: SKPhysicsJoint)     func removeAllJoints()     func sampleFieldsAt(_ position: vector_float3) -> vector_float3     func bodyAtPoint(_ point: CGPoint) -> SKPhysicsBody?     func bodyInRect(_ rect: CGRect) -> SKPhysicsBody?     func bodyAlongRayStart(_ start: CGPoint, end end: CGPoint) -> SKPhysicsBody?     func enumerateBodiesAtPoint(_ point: CGPoint, usingBlock block: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateBodiesInRect(_ rect: CGRect, usingBlock block: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void)     func enumerateBodiesAlongRayStart(_ start: CGPoint, end end: CGPoint, usingBlock block: (SKPhysicsBody, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void) } ``` | NSCoding |
| To | ``` class SKPhysicsWorld : NSObject, NSCoding {     var gravity: CGVector     var speed: CGFloat     unowned(unsafe) var contactDelegate: SKPhysicsContactDelegate?     func add(_ joint: SKPhysicsJoint)     func remove(_ joint: SKPhysicsJoint)     func removeAllJoints()     func sampleFields(at position: vector_float3) -> vector_float3     func body(at point: CGPoint) -> SKPhysicsBody?     func body(in rect: CGRect) -> SKPhysicsBody?     func body(alongRayStart start: CGPoint, end end: CGPoint) -> SKPhysicsBody?     func enumerateBodies(at point: CGPoint, using block: @escaping (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)     func enumerateBodies(in rect: CGRect, using block: @escaping (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)     func enumerateBodies(alongRayStart start: CGPoint, end end: CGPoint, using block: @escaping (SKPhysicsBody, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKPhysicsWorld : CVarArg { } extension SKPhysicsWorld : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding |

Modified [SKPhysicsWorld.add(_: SKPhysicsJoint)](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449617-add)

|  | Declaration |
| --- | --- |
| From | ``` func addJoint(_ joint: SKPhysicsJoint) ``` |
| To | ``` func add(_ joint: SKPhysicsJoint) ``` |

Modified [SKPhysicsWorld.body(alongRayStart: CGPoint, end: CGPoint) -> SKPhysicsBody?](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449613-body)

|  | Declaration |
| --- | --- |
| From | ``` func bodyAlongRayStart(_ start: CGPoint, end end: CGPoint) -> SKPhysicsBody? ``` |
| To | ``` func body(alongRayStart start: CGPoint, end end: CGPoint) -> SKPhysicsBody? ``` |

Modified [SKPhysicsWorld.body(at: CGPoint) -> SKPhysicsBody?](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449625-body)

|  | Declaration |
| --- | --- |
| From | ``` func bodyAtPoint(_ point: CGPoint) -> SKPhysicsBody? ``` |
| To | ``` func body(at point: CGPoint) -> SKPhysicsBody? ``` |

Modified [SKPhysicsWorld.body(in: CGRect) -> SKPhysicsBody?](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449604-body)

|  | Declaration |
| --- | --- |
| From | ``` func bodyInRect(_ rect: CGRect) -> SKPhysicsBody? ``` |
| To | ``` func body(in rect: CGRect) -> SKPhysicsBody? ``` |

Modified [SKPhysicsWorld.enumerateBodies(alongRayStart: CGPoint, end: CGPoint, using: (SKPhysicsBody, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449615-enumeratebodies)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateBodiesAlongRayStart(_ start: CGPoint, end end: CGPoint, usingBlock block: (SKPhysicsBody, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateBodies(alongRayStart start: CGPoint, end end: CGPoint, using block: @escaping (SKPhysicsBody, CGPoint, CGVector, UnsafeMutablePointer<ObjCBool>) -> Swift.Void) ``` |

Modified [SKPhysicsWorld.enumerateBodies(at: CGPoint, using: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449597-enumeratebodies)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateBodiesAtPoint(_ point: CGPoint, usingBlock block: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateBodies(at point: CGPoint, using block: @escaping (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Swift.Void) ``` |

Modified [SKPhysicsWorld.enumerateBodies(in: CGRect, using: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449619-enumeratebodies)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateBodiesInRect(_ rect: CGRect, usingBlock block: (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateBodies(in rect: CGRect, using block: @escaping (SKPhysicsBody, UnsafeMutablePointer<ObjCBool>) -> Swift.Void) ``` |

Modified [SKPhysicsWorld.remove(_: SKPhysicsJoint)](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449609-remove)

|  | Declaration |
| --- | --- |
| From | ``` func removeJoint(_ joint: SKPhysicsJoint) ``` |
| To | ``` func remove(_ joint: SKPhysicsJoint) ``` |

Modified [SKPhysicsWorld.sampleFields(at: vector_float3) -> vector_float3](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449627-samplefieldsat)

|  | Declaration |
| --- | --- |
| From | ``` func sampleFieldsAt(_ position: vector_float3) -> vector_float3 ``` |
| To | ``` func sampleFields(at position: vector_float3) -> vector_float3 ``` |

Modified [SKRange](https://developer.apple.com/documentation/spritekit/skrange)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKRange : NSObject, NSCoding, NSCopying {     init(lowerLimit lower: CGFloat, upperLimit upper: CGFloat)     class func rangeWithLowerLimit(_ lower: CGFloat, upperLimit upper: CGFloat) -> Self     convenience init(lowerLimit lower: CGFloat)     class func rangeWithLowerLimit(_ lower: CGFloat) -> Self     convenience init(upperLimit upper: CGFloat)     class func rangeWithUpperLimit(_ upper: CGFloat) -> Self     convenience init(constantValue value: CGFloat)     class func rangeWithConstantValue(_ value: CGFloat) -> Self     convenience init(value value: CGFloat, variance variance: CGFloat)     class func rangeWithValue(_ value: CGFloat, variance variance: CGFloat) -> Self     class func rangeWithNoLimits() -> Self     var lowerLimit: CGFloat     var upperLimit: CGFloat } ``` | NSCoding, NSCopying |
| To | ``` class SKRange : NSObject, NSCoding, NSCopying {     init(lowerLimit lower: CGFloat, upperLimit upper: CGFloat)     class func withLowerLimit(_ lower: CGFloat, upperLimit upper: CGFloat) -> Self     convenience init(lowerLimit lower: CGFloat)     class func withLowerLimit(_ lower: CGFloat) -> Self     convenience init(upperLimit upper: CGFloat)     class func withUpperLimit(_ upper: CGFloat) -> Self     convenience init(constantValue value: CGFloat)     class func withConstantValue(_ value: CGFloat) -> Self     convenience init(value value: CGFloat, variance variance: CGFloat)     class func withValue(_ value: CGFloat, variance variance: CGFloat) -> Self     class func withNoLimits() -> Self     var lowerLimit: CGFloat     var upperLimit: CGFloat     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKRange : CVarArg { } extension SKRange : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying |

Modified [SKRange.withNoLimits() -> Self [class]](https://developer.apple.com/documentation/spritekit/skrange/1519920-rangewithnolimits)

|  | Declaration |
| --- | --- |
| From | ``` class func rangeWithNoLimits() -> Self ``` |
| To | ``` class func withNoLimits() -> Self ``` |

Modified [SKReachConstraints](https://developer.apple.com/documentation/spritekit/skreachconstraints)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKReachConstraints : NSObject, NSCoding {     var lowerAngleLimit: CGFloat     var upperAngleLimit: CGFloat     init(lowerAngleLimit lowerAngleLimit: CGFloat, upperAngleLimit upperAngleLimit: CGFloat) } ``` | NSCoding |
| To | ``` class SKReachConstraints : NSObject, NSCoding {     var lowerAngleLimit: CGFloat     var upperAngleLimit: CGFloat     init(lowerAngleLimit lowerAngleLimit: CGFloat, upperAngleLimit upperAngleLimit: CGFloat)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKReachConstraints : CVarArg { } extension SKReachConstraints : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding |

Modified [SKReferenceNode](https://developer.apple.com/documentation/spritekit/skreferencenode)

|  | Declaration |
| --- | --- |
| From | ``` class SKReferenceNode : SKNode {     init(URL url: NSURL?)     init(fileNamed fileName: String?)     init?(coder aDecoder: NSCoder)     convenience init(fileNamed fileName: String)     class func referenceNodeWithFileNamed(_ fileName: String) -> Self     convenience init(URL referenceURL: NSURL)     class func referenceNodeWithURL(_ referenceURL: NSURL) -> Self     func didLoadReferenceNode(_ node: SKNode?)     func resolveReferenceNode() } ``` |
| To | ``` class SKReferenceNode : SKNode {     init(url url: URL?)     init(fileNamed fileName: String?)     init?(coder aDecoder: NSCoder)     convenience init(fileNamed fileName: String)     class func withFileNamed(_ fileName: String) -> Self     convenience init(url referenceURL: URL)     class func withURL(_ referenceURL: URL) -> Self     func didLoad(_ node: SKNode?)     func resolve() } ``` |

Modified [SKReferenceNode.didLoad(_: SKNode?)](https://developer.apple.com/documentation/spritekit/skreferencenode/1508364-didload)

|  | Declaration |
| --- | --- |
| From | ``` func didLoadReferenceNode(_ node: SKNode?) ``` |
| To | ``` func didLoad(_ node: SKNode?) ``` |

Modified [SKReferenceNode.init(url: URL)](https://developer.apple.com/documentation/spritekit/skreferencenode/1508365-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(URL referenceURL: NSURL) ``` |
| To | ``` convenience init(url referenceURL: URL) ``` |

Modified [SKReferenceNode.init(url: URL?)](https://developer.apple.com/documentation/spritekit/skreferencenode/1508366-init)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL?) ``` |
| To | ``` init(url url: URL?) ``` |

Modified [SKReferenceNode.resolve()](https://developer.apple.com/documentation/spritekit/skreferencenode/1508371-resolvereferencenode)

|  | Declaration |
| --- | --- |
| From | ``` func resolveReferenceNode() ``` |
| To | ``` func resolve() ``` |

Modified [SKRegion](https://developer.apple.com/documentation/spritekit/skregion)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKRegion : NSObject, NSCopying, NSCoding {     var path: CGPath? { get }     class func infiniteRegion() -> Self     init(radius radius: Float)     init(size size: CGSize)     init(path path: CGPath)     func inverseRegion() -> Self     func regionByUnionWithRegion(_ region: SKRegion) -> Self     func regionByDifferenceFromRegion(_ region: SKRegion) -> Self     func regionByIntersectionWithRegion(_ region: SKRegion) -> Self     func containsPoint(_ point: CGPoint) -> Bool } ``` | NSCoding, NSCopying |
| To | ``` class SKRegion : NSObject, NSCopying, NSCoding {     var path: CGPath? { get }     class func infinite() -> Self     init(radius radius: Float)     init(size size: CGSize)     init(path path: CGPath)     func inverse() -> Self     func byUnion(with region: SKRegion) -> Self     func byDifference(from region: SKRegion) -> Self     func byIntersection(with region: SKRegion) -> Self     func contains(_ point: CGPoint) -> Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKRegion : CVarArg { } extension SKRegion : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying |

Modified [SKRegion.byDifference(from: SKRegion) -> Self](https://developer.apple.com/documentation/spritekit/skregion/1519879-bydifference)

|  | Declaration |
| --- | --- |
| From | ``` func regionByDifferenceFromRegion(_ region: SKRegion) -> Self ``` |
| To | ``` func byDifference(from region: SKRegion) -> Self ``` |

Modified [SKRegion.byIntersection(with: SKRegion) -> Self](https://developer.apple.com/documentation/spritekit/skregion/1519646-byintersection)

|  | Declaration |
| --- | --- |
| From | ``` func regionByIntersectionWithRegion(_ region: SKRegion) -> Self ``` |
| To | ``` func byIntersection(with region: SKRegion) -> Self ``` |

Modified [SKRegion.byUnion(with: SKRegion) -> Self](https://developer.apple.com/documentation/spritekit/skregion/1519702-byunion)

|  | Declaration |
| --- | --- |
| From | ``` func regionByUnionWithRegion(_ region: SKRegion) -> Self ``` |
| To | ``` func byUnion(with region: SKRegion) -> Self ``` |

Modified [SKRegion.contains(_: CGPoint) -> Bool](https://developer.apple.com/documentation/spritekit/skregion/1519695-contains)

|  | Declaration |
| --- | --- |
| From | ``` func containsPoint(_ point: CGPoint) -> Bool ``` |
| To | ``` func contains(_ point: CGPoint) -> Bool ``` |

Modified [SKRegion.infinite() -> Self [class]](https://developer.apple.com/documentation/spritekit/skregion/1520061-infiniteregion)

|  | Declaration |
| --- | --- |
| From | ``` class func infiniteRegion() -> Self ``` |
| To | ``` class func infinite() -> Self ``` |

Modified [SKRegion.inverse() -> Self](https://developer.apple.com/documentation/spritekit/skregion/1519700-inverseregion)

|  | Declaration |
| --- | --- |
| From | ``` func inverseRegion() -> Self ``` |
| To | ``` func inverse() -> Self ``` |

Modified [SKRepeatMode [enum]](https://developer.apple.com/documentation/spritekit/skrepeatmode)

|  | Declaration |
| --- | --- |
| From | ``` enum SKRepeatMode : Int {     case Clamp     case Loop } ``` |
| To | ``` enum SKRepeatMode : Int {     case clamp     case loop } ``` |

Modified [SKRepeatMode.clamp](https://developer.apple.com/documentation/spritekit/skrepeatmode/skrepeatmodeclamp)

|  | Declaration |
| --- | --- |
| From | ``` case Clamp ``` |
| To | ``` case clamp ``` |

Modified [SKRepeatMode.loop](https://developer.apple.com/documentation/spritekit/skrepeatmode/skrepeatmodeloop)

|  | Declaration |
| --- | --- |
| From | ``` case Loop ``` |
| To | ``` case loop ``` |

Modified [SKScene](https://developer.apple.com/documentation/spritekit/skscene)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKScene : SKEffectNode {     init(size size: CGSize)     class func sceneWithSize(_ size: CGSize) -> Self     var size: CGSize     var scaleMode: SKSceneScaleMode     weak var camera: SKCameraNode?     weak var listener: SKNode?     var audioEngine: AVAudioEngine { get }     var backgroundColor: UIColor     unowned(unsafe) var delegate: SKSceneDelegate?     var anchorPoint: CGPoint     var physicsWorld: SKPhysicsWorld { get }     func convertPointFromView(_ point: CGPoint) -> CGPoint     func convertPointToView(_ point: CGPoint) -> CGPoint     weak var view: SKView? { get }     func update(_ currentTime: NSTimeInterval)     func didEvaluateActions()     func didSimulatePhysics()     func didApplyConstraints()     func didFinishUpdate()     func didMoveToView(_ view: SKView)     func willMoveFromView(_ view: SKView)     func didChangeSize(_ oldSize: CGSize) } ``` | -- |
| To | ``` class SKScene : SKEffectNode {     init(size size: CGSize)     class func withSize(_ size: CGSize) -> Self     func sceneDidLoad()     var size: CGSize     var scaleMode: SKSceneScaleMode     weak var camera: SKCameraNode?     weak var listener: SKNode?     var audioEngine: AVAudioEngine { get }     var backgroundColor: UIColor     weak var delegate: SKSceneDelegate?     var anchorPoint: CGPoint     var physicsWorld: SKPhysicsWorld { get }     weak var view: SKView? { get }     func convertPoint(fromView point: CGPoint) -> CGPoint     func convertPoint(toView point: CGPoint) -> CGPoint     func update(_ currentTime: TimeInterval)     func didEvaluateActions()     func didSimulatePhysics()     func didApplyConstraints()     func didFinishUpdate()     func didMove(to view: SKView)     func willMove(from view: SKView)     func didChangeSize(_ oldSize: CGSize) } extension SKScene : GKSceneRootNodeType { } ``` | GKSceneRootNodeType |

Modified [SKScene.convertPoint(fromView: CGPoint) -> CGPoint](https://developer.apple.com/documentation/spritekit/skscene/1520395-convertpoint)

|  | Declaration |
| --- | --- |
| From | ``` func convertPointFromView(_ point: CGPoint) -> CGPoint ``` |
| To | ``` func convertPoint(fromView point: CGPoint) -> CGPoint ``` |

Modified [SKScene.convertPoint(toView: CGPoint) -> CGPoint](https://developer.apple.com/documentation/spritekit/skscene/1520082-convertpointtoview)

|  | Declaration |
| --- | --- |
| From | ``` func convertPointToView(_ point: CGPoint) -> CGPoint ``` |
| To | ``` func convertPoint(toView point: CGPoint) -> CGPoint ``` |

Modified [SKScene.delegate](https://developer.apple.com/documentation/spritekit/skscene/1520213-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: SKSceneDelegate? ``` |
| To | ``` weak var delegate: SKSceneDelegate? ``` |

Modified [SKScene.didMove(to: SKView)](https://developer.apple.com/documentation/spritekit/skscene/1519607-didmovetoview)

|  | Declaration |
| --- | --- |
| From | ``` func didMoveToView(_ view: SKView) ``` |
| To | ``` func didMove(to view: SKView) ``` |

Modified [SKScene.update(_: TimeInterval)](https://developer.apple.com/documentation/spritekit/skscene/1519802-update)

|  | Declaration |
| --- | --- |
| From | ``` func update(_ currentTime: NSTimeInterval) ``` |
| To | ``` func update(_ currentTime: TimeInterval) ``` |

Modified [SKScene.willMove(from: SKView)](https://developer.apple.com/documentation/spritekit/skscene/1519703-willmovefromview)

|  | Declaration |
| --- | --- |
| From | ``` func willMoveFromView(_ view: SKView) ``` |
| To | ``` func willMove(from view: SKView) ``` |

Modified [SKSceneDelegate](https://developer.apple.com/documentation/spritekit/skscenedelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol SKSceneDelegate : NSObjectProtocol {     optional func update(_ currentTime: NSTimeInterval, forScene scene: SKScene)     optional func didEvaluateActionsForScene(_ scene: SKScene)     optional func didSimulatePhysicsForScene(_ scene: SKScene)     optional func didApplyConstraintsForScene(_ scene: SKScene)     optional func didFinishUpdateForScene(_ scene: SKScene) } ``` |
| To | ``` protocol SKSceneDelegate : NSObjectProtocol {     optional func update(_ currentTime: TimeInterval, for scene: SKScene)     optional func didEvaluateActions(for scene: SKScene)     optional func didSimulatePhysics(for scene: SKScene)     optional func didApplyConstraints(for scene: SKScene)     optional func didFinishUpdate(for scene: SKScene) } ``` |

Modified [SKSceneDelegate.didApplyConstraints(for: SKScene)](https://developer.apple.com/documentation/spritekit/skscenedelegate/1520375-didapplyconstraints)

|  | Declaration |
| --- | --- |
| From | ``` optional func didApplyConstraintsForScene(_ scene: SKScene) ``` |
| To | ``` optional func didApplyConstraints(for scene: SKScene) ``` |

Modified [SKSceneDelegate.didEvaluateActions(for: SKScene)](https://developer.apple.com/documentation/spritekit/skscenedelegate/1520071-didevaluateactions)

|  | Declaration |
| --- | --- |
| From | ``` optional func didEvaluateActionsForScene(_ scene: SKScene) ``` |
| To | ``` optional func didEvaluateActions(for scene: SKScene) ``` |

Modified [SKSceneDelegate.didFinishUpdate(for: SKScene)](https://developer.apple.com/documentation/spritekit/skscenedelegate/1519814-didfinishupdateforscene)

|  | Declaration |
| --- | --- |
| From | ``` optional func didFinishUpdateForScene(_ scene: SKScene) ``` |
| To | ``` optional func didFinishUpdate(for scene: SKScene) ``` |

Modified [SKSceneDelegate.didSimulatePhysics(for: SKScene)](https://developer.apple.com/documentation/spritekit/skscenedelegate/1520392-didsimulatephysics)

|  | Declaration |
| --- | --- |
| From | ``` optional func didSimulatePhysicsForScene(_ scene: SKScene) ``` |
| To | ``` optional func didSimulatePhysics(for scene: SKScene) ``` |

Modified [SKSceneDelegate.update(_: TimeInterval, for: SKScene)](https://developer.apple.com/documentation/spritekit/skscenedelegate/1519757-update)

|  | Declaration |
| --- | --- |
| From | ``` optional func update(_ currentTime: NSTimeInterval, forScene scene: SKScene) ``` |
| To | ``` optional func update(_ currentTime: TimeInterval, for scene: SKScene) ``` |

Modified [SKSceneScaleMode [enum]](https://developer.apple.com/documentation/spritekit/skscenescalemode)

|  | Declaration |
| --- | --- |
| From | ``` enum SKSceneScaleMode : Int {     case Fill     case AspectFill     case AspectFit     case ResizeFill } ``` |
| To | ``` enum SKSceneScaleMode : Int {     case fill     case aspectFill     case aspectFit     case resizeFill } ``` |

Modified [SKSceneScaleMode.aspectFill](https://developer.apple.com/documentation/spritekit/skscenescalemode/aspectfill)

|  | Declaration |
| --- | --- |
| From | ``` case AspectFill ``` |
| To | ``` case aspectFill ``` |

Modified [SKSceneScaleMode.aspectFit](https://developer.apple.com/documentation/spritekit/skscenescalemode/aspectfit)

|  | Declaration |
| --- | --- |
| From | ``` case AspectFit ``` |
| To | ``` case aspectFit ``` |

Modified [SKSceneScaleMode.fill](https://developer.apple.com/documentation/spritekit/skscenescalemode/skscenescalemodefill)

|  | Declaration |
| --- | --- |
| From | ``` case Fill ``` |
| To | ``` case fill ``` |

Modified [SKSceneScaleMode.resizeFill](https://developer.apple.com/documentation/spritekit/skscenescalemode/skscenescalemoderesizefill)

|  | Declaration |
| --- | --- |
| From | ``` case ResizeFill ``` |
| To | ``` case resizeFill ``` |

Modified [SKShader](https://developer.apple.com/documentation/spritekit/skshader)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKShader : NSObject, NSCopying, NSCoding {     init(source source: String)     init(source source: String, uniforms uniforms: [SKUniform])     convenience init()     class func shader() -> Self     class func shaderWithSource(_ source: String) -> Self     class func shaderWithSource(_ source: String, uniforms uniforms: [SKUniform]) -> Self     convenience init(fileNamed name: String)     class func shaderWithFileNamed(_ name: String) -> Self     var source: String?     var uniforms: [SKUniform]     func addUniform(_ uniform: SKUniform)     func uniformNamed(_ name: String) -> SKUniform?     func removeUniformNamed(_ name: String) } ``` | NSCoding, NSCopying |
| To | ``` class SKShader : NSObject, NSCopying, NSCoding {     init(source source: String)     init(source source: String, uniforms uniforms: [SKUniform])     convenience init()     class func shader() -> Self     class func withSource(_ source: String) -> Self     class func withSource(_ source: String, uniforms uniforms: [SKUniform]) -> Self     convenience init(fileNamed name: String)     class func withFileNamed(_ name: String) -> Self     var source: String?     var uniforms: [SKUniform]     func addUniform(_ uniform: SKUniform)     func uniformNamed(_ name: String) -> SKUniform?     func removeUniformNamed(_ name: String)     var attributes: [SKAttribute]     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKShader : CVarArg { } extension SKShader : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying |

Modified [SKShapeNode](https://developer.apple.com/documentation/spritekit/skshapenode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKShapeNode : SKNode {     convenience init(path path: CGPath)     class func shapeNodeWithPath(_ path: CGPath) -> Self     convenience init(path path: CGPath, centered centered: Bool)     class func shapeNodeWithPath(_ path: CGPath, centered centered: Bool) -> Self     convenience init(rect rect: CGRect)     class func shapeNodeWithRect(_ rect: CGRect) -> Self     convenience init(rectOfSize size: CGSize)     class func shapeNodeWithRectOfSize(_ size: CGSize) -> Self     convenience init(rect rect: CGRect, cornerRadius cornerRadius: CGFloat)     class func shapeNodeWithRect(_ rect: CGRect, cornerRadius cornerRadius: CGFloat) -> Self     convenience init(rectOfSize size: CGSize, cornerRadius cornerRadius: CGFloat)     class func shapeNodeWithRectOfSize(_ size: CGSize, cornerRadius cornerRadius: CGFloat) -> Self     convenience init(circleOfRadius radius: CGFloat)     class func shapeNodeWithCircleOfRadius(_ radius: CGFloat) -> Self     convenience init(ellipseInRect rect: CGRect)     class func shapeNodeWithEllipseInRect(_ rect: CGRect) -> Self     convenience init(ellipseOfSize size: CGSize)     class func shapeNodeWithEllipseOfSize(_ size: CGSize) -> Self     convenience init(points points: UnsafeMutablePointer<CGPoint>, count numPoints: Int)     class func shapeNodeWithPoints(_ points: UnsafeMutablePointer<CGPoint>, count numPoints: Int) -> Self     convenience init(splinePoints points: UnsafeMutablePointer<CGPoint>, count numPoints: Int)     class func shapeNodeWithSplinePoints(_ points: UnsafeMutablePointer<CGPoint>, count numPoints: Int) -> Self     var path: CGPath?     var strokeColor: UIColor     var fillColor: UIColor     var blendMode: SKBlendMode     var antialiased: Bool     var lineWidth: CGFloat     var glowWidth: CGFloat     var lineCap: CGLineCap     var lineJoin: CGLineJoin     var miterLimit: CGFloat     var lineLength: CGFloat { get }     var fillTexture: SKTexture?     var fillShader: SKShader?     var strokeTexture: SKTexture?     var strokeShader: SKShader? } extension SKShapeNode : _Reflectable { } extension SKShapeNode : _Reflectable { } ``` | -- |
| To | ``` class SKShapeNode : SKNode {     convenience init(path path: CGPath)     class func withPath(_ path: CGPath) -> Self     convenience init(path path: CGPath, centered centered: Bool)     class func withPath(_ path: CGPath, centered centered: Bool) -> Self     convenience init(rect rect: CGRect)     class func withRect(_ rect: CGRect) -> Self     convenience init(rectOf size: CGSize)     class func withRectOf(_ size: CGSize) -> Self     convenience init(rect rect: CGRect, cornerRadius cornerRadius: CGFloat)     class func withRect(_ rect: CGRect, cornerRadius cornerRadius: CGFloat) -> Self     convenience init(rectOf size: CGSize, cornerRadius cornerRadius: CGFloat)     class func withRectOf(_ size: CGSize, cornerRadius cornerRadius: CGFloat) -> Self     convenience init(circleOfRadius radius: CGFloat)     class func withCircleOfRadius(_ radius: CGFloat) -> Self     convenience init(ellipseIn rect: CGRect)     class func withEllipseIn(_ rect: CGRect) -> Self     convenience init(ellipseOf size: CGSize)     class func withEllipseOf(_ size: CGSize) -> Self     convenience init(points points: UnsafeMutablePointer<CGPoint>, count numPoints: Int)     class func withPoints(_ points: UnsafeMutablePointer<CGPoint>, count numPoints: Int) -> Self     convenience init(splinePoints points: UnsafeMutablePointer<CGPoint>, count numPoints: Int)     class func withSplinePoints(_ points: UnsafeMutablePointer<CGPoint>, count numPoints: Int) -> Self     var path: CGPath?     var strokeColor: UIColor     var fillColor: UIColor     var blendMode: SKBlendMode     var isAntialiased: Bool     var lineWidth: CGFloat     var glowWidth: CGFloat     var lineCap: CGLineCap     var lineJoin: CGLineJoin     var miterLimit: CGFloat     var lineLength: CGFloat { get }     var fillTexture: SKTexture?     var fillShader: SKShader?     var strokeTexture: SKTexture?     var strokeShader: SKShader? } extension SKShapeNode : CustomPlaygroundQuickLookable {     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } extension SKShapeNode : CustomPlaygroundQuickLookable {     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } ``` | CustomPlaygroundQuickLookable |

Modified [SKShapeNode.init(ellipseIn: CGRect)](https://developer.apple.com/documentation/spritekit/skshapenode/1520412-shapenodewithellipseinrect)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(ellipseInRect rect: CGRect) ``` |
| To | ``` convenience init(ellipseIn rect: CGRect) ``` |

Modified [SKShapeNode.init(ellipseOf: CGSize)](https://developer.apple.com/documentation/spritekit/skshapenode/1519980-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(ellipseOfSize size: CGSize) ``` |
| To | ``` convenience init(ellipseOf size: CGSize) ``` |

Modified [SKShapeNode.init(rectOf: CGSize)](https://developer.apple.com/documentation/spritekit/skshapenode/1520147-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(rectOfSize size: CGSize) ``` |
| To | ``` convenience init(rectOf size: CGSize) ``` |

Modified [SKShapeNode.init(rectOf: CGSize, cornerRadius: CGFloat)](https://developer.apple.com/documentation/spritekit/skshapenode/1519712-shapenodewithrectofsize)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(rectOfSize size: CGSize, cornerRadius cornerRadius: CGFloat) ``` |
| To | ``` convenience init(rectOf size: CGSize, cornerRadius cornerRadius: CGFloat) ``` |

Modified [SKShapeNode.isAntialiased](https://developer.apple.com/documentation/spritekit/skshapenode/1519719-isantialiased)

|  | Declaration |
| --- | --- |
| From | ``` var antialiased: Bool ``` |
| To | ``` var isAntialiased: Bool ``` |

Modified [SKSpriteNode](https://developer.apple.com/documentation/spritekit/skspritenode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKSpriteNode : SKNode {     convenience init(texture texture: SKTexture?, size size: CGSize)     class func spriteNodeWithTexture(_ texture: SKTexture?, size size: CGSize) -> Self     convenience init(texture texture: SKTexture?)     class func spriteNodeWithTexture(_ texture: SKTexture?) -> Self     convenience init(texture texture: SKTexture?, normalMap normalMap: SKTexture?)     class func spriteNodeWithTexture(_ texture: SKTexture?, normalMap normalMap: SKTexture?) -> Self     convenience init(imageNamed name: String)     class func spriteNodeWithImageNamed(_ name: String) -> Self     convenience init(imageNamed name: String, normalMapped generateNormalMap: Bool)     class func spriteNodeWithImageNamed(_ name: String, normalMapped generateNormalMap: Bool) -> Self     convenience init(color color: UIColor, size size: CGSize)     class func spriteNodeWithColor(_ color: UIColor, size size: CGSize) -> Self     init(texture texture: SKTexture?, color color: UIColor, size size: CGSize)     convenience init(texture texture: SKTexture?)     convenience init(imageNamed name: String)     convenience init(color color: UIColor, size size: CGSize)     init?(coder aDecoder: NSCoder)     var texture: SKTexture?     var normalTexture: SKTexture?     var lightingBitMask: UInt32     var shadowCastBitMask: UInt32     var shadowedBitMask: UInt32     var centerRect: CGRect     var colorBlendFactor: CGFloat     var color: UIColor     var blendMode: SKBlendMode     var anchorPoint: CGPoint     var size: CGSize     var shader: SKShader? } extension SKSpriteNode : _Reflectable { } extension SKSpriteNode : _Reflectable { } ``` | -- |
| To | ``` class SKSpriteNode : SKNode, SKWarpable {     convenience init(texture texture: SKTexture?, size size: CGSize)     class func withTexture(_ texture: SKTexture?, size size: CGSize) -> Self     convenience init(texture texture: SKTexture?)     class func withTexture(_ texture: SKTexture?) -> Self     convenience init(texture texture: SKTexture?, normalMap normalMap: SKTexture?)     class func withTexture(_ texture: SKTexture?, normalMap normalMap: SKTexture?) -> Self     convenience init(imageNamed name: String)     class func withImageNamed(_ name: String) -> Self     convenience init(imageNamed name: String, normalMapped generateNormalMap: Bool)     class func withImageNamed(_ name: String, normalMapped generateNormalMap: Bool) -> Self     convenience init(color color: UIColor, size size: CGSize)     class func withColor(_ color: UIColor, size size: CGSize) -> Self     init(texture texture: SKTexture?, color color: UIColor, size size: CGSize)     convenience init(texture texture: SKTexture?)     convenience init(imageNamed name: String)     convenience init(color color: UIColor, size size: CGSize)     init?(coder aDecoder: NSCoder)     var texture: SKTexture?     var normalTexture: SKTexture?     var lightingBitMask: UInt32     var shadowCastBitMask: UInt32     var shadowedBitMask: UInt32     var centerRect: CGRect     var colorBlendFactor: CGFloat     var color: UIColor     var blendMode: SKBlendMode     var anchorPoint: CGPoint     var size: CGSize     func scale(to size: CGSize)     var shader: SKShader? } extension SKSpriteNode : CustomPlaygroundQuickLookable {     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } extension SKSpriteNode : CustomPlaygroundQuickLookable {     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } ``` | CustomPlaygroundQuickLookable, SKWarpable |

Modified [SKTexture](https://developer.apple.com/documentation/spritekit/sktexture)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKTexture : NSObject, NSCopying, NSCoding {     convenience init(imageNamed name: String)     class func textureWithImageNamed(_ name: String) -> Self     convenience init(rect rect: CGRect, inTexture texture: SKTexture)     class func textureWithRect(_ rect: CGRect, inTexture texture: SKTexture) -> Self     convenience init(vectorNoiseWithSmoothness smoothness: CGFloat, size size: CGSize)     class func textureVectorNoiseWithSmoothness(_ smoothness: CGFloat, size size: CGSize) -> Self     convenience init(noiseWithSmoothness smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool)     class func textureNoiseWithSmoothness(_ smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool) -> Self     convenience init(CGImage image: CGImage)     class func textureWithCGImage(_ image: CGImage) -> Self     convenience init(image image: UIImage)     class func textureWithImage(_ image: UIImage) -> Self     convenience init(data pixelData: NSData, size size: CGSize)     class func textureWithData(_ pixelData: NSData, size size: CGSize) -> Self     convenience init(data pixelData: NSData, size size: CGSize, flipped flipped: Bool)     class func textureWithData(_ pixelData: NSData, size size: CGSize, flipped flipped: Bool) -> Self     convenience init(data pixelData: NSData, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32)     class func textureWithData(_ pixelData: NSData, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32) -> Self     func textureByApplyingCIFilter(_ filter: CIFilter) -> Self     func textureByGeneratingNormalMap() -> Self     func textureByGeneratingNormalMapWithSmoothness(_ smoothness: CGFloat, contrast contrast: CGFloat) -> Self     func textureRect() -> CGRect     func size() -> CGSize     var filteringMode: SKTextureFilteringMode     var usesMipmaps: Bool     func CGImage() -> CGImage     class func preloadTextures(_ textures: [SKTexture], withCompletionHandler completionHandler: () -> Void)     func preloadWithCompletionHandler(_ completionHandler: () -> Void) } extension SKTexture : _Reflectable { } extension SKTexture : _Reflectable { } ``` | NSCoding, NSCopying |
| To | ``` class SKTexture : NSObject, NSCopying, NSCoding {     convenience init(imageNamed name: String)     class func withImageNamed(_ name: String) -> Self     convenience init(rect rect: CGRect, in texture: SKTexture)     class func withRect(_ rect: CGRect, in texture: SKTexture) -> Self     convenience init(vectorNoiseWithSmoothness smoothness: CGFloat, size size: CGSize)     class func textureVectorNoise(withSmoothness smoothness: CGFloat, size size: CGSize) -> Self     convenience init(noiseWithSmoothness smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool)     class func textureNoise(withSmoothness smoothness: CGFloat, size size: CGSize, grayscale grayscale: Bool) -> Self     convenience init(cgImage image: CGImage)     class func withCGImage(_ image: CGImage) -> Self     convenience init(image image: UIImage)     class func withImage(_ image: UIImage) -> Self     convenience init(data pixelData: Data, size size: CGSize)     class func withData(_ pixelData: Data, size size: CGSize) -> Self     convenience init(data pixelData: Data, size size: CGSize, flipped flipped: Bool)     class func withData(_ pixelData: Data, size size: CGSize, flipped flipped: Bool) -> Self     convenience init(data pixelData: Data, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32)     class func withData(_ pixelData: Data, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32) -> Self     func applying(_ filter: CIFilter) -> Self     func generatingNormalMap() -> Self     func generatingNormalMap(withSmoothness smoothness: CGFloat, contrast contrast: CGFloat) -> Self     func textureRect() -> CGRect     func size() -> CGSize     var filteringMode: SKTextureFilteringMode     var usesMipmaps: Bool     func cgImage() -> CGImage     class func preload(_ textures: [SKTexture], withCompletionHandler completionHandler: @escaping () -> Swift.Void)     func preload(completionHandler completionHandler: @escaping () -> Swift.Void)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKTexture {     convenience init(noiseMap noiseMap: GKNoiseMap)     class func withNoiseMap(_ noiseMap: GKNoiseMap) -> Self } extension SKTexture : CVarArg { } extension SKTexture : CustomPlaygroundQuickLookable {     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } extension SKTexture : Equatable, Hashable {     var hashValue: Int { get } } extension SKTexture : CustomPlaygroundQuickLookable {     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } ``` | CVarArg, CustomPlaygroundQuickLookable, Equatable, Hashable, NSCoding, NSCopying |

Modified [SKTexture.applying(_: CIFilter) -> Self](https://developer.apple.com/documentation/spritekit/sktexture/1520388-texturebyapplyingcifilter)

|  | Declaration |
| --- | --- |
| From | ``` func textureByApplyingCIFilter(_ filter: CIFilter) -> Self ``` |
| To | ``` func applying(_ filter: CIFilter) -> Self ``` |

Modified [SKTexture.cgImage() -> CGImage](https://developer.apple.com/documentation/spritekit/sktexture/1519755-cgimage)

|  | Declaration |
| --- | --- |
| From | ``` func CGImage() -> CGImage ``` |
| To | ``` func cgImage() -> CGImage ``` |

Modified [SKTexture.generatingNormalMap() -> Self](https://developer.apple.com/documentation/spritekit/sktexture/1519687-texturebygeneratingnormalmap)

|  | Declaration |
| --- | --- |
| From | ``` func textureByGeneratingNormalMap() -> Self ``` |
| To | ``` func generatingNormalMap() -> Self ``` |

Modified [SKTexture.generatingNormalMap(withSmoothness: CGFloat, contrast: CGFloat) -> Self](https://developer.apple.com/documentation/spritekit/sktexture/1520441-texturebygeneratingnormalmapwith)

|  | Declaration |
| --- | --- |
| From | ``` func textureByGeneratingNormalMapWithSmoothness(_ smoothness: CGFloat, contrast contrast: CGFloat) -> Self ``` |
| To | ``` func generatingNormalMap(withSmoothness smoothness: CGFloat, contrast contrast: CGFloat) -> Self ``` |

Modified [SKTexture.init(cgImage: CGImage)](https://developer.apple.com/documentation/spritekit/sktexture/1519576-texturewithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(CGImage image: CGImage) ``` |
| To | ``` convenience init(cgImage image: CGImage) ``` |

Modified [SKTexture.init(data: Data, size: CGSize)](https://developer.apple.com/documentation/spritekit/sktexture/1519962-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(data pixelData: NSData, size size: CGSize) ``` |
| To | ``` convenience init(data pixelData: Data, size size: CGSize) ``` |

Modified [SKTexture.init(data: Data, size: CGSize, flipped: Bool)](https://developer.apple.com/documentation/spritekit/sktexture/1519674-texturewithdata)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(data pixelData: NSData, size size: CGSize, flipped flipped: Bool) ``` |
| To | ``` convenience init(data pixelData: Data, size size: CGSize, flipped flipped: Bool) ``` |

Modified [SKTexture.init(data: Data, size: CGSize, rowLength: UInt32, alignment: UInt32)](https://developer.apple.com/documentation/spritekit/sktexture/1520181-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(data pixelData: NSData, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32) ``` |
| To | ``` convenience init(data pixelData: Data, size size: CGSize, rowLength rowLength: UInt32, alignment alignment: UInt32) ``` |

Modified [SKTexture.init(rect: CGRect, in: SKTexture)](https://developer.apple.com/documentation/spritekit/sktexture/1520425-texturewithrect)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(rect rect: CGRect, inTexture texture: SKTexture) ``` |
| To | ``` convenience init(rect rect: CGRect, in texture: SKTexture) ``` |

Modified [SKTexture.preload(_: [SKTexture], withCompletionHandler: () -> Swift.Void) [class]](https://developer.apple.com/documentation/spritekit/sktexture/1519817-preloadtextures)

|  | Declaration |
| --- | --- |
| From | ``` class func preloadTextures(_ textures: [SKTexture], withCompletionHandler completionHandler: () -> Void) ``` |
| To | ``` class func preload(_ textures: [SKTexture], withCompletionHandler completionHandler: @escaping () -> Swift.Void) ``` |

Modified [SKTexture.preload(completionHandler: () -> Swift.Void)](https://developer.apple.com/documentation/spritekit/sktexture/1520172-preloadwithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func preloadWithCompletionHandler(_ completionHandler: () -> Void) ``` |
| To | ``` func preload(completionHandler completionHandler: @escaping () -> Swift.Void) ``` |

Modified [SKTextureAtlas](https://developer.apple.com/documentation/spritekit/sktextureatlas)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKTextureAtlas : NSObject, NSCoding {     convenience init(named name: String)     class func atlasNamed(_ name: String) -> Self     convenience init(dictionary properties: [String : AnyObject])     class func atlasWithDictionary(_ properties: [String : AnyObject]) -> Self     func textureNamed(_ name: String) -> SKTexture     class func preloadTextureAtlases(_ textureAtlases: [SKTextureAtlas], withCompletionHandler completionHandler: () -> Void)     class func preloadTextureAtlasesNamed(_ atlasNames: [String], withCompletionHandler completionHandler: (NSError?, [SKTextureAtlas]) -> Void)     func preloadWithCompletionHandler(_ completionHandler: () -> Void)     var textureNames: [String] { get } } extension SKTextureAtlas : _Reflectable { } extension SKTextureAtlas : _Reflectable { } ``` | NSCoding |
| To | ``` class SKTextureAtlas : NSObject, NSCoding {     convenience init(named name: String)     class func atlasNamed(_ name: String) -> Self     convenience init(dictionary properties: [String : Any])     class func withDictionary(_ properties: [String : Any]) -> Self     func textureNamed(_ name: String) -> SKTexture     class func preloadTextureAtlases(_ textureAtlases: [SKTextureAtlas], withCompletionHandler completionHandler: @escaping () -> Swift.Void)     class func preloadTextureAtlasesNamed(_ atlasNames: [String], withCompletionHandler completionHandler: @escaping (Error?, [SKTextureAtlas]) -> Swift.Void)     func preload(completionHandler completionHandler: @escaping () -> Swift.Void)     var textureNames: [String] { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKTextureAtlas : CVarArg { } extension SKTextureAtlas : CustomPlaygroundQuickLookable {     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } extension SKTextureAtlas : Equatable, Hashable {     var hashValue: Int { get } } extension SKTextureAtlas : CustomPlaygroundQuickLookable {     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } ``` | CVarArg, CustomPlaygroundQuickLookable, Equatable, Hashable, NSCoding |

Modified [SKTextureAtlas.init(dictionary: [String : Any])](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427383-atlaswithdictionary)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(dictionary properties: [String : AnyObject]) ``` |
| To | ``` convenience init(dictionary properties: [String : Any]) ``` |

Modified [SKTextureAtlas.preload(completionHandler: () -> Swift.Void)](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427385-preload)

|  | Declaration |
| --- | --- |
| From | ``` func preloadWithCompletionHandler(_ completionHandler: () -> Void) ``` |
| To | ``` func preload(completionHandler completionHandler: @escaping () -> Swift.Void) ``` |

Modified [SKTextureAtlas.preloadTextureAtlases(_: [SKTextureAtlas], withCompletionHandler: () -> Swift.Void) [class]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427379-preloadtextureatlases)

|  | Declaration |
| --- | --- |
| From | ``` class func preloadTextureAtlases(_ textureAtlases: [SKTextureAtlas], withCompletionHandler completionHandler: () -> Void) ``` |
| To | ``` class func preloadTextureAtlases(_ textureAtlases: [SKTextureAtlas], withCompletionHandler completionHandler: @escaping () -> Swift.Void) ``` |

Modified [SKTextureAtlas.preloadTextureAtlasesNamed(_: [String], withCompletionHandler: (Error?, [SKTextureAtlas]) -> Swift.Void) [class]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427377-preloadtextureatlasesnamed)

|  | Declaration |
| --- | --- |
| From | ``` class func preloadTextureAtlasesNamed(_ atlasNames: [String], withCompletionHandler completionHandler: (NSError?, [SKTextureAtlas]) -> Void) ``` |
| To | ``` class func preloadTextureAtlasesNamed(_ atlasNames: [String], withCompletionHandler completionHandler: @escaping (Error?, [SKTextureAtlas]) -> Swift.Void) ``` |

Modified [SKTextureFilteringMode [enum]](https://developer.apple.com/documentation/spritekit/sktexturefilteringmode)

|  | Declaration |
| --- | --- |
| From | ``` enum SKTextureFilteringMode : Int {     case Nearest     case Linear } ``` |
| To | ``` enum SKTextureFilteringMode : Int {     case nearest     case linear } ``` |

Modified [SKTextureFilteringMode.linear](https://developer.apple.com/documentation/spritekit/sktexturefilteringmode/linear)

|  | Declaration |
| --- | --- |
| From | ``` case Linear ``` |
| To | ``` case linear ``` |

Modified [SKTextureFilteringMode.nearest](https://developer.apple.com/documentation/spritekit/sktexturefilteringmode/nearest)

|  | Declaration |
| --- | --- |
| From | ``` case Nearest ``` |
| To | ``` case nearest ``` |

Modified [SKTransition](https://developer.apple.com/documentation/spritekit/sktransition)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKTransition : NSObject, NSCopying {     class func crossFadeWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func fadeWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func fadeWithColor(_ color: UIColor, duration sec: NSTimeInterval) -> SKTransition     class func flipHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func flipVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func revealWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition     class func moveInWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition     class func pushWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition     class func doorsOpenHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func doorsOpenVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func doorsCloseHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func doorsCloseVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition     class func doorwayWithDuration(_ sec: NSTimeInterval) -> SKTransition      init(CIFilter filter: CIFilter, duration sec: NSTimeInterval)     class func transitionWithCIFilter(_ filter: CIFilter, duration sec: NSTimeInterval) -> SKTransition     var pausesIncomingScene: Bool     var pausesOutgoingScene: Bool } ``` | NSCopying |
| To | ``` class SKTransition : NSObject, NSCopying {     class func crossFade(withDuration sec: TimeInterval) -> SKTransition     class func fade(withDuration sec: TimeInterval) -> SKTransition     class func fade(with color: UIColor, duration sec: TimeInterval) -> SKTransition     class func flipHorizontal(withDuration sec: TimeInterval) -> SKTransition     class func flipVertical(withDuration sec: TimeInterval) -> SKTransition     class func reveal(with direction: SKTransitionDirection, duration sec: TimeInterval) -> SKTransition     class func moveIn(with direction: SKTransitionDirection, duration sec: TimeInterval) -> SKTransition     class func push(with direction: SKTransitionDirection, duration sec: TimeInterval) -> SKTransition     class func doorsOpenHorizontal(withDuration sec: TimeInterval) -> SKTransition     class func doorsOpenVertical(withDuration sec: TimeInterval) -> SKTransition     class func doorsCloseHorizontal(withDuration sec: TimeInterval) -> SKTransition     class func doorsCloseVertical(withDuration sec: TimeInterval) -> SKTransition     class func doorway(withDuration sec: TimeInterval) -> SKTransition      init(ciFilter filter: CIFilter, duration sec: TimeInterval)     class func withCIFilter(_ filter: CIFilter, duration sec: TimeInterval) -> SKTransition     var pausesIncomingScene: Bool     var pausesOutgoingScene: Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKTransition : CVarArg { } extension SKTransition : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [SKTransition.crossFade(withDuration: TimeInterval) -> SKTransition [class]](https://developer.apple.com/documentation/spritekit/sktransition/1395897-crossfadewithduration)

|  | Declaration |
| --- | --- |
| From | ``` class func crossFadeWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |
| To | ``` class func crossFade(withDuration sec: TimeInterval) -> SKTransition ``` |

Modified [SKTransition.doorsCloseHorizontal(withDuration: TimeInterval) -> SKTransition [class]](https://developer.apple.com/documentation/spritekit/sktransition/1395899-doorsclosehorizontal)

|  | Declaration |
| --- | --- |
| From | ``` class func doorsCloseHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |
| To | ``` class func doorsCloseHorizontal(withDuration sec: TimeInterval) -> SKTransition ``` |

Modified [SKTransition.doorsCloseVertical(withDuration: TimeInterval) -> SKTransition [class]](https://developer.apple.com/documentation/spritekit/sktransition/1395914-doorscloseverticalwithduration)

|  | Declaration |
| --- | --- |
| From | ``` class func doorsCloseVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |
| To | ``` class func doorsCloseVertical(withDuration sec: TimeInterval) -> SKTransition ``` |

Modified [SKTransition.doorsOpenHorizontal(withDuration: TimeInterval) -> SKTransition [class]](https://developer.apple.com/documentation/spritekit/sktransition/1395875-doorsopenhorizontal)

|  | Declaration |
| --- | --- |
| From | ``` class func doorsOpenHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |
| To | ``` class func doorsOpenHorizontal(withDuration sec: TimeInterval) -> SKTransition ``` |

Modified [SKTransition.doorsOpenVertical(withDuration: TimeInterval) -> SKTransition [class]](https://developer.apple.com/documentation/spritekit/sktransition/1395909-doorsopenvertical)

|  | Declaration |
| --- | --- |
| From | ``` class func doorsOpenVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |
| To | ``` class func doorsOpenVertical(withDuration sec: TimeInterval) -> SKTransition ``` |

Modified [SKTransition.doorway(withDuration: TimeInterval) -> SKTransition [class]](https://developer.apple.com/documentation/spritekit/sktransition/1395881-doorwaywithduration)

|  | Declaration |
| --- | --- |
| From | ``` class func doorwayWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |
| To | ``` class func doorway(withDuration sec: TimeInterval) -> SKTransition ``` |

Modified [SKTransition.fade(with: UIColor, duration: TimeInterval) -> SKTransition [class]](https://developer.apple.com/documentation/spritekit/sktransition/1395871-fade)

|  | Declaration |
| --- | --- |
| From | ``` class func fadeWithColor(_ color: UIColor, duration sec: NSTimeInterval) -> SKTransition ``` |
| To | ``` class func fade(with color: UIColor, duration sec: TimeInterval) -> SKTransition ``` |

Modified [SKTransition.fade(withDuration: TimeInterval) -> SKTransition [class]](https://developer.apple.com/documentation/spritekit/sktransition/1395907-fade)

|  | Declaration |
| --- | --- |
| From | ``` class func fadeWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |
| To | ``` class func fade(withDuration sec: TimeInterval) -> SKTransition ``` |

Modified [SKTransition.flipHorizontal(withDuration: TimeInterval) -> SKTransition [class]](https://developer.apple.com/documentation/spritekit/sktransition/1395901-fliphorizontalwithduration)

|  | Declaration |
| --- | --- |
| From | ``` class func flipHorizontalWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |
| To | ``` class func flipHorizontal(withDuration sec: TimeInterval) -> SKTransition ``` |

Modified [SKTransition.flipVertical(withDuration: TimeInterval) -> SKTransition [class]](https://developer.apple.com/documentation/spritekit/sktransition/1395889-flipvertical)

|  | Declaration |
| --- | --- |
| From | ``` class func flipVerticalWithDuration(_ sec: NSTimeInterval) -> SKTransition ``` |
| To | ``` class func flipVertical(withDuration sec: TimeInterval) -> SKTransition ``` |

Modified [SKTransition.init(ciFilter: CIFilter, duration: TimeInterval)](https://developer.apple.com/documentation/spritekit/sktransition/1395895-init)

|  | Declaration |
| --- | --- |
| From | ``` init(CIFilter filter: CIFilter, duration sec: NSTimeInterval) ``` |
| To | ``` init(ciFilter filter: CIFilter, duration sec: TimeInterval) ``` |

Modified [SKTransition.moveIn(with: SKTransitionDirection, duration: TimeInterval) -> SKTransition [class]](https://developer.apple.com/documentation/spritekit/sktransition/1395905-movein)

|  | Declaration |
| --- | --- |
| From | ``` class func moveInWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition ``` |
| To | ``` class func moveIn(with direction: SKTransitionDirection, duration sec: TimeInterval) -> SKTransition ``` |

Modified [SKTransition.push(with: SKTransitionDirection, duration: TimeInterval) -> SKTransition [class]](https://developer.apple.com/documentation/spritekit/sktransition/1395903-push)

|  | Declaration |
| --- | --- |
| From | ``` class func pushWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition ``` |
| To | ``` class func push(with direction: SKTransitionDirection, duration sec: TimeInterval) -> SKTransition ``` |

Modified [SKTransition.reveal(with: SKTransitionDirection, duration: TimeInterval) -> SKTransition [class]](https://developer.apple.com/documentation/spritekit/sktransition/1395887-reveal)

|  | Declaration |
| --- | --- |
| From | ``` class func revealWithDirection(_ direction: SKTransitionDirection, duration sec: NSTimeInterval) -> SKTransition ``` |
| To | ``` class func reveal(with direction: SKTransitionDirection, duration sec: TimeInterval) -> SKTransition ``` |

Modified [SKTransitionDirection [enum]](https://developer.apple.com/documentation/spritekit/sktransitiondirection)

|  | Declaration |
| --- | --- |
| From | ``` enum SKTransitionDirection : Int {     case Up     case Down     case Right     case Left } ``` |
| To | ``` enum SKTransitionDirection : Int {     case up     case down     case right     case left } ``` |

Modified [SKTransitionDirection.down](https://developer.apple.com/documentation/spritekit/sktransitiondirection/down)

|  | Declaration |
| --- | --- |
| From | ``` case Down ``` |
| To | ``` case down ``` |

Modified [SKTransitionDirection.left](https://developer.apple.com/documentation/spritekit/sktransitiondirection/left)

|  | Declaration |
| --- | --- |
| From | ``` case Left ``` |
| To | ``` case left ``` |

Modified [SKTransitionDirection.right](https://developer.apple.com/documentation/spritekit/sktransitiondirection/right)

|  | Declaration |
| --- | --- |
| From | ``` case Right ``` |
| To | ``` case right ``` |

Modified [SKTransitionDirection.up](https://developer.apple.com/documentation/spritekit/sktransitiondirection/up)

|  | Declaration |
| --- | --- |
| From | ``` case Up ``` |
| To | ``` case up ``` |

Modified [SKUniform](https://developer.apple.com/documentation/spritekit/skuniform)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKUniform : NSObject, NSCopying, NSCoding {     convenience init(name name: String)     class func uniformWithName(_ name: String) -> Self     convenience init(name name: String, texture texture: SKTexture)     class func uniformWithName(_ name: String, texture texture: SKTexture) -> Self     convenience init(name name: String, float value: Float)     class func uniformWithName(_ name: String, float value: Float) -> Self     convenience init(name name: String, floatVector2 value: GLKVector2)     class func uniformWithName(_ name: String, floatVector2 value: GLKVector2) -> Self     convenience init(name name: String, floatVector3 value: GLKVector3)     class func uniformWithName(_ name: String, floatVector3 value: GLKVector3) -> Self     convenience init(name name: String, floatVector4 value: GLKVector4)     class func uniformWithName(_ name: String, floatVector4 value: GLKVector4) -> Self     convenience init(name name: String, floatMatrix2 value: GLKMatrix2)     class func uniformWithName(_ name: String, floatMatrix2 value: GLKMatrix2) -> Self     convenience init(name name: String, floatMatrix3 value: GLKMatrix3)     class func uniformWithName(_ name: String, floatMatrix3 value: GLKMatrix3) -> Self     convenience init(name name: String, floatMatrix4 value: GLKMatrix4)     class func uniformWithName(_ name: String, floatMatrix4 value: GLKMatrix4) -> Self     var name: String { get }     var uniformType: SKUniformType { get }     var textureValue: SKTexture?     var floatValue: Float     var floatVector2Value: GLKVector2     var floatVector3Value: GLKVector3     var floatVector4Value: GLKVector4     var floatMatrix2Value: GLKMatrix2     var floatMatrix3Value: GLKMatrix3     var floatMatrix4Value: GLKMatrix4     init(name name: String)     init(name name: String, texture texture: SKTexture?)     init(name name: String, float value: Float)     init(name name: String, floatVector2 value: GLKVector2)     init(name name: String, floatVector3 value: GLKVector3)     init(name name: String, floatVector4 value: GLKVector4)     init(name name: String, floatMatrix2 value: GLKMatrix2)     init(name name: String, floatMatrix3 value: GLKMatrix3)     init(name name: String, floatMatrix4 value: GLKMatrix4) } ``` | NSCoding, NSCopying |
| To | ``` class SKUniform : NSObject, NSCopying, NSCoding {     convenience init(name name: String)     class func withName(_ name: String) -> Self     convenience init(name name: String, texture texture: SKTexture?)     class func withName(_ name: String, texture texture: SKTexture?) -> Self     convenience init(name name: String, float value: Float)     class func withName(_ name: String, float value: Float) -> Self     convenience init(name name: String, vectorFloat2 value: vector_float2)     class func withName(_ name: String, vectorFloat2 value: vector_float2) -> Self     convenience init(name name: String, vectorFloat3 value: vector_float3)     class func withName(_ name: String, vectorFloat3 value: vector_float3) -> Self     convenience init(name name: String, vectorFloat4 value: vector_float4)     class func withName(_ name: String, vectorFloat4 value: vector_float4) -> Self     convenience init(name name: String, matrixFloat2x2 value: matrix_float2x2)     class func withName(_ name: String, matrixFloat2x2 value: matrix_float2x2) -> Self     convenience init(name name: String, matrixFloat3x3 value: matrix_float3x3)     class func withName(_ name: String, matrixFloat3x3 value: matrix_float3x3) -> Self     convenience init(name name: String, matrixFloat4x4 value: matrix_float4x4)     class func withName(_ name: String, matrixFloat4x4 value: matrix_float4x4) -> Self     var name: String { get }     var uniformType: SKUniformType { get }     var textureValue: SKTexture?     var floatValue: Float     var vectorFloat2Value: vector_float2     var vectorFloat3Value: vector_float3     var vectorFloat4Value: vector_float4     var matrixFloat2x2Value: matrix_float2x2     var matrixFloat3x3Value: matrix_float3x3     var matrixFloat4x4Value: matrix_float4x4     init(name name: String)     init(name name: String, texture texture: SKTexture?)     init(name name: String, float value: Float)     init(name name: String, vectorFloat2 value: vector_float2)     init(name name: String, vectorFloat3 value: vector_float3)     init(name name: String, vectorFloat4 value: vector_float4)     init(name name: String, matrixFloat2x2 value: matrix_float2x2)     init(name name: String, matrixFloat3x3 value: matrix_float3x3)     init(name name: String, matrixFloat4x4 value: matrix_float4x4)     var floatVector2Value: GLKVector2     var floatVector3Value: GLKVector3     var floatVector4Value: GLKVector4     var floatMatrix2Value: GLKMatrix2     var floatMatrix3Value: GLKMatrix3     var floatMatrix4Value: GLKMatrix4     convenience init(name name: String, float value: GLKVector2)     class func withName(_ name: String, float value: GLKVector2) -> Self     convenience init(name name: String, float value: GLKVector3)     class func withName(_ name: String, float value: GLKVector3) -> Self     convenience init(name name: String, float value: GLKVector4)     class func withName(_ name: String, float value: GLKVector4) -> Self     convenience init(name name: String, float value: GLKMatrix2)     class func withName(_ name: String, float value: GLKMatrix2) -> Self     convenience init(name name: String, float value: GLKMatrix3)     class func withName(_ name: String, float value: GLKMatrix3) -> Self     convenience init(name name: String, float value: GLKMatrix4)     class func withName(_ name: String, float value: GLKMatrix4) -> Self     init(name name: String, float value: GLKVector2)     init(name name: String, float value: GLKVector3)     init(name name: String, float value: GLKVector4)     init(name name: String, float value: GLKMatrix2)     init(name name: String, float value: GLKMatrix3)     init(name name: String, float value: GLKMatrix4)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKUniform : CVarArg { } extension SKUniform : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying |

Modified [SKUniform.floatMatrix2Value](https://developer.apple.com/documentation/spritekit/skuniform/1455410-floatmatrix2value)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.3 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.floatMatrix3Value](https://developer.apple.com/documentation/spritekit/skuniform/1455438-floatmatrix3value)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.3 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.floatMatrix4Value](https://developer.apple.com/documentation/spritekit/skuniform/1455460-floatmatrix4value)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.3 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.floatVector2Value](https://developer.apple.com/documentation/spritekit/skuniform/1455436-floatvector2value)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.3 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.floatVector3Value](https://developer.apple.com/documentation/spritekit/skuniform/1455434-floatvector3value)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.3 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.floatVector4Value](https://developer.apple.com/documentation/spritekit/skuniform/1455404-floatvector4value)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.3 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.init(name: String, float: GLKVector3)](https://developer.apple.com/documentation/spritekit/skuniform/1455416-initwithname)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(name name: String, floatVector3 value: GLKVector3) ``` | iOS 8.3 | -- |
| To | ``` init(name name: String, float value: GLKVector3) ``` | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.init(name: String, float: GLKMatrix2)](https://developer.apple.com/documentation/spritekit/skuniform/1455431-initwithname)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(name name: String, floatMatrix2 value: GLKMatrix2) ``` | iOS 8.3 | -- |
| To | ``` init(name name: String, float value: GLKMatrix2) ``` | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.init(name: String, float: GLKMatrix4)](https://developer.apple.com/documentation/spritekit/skuniform/1455429-init)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(name name: String, floatMatrix4 value: GLKMatrix4) ``` | iOS 8.3 | -- |
| To | ``` init(name name: String, float value: GLKMatrix4) ``` | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.init(name: String, float: GLKVector2)](https://developer.apple.com/documentation/spritekit/skuniform/1455444-initwithname)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(name name: String, floatVector2 value: GLKVector2) ``` | iOS 8.3 | -- |
| To | ``` init(name name: String, float value: GLKVector2) ``` | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.init(name: String, float: GLKVector4)](https://developer.apple.com/documentation/spritekit/skuniform/1455418-initwithname)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(name name: String, floatVector4 value: GLKVector4) ``` | iOS 8.3 | -- |
| To | ``` init(name name: String, float value: GLKVector4) ``` | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.init(name: String, float: GLKMatrix3)](https://developer.apple.com/documentation/spritekit/skuniform/1455462-init)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(name name: String, floatMatrix3 value: GLKMatrix3) ``` | iOS 8.3 | -- |
| To | ``` init(name name: String, float value: GLKMatrix3) ``` | iOS 7.0 | iOS 10.0 |

Modified [SKUniformType [enum]](https://developer.apple.com/documentation/spritekit/skuniformtype)

|  | Declaration |
| --- | --- |
| From | ``` enum SKUniformType : Int {     case None     case Float     case FloatVector2     case FloatVector3     case FloatVector4     case FloatMatrix2     case FloatMatrix3     case FloatMatrix4     case Texture } ``` |
| To | ``` enum SKUniformType : Int {     case none     case float     case floatVector2     case floatVector3     case floatVector4     case floatMatrix2     case floatMatrix3     case floatMatrix4     case texture } ``` |

Modified [SKUniformType.float](https://developer.apple.com/documentation/spritekit/skuniformtype/float)

|  | Declaration |
| --- | --- |
| From | ``` case Float ``` |
| To | ``` case float ``` |

Modified [SKUniformType.floatMatrix2](https://developer.apple.com/documentation/spritekit/skuniformtype/floatmatrix2)

|  | Declaration |
| --- | --- |
| From | ``` case FloatMatrix2 ``` |
| To | ``` case floatMatrix2 ``` |

Modified [SKUniformType.floatMatrix3](https://developer.apple.com/documentation/spritekit/skuniformtype/floatmatrix3)

|  | Declaration |
| --- | --- |
| From | ``` case FloatMatrix3 ``` |
| To | ``` case floatMatrix3 ``` |

Modified [SKUniformType.floatMatrix4](https://developer.apple.com/documentation/spritekit/skuniformtype/floatmatrix4)

|  | Declaration |
| --- | --- |
| From | ``` case FloatMatrix4 ``` |
| To | ``` case floatMatrix4 ``` |

Modified [SKUniformType.floatVector2](https://developer.apple.com/documentation/spritekit/skuniformtype/floatvector2)

|  | Declaration |
| --- | --- |
| From | ``` case FloatVector2 ``` |
| To | ``` case floatVector2 ``` |

Modified [SKUniformType.floatVector3](https://developer.apple.com/documentation/spritekit/skuniformtype/skuniformtypefloatvector3)

|  | Declaration |
| --- | --- |
| From | ``` case FloatVector3 ``` |
| To | ``` case floatVector3 ``` |

Modified [SKUniformType.floatVector4](https://developer.apple.com/documentation/spritekit/skuniformtype/skuniformtypefloatvector4)

|  | Declaration |
| --- | --- |
| From | ``` case FloatVector4 ``` |
| To | ``` case floatVector4 ``` |

Modified [SKUniformType.none](https://developer.apple.com/documentation/spritekit/skuniformtype/skuniformtypenone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [SKUniformType.texture](https://developer.apple.com/documentation/spritekit/skuniformtype/texture)

|  | Declaration |
| --- | --- |
| From | ``` case Texture ``` |
| To | ``` case texture ``` |

Modified [SKVideoNode](https://developer.apple.com/documentation/spritekit/skvideonode)

|  | Declaration |
| --- | --- |
| From | ``` class SKVideoNode : SKNode {      init(AVPlayer player: AVPlayer)     class func videoNodeWithAVPlayer(_ player: AVPlayer) -> SKVideoNode      init(videoFileNamed videoFile: String)     class func videoNodeWithVideoFileNamed(_ videoFile: String) -> SKVideoNode      init(fileNamed videoFile: String)     class func videoNodeWithFileNamed(_ videoFile: String) -> SKVideoNode      init(videoURL videoURL: NSURL)     class func videoNodeWithVideoURL(_ videoURL: NSURL) -> SKVideoNode      init(URL videoURL: NSURL)     class func videoNodeWithURL(_ videoURL: NSURL) -> SKVideoNode     init(AVPlayer player: AVPlayer)     init(videoFileNamed videoFile: String)     init(fileNamed videoFile: String)     init(videoURL url: NSURL)     init(URL url: NSURL)     init?(coder aDecoder: NSCoder)     func play()     func pause()     var size: CGSize     var anchorPoint: CGPoint } ``` |
| To | ``` class SKVideoNode : SKNode {      init(avPlayer player: AVPlayer)     class func withAVPlayer(_ player: AVPlayer) -> SKVideoNode      init(videoFileNamed videoFile: String)     class func withVideoFileNamed(_ videoFile: String) -> SKVideoNode      init(fileNamed videoFile: String)     class func withFileNamed(_ videoFile: String) -> SKVideoNode      init(videoURL videoURL: URL)     class func withVideoURL(_ videoURL: URL) -> SKVideoNode      init(url videoURL: URL)     class func withURL(_ videoURL: URL) -> SKVideoNode     init(avPlayer player: AVPlayer)     init(videoFileNamed videoFile: String)     init(fileNamed videoFile: String)     init(videoURL url: URL)     init(url url: URL)     init?(coder aDecoder: NSCoder)     func play()     func pause()     var size: CGSize     var anchorPoint: CGPoint } ``` |

Modified [SKVideoNode.init(avPlayer: AVPlayer)](https://developer.apple.com/documentation/spritekit/skvideonode/1407900-initwithavplayer)

|  | Declaration |
| --- | --- |
| From | ``` init(AVPlayer player: AVPlayer) ``` |
| To | ``` init(avPlayer player: AVPlayer) ``` |

Modified [SKVideoNode.init(url: URL)](https://developer.apple.com/documentation/spritekit/skvideonode/1407898-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL) ``` |
| To | ``` init(url url: URL) ``` |

Modified [SKVideoNode.init(videoURL: URL)](https://developer.apple.com/documentation/spritekit/skvideonode/1407908-init)

|  | Declaration |
| --- | --- |
| From | ``` init(videoURL url: NSURL) ``` |
| To | ``` init(videoURL url: URL) ``` |

Modified [SKView](https://developer.apple.com/documentation/spritekit/skview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SKView : UIView {     var paused: Bool     var showsFPS: Bool     var showsDrawCount: Bool     var showsNodeCount: Bool     var showsQuadCount: Bool     var showsPhysics: Bool     var showsFields: Bool     var asynchronous: Bool     var allowsTransparency: Bool     var ignoresSiblingOrder: Bool     var shouldCullNonVisibleNodes: Bool     var frameInterval: Int     func presentScene(_ scene: SKScene?)     func presentScene(_ scene: SKScene, transition transition: SKTransition)     var scene: SKScene? { get }     func textureFromNode(_ node: SKNode) -> SKTexture?     func textureFromNode(_ node: SKNode, crop crop: CGRect) -> SKTexture?     func convertPoint(_ point: CGPoint, toScene scene: SKScene) -> CGPoint     func convertPoint(_ point: CGPoint, fromScene scene: SKScene) -> CGPoint } ``` | -- |
| To | ``` class SKView : UIView {     var isPaused: Bool     var showsFPS: Bool     var showsDrawCount: Bool     var showsNodeCount: Bool     var showsQuadCount: Bool     var showsPhysics: Bool     var showsFields: Bool     var isAsynchronous: Bool     var allowsTransparency: Bool     var ignoresSiblingOrder: Bool     var shouldCullNonVisibleNodes: Bool     var preferredFramesPerSecond: Int     weak var delegate: SKViewDelegate?     var frameInterval: Int     var preferredFrameRate: Float     func presentScene(_ scene: SKScene?)     func presentScene(_ scene: SKScene, transition transition: SKTransition)     var scene: SKScene? { get }     func texture(from node: SKNode) -> SKTexture?     func texture(from node: SKNode, crop crop: CGRect) -> SKTexture?     func convert(_ point: CGPoint, to scene: SKScene) -> CGPoint     func convert(_ point: CGPoint, from scene: SKScene) -> CGPoint     func viewPrintFormatter() -> UIViewPrintFormatter     func draw(_ rect: CGRect, for formatter: UIViewPrintFormatter)     func endEditing(_ force: Bool) -> Bool     func snapshotView(afterScreenUpdates afterUpdates: Bool) -> UIView?     func resizableSnapshotView(from rect: CGRect, afterScreenUpdates afterUpdates: Bool, withCapInsets capInsets: UIEdgeInsets) -> UIView?     func drawHierarchy(in rect: CGRect, afterScreenUpdates afterUpdates: Bool) -> Bool     var restorationIdentifier: String?     func encodeRestorableState(with coder: NSCoder)     func decodeRestorableState(with coder: NSCoder)     func constraintsAffectingLayout(for axis: UILayoutConstraintAxis) -> [NSLayoutConstraint]     var hasAmbiguousLayout: Bool { get }     func exerciseAmbiguityInLayout()     var leadingAnchor: NSLayoutXAxisAnchor { get }     var trailingAnchor: NSLayoutXAxisAnchor { get }     var leftAnchor: NSLayoutXAxisAnchor { get }     var rightAnchor: NSLayoutXAxisAnchor { get }     var topAnchor: NSLayoutYAxisAnchor { get }     var bottomAnchor: NSLayoutYAxisAnchor { get }     var widthAnchor: NSLayoutDimension { get }     var heightAnchor: NSLayoutDimension { get }     var centerXAnchor: NSLayoutXAxisAnchor { get }     var centerYAnchor: NSLayoutYAxisAnchor { get }     var firstBaselineAnchor: NSLayoutYAxisAnchor { get }     var lastBaselineAnchor: NSLayoutYAxisAnchor { get }     var layoutGuides: [UILayoutGuide] { get }     func addLayoutGuide(_ layoutGuide: UILayoutGuide)     func removeLayoutGuide(_ layoutGuide: UILayoutGuide)     func systemLayoutSizeFitting(_ targetSize: CGSize) -> CGSize     func systemLayoutSizeFitting(_ targetSize: CGSize, withHorizontalFittingPriority horizontalFittingPriority: UILayoutPriority, verticalFittingPriority verticalFittingPriority: UILayoutPriority) -> CGSize     func alignmentRect(forFrame frame: CGRect) -> CGRect     func frame(forAlignmentRect alignmentRect: CGRect) -> CGRect     var alignmentRectInsets: UIEdgeInsets { get }     func forBaselineLayout() -> UIView     var forFirstBaselineLayout: UIView { get }     var forLastBaselineLayout: UIView { get }     var intrinsicContentSize: CGSize { get }     func invalidateIntrinsicContentSize()     func contentHuggingPriority(for axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentHuggingPriority(_ priority: UILayoutPriority, for axis: UILayoutConstraintAxis)     func contentCompressionResistancePriority(for axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentCompressionResistancePriority(_ priority: UILayoutPriority, for axis: UILayoutConstraintAxis)     var translatesAutoresizingMaskIntoConstraints: Bool     class var requiresConstraintBasedLayout: Bool { get }     func updateConstraintsIfNeeded()     func updateConstraints()     func needsUpdateConstraints() -> Bool     func setNeedsUpdateConstraints()     var constraints: [NSLayoutConstraint] { get }     func addConstraint(_ constraint: NSLayoutConstraint)     func addConstraints(_ constraints: [NSLayoutConstraint])     func removeConstraint(_ constraint: NSLayoutConstraint)     func removeConstraints(_ constraints: [NSLayoutConstraint])     func addMotionEffect(_ effect: UIMotionEffect)     func removeMotionEffect(_ effect: UIMotionEffect)     var motionEffects: [UIMotionEffect]     var gestureRecognizers: [UIGestureRecognizer]?     func addGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func removeGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool     class func animateKeyframes(withDuration duration: TimeInterval, delay delay: TimeInterval, options options: UIViewKeyframeAnimationOptions = [], animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func addKeyframe(withRelativeStartTime frameStartTime: Double, relativeDuration frameDuration: Double, animations animations: @escaping () -> Void)     class func animate(withDuration duration: TimeInterval, delay delay: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func animate(withDuration duration: TimeInterval, animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func animate(withDuration duration: TimeInterval, animations animations: @escaping () -> Void)     class func animate(withDuration duration: TimeInterval, delay delay: TimeInterval, usingSpringWithDamping dampingRatio: CGFloat, initialSpringVelocity velocity: CGFloat, options options: UIViewAnimationOptions = [], animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func transition(with view: UIView, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     class func transition(from fromView: UIView, to toView: UIView, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], completion completion: (@escaping (Bool) -> Void)? = nil)     class func perform(_ animation: UISystemAnimation, on views: [UIView], options options: UIViewAnimationOptions = [], animations parallelAnimations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     class func beginAnimations(_ animationID: String?, context context: UnsafeMutableRawPointer?)     class func commitAnimations()     class func setAnimationDelegate(_ delegate: Any?)     class func setAnimationWillStart(_ selector: Selector?)     class func setAnimationDidStop(_ selector: Selector?)     class func setAnimationDuration(_ duration: TimeInterval)     class func setAnimationDelay(_ delay: TimeInterval)     class func setAnimationStart(_ startDate: Date)     class func setAnimationCurve(_ curve: UIViewAnimationCurve)     class func setAnimationRepeatCount(_ repeatCount: Float)     class func setAnimationRepeatAutoreverses(_ repeatAutoreverses: Bool)     class func setAnimationBeginsFromCurrentState(_ fromCurrentState: Bool)     class func setAnimationTransition(_ transition: UIViewAnimationTransition, for view: UIView, cache cache: Bool)     class func setAnimationsEnabled(_ enabled: Bool)     class var areAnimationsEnabled: Bool { get }     class func performWithoutAnimation(_ actionsWithoutAnimation: () -> Void)     class var inheritedAnimationDuration: TimeInterval { get }     func draw(_ rect: CGRect)     func setNeedsDisplay()     func setNeedsDisplay(_ rect: CGRect)     var clipsToBounds: Bool     @NSCopying var backgroundColor: UIColor?     var alpha: CGFloat     var isOpaque: Bool     var clearsContextBeforeDrawing: Bool     var isHidden: Bool     var contentMode: UIViewContentMode     var contentStretch: CGRect     var mask: UIView?     var tintColor: UIColor!     var tintAdjustmentMode: UIViewTintAdjustmentMode     func tintColorDidChange()     var superview: UIView? { get }     var subviews: [UIView] { get }     var window: UIWindow? { get }     func removeFromSuperview()     func insertSubview(_ view: UIView, at index: Int)     func exchangeSubview(at index1: Int, withSubviewAt index2: Int)     func addSubview(_ view: UIView)     func insertSubview(_ view: UIView, belowSubview siblingSubview: UIView)     func insertSubview(_ view: UIView, aboveSubview siblingSubview: UIView)     func bringSubview(toFront view: UIView)     func sendSubview(toBack view: UIView)     func didAddSubview(_ subview: UIView)     func willRemoveSubview(_ subview: UIView)     func willMove(toSuperview newSuperview: UIView?)     func didMoveToSuperview()     func willMove(toWindow newWindow: UIWindow?)     func didMoveToWindow()     func isDescendant(of view: UIView) -> Bool     func viewWithTag(_ tag: Int) -> UIView?     func setNeedsLayout()     func layoutIfNeeded()     func layoutSubviews()     var layoutMargins: UIEdgeInsets     var preservesSuperviewLayoutMargins: Bool     func layoutMarginsDidChange()     var layoutMarginsGuide: UILayoutGuide { get }     var readableContentGuide: UILayoutGuide { get }     var frame: CGRect     var bounds: CGRect     var center: CGPoint     var transform: CGAffineTransform     var contentScaleFactor: CGFloat     var isMultipleTouchEnabled: Bool     var isExclusiveTouch: Bool     func hitTest(_ point: CGPoint, with event: UIEvent?) -> UIView?     func point(inside point: CGPoint, with event: UIEvent?) -> Bool     func convert(_ point: CGPoint, to view: UIView?) -> CGPoint     func convert(_ point: CGPoint, from view: UIView?) -> CGPoint     func convert(_ rect: CGRect, to view: UIView?) -> CGRect     func convert(_ rect: CGRect, from view: UIView?) -> CGRect     var autoresizesSubviews: Bool     var autoresizingMask: UIViewAutoresizing     func sizeThatFits(_ size: CGSize) -> CGSize     func sizeToFit()     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity)     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews()     var keyCommands: [UIKeyCommand]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension SKView : UIAccessibilityIdentification { } extension SKView : CVarArg { } extension SKView : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, UIAccessibilityIdentification |

Modified [SKView.convert(_: CGPoint, from: SKScene) -> CGPoint](https://developer.apple.com/documentation/spritekit/skview/1520328-convert)

|  | Declaration |
| --- | --- |
| From | ``` func convertPoint(_ point: CGPoint, fromScene scene: SKScene) -> CGPoint ``` |
| To | ``` func convert(_ point: CGPoint, from scene: SKScene) -> CGPoint ``` |

Modified [SKView.convert(_: CGPoint, to: SKScene) -> CGPoint](https://developer.apple.com/documentation/spritekit/skview/1519847-convertpoint)

|  | Declaration |
| --- | --- |
| From | ``` func convertPoint(_ point: CGPoint, toScene scene: SKScene) -> CGPoint ``` |
| To | ``` func convert(_ point: CGPoint, to scene: SKScene) -> CGPoint ``` |

Modified [SKView.frameInterval](https://developer.apple.com/documentation/spritekit/skview/1520008-frameinterval)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [SKView.isAsynchronous](https://developer.apple.com/documentation/spritekit/skview/1520229-asynchronous)

|  | Declaration |
| --- | --- |
| From | ``` var asynchronous: Bool ``` |
| To | ``` var isAsynchronous: Bool ``` |

Modified [SKView.isPaused](https://developer.apple.com/documentation/spritekit/skview/1519654-ispaused)

|  | Declaration |
| --- | --- |
| From | ``` var paused: Bool ``` |
| To | ``` var isPaused: Bool ``` |

Modified [SKView.texture(from: SKNode) -> SKTexture?](https://developer.apple.com/documentation/spritekit/skview/1520114-texture)

|  | Declaration |
| --- | --- |
| From | ``` func textureFromNode(_ node: SKNode) -> SKTexture? ``` |
| To | ``` func texture(from node: SKNode) -> SKTexture? ``` |

Modified [SKView.texture(from: SKNode, crop: CGRect) -> SKTexture?](https://developer.apple.com/documentation/spritekit/skview/1519994-texturefromnode)

|  | Declaration |
| --- | --- |
| From | ``` func textureFromNode(_ node: SKNode, crop crop: CGRect) -> SKTexture? ``` |
| To | ``` func texture(from node: SKNode, crop crop: CGRect) -> SKTexture? ``` |

Modified [UITouch.location(in: SKNode) -> CGPoint](https://developer.apple.com/documentation/uikit/uitouch/1614836-location)

|  | Declaration |
| --- | --- |
| From | ``` func locationInNode(_ node: SKNode) -> CGPoint ``` |
| To | ``` func location(in node: SKNode) -> CGPoint ``` |

Modified [UITouch.previousLocation(in: SKNode) -> CGPoint](https://developer.apple.com/documentation/uikit/uitouch/1615023-previouslocation)

|  | Declaration |
| --- | --- |
| From | ``` func previousLocationInNode(_ node: SKNode) -> CGPoint ``` |
| To | ``` func previousLocation(in node: SKNode) -> CGPoint ``` |

Modified [SKFieldForceEvaluator](https://developer.apple.com/documentation/spritekit/skfieldforceevaluator)

|  | Declaration |
| --- | --- |
| From | ``` typealias SKFieldForceEvaluator = (vector_float3, vector_float3, Float, Float, NSTimeInterval) -> vector_float3 ``` |
| To | ``` typealias SKFieldForceEvaluator = (vector_float3, vector_float3, Float, Float, TimeInterval) -> vector_float3 ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
