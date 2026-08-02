---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/GameplayKit.html
archived_at: '2026-07-18T02:50:39.345980Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# GameplayKit Changes for Objective-C

### GameplayKit

#### GKAgent.h

Added [GKAgent3D](https://developer.apple.com/documentation/gameplaykit/gkagent3d)Added [GKAgent3D.position](https://developer.apple.com/documentation/gameplaykit/gkagent3d/1640702-position)Added [GKAgent3D.rightHanded](https://developer.apple.com/documentation/gameplaykit/gkagent3d/2143064-righthanded)Added [GKAgent3D.rotation](https://developer.apple.com/documentation/gameplaykit/gkagent3d/1640665-rotation)Added [-[GKAgent3D updateWithDeltaTime:]](https://developer.apple.com/documentation/gameplaykit/gkagent3d/1640645-update)Added [GKAgent3D.velocity](https://developer.apple.com/documentation/gameplaykit/gkagent3d/1640961-velocity)Modified [GKAgent](https://developer.apple.com/documentation/gameplaykit/gkagent)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCoding |

Modified [GKAgent.speed](https://developer.apple.com/documentation/gameplaykit/gkagent/1501038-speed)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` @property(nonatomic, readonly) float speed ``` | yes |
| To | ``` @property(nonatomic) float speed ``` | -- |

Modified [GKAgent2D](https://developer.apple.com/documentation/gameplaykit/gkagent2d)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCoding |

#### GKBehavior.h

Modified [GKBehavior](https://developer.apple.com/documentation/gameplaykit/gkbehavior)

|  | Protocols |
| --- | --- |
| From | NSFastEnumeration |
| To | NSCopying, NSFastEnumeration |

#### GKComponent.h

Added [-[GKComponent didAddToEntity]](https://developer.apple.com/documentation/gameplaykit/gkcomponent/1687601-didaddtoentity)Added [-[GKComponent willRemoveFromEntity]](https://developer.apple.com/documentation/gameplaykit/gkcomponent/1640914-willremovefromentity)Added [-[GKComponentSystem classForGenericArgumentAtIndex:]](https://developer.apple.com/documentation/gameplaykit/gkcomponentsystem/1640904-classforgenericargumentatindex)Modified [GKComponent](https://developer.apple.com/documentation/gameplaykit/gkcomponent)

|  | Protocols |
| --- | --- |
| From | NSCopying |
| To | NSCoding, NSCopying |

#### GKCompositeBehavior.h (Added)

Added [GKCompositeBehavior](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior)Added [GKCompositeBehavior.behaviorCount](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/1640881-behaviorcount)Added [+[GKCompositeBehavior behaviorWithBehaviors:]](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/1640636-behaviorwithbehaviors)Added [+[GKCompositeBehavior behaviorWithBehaviors:andWeights:]](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/1640948-init)Added [-[GKCompositeBehavior objectAtIndexedSubscript:]](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/1640637-subscript)Added [-[GKCompositeBehavior objectForKeyedSubscript:]](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/1640719-objectforkeyedsubscript)Added [-[GKCompositeBehavior removeAllBehaviors]](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/1640639-removeallbehaviors)Added [-[GKCompositeBehavior removeBehavior:]](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/1640706-remove)Added [-[GKCompositeBehavior setObject:forKeyedSubscript:]](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/1646643-setobject)Added [-[GKCompositeBehavior setWeight:forBehavior:]](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/1640713-setweight)Added [-[GKCompositeBehavior weightForBehavior:]](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/1640732-weightforbehavior)

#### GKDecisionTree.h (Added)

Added [GKDecisionNode](https://developer.apple.com/documentation/gameplaykit/gkdecisionnode)Added [-[GKDecisionNode createBranchWithPredicate:attribute:]](https://developer.apple.com/documentation/gameplaykit/gkdecisionnode/1640764-createbranchwithpredicate)Added [-[GKDecisionNode createBranchWithValue:attribute:]](https://developer.apple.com/documentation/gameplaykit/gkdecisionnode/1640673-createbranchwithvalue)Added [-[GKDecisionNode createBranchWithWeight:attribute:]](https://developer.apple.com/documentation/gameplaykit/gkdecisionnode/1640671-createbranchwithweight)Added [GKDecisionTree](https://developer.apple.com/documentation/gameplaykit/gkdecisiontree)Added [-[GKDecisionTree findActionForAnswers:]](https://developer.apple.com/documentation/gameplaykit/gkdecisiontree/1640891-findactionforanswers)Added [-[GKDecisionTree initWithAttribute:]](https://developer.apple.com/documentation/gameplaykit/gkdecisiontree/1640933-initwithattribute)Added [-[GKDecisionTree initWithExamples:actions:attributes:]](https://developer.apple.com/documentation/gameplaykit/gkdecisiontree/1640769-init)Added [GKDecisionTree.randomSource](https://developer.apple.com/documentation/gameplaykit/gkdecisiontree/1640654-randomsource)Added [GKDecisionTree.rootNode](https://developer.apple.com/documentation/gameplaykit/gkdecisiontree/1640655-rootnode)

#### GKEntity.h

Modified [GKEntity](https://developer.apple.com/documentation/gameplaykit/gkentity)

|  | Protocols |
| --- | --- |
| From | NSCopying |
| To | NSCoding, NSCopying |

#### GKGraph.h

Modified [GKGraph](https://developer.apple.com/documentation/gameplaykit/gkgraph)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCoding, NSCopying |

Modified [GKGridGraph](https://developer.apple.com/documentation/gameplaykit/gkgridgraph)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [-[GKGridGraph connectNodeToAdjacentNodes:]](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1501192-connectnodetoadjacentnodes)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [GKGridGraph.diagonalsAllowed](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1501179-diagonalsallowed)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [+[GKGridGraph graphFromGridStartingAt:width:height:diagonalsAllowed:]](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1556416-graphfromgridstartingat)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [GKGridGraph.gridHeight](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1501184-gridheight)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [GKGridGraph.gridOrigin](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1501194-gridorigin)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [GKGridGraph.gridWidth](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1501291-gridwidth)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [-[GKGridGraph initFromGridStartingAt:width:height:diagonalsAllowed:]](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1501289-init)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [-[GKGridGraph nodeAtGridPosition:]](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1501287-node)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (GKGridGraphNode *)nodeAtGridPosition:(vector_int2)position ``` | GameplayKit/GKGraph.h |
| To | ``` - (NodeType)nodeAtGridPosition:(vector_int2)position ``` | GameplayKit/GKGridGraph.h |

Modified [GKObstacleGraph](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph addObstacles:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501073-addobstacles)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [GKObstacleGraph.bufferRadius](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501119-bufferradius)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph connectNodeUsingObstacles:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501129-connectnodeusingobstacles)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)connectNodeUsingObstacles:(GKGraphNode2D *)node ``` | GameplayKit/GKGraph.h |
| To | ``` - (void)connectNodeUsingObstacles:(NodeType)node ``` | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph connectNodeUsingObstacles:ignoringBufferRadiusOfObstacles:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501220-connectnodeusingobstacles)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)connectNodeUsingObstacles:(GKGraphNode2D *)node ignoringBufferRadiusOfObstacles:(NSArray<GKPolygonObstacle *> *)obstaclesBufferRadiusToIgnore ``` | GameplayKit/GKGraph.h |
| To | ``` - (void)connectNodeUsingObstacles:(NodeType)node ignoringBufferRadiusOfObstacles:(NSArray<GKPolygonObstacle *> *)obstaclesBufferRadiusToIgnore ``` | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph connectNodeUsingObstacles:ignoringObstacles:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501075-connectusingobstacles)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)connectNodeUsingObstacles:(GKGraphNode2D *)node ignoringObstacles:(NSArray<GKPolygonObstacle *> *)obstaclesToIgnore ``` | GameplayKit/GKGraph.h |
| To | ``` - (void)connectNodeUsingObstacles:(NodeType)node ignoringObstacles:(NSArray<GKPolygonObstacle *> *)obstaclesToIgnore ``` | GameplayKit/GKObstacleGraph.h |

Modified [+[GKObstacleGraph graphWithObstacles:bufferRadius:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1556417-graphwithobstacles)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph initWithObstacles:bufferRadius:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501299-initwithobstacles)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph isConnectionLockedFromNode:toNode:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501126-isconnectionlockedfromnode)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (BOOL)isConnectionLockedFromNode:(GKGraphNode2D *)startNode toNode:(GKGraphNode2D *)endNode ``` | GameplayKit/GKGraph.h |
| To | ``` - (BOOL)isConnectionLockedFromNode:(NodeType)startNode toNode:(NodeType)endNode ``` | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph lockConnectionFromNode:toNode:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501060-lockconnectionfromnode)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)lockConnectionFromNode:(GKGraphNode2D *)startNode toNode:(GKGraphNode2D *)endNode ``` | GameplayKit/GKGraph.h |
| To | ``` - (void)lockConnectionFromNode:(NodeType)startNode toNode:(NodeType)endNode ``` | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph nodesForObstacle:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501285-nodesforobstacle)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (NSArray<GKGraphNode2D *> *)nodesForObstacle:(GKPolygonObstacle *)obstacle ``` | GameplayKit/GKGraph.h |
| To | ``` - (NSArray<NodeType> *)nodesForObstacle:(GKPolygonObstacle *)obstacle ``` | GameplayKit/GKObstacleGraph.h |

Modified [GKObstacleGraph.obstacles](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501213-obstacles)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph removeAllObstacles]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501297-removeallobstacles)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph removeObstacles:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501058-removeobstacles)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph unlockConnectionFromNode:toNode:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501093-unlockconnectionfromnode)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)unlockConnectionFromNode:(GKGraphNode2D *)startNode toNode:(GKGraphNode2D *)endNode ``` | GameplayKit/GKGraph.h |
| To | ``` - (void)unlockConnectionFromNode:(NodeType)startNode toNode:(NodeType)endNode ``` | GameplayKit/GKObstacleGraph.h |

#### GKGraphNode.h

Added [GKGraphNode3D](https://developer.apple.com/documentation/gameplaykit/gkgraphnode3d)Added [-[GKGraphNode3D initWithPoint:]](https://developer.apple.com/documentation/gameplaykit/gkgraphnode3d/1640778-initwithpoint)Added [+[GKGraphNode3D nodeWithPoint:]](https://developer.apple.com/documentation/gameplaykit/gkgraphnode3d/1640907-nodewithpoint)Added [GKGraphNode3D.position](https://developer.apple.com/documentation/gameplaykit/gkgraphnode3d/1640786-position)Modified [GKGraphNode](https://developer.apple.com/documentation/gameplaykit/gkgraphnode)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCoding |

Modified [-[GKGraphNode2D initWithPoint:]](https://developer.apple.com/documentation/gameplaykit/gkgraphnode2d/1427547-init)

|  | Designated Initializer |
| --- | --- |
| From | yes |
| To | -- |

Modified [GKGridGraphNode.gridPosition](https://developer.apple.com/documentation/gameplaykit/gkgridgraphnode/1427533-gridposition)

|  | Declaration | Readonly |
| --- | --- | --- |
| From | ``` @property(nonatomic) vector_int2 gridPosition ``` | -- |
| To | ``` @property(nonatomic, readonly) vector_int2 gridPosition ``` | yes |

Modified [-[GKGridGraphNode initWithGridPosition:]](https://developer.apple.com/documentation/gameplaykit/gkgridgraphnode/1427527-initwithgridposition)

|  | Designated Initializer |
| --- | --- |
| From | yes |
| To | -- |

#### GKGridGraph.h (Added)

Added [-[GKGridGraph classForGenericArgumentAtIndex:]](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1640837-classforgenericargument)Added [+[GKGridGraph graphFromGridStartingAt:width:height:diagonalsAllowed:nodeClass:]](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1644761-graphfromgridstartingat)Added [-[GKGridGraph initFromGridStartingAt:width:height:diagonalsAllowed:nodeClass:]](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1640883-initfromgridstartingat)Modified [GKGridGraph](https://developer.apple.com/documentation/gameplaykit/gkgridgraph)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [-[GKGridGraph connectNodeToAdjacentNodes:]](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1501192-connectnodetoadjacentnodes)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [GKGridGraph.diagonalsAllowed](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1501179-diagonalsallowed)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [+[GKGridGraph graphFromGridStartingAt:width:height:diagonalsAllowed:]](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1556416-graphfromgridstartingat)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [GKGridGraph.gridHeight](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1501184-gridheight)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [GKGridGraph.gridOrigin](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1501194-gridorigin)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [GKGridGraph.gridWidth](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1501291-gridwidth)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [-[GKGridGraph initFromGridStartingAt:width:height:diagonalsAllowed:]](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1501289-init)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKGridGraph.h |

Modified [-[GKGridGraph nodeAtGridPosition:]](https://developer.apple.com/documentation/gameplaykit/gkgridgraph/1501287-node)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (GKGridGraphNode *)nodeAtGridPosition:(vector_int2)position ``` | GameplayKit/GKGraph.h |
| To | ``` - (NodeType)nodeAtGridPosition:(vector_int2)position ``` | GameplayKit/GKGridGraph.h |

#### GKMeshGraph.h (Added)

Added [GKMeshGraph](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph)Added [-[GKMeshGraph addObstacles:]](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/1640689-addobstacles)Added [GKMeshGraph.bufferRadius](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/1640945-bufferradius)Added [-[GKMeshGraph classForGenericArgumentAtIndex:]](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/1640740-classforgenericargumentatindex)Added [-[GKMeshGraph connectNodeUsingObstacles:]](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/1640849-connectnodeusingobstacles)Added [+[GKMeshGraph graphWithBufferRadius:minCoordinate:maxCoordinate:]](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/1644762-graphwithbufferradius)Added [+[GKMeshGraph graphWithBufferRadius:minCoordinate:maxCoordinate:nodeClass:]](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/1644763-graphwithbufferradius)Added [-[GKMeshGraph initWithBufferRadius:minCoordinate:maxCoordinate:]](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/1640735-initwithbufferradius)Added [-[GKMeshGraph initWithBufferRadius:minCoordinate:maxCoordinate:nodeClass:]](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/1640725-initwithbufferradius)Added [GKMeshGraph.obstacles](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/1640684-obstacles)Added [-[GKMeshGraph removeObstacles:]](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/1640677-removeobstacles)Added [-[GKMeshGraph triangleAtIndex:]](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/1640709-triangle)Added [GKMeshGraph.triangleCount](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/1687602-trianglecount)Added [-[GKMeshGraph triangulate]](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/1640683-triangulate)Added [GKMeshGraph.triangulationMode](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph/1640674-triangulationmode)Added [GKMeshGraphTriangulationMode](https://developer.apple.com/documentation/gameplaykit/gkmeshgraphtriangulationmode)Added [GKMeshGraphTriangulationModeCenters](https://developer.apple.com/documentation/gameplaykit/gkmeshgraphtriangulationmode/1640638-centers)Added [GKMeshGraphTriangulationModeEdgeMidpoints](https://developer.apple.com/documentation/gameplaykit/gkmeshgraphtriangulationmode/1640754-edgemidpoints)Added [GKMeshGraphTriangulationModeVertices](https://developer.apple.com/documentation/gameplaykit/gkmeshgraphtriangulationmode/1640701-vertices)

#### GKMonteCarloStrategist.h (Added)

Added [GKMonteCarloStrategist](https://developer.apple.com/documentation/gameplaykit/gkmontecarlostrategist)Added [GKMonteCarloStrategist.budget](https://developer.apple.com/documentation/gameplaykit/gkmontecarlostrategist/1640936-budget)Added [GKMonteCarloStrategist.explorationParameter](https://developer.apple.com/documentation/gameplaykit/gkmontecarlostrategist/1640679-explorationparameter)

#### GKNoise.h (Added)

Added [GKNoise](https://developer.apple.com/documentation/gameplaykit/gknoise)Added [-[GKNoise addWithNoise:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778324-addwithnoise)Added [-[GKNoise applyAbsoluteValue]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778317-applyabsolutevalue)Added [-[GKNoise applyTurbulenceWithFrequency:power:roughness:seed:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778323-applyturbulence)Added [-[GKNoise clampWithLowerBound:upperBound:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778331-clampwithlowerbound)Added [-[GKNoise displaceXWithNoise:yWithNoise:zWithNoise:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778298-displacewithnoises)Added [GKNoise.gradientColors](https://developer.apple.com/documentation/gameplaykit/gknoise/1778278-gradientcolors)Added [-[GKNoise init]](https://developer.apple.com/documentation/gameplaykit/gknoise/1823485-init)Added [-[GKNoise initWithNoiseSource:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778291-initwithnoisesource)Added [-[GKNoise initWithNoiseSource:gradientColors:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778287-initwithnoisesource)Added [-[GKNoise invert]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778306-invert)Added [-[GKNoise maximumWithNoise:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778304-maximumwithnoise)Added [-[GKNoise minimumWithNoise:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778305-minimumwithnoise)Added [-[GKNoise moveBy:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778309-moveby)Added [-[GKNoise multiplyWithNoise:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778332-multiply)Added [+[GKNoise noiseWithComponentNoises:selectionNoise:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778280-noisewithcomponentnoises)Added [+[GKNoise noiseWithComponentNoises:selectionNoise:componentBoundaries:boundaryBlendDistances:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778283-noisewithcomponentnoises)Added [+[GKNoise noiseWithNoiseSource:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1779741-noisewithnoisesource)Added [+[GKNoise noiseWithNoiseSource:gradientColors:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1779743-noisewithnoisesource)Added [-[GKNoise raiseToPower:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778288-raisetopower)Added [-[GKNoise raiseToPowerWithNoise:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778300-raisetopowerwithnoise)Added [-[GKNoise remapValuesToCurveWithControlPoints:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1823487-remapvalues)Added [-[GKNoise remapValuesToTerracesWithPeaks:terracesInverted:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1823486-remapvaluestoterraceswithpeaks)Added [-[GKNoise rotateBy:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778289-rotateby)Added [-[GKNoise scaleBy:]](https://developer.apple.com/documentation/gameplaykit/gknoise/1778290-scaleby)Added [-[GKNoise valueAtPosition:]](https://developer.apple.com/documentation/gameplaykit/gknoise/2138321-valueatposition)

#### GKNoiseMap.h (Added)

Added [GKNoiseMap](https://developer.apple.com/documentation/gameplaykit/gknoisemap)Added [-[GKNoiseMap init]](https://developer.apple.com/documentation/gameplaykit/gknoisemap/1823702-init)Added [-[GKNoiseMap initWithNoise:]](https://developer.apple.com/documentation/gameplaykit/gknoisemap/1823706-initwithnoise)Added [-[GKNoiseMap initWithNoise:size:origin:sampleCount:seamless:]](https://developer.apple.com/documentation/gameplaykit/gknoisemap/1823704-initwithnoise)Added [-[GKNoiseMap interpolatedValueAtPosition:]](https://developer.apple.com/documentation/gameplaykit/gknoisemap/1823703-interpolatedvalueatposition)Added [+[GKNoiseMap noiseMapWithNoise:]](https://developer.apple.com/documentation/gameplaykit/gknoisemap/1827529-noisemapwithnoise)Added [+[GKNoiseMap noiseMapWithNoise:size:origin:sampleCount:seamless:]](https://developer.apple.com/documentation/gameplaykit/gknoisemap/1827530-noisemapwithnoise)Added [GKNoiseMap.origin](https://developer.apple.com/documentation/gameplaykit/gknoisemap/1823696-origin)Added [GKNoiseMap.sampleCount](https://developer.apple.com/documentation/gameplaykit/gknoisemap/1823697-samplecount)Added [GKNoiseMap.seamless](https://developer.apple.com/documentation/gameplaykit/gknoisemap/1640681-seamless)Added [-[GKNoiseMap setValue:atPosition:]](https://developer.apple.com/documentation/gameplaykit/gknoisemap/1823699-setvalue)Added [GKNoiseMap.size](https://developer.apple.com/documentation/gameplaykit/gknoisemap/1823700-size)Added [-[GKNoiseMap valueAtPosition:]](https://developer.apple.com/documentation/gameplaykit/gknoisemap/1823698-value)

#### GKNoiseSource.h (Added)

Added [GKBillowNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkbillownoisesource)Added [+[GKBillowNoiseSource billowNoiseSourceWithFrequency:octaveCount:persistence:lacunarity:seed:]](https://developer.apple.com/documentation/gameplaykit/gkbillownoisesource/1644029-billownoisesourcewithfrequency)Added [-[GKBillowNoiseSource initWithFrequency:octaveCount:persistence:lacunarity:seed:]](https://developer.apple.com/documentation/gameplaykit/gkbillownoisesource/1640893-initwithfrequency)Added [GKBillowNoiseSource.persistence](https://developer.apple.com/documentation/gameplaykit/gkbillownoisesource/1640650-persistence)Added [GKCheckerboardNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkcheckerboardnoisesource)Added [+[GKCheckerboardNoiseSource checkerboardNoiseWithSquareSize:]](https://developer.apple.com/documentation/gameplaykit/gkcheckerboardnoisesource/1823707-checkerboardnoise)Added [-[GKCheckerboardNoiseSource initWithSquareSize:]](https://developer.apple.com/documentation/gameplaykit/gkcheckerboardnoisesource/1823701-initwithsquaresize)Added [GKCheckerboardNoiseSource.squareSize](https://developer.apple.com/documentation/gameplaykit/gkcheckerboardnoisesource/1823705-squaresize)Added [GKCoherentNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkcoherentnoisesource)Added [GKCoherentNoiseSource.frequency](https://developer.apple.com/documentation/gameplaykit/gkcoherentnoisesource/1823695-frequency)Added [GKCoherentNoiseSource.lacunarity](https://developer.apple.com/documentation/gameplaykit/gkcoherentnoisesource/1778292-lacunarity)Added [GKCoherentNoiseSource.octaveCount](https://developer.apple.com/documentation/gameplaykit/gkcoherentnoisesource/1778299-octavecount)Added [GKCoherentNoiseSource.seed](https://developer.apple.com/documentation/gameplaykit/gkcoherentnoisesource/1778293-seed)Added [GKConstantNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkconstantnoisesource)Added [+[GKConstantNoiseSource constantNoiseWithValue:]](https://developer.apple.com/documentation/gameplaykit/gkconstantnoisesource/1640720-constantnoise)Added [-[GKConstantNoiseSource initWithValue:]](https://developer.apple.com/documentation/gameplaykit/gkconstantnoisesource/1640714-initwithvalue)Added [GKConstantNoiseSource.value](https://developer.apple.com/documentation/gameplaykit/gkconstantnoisesource/1640959-value)Added [GKCylindersNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkcylindersnoisesource)Added [+[GKCylindersNoiseSource cylindersNoiseWithFrequency:]](https://developer.apple.com/documentation/gameplaykit/gkcylindersnoisesource/1640644-cylindersnoisewithfrequency)Added [GKCylindersNoiseSource.frequency](https://developer.apple.com/documentation/gameplaykit/gkcylindersnoisesource/1640822-frequency)Added [-[GKCylindersNoiseSource initWithFrequency:]](https://developer.apple.com/documentation/gameplaykit/gkcylindersnoisesource/1640886-initwithfrequency)Added [GKNoiseSource](https://developer.apple.com/documentation/gameplaykit/gknoisesource)Added [GKPerlinNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkperlinnoisesource)Added [-[GKPerlinNoiseSource initWithFrequency:octaveCount:persistence:lacunarity:seed:]](https://developer.apple.com/documentation/gameplaykit/gkperlinnoisesource/1640305-initwithfrequency)Added [+[GKPerlinNoiseSource perlinNoiseSourceWithFrequency:octaveCount:persistence:lacunarity:seed:]](https://developer.apple.com/documentation/gameplaykit/gkperlinnoisesource/1640309-perlinnoisesourcewithfrequency)Added [GKPerlinNoiseSource.persistence](https://developer.apple.com/documentation/gameplaykit/gkperlinnoisesource/1640299-persistence)Added [GKRidgedNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkridgednoisesource)Added [-[GKRidgedNoiseSource initWithFrequency:octaveCount:lacunarity:seed:]](https://developer.apple.com/documentation/gameplaykit/gkridgednoisesource/1640658-initwithfrequency)Added [+[GKRidgedNoiseSource ridgedNoiseSourceWithFrequency:octaveCount:lacunarity:seed:]](https://developer.apple.com/documentation/gameplaykit/gkridgednoisesource/1646493-ridgednoisesourcewithfrequency)Added [GKSpheresNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkspheresnoisesource)Added [GKSpheresNoiseSource.frequency](https://developer.apple.com/documentation/gameplaykit/gkspheresnoisesource/1640716-frequency)Added [-[GKSpheresNoiseSource initWithFrequency:]](https://developer.apple.com/documentation/gameplaykit/gkspheresnoisesource/1640802-initwithfrequency)Added [+[GKSpheresNoiseSource spheresNoiseWithFrequency:]](https://developer.apple.com/documentation/gameplaykit/gkspheresnoisesource/1640830-spheresnoisewithfrequency)Added [GKVoronoiNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkvoronoinoisesource)Added [GKVoronoiNoiseSource.displacement](https://developer.apple.com/documentation/gameplaykit/gkvoronoinoisesource/1640682-displacement)Added [GKVoronoiNoiseSource.distanceEnabled](https://developer.apple.com/documentation/gameplaykit/gkvoronoinoisesource/1640789-distanceenabled)Added [GKVoronoiNoiseSource.frequency](https://developer.apple.com/documentation/gameplaykit/gkvoronoinoisesource/1640711-frequency)Added [-[GKVoronoiNoiseSource initWithFrequency:displacement:distanceEnabled:seed:]](https://developer.apple.com/documentation/gameplaykit/gkvoronoinoisesource/1640726-initwithfrequency)Added [GKVoronoiNoiseSource.seed](https://developer.apple.com/documentation/gameplaykit/gkvoronoinoisesource/1640938-seed)Added [+[GKVoronoiNoiseSource voronoiNoiseWithFrequency:displacement:distanceEnabled:seed:]](https://developer.apple.com/documentation/gameplaykit/gkvoronoinoisesource/1640771-voronoinoisewithfrequency)

#### GKObstacle.h

Added [GKSphereObstacle](https://developer.apple.com/documentation/gameplaykit/gksphereobstacle)Added [-[GKSphereObstacle initWithRadius:]](https://developer.apple.com/documentation/gameplaykit/gksphereobstacle/1778308-init)Added [+[GKSphereObstacle obstacleWithRadius:]](https://developer.apple.com/documentation/gameplaykit/gksphereobstacle/1779558-obstaclewithradius)Added [GKSphereObstacle.position](https://developer.apple.com/documentation/gameplaykit/gksphereobstacle/1778313-position)Added [GKSphereObstacle.radius](https://developer.apple.com/documentation/gameplaykit/gksphereobstacle/1778325-radius)Modified [GKPolygonObstacle](https://developer.apple.com/documentation/gameplaykit/gkpolygonobstacle)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCoding |

#### GKObstacleGraph.h (Added)

Added [-[GKObstacleGraph classForGenericArgumentAtIndex:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1640659-classforgenericargumentatindex)Added [+[GKObstacleGraph graphWithObstacles:bufferRadius:nodeClass:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1644731-graphwithobstacles)Added [-[GKObstacleGraph initWithObstacles:bufferRadius:nodeClass:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1640694-initwithobstacles)Modified [GKObstacleGraph](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph addObstacles:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501073-addobstacles)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [GKObstacleGraph.bufferRadius](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501119-bufferradius)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph connectNodeUsingObstacles:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501129-connectnodeusingobstacles)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)connectNodeUsingObstacles:(GKGraphNode2D *)node ``` | GameplayKit/GKGraph.h |
| To | ``` - (void)connectNodeUsingObstacles:(NodeType)node ``` | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph connectNodeUsingObstacles:ignoringBufferRadiusOfObstacles:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501220-connectnodeusingobstacles)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)connectNodeUsingObstacles:(GKGraphNode2D *)node ignoringBufferRadiusOfObstacles:(NSArray<GKPolygonObstacle *> *)obstaclesBufferRadiusToIgnore ``` | GameplayKit/GKGraph.h |
| To | ``` - (void)connectNodeUsingObstacles:(NodeType)node ignoringBufferRadiusOfObstacles:(NSArray<GKPolygonObstacle *> *)obstaclesBufferRadiusToIgnore ``` | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph connectNodeUsingObstacles:ignoringObstacles:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501075-connectusingobstacles)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)connectNodeUsingObstacles:(GKGraphNode2D *)node ignoringObstacles:(NSArray<GKPolygonObstacle *> *)obstaclesToIgnore ``` | GameplayKit/GKGraph.h |
| To | ``` - (void)connectNodeUsingObstacles:(NodeType)node ignoringObstacles:(NSArray<GKPolygonObstacle *> *)obstaclesToIgnore ``` | GameplayKit/GKObstacleGraph.h |

Modified [+[GKObstacleGraph graphWithObstacles:bufferRadius:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1556417-graphwithobstacles)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph initWithObstacles:bufferRadius:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501299-initwithobstacles)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph isConnectionLockedFromNode:toNode:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501126-isconnectionlockedfromnode)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (BOOL)isConnectionLockedFromNode:(GKGraphNode2D *)startNode toNode:(GKGraphNode2D *)endNode ``` | GameplayKit/GKGraph.h |
| To | ``` - (BOOL)isConnectionLockedFromNode:(NodeType)startNode toNode:(NodeType)endNode ``` | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph lockConnectionFromNode:toNode:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501060-lockconnectionfromnode)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)lockConnectionFromNode:(GKGraphNode2D *)startNode toNode:(GKGraphNode2D *)endNode ``` | GameplayKit/GKGraph.h |
| To | ``` - (void)lockConnectionFromNode:(NodeType)startNode toNode:(NodeType)endNode ``` | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph nodesForObstacle:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501285-nodesforobstacle)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (NSArray<GKGraphNode2D *> *)nodesForObstacle:(GKPolygonObstacle *)obstacle ``` | GameplayKit/GKGraph.h |
| To | ``` - (NSArray<NodeType> *)nodesForObstacle:(GKPolygonObstacle *)obstacle ``` | GameplayKit/GKObstacleGraph.h |

Modified [GKObstacleGraph.obstacles](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501213-obstacles)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph removeAllObstacles]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501297-removeallobstacles)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph removeObstacles:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501058-removeobstacles)

|  | Header |
| --- | --- |
| From | GameplayKit/GKGraph.h |
| To | GameplayKit/GKObstacleGraph.h |

Modified [-[GKObstacleGraph unlockConnectionFromNode:toNode:]](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph/1501093-unlockconnectionfromnode)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)unlockConnectionFromNode:(GKGraphNode2D *)startNode toNode:(GKGraphNode2D *)endNode ``` | GameplayKit/GKGraph.h |
| To | ``` - (void)unlockConnectionFromNode:(NodeType)startNode toNode:(NodeType)endNode ``` | GameplayKit/GKObstacleGraph.h |

#### GKOctree.h (Added)

Added [GKOctree](https://developer.apple.com/documentation/gameplaykit/gkoctree)Added [-[GKOctree addElement:withBox:]](https://developer.apple.com/documentation/gameplaykit/gkoctree/1640833-addelement)Added [-[GKOctree addElement:withPoint:]](https://developer.apple.com/documentation/gameplaykit/gkoctree/1640958-add)Added [-[GKOctree elementsAtPoint:]](https://developer.apple.com/documentation/gameplaykit/gkoctree/1640859-elementsatpoint)Added [-[GKOctree elementsInBox:]](https://developer.apple.com/documentation/gameplaykit/gkoctree/1640941-elements)Added [-[GKOctree initWithBoundingBox:minimumCellSize:]](https://developer.apple.com/documentation/gameplaykit/gkoctree/1640712-init)Added [+[GKOctree octreeWithBoundingBox:minimumCellSize:]](https://developer.apple.com/documentation/gameplaykit/gkoctree/1644791-octreewithboundingbox)Added [-[GKOctree removeElement:]](https://developer.apple.com/documentation/gameplaykit/gkoctree/1640873-remove)Added [-[GKOctree removeElement:withNode:]](https://developer.apple.com/documentation/gameplaykit/gkoctree/1640653-removeelement)Added [GKOctreeNode](https://developer.apple.com/documentation/gameplaykit/gkoctreenode)Added [GKOctreeNode.box](https://developer.apple.com/documentation/gameplaykit/gkoctreenode/1640729-box)

#### GKPath.h

Added [-[GKPath float2AtIndex:]](https://developer.apple.com/documentation/gameplaykit/gkpath/1778285-float2atindex)Added [-[GKPath float3AtIndex:]](https://developer.apple.com/documentation/gameplaykit/gkpath/1778310-float3)Added [-[GKPath initWithFloat3Points:count:radius:cyclical:]](https://developer.apple.com/documentation/gameplaykit/gkpath/1778297-initwithfloat3points)Added [+[GKPath pathWithFloat3Points:count:radius:cyclical:]](https://developer.apple.com/documentation/gameplaykit/gkpath/1779559-pathwithfloat3points)Modified [-[GKPath initWithGraphNodes:radius:]](https://developer.apple.com/documentation/gameplaykit/gkpath/1501138-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithGraphNodes:(NSArray<GKGraphNode2D *> *)graphNodes radius:(float)radius ``` |
| To | ``` - (instancetype)initWithGraphNodes:(NSArray<GKGraphNode *> *)graphNodes radius:(float)radius ``` |

Modified [-[GKPath initWithPoints:count:radius:cyclical:]](https://developer.apple.com/documentation/gameplaykit/gkpath/1501048-initwithpoints)

|  | Designated Initializer |
| --- | --- |
| From | yes |
| To | -- |

Modified [+[GKPath pathWithGraphNodes:radius:]](https://developer.apple.com/documentation/gameplaykit/gkpath/1574696-pathwithgraphnodes)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)pathWithGraphNodes:(NSArray<GKGraphNode2D *> *)graphNodes radius:(float)radius ``` |
| To | ``` + (instancetype)pathWithGraphNodes:(NSArray<GKGraphNode *> *)graphNodes radius:(float)radius ``` |

Modified [-[GKPath pointAtIndex:]](https://developer.apple.com/documentation/gameplaykit/gkpath/1501172-point)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### GKPrimitives.h (Added)

Added [GKBox](https://developer.apple.com/documentation/gameplaykit/gkbox)Added [GKQuad](https://developer.apple.com/documentation/gameplaykit/gkquad)Added [GKTriangle](https://developer.apple.com/documentation/gameplaykit/gktriangle)

#### GKQuadtree.h (Added)

Added [GKQuadtree](https://developer.apple.com/documentation/gameplaykit/gkquadtree)Added [-[GKQuadtree addElement:withPoint:]](https://developer.apple.com/documentation/gameplaykit/gkquadtree/1778303-addelement)Added [-[GKQuadtree addElement:withQuad:]](https://developer.apple.com/documentation/gameplaykit/gkquadtree/1778320-addelement)Added [-[GKQuadtree elementsAtPoint:]](https://developer.apple.com/documentation/gameplaykit/gkquadtree/1778327-elements)Added [-[GKQuadtree elementsInQuad:]](https://developer.apple.com/documentation/gameplaykit/gkquadtree/1778279-elements)Added [-[GKQuadtree initWithBoundingQuad:minimumCellSize:]](https://developer.apple.com/documentation/gameplaykit/gkquadtree/1778321-initwithboundingquad)Added [+[GKQuadtree quadtreeWithBoundingQuad:minimumCellSize:]](https://developer.apple.com/documentation/gameplaykit/gkquadtree/1779583-quadtreewithboundingquad)Added [-[GKQuadtree removeElement:]](https://developer.apple.com/documentation/gameplaykit/gkquadtree/1778294-remove)Added [-[GKQuadtree removeElement:withNode:]](https://developer.apple.com/documentation/gameplaykit/gkquadtree/1778286-remove)Added [GKQuadtreeNode](https://developer.apple.com/documentation/gameplaykit/gkquadtreenode)Added [GKQuadtreeNode.quad](https://developer.apple.com/documentation/gameplaykit/gkquadtreenode/1778318-quad)

#### GKRandomSource.h

Added [-[NSArray shuffledArray]](https://developer.apple.com/documentation/foundation/nsarray/1640855-shuffledarray)Added [-[NSArray shuffledArrayWithRandomSource:]](https://developer.apple.com/documentation/foundation/nsarray/1640687-shuffledarraywithrandomsource)Added NSArray(GameplayKit)

#### GKRTree.h (Added)

Added [GKRTree](https://developer.apple.com/documentation/gameplaykit/gkrtree)Added [-[GKRTree addElement:boundingRectMin:boundingRectMax:splitStrategy:]](https://developer.apple.com/documentation/gameplaykit/gkrtree/1640262-addelement)Added [-[GKRTree elementsInBoundingRectMin:rectMax:]](https://developer.apple.com/documentation/gameplaykit/gkrtree/1640264-elements)Added [-[GKRTree initWithMaxNumberOfChildren:]](https://developer.apple.com/documentation/gameplaykit/gkrtree/1640256-init)Added [GKRTree.queryReserve](https://developer.apple.com/documentation/gameplaykit/gkrtree/1640267-queryreserve)Added [-[GKRTree removeElement:boundingRectMin:boundingRectMax:]](https://developer.apple.com/documentation/gameplaykit/gkrtree/1640259-removeelement)Added [+[GKRTree treeWithMaxNumberOfChildren:]](https://developer.apple.com/documentation/gameplaykit/gkrtree/1640257-treewithmaxnumberofchildren)Added [GKRTreeSplitStrategy](https://developer.apple.com/documentation/gameplaykit/gkrtreesplitstrategy)Added [GKRTreeSplitStrategyHalve](https://developer.apple.com/documentation/gameplaykit/gkrtreesplitstrategy/halve)Added [GKRTreeSplitStrategyLinear](https://developer.apple.com/documentation/gameplaykit/gkrtreesplitstrategy/linear)Added [GKRTreeSplitStrategyQuadratic](https://developer.apple.com/documentation/gameplaykit/gkrtreesplitstrategy/gkrtreesplitstrategyquadratic)Added [GKRTreeSplitStrategyReduceOverlap](https://developer.apple.com/documentation/gameplaykit/gkrtreesplitstrategy/gkrtreesplitstrategyreduceoverlap)

#### GKScene.h (Added)

Added [GKScene](https://developer.apple.com/documentation/gameplaykit/gkscene)Added [-[GKScene addEntity:]](https://developer.apple.com/documentation/gameplaykit/gkscene/1640954-addentity)Added [-[GKScene addGraph:name:]](https://developer.apple.com/documentation/gameplaykit/gkscene/2143063-addgraph)Added [GKScene.entities](https://developer.apple.com/documentation/gameplaykit/gkscene/1640795-entities)Added [GKScene.graphs](https://developer.apple.com/documentation/gameplaykit/gkscene/1640940-graphs)Added [-[GKScene removeEntity:]](https://developer.apple.com/documentation/gameplaykit/gkscene/1640686-removeentity)Added [-[GKScene removeGraph:]](https://developer.apple.com/documentation/gameplaykit/gkscene/1640663-removegraph)Added [GKScene.rootNode](https://developer.apple.com/documentation/gameplaykit/gkscene/1640947-rootnode)Added [+[GKScene sceneWithFileNamed:]](https://developer.apple.com/documentation/gameplaykit/gkscene/1640935-init)Added [GKSceneRootNodeType](https://developer.apple.com/documentation/gameplaykit/gkscenerootnodetype)

#### GKSKNodeComponent.h (Added)

Added [GKSKNodeComponent](https://developer.apple.com/documentation/gameplaykit/gksknodecomponent)Added [+[GKSKNodeComponent componentWithNode:]](https://developer.apple.com/documentation/gameplaykit/gksknodecomponent/1640983-componentwithnode)Added [-[GKSKNodeComponent initWithNode:]](https://developer.apple.com/documentation/gameplaykit/gksknodecomponent/1640693-initwithnode)Added [GKSKNodeComponent.node](https://developer.apple.com/documentation/gameplaykit/gksknodecomponent/1640728-node)

#### SpriteKit+Additions.h (Added)

Added [SKNode.entity](https://developer.apple.com/documentation/spritekit/sknode/1640688-entity)Added [+[SKTexture textureWithNoiseMap:]](https://developer.apple.com/documentation/spritekit/sktexture/1640752-init)Added [+[SKTileMapNode tileMapNodesWithTileSet:columns:rows:tileSize:fromNoiseMap:tileTypeNoiseMapThresholds:]](https://developer.apple.com/documentation/spritekit/sktilemapnode/1640698-tilemapnodes)Added SKNode(GameplayKit)Added SKScene(GameplayKit)Added SKTexture(GameplayKit)Added SKTileMapNode(GameplayKit)Modified [+[SKNode obstaclesFromNodeBounds:]](https://developer.apple.com/documentation/spritekit/sknode/1483132-obstacles)

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
