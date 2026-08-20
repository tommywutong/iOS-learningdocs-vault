---
title: What's New in macOS
apple_id: TP40001812
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/WhatsNewInOSX/Articles/OSXv10.html
archived_at: '2026-07-18T02:58:54.508727Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [What's New in macOS](Introduction.md)


[Next](OS%20X%20El%20Capitan%20v10.11.2.md)[Previous](macOS%20Sierra%2010.12.1.md)

# macOS Sierra 10.12

The following sections highlight macOS 10.12 features that span multiple technology areas or that are otherwise of particular importance to most developers.

In macOS 10.12, users can make purchases with Apple Pay from websites. For developers, macOS 10.12 introduces new API you can use in code that runs in macOS, iOS and watchOS, as well as the ability to support dynamic payment networks, and a new sandbox testing environment.
macOS 10.12 introduces the ApplePay JavaScript framework, which helps you incorporate Apple Pay directly into iOS and macOS Safari-based websites. When you support Apple Pay in your website, users can authorize payments using their iPhone or Apple Watch. To learn more, see _ApplePay JS Framework Reference_.

macOS 10.12 introduces several changes and additions that help you improve the security of your code and maintain the privacy of user data. To learn more about these items, see `https://developer.apple.com/security/`.

- The new `NSAllowsArbitraryLoadsInWebContent` key for your `Info.plist` file gives you a convenient way to allow arbitrary web page loads to work while retaining ATS protection for the rest of your app.
- The SecKey API includes improvements for asymmetric key generation. Use the SecKey API instead of the deprecated Common Data Security Architecture (CDSA) APIs.
- SSLv3 cryptographic protocol and the RC4 symmetric cipher suite are no longer supported, starting at the end of 2016. It's recommended that you stop using the SHA-1 and 3DES cryptographic algorithms as soon as possible.
- Developer ID-signed apps can now take advantage of CloudKit, iCloud Keychain, iCloud Drive, remote (push) notifications, MapKit, and VPN entitlements. Starting in macOS 10.12, you can no longer provide external code or data alongside your code-signed app in a zip archive or unsigned disk image. An app distributed outside the Mac App Store runs from a randomized path when it is launched and so cannot access such external resources. To provide secure execution, code sign your disk image itself using the codesign tool, or distribute your app through the Mac App Store. For more information, see the updated revision to _[macOS Code Signing In Depth](https://developer.apple.com/library/archive/technotes/tn2206/_index.html#//apple_ref/doc/uid/DTS40007919)_.
- You must statically declare your app’s intended use of protected data classes by including the appropriate purpose string keys in your `Info.plist` file. For example, you must include the `NSCalendarsUsageDescription` key to access the user’s Calendar data. If you don’t include the relevant purpose string keys, your app exits the first time it tries to access the data.

Most graphics frameworks throughout the system, including Core Graphics, Core Image, Metal, and AVFoundation, have substantially improved support for extended-range pixel formats and wide-gamut color spaces. By extending this behavior throughout the entire graphics stack, it is easier than ever to support devices with a wide color display.

To take advantage of extended-range pixel formats in your Metal graphics pipeline, use the [MTLPixelFormatRGBA16Float](https://developer.apple.com/documentation/metal/mtlpixelformat/rgba16float) pixel format.

Here are a couple best practices to adopt as you start working with wide-gamut colors.

- If you are performing your own image processing using a lower-level API, such as Core Graphics or Metal, then on those devices you should use an extended range color space and a pixel format that supports 16-bit floating-point component values. When clamping of color values is necessary, you should do so explicitly.
- Core Graphics, Core Image, and Metal Performance Shaders provide new options for easily converting colors and images between color spaces.

The latest release of Swift includes significant refinement to API naming designed to enhance your code's consistency and clarity. Also in this release, important frameworks have been upgraded to native Swift interfaces, such as Core Graphics and Grand Central Dispatch. To learn about what’s new in Swift, see _The Swift Programming Language (Swift 3)_.

This year, the CloudKit framework includes a sharing API, so your app's users can easily share a record or set of records within their private database. CloudKit provides the complete UI for sending and accepting shared record invitations. Unique URLs are generated for every share and users have full privacy control. Read or write access can be restricted to just the people they choose or they can make it visible to everyone with the URL. Shared records are stored in the owner’s private database.

Apple File System is a new modern file system for iOS, macOS, tvOS and watchOS. Apple File System is optimized for Flash/SSD storage and features strong encryption, copy-on-write metadata, space sharing, cloning for files and directories, snapshots, fast directory sizing, atomic safe-save primitives, and improved filesystem fundamentals. A Developer Preview is available in macOS 10.12. For more information, see _[Apple File System Guide](../../../documentation/File%20Management/Apple%20File%20System%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dsojz)_.

Unified logging provides a single, efficient, performant API for capturing messaging across all levels of the system. Unified logging provides developers with fine-grained control over multiple logging levels, includes built-in privacy protection, and integrates with activity tracing to make problem diagnosis easier. When activity tracing and logging are used in tandem, related messages are automatically correlated. Logging is also integrated with Simulator.

A new version of Console in /Applications/Utilities/ displays log data from connected devices, supports tokenized searching and saved searches, and shows connections between related messages across multiple processes. Log messages can also be viewed and managed using the log command-line tool.

Unified logging supersedes ASL (Apple System Logger) and the Syslog APIs. Messages are now stored in memory and a data store, rather than in text-based log files.

For more information, see _Logging Reference_.

You can extend the behavior of Safari using app extensions. Safari app extensions let you take full advantage of web technologies while also being tightly integrated with macOS, easily created through Xcode, and distributed with your apps through the Mac App Store. It is also easy to port your iOS Content Blocker App Extensions to macOS. For more information, see _[Safari App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/SafariAppExtension_PG/index.html#//apple_ref/doc/uid/TP40017319)_.

You can now create `NSExtension`-based smart card drivers, allowing the contents of certain types of smart cards to be presented as part of the system keychain. This mechanism is intended to replace the deprecated Common Data Security Architecture, although for macOS 10.12, both architectures are supported.

The driver extensions are limited to read-only mode, so that it is not possible to alter the contents of a smart card using the standard keychain interface. For more information, see _[CryptoTokenKit Framework Reference](https://developer.apple.com/documentation/cryptotokenkit)_.

The following sections highlight changes to frameworks and framework technologies in macOS 10.12.

The following frameworks have been added in macOS 10.12:

- __Intents.__ Apps linked against the Intents framework can use it to examine interactions, such as a person’s location or actions, and take action based on that information.
- __SafariServices.__ App developers can use the new SafariServices framework to create app extensions for Safari on macOS and iOS.

New functionality has been added in several areas, including:

- Quadrature (integral calculus)
- Basic functions for constructing neural networks
- Geometric predicate functions to test for such things as the intersection of two geometric objects

The AppKit framework introduces several new features in macOS 10.12, including:

- Several [NSCollectionView](https://developer.apple.com/documentation/appkit/nscollectionview)nhancements, such as:

  - __Collapsible Sections.__ Finder’s icon view offers users the ability to collapse any section into a single horizontally scrollable row, via a “Show Less” button in the section’s header. You can now easily offer the same capability to users of your `NSCollectionView` objects.
  - __Floating Headers.__ Header and footer views in a flow layout can now be “floated,” using the same API provided by [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview) in iOS.
  - __Scrollable Background Views.__ An `NSCollectionView` instance’s `backgroundView` can now be set to scroll together with the content in the `CollectionView`, instead of floating stationary behind the content.
- The deferred view layout pass has been cleaned up, optimized and extended.
- The drag-and-drop API has been modernized with two new classes: `NSFilePromiseProvider` and `NSFilePromiseReceiver`. These new objects support drag flocking, are UTI based, and are pasteboard writer/reader compliant.
- Several new control convenience constructors are available, including:

  - [NSButton](https://developer.apple.com/documentation/appkit/nsbutton) now has several convenience constructors for creating system standard push buttons, checkboxes, and radio buttons.
  - [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield) now has several convenience constructors for creating non-wrapping labels, wrapping labels, attributed labels, and editable text fields.
  - [NSSegmentedControl](https://developer.apple.com/documentation/appkit/nssegmentedcontrol) has convenience constructors for creating a segmented control given an array of labels or an array of images.
  - [NSSlider](https://developer.apple.com/documentation/appkit/nsslider) has convenience constructors for creating horizontal linear sliders.
  - [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) has a convenience constructor for creating a non-editable image view with a given instance of [NSImage](https://developer.apple.com/documentation/appkit/nsimage).
- `NSGridView` is a new auto layout container for arranging content views into a grid. It's similar to [NSStackView](https://developer.apple.com/documentation/appkit/nsstackview), but allows for alignment across both rows and columns. Like a spreadsheet, rows and columns can all be varying sizes, or dynamically hidden and shown.

For more information on these and other AppKit changes, see _[AppKit Release Notes for macOS 10.13](../../App%20Kit/AppKit%20Release%20Notes%20for%20macOS%2010.13.md)_.

The AVFoundation framework includes the following enhancements:

- You no longer need to implement different behaviors for [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem), depending on whether the content is a movie file or HLS content.
- The `AVPlayerLooper` class makes it easier to loop a particular piece of media content during playback.
- Use the `AVAssetDownloadURLSession` and `AVAssetDownloadURLSession` classes to download an asset, including an HLS stream, to the device and then play it later. When used in conjunction with FairPlay Streaming, you can download an encrypted HLS stream and play the stream securely at a later time.

The Core Data framework includes the following enhancements:

- [NSPersistentStoreCoordinator](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator) now maintains a connection pool for SQLite stores. Root [NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext) instances (those without parent MOCs) transparently support concurrent fetching and faulting without serializing against each other.
- `NSManagedObjectContext` objects with SQLite stores in WAL journal_mode support a new feature called query generations. These allow a MOC to be pinned to a version of the database at a point in time and perform all future fetching and faulting against that version of the database. Pinned MOCs are moved to the most recent transaction with any save, and query generations do not survive the process's life time.
- The new class `NSPersistentContainer` provides your app with a high-level integration point that maintains references to your `NSPersistentStoreCoordinator`, [NSManagedObjectModel](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel) and other configuration resources.
- Core Data now has tighter integration with Xcode and automatically generates and updates your [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject) subclasses.
- `NSManagedObject` has several additional convenience methods making it easier to fetch and create subclasses. `NSManagedObject` subclasses that have a 1:1 relationship with an entity now support +entity.
- Core Data has received several API adjustments to provide better integration with Swift, including parameters on [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest).

For more information, see _[What's New In Core Data](../../General/What%27s%20New%20In%20Core%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tgnbs)_ and the _[Core Data Framework Reference](https://developer.apple.com/documentation/coredata)_.

The Core Image framework includes several enhancements.

You can now insert custom processing into a Core Image filter graph by using the `imageWithExtent:processorDescription:argumentDigest:inputFormat:outputFormat:options:roiCallback:processor:` method. This method adds a callback block that Core Image invokes in between filters when processing an image for display or output; in the block, you can access the pixel buffers or Metal textures containing the current state of the processed image and apply your own image processing algorithms.

When using a custom processor block or writing filter kernels, you can process images in a color space other than the Core Image context’s working color space. Use the [imageByColorMatchingWorkingSpaceToColorSpace:](https://developer.apple.com/documentation/coreimage/ciimage/1645898-imagebycolormatchingworkingspace) and [imageByColorMatchingColorSpaceToWorkingSpace:](https://developer.apple.com/documentation/coreimage/ciimage/1645896-imagebycolormatchingcolorspaceto) methods to convert into and out of your color space before and after processing.

Core Image kernel code can now request a specific output pixel format.

Core Image introduces five new filters:

- CINinePartTiled
- CINinePartStretched
- CIHueSaturationValueGradient
- CIEdgePreserveUpsampleFilter
- CIClamp

The Foundation framework introduces several new features in macOS 10.12, including:

- APIs for representing, converting, and displaying quantities of units—including built-in support for many of the most common physical units, such as mass, length, speed, duration and temperature. For more information, see [NSDimension](https://developer.apple.com/documentation/foundation/nsdimension).
- A formatter for parsing and generating ISO 8601 date representations. For more information, see [NSISO8601DateFormatter](https://developer.apple.com/documentation/foundation/nsiso8601dateformatter).
- A new class for representing date intervals. For more information, see [NSDateInterval](https://developer.apple.com/documentation/foundation/nsdateinterval).
- Support for parsing person name components from a string. For more information, see [NSPersonNameComponentsFormatter](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter).
- New APIs for obtaining metrics for URL session networking. For more information, see [NSURLSessionTaskMetrics](https://developer.apple.com/documentation/foundation/nsurlsessiontaskmetrics).

In addition, this release brings many API refinements to Foundation, taking advantage of new API features in Objective-C and enabling APIs to come across more naturally in Swift. Some of the key API update areas include:

- Adoption of Swift 3 API design guidelines. For more information, see [Swift Evolution document SE-0023, "API Design Guidelines."](https://github.com/apple/swift-evolution/blob/master/proposals/0023-api-guidelines.md)
- The addition of value types, where many Foundation classes are exposed as structs with value type semantics for Swift. For more information, see [Swift Evolution document SE-0069, "Mutability and Foundation Value Types."](https://github.com/apple/swift-evolution/blob/master/proposals/0069-swift-mutability-for-foundation.md)
- Introduction and adoption of string enumerations, with `NS_STRING_ENUM` and `NS_EXTENSIBLE_STRING_ENUM`.
- Introduction and adoption of `NS_NOESCAPE` to mark blocks whose execution completes before the API the block is passed in as an argument to.
- Dropping of "NS" prefix on certain Foundation classes and types, in both Swift and Objective-C.

For more information on these and other Foundation changes, see _[Foundation Release Notes for macOS 10.12 and iOS 10](../../Miscellaneous/Foundation%20Release%20Notes%20for%20macOS%2010.12%20and%20iOS%2010.md)_.

The GameKit framework includes the following changes and enhancements:

- The Game Center app has been removed. If your game implements GameKit features, it must also implement the interface behavior necessary for the user to see these features. For example, if your game supports leaderboards, it could present a [GKGameCenterViewController](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller) object or read the data directly from Game Center to implement a custom user interface.
- A new account type, implemented by the [GKCloudPlayer](https://developer.apple.com/documentation/gamekit/gkcloudplayer) class, supports iCloud-only game accounts.
- Game Center provides a new generalized solution for managing persistent storage of data on Game Center. A game session ([GKGameSession](https://developer.apple.com/documentation/gamekit/gkgamesession)) has a list of players who are the session’s participants. Your game’s implementation defines when and how a participant stores or retrieves data from the server or exchanges data between players. Game sessions can often replace existing turn-based matches, real-time matches, and persistent save games, and also enable other models of interaction between participants.

The GameplayKit framework includes the following changes and enhancements:

- Procedural noise generation can be used to generate rich game worlds, create sophisticated natural-looking textures, and add realism to camera movement.
- Spatial partitioning lets you partition your game world data so that the data in the game world can be searched efficiently.
- A new Monte Carlo strategist ([GKMonteCarloStrategist](https://developer.apple.com/documentation/gameplaykit/gkmontecarlostrategist)) helps you model games where exhaustive computation of possible moves is difficult.
- The new decision tree API can enhance your game-building AI when you adopt decision-tree learning to generalize behavior based on data mining of logged player actions. To learn more, see [GKDecisionTree](https://developer.apple.com/documentation/gameplaykit/gkdecisiontree) and [GKDecisionNode](https://developer.apple.com/documentation/gameplaykit/gkdecisionnode).
- The [GKAgent3D](https://developer.apple.com/documentation/gameplaykit/gkagent3d) and [GKGraphNode3D](https://developer.apple.com/documentation/gameplaykit/gkgraphnode3d) classes introduce 3D support to existing agent and path-finding behavior.
- The new [GKMeshGraph](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph) class provides a higher performance alternative to [GKObstacleGraph](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph), allowing you to produce more natural-looking output at the cost of less mathematically perfect paths.
- The new [GKScene](https://developer.apple.com/documentation/gameplaykit/gkscene) and [GKSKNodeComponent](https://developer.apple.com/documentation/gameplaykit/gksknodecomponent) classes, combined with changes in SpriteKit and the Xcode editor, make integrating GameplayKit with SpriteKit easier than ever.

In macOS 10.12, Metal includes several new features and enhancements, such as:

- Support for tessellation, enabling 3D apps and games to render more detailed scenes by efficiently describing complex geometry to the GPU.
- Function Specialization, which makes it easy to create a collection of highly optimized functions to handle all the material and light combinations in a scene.
- Metal System Trace, now in macOS, which offers deep insight into the graphics pipeline by profiling the interaction of the CPU and GPU, revealing performance optimization opportunities for Metal-based apps.

To learn more, see [What’s New in iOS 10, tvOS 10, and OS X 10.12](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/WhatsNewiniOS10tvOS10andOSX1012/WhatsNewiniOS10tvOS10andOSX1012.html#//apple_ref/doc/uid/TP40014221-CH14) in _[Metal Programming Guide](../../../documentation/Miscellaneous/Metal%20Programming%20Guide/About%20Metal%20and%20This%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrr)_.

The Model I/O framework includes the following enhancements:

- The USD file format is now supported.
- The new `MDLMaterialPropertyGraph` class makes it easier to support runtime procedural changes to models.
- The [MDLVoxelArray](https://developer.apple.com/documentation/modelio/mdlvoxelarray) class adds support for signed distance fields.
- You can add assisted light probe placement by implementing the `MDLLightProbeIrradianceDataSource` protocol.

Live Photo editing is now available to photo editing app extensions for use in the Photos app. Specifically, the new [PHLivePhotoEditingContext](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext) class lets you apply edits to the video and still photo content of a Live Photo, with an easy-to-use API based on Core Image enhancements. (To perform edits using other image processing technologies, see [CIImageProcessorInput](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput) and [CIImageProcessorOutput](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput).).

To support Live Photo editing extensions, the [PHLivePhoto](https://developer.apple.com/documentation/photokit/phlivephoto) and [PHLivePhotoView](https://developer.apple.com/documentation/photokit/phlivephotoview) classes (introduced in iOS 9.1) are now available in macOS.

The SceneKit framework includes several enhancements.

A new Physically Based Rendering (PBR) system allows you to leverage the latest in 3D graphics research to create more realistic results with simpler asset authoring. Specifically:

- Use the new [SCNLightingModelPhysicallyBased](https://developer.apple.com/documentation/scenekit/scnmaterial/lightingmodel/1640553-physicallybased) shading model to opt into PBR shading for materials. PBR materials require only three fundamental properties—[diffuse](https://developer.apple.com/documentation/scenekit/scnmaterial/1462589-diffuse), [metalness](https://developer.apple.com/documentation/scenekit/scnmaterial/1640554-metalness), and [roughness](https://developer.apple.com/documentation/scenekit/scnmaterial/1640555-roughness)—to produce a wide range of realistic shading effects. (The [normal](https://developer.apple.com/documentation/scenekit/scnmaterial/1462542-normal), [ambientOcclusion](https://developer.apple.com/documentation/scenekit/scnmaterial/1462579-ambientocclusion), and [selfIllumination](https://developer.apple.com/documentation/scenekit/scnmaterial/1462524-selfillumination) material properties also remain useful for PBR materials, but you can now ignore the large number of other properties used for traditional materials.)
- PBR shading works best with environment-based lighting, which causes even diffuse surfaces to pick up the colors of the scene around them. Use the [lightingEnvironment](https://developer.apple.com/documentation/scenekit/scnscene/1639532-lightingenvironment) property to assign global image-based lighting to an entire scene, and place light probes in the Xcode scene editor to pick up the local lighting contributions from objects within your scene.
- Authors of PBR scene content often prefer working in physically based terms, so you can now define lighting using intensity (in lumens) and color temperature (in degrees Kelvin), and import specifications for real-world light fixtures using the [IESProfileURL](https://developer.apple.com/documentation/scenekit/scnlight/1640546-iesprofileurl) property.

Add even more realism with the new HDR features and effects in the [SCNCamera](https://developer.apple.com/documentation/scenekit/scncamera) class. With HDR rendering, SceneKit captures a much wider range of brightness and contrast in a scene, then allows you to customize the tone mapping that adapts that scene for the narrower range of a device’s display. Enable exposure adaptation to create automatic effects when, for example, the player in your game moves from a darkened area into sunlight. Or use vignetting, color fringing, and color grading to add a filmic look to your game.

Although linear, more color-accurate rendering is the basis for PBR shading and HDR camera features, it produces better results even for traditional rendering. By default, SceneKit now performs all color calculations in a linear (not gamma-adjusted) color space, and uses the P3 color gamut of devices that include wide-color displays. This feature is enabled automatically for all apps linking against the macOS 10.12 SDK, and has a few ramifications for content design and asset management:

- SceneKit color matches all colors. In previous versions, SceneKit would read only the color values from material colors specified as [NSColor](https://developer.apple.com/documentation/appkit/nscolor) or [UIColor](https://developer.apple.com/documentation/uikit/uicolor) objects, ignoring color profile information and assuming the sRGB color space.
- SceneKit interprets color component values specified within shader modifier or custom Metal or OpenGL shader code in linear RGB space.
- SceneKit reads and adjusts for color profile information in texture images. Design textures for a linear brightness ramp, and use Asset Catalogs in Xcode to make sure your images use the correct color profile.
- If necesary, you can disable linear space rendering with the `SCNDisableLinearSpaceRendering` key in your app’s `Info.plist` file, and wide color rendering with the `SCNDisableWideGamut` key.

Geometry can now be loaded from scene files or programmatically defined using arbitrary polygon primitives ([SCNGeometryPrimitiveTypePolygon](https://developer.apple.com/documentation/scenekit/scngeometryprimitivetype/scngeometryprimitivetypepolygon)). SceneKit automatically triangulates polygon meshes for rendering, but makes use of the underlying polygon mesh for more accurate surface subdivision (to learn more, see the [subdivisionLevel](https://developer.apple.com/documentation/scenekit/scngeometry/1524177-subdivisionlevel) property).

The `SecKey` interface has been modernized and unified across platforms.

The SpriteKit framework includes the following enhancements:

- A new tilemap solution supports square, hexagonal, and isometric tilemaps that make it easy to create 2D, 2.5D, and side-scroller games. The Xcode editor provides comprehensive support for organizing your tiles and creating your tilemap. For more information, see the `SKTileMapNode`, `SKTileGroup`, `SKTileGroupRule`, and `SKTileSet` classes.
- The new `SKWarpGeometry` class is used to stretch or distort how a [SKSpriteNode](https://developer.apple.com/documentation/spritekit/skspritenode) or [SKEffectNode](https://developer.apple.com/documentation/spritekit/skeffectnode) object is rendered. The warp is specifed by a set of control points. New [SKAction](https://developer.apple.com/documentation/spritekit/skaction) types can be used to animate between different warp effects.
- A custom shader can use attributes that can be configured separately by each node that uses the shader. To add an attribute, create an `SKAttribute` object and attach it to your shader. Then, for each node that uses that shader, attach an `SKAttributeValue` object.
- The [SKView](https://developer.apple.com/documentation/spritekit/skview) class defines new methods that give you finer control over when and how your screne is rendered.

Periodically, Apple adds deprecation macros to APIs to indicate that those APIs should no longer be used in active development. When a deprecation occurs, it is not an immediate end of life for the specified API. Instead, it is the beginning of a grace period for transitioning from that API and to newer and more modern replacements. Deprecated APIs typically remain present and usable in the system for a reasonable time past the release in which they were deprecated. However, active development on them ceases, and the APIs receive only minor changes to accommodate security patches or to fix other critical bugs. Deprecated APIs may be removed entirely from a future version of the operating system.

As a developer, avoid using deprecated APIs in your code as soon as possible. At a minimum, new code you write should never use deprecated APIs. And if your existing code uses deprecated APIs, update that code as soon as possible. Fortunately, the compiler generates warnings whenever it spots the use of a deprecated API in your code. You can use those warnings to track down and remove all references to those APIs.

Frameworks and technologies deprecated or removed in macOS 10.12 include the following:

- The UIAutomation framework is deprecated.
- The HFS Standard filesystem is no longer supported.

[Next](OS%20X%20El%20Capitan%20v10.11.2.md)[Previous](macOS%20Sierra%2010.12.1.md)

