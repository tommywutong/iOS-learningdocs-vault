---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/SpriteKit.html
archived_at: '2026-07-18T02:54:59.045152Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# SpriteKit Changes for Objective-C

### SpriteKit

#### SKAction.h

Added [+[SKAction scaleToSize:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1643619-scaletosize)

#### SKAttribute.h (Added)

Added [SKAttribute](https://developer.apple.com/documentation/spritekit/skattribute)Added [+[SKAttribute attributeWithName:type:]](https://developer.apple.com/documentation/spritekit/skattribute/1643426-attributewithname)Added [-[SKAttribute initWithName:type:]](https://developer.apple.com/documentation/spritekit/skattribute/1643431-initwithname)Added [SKAttribute.name](https://developer.apple.com/documentation/spritekit/skattribute/1643444-name)Added [SKAttribute.type](https://developer.apple.com/documentation/spritekit/skattribute/1643432-type)Added [SKAttributeValue](https://developer.apple.com/documentation/spritekit/skattributevalue)Added [SKAttributeValue.floatValue](https://developer.apple.com/documentation/spritekit/skattributevalue/1643424-floatvalue)Added [-[SKAttributeValue init]](https://developer.apple.com/documentation/spritekit/skattributevalue/1643441-init)Added [+[SKAttributeValue valueWithFloat:]](https://developer.apple.com/documentation/spritekit/skattributevalue/1643428-init)Added [+[SKAttributeValue valueWithVectorFloat2:]](https://developer.apple.com/documentation/spritekit/skattributevalue/1643427-init)Added [+[SKAttributeValue valueWithVectorFloat3:]](https://developer.apple.com/documentation/spritekit/skattributevalue/1643421-init)Added [+[SKAttributeValue valueWithVectorFloat4:]](https://developer.apple.com/documentation/spritekit/skattributevalue/1643436-valuewithvectorfloat4)Added [SKAttributeValue.vectorFloat2Value](https://developer.apple.com/documentation/spritekit/skattributevalue/1643435-vectorfloat2value)Added [SKAttributeValue.vectorFloat3Value](https://developer.apple.com/documentation/spritekit/skattributevalue/1643434-vectorfloat3value)Added [SKAttributeValue.vectorFloat4Value](https://developer.apple.com/documentation/spritekit/skattributevalue/1643442-vectorfloat4value)Added [SKAttributeType](https://developer.apple.com/documentation/spritekit/skattributetype)Added [SKAttributeTypeFloat](https://developer.apple.com/documentation/spritekit/skattributetype/float)Added [SKAttributeTypeHalfFloat](https://developer.apple.com/documentation/spritekit/skattributetype/skattributetypehalffloat)Added [SKAttributeTypeNone](https://developer.apple.com/documentation/spritekit/skattributetype/none)Added [SKAttributeTypeVectorFloat2](https://developer.apple.com/documentation/spritekit/skattributetype/vectorfloat2)Added [SKAttributeTypeVectorFloat3](https://developer.apple.com/documentation/spritekit/skattributetype/vectorfloat3)Added [SKAttributeTypeVectorFloat4](https://developer.apple.com/documentation/spritekit/skattributetype/vectorfloat4)Added [SKAttributeTypeVectorHalfFloat2](https://developer.apple.com/documentation/spritekit/skattributetype/skattributetypevectorhalffloat2)Added [SKAttributeTypeVectorHalfFloat3](https://developer.apple.com/documentation/spritekit/skattributetype/skattributetypevectorhalffloat3)Added [SKAttributeTypeVectorHalfFloat4](https://developer.apple.com/documentation/spritekit/skattributetype/skattributetypevectorhalffloat4)

#### SKEffectNode.h

Modified [SKEffectNode](https://developer.apple.com/documentation/spritekit/skeffectnode)

|  | Protocols |
| --- | --- |
| From | -- |
| To | SKWarpable |

#### SKNode.h

Added [SKNode.attributeValues](https://developer.apple.com/documentation/spritekit/sknode/1644181-attributevalues)Added [-[SKNode setValue:forAttributeNamed:]](https://developer.apple.com/documentation/spritekit/sknode/1644180-setvalue)Added [-[SKNode valueForAttributeNamed:]](https://developer.apple.com/documentation/spritekit/sknode/1644182-value)Modified [SKNode](https://developer.apple.com/documentation/spritekit/sknode)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCoding, NSCopying, UIFocusItem |

Modified [+[SKNode obstaclesFromNodeBounds:]](https://developer.apple.com/documentation/spritekit/sknode/1483132-obstacles)

|  | Header |
| --- | --- |
| From | SpriteKit/SKNode.h |
| To | GameplayKit/SpriteKit+Additions.h |

Modified [+[SKNode obstaclesFromNodePhysicsBodies:]](https://developer.apple.com/documentation/spritekit/sknode/1483085-obstaclesfromnodephysicsbodies)

|  | Header |
| --- | --- |
| From | SpriteKit/SKNode.h |
| To | GameplayKit/SpriteKit+Additions.h |

Modified [+[SKNode obstaclesFromSpriteTextures:accuracy:]](https://developer.apple.com/documentation/spritekit/sknode/1483134-obstaclesfromspritetextures)

|  | Header |
| --- | --- |
| From | SpriteKit/SKNode.h |
| To | GameplayKit/SpriteKit+Additions.h |

#### SKScene.h

Added [-[SKScene sceneDidLoad]](https://developer.apple.com/documentation/spritekit/skscene/1645216-scenedidload)Modified [SKScene.delegate](https://developer.apple.com/documentation/spritekit/skscene/1520213-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<SKSceneDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak) id<SKSceneDelegate> delegate ``` |

#### SKShader.h

Added [SKShader.attributes](https://developer.apple.com/documentation/spritekit/skshader/1645287-attributes)

#### SKSpriteNode.h

Added [-[SKSpriteNode scaleToSize:]](https://developer.apple.com/documentation/spritekit/skspritenode/1645445-scaletosize)Modified [SKSpriteNode](https://developer.apple.com/documentation/spritekit/skspritenode)

|  | Protocols |
| --- | --- |
| From | -- |
| To | SKWarpable |

#### SKTileDefinition.h (Added)

Added [SKTileDefinition](https://developer.apple.com/documentation/spritekit/sktiledefinition)Added [SKTileDefinition.flipHorizontally](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645804-fliphorizontally)Added [SKTileDefinition.flipVertically](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645800-flipvertically)Added [-[SKTileDefinition initWithTexture:]](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645815-init)Added [-[SKTileDefinition initWithTexture:normalTexture:size:]](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645778-initwithtexture)Added [-[SKTileDefinition initWithTexture:size:]](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645787-initwithtexture)Added [-[SKTileDefinition initWithTextures:normalTextures:size:timePerFrame:]](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645814-init)Added [-[SKTileDefinition initWithTextures:size:timePerFrame:]](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645776-init)Added [SKTileDefinition.name](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645779-name)Added [SKTileDefinition.normalTextures](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645780-normaltextures)Added [SKTileDefinition.placementWeight](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645820-placementweight)Added [SKTileDefinition.rotation](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645775-rotation)Added [SKTileDefinition.size](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645790-size)Added [SKTileDefinition.textures](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645802-textures)Added [+[SKTileDefinition tileDefinitionWithTexture:]](https://developer.apple.com/documentation/spritekit/sktiledefinition/1646654-tiledefinitionwithtexture)Added [+[SKTileDefinition tileDefinitionWithTexture:normalTexture:size:]](https://developer.apple.com/documentation/spritekit/sktiledefinition/1646656-tiledefinitionwithtexture)Added [+[SKTileDefinition tileDefinitionWithTexture:size:]](https://developer.apple.com/documentation/spritekit/sktiledefinition/1646652-tiledefinitionwithtexture)Added [+[SKTileDefinition tileDefinitionWithTextures:normalTextures:size:timePerFrame:]](https://developer.apple.com/documentation/spritekit/sktiledefinition/1646655-tiledefinitionwithtextures)Added [+[SKTileDefinition tileDefinitionWithTextures:size:timePerFrame:]](https://developer.apple.com/documentation/spritekit/sktiledefinition/1646653-tiledefinitionwithtextures)Added [SKTileDefinition.timePerFrame](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645811-timeperframe)Added [SKTileDefinition.userData](https://developer.apple.com/documentation/spritekit/sktiledefinition/1645813-userdata)Added [SKTileDefinitionRotation](https://developer.apple.com/documentation/spritekit/sktiledefinitionrotation)Added [SKTileDefinitionRotation0](https://developer.apple.com/documentation/spritekit/sktiledefinitionrotation/sktiledefinitionrotation0)Added [SKTileDefinitionRotation180](https://developer.apple.com/documentation/spritekit/sktiledefinitionrotation/sktiledefinitionrotation180)Added [SKTileDefinitionRotation270](https://developer.apple.com/documentation/spritekit/sktiledefinitionrotation/rotation270)Added [SKTileDefinitionRotation90](https://developer.apple.com/documentation/spritekit/sktiledefinitionrotation/rotation90)

#### SKTileMapNode.h (Added)

Added [SKTileMapNode](https://developer.apple.com/documentation/spritekit/sktilemapnode)Added [SKTileMapNode.anchorPoint](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643608-anchorpoint)Added [SKTileMapNode.blendMode](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643598-blendmode)Added [-[SKTileMapNode centerOfTileAtColumn:row:]](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643599-centeroftileatcolumn)Added [SKTileMapNode.color](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643601-color)Added [SKTileMapNode.colorBlendFactor](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643607-colorblendfactor)Added [SKTileMapNode.enableAutomapping](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643604-enableautomapping)Added [-[SKTileMapNode fillWithTileGroup:]](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643615-fillwithtilegroup)Added [-[SKTileMapNode initWithTileSet:columns:rows:tileSize:]](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643609-init)Added [-[SKTileMapNode initWithTileSet:columns:rows:tileSize:fillWithTileGroup:]](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643612-initwithtileset)Added [-[SKTileMapNode initWithTileSet:columns:rows:tileSize:tileGroupLayout:]](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643597-initwithtileset)Added [SKTileMapNode.lightingBitMask](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643618-lightingbitmask)Added [SKTileMapNode.mapSize](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643595-mapsize)Added [SKTileMapNode.numberOfColumns](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643600-numberofcolumns)Added [SKTileMapNode.numberOfRows](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643611-numberofrows)Added [-[SKTileMapNode setTileGroup:andTileDefinition:forColumn:row:]](https://developer.apple.com/documentation/spritekit/sktilemapnode/1690935-settilegroup)Added [-[SKTileMapNode setTileGroup:forColumn:row:]](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643605-settilegroup)Added [SKTileMapNode.shader](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643596-shader)Added [-[SKTileMapNode tileColumnIndexFromPosition:]](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643617-tilecolumnindex)Added [-[SKTileMapNode tileDefinitionAtColumn:row:]](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643602-tiledefinition)Added [-[SKTileMapNode tileGroupAtColumn:row:]](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643613-tilegroupatcolumn)Added [+[SKTileMapNode tileMapNodeWithTileSet:columns:rows:tileSize:]](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643593-tilemapnodewithtileset)Added [+[SKTileMapNode tileMapNodeWithTileSet:columns:rows:tileSize:fillWithTileGroup:]](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643606-tilemapnodewithtileset)Added [+[SKTileMapNode tileMapNodeWithTileSet:columns:rows:tileSize:tileGroupLayout:]](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643603-tilemapnodewithtileset)Added [-[SKTileMapNode tileRowIndexFromPosition:]](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643614-tilerowindex)Added [SKTileMapNode.tileSet](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643610-tileset)Added [SKTileMapNode.tileSize](https://developer.apple.com/documentation/spritekit/sktilemapnode/1643594-tilesize)

#### SKTileSet.h (Added)

Added [SKTileGroup](https://developer.apple.com/documentation/spritekit/sktilegroup)Added [+[SKTileGroup emptyTileGroup]](https://developer.apple.com/documentation/spritekit/sktilegroup/1643840-emptytilegroup)Added [-[SKTileGroup initWithRules:]](https://developer.apple.com/documentation/spritekit/sktilegroup/1643839-initwithrules)Added [-[SKTileGroup initWithTileDefinition:]](https://developer.apple.com/documentation/spritekit/sktilegroup/1643832-initwithtiledefinition)Added [SKTileGroup.name](https://developer.apple.com/documentation/spritekit/sktilegroup/1643893-name)Added [SKTileGroup.rules](https://developer.apple.com/documentation/spritekit/sktilegroup/1643867-rules)Added [+[SKTileGroup tileGroupWithRules:]](https://developer.apple.com/documentation/spritekit/sktilegroup/1643891-tilegroupwithrules)Added [+[SKTileGroup tileGroupWithTileDefinition:]](https://developer.apple.com/documentation/spritekit/sktilegroup/1643887-tilegroupwithtiledefinition)Added [SKTileGroupRule](https://developer.apple.com/documentation/spritekit/sktilegrouprule)Added [SKTileGroupRule.adjacency](https://developer.apple.com/documentation/spritekit/sktilegrouprule/1643818-adjacency)Added [-[SKTileGroupRule initWithAdjacency:tileDefinitions:]](https://developer.apple.com/documentation/spritekit/sktilegrouprule/1643837-initwithadjacency)Added [SKTileGroupRule.name](https://developer.apple.com/documentation/spritekit/sktilegrouprule/1643860-name)Added [SKTileGroupRule.tileDefinitions](https://developer.apple.com/documentation/spritekit/sktilegrouprule/1643823-tiledefinitions)Added [+[SKTileGroupRule tileGroupRuleWithAdjacency:tileDefinitions:]](https://developer.apple.com/documentation/spritekit/sktilegrouprule/1643846-tilegrouprulewithadjacency)Added [SKTileSet](https://developer.apple.com/documentation/spritekit/sktileset)Added [SKTileSet.defaultTileGroup](https://developer.apple.com/documentation/spritekit/sktileset/1643878-defaulttilegroup)Added [SKTileSet.defaultTileSize](https://developer.apple.com/documentation/spritekit/sktileset/1643889-defaulttilesize)Added [-[SKTileSet initWithTileGroups:]](https://developer.apple.com/documentation/spritekit/sktileset/1643885-initwithtilegroups)Added [-[SKTileSet initWithTileGroups:tileSetType:]](https://developer.apple.com/documentation/spritekit/sktileset/1643896-initwithtilegroups)Added [SKTileSet.name](https://developer.apple.com/documentation/spritekit/sktileset/1643888-name)Added [SKTileSet.tileGroups](https://developer.apple.com/documentation/spritekit/sktileset/1643874-tilegroups)Added [+[SKTileSet tileSetFromURL:]](https://developer.apple.com/documentation/spritekit/sktileset/1643830-tilesetfromurl)Added [+[SKTileSet tileSetNamed:]](https://developer.apple.com/documentation/spritekit/sktileset/1643819-tilesetnamed)Added [+[SKTileSet tileSetWithTileGroups:]](https://developer.apple.com/documentation/spritekit/sktileset/1643872-tilesetwithtilegroups)Added [+[SKTileSet tileSetWithTileGroups:tileSetType:]](https://developer.apple.com/documentation/spritekit/sktileset/1643843-tilesetwithtilegroups)Added [SKTileSet.type](https://developer.apple.com/documentation/spritekit/sktileset/1643836-type)Added [SKTileAdjacencyAll](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencyall)Added [SKTileAdjacencyDown](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643890-adjacencydown)Added [SKTileAdjacencyDownEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencydownedge)Added [SKTileAdjacencyLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643880-adjacencyleft)Added [SKTileAdjacencyLeftEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1690888-adjacencyleftedge)Added [SKTileAdjacencyLowerLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencylowerleft)Added [SKTileAdjacencyLowerLeftCorner](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencylowerleftcorner)Added [SKTileAdjacencyLowerLeftEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1690891-adjacencylowerleftedge)Added [SKTileAdjacencyLowerRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643825-adjacencylowerright)Added [SKTileAdjacencyLowerRightCorner](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1690893-adjacencylowerrightcorner)Added [SKTileAdjacencyLowerRightEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1690896-adjacencylowerrightedge)Added [SKTileAdjacencyMask](https://developer.apple.com/documentation/spritekit/sktileadjacencymask)Added [SKTileAdjacencyRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencyright)Added [SKTileAdjacencyRightEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencyrightedge)Added [SKTileAdjacencyUp](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencyup)Added [SKTileAdjacencyUpEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencyupedge)Added [SKTileAdjacencyUpperLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643864-adjacencyupperleft)Added [SKTileAdjacencyUpperLeftCorner](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencyupperleftcorner)Added [SKTileAdjacencyUpperLeftEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencyupperleftedge)Added [SKTileAdjacencyUpperRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencyupperright)Added [SKTileAdjacencyUpperRightCorner](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1690895-adjacencyupperrightcorner)Added [SKTileAdjacencyUpperRightEdge](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktileadjacencyupperrightedge)Added [SKTileHexFlatAdjacencyAll](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643899-hexflatadjacencyall)Added [SKTileHexFlatAdjacencyDown](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktilehexflatadjacencydown)Added [SKTileHexFlatAdjacencyLowerLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktilehexflatadjacencylowerleft)Added [SKTileHexFlatAdjacencyLowerRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktilehexflatadjacencylowerright)Added [SKTileHexFlatAdjacencyUp](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643844-hexflatadjacencyup)Added [SKTileHexFlatAdjacencyUpperLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktilehexflatadjacencyupperleft)Added [SKTileHexFlatAdjacencyUpperRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktilehexflatadjacencyupperright)Added [SKTileHexPointyAdjacencyAdd](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643826-hexpointyadjacencyadd)Added [SKTileHexPointyAdjacencyLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643866-hexpointyadjacencyleft)Added [SKTileHexPointyAdjacencyLowerLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktilehexpointyadjacencylowerleft)Added [SKTileHexPointyAdjacencyLowerRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/sktilehexpointyadjacencylowerright)Added [SKTileHexPointyAdjacencyRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643859-hexpointyadjacencyright)Added [SKTileHexPointyAdjacencyUpperLeft](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643879-hexpointyadjacencyupperleft)Added [SKTileHexPointyAdjacencyUpperRight](https://developer.apple.com/documentation/spritekit/sktileadjacencymask/1643900-hexpointyadjacencyupperright)Added [SKTileSetType](https://developer.apple.com/documentation/spritekit/sktilesettype)Added [SKTileSetTypeGrid](https://developer.apple.com/documentation/spritekit/sktilesettype/sktilesettypegrid)Added [SKTileSetTypeHexagonalFlat](https://developer.apple.com/documentation/spritekit/sktilesettype/hexagonalflat)Added [SKTileSetTypeHexagonalPointy](https://developer.apple.com/documentation/spritekit/sktilesettype/sktilesettypehexagonalpointy)Added [SKTileSetTypeIsometric](https://developer.apple.com/documentation/spritekit/sktilesettype/isometric)

#### SKUniform.h

Added [-[SKUniform initWithName:matrixFloat2x2:]](https://developer.apple.com/documentation/spritekit/skuniform/1645806-init)Added [-[SKUniform initWithName:matrixFloat3x3:]](https://developer.apple.com/documentation/spritekit/skuniform/1645799-initwithname)Added [-[SKUniform initWithName:matrixFloat4x4:]](https://developer.apple.com/documentation/spritekit/skuniform/1645816-init)Added [-[SKUniform initWithName:vectorFloat2:]](https://developer.apple.com/documentation/spritekit/skuniform/1645782-initwithname)Added [-[SKUniform initWithName:vectorFloat3:]](https://developer.apple.com/documentation/spritekit/skuniform/1645803-initwithname)Added [-[SKUniform initWithName:vectorFloat4:]](https://developer.apple.com/documentation/spritekit/skuniform/1645808-initwithname)Added [SKUniform.matrixFloat2x2Value](https://developer.apple.com/documentation/spritekit/skuniform/1645818-matrixfloat2x2value)Added [SKUniform.matrixFloat3x3Value](https://developer.apple.com/documentation/spritekit/skuniform/1645810-matrixfloat3x3value)Added [SKUniform.matrixFloat4x4Value](https://developer.apple.com/documentation/spritekit/skuniform/1645817-matrixfloat4x4value)Added [+[SKUniform uniformWithName:matrixFloat2x2:]](https://developer.apple.com/documentation/spritekit/skuniform/1646689-uniformwithname)Added [+[SKUniform uniformWithName:matrixFloat3x3:]](https://developer.apple.com/documentation/spritekit/skuniform/1646692-uniformwithname)Added [+[SKUniform uniformWithName:matrixFloat4x4:]](https://developer.apple.com/documentation/spritekit/skuniform/1646694-uniformwithname)Added [+[SKUniform uniformWithName:vectorFloat2:]](https://developer.apple.com/documentation/spritekit/skuniform/1646690-uniformwithname)Added [+[SKUniform uniformWithName:vectorFloat3:]](https://developer.apple.com/documentation/spritekit/skuniform/1646691-uniformwithname)Added [+[SKUniform uniformWithName:vectorFloat4:]](https://developer.apple.com/documentation/spritekit/skuniform/1646693-uniformwithname)Added [SKUniform.vectorFloat2Value](https://developer.apple.com/documentation/spritekit/skuniform/1645819-vectorfloat2value)Added [SKUniform.vectorFloat3Value](https://developer.apple.com/documentation/spritekit/skuniform/1645805-vectorfloat3value)Added [SKUniform.vectorFloat4Value](https://developer.apple.com/documentation/spritekit/skuniform/1645789-vectorfloat4value)Modified [SKUniform.floatMatrix2Value](https://developer.apple.com/documentation/spritekit/skuniform/1455410-floatmatrix2value)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.floatMatrix3Value](https://developer.apple.com/documentation/spritekit/skuniform/1455438-floatmatrix3value)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.floatMatrix4Value](https://developer.apple.com/documentation/spritekit/skuniform/1455460-floatmatrix4value)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.floatValue](https://developer.apple.com/documentation/spritekit/skuniform/1455406-floatvalue)

|  | Declaration |
| --- | --- |
| From | ``` @property float floatValue ``` |
| To | ``` @property(nonatomic) float floatValue ``` |

Modified [SKUniform.floatVector2Value](https://developer.apple.com/documentation/spritekit/skuniform/1455436-floatvector2value)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.floatVector3Value](https://developer.apple.com/documentation/spritekit/skuniform/1455434-floatvector3value)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [SKUniform.floatVector4Value](https://developer.apple.com/documentation/spritekit/skuniform/1455404-floatvector4value)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [-[SKUniform initWithName:floatMatrix2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455431-initwithname)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [-[SKUniform initWithName:floatMatrix3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455462-init)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [-[SKUniform initWithName:floatMatrix4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455429-init)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [-[SKUniform initWithName:floatVector2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455444-initwithname)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [-[SKUniform initWithName:floatVector3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455416-initwithname)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [-[SKUniform initWithName:floatVector4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455418-initwithname)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [+[SKUniform uniformWithName:floatMatrix2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455463-uniformwithname)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [+[SKUniform uniformWithName:floatMatrix3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455402-uniformwithname)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [+[SKUniform uniformWithName:floatMatrix4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455446-uniformwithname)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [+[SKUniform uniformWithName:floatVector2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455472-uniformwithname)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [+[SKUniform uniformWithName:floatVector3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455414-uniformwithname)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

Modified [+[SKUniform uniformWithName:floatVector4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455465-uniformwithname)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 10.0 |

#### SKVideoNode.h

Modified [+[SKVideoNode videoNodeWithFileNamed:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407924-videonodewithfilenamed)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [+[SKVideoNode videoNodeWithURL:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407902-videonodewithurl)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [+[SKVideoNode videoNodeWithVideoFileNamed:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407914-videonodewithvideofilenamed)

|  | Deprecation |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified [+[SKVideoNode videoNodeWithVideoURL:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407906-videonodewithvideourl)

|  | Deprecation |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

#### SKView.h

Added [SKView.delegate](https://developer.apple.com/documentation/spritekit/skview/1642774-delegate)Added [SKView.preferredFrameRate](https://developer.apple.com/documentation/spritekit/skview/1642777-preferredframerate)Added [SKView.preferredFramesPerSecond](https://developer.apple.com/documentation/spritekit/skview/1642773-preferredframespersecond)Added [SKViewDelegate](https://developer.apple.com/documentation/spritekit/skviewdelegate)Added [-[SKViewDelegate view:shouldRenderAtTime:]](https://developer.apple.com/documentation/spritekit/skviewdelegate/1642775-view)Modified [SKView.frameInterval](https://developer.apple.com/documentation/spritekit/skview/1520008-frameinterval)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### SKWarpGeometry.h (Added)

Added [+[SKAction animateWithWarps:times:]](https://developer.apple.com/documentation/spritekit/skaction/1690937-animate)Added [+[SKAction animateWithWarps:times:restore:]](https://developer.apple.com/documentation/spritekit/skaction/1690936-animatewithwarps)Added [+[SKAction warpTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1690951-warpto)Added [SKWarpable](https://developer.apple.com/documentation/spritekit/skwarpable)Added [SKWarpable.subdivisionLevels](https://developer.apple.com/documentation/spritekit/skwarpable/1690947-subdivisionlevels)Added [SKWarpable.warpGeometry](https://developer.apple.com/documentation/spritekit/skwarpable/1690953-warpgeometry)Added [SKWarpGeometry](https://developer.apple.com/documentation/spritekit/skwarpgeometry)Added [SKWarpGeometryGrid](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid)Added [-[SKWarpGeometryGrid destPositionAtIndex:]](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690944-destpositionatindex)Added [+[SKWarpGeometryGrid grid]](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690985-grid)Added [-[SKWarpGeometryGrid gridByReplacingDestPositions:]](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690946-gridbyreplacingdestpositions)Added [-[SKWarpGeometryGrid gridByReplacingSourcePositions:]](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690948-gridbyreplacingsourcepositions)Added [+[SKWarpGeometryGrid gridWithColumns:rows:]](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690938-gridwithcolumns)Added [+[SKWarpGeometryGrid gridWithColumns:rows:sourcePositions:destPositions:]](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690986-gridwithcolumns)Added [-[SKWarpGeometryGrid initWithCoder:]](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690949-init)Added [-[SKWarpGeometryGrid initWithColumns:rows:sourcePositions:destPositions:]](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690945-init)Added [SKWarpGeometryGrid.numberOfColumns](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690942-numberofcolumns)Added [SKWarpGeometryGrid.numberOfRows](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690943-numberofrows)Added [-[SKWarpGeometryGrid sourcePositionAtIndex:]](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690952-sourceposition)Added [SKWarpGeometryGrid.vertexCount](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid/1690940-vertexcount)Added SKAction(SKWarpable)

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
