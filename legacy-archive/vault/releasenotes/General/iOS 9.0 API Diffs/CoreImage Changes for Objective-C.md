---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/CoreImage.html
archived_at: '2026-07-18T02:56:31.922531Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreImage Changes for Objective-C

### CoreImage

#### CIColor.h

Added [-[CIColor initWithRed:green:blue:]](https://developer.apple.com/documentation/coreimage/cicolor/1502102-initwithred)Added [-[CIColor initWithRed:green:blue:alpha:]](https://developer.apple.com/documentation/coreimage/cicolor/1438084-initwithred)Modified [CIColor](https://developer.apple.com/documentation/coreimage/cicolor)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [CIColor.alpha](https://developer.apple.com/documentation/coreimage/cicolor/1437981-alpha)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)alpha ``` |
| To | ``` @property(readonly) CGFloat alpha ``` |

Modified [CIColor.blue](https://developer.apple.com/documentation/coreimage/cicolor/1438033-blue)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)blue ``` |
| To | ``` @property(readonly) CGFloat blue ``` |

Modified [CIColor.colorSpace](https://developer.apple.com/documentation/coreimage/cicolor/1437917-colorspace)

|  | Declaration |
| --- | --- |
| From | ``` - (CGColorSpaceRef)colorSpace ``` |
| To | ``` @property(readonly, nonnull) CGColorSpaceRef colorSpace ``` |

Modified [+[CIColor colorWithCGColor:]](https://developer.apple.com/documentation/coreimage/cicolor/1502106-colorwithcgcolor)

|  | Declaration |
| --- | --- |
| From | ``` + (CIColor *)colorWithCGColor:(CGColorRef)c ``` |
| To | ``` + (instancetype _Nonnull)colorWithCGColor:(CGColorRef _Nonnull)c ``` |

Modified [+[CIColor colorWithRed:green:blue:]](https://developer.apple.com/documentation/coreimage/cicolor/1437941-colorwithred)

|  | Declaration |
| --- | --- |
| From | ``` + (CIColor *)colorWithRed:(CGFloat)r green:(CGFloat)g blue:(CGFloat)b ``` |
| To | ``` + (instancetype _Nonnull)colorWithRed:(CGFloat)r green:(CGFloat)g blue:(CGFloat)b ``` |

Modified [+[CIColor colorWithRed:green:blue:alpha:]](https://developer.apple.com/documentation/coreimage/cicolor/1502111-colorwithred)

|  | Declaration |
| --- | --- |
| From | ``` + (CIColor *)colorWithRed:(CGFloat)r green:(CGFloat)g blue:(CGFloat)b alpha:(CGFloat)a ``` |
| To | ``` + (instancetype _Nonnull)colorWithRed:(CGFloat)r green:(CGFloat)g blue:(CGFloat)b alpha:(CGFloat)a ``` |

Modified [+[CIColor colorWithString:]](https://developer.apple.com/documentation/coreimage/cicolor/1438059-init)

|  | Declaration |
| --- | --- |
| From | ``` + (CIColor *)colorWithString:(NSString *)representation ``` |
| To | ``` + (instancetype _Nonnull)colorWithString:(NSString * _Nonnull)representation ``` |

Modified [CIColor.components](https://developer.apple.com/documentation/coreimage/cicolor/1437862-components)

|  | Declaration |
| --- | --- |
| From | ``` - (const CGFloat *)components ``` |
| To | ``` @property(readonly, nonnull) const CGFloat *components ``` |

Modified [CIColor.green](https://developer.apple.com/documentation/coreimage/cicolor/1437607-green)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)green ``` |
| To | ``` @property(readonly) CGFloat green ``` |

Modified [-[CIColor initWithCGColor:]](https://developer.apple.com/documentation/coreimage/cicolor/1437821-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithCGColor:(CGColorRef)c ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithCGColor:(CGColorRef _Nonnull)c ``` | yes |

Modified [CIColor.numberOfComponents](https://developer.apple.com/documentation/coreimage/cicolor/1438151-numberofcomponents)

|  | Declaration |
| --- | --- |
| From | ``` - (size_t)numberOfComponents ``` |
| To | ``` @property(readonly) size_t numberOfComponents ``` |

Modified [CIColor.red](https://developer.apple.com/documentation/coreimage/cicolor/1437969-red)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)red ``` |
| To | ``` @property(readonly) CGFloat red ``` |

Modified [CIColor.stringRepresentation](https://developer.apple.com/documentation/coreimage/cicolor/1437910-stringrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)stringRepresentation ``` |
| To | ``` @property(readonly, nonnull) NSString *stringRepresentation ``` |

#### CIContext.h

Added [+[CIContext contextWithCGContext:options:]](https://developer.apple.com/documentation/coreimage/cicontext/1437864-init)Added [+[CIContext contextWithMTLDevice:]](https://developer.apple.com/documentation/coreimage/cicontext/1437609-init)Added [+[CIContext contextWithMTLDevice:options:]](https://developer.apple.com/documentation/coreimage/cicontext/1437711-contextwithmtldevice)Added [-[CIContext render:toMTLTexture:commandBuffer:bounds:colorSpace:]](https://developer.apple.com/documentation/coreimage/cicontext/1438026-render)Added [CIContext.workingColorSpace](https://developer.apple.com/documentation/coreimage/cicontext/1438061-workingcolorspace)Added #def CI_ARRAYAdded #def CI_DICTIONARYAdded CIContext(OfflineGPUSupport)Added [kCIContextHighQualityDownsample](https://developer.apple.com/documentation/coreimage/cicontextoption/1437699-highqualitydownsample)Modified [+[CIContext contextWithEAGLContext:options:]](https://developer.apple.com/documentation/coreimage/cicontext/1620362-contextwitheaglcontext)

|  | Declaration |
| --- | --- |
| From | ``` + (CIContext *)contextWithEAGLContext:(EAGLContext *)eaglContext options:(NSDictionary *)dict ``` |
| To | ``` + (CIContext * _Nonnull)contextWithEAGLContext:(EAGLContext * _Nonnull)eaglContext options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [+[CIContext contextWithOptions:]](https://developer.apple.com/documentation/coreimage/cicontext/1438261-init)

|  | Declaration |
| --- | --- |
| From | ``` + (CIContext *)contextWithOptions:(NSDictionary *)dict ``` |
| To | ``` + (CIContext * _Nonnull)contextWithOptions:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[CIContext createCGImage:fromRect:]](https://developer.apple.com/documentation/coreimage/cicontext/1437784-createcgimage)

|  | Declaration |
| --- | --- |
| From | ``` - (CGImageRef)createCGImage:(CIImage *)im fromRect:(CGRect)r ``` |
| To | ``` - (CGImageRef _Nonnull)createCGImage:(CIImage * _Nonnull)image fromRect:(CGRect)fromRect ``` |

Modified [-[CIContext createCGImage:fromRect:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/cicontext/1437978-createcgimage)

|  | Declaration |
| --- | --- |
| From | ``` - (CGImageRef)createCGImage:(CIImage *)im fromRect:(CGRect)r format:(CIFormat)f colorSpace:(CGColorSpaceRef)cs ``` |
| To | ``` - (CGImageRef _Nonnull)createCGImage:(CIImage * _Nonnull)image fromRect:(CGRect)fromRect format:(CIFormat)format colorSpace:(CGColorSpaceRef _Nullable)colorSpace ``` |

Modified [-[CIContext drawImage:atPoint:fromRect:]](https://developer.apple.com/documentation/coreimage/cicontext/1473521-drawimage)

|  | Declaration |
| --- | --- |
| From | ``` - (void)drawImage:(CIImage *)im atPoint:(CGPoint)p fromRect:(CGRect)src ``` |
| To | ``` - (void)drawImage:(CIImage * _Nonnull)image atPoint:(CGPoint)atPoint fromRect:(CGRect)fromRect ``` |

Modified [-[CIContext drawImage:inRect:fromRect:]](https://developer.apple.com/documentation/coreimage/cicontext/1437786-drawimage)

|  | Declaration |
| --- | --- |
| From | ``` - (void)drawImage:(CIImage *)im inRect:(CGRect)dest fromRect:(CGRect)src ``` |
| To | ``` - (void)drawImage:(CIImage * _Nonnull)image inRect:(CGRect)inRect fromRect:(CGRect)fromRect ``` |

Modified [-[CIContext render:toBitmap:rowBytes:bounds:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/cicontext/1437897-render)

|  | Declaration |
| --- | --- |
| From | ``` - (void)render:(CIImage *)im toBitmap:(void *)data rowBytes:(ptrdiff_t)rb bounds:(CGRect)r format:(CIFormat)f colorSpace:(CGColorSpaceRef)cs ``` |
| To | ``` - (void)render:(CIImage * _Nonnull)image toBitmap:(void * _Nonnull)data rowBytes:(ptrdiff_t)rowBytes bounds:(CGRect)bounds format:(CIFormat)format colorSpace:(CGColorSpaceRef _Nullable)colorSpace ``` |

Modified [-[CIContext render:toCVPixelBuffer:bounds:colorSpace:]](https://developer.apple.com/documentation/coreimage/cicontext/1437835-render)

|  | Declaration |
| --- | --- |
| From | ``` - (void)render:(CIImage *)image toCVPixelBuffer:(CVPixelBufferRef)buffer bounds:(CGRect)r colorSpace:(CGColorSpaceRef)cs ``` |
| To | ``` - (void)render:(CIImage * _Nonnull)image toCVPixelBuffer:(CVPixelBufferRef _Nonnull)buffer bounds:(CGRect)bounds colorSpace:(CGColorSpaceRef _Nullable)colorSpace ``` |

#### CIDetector.h

Added #def CI_ARRAYAdded #def CI_DICTIONARYAdded [CIDetectorNumberOfAngles](https://developer.apple.com/documentation/coreimage/cidetectornumberofangles)Added [CIDetectorReturnSubFeatures](https://developer.apple.com/documentation/coreimage/cidetectorreturnsubfeatures)Added [CIDetectorTypeText](https://developer.apple.com/documentation/coreimage/cidetectortypetext)Modified [+[CIDetector detectorOfType:context:options:]](https://developer.apple.com/documentation/coreimage/cidetector/1437884-init)

|  | Declaration |
| --- | --- |
| From | ``` + (CIDetector *)detectorOfType:(NSString *)type context:(CIContext *)context options:(NSDictionary *)options ``` |
| To | ``` + (CIDetector * _Nonnull)detectorOfType:(NSString * _Nonnull)type context:(CIContext * _Nullable)context options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[CIDetector featuresInImage:]](https://developer.apple.com/documentation/coreimage/cidetector/1438049-featuresinimage)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)featuresInImage:(CIImage *)image ``` |
| To | ``` - (NSArray<CIFeature *> * _Nonnull)featuresInImage:(CIImage * _Nonnull)image ``` |

Modified [-[CIDetector featuresInImage:options:]](https://developer.apple.com/documentation/coreimage/cidetector/1438189-features)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)featuresInImage:(CIImage *)image options:(NSDictionary *)options ``` |
| To | ``` - (NSArray<CIFeature *> * _Nonnull)featuresInImage:(CIImage * _Nonnull)image options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

#### CIFeature.h

Added [CITextFeature](https://developer.apple.com/documentation/coreimage/citextfeature)Added [CITextFeature.bottomLeft](https://developer.apple.com/documentation/coreimage/citextfeature/1438004-bottomleft)Added [CITextFeature.bottomRight](https://developer.apple.com/documentation/coreimage/citextfeature/1437659-bottomright)Added [CITextFeature.bounds](https://developer.apple.com/documentation/coreimage/citextfeature/1437885-bounds)Added [CITextFeature.subFeatures](https://developer.apple.com/documentation/coreimage/citextfeature/1437810-subfeatures)Added [CITextFeature.topLeft](https://developer.apple.com/documentation/coreimage/citextfeature/1438221-topleft)Added [CITextFeature.topRight](https://developer.apple.com/documentation/coreimage/citextfeature/1438282-topright)Added [CIFeatureTypeQRCode](https://developer.apple.com/documentation/coreimage/cifeaturetypeqrcode)Added [CIFeatureTypeRectangle](https://developer.apple.com/documentation/coreimage/cifeaturetyperectangle)Added [CIFeatureTypeText](https://developer.apple.com/documentation/coreimage/cifeaturetypetext)Modified [CIQRCodeFeature.bottomLeft](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437985-bottomleft)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) CGPoint bottomLeft ``` |
| To | ``` @property(readonly) CGPoint bottomLeft ``` |

Modified [CIQRCodeFeature.bottomRight](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438245-bottomright)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) CGPoint bottomRight ``` |
| To | ``` @property(readonly) CGPoint bottomRight ``` |

Modified [CIQRCodeFeature.bounds](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438153-bounds)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) CGRect bounds ``` |
| To | ``` @property(readonly) CGRect bounds ``` |

Modified [CIQRCodeFeature.messageString](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438035-messagestring)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *messageString ``` |
| To | ``` @property(readonly, nonnull) NSString *messageString ``` |

Modified [CIQRCodeFeature.topLeft](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437780-topleft)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) CGPoint topLeft ``` |
| To | ``` @property(readonly) CGPoint topLeft ``` |

Modified [CIQRCodeFeature.topRight](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437896-topright)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) CGPoint topRight ``` |
| To | ``` @property(readonly) CGPoint topRight ``` |

Modified [CIRectangleFeature.bottomLeft](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437878-bottomleft)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) CGPoint bottomLeft ``` |
| To | ``` @property(readonly) CGPoint bottomLeft ``` |

Modified [CIRectangleFeature.bottomRight](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437888-bottomright)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) CGPoint bottomRight ``` |
| To | ``` @property(readonly) CGPoint bottomRight ``` |

Modified [CIRectangleFeature.bounds](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1438024-bounds)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) CGRect bounds ``` |
| To | ``` @property(readonly) CGRect bounds ``` |

Modified [CIRectangleFeature.topLeft](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437951-topleft)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) CGPoint topLeft ``` |
| To | ``` @property(readonly) CGPoint topLeft ``` |

Modified [CIRectangleFeature.topRight](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1438071-topright)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) CGPoint topRight ``` |
| To | ``` @property(readonly) CGPoint topRight ``` |

#### CIFilter.h

Added [+[CIFilter localizedDescriptionForFilterName:]](https://developer.apple.com/documentation/coreimage/cifilter/1437591-localizeddescription)Added [+[CIFilter localizedNameForCategory:]](https://developer.apple.com/documentation/coreimage/cifilter/1438057-localizedname)Added [+[CIFilter localizedNameForFilterName:]](https://developer.apple.com/documentation/coreimage/cifilter/1437697-localizedname)Added [+[CIFilter localizedReferenceDocumentationForFilterName:]](https://developer.apple.com/documentation/coreimage/cifilter/1437642-localizedreferencedocumentation)Added [+[CIFilter registerFilterName:constructor:classAttributes:]](https://developer.apple.com/documentation/coreimage/cifilter/1437889-registername)Added #def CI_ARRAYAdded #def CI_DICTIONARYAdded [kCIAttributeDescription](https://developer.apple.com/documentation/coreimage/kciattributedescription)Added [kCIAttributeFilterAvailable_iOS](https://developer.apple.com/documentation/coreimage/kciattributefilteravailable_ios)Added [kCIAttributeFilterAvailable_Mac](https://developer.apple.com/documentation/coreimage/kciattributefilteravailable_mac)Added [kCIAttributeReferenceDocumentation](https://developer.apple.com/documentation/coreimage/kciattributereferencedocumentation)Added [kCIAttributeTypeGradient](https://developer.apple.com/documentation/coreimage/kciattributetypegradient)Added [kCIAttributeTypeOpaqueColor](https://developer.apple.com/documentation/coreimage/kciattributetypeopaquecolor)Added [kCICategoryFilterGenerator](https://developer.apple.com/documentation/coreimage/kcicategoryfiltergenerator)Added [kCIInputBiasKey](https://developer.apple.com/documentation/coreimage/kciinputbiaskey)Added [kCIInputGradientImageKey](https://developer.apple.com/documentation/coreimage/kciinputgradientimagekey)Added [kCIInputRefractionKey](https://developer.apple.com/documentation/coreimage/kciinputrefractionkey)Added [kCIInputShadingImageKey](https://developer.apple.com/documentation/coreimage/kciinputshadingimagekey)Added [kCIInputWeightsKey](https://developer.apple.com/documentation/coreimage/kciinputweightskey)Added [kCIUIParameterSet](https://developer.apple.com/documentation/coreimage/kciuiparameterset)Added [kCIUISetAdvanced](https://developer.apple.com/documentation/coreimage/kciuisetadvanced)Added [kCIUISetBasic](https://developer.apple.com/documentation/coreimage/kciuisetbasic)Added [kCIUISetDevelopment](https://developer.apple.com/documentation/coreimage/kciuisetdevelopment)Added [kCIUISetIntermediate](https://developer.apple.com/documentation/coreimage/kciuisetintermediate)Modified [CIFilter](https://developer.apple.com/documentation/coreimage/cifilter)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [CIFilter.attributes](https://developer.apple.com/documentation/coreimage/cifilter/1437661-attributes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)attributes ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSDictionary<NSString *,id> *attributes ``` |

Modified [+[CIFilter filterArrayFromSerializedXMP:inputImageExtent:error:]](https://developer.apple.com/documentation/coreimage/cifilter/1438237-filterarray)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)filterArrayFromSerializedXMP:(NSData *)xmpData inputImageExtent:(CGRect)extent error:(NSError **)outError ``` |
| To | ``` + (NSArray<CIFilter *> * _Nonnull)filterArrayFromSerializedXMP:(NSData * _Nonnull)xmpData inputImageExtent:(CGRect)extent error:(NSError * _Nullable * _Nullable)outError ``` |

Modified [+[CIFilter filterNamesInCategories:]](https://developer.apple.com/documentation/coreimage/cifilter/1437595-filternamesincategories)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)filterNamesInCategories:(NSArray *)categories ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)filterNamesInCategories:(NSArray<NSString *> * _Nullable)categories ``` |

Modified [+[CIFilter filterNamesInCategory:]](https://developer.apple.com/documentation/coreimage/cifilter/1438145-filternames)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)filterNamesInCategory:(NSString *)category ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)filterNamesInCategory:(NSString * _Nullable)category ``` |

Modified [+[CIFilter filterWithName:withInputParameters:]](https://developer.apple.com/documentation/coreimage/cifilter/1437894-init)

|  | Declaration |
| --- | --- |
| From | ``` + (CIFilter *)filterWithName:(NSString *)name withInputParameters:(NSDictionary *)params ``` |
| To | ``` + (CIFilter * _Nullable)filterWithName:(NSString * _Nonnull)name withInputParameters:(NSDictionary<NSString *,id> * _Nullable)params ``` |

Modified [CIFilter.inputKeys](https://developer.apple.com/documentation/coreimage/cifilter/1438013-inputkeys)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)inputKeys ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *inputKeys ``` |

Modified [CIFilter.name](https://developer.apple.com/documentation/coreimage/cifilter/1437997-setname)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)name ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *name ``` |

Modified [CIFilter.outputKeys](https://developer.apple.com/documentation/coreimage/cifilter/1438122-outputkeys)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)outputKeys ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *outputKeys ``` |

Modified [+[CIFilter serializedXMPFromFilters:inputImageExtent:]](https://developer.apple.com/documentation/coreimage/cifilter/1438006-serializedxmp)

|  | Declaration |
| --- | --- |
| From | ``` + (NSData *)serializedXMPFromFilters:(NSArray *)filters inputImageExtent:(CGRect)extent ``` |
| To | ``` + (NSData * _Nonnull)serializedXMPFromFilters:(NSArray<CIFilter *> * _Nonnull)filters inputImageExtent:(CGRect)extent ``` |

#### CIFilterConstructor.h (Added)

Added [CIFilterConstructor](https://developer.apple.com/documentation/coreimage/cifilterconstructor)Added [-[CIFilterConstructor filterWithName:]](https://developer.apple.com/documentation/coreimage/cifilterconstructor/1438018-filterwithname)

#### CIFilterShape.h (Added)

Added [CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape)Added [CIFilterShape.extent](https://developer.apple.com/documentation/coreimage/cifiltershape/1438022-extent)Added [-[CIFilterShape initWithRect:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1437921-initwithrect)Added [-[CIFilterShape insetByX:Y:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1437987-insetbyx)Added [-[CIFilterShape intersectWith:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1437881-intersect)Added [-[CIFilterShape intersectWithRect:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1437806-intersect)Added [+[CIFilterShape shapeWithRect:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1562074-shapewithrect)Added [-[CIFilterShape transformBy:interior:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1437808-transform)Added [-[CIFilterShape unionWith:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1438227-unionwith)Added [-[CIFilterShape unionWithRect:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1437601-unionwithrect)

#### CIImage.h

Removed [-[CIImage autoAdjustmentFilters]](https://developer.apple.com/documentation/coreimage/ciimage/1645889-autoadjustmentfilters)Added [CIImage.colorSpace](https://developer.apple.com/documentation/coreimage/ciimage/1437750-colorspace)Added [+[CIImage imageWithCVImageBuffer:]](https://developer.apple.com/documentation/coreimage/ciimage/1547007-imagewithcvimagebuffer)Added [+[CIImage imageWithCVImageBuffer:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1547028-imagewithcvimagebuffer)Added [+[CIImage imageWithMTLTexture:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1546999-imagewithmtltexture)Added [-[CIImage initWithCVImageBuffer:]](https://developer.apple.com/documentation/coreimage/ciimage/1438012-initwithcvimagebuffer)Added [-[CIImage initWithCVImageBuffer:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437617-initwithcvimagebuffer)Added [-[CIImage initWithMTLTexture:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437890-init)Added [CIImage.url](https://developer.apple.com/documentation/coreimage/ciimage/1438195-url)Added #def CI_ARRAYAdded #def CI_DICTIONARYAdded [kCIFormatA16](https://developer.apple.com/documentation/coreimage/kciformata16)Added [kCIFormatA8](https://developer.apple.com/documentation/coreimage/ciformat/1438141-a8)Added [kCIFormatABGR8](https://developer.apple.com/documentation/coreimage/kciformatabgr8)Added [kCIFormatAf](https://developer.apple.com/documentation/coreimage/kciformataf)Added [kCIFormatAh](https://developer.apple.com/documentation/coreimage/ciformat/1438161-ah)Added [kCIFormatR16](https://developer.apple.com/documentation/coreimage/kciformatr16)Added [kCIFormatR8](https://developer.apple.com/documentation/coreimage/kciformatr8)Added [kCIFormatRf](https://developer.apple.com/documentation/coreimage/kciformatrf)Added [kCIFormatRG16](https://developer.apple.com/documentation/coreimage/ciformat/1437648-rg16)Added [kCIFormatRG8](https://developer.apple.com/documentation/coreimage/kciformatrg8)Added [kCIFormatRGf](https://developer.apple.com/documentation/coreimage/kciformatrgf)Added [kCIFormatRGh](https://developer.apple.com/documentation/coreimage/kciformatrgh)Added [kCIFormatRh](https://developer.apple.com/documentation/coreimage/kciformatrh)Modified [CIImage](https://developer.apple.com/documentation/coreimage/ciimage)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [-[CIImage autoAdjustmentFiltersWithOptions:]](https://developer.apple.com/documentation/coreimage/ciimage/1437792-autoadjustmentfilters)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)autoAdjustmentFiltersWithOptions:(NSDictionary *)dict ``` |
| To | ``` - (NSArray<CIFilter *> * _Nonnull)autoAdjustmentFiltersWithOptions:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [CIImage.extent](https://developer.apple.com/documentation/coreimage/ciimage/1437996-extent)

|  | Declaration |
| --- | --- |
| From | ``` - (CGRect)extent ``` |
| To | ``` @property(readonly, nonatomic) CGRect extent ``` |

Modified [-[CIImage imageByApplyingFilter:withInputParameters:]](https://developer.apple.com/documentation/coreimage/ciimage/1437589-applyingfilter)

|  | Declaration |
| --- | --- |
| From | ``` - (CIImage *)imageByApplyingFilter:(NSString *)filterName withInputParameters:(NSDictionary *)params ``` |
| To | ``` - (CIImage * _Nonnull)imageByApplyingFilter:(NSString * _Nonnull)filterName withInputParameters:(NSDictionary<NSString *,id> * _Nullable)params ``` |

Modified [-[CIImage imageByCroppingToRect:]](https://developer.apple.com/documentation/coreimage/ciimage/1437833-imagebycroppingtorect)

|  | Declaration |
| --- | --- |
| From | ``` - (CIImage *)imageByCroppingToRect:(CGRect)r ``` |
| To | ``` - (CIImage * _Nonnull)imageByCroppingToRect:(CGRect)rect ``` |

Modified [+[CIImage imageWithBitmapData:bytesPerRow:size:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimage/1547023-imagewithbitmapdata)

|  | Declaration |
| --- | --- |
| From | ``` + (CIImage *)imageWithBitmapData:(NSData *)d bytesPerRow:(size_t)bpr size:(CGSize)size format:(CIFormat)f colorSpace:(CGColorSpaceRef)cs ``` |
| To | ``` + (CIImage * _Nonnull)imageWithBitmapData:(NSData * _Nonnull)data bytesPerRow:(size_t)bytesPerRow size:(CGSize)size format:(CIFormat)format colorSpace:(CGColorSpaceRef _Nullable)colorSpace ``` |

Modified [+[CIImage imageWithCGImage:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1547021-imagewithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` + (CIImage *)imageWithCGImage:(CGImageRef)image options:(NSDictionary *)d ``` |
| To | ``` + (CIImage * _Nonnull)imageWithCGImage:(CGImageRef _Nonnull)image options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [+[CIImage imageWithContentsOfURL:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1546997-imagewithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` + (CIImage *)imageWithContentsOfURL:(NSURL *)url options:(NSDictionary *)d ``` |
| To | ``` + (CIImage * _Nullable)imageWithContentsOfURL:(NSURL * _Nonnull)url options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [+[CIImage imageWithCVPixelBuffer:]](https://developer.apple.com/documentation/coreimage/ciimage/1547005-imagewithcvpixelbuffer)

|  | Declaration |
| --- | --- |
| From | ``` + (CIImage *)imageWithCVPixelBuffer:(CVPixelBufferRef)buffer ``` |
| To | ``` + (CIImage * _Nonnull)imageWithCVPixelBuffer:(CVPixelBufferRef _Nonnull)pixelBuffer ``` |

Modified [+[CIImage imageWithCVPixelBuffer:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1547003-imagewithcvpixelbuffer)

|  | Declaration |
| --- | --- |
| From | ``` + (CIImage *)imageWithCVPixelBuffer:(CVPixelBufferRef)buffer options:(NSDictionary *)dict ``` |
| To | ``` + (CIImage * _Nonnull)imageWithCVPixelBuffer:(CVPixelBufferRef _Nonnull)pixelBuffer options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [+[CIImage imageWithData:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1547016-imagewithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (CIImage *)imageWithData:(NSData *)data options:(NSDictionary *)d ``` |
| To | ``` + (CIImage * _Nullable)imageWithData:(NSData * _Nonnull)data options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [+[CIImage imageWithTexture:size:flipped:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimage/1547006-imagewithtexture)

|  | Declaration |
| --- | --- |
| From | ``` + (CIImage *)imageWithTexture:(unsigned int)name size:(CGSize)size flipped:(BOOL)flag colorSpace:(CGColorSpaceRef)cs ``` |
| To | ``` + (CIImage * _Nonnull)imageWithTexture:(unsigned int)name size:(CGSize)size flipped:(BOOL)flipped colorSpace:(CGColorSpaceRef _Nullable)colorSpace ``` |

Modified [-[CIImage initWithBitmapData:bytesPerRow:size:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimage/1437857-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithBitmapData:(NSData *)d bytesPerRow:(size_t)bpr size:(CGSize)size format:(CIFormat)f colorSpace:(CGColorSpaceRef)c ``` |
| To | ``` - (instancetype _Nonnull)initWithBitmapData:(NSData * _Nonnull)data bytesPerRow:(size_t)bytesPerRow size:(CGSize)size format:(CIFormat)format colorSpace:(CGColorSpaceRef _Nullable)colorSpace ``` |

Modified [-[CIImage initWithCGImage:]](https://developer.apple.com/documentation/coreimage/ciimage/1437986-initwithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCGImage:(CGImageRef)image ``` |
| To | ``` - (instancetype _Nonnull)initWithCGImage:(CGImageRef _Nonnull)image ``` |

Modified [-[CIImage initWithCGImage:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437764-initwithcgimage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCGImage:(CGImageRef)image options:(NSDictionary *)d ``` |
| To | ``` - (instancetype _Nonnull)initWithCGImage:(CGImageRef _Nonnull)image options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[CIImage initWithColor:]](https://developer.apple.com/documentation/coreimage/ciimage/1437947-initwithcolor)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithColor:(CIColor *)color ``` |
| To | ``` - (instancetype _Nonnull)initWithColor:(CIColor * _Nonnull)color ``` |

Modified [-[CIImage initWithContentsOfURL:]](https://developer.apple.com/documentation/coreimage/ciimage/1437908-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url ``` |
| To | ``` - (instancetype _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)url ``` |

Modified [-[CIImage initWithContentsOfURL:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437867-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url options:(NSDictionary *)d ``` |
| To | ``` - (instancetype _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)url options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[CIImage initWithCVPixelBuffer:]](https://developer.apple.com/documentation/coreimage/ciimage/1438072-initwithcvpixelbuffer)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCVPixelBuffer:(CVPixelBufferRef)buffer ``` |
| To | ``` - (instancetype _Nonnull)initWithCVPixelBuffer:(CVPixelBufferRef _Nonnull)pixelBuffer ``` |

Modified [-[CIImage initWithCVPixelBuffer:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1438209-initwithcvpixelbuffer)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCVPixelBuffer:(CVPixelBufferRef)buffer options:(NSDictionary *)dict ``` |
| To | ``` - (instancetype _Nonnull)initWithCVPixelBuffer:(CVPixelBufferRef _Nonnull)pixelBuffer options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[CIImage initWithData:]](https://developer.apple.com/documentation/coreimage/ciimage/1437925-initwithdata)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data ``` |
| To | ``` - (instancetype _Nullable)initWithData:(NSData * _Nonnull)data ``` |

Modified [-[CIImage initWithData:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1438032-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data options:(NSDictionary *)d ``` |
| To | ``` - (instancetype _Nullable)initWithData:(NSData * _Nonnull)data options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[CIImage initWithTexture:size:flipped:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimage/1438015-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTexture:(unsigned int)name size:(CGSize)size flipped:(BOOL)flag colorSpace:(CGColorSpaceRef)cs ``` |
| To | ``` - (instancetype _Nonnull)initWithTexture:(unsigned int)name size:(CGSize)size flipped:(BOOL)flipped colorSpace:(CGColorSpaceRef _Nullable)colorSpace ``` |

Modified [CIImage.properties](https://developer.apple.com/documentation/coreimage/ciimage/1437733-properties)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)properties ``` |
| To | ``` @property(atomic, readonly, nonnull) NSDictionary<NSString *,id> *properties ``` |

Modified [-[CIImage regionOfInterestForImage:inRect:]](https://developer.apple.com/documentation/coreimage/ciimage/1437994-regionofinterest)

|  | Declaration |
| --- | --- |
| From | ``` - (CGRect)regionOfInterestForImage:(CIImage *)im inRect:(CGRect)r ``` |
| To | ``` - (CGRect)regionOfInterestForImage:(CIImage * _Nonnull)image inRect:(CGRect)rect ``` |

#### CIImageAccumulator.h (Added)

Added [CIImageAccumulator](https://developer.apple.com/documentation/coreimage/ciimageaccumulator)Added [-[CIImageAccumulator clear]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427720-clear)Added [CIImageAccumulator.extent](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427714-extent)Added [CIImageAccumulator.format](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427716-format)Added [-[CIImageAccumulator image]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427704-image)Added [+[CIImageAccumulator imageAccumulatorWithExtent:format:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427722-imageaccumulatorwithextent)Added [+[CIImageAccumulator imageAccumulatorWithExtent:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427712-imageaccumulatorwithextent)Added [-[CIImageAccumulator initWithExtent:format:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427718-init)Added [-[CIImageAccumulator initWithExtent:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427710-init)Added [-[CIImageAccumulator setImage:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427702-setimage)Added [-[CIImageAccumulator setImage:dirtyRect:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427706-setimage)

#### CIImageProvider.h (Added)

Added [+[CIImage imageWithImageProvider:size::format:colorSpace:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1579115-imagewithimageprovider)Added [-[CIImage initWithImageProvider:size::format:colorSpace:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437868-init)Added [-[NSObject provideImageData:bytesPerRow:origin::size::userInfo:]](https://developer.apple.com/documentation/objectivec/nsobject/1438175-provideimagedata)Added #def CI_ARRAYAdded #def CI_DICTIONARYAdded CIImage(CIImageProvider)Added [kCIImageProviderTileSize](https://developer.apple.com/documentation/coreimage/kciimageprovidertilesize)Added [kCIImageProviderUserInfo](https://developer.apple.com/documentation/coreimage/kciimageprovideruserinfo)Added NSObject(CIImageProvider)

#### CIKernel.h

Added [+[CIColorKernel kernelWithString:]](https://developer.apple.com/documentation/coreimage/cicolorkernel/1438143-init)Added [-[CIKernel setROISelector:]](https://developer.apple.com/documentation/coreimage/cikernel/1437691-setroiselector)Added [+[CIWarpKernel kernelWithString:]](https://developer.apple.com/documentation/coreimage/ciwarpkernel/1438278-init)Added #def CI_ARRAYAdded #def CI_DICTIONARYModified [-[CIColorKernel applyWithExtent:arguments:]](https://developer.apple.com/documentation/coreimage/cicolorkernel/1438110-applywithextent)

|  | Declaration |
| --- | --- |
| From | ``` - (CIImage *)applyWithExtent:(CGRect)extent arguments:(NSArray *)args ``` |
| To | ``` - (CIImage * _Nullable)applyWithExtent:(CGRect)extent arguments:(NSArray<id> * _Nullable)args ``` |

Modified [-[CIKernel applyWithExtent:roiCallback:arguments:]](https://developer.apple.com/documentation/coreimage/cikernel/1438243-applywithextent)

|  | Declaration |
| --- | --- |
| From | ``` - (CIImage *)applyWithExtent:(CGRect)extent roiCallback:(CIKernelROICallback)callback arguments:(NSArray *)args ``` |
| To | ``` - (CIImage * _Nullable)applyWithExtent:(CGRect)extent roiCallback:(CIKernelROICallback _Nonnull)callback arguments:(NSArray<id> * _Nullable)args ``` |

Modified [+[CIKernel kernelsWithString:]](https://developer.apple.com/documentation/coreimage/cikernel/1437876-kernelswithstring)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)kernelsWithString:(NSString *)s ``` |
| To | ``` + (NSArray<CIKernel *> * _Nullable)kernelsWithString:(NSString * _Nonnull)string ``` |

Modified [CIKernel.name](https://developer.apple.com/documentation/coreimage/cikernel/1438067-name)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)name ``` |
| To | ``` @property(atomic, readonly, nonnull) NSString *name ``` |

Modified [-[CIWarpKernel applyWithExtent:roiCallback:inputImage:arguments:]](https://developer.apple.com/documentation/coreimage/ciwarpkernel/1437798-apply)

|  | Declaration |
| --- | --- |
| From | ``` - (CIImage *)applyWithExtent:(CGRect)extent roiCallback:(CIKernelROICallback)callback inputImage:(CIImage *)image arguments:(NSArray *)args ``` |
| To | ``` - (CIImage * _Nullable)applyWithExtent:(CGRect)extent roiCallback:(CIKernelROICallback _Nonnull)callback inputImage:(CIImage * _Nonnull)image arguments:(NSArray<id> * _Nullable)args ``` |

#### CISampler.h (Added)

Added [CISampler](https://developer.apple.com/documentation/coreimage/cisampler)Added [CISampler.definition](https://developer.apple.com/documentation/coreimage/cisampler/1437877-definition)Added [CISampler.extent](https://developer.apple.com/documentation/coreimage/cisampler/1437872-extent)Added [-[CISampler initWithImage:]](https://developer.apple.com/documentation/coreimage/cisampler/1438117-initwithimage)Added [-[CISampler initWithImage:keysAndValues:]](https://developer.apple.com/documentation/coreimage/cisampler/1555077-initwithimage)Added [-[CISampler initWithImage:options:]](https://developer.apple.com/documentation/coreimage/cisampler/1437963-init)Added [+[CISampler samplerWithImage:]](https://developer.apple.com/documentation/coreimage/cisampler/1555075-samplerwithimage)Added [+[CISampler samplerWithImage:keysAndValues:]](https://developer.apple.com/documentation/coreimage/cisampler/1555078-samplerwithimage)Added [+[CISampler samplerWithImage:options:]](https://developer.apple.com/documentation/coreimage/cisampler/1555076-samplerwithimage)Added [kCISamplerAffineMatrix](https://developer.apple.com/documentation/coreimage/kcisampleraffinematrix)Added [kCISamplerColorSpace](https://developer.apple.com/documentation/coreimage/kcisamplercolorspace)Added [kCISamplerFilterLinear](https://developer.apple.com/documentation/coreimage/kcisamplerfilterlinear)Added [kCISamplerFilterMode](https://developer.apple.com/documentation/coreimage/kcisamplerfiltermode)Added [kCISamplerFilterNearest](https://developer.apple.com/documentation/coreimage/kcisamplerfilternearest)Added [kCISamplerWrapBlack](https://developer.apple.com/documentation/coreimage/kcisamplerwrapblack)Added [kCISamplerWrapClamp](https://developer.apple.com/documentation/coreimage/kcisamplerwrapclamp)Added [kCISamplerWrapMode](https://developer.apple.com/documentation/coreimage/kcisamplerwrapmode)

#### CIVector.h

Modified [CIVector](https://developer.apple.com/documentation/coreimage/civector)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | NSCopying, NSSecureCoding |

Modified [CIVector.CGAffineTransformValue](https://developer.apple.com/documentation/coreimage/civector/1438249-cgaffinetransformvalue)

|  | Declaration |
| --- | --- |
| From | ``` - (CGAffineTransform)CGAffineTransformValue ``` |
| To | ``` @property(readonly) CGAffineTransform CGAffineTransformValue ``` |

Modified [CIVector.CGPointValue](https://developer.apple.com/documentation/coreimage/civector/1437672-cgpointvalue)

|  | Declaration |
| --- | --- |
| From | ``` - (CGPoint)CGPointValue ``` |
| To | ``` @property(readonly) CGPoint CGPointValue ``` |

Modified [CIVector.CGRectValue](https://developer.apple.com/documentation/coreimage/civector/1438108-cgrectvalue)

|  | Declaration |
| --- | --- |
| From | ``` - (CGRect)CGRectValue ``` |
| To | ``` @property(readonly) CGRect CGRectValue ``` |

Modified [CIVector.count](https://developer.apple.com/documentation/coreimage/civector/1438197-count)

|  | Declaration |
| --- | --- |
| From | ``` - (size_t)count ``` |
| To | ``` @property(readonly) size_t count ``` |

Modified [-[CIVector initWithCGAffineTransform:]](https://developer.apple.com/documentation/coreimage/civector/1438102-initwithcgaffinetransform)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCGAffineTransform:(CGAffineTransform)r ``` |
| To | ``` - (instancetype _Nonnull)initWithCGAffineTransform:(CGAffineTransform)r ``` |

Modified [-[CIVector initWithCGPoint:]](https://developer.apple.com/documentation/coreimage/civector/1438133-initwithcgpoint)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCGPoint:(CGPoint)p ``` |
| To | ``` - (instancetype _Nonnull)initWithCGPoint:(CGPoint)p ``` |

Modified [-[CIVector initWithCGRect:]](https://developer.apple.com/documentation/coreimage/civector/1437644-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCGRect:(CGRect)r ``` |
| To | ``` - (instancetype _Nonnull)initWithCGRect:(CGRect)r ``` |

Modified [-[CIVector initWithString:]](https://developer.apple.com/documentation/coreimage/civector/1437938-initwithstring)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithString:(NSString *)representation ``` |
| To | ``` - (instancetype _Nonnull)initWithString:(NSString * _Nonnull)representation ``` |

Modified [-[CIVector initWithValues:count:]](https://developer.apple.com/documentation/coreimage/civector/1437849-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithValues:(const CGFloat *)values count:(size_t)count ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithValues:(const CGFloat * _Nonnull)values count:(size_t)count ``` | yes |

Modified [-[CIVector initWithX:]](https://developer.apple.com/documentation/coreimage/civector/1437657-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithX:(CGFloat)x ``` |
| To | ``` - (instancetype _Nonnull)initWithX:(CGFloat)x ``` |

Modified [-[CIVector initWithX:Y:]](https://developer.apple.com/documentation/coreimage/civector/1437865-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithX:(CGFloat)x Y:(CGFloat)y ``` |
| To | ``` - (instancetype _Nonnull)initWithX:(CGFloat)x Y:(CGFloat)y ``` |

Modified [-[CIVector initWithX:Y:Z:]](https://developer.apple.com/documentation/coreimage/civector/1438056-initwithx)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z ``` |
| To | ``` - (instancetype _Nonnull)initWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z ``` |

Modified [-[CIVector initWithX:Y:Z:W:]](https://developer.apple.com/documentation/coreimage/civector/1438088-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z W:(CGFloat)w ``` |
| To | ``` - (instancetype _Nonnull)initWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z W:(CGFloat)w ``` |

Modified [CIVector.stringRepresentation](https://developer.apple.com/documentation/coreimage/civector/1437752-stringrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)stringRepresentation ``` |
| To | ``` @property(readonly, nonnull) NSString *stringRepresentation ``` |

Modified [+[CIVector vectorWithCGAffineTransform:]](https://developer.apple.com/documentation/coreimage/civector/1564090-vectorwithcgaffinetransform)

|  | Declaration |
| --- | --- |
| From | ``` + (CIVector *)vectorWithCGAffineTransform:(CGAffineTransform)t ``` |
| To | ``` + (instancetype _Nonnull)vectorWithCGAffineTransform:(CGAffineTransform)t ``` |

Modified [+[CIVector vectorWithCGPoint:]](https://developer.apple.com/documentation/coreimage/civector/1564086-vectorwithcgpoint)

|  | Declaration |
| --- | --- |
| From | ``` + (CIVector *)vectorWithCGPoint:(CGPoint)p ``` |
| To | ``` + (instancetype _Nonnull)vectorWithCGPoint:(CGPoint)p ``` |

Modified [+[CIVector vectorWithCGRect:]](https://developer.apple.com/documentation/coreimage/civector/1564085-vectorwithcgrect)

|  | Declaration |
| --- | --- |
| From | ``` + (CIVector *)vectorWithCGRect:(CGRect)r ``` |
| To | ``` + (instancetype _Nonnull)vectorWithCGRect:(CGRect)r ``` |

Modified [+[CIVector vectorWithString:]](https://developer.apple.com/documentation/coreimage/civector/1564093-vectorwithstring)

|  | Declaration |
| --- | --- |
| From | ``` + (CIVector *)vectorWithString:(NSString *)representation ``` |
| To | ``` + (instancetype _Nonnull)vectorWithString:(NSString * _Nonnull)representation ``` |

Modified [+[CIVector vectorWithValues:count:]](https://developer.apple.com/documentation/coreimage/civector/1564088-vectorwithvalues)

|  | Declaration |
| --- | --- |
| From | ``` + (CIVector *)vectorWithValues:(const CGFloat *)values count:(size_t)count ``` |
| To | ``` + (instancetype _Nonnull)vectorWithValues:(const CGFloat * _Nonnull)values count:(size_t)count ``` |

Modified [+[CIVector vectorWithX:]](https://developer.apple.com/documentation/coreimage/civector/1564092-vectorwithx)

|  | Declaration |
| --- | --- |
| From | ``` + (CIVector *)vectorWithX:(CGFloat)x ``` |
| To | ``` + (instancetype _Nonnull)vectorWithX:(CGFloat)x ``` |

Modified [+[CIVector vectorWithX:Y:]](https://developer.apple.com/documentation/coreimage/civector/1564091-vectorwithx)

|  | Declaration |
| --- | --- |
| From | ``` + (CIVector *)vectorWithX:(CGFloat)x Y:(CGFloat)y ``` |
| To | ``` + (instancetype _Nonnull)vectorWithX:(CGFloat)x Y:(CGFloat)y ``` |

Modified [+[CIVector vectorWithX:Y:Z:]](https://developer.apple.com/documentation/coreimage/civector/1564089-vectorwithx)

|  | Declaration |
| --- | --- |
| From | ``` + (CIVector *)vectorWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z ``` |
| To | ``` + (instancetype _Nonnull)vectorWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z ``` |

Modified [+[CIVector vectorWithX:Y:Z:W:]](https://developer.apple.com/documentation/coreimage/civector/1564087-vectorwithx)

|  | Declaration |
| --- | --- |
| From | ``` + (CIVector *)vectorWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z W:(CGFloat)w ``` |
| To | ``` + (instancetype _Nonnull)vectorWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z W:(CGFloat)w ``` |

Modified [CIVector.W](https://developer.apple.com/documentation/coreimage/civector/1438058-w)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)W ``` |
| To | ``` @property(readonly) CGFloat W ``` |

Modified [CIVector.X](https://developer.apple.com/documentation/coreimage/civector/1437738-x)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)X ``` |
| To | ``` @property(readonly) CGFloat X ``` |

Modified [CIVector.Y](https://developer.apple.com/documentation/coreimage/civector/1437843-y)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)Y ``` |
| To | ``` @property(readonly) CGFloat Y ``` |

Modified [CIVector.Z](https://developer.apple.com/documentation/coreimage/civector/1437627-z)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)Z ``` |
| To | ``` @property(readonly) CGFloat Z ``` |

#### CoreImage.h

Added #def UNIFIED_CORE_IMAGE

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
