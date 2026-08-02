---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Interfaces/EOControllerFactory.Deleg.html
archived_at: '2026-07-15T08:11:44.253259Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOGeneration Reference

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

# EOControllerFactory.Delegate

> **__Package:__**
> : com.apple.client.eogeneration

---

## Interface Description

---

Documentation for this interface
is forthcoming. For information on using this interface, see the
book _Getting Started with Direct to Java Client_.

## Method Types

---

> **All methods**
> : [controllerFactoryShouldActivateDefaultControllers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6ktnbxxk3deifrxi2lwmf2gkrdfmzqxk3duinxw45dsn5wgyzlsom)
> : [controllerFactoryShouldCacheController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6ktnbxxk3deinqwg2dfinxw45dsn5wgyzls)
> : [controllerFactoryWillEvaluateRules](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyrlwmfwhkylumvjhk3dfom)
> : [controllerFactoryWillReturnControllerForSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyutfor2xe3sdn5xhi4tpnrwgk4sgn5zfg4dfmnuwm2ldmf2gs33o)
> : [controllerFactoryWillReturnPropertyKeysForEntityAndTaskName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyutfor2xe3sqojxxazlsor4uwzlzondg64sfnz2gs5dzifxgivdbonvu4ylnmu)
> : [controllerFactoryWillReuseControllersForSpecificationWithMode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyutfovzwkq3pnz2he33mnrsxe42gn5zfg4dfmnuwm2ldmf2gs33ok5uxi2cnn5sgk)
> : [controllerFactoryWillUseActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvawg5djn5xhg)
> : [controllerFactoryWillUseSpecificationForController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5zeg33oorzg63dmmvza)
> : [controllerFactoryWillUseSpecificationForModalDialogController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5ze233emfwei2lbnrxwoq3pnz2he33mnrsxe)
> : [controllerFactoryWillUseSpecificationForModalDialogWithSelectByInsertingController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5ze233emfwei2lbnrxwov3jorufgzlmmvrxiqtzjfxhgzlsoruw4z2dn5xhi4tpnrwgk4q)
> : [controllerFactoryWillUseSpecificationForModalDialogWithSelectController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5ze233emfwei2lbnrxwov3jorufgzlmmvrxiq3pnz2he33mnrsxe)
> : [controllerFactoryWillUseSpecificationForWindowController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5zfo2lomrxxoq3pnz2he33mnrsxe)
> : [controllerFactoryWillUseSpecificationForWindowWithInsertController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5zfo2lomrxxov3jorues3ttmvzhiq3pnz2he33mnrsxe)
> : [controllerFactoryWillUseSpecificationForWindowWithOpenController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5zfo2lomrxxov3jorue64dfnzbw63tuojxwy3dfoi)
> : [controllerFactoryWillUseSpecificationForWindowWithQueryController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5zfo2lomrxxov3jorufc5lfoj4ug33oorzg63dmmvza)

## Instance Methods

---

### controllerFactoryShouldActivateDefaultControllers

`public abstract boolean controllerFactoryShouldActivateDefaultControllers(EOControllerFactory anEOControllerFactory)`

---

### controllerFactoryShouldCacheController

`public abstract boolean controllerFactoryShouldCacheController(
EOControllerFactory anEOControllerFactory,
com.apple.client.eoapplication.EOController anEOController)`

---

### controllerFactoryWillEvaluateRules

`public abstract NSDictionary controllerFactoryWillEvaluateRules(
EOControllerFactory anEOControllerFactory,
NSDictionary aNSDictionary)`

---

### controllerFactoryWillReturnControllerForSpecification

`public abstract com.apple.client.eoapplication.EOController controllerFactoryWillReturnControllerForSpecification(
EOControllerFactory anEOControllerFactory,
com.apple.client.eoapplication.EOController anEOController,
NSDictionary aNSDictionary)`

---

### controllerFactoryWillReturnPropertyKeysForEntityAndTaskName

`public abstract NSArray controllerFactoryWillReturnPropertyKeysForEntityAndTaskName(
EOControllerFactory anEOControllerFactory,
NSArray aNSArray,
String aString,
String aString)`

---

### controllerFactoryWillReuseControllersForSpecificationWithMode

`public abstract int controllerFactoryWillReuseControllersForSpecificationWithMode(
EOControllerFactory anEOControllerFactory,
int anInt,
NSDictionary aNSDictionary)`

---

### controllerFactoryWillUseActions

`public abstract NSArray controllerFactoryWillUseActions(
EOControllerFactory anEOControllerFactory,
NSArray aNSArray)`

---

### controllerFactoryWillUseSpecificationForController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForController(
EOControllerFactory anEOControllerFactory,
NSDictionary aNSDictionary,
String aString,
String aString)`

---

### controllerFactoryWillUseSpecificationForModalDialogController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForModalDialogController(
EOControllerFactory anEOControllerFactory,
NSDictionary aNSDictionary,
String aString)`

---

### controllerFactoryWillUseSpecificationForModalDialogWithSelectByInsertingController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForModalDialogWithSelectByInsertingController(
EOControllerFactory anEOControllerFactory,
NSDictionary aNSDictionary,
String aString)`

---

### controllerFactoryWillUseSpecificationForModalDialogWithSelectController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForModalDialogWithSelectController(
EOControllerFactory anEOControllerFactory,
NSDictionary aNSDictionary,
String aString)`

---

### controllerFactoryWillUseSpecificationForWindowController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForWindowController(
EOControllerFactory anEOControllerFactory,
NSDictionary aNSDictionary,
String aString)`

---

### controllerFactoryWillUseSpecificationForWindowWithInsertController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForWindowWithInsertController(
EOControllerFactory anEOControllerFactory,
NSDictionary aNSDictionary,
String aString)`

---

### controllerFactoryWillUseSpecificationForWindowWithOpenController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForWindowWithOpenController(
EOControllerFactory anEOControllerFactory,
NSDictionary aNSDictionary,
String aString)`

---

### controllerFactoryWillUseSpecificationForWindowWithQueryController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForWindowWithQueryController(
EOControllerFactory anEOControllerFactory,
NSDictionary aNSDictionary,
String aString)`

---

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

__DRAFT__
