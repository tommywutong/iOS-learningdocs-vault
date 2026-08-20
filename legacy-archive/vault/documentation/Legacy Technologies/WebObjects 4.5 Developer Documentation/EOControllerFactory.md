---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EOControllerFactory.html
archived_at: '2026-07-15T08:11:43.709776Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOGeneration Reference

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

# EOControllerFactory

> **__Inherits
> from:__**
> : Object

> **__Implements:__**
> : NSDisposable

> **__Package:__**
> : com.apple.client.eogeneration

---

## Class Description

---

Documentation for this class is forthcoming.
For information on using this class, see the book _Getting Started
with Direct to Java Client_.

## Method Types

---

> **All methods**
> : [createSharedControllerFactoryWithClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3pnz2he33mnrsxertbmn2g64tzf5rxezlborsvg2dbojswiq3pnz2he33mnrsxertbmn2g64tzk5uxi2cdnrqxg4y)
> : [sharedControllerFactory](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3pnz2he33mnrsxertbmn2g64tzf5zwqylsmvseg33oorzg63dmmvzemyldorxxe6i)
> : [actions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6yldoruw63tt)
> : [activateDefaultControllers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6yldoruxmylumvcgkztbovwhiq3pnz2he33mnrsxe4y)
> : [cachesControllers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6y3bmnugk42dn5xhi4tpnrwgk4tt)
> : [canInsertWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6y3bnzew443foj2fo2lunbcw45djor4u4ylnmu)
> : [canOpenGlobalIDsWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6y3bnzhxazloi5wg6ytbnreui42xnf2gqrlooruxi6komfwwk)
> : [canOpenModalDialogForTaskName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6y3bnzhxazlojvxwiylmiruwc3dpm5dg64sumfzwwttbnvsq)
> : [canOpenWindowForTaskName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6y3bnzhxazlok5uw4zdpo5dg64sumfzwwttbnvsq)
> : [canOpenWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6y3bnzhxazlok5uxi2cfnz2gs5dzjzqw2zi)
> : [canQueryWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6y3bnzixkzlspflws5diivxhi2lupfhgc3lf)
> : [canSelectByInsertingWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6y3bnzjwk3dfmn2ee6kjnzzwk4tunfxgov3joruek3tunf2hsttbnvsq)
> : [canSelectWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6y3bnzjwk3dfmn2fo2lunbcw45djor4u4ylnmu)
> : [controllerWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6y3pnz2he33mnrsxev3joruek3tunf2hsttbnvsq)
> : [controllerWithSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6y3pnz2he33mnrsxev3jorufg4dfmnuwm2ldmf2gs33o)
> : [defaultReuseModeForSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6zdfmzqxk3dukjsxk43fjvxwizkgn5zfg4dfmnuwm2ldmf2gs33o)
> : [delegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6zdfnrswoylumu)
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6zdjonyg643f)
> : [editorControllerWithEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6zlenf2g64sdn5xhi4tpnrwgk4sxnf2gqrlooruxi6i)
> : [evaluateRules](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6zlwmfwhkylumvjhk3dfom)
> : [expandedKeyPathsForEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6zlyobqw4zdfmrfwk6kqmf2gq42gn5zek3tunf2hsttbnvsq)
> : [expandedKeyPathsForEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6zlyobqw4zdfmrfwk6kqmf2gq42gn5zek3tunf2hsttbnvsq)
> : [formControllerWithEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s6ztpojwug33oorzg63dmmvzfo2lunbcw45djor4q)
> : [hasControllerWithSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s62dbonbw63tuojxwy3dfojlws5diknygky3jmzuwgylunfxw4)
> : [insertWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s62loonsxe5cxnf2gqrlooruxi6komfwwk)
> : [invalidateRules](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s62loozqwy2lemf2gkutvnrsxg)
> : [listControllerWithEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s63djon2eg33oorzg63dmmvzfo2lunbcw45djor4q)
> : [openGlobalIDWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s633qmvxeo3dpmjqwyskek5uxi2cfnz2gs5dzjzqw2zi)
> : [openGlobalIDsWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s633qmvxeo3dpmjqwyskeonlws5diivxhi2lupfhgc3lf)
> : [openModalDialogForTaskName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s633qmvxe233emfwei2lbnrxwortpojkgc43ljzqw2zi)
> : [openSingleWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s633qmvxfg2lom5wgkv3joruek3tunf2hsttbnvsq)
> : [openWindowForTaskName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s633qmvxfo2lomrxxortpojkgc43ljzqw2zi)
> : [openWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s633qmvxfo2lunbcw45djor4u4ylnmu)
> : [performTaskWithController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s64dfojtg64tnkrqxg22xnf2gqq3pnz2he33mnrsxe)
> : [propertyKeysForEntityAndTaskName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s64dsn5ygk4tupffwk6ltizxxerlooruxi6kbnzsfiyltnnhgc3lf)
> : [queryControllerWithEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s64lvmvzhsq3pnz2he33mnrsxev3joruek3tunf2hs)
> : [queryWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s64lvmvzhsv3joruek3tunf2hsttbnvsq)
> : [selectByInsertingWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s643fnrswg5ccpfew443foj2gs3thk5uxi2cfnz2gs5dzjzqw2zi)
> : [selectControllerWithEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s643fnrswg5cdn5xhi4tpnrwgk4sxnf2gqrlooruxi6i)
> : [selectWithEntityName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s643fnrswg5cxnf2gqrlooruxi6komfwwk)
> : [setCachesControllers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s643forbwcy3imvzug33oorzg63dmmvzhg)
> : [setDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s643forcgk3dfm5qxizi)
> : [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s65dpkn2he2lom4)

## Static Methods

---

### createSharedControllerFactoryWithClass

`public static EOControllerFactory createSharedControllerFactoryWithClass(String aString)`

---

### sharedControllerFactory

`public static EOControllerFactory sharedControllerFactory()`

---

## Instance Methods

---

### actions

`public NSArray actions()`

---

### activateDefaultControllers

`public void activateDefaultControllers()`

---

### cachesControllers

`public boolean cachesControllers()`

---

### canInsertWithEntityName

`public boolean canInsertWithEntityName(String aString)`

---

### canOpenGlobalIDsWithEntityName

`public boolean canOpenGlobalIDsWithEntityName(String aString)`

---

### canOpenModalDialogForTaskName

`public boolean canOpenModalDialogForTaskName(String aString)`

---

### canOpenWindowForTaskName

`public boolean canOpenWindowForTaskName(String aString)`

---

### canOpenWithEntityName

`public boolean canOpenWithEntityName(String aString)`

---

### canQueryWithEntityName

`public boolean canQueryWithEntityName(String aString)`

---

### canSelectByInsertingWithEntityName

`public boolean canSelectByInsertingWithEntityName(String aString)`

---

### canSelectWithEntityName

`public boolean canSelectWithEntityName(String aString)`

---

### controllerWithEntityName

`public com.apple.client.eoapplication.EOController controllerWithEntityName(
com.apple.client.eoapplication.EOController anEOController,
Class aClass,
String aString)`

---

### controllerWithSpecification

`public com.apple.client.eoapplication.EOController controllerWithSpecification(
NSDictionary aNSDictionary,
boolean aBoolean)`

---

### defaultReuseModeForSpecification

`protected int defaultReuseModeForSpecification(NSDictionary aNSDictionary)`

---

### delegate

`public Object delegate()`

---

### dispose

`public void dispose()`

---

### editorControllerWithEntity

`public com.apple.client.eoapplication.EOController editorControllerWithEntity(String aString)`

---

### evaluateRules

`public Object evaluateRules(NSDictionary aNSDictionary)`

---

### expandedKeyPathsForEntityName

`public NSArray expandedKeyPathsForEntityName(
String aString,
String aString)`

---

### expandedKeyPathsForEntityName

`public NSArray expandedKeyPathsForEntityName(
String aString,
NSArray aNSArray)`

---

### formControllerWithEntity

`public com.apple.client.eoapplication.EOController formControllerWithEntity(String aString)`

---

### hasControllerWithSpecification

`public boolean hasControllerWithSpecification(
NSDictionary aNSDictionary,
boolean aBoolean)`

---

### insertWithEntityName

`public EOControllerFactory.Insert insertWithEntityName(String aString)`

---

### invalidateRules

`public void invalidateRules()`

---

### listControllerWithEntity

`public com.apple.client.eoapplication.EOController listControllerWithEntity(String aString)`

---

### openGlobalIDWithEntityName

`public EOControllerFactory.Open openGlobalIDWithEntityName(
String aString,
com.apple.client.eocontrol.EOGlobalID anEOGlobalID)`

---

### openGlobalIDsWithEntityName

`public NSArray openGlobalIDsWithEntityName(
String aString,
NSArray aNSArray)`

---

### openModalDialogForTaskName

`public com.apple.client.eoapplication.EOController openModalDialogForTaskName(String aString)`

---

### openSingleWithEntityName

`public EOControllerFactory.Open openSingleWithEntityName(String aString)`

---

### openWindowForTaskName

`public com.apple.client.eoapplication.EOController openWindowForTaskName(String aString)`

---

### openWithEntityName

`public NSArray openWithEntityName(String aString)`

---

### performTaskWithController

`public void performTaskWithController(
com.apple.client.eoapplication.EOController anEOController,
EOControllerFactory.ControllerTaskCallback aControllerTaskCallback,
Object[] anObject[])`

---

### propertyKeysForEntityAndTaskName

`public NSArray propertyKeysForEntityAndTaskName(
String aString,
String aString)`

---

### queryControllerWithEntity

`public com.apple.client.eoapplication.EOController queryControllerWithEntity(String aString)`

---

### queryWithEntityName

`public EOControllerFactory.Query queryWithEntityName(String aString)`

---

### selectByInsertingWithEntityName

`public com.apple.client.eocontrol.EOGlobalID selectByInsertingWithEntityName(String aString)`

---

### selectControllerWithEntity

`public com.apple.client.eoapplication.EOController selectControllerWithEntity(String aString)`

---

### selectWithEntityName

`public NSArray selectWithEntityName(
String aString,
boolean aBoolean,
boolean aBoolean)`

---

### setCachesControllers

`public void setCachesControllers(boolean aBoolean)`

---

### setDelegate

`public void setDelegate(Object anObject)`

---

### toString

`public String toString()`

---

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

__DRAFT__
