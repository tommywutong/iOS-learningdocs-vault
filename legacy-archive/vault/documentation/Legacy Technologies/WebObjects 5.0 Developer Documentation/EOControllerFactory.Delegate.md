---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOGenerationRef/Java/eogeneration.client/Classes/EOControllerFactory.Deleg.html
archived_at: '2026-07-15T08:13:50.586765Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration.client/Art/up.gif)](../../WebObjectsTOC.md)

# EOControllerFactory.Delegate

> **__Package:__**
> : com.webobjects.eogeneration.client

---

## Interface Description

---

Documentation for this interface is forthcoming. For information on using this interface, see the book _Getting Started with Direct to Java Client_.

## Method Types

---

> **All methods**
> : [controllerFactoryShouldActivateDefaultControllers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6ktnbxxk3deifrxi2lwmf2gkrdfmzqxk3duinxw45dsn5wgyzlsom): [controllerFactoryShouldCacheController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6ktnbxxk3deinqwg2dfinxw45dsn5wgyzls): [controllerFactoryWillEvaluateRules](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyrlwmfwhkylumvjhk3dfom): [controllerFactoryWillReturnControllerForSpecification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyutfor2xe3sdn5xhi4tpnrwgk4sgn5zfg4dfmnuwm2ldmf2gs33o): [controllerFactoryWillReturnPropertyKeysForEntityAndTaskName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyutfor2xe3sqojxxazlsor4uwzlzondg64sfnz2gs5dzifxgivdbonvu4ylnmu): [controllerFactoryWillReuseControllersForSpecificationWithMode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyutfovzwkq3pnz2he33mnrsxe42gn5zfg4dfmnuwm2ldmf2gs33ok5uxi2cnn5sgk): [controllerFactoryWillUseActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvawg5djn5xhg): [controllerFactoryWillUseSpecificationForController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5zeg33oorzg63dmmvza): [controllerFactoryWillUseSpecificationForModalDialogController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5ze233emfwei2lbnrxwoq3pnz2he33mnrsxe): [controllerFactoryWillUseSpecificationForModalDialogWithSelectByInsertingController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5ze233emfwei2lbnrxwov3jorufgzlmmvrxiqtzjfxhgzlsoruw4z2dn5xhi4tpnrwgk4q): [controllerFactoryWillUseSpecificationForModalDialogWithSelectController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5ze233emfwei2lbnrxwov3jorufgzlmmvrxiq3pnz2he33mnrsxe): [controllerFactoryWillUseSpecificationForWindowController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5zfo2lomrxxoq3pnz2he33mnrsxe): [controllerFactoryWillUseSpecificationForWindowWithInsertController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5zfo2lomrxxov3jorues3ttmvzhiq3pnz2he33mnrsxe): [controllerFactoryWillUseSpecificationForWindowWithOpenController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5zfo2lomrxxov3jorue64dfnzbw63tuojxwy3dfoi): [controllerFactoryWillUseSpecificationForWindowWithQueryController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsizqwg5dpoj4s4rdfnrswoylumuxwg33oorzg63dmmvzemyldorxxe6kxnfwgyvltmvjxazldnftgsy3boruw63sgn5zfo2lomrxxov3jorufc5lfoj4ug33oorzg63dmmvza)

## Instance Methods

---

### controllerFactoryShouldActivateDefaultControllers

`public abstract boolean controllerFactoryShouldActivateDefaultControllers(EOControllerFactory anEOControllerFactory)`

---

### controllerFactoryShouldCacheController

`public abstract boolean controllerFactoryShouldCacheController( EOControllerFactory anEOControllerFactory, com.webobjects.eoapplication.EOController anEOController)`

---

### controllerFactoryWillEvaluateRules

`public abstract NSDictionary controllerFactoryWillEvaluateRules( EOControllerFactory anEOControllerFactory, NSDictionary aNSDictionary)`

---

### controllerFactoryWillReturnControllerForSpecification

`public abstract com.webobjects.eoapplication.EOController controllerFactoryWillReturnControllerForSpecification( EOControllerFactory anEOControllerFactory, com.webobjects.eoapplication.EOController anEOController, NSDictionary aNSDictionary)`

---

### controllerFactoryWillReturnPropertyKeysForEntityAndTaskName

`public abstract NSArray controllerFactoryWillReturnPropertyKeysForEntityAndTaskName( EOControllerFactory anEOControllerFactory, NSArray aNSArray, String aString, String aString)`

---

### controllerFactoryWillReuseControllersForSpecificationWithMode

`public abstract int controllerFactoryWillReuseControllersForSpecificationWithMode( EOControllerFactory anEOControllerFactory, int anInt, NSDictionary aNSDictionary)`

---

### controllerFactoryWillUseActions

`public abstract NSArray controllerFactoryWillUseActions( EOControllerFactory anEOControllerFactory, NSArray aNSArray)`

---

### controllerFactoryWillUseSpecificationForController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForController( EOControllerFactory anEOControllerFactory, NSDictionary aNSDictionary, String aString, String aString)`

---

### controllerFactoryWillUseSpecificationForModalDialogController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForModalDialogController( EOControllerFactory anEOControllerFactory, NSDictionary aNSDictionary, String aString)`

---

### controllerFactoryWillUseSpecificationForModalDialogWithSelectByInsertingController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForModalDialogWithSelectByInsertingController( EOControllerFactory anEOControllerFactory, NSDictionary aNSDictionary, String aString)`

---

### controllerFactoryWillUseSpecificationForModalDialogWithSelectController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForModalDialogWithSelectController( EOControllerFactory anEOControllerFactory, NSDictionary aNSDictionary, String aString)`

---

### controllerFactoryWillUseSpecificationForWindowController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForWindowController( EOControllerFactory anEOControllerFactory, NSDictionary aNSDictionary, String aString)`

---

### controllerFactoryWillUseSpecificationForWindowWithInsertController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForWindowWithInsertController( EOControllerFactory anEOControllerFactory, NSDictionary aNSDictionary, String aString)`

---

### controllerFactoryWillUseSpecificationForWindowWithOpenController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForWindowWithOpenController( EOControllerFactory anEOControllerFactory, NSDictionary aNSDictionary, String aString)`

---

### controllerFactoryWillUseSpecificationForWindowWithQueryController

`public abstract NSDictionary controllerFactoryWillUseSpecificationForWindowWithQueryController( EOControllerFactory anEOControllerFactory, NSDictionary aNSDictionary, String aString)`

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration.client/Art/up.gif)](../../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
